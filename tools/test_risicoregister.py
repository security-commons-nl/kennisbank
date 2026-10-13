#!/usr/bin/env python3
"""Tests voor tools/bouw_risicoregister.py.

Draaien:  python tools/test_risicoregister.py

Drie soorten: het script weigert een register dat niet klopt; de afleiding en de rekenregels doen wat
het model zegt; en de uitvoer (markdown en verkenner) zegt hetzelfde, in dezelfde volgorde. De laatste
test legt de prioriteit van het voorbeeld vast, zodat een wijziging aan de regels zichtbaar wordt.
"""
from __future__ import annotations

import copy
import importlib.util
import json
import re
import tempfile
import unittest
from pathlib import Path

HIER = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("rr", HIER / "bouw_risicoregister.py")
rr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rr)

VOORBEELD = json.loads(rr.INVOER.read_text(encoding="utf-8"))


def reg() -> dict:
    return copy.deepcopy(VOORBEELD)


def bev(r: dict, code: str) -> dict:
    return next(b for b in r["bevindingen"] if b["code"] == code)


def maatr(r: dict, sleutel: str) -> dict:
    return next(m for m in r["maatregelen"] if m["sleutel"] == sleutel)


class Weigeren(unittest.TestCase):
    """Wat de generator niet accepteert. Elke test breekt het voorbeeld op één punt."""

    def weigert(self, r: dict, tekst: str) -> None:
        with self.assertRaises(rr.RegisterFout) as ctx:
            rr.toets(r)
        self.assertIn(tekst, str(ctx.exception))

    def test_voorbeeld_is_geldig(self):
        self.assertEqual(rr.toets(reg()), [])

    def test_bevinding_zonder_maatregel_en_zonder_uitzondering(self):
        r = reg(); bev(r, "B-01")["maatregelen"] = []
        self.weigert(r, "noemt geen maatregel en geen uitzondering")

    def test_onbekende_maatregelsleutel(self):
        r = reg(); bev(r, "B-01")["maatregelen"][0]["sleutel"] = "BIO2:9.99.99"
        self.weigert(r, "'BIO2:9.99.99' bestaat niet")

    def test_maatregel_zonder_reden(self):
        r = reg(); bev(r, "B-01")["maatregelen"][0]["reden"] = " "
        self.weigert(r, "zonder reden")

    def test_bevinding_zonder_bron(self):
        r = reg(); bev(r, "B-02")["bron"] = ""
        self.weigert(r, "'bron' ontbreekt")

    def test_bevinding_zonder_peildatum(self):
        r = reg(); del bev(r, "B-02")["peildatum"]
        self.weigert(r, "peildatum ontbreekt")

    def test_dubbele_code(self):
        r = reg(); bev(r, "B-02")["code"] = "B-01"
        self.weigert(r, "B-01: dubbele code")

    def test_onbekende_status(self):
        r = reg(); bev(r, "B-02")["status"] = "afgehandeld"
        self.weigert(r, "status 'afgehandeld'")

    def test_onbekende_bronsoort(self):
        r = reg(); bev(r, "B-02")["bronsoort"] = "gevoel"
        self.weigert(r, "bronsoort 'gevoel'")

    def test_geaccepteerd_zonder_besluit(self):
        r = reg(); del bev(r, "B-06")["acceptatie"]
        self.weigert(r, "geaccepteerd zonder besluit")

    def test_maatregel_onder_or_van_ander_kader(self):
        r = reg(); maatr(r, "AVG:A15")["or"] = "OR-05"
        self.weigert(r, "een maatregel hangt onder een OR uit de standaardlijst van zijn eigen kader")

    def test_or_met_onbekend_sr(self):
        r = reg(); r["or"][0]["sr"] = "SR-99"
        self.weigert(r, "SR 'SR-99' bestaat niet")

    def test_score_buiten_schaal(self):
        r = reg(); bev(r, "B-01")["kans"] = 7
        self.weigert(r, "kans moet een geheel getal van 1 tot en met 5 zijn")

    def test_uitzondering_vraagt_motivering(self):
        r = reg(); b = bev(r, "B-01"); b["maatregelen"] = []; b["uitzondering"] = {"or": "OR-05", "motivering": ""}
        self.weigert(r, "uitzondering vraagt een bestaand OR en een motivering")


