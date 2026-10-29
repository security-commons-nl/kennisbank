"""Tests voor de platen bij governance/cbw-uitleggen-aan-het-mt.

    python tools/test_cbw_mt.py

Vier soorten toets:
- de gebouwde bestanden lopen niet achter op data/platen.json;
- inhoud: de tien vereisten van de zorgplicht staan er in volgorde, elk met de drie vragen van het refrein,
  de tekst volgt de schrijfregels, de pagina laadt niets van buiten en de romp noemt geen echte organisatie;
- invullen: een eigen invulblok vervangt elk invulveld, zet de stand op de platen en zet een foto in de pagina;
- meetkunde: elk label in elk beeld past binnen het beeld, in zijn eigen vlak en raakt geen ander label en geen
  waarschuwingsdriehoek. De breedte wordt gemeten met een echte letter (Segoe UI, of DejaVu Sans op Linux).
  Is er geen letter te vinden, dan slaat de toets zichtbaar over in plaats van stil te slagen.
"""
from __future__ import annotations

import base64
import importlib.util
import json
import re
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

HIER = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("bouw_cbw_mt", HIER / "bouw_cbw_mt.py")
bouw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bouw)

DATA = json.loads(bouw.DATA.read_text(encoding="utf-8"))
NS = "{http://www.w3.org/2000/svg}"
EISEN = [p for p in DATA["platen"] if p["soort"] == "eis"]

