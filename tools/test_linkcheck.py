#!/usr/bin/env python3
"""Tests voor tools/linkcheck.py. Zonder netwerk: de ophaler wordt vervangen.

Draaien:  python tools/test_linkcheck.py
"""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

HIER = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("linkcheck", HIER / "linkcheck.py")
lc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lc)


class Beoordeel(unittest.TestCase):
    def test_open(self):
        self.assertEqual(lc.beoordeel(200, "open"), "ok")
        self.assertEqual(lc.beoordeel(404, "open"), "dood")
        self.assertEqual(lc.beoordeel(410, "open"), "dood")
        self.assertEqual(lc.beoordeel(403, "open"), "muur")
        self.assertEqual(lc.beoordeel(0, "open"), "onbereikbaar")
        self.assertEqual(lc.beoordeel(503, "open"), "onbereikbaar")

    def test_inlog_is_een_muur_juist_goed(self):
        """Bij een besloten bron betekent 401 of 403 dat de ingang leeft."""
        self.assertEqual(lc.beoordeel(401, "inlog"), "ok")
        self.assertEqual(lc.beoordeel(403, "inlog"), "ok")
        self.assertEqual(lc.beoordeel(404, "inlog"), "dood")

    def test_partij_die_scripts_weert_is_geen_muur(self):
        """politie.nl en z-cert.nl geven een 403 aan elke client die geen browser is."""
        self.assertEqual(lc.beoordeel(403, "partij"), "ok")
        self.assertEqual(lc.beoordeel(404, "partij"), "dood")


class Verzamelen(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp()).resolve()
        (self.root / lc.PARTIJEN_REL).parent.mkdir(parents=True)
        (self.root / lc.PARTIJEN_REL).write_text(json.dumps({"partijen": [
            {"id": "ncsc", "url": "https://www.ncsc.nl/"}, {"id": "zonder"}]}), encoding="utf-8")
        (self.root / "bronnen.json").write_text(json.dumps({"bronnen": {
            "a": {"url": "https://a.nl/x", "toegang": "open"},
            "b": {"url": "https://b.nl/y", "toegang": "inlog", "archief": "https://web.archive.org/b"},
            "c": {"url": "https://c.nl/weg", "toegang": "open", "vervallen": "2026-10-01"},
        }}), encoding="utf-8")

    def test_bronnen_archief_en_partijen(self):
        urls = {r["url"] for r in lc.te_controleren(self.root)}
        self.assertEqual(urls, {"https://a.nl/x", "https://b.nl/y", "https://web.archive.org/b",
                                "https://www.ncsc.nl/"})

    def test_vervallen_bron_wordt_niet_meer_opgevraagd(self):
        self.assertNotIn("https://c.nl/weg", {r["url"] for r in lc.te_controleren(self.root)})

    def test_rapport_en_volgorde(self):
        antwoorden = {"https://a.nl/x": 404, "https://b.nl/y": 403, "https://web.archive.org/b": 200,
                      "https://www.ncsc.nl/": 0}
        uitslag = lc.controleer(lc.te_controleren(self.root), antwoorden.__getitem__)
        tekst = lc.rapport(uitslag)
        self.assertIn("4 adressen, 2 met een melding", tekst)
        self.assertLess(tekst.index("| dood |"), tekst.index("| onbereikbaar |"))
        self.assertIn("geen antwoord", tekst)
        self.assertNotIn("bron b ", tekst)  # inlog met 403 is in orde

    def test_alles_goed_geeft_een_regel(self):
        uitslag = lc.controleer(lc.te_controleren(self.root), lambda url: 200)
        self.assertFalse(lc.heeft_melding(uitslag))
        self.assertEqual(lc.rapport(uitslag).strip().count("\n"), 0)

    def test_alleen_onbereikbaar_opent_geen_issue(self):
        """Een certificaatfout bij een ander mag niet elke maand een issue openen."""
        uitslag = lc.controleer(lc.te_controleren(self.root), lambda url: 0 if "ncsc" in url else 200)
        self.assertFalse(lc.heeft_melding(uitslag))
        tekst = lc.rapport(uitslag)
        self.assertNotIn("| Oordeel |", tekst)
        self.assertIn("partij ncsc", tekst)

    def test_dood_opent_wel_een_issue(self):
        uitslag = lc.controleer(lc.te_controleren(self.root), lambda url: 404 if "a.nl" in url else 200)
        self.assertTrue(lc.heeft_melding(uitslag))
        self.assertIn("| dood | bron a |", lc.rapport(uitslag))


if __name__ == "__main__":
    unittest.main()