class Meldingen(unittest.TestCase):
    def test_oud_feit_wordt_gemeld(self):
        r = reg(); bev(r, "B-01")["peildatum"] = "2025-08-01"
        self.assertTrue(any("B-01" in m and "twaalf maanden" in m for m in rr.toets(r)))

    def test_oud_feit_van_een_gesloten_bevinding_niet(self):
        r = reg(); b = bev(r, "B-01"); b["peildatum"] = "2025-08-01"; b["status"] = "gesloten"
        self.assertEqual(rr.toets(r), [])

    def test_sr_zonder_or_wordt_gemeld(self):
        r = reg(); r["sr"].append({"code": "SR-04", "titel": "Leeg", "kans": 2, "impact": 2})
        self.assertTrue(any(m.startswith("SR-04") for m in rr.toets(r)))

    def test_uitzondering_wordt_gemeld(self):
        r = reg(); b = bev(r, "B-01"); b["maatregelen"] = []
        b["uitzondering"] = {"or": "OR-05", "motivering": "geen maatregel in de set dekt dit"}
        meldingen = rr.toets(r)
        self.assertTrue(any("uitzondering" in m for m in meldingen))
        u = rr.reken(r)
        self.assertEqual(next(x for x in u["bevindingen"] if x["code"] == "B-01")["or_primair"], "OR-05")


class Afleiding(unittest.TestCase):
    def setUp(self):
        self.u = rr.reken(reg())

    def b(self, code):
        return next(b for b in self.u["bevindingen"] if b["code"] == code)

    def test_primair_or_uit_eerste_maatregel(self):
        self.assertEqual(self.b("B-05")["or_primair"], "OR-06")
        self.assertEqual(self.b("B-05")["or_secundair"], ["OR-05"])

    def test_volgorde_van_maatregelen_bepaalt_het_primaire_or(self):
        r = reg(); b = bev(r, "B-05"); b["maatregelen"].reverse()
        u = rr.reken(r)
        x = next(b for b in u["bevindingen"] if b["code"] == "B-05")
        self.assertEqual((x["or_primair"], x["or_secundair"]), ("OR-05", ["OR-06"]))

    def test_secundair_zonder_dubbel_primair(self):
        self.assertEqual(self.b("B-02")["or_secundair"], [])  # beide maatregelen onder OR-01

    def test_sr_uit_het_primaire_or(self):
        self.assertEqual(self.b("B-03")["sr"], "SR-01")
        self.assertEqual(self.b("B-04")["sr"], "SR-02")

    def test_geaccepteerd_telt_niet(self):
        self.assertFalse(self.b("B-06")["telt"])
        self.assertFalse(self.u["or"]["OR-04"]["beoordeeld"])
        self.assertIn("B-06", self.u["or"]["OR-04"]["bevindingen"])  # wel zichtbaar

    def test_kandidaat_telt_niet(self):
        r = reg(); bev(r, "B-04")["status"] = "kandidaat"
        self.assertFalse(rr.reken(r)["or"]["OR-03"]["beoordeeld"])

    def test_or_score_alleen_uit_primaire_bevindingen(self):
        # B-05 raakt OR-05 secundair met score 12; OR-05 heeft B-01 (12) als primair. Maak B-01 lager:
        r = reg(); b = bev(r, "B-01"); b["kans"], b["impact"] = 1, 2
        self.assertEqual(rr.reken(r)["or"]["OR-05"]["score"], 2)

    def test_or_score_is_hoogste_meetellende(self):
        self.assertEqual(self.u["or"]["OR-01"]["score"], 20)
        self.assertEqual(self.u["or"]["OR-01"]["klasse"], "Kritiek")


