"""Tests voor de platensets bij governance/quantumveilig-per-laag.

    python tools/test_quantumplaten.py

Drie soorten toets:
- de gebouwde bestanden lopen niet achter op data/platen.json;
- inhoud: elke plaat heeft een kop, feiten en een bron, de tekst volgt de schrijfregels, de pagina laadt
  niets van buiten;
- meetkunde: elk label in elk beeld past binnen het beeld en raakt geen ander label. De breedte wordt gemeten
  met een echte letter (Segoe UI, of DejaVu Sans op Linux). Is er geen letter te vinden, dan slaat de toets
  zichtbaar over in plaats van stil te slagen.
"""
from __future__ import annotations

import importlib.util
import json
import re
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

HIER = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("bouw", HIER / "bouw_quantumplaten.py")
bouw = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bouw)

DATA = json.loads(bouw.DATA.read_text(encoding="utf-8"))
NS = "{http://www.w3.org/2000/svg}"

LETTERS = [
    (Path("C:/Windows/Fonts/segoeui.ttf"), Path("C:/Windows/Fonts/segoeuib.ttf")),
    (Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
     Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf")),
]


def meetlat():
    try:
        from PIL import ImageFont
    except ImportError:
        return None
    for gewoon, vet in LETTERS:
        if gewoon.is_file() and vet.is_file():
            cache: dict = {}

            def breedte(s: str, maat: int, is_vet: bool) -> float:
                sleutel = (maat, is_vet)
                if sleutel not in cache:
                    cache[sleutel] = ImageFont.truetype(str(vet if is_vet else gewoon), maat)
                return cache[sleutel].getlength(s)
            return breedte
    return None


def labels(svg_tekst: str) -> list[dict]:
    wortel = ET.fromstring(svg_tekst)
    uit = []
    for t in wortel.iter(NS + "text"):
        uit.append({"x": float(t.get("x")), "y": float(t.get("y")), "maat": int(t.get("font-size")),
                    "vet": t.get("font-weight") == "700", "anker": t.get("text-anchor"),
                    "tekst": "".join(t.itertext())})
    return uit


def kader(label: dict, breedte) -> tuple[float, float, float, float]:
    b = breedte(label["tekst"], label["maat"], label["vet"])
    x = label["x"] - {"start": 0, "middle": b / 2, "end": b}[label["anker"]]
    # boven de basislijn de hoogte van een hoofdletter met marge, eronder de staarten
    return x, label["y"] - label["maat"] * 0.78, x + b, label["y"] + label["maat"] * 0.24


class Bestanden(unittest.TestCase):
    def test_niets_loopt_achter(self):
        for pad, inhoud in bouw.doelen().items():
            with self.subTest(pad=pad.name):
                self.assertTrue(pad.is_file(), f"{pad.name} ontbreekt; draai bouw_quantumplaten.py")
                self.assertEqual(pad.read_text(encoding="utf-8"), inhoud,
                                 f"{pad.name} loopt achter; draai bouw_quantumplaten.py")

    def test_svg_los_gelijk_aan_inline(self):
        for deck in DATA["decks"]:
            html = (bouw.MAP / f"platen-{deck['id']}.html").read_text(encoding="utf-8")
            for p in deck["platen"]:
                if p["soort"] == "beeld":
                    los = (bouw.MAP / "img" / f"{p['beeld']}.svg").read_text(encoding="utf-8").strip()
                    self.assertIn(los, html, f"{p['beeld']}.svg wijkt af van de plaat in {deck['id']}")


class Inhoud(unittest.TestCase):
    def test_vijf_gremia_elk_met_beeld_en_vraag(self):
        ids = [d["id"] for d in DATA["decks"]]
        self.assertEqual(ids, ["bestuur", "directie", "ciso-privacy", "it", "inkoop"])
        for deck in DATA["decks"]:
            soorten = [p["soort"] for p in deck["platen"]]
            with self.subTest(deck=deck["id"]):
                self.assertEqual(soorten[0], "beeld", "elke set opent met een beeld")
                self.assertEqual(soorten.count("beeld"), 1, "precies een beeldplaat per set")
                self.assertIn("vraag", soorten, "elke set zegt wat er van dit gremium gevraagd wordt")
                self.assertTrue(5 <= len(deck["platen"]) <= 8, "zes tot acht platen houdt het kort")

    def test_elke_plaat_compleet(self):
        for deck in DATA["decks"]:
            for i, p in enumerate(deck["platen"], 1):
                with self.subTest(deck=deck["id"], plaat=i):
                    self.assertIn(p["soort"], ("beeld", "zin", "vraag"))
                    self.assertTrue(p["kop"].strip())
                    self.assertTrue(p["bron"].strip(), "elke plaat noemt zijn bron")
                    self.assertTrue(1 <= len(p["onthul"]) <= 3, "een tot drie feiten per plaat")
                    if p["soort"] == "beeld":
                        self.assertIn(p["beeld"], bouw.BEELDEN)

    def test_schrijfregels(self):
        tekst = bouw.DATA.read_text(encoding="utf-8") + (bouw.MAP / "README.md").read_text(encoding="utf-8")
        for teken, naam in (("\u2014", "em-dash"), ("\u2013", "en-dash")):
            self.assertNotIn(teken, tekst, f"geen {naam} in de tekst")

    def test_2030_is_het_jaar(self):
        """De platen houden een jaar aan voor 'op straat': 2030, het advies van de AIVD."""
        bestuur = DATA["decks"][0]["platen"][0]
        self.assertIn("2030", bestuur["kop"])

    def test_pagina_laadt_niets_van_buiten(self):
        for deck in DATA["decks"]:
            html = (bouw.MAP / f"platen-{deck['id']}.html").read_text(encoding="utf-8")
            with self.subTest(deck=deck["id"]):
                self.assertNotRegex(html, r'<script[^>]+src=', "geen externe scripts")
                self.assertNotRegex(html, r'<link[^>]+stylesheet', "geen externe stylesheets")
                self.assertNotRegex(html, r'src="https?://', "geen externe bronnen")
                self.assertIn('lang="nl"', html)
                self.assertIn("[hidden]{display:none!important}", html,
                              "verborgen feiten moeten ook verborgen blijven als een regel display zet")
                self.assertIn("@media print", html)
                aantal = len(re.findall(r'<section class="plaat', html))
                self.assertEqual(aantal, len(deck["platen"]) + 1, "titelplaat plus de platen uit de data")


class Meetkunde(unittest.TestCase):
    MARGE = 8

    def setUp(self):
        self.breedte = meetlat()
        if self.breedte is None:
            self.skipTest("geen letter of geen Pillow gevonden; meetkunde niet getoetst")

    def test_labels_binnen_het_beeld(self):
        for naam, maak in bouw.BEELDEN.items():
            for label in labels(maak()):
                x1, y1, x2, y2 = kader(label, self.breedte)
                with self.subTest(beeld=naam, label=label["tekst"]):
                    self.assertGreaterEqual(x1, self.MARGE)
                    self.assertLessEqual(x2, bouw.B - self.MARGE)
                    self.assertGreaterEqual(y1, self.MARGE)
                    self.assertLessEqual(y2, bouw.H - self.MARGE)

    def test_labels_raken_elkaar_niet(self):
        for naam, maak in bouw.BEELDEN.items():
            ls = [(lab["tekst"], kader(lab, self.breedte)) for lab in labels(maak())]
            for i, (ta, a) in enumerate(ls):
                for tb, b in ls[i + 1:]:
                    with self.subTest(beeld=naam, a=ta, b=tb):
                        overlap = a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]
                        self.assertFalse(overlap, f"'{ta}' en '{tb}' overlappen in {naam}")

    def test_geen_lijn_door_een_label(self):
        """Een lijn die door een woord loopt, zie je pas bij het renderen; deze toets vangt hem eerder."""
        for naam, maak in bouw.BEELDEN.items():
            wortel = ET.fromstring(maak())
            kaders = [(lab["tekst"], kader(lab, self.breedte)) for lab in labels(maak())]
            for ln in wortel.iter(NS + "line"):
                x1, y1, x2, y2 = (float(ln.get(k)) for k in ("x1", "y1", "x2", "y2"))
                for tekst_, (a, b, c, d) in kaders:
                    geraakt = any(a + 1 < x1 + (x2 - x1) * i / 200 < c - 1 and
                                  b + 1 < y1 + (y2 - y1) * i / 200 < d - 1 for i in range(201))
                    with self.subTest(beeld=naam, label=tekst_):
                        self.assertFalse(geraakt, f"een lijn loopt door '{tekst_}' in {naam}")

    def test_tekst_in_balk_past_in_de_balk(self):
        """Labels die midden in een gekleurde balk staan, moeten er met wat lucht in passen."""
        for naam, maak in bouw.BEELDEN.items():
            wortel = ET.fromstring(maak())
            vlakken = [r for r in wortel.iter(NS + "rect")
                       if r.get("fill") not in (bouw.DONKER,) and float(r.get("height")) >= 30]
            for label in labels(maak()):
                x1, y1, x2, y2 = kader(label, self.breedte)
                for r in vlakken:
                    rx, ry = float(r.get("x")), float(r.get("y"))
                    rb, rh = float(r.get("width")), float(r.get("height"))
                    # alleen een label waarvan het midden in de balk valt
                    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                    if rx < mx < rx + rb and ry < my < ry + rh and rb < 700:
                        with self.subTest(beeld=naam, label=label["tekst"]):
                            self.assertGreaterEqual(x1, rx + 4, "label steekt links uit de balk")
                            self.assertLessEqual(x2, rx + rb - 4, "label steekt rechts uit de balk")


if __name__ == "__main__":
    unittest.main(verbosity=1)
