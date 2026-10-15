#!/usr/bin/env python3
"""Tests voor tools/bouw_stelselkaart.py.

De stelselkaart wordt gebouwd uit data/partijen.json en data/diensten.json. Deze tests controleren
dat de pagina dezelfde partijen toont als de publieke versie van voor de omzetting (aantal, id's en
namen), dat de pagina bij de dataset past, en dat de controle op de dataset fouten vangt.

Draaien:  python tools/test_stelselkaart.py
"""
from __future__ import annotations

import copy
import importlib.util
import json
import re
import unittest
from pathlib import Path

HIER = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("bouw_stelselkaart", HIER / "bouw_stelselkaart.py")
bs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bs)

PEIL = json.loads((HIER / "fixtures" / "stelselkaart-publiek-2026-10-01.json").read_text(encoding="utf-8"))


def rijen(html: str, naam: str) -> list[list]:
    """Leest een datablok uit de pagina, los van de bouwer: een JSON-array per regel."""
    m = re.search(r"\nconst " + naam + r"=\[\n(.*?)\n\];", html, re.S)
    if not m:
        raise AssertionError(f"blok const {naam} niet gevonden")
    return [json.loads(r.rstrip(",")) for r in m.group(1).split("\n") if r.startswith("[")]


class HerbouwdeKaart(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.partijen = bs.lees(bs.PARTIJEN)
        cls.diensten = bs.lees(bs.DIENSTEN)
        cls.pagina = bs.PAGINA.read_text(encoding="utf-8")
        cls.herbouwd = bs.bouw(cls.pagina, cls.partijen, cls.diensten)
        cls.p = rijen(cls.herbouwd, "P")

    def test_zelfde_aantal_als_de_publieke_versie(self):
        self.assertEqual(PEIL["aantal"], 83)
        self.assertEqual(len(self.p), PEIL["aantal"])

    def test_zelfde_partijen_en_namen_als_de_publieke_versie(self):
        self.assertEqual([(r[0], r[1]) for r in self.p],
                         [(x["id"], x["naam"]) for x in PEIL["partijen"]])

    def test_pagina_is_bijgewerkt(self):
        """Wat in de repo staat, is wat de bouwer van de dataset maakt (zelfde als --check)."""
        self.assertEqual(self.herbouwd, self.pagina,
                         "index.html past niet bij de dataset; draai python tools/bouw_stelselkaart.py")

    def test_bouwen_is_herhaalbaar(self):
        self.assertEqual(bs.bouw(self.herbouwd, self.partijen, self.diensten), self.herbouwd)

    def test_elke_partij_met_al_haar_velden(self):
        jp = {p["id"]: p for p in self.partijen["partijen"]}
        for r in self.p:
            p = jp[r[0]]
            self.assertEqual(r[2:5], [p["laag"], p["mandaat"], p["functies"]], r[0])
            self.assertEqual(r[5], bs.TOEGANG_PAGINA[p["toegang_gemeente"]], r[0])
            self.assertEqual(r[6:8], [p["omschrijving"], p["toelichting"]], r[0])
            self.assertEqual(r[8], p.get("url") or "", r[0])

    def test_adressen_staan_op_de_kaart(self):
        met_adres = [r for r in self.p if r[8]]
        self.assertGreater(len(met_adres), 0)
        self.assertTrue(all(r[8].startswith("https://") for r in met_adres))

    def test_diensten_uit_de_dataset(self):
        d = rijen(self.herbouwd, "D")
        self.assertEqual(len(d), len(self.diensten["diensten"]))
        for rij, dienst in zip(d, self.diensten["diensten"]):
            self.assertEqual(rij[:3], [dienst["dienst"], dienst["partijen"], dienst["duiding"]])
            self.assertEqual(rij[3] if len(rij) > 3 else [], dienst["werk_in_uitvoering"])


class Redactie(unittest.TestCase):
    """Geen organisatienaam van de eigen gemeente (redactiestatuut). Namen van publieke functionarissen en het voorbeeld
    Servicepunt71 mogen wel (statuut A2; bewuste publicatiekeuze van vóór 01-10-2026)."""

    VERBODEN = ["Leiden", "Leidse"]

    def test_niet_in_dataset_en_pagina(self):
        for pad in (bs.PARTIJEN, bs.DIENSTEN, bs.PAGINA):
            # Een publiek onderzoek van de universiteit als bron is geen verwijzing naar een gemeente.
            tekst = pad.read_text(encoding="utf-8").replace("Universiteit Leiden", "")
            for woord in self.VERBODEN:
                self.assertFalse(woord in tekst, f"{pad.name} bevat '{woord}'")


class Controle(unittest.TestCase):
    def setUp(self):
        self.partijen = bs.lees(bs.PARTIJEN)
        self.diensten = bs.lees(bs.DIENSTEN)

    def test_schone_dataset(self):
        self.assertEqual(bs.controleer(self.partijen, self.diensten), [])

    def test_onbekende_laag(self):
        p = copy.deepcopy(self.partijen)
        p["partijen"][0]["laag"] = "gemeente"
        self.assertTrue(any("laag" in f for f in bs.controleer(p, self.diensten)))

    def test_aantal_klopt_niet(self):
        p = copy.deepcopy(self.partijen)
        p["partijen"].pop()
        self.assertTrue(any("aantal" in f for f in bs.controleer(p, self.diensten)))

    def test_dubbele_id(self):
        p = copy.deepcopy(self.partijen)
        p["partijen"][1]["id"] = p["partijen"][0]["id"]
        self.assertTrue(any("dubbele" in f for f in bs.controleer(p, self.diensten)))

    def test_dienst_met_onbekende_partij(self):
        d = copy.deepcopy(self.diensten)
        d["diensten"][0]["partijen"].append("bestaatniet")
        self.assertTrue(any("bestaatniet" in f for f in bs.controleer(self.partijen, d)))

    def test_adres_zonder_https(self):
        p = copy.deepcopy(self.partijen)
        p["partijen"][0]["url"] = "http://voorbeeld.nl"
        self.assertTrue(any("https" in f for f in bs.controleer(p, self.diensten)))

    def test_ontbrekend_blok_stopt_de_bouw(self):
        with self.assertRaises(SystemExit):
            bs.bouw("<html></html>", self.partijen, self.diensten)


if __name__ == "__main__":
    unittest.main(verbosity=1)