class Niveau(unittest.TestCase):
    def setUp(self):
        self.u = rr.reken(reg())

    def n(self, sleutel):
        return self.u["maatregelen"][sleutel]["niveau"]

    def test_avg_cumulatief(self):
        self.assertEqual(self.n("AVG:A15"), 2)  # groen, groen, rood
        self.assertEqual(self.n("AVG:A12"), 1)  # groen, oranje, rood: oranje telt niet
        self.assertEqual(self.n("AVG:A29"), 1)

    def test_avg_werking_vraagt_ook_opzet_en_bestaan(self):
        m = {"sleutel": "AVG:A15", "stand": {"opzet": "rood", "bestaan": "groen", "werking": "groen"}}
        self.assertEqual(rr.niveau_uit_bron(m), 0)

    def test_bcm(self):
        self.assertEqual((self.n("BCM:8.2.2"), self.n("BCM:8.4.4"), self.n("BCM:8.5")), (2, 1, 0))

    def test_bio2_zelfbeoordeling_hooguit_bestaan(self):
        self.assertEqual(self.n("BIO2:8.15.01"), 2)
        self.assertEqual(self.n("BIO2:8.16.01"), 0)

    def test_werking_alleen_via_getoetste_control(self):
        self.assertEqual(self.n("BIO2:8.05.01"), 3)

    def test_werking_vervalt_bij_gemiste_cyclus(self):
        self.assertEqual(self.n("BIO2:5.15.01"), 2)
        self.assertIn("verlopen", self.u["maatregelen"]["BIO2:5.15.01"]["niveau_herkomst"])
        r = reg(); r["peildatum"] = "2026-06-20"  # binnen de maandcyclus van C-03
        self.assertEqual(rr.reken(r)["maatregelen"]["BIO2:5.15.01"]["niveau"], 3)

    def test_zwakste_control_wint(self):
        # 5.18.01: C-01 werking negatief (2), C-03 verlopen (2). Zet C-03 op tijd en C-01 op niets:
        r = reg(); r["peildatum"] = "2026-06-20"
        r["controls"][0]["toets"].update({"opzet": False, "bestaan": False, "werking": False})
        self.assertEqual(rr.reken(r)["maatregelen"]["BIO2:5.18.01"]["niveau"], 0)

    def test_meetellende_bevinding_zet_werking_terug(self):
        r = reg()
        bev(r, "B-01")["maatregelen"].append({"sleutel": "BIO2:8.05.01", "reden": "test"})
        u = rr.reken(r)
        self.assertEqual(u["maatregelen"]["BIO2:8.05.01"]["niveau"], 2)
        self.assertIn("weerlegd door B-01", u["maatregelen"]["BIO2:8.05.01"]["niveau_herkomst"])

    def test_geaccepteerde_bevinding_zet_niets_terug(self):
        r = reg(); bev(r, "B-06")["maatregelen"][0]["sleutel"] = "BIO2:8.05.01"
        self.assertEqual(rr.reken(r)["maatregelen"]["BIO2:8.05.01"]["niveau"], 3)


