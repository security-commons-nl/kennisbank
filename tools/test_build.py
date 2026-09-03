#!/usr/bin/env python3
"""Tests voor tools/build.py.

Draaien:  python tools/test_build.py        (of: python -m unittest discover -s tools)

De nadruk ligt op de controles die een lezer op de site raken: staat wat in de map ligt ook als
link op de pagina, wijzen links naar iets dat bestaat, en sluit elke leesversie af met een route
naar de bron. De laatste test draait de echte kennisbank door de controle heen.
"""
from __future__ import annotations

import importlib.util
import re
import tempfile
import unittest
from pathlib import Path

HIER = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("build", HIER / "build.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class Basis(unittest.TestCase):
    def setUp(self) -> None:
        build.fouten.clear()
        # resolve(): op Windows levert mkdtemp() de korte 8.3-vorm en build.ROOT de lange, waardoor
        # een bestand binnen de map buiten de kennisbank lijkt te vallen.
        self.map = Path(tempfile.mkdtemp()).resolve()
        self.oude_root = build.ROOT
        build.ROOT = self.map

    def tearDown(self) -> None:
        build.ROOT = self.oude_root
        build.fouten.clear()

    def item(self, readme: str, pagina: str | None = None, **bestanden: str) -> Path:
        map_ = self.map / "security" / "een-item"
        map_.mkdir(parents=True)
        (map_ / "README.md").write_text(readme, encoding="utf-8")
        if pagina is not None:
            (map_ / "index.html").write_text(pagina, encoding="utf-8")
        for naam, inhoud in bestanden.items():
            pad = map_ / naam.replace("__", "/")
            pad.parent.mkdir(parents=True, exist_ok=True)
            pad.write_text(inhoud, encoding="utf-8")
        return map_

    @property
    def meldingen(self) -> str:
        return "\n".join(build.fouten)


class Bronvoet(Basis):
    """De afsluitende regel die naar de bronbestanden wijst (statuut B10)."""

    def test_wijst_naar_de_map_van_het_item(self):
        voet = build.bronvoet("security", "passkeys-invoeren")
        self.assertIn(f"{build.REPO}/tree/main/security/passkeys-invoeren", voet)
        self.assertIn("EUPL-1.2", voet)

    def test_komt_voor_body_einde(self):
        uit = build.zet_bronvoet("<html><body><p>tekst</p></body></html>", "security", "x")
        self.assertLess(uit.index(build.BRON_START), uit.index("</body>"))

    def test_stapelt_niet_bij_opnieuw_bouwen(self):
        een = build.zet_bronvoet("<html><body>t</body></html>", "security", "x")
        twee = build.zet_bronvoet(een, "security", "x")
        self.assertEqual(een, twee)
        self.assertEqual(twee.count(build.BRON_START), 1)

    def test_vernieuwt_een_verouderde_voet(self):
        oud = build.zet_bronvoet("<html><body>t</body></html>", "security", "oude-naam")
        nieuw = build.zet_bronvoet(oud, "security", "nieuwe-naam")
        self.assertIn("security/nieuwe-naam", nieuw)
        self.assertNotIn("security/oude-naam", nieuw)

    def test_zonder_body_geen_voet(self):
        # Dan meldt zet_kruimelpad het als fout; stil toevoegen zou de pagina stukmaken.
        self.assertNotIn(build.BRON_START, build.zet_bronvoet("<p>los fragment</p>", "security", "x"))


class Bestandslinks(Basis):
    """Statuut B3: wat in de map staat, is bereikbaar vanaf de README en vanaf de pagina."""

    def test_bijlage_alleen_als_code_in_de_readme_is_een_fout(self):
        # Precies wat er misging: de pptx stond er wel, maar nergens klikbaar.
        map_ = self.item("Zie `sessie.pptx` voor de slides.",
                         "<html><body><code>sessie.pptx</code></body></html>",
                         **{"sessie.pptx": "x"})
        build.controleer_bestandslinks(map_, map_ / "README.md")
        self.assertIn("sessie.pptx", self.meldingen)
        self.assertIn("de README", self.meldingen)
        self.assertIn("de leesversie", self.meldingen)

    def test_link_in_readme_maar_niet_op_de_pagina(self):
        map_ = self.item("[slides](sessie.pptx)", "<html><body>niets</body></html>",
                         **{"sessie.pptx": "x"})
        build.controleer_bestandslinks(map_, map_ / "README.md")
        self.assertIn("de leesversie", self.meldingen)
        self.assertNotIn("in de README", self.meldingen)

    def test_beide_gelinkt_is_goed(self):
        map_ = self.item("[slides](sessie.pptx)",
                         '<html><body><a href="sessie.pptx">slides</a></body></html>',
                         **{"sessie.pptx": "x"})
        build.controleer_bestandslinks(map_, map_ / "README.md")
        self.assertEqual(build.fouten, [])

    def test_link_naar_een_anker_telt_mee(self):
        map_ = self.item("[artikel 3](annex.md#artikel-3)",
                         '<html><body><a href="annex.md#artikel-3">a3</a></body></html>',
                         **{"annex.md": "# Annex"})
        build.controleer_bestandslinks(map_, map_ / "README.md")
        self.assertEqual(build.fouten, [])

    def test_bestand_in_submap_telt_mee(self):
        map_ = self.item("[dataset](data/partijen.json)",
                         '<html><body><a href="data/partijen.json">d</a></body></html>',
                         **{"data__partijen.json": "{}"})
        build.controleer_bestandslinks(map_, map_ / "README.md")
        self.assertEqual(build.fouten, [])


class DodeLinks(Basis):
    """Statuut B3: een verwijzing wijst naar iets dat bestaat en binnen de kennisbank blijft."""

    def test_verdwenen_bestand_wordt_gemeld(self):
        # Zo bleef blue-team-opzetten verwijzen naar een bestand dat index.html was gaan heten.
        map_ = self.item("[leesversie](een-blue-team-opzetten.html)")
        build.controleer_dode_links(map_)
        self.assertIn("een-blue-team-opzetten.html", self.meldingen)

    def test_een_niveau_te_hoog_wordt_gemeld(self):
        map_ = self.item("[kennisbank](../../../)")
        build.controleer_dode_links(map_)
        self.assertIn("buiten de kennisbank", self.meldingen)

    def test_externe_en_site_links_blijven_buiten_schot(self):
        map_ = self.item("[extern](https://example.org/x) [icoon](/favicon.svg) "
                         "[mail](mailto:iemand@example.org) [kop](#ergens)")
        build.controleer_dode_links(map_)
        self.assertEqual(build.fouten, [])

    def test_link_naar_bestaand_bestand_is_goed(self):
        map_ = self.item("[bijlage](bijlage.md)", **{"bijlage.md": "# Bijlage"})
        build.controleer_dode_links(map_)
        self.assertEqual(build.fouten, [])




class Frontmatter(unittest.TestCase):
    """Een waarde mag over meerdere regels lopen; dat is gewone YAML en het gebeurt bij samenvattingen."""

    @staticmethod
    def blok(*regels: str) -> str:
        return "\n".join(("---", *regels, "---", "# Kop", ""))

    def test_vervolgregels_horen_bij_de_waarde(self):
        fm, _ = build.lees_frontmatter(self.blok(
            "titel: Een titel", "samenvatting: Eerste regel", "  tweede regel", "  derde regel"))
        self.assertEqual(fm["samenvatting"], "Eerste regel tweede regel derde regel")

    def test_een_dubbele_punt_in_een_vervolgregel_is_geen_nieuw_veld(self):
        """De val: 'bestrijdt: en meer' op een vervolgregel werd een eigen veld en dan weigerde B2 het."""
        fm, _ = build.lees_frontmatter(self.blok(
            "titel: T", "samenvatting: Een team dat een calamiteit", "  bestrijdt: en meer."))
        self.assertNotIn("bestrijdt", fm)
        self.assertIn("bestrijdt: en meer.", fm["samenvatting"])

    def test_lijsten_blijven_lijsten(self):
        fm, _ = build.lees_frontmatter(self.blok(
            "normen: [BIO2, NIS2]", "barrieres:", "  - crisis", "  - critical"))
        self.assertEqual(fm["normen"], ["BIO2", "NIS2"])
        self.assertEqual(fm["barrieres"], ["crisis", "critical"])


class Zoeken(Basis):
    """Het zoekvak en het barrierefilter op de landingspagina.

    Het vakgebiedfilter is hier weggehaald: 48 van de 51 items staan onder security, dus dat filter
    onderscheidde niets meer. De barriere spreidt wel (36 verschillende) en is dezelfde sleutel als de
    zelfcheck.
    """

    def kaartje(self, **velden) -> dict:
        basis = {"titel": "Titel", "samenvatting": "Samenvatting.", "type": "handleiding",
                 "status": "in gebruik", "_vak": "security", "_link": "een-item/", "_weergave": "live"}
        basis.update(velden)
        return basis

    def test_kaart_draagt_zoektekst_en_barrieres(self):
        html = build.kaart(self.kaartje(titel="Passkeys invoeren", barrieres=["pr", "fallback"]), "", True)
        self.assertIn('data-barrieres="pr fallback"', html)
        self.assertIn("passkeys invoeren", html)  # kleine letters, want daar wordt op vergeleken

    def test_zoektekst_bevat_titel_en_samenvatting(self):
        html = build.kaart(self.kaartje(titel="Logboek", samenvatting="Vastleggen tijdens een calamiteit."), "", True)
        for woord in ("logboek", "calamiteit"):
            self.assertIn(woord, html)

    def test_kaart_zonder_barrieres_krijgt_een_leeg_veld(self):
        """Zo'n kaart hoort te verdwijnen zodra er een barriere gekozen wordt, en niet te blijven staan."""
        self.assertIn('data-barrieres=""', build.kaart(self.kaartje(), "", True))

    def test_balk_staat_uit_tot_het_script_hem_aanzet(self):
        """Zonder JavaScript blijft alles zichtbaar in plaats van dat er een dood zoekvak staat."""
        self.assertIn("hidden>", build.zoekbalk([self.kaartje()]))

    def test_de_keuzelijst_telt_per_barriere(self):
        balk = build.zoekbalk([self.kaartje(barrieres=["crisis"]), self.kaartje(barrieres=["crisis"]),
                               self.kaartje(barrieres=["critical"])])
        self.assertIn('<option value="">Alle barrieres</option>', balk)
        self.assertIn('value="crisis"', balk)
        self.assertIn("(2)", balk)
        self.assertIn("(1)", balk)

    def test_alleen_barrieres_die_voorkomen_staan_in_de_lijst(self):
        """Een keuzelijst met barrieres zonder stuk erachter levert alleen lege uitkomsten op."""
        balk = build.zoekbalk([self.kaartje(barrieres=["crisis"])])
        self.assertIn('value="crisis"', balk)
        self.assertNotIn('value="critical"', balk)

    def test_de_telling_noemt_het_totaal(self):
        self.assertIn("3 stukken", build.zoekbalk([self.kaartje(), self.kaartje(), self.kaartje()]))


class Volgorde(Basis):
    """Statuut B4: de volgorde van de items staat in de README van de sectie, niet in het alfabet."""

    README = """# Security

## Volgorde

1. [Derde](derde/)
2. [Eerste](eerste/)
3. [Tweede](tweede/)

## Bijdragen
"""

    def items(self, *namen: str) -> list[dict]:
        return [{"_map": self.map / n} for n in namen]

    def test_leest_de_mapnamen_in_de_volgorde_van_de_lijst(self):
        self.assertEqual(build.lees_volgorde(self.README), ["derde", "eerste", "tweede"])

    def test_zonder_lijst_leeg(self):
        self.assertEqual(build.lees_volgorde("# Security\n\n## Bijdragen\n"), [])

    def test_items_volgen_de_lijst(self):
        uit = build.zet_op_volgorde("security", self.items("eerste", "tweede", "derde"),
                                    {"volgorde": ["derde", "eerste", "tweede"]})
        self.assertEqual([fm["_map"].name for fm in uit], ["derde", "eerste", "tweede"])
        self.assertEqual(build.fouten, [])

    def test_item_dat_niet_in_de_lijst_staat_is_een_fout(self):
        (self.map / "security").mkdir(parents=True, exist_ok=True)
        (self.map / "security" / "README.md").write_text("x", encoding="utf-8")
        uit = build.zet_op_volgorde("security", self.items("eerste", "vergeten"),
                                    {"volgorde": ["eerste"]})
        self.assertIn("vergeten", self.meldingen)
        # Vergeten items verdwijnen niet: ze staan achteraan zodat de pagina compleet blijft.
        self.assertEqual([fm["_map"].name for fm in uit], ["eerste", "vergeten"])

    def test_naam_in_de_lijst_die_niet_bestaat_is_een_fout(self):
        (self.map / "security").mkdir(parents=True, exist_ok=True)
        (self.map / "security" / "README.md").write_text("x", encoding="utf-8")
        build.zet_op_volgorde("security", self.items("eerste"), {"volgorde": ["eerste", "spook"]})
        self.assertIn("spook", self.meldingen)

    def test_sectie_zonder_lijst_is_een_fout(self):
        (self.map / "security").mkdir(parents=True, exist_ok=True)
        (self.map / "security" / "README.md").write_text("x", encoding="utf-8")
        build.zet_op_volgorde("security", self.items("eerste"), {"volgorde": []})
        self.assertIn("Volgorde", self.meldingen)

    def test_lege_sectie_hoeft_geen_lijst(self):
        self.assertEqual(build.zet_op_volgorde("privacy", [], {"volgorde": []}), [])
        self.assertEqual(build.fouten, [])


class EchteKennisbank(unittest.TestCase):
    """De controle over de echte inhoud; dit is het net onder alle regels samen."""

    def test_geen_overtredingen(self):
        build.fouten.clear()
        build.controleer_alles()
        self.assertEqual(build.fouten, [], "\n".join(build.fouten))

    def test_elke_leesversie_heeft_een_bronvoet(self):
        for pagina in sorted(build.ROOT.glob("*/*/index.html")):
            with self.subTest(pagina=str(pagina)):
                self.assertIn(build.BRON_START, pagina.read_text(encoding="utf-8"))



class Voorpagina(unittest.TestCase):
    """De indeling van de gebouwde voorpagina (index.html in de repo-root).

    De vier vakgebieden zijn orientatie en horen boven de publicaties te staan. Ze stonden onderaan
    onder het kopje "Secties", waar niemand ze zag, terwijl "is hier iets voor mij?" juist de eerste
    vraag is van een FG of een BCM-coordinator (Bas, 03-09-2026). Geen filter op vakgebied: 48 van de
    52 stukken staan onder security en privacy is leeg, dus filteren zou vier stukken verbergen of
    een lege pagina geven. Een tegel met de telling erin, ook als die nul is, zegt hetzelfde
    eerlijker en nodigt uit om iets in te brengen.
    """

    @classmethod
    def setUpClass(cls) -> None:
        pad = build.ROOT / "index.html"
        if not pad.exists():
            raise unittest.SkipTest("index.html is nog niet gebouwd; draai tools/build.py")
        cls.html = pad.read_text(encoding="utf-8")

    def test_vakgebieden_staan_boven_de_kaarten(self) -> None:
        self.assertIn('<div class="vakken">', self.html)
        self.assertLess(self.html.index("Waar zoek je in?"), self.html.index("Direct te lezen"))
        self.assertLess(self.html.index('class="vakken"'), self.html.index('id="direct-te-lezen"'))
        self.assertNotIn("<h2>Secties</h2>", self.html)
        for vak in ("security", "privacy", "bcm", "governance"):
            self.assertIn('href="%s/"' % vak, self.html)
        self.assertIn("nog leeg", self.html)

    def test_filter_blijft_zoeken_en_barriere(self) -> None:
        """Geen vakgebiedfilter erbij: dat onderscheidt niets en zou op privacy een lege lijst geven."""
        self.assertIn('id="zoek"', self.html)
        self.assertIn('id="barriere"', self.html)
        self.assertNotIn('id="vakgebied"', self.html)

    def test_tegeltekst_is_kort_en_heel(self) -> None:
        begin = self.html.index('<div class="vakken">')
        blok = self.html[begin:self.html.index("</div>", begin)]
        teksten = re.findall(r'itemdesc">([^<]*)<', blok)
        self.assertEqual(len(teksten), 4, teksten)
        for tekst in teksten:
            self.assertTrue(0 < len(tekst) <= 72, tekst)
            self.assertFalse(tekst.endswith(("-", ",", ";")), tekst)

if __name__ == "__main__":
    unittest.main(verbosity=2)