LETTERS = [
    ("Segoe UI", Path("C:/Windows/Fonts/segoeui.ttf"), Path("C:/Windows/Fonts/segoeuib.ttf")),
    ("DejaVu Sans", Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
     Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")),
]


def matplotlib_dejavu() -> list[tuple[str, Path, Path]]:
    try:
        import matplotlib  # noqa: F401
    except ImportError:
        return []
    ttf = Path(matplotlib.__file__).resolve().parent / "mpl-data" / "fonts" / "ttf"
    return [("DejaVu Sans (matplotlib)", ttf / "DejaVuSans.ttf", ttf / "DejaVuSans-Bold.ttf")]


def meetlatten() -> list[tuple[str, object]]:
    try:
        from PIL import ImageFont
    except ImportError:
        return []
    uit = []
    for naam, gewoon, vet in LETTERS + matplotlib_dejavu():
        if not (gewoon.is_file() and vet.is_file()):
            continue
        cache: dict = {}

        def breedte(s: str, maat: int, is_vet: bool, gewoon=gewoon, vet=vet, cache=cache) -> float:
            sleutel = (maat, is_vet)
            if sleutel not in cache:
                cache[sleutel] = ImageFont.truetype(str(vet if is_vet else gewoon), maat)
            return cache[sleutel].getlength(s)
        uit.append((naam, breedte))
    return uit


def labels(wortel: ET.Element) -> list[dict]:
    uit = []
    for t in wortel.iter(NS + "text"):
        uit.append({"x": float(t.get("x")), "y": float(t.get("y")), "maat": int(t.get("font-size")),
                    "vet": t.get("font-weight") == "700", "anker": t.get("text-anchor"),
                    "tekst": "".join(t.itertext())})
    return uit


def kader(label: dict, breedte) -> tuple[float, float, float, float]:
    b = breedte(label["tekst"], label["maat"], label["vet"])
    x = label["x"] - {"start": 0, "middle": b / 2, "end": b}[label["anker"]]
    return x, label["y"] - label["maat"] * 0.78, x + b, label["y"] + label["maat"] * 0.24


def raakt(a, b) -> bool:
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


class Bestanden(unittest.TestCase):
    def test_niets_loopt_achter(self):
        doelen = bouw.doelen()
        self.assertGreaterEqual(len(doelen), 17, "platen, draaiboek en vijftien beelden")
        for pad, inhoud in doelen.items():
            with self.subTest(pad=pad.name):
                self.assertTrue(pad.is_file(), f"{pad.name} ontbreekt; draai bouw_cbw_mt.py")
                self.assertEqual(pad.read_text(encoding="utf-8"), inhoud,
                                 f"{pad.name} loopt achter; draai bouw_cbw_mt.py")

    def test_svg_los_gelijk_aan_inline(self):
        pagina = (bouw.MAP / "platen.html").read_text(encoding="utf-8")
        beelden = {p["beeld"] for p in DATA["platen"] if p.get("beeld")}
        self.assertEqual(beelden, set(bouw.BEELDEN), "elk getekend beeld staat op een plaat")
        for naam in beelden:
            los = (bouw.MAP / "img" / f"{naam}.svg").read_text(encoding="utf-8").strip()
            self.assertIn(los, pagina, f"{naam}.svg wijkt af van de plaat")

    def test_readme_linkt_elk_bestand(self):
        readme = (bouw.MAP / "README.md").read_text(encoding="utf-8")
        for pad in sorted(bouw.MAP.rglob("*")):
            rel = pad.relative_to(bouw.MAP).as_posix()
            if pad.is_file() and rel not in ("README.md", "index.html", "draaiboek.html"):
                with self.subTest(bestand=rel):
                    self.assertIn(f"]({rel})", readme, f"{rel} staat niet als link in de README")


class Inhoud(unittest.TestCase):
    def test_tien_vereisten_in_volgorde(self):
        self.assertEqual([p["letter"] for p in EISEN], list("abcdefghij"))
        for p in EISEN:
            with self.subTest(eis=p["letter"]):
                for veld in ("kop", "wet", "proces", "watals", "keuze", "gepast", "beeld", "bron"):
                    self.assertTrue(str(p.get(veld, "")).strip(), f"veld {veld} ontbreekt")
                self.assertTrue(set(p["biv"]) <= set("BIV") and p["biv"], "biv is een deel van B, I en V")
                self.assertIn(f"onder {p['letter']}", p["bron"], "de bron noemt het onderdeel van artikel 21")

    def test_zorgplicht_komt_als_laatste_plicht(self):
        soorten = [p["soort"] for p in DATA["platen"]]
        eerste_eis = soorten.index("eis")
        self.assertEqual(soorten[eerste_eis - 1], "raster", "het overzicht van de tien gaat voor de tien")
        self.assertGreater(eerste_eis, [p.get("beeld") for p in DATA["platen"]].index("meldklok"),
                           "eerst de andere plichten, dan de zorgplicht")
        self.assertEqual([p["stand"] for p in DATA["platen"] if p["soort"] == "stand"],
                         ["plichten", "zorgplicht", "processen"])

    def test_refrein_op_elke_eisplaat(self):
        pagina = (bouw.MAP / "platen.html").read_text(encoding="utf-8")
        refrein = f'<p class="refrein">{bouw.e(DATA["refrein"])}</p>'
        for p in EISEN:
            blok = re.search(rf'<section class="plaat p-eis" id="eis-{p["letter"]}".*?</section>', pagina, re.S)
            with self.subTest(eis=p["letter"]):
                self.assertIsNotNone(blok, "plaat ontbreekt")
                self.assertIn(refrein, blok.group(0))
                for kop in ("Wat als", "De keuze", "Waar gepast"):
                    self.assertIn(f"<dt>{kop}</dt>", blok.group(0))

    def test_schrijfregels(self):
        tekst = bouw.DATA.read_text(encoding="utf-8") + (bouw.MAP / "README.md").read_text(encoding="utf-8")
        for teken, naam in (("\u2014", "em-dash"), ("\u2013", "en-dash")):
            self.assertNotIn(teken, tekst, f"geen {naam} in de tekst")

    def test_romp_noemt_geen_echte_organisatie(self):
        """Het sjabloon is generiek; de eigen organisatie komt alleen via het invulblok binnen."""
        tekst = "".join(p.read_text(encoding="utf-8") for p in bouw.MAP.rglob("*")
                        if p.is_file() and p.suffix in (".md", ".json", ".html", ".svg"))
        for naam in ("Leiden", "Leiderdorp", "Oegstgeest", "Zoeterwoude", "IDA", "Servicepunt71"):
            self.assertNotRegex(tekst, rf"\b{naam}\b", f"'{naam}' hoort niet in de romp")

    def test_elke_plaat_heeft_een_vaste_naam(self):
        namen = [bouw.plaat_id(p) for p in DATA["platen"]]
        self.assertEqual(len(namen), len(set(namen)), "plaatnamen zijn uniek")
        self.assertIn("tijdlijn", namen)

    def test_alleen_bekende_invulvelden(self):
        velden = set(re.findall(r"\{([a-z]+)\}", bouw.DATA.read_text(encoding="utf-8")))
        self.assertTrue(velden <= set(bouw.INVULVELDEN) | {"refrein"}, velden)
        sjabloon = json.loads(bouw.INVUL_SJABLOON.read_text(encoding="utf-8"))
        for veld in bouw.INVULVELDEN:
            self.assertIn(veld, sjabloon, f"het invulblok mist {veld}")
        self.assertEqual(sorted(sjabloon["stand"]["zorgplicht"]), list("abcdefghij"))

    def test_pagina_laadt_niets_van_buiten(self):
        pagina = (bouw.MAP / "platen.html").read_text(encoding="utf-8")
        self.assertNotRegex(pagina, r'<script[^>]+src=', "geen externe scripts")
        self.assertNotRegex(pagina, r'<link[^>]+stylesheet', "geen externe stylesheets")
        self.assertNotRegex(pagina, r'src="https?://', "geen externe bronnen")
        self.assertIn('lang="nl"', pagina)
        self.assertIn("[hidden]{display:none!important}", pagina)
        self.assertIn("@media print", pagina)
        self.assertEqual(len(re.findall(r'<section class="plaat', pagina)), len(DATA["platen"]))
        self.assertEqual(len(re.findall(r'id="t-', pagina)), len(set(re.findall(r'id="t-[a-z]+"', pagina))),
                         "elke svg heeft een eigen titel-id")

    def test_sjabloon_toont_invulvelden(self):
        pagina = (bouw.MAP / "platen.html").read_text(encoding="utf-8")
        for veld in ("[gemeente]", "[datum]", "[contact]", "[toelichting]", "[Foto: jullie gemeentehuis]"):
            self.assertIn(veld, pagina, f"{veld} hoort zichtbaar op het sjabloon")

    def test_draaiboek_heeft_elke_plaat(self):
        draaiboek = (bouw.MAP / "draaiboek.md").read_text(encoding="utf-8")
        rijen = re.findall(r"^\| (\d+) \|", draaiboek, re.M)
        self.assertEqual([int(r) for r in rijen], list(range(1, len(DATA["platen"]) + 1)))
        totaal = sum(p["minuten"] for p in DATA["platen"])
        self.assertTrue(110 <= totaal <= 125, f"een sessie van twee uur, nu {totaal} minuten")
        self.assertIn("## Antwoordlijnen", draaiboek)


class Invullen(unittest.TestCase):
    def setUp(self):
        self.map = Path(tempfile.mkdtemp())
        # een png van een pixel als foto
        png = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg==")
        (self.map / "huis.png").write_bytes(png)
        blok = json.loads(bouw.INVUL_SJABLOON.read_text(encoding="utf-8"))
        blok.update(gemeente="Voorbeeldstad", datum="1 april 2027", contact="de CISO, ciso@voorbeeld.nl")
        blok["fotos"]["gemeentehuis"] = "huis.png"
        blok["stand"]["zorgplicht"]["c"] = {"status": "rood", "tekst": "Herstel nooit getest"}
        blok["stand"]["plichten"]["registratie"] = {"status": "groen", "tekst": "Geregistreerd in augustus"}
        blok["aanvullingen"] = {"tijdlijn": "Samen met de buurgemeenten", "stand-processen": ["Eigen regel"]}
        (self.map / "blok.json").write_text(json.dumps(blok), encoding="utf-8")
        self.uit = self.map / "eigen.html"
        self.assertEqual(bouw.main(["--invul", str(self.map / "blok.json"), "--uit", str(self.uit)]), 0)
        self.pagina = self.uit.read_text(encoding="utf-8")

    def test_velden_ingevuld(self):
        self.assertIn("De Cyberbeveiligingswet in Voorbeeldstad", self.pagina)
        self.assertIn("1 april 2027", self.pagina)
        for veld in ("[gemeente]", "[datum]", "[contact]", "[Foto: jullie gemeentehuis]"):
            self.assertNotIn(veld, self.pagina)
        self.assertIn("<title>De Cyberbeveiligingswet uitgelegd aan het MT - Voorbeeldstad</title>", self.pagina)

    def test_stand_en_foto(self):
        self.assertRegex(self.pagina, r'stip rood.*?c\. Doordraaien en herstellen.*?Herstel nooit getest')
        self.assertRegex(self.pagina, r'stip groen.*?Geregistreerd in augustus')
        self.assertIn('src="data:image/png;base64,', self.pagina)
        self.assertIn("[Foto: een eigen kritiek proces]", self.pagina, "een lege foto blijft een invulveld")

    def test_aanvulling_in_groen_op_de_juiste_plaat(self):
        tijdlijn = re.search(r'<section class="plaat p-beeld" id="plaat-6".*?</section>', self.pagina, re.S).group(0)
        self.assertIn('<li class="lokaal">Samen met de buurgemeenten</li>', tijdlijn)
        processen = re.search(r'<section class="plaat p-stand" id="plaat-24".*?</section>', self.pagina, re.S).group(0)
        self.assertIn('<p class="lokaal">Eigen regel</p>', processen)
        self.assertEqual(self.pagina.count('class="lokaal"'), 2, "alleen waar gevraagd")

    def test_onbekende_plaat_is_een_fout(self):
        with self.assertRaises(ValueError):
            bouw.aanvullingen({"aanvullingen": {"bestaat-niet": "x"}}, DATA)

    def test_sjabloon_niet_aangeraakt(self):
        self.assertNotIn("Voorbeeldstad", (bouw.MAP / "platen.html").read_text(encoding="utf-8"))


class Meetkunde(unittest.TestCase):
    MARGE = 8

    def setUp(self):
        self.letters = meetlatten()
        if not self.letters:
            self.skipTest("geen letter of geen Pillow gevonden; meetkunde niet getoetst")

    def per_letter(self):
        for letter, breedte in self.letters:
            for naam, maak in bouw.BEELDEN.items():
                yield letter, breedte, naam, ET.fromstring(maak())

    def test_labels_binnen_het_beeld(self):
        for letter, breedte, naam, wortel in self.per_letter():
            ls = labels(wortel)
            self.assertGreater(len(ls), 0, f"{naam} heeft geen tekst")
            for label in ls:
                x1, y1, x2, y2 = kader(label, breedte)
                with self.subTest(letter=letter, beeld=naam, label=label["tekst"]):
                    self.assertGreaterEqual(x1, self.MARGE)
                    self.assertLessEqual(x2, bouw.B - self.MARGE)
                    self.assertGreaterEqual(y1, self.MARGE)
                    self.assertLessEqual(y2, bouw.H - self.MARGE)

    def test_labels_raken_elkaar_niet(self):
        for letter, breedte, naam, wortel in self.per_letter():
            ls = [(lab["tekst"], kader(lab, breedte)) for lab in labels(wortel)]
            for i, (ta, a) in enumerate(ls):
                for tb, b in ls[i + 1:]:
                    with self.subTest(letter=letter, beeld=naam, a=ta, b=tb):
                        self.assertFalse(raakt(a, b), f"'{ta}' en '{tb}' overlappen in {naam}")

    def test_waarschuwing_raakt_geen_label(self):
        aantal = 0
        for letter, breedte, naam, wortel in self.per_letter():
            for g in wortel.iter(NS + "g"):
                if g.get("data-gevaar") is None:
                    continue
                aantal += 1
                vak = tuple(float(v) for v in g.get("data-gevaar").split())
                for lab in labels(wortel):
                    with self.subTest(letter=letter, beeld=naam, label=lab["tekst"]):
                        self.assertFalse(raakt(vak, kader(lab, breedte)),
                                         f"een waarschuwing ligt over '{lab['tekst']}' in {naam}")
        self.assertGreaterEqual(aantal, 11 * len(self.letters), "elk vereiste heeft minstens een waarschuwing")

    def test_geen_lijn_door_een_label(self):
        for letter, breedte, naam, wortel in self.per_letter():
            kaders = [(lab["tekst"], kader(lab, breedte)) for lab in labels(wortel)]
            for ln in wortel.iter(NS + "line"):
                x1, y1, x2, y2 = (float(ln.get(k)) for k in ("x1", "y1", "x2", "y2"))
                for tekst_, (a, b, c, d) in kaders:
                    geraakt = any(a + 1 < x1 + (x2 - x1) * i / 200 < c - 1 and
                                  b + 1 < y1 + (y2 - y1) * i / 200 < d - 1 for i in range(201))
                    with self.subTest(letter=letter, beeld=naam, label=tekst_):
                        self.assertFalse(geraakt, f"een lijn loopt door '{tekst_}' in {naam}")

    def test_tekst_in_vlak_past_in_het_vlak(self):
        """Een label waarvan het midden in een vlak valt, moet er met wat lucht in passen."""
        gecontroleerd = 0
        for letter, breedte, naam, wortel in self.per_letter():
            vlakken = []
            for r in wortel.iter(NS + "rect"):
                b_, h_ = float(r.get("width")), float(r.get("height"))
                if r.get("fill") == bouw.DONKER and r.get("data-label") is None:
                    continue
                if r.get("data-label") is not None or (h_ >= 30 and b_ < 700):
                    vlakken.append((float(r.get("x")), float(r.get("y")), b_, h_))
            for label in labels(wortel):
                x1, y1, x2, y2 = kader(label, breedte)
                mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                for rx, ry, rb, rh in vlakken:
                    if rx < mx < rx + rb and ry < my < ry + rh:
                        gecontroleerd += 1
                        with self.subTest(letter=letter, beeld=naam, label=label["tekst"]):
                            self.assertGreaterEqual(x1, rx + 4, "label steekt links uit zijn vlak")
                            self.assertLessEqual(x2, rx + rb - 4, "label steekt rechts uit zijn vlak")
        self.assertGreater(gecontroleerd, 40, "de toets moet echt labels in vlakken vinden")


if __name__ == "__main__":
    unittest.main(verbosity=1)