class Prioriteit(unittest.TestCase):
    def setUp(self):
        self.u = rr.reken(reg())
        self.volgorde = [r["sleutel"] for r in self.u["prioriteit"]]

    def test_volgorde_van_het_voorbeeld(self):
        self.assertEqual(self.volgorde, [
            "BIO2:8.08.01", "BIO2:8.08.02",                       # OR-01, score 20
            "BCM:8.5", "BCM:8.4.4", "BCM:8.2.2",                  # OR-02, score 15
            "BIO2:8.02.01", "BIO2:8.16.01",                       # OR-05 en OR-06, score 12, SR-03 15, niveau 0
            "BIO2:5.15.01", "BIO2:5.18.01", "BIO2:8.15.01",       # idem, niveau 2
            "BIO2:8.05.01",                                       # idem, op werking: achteraan
            "AVG:A12", "AVG:A15",                                 # OR-03, score 8
            "AVG:A29", "AVG:A28",                                 # OR-04 niet beoordeeld, SR-02 12
            "BIO2:7.02.01",                                       # buiten de SRA
        ])

    def test_aangetoond_gat_gaat_voor_hoger_sr(self):
        # OR-03 (score 8) staat voor OR-04 (niet beoordeeld) ook al hangen ze onder hetzelfde SR.
        self.assertLess(self.volgorde.index("AVG:A15"), self.volgorde.index("AVG:A29"))

    def test_buiten_de_sra_laatst(self):
        self.assertEqual(self.volgorde[-1], "BIO2:7.02.01")

    def test_elke_maatregel_precies_een_keer(self):
        self.assertEqual(sorted(self.volgorde), sorted(self.u["maatregelen"]))


class Uitvoer(unittest.TestCase):
    def setUp(self):
        self.uit = {p.name: t for p, t in rr.bouw(rr.INVOER, rr.ITEM).items()}
        self.md = self.uit["voorbeeld-register.md"]
        self.html = self.uit["voorbeeld-register-verkenner.html"]

    def test_markdown_en_verkenner_dezelfde_volgorde(self):
        sectie = self.md.split("## Prioriteit")[1].split("\n## ")[0]
        md = re.findall(r"^\| \d+ \| (\S+) \|", sectie, re.M)
        paneel = self.html.split('data-paneel="prioriteit"')[1].split("</section>")[0]
        htm = re.findall(r'data-sleutel="([^"]+)"', paneel)
        self.assertEqual(md, htm)
        self.assertEqual(len(md), len(VOORBEELD["maatregelen"]))

    def test_elke_bevinding_in_beide(self):
        for b in VOORBEELD["bevindingen"]:
            self.assertIn(f"### {b['code']} · ", self.md)
            self.assertIn(f"{b['code']} · ", self.html)

    def test_verkenner_rekent_niet(self):
        script = self.html.split("<script>")[1]
        for woord in ("score", "kans", "impact", "niveau", "sort("):
            self.assertNotIn(woord, script, f"de verkenner hoort niet te rekenen ({woord})")

    def test_verkenner_zelfstandig(self):
        externe = re.findall(r'<(?:script|link)[^>]+(?:src|href)="(https?://[^"]+)"', self.html)
        self.assertEqual([u for u in externe if not u.endswith("favicon.svg")], [])

    def test_verkenner_kruimelpad_en_tabs(self):
        self.assertIn('class="kruimel"', self.html)
        for tab in ("prioriteit", "boom", "bevindingen", "maatregelen", "controls"):
            self.assertIn(f'data-tab="{tab}"', self.html)
            self.assertIn(f'data-paneel="{tab}"', self.html)

    def test_verborgen_wint_van_weergave(self):
        # display:flex of grid op een element wint anders van het hidden-attribuut.
        self.assertIn("[hidden]{display:none!important}", self.html)

    def test_geen_em_dashes(self):
        for naam, tekst in self.uit.items():
            self.assertNotIn("—", tekst, naam)
            self.assertNotIn("–", tekst, naam)

    def test_check_ziet_achterstand(self):
        with tempfile.TemporaryDirectory() as d:
            uit = Path(d)
            self.assertEqual(rr.main([str(rr.INVOER), str(uit)]), 0)
            self.assertEqual(rr.main([str(rr.INVOER), str(uit), "--check"]), 0)
            (uit / "voorbeeld-register.md").write_text("verouderd", encoding="utf-8")
            self.assertEqual(rr.main([str(rr.INVOER), str(uit), "--check"]), 1)

    def test_bestanden_in_de_kennisbank_lopen_niet_achter(self):
        self.assertEqual(rr.main(["--check"]), 0)


if __name__ == "__main__":
    unittest.main(verbosity=1)
