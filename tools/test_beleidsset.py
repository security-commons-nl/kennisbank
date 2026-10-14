"""Tests van de beleidsset: het bouwsteenformaat, de rekenregel, de dekking en de spiegel met JavaScript.

Draaien:  python tools/test_beleidsset.py
"""
from __future__ import annotations

import copy
import json
import random
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import bouw_beleidsset as b  # noqa: E402

VRAGEN = {
    "hosting": {"id": "hosting", "vraag": "Waar draaien je systemen?", "meerdere": True, "doel": "inhoud",
                "antwoorden": [{"id": "eigen-dc", "label": "Eigen"}, {"id": "saas", "label": "SaaS"}]},
    "beheer": {"id": "beheer", "vraag": "Wie beheert je IT?", "meerdere": False, "doel": "inhoud",
               "antwoorden": [{"id": "eigen", "label": "Zelf"}, {"id": "uitbesteed", "label": "Uitbesteed"}]},
}


def data_met(tekst: str) -> dict:
    """Een mini-set met één domein en twee overheidsmaatregelen."""
    profiel = {"vragen": list(VRAGEN.values()), "domeinen": [{"id": "proef", "naam": "Proefdomein"}]}
    maatregelen = {"versie": "proef", "maatregelen": [
        {"id": "8.13.01", "titel": "Back-up", "thema": "Proefdomein", "soort": "overheid"},
        {"id": "8.13.02", "titel": "Back-up", "thema": "Proefdomein", "soort": "overheid"},
        {"id": "8.13.03", "titel": "Back-up", "thema": "Proefdomein", "soort": "alleen-iso"},
        {"id": "5.01.01", "titel": "Beleid", "thema": "Elders", "soort": "overheid"},
    ]}
    steen = b.parse_bouwsteen(tekst, VRAGEN, "proef.md")
    steen["bestand"] = "01-proef.md"
    afkortingen = {"CISO": "Chief Information Security Officer", "BIO": "Baseline Informatiebeveiliging Overheid"}
    return {"profiel": profiel, "maatregelen": maatregelen, "afkortingen": afkortingen, "bouwstenen": [steen]}


KOP = "---\ndomein: proef\ntitel: Proefbeleid\n---\n\n"


class Formaat(unittest.TestCase):
    def fout(self, romp: str, verwacht: str):
        with self.assertRaises(b.BouwsteenFout) as ctx:
            b.parse_bouwsteen(KOP + romp, VRAGEN, "proef.md")
        self.assertIn(verwacht, str(ctx.exception))

    def test_zonder_frontmatter(self):
        with self.assertRaises(b.BouwsteenFout):
            b.parse_bouwsteen("## Kop\n", VRAGEN, "proef.md")

    def test_frontmatter_mist_titel(self):
        with self.assertRaises(b.BouwsteenFout) as ctx:
            b.parse_bouwsteen("---\ndomein: proef\n---\ntekst\n", VRAGEN, "proef.md")
        self.assertIn("titel", str(ctx.exception))

    def test_onbekende_vraag(self):
        self.fout("::: als kleur=rood\nx\n:::\n", "staat niet in profiel.json")

    def test_onbekend_antwoord(self):
        self.fout("::: als beheer=deels\nx\n:::\n", "geen antwoord op 'beheer'")

    def test_genest_blok(self):
        self.fout("::: als beheer=eigen\n::: als hosting=saas\nx\n:::\n:::\n", "nesten niet")

    def test_niet_afgesloten(self):
        self.fout("::: als beheer=eigen\nx\n", "zonder afsluitende")

    def test_losse_sluiter(self):
        self.fout("x\n:::\n", "sluit niets af")

    def test_onleesbare_voorwaarde(self):
        self.fout("::: als beheer is eigen\nx\n:::\n", "niet te lezen")

    def test_invulveld_over_twee_regels(self):
        self.fout("- regel [[veld: begint\n  hier]]\n", "op één regel")

    def test_crlf_wordt_gelezen(self):
        steen = b.parse_bouwsteen((KOP + "- regel [8.13.01]\n").replace("\n", "\r\n"), VRAGEN, "proef.md")
        self.assertEqual(steen["titel"], "Proefbeleid")


class Rekenregel(unittest.TestCase):
    def test_beoordeel(self):
        als = [{"vraag": "beheer", "niet": False, "antwoorden": ["uitbesteed"]}]
        self.assertEqual(b.beoordeel(als, {"beheer": "uitbesteed"}), "ja")
        self.assertEqual(b.beoordeel(als, {"beheer": "eigen"}), "nee")
        self.assertEqual(b.beoordeel(als, {}), "open")

    def test_niet(self):
        als = [{"vraag": "hosting", "niet": True, "antwoorden": ["saas"]}]
        self.assertEqual(b.beoordeel(als, {"hosting": ["eigen-dc"]}), "ja")
        self.assertEqual(b.beoordeel(als, {"hosting": ["eigen-dc", "saas"]}), "nee")

    def test_en_met_een_nee_is_nee_ook_als_een_vraag_open_is(self):
        als = [{"vraag": "beheer", "niet": False, "antwoorden": ["eigen"]},
               {"vraag": "hosting", "niet": False, "antwoorden": ["saas"]}]
        self.assertEqual(b.beoordeel(als, {"hosting": ["eigen-dc"]}), "nee")
        self.assertEqual(b.beoordeel(als, {"hosting": ["saas"]}), "open")

    def test_meerdere_antwoorden_raken_als_een_er_een_past(self):
        als = [{"vraag": "hosting", "niet": False, "antwoorden": ["saas"]}]
        self.assertEqual(b.beoordeel(als, {"hosting": ["eigen-dc", "saas"]}), "ja")

    def test_leeg_antwoord_is_geen_antwoord(self):
        als = [{"vraag": "hosting", "niet": False, "antwoorden": ["saas"]}]
        self.assertEqual(b.beoordeel(als, {"hosting": []}), "open")

    def test_open_blok_krijgt_kader_met_vraag(self):
        d = data_met(KOP + "- a [8.13.01]\n\n::: als beheer=uitbesteed\n- b [8.13.02]\n:::\n")
        md = b.genereer_stuk(d["bouwstenen"][0], d, {})["markdown"]
        self.assertIn("> **Alleen als: Wie beheert je IT? «Uitbesteed»**", md)
        self.assertIn("> 2. b [8.13.02]", md)  # de nummering loopt door in het kader

    def test_gekozen_blok_zonder_kader_en_ander_blok_weg(self):
        tekst = KOP + "::: als beheer=uitbesteed\n- b [8.13.02]\n:::\n::: als beheer=eigen\n- c [8.13.02]\n:::\n"
        d = data_met(tekst)
        md = b.genereer_stuk(d["bouwstenen"][0], d, {"beheer": "uitbesteed"})["markdown"]
        self.assertIn("\n1. b [8.13.02]", md)
        self.assertNotIn("- c", md)
        self.assertNotIn("Alleen als", md)
        self.assertIn("Opgesteld voor dit profiel: Wie beheert je IT? Uitbesteed.", md)

    def test_invulvelden_vet_en_in_de_lijst(self):
        d = data_met(KOP + "- de [[eigenaar: de rol die het doet]] doet het [8.13.01]\n- weer [[eigenaar]] [8.13.02]\n")
        md = b.genereer_stuk(d["bouwstenen"][0], d, {})["markdown"]
        self.assertIn("de **[eigenaar]** doet het", md)
        self.assertEqual(md.count("- **eigenaar**: de rol die het doet"), 1)

    def test_bijlage_noemt_kop_controle_en_ontbrekende(self):
        d = data_met(KOP + "## 3. Regels\n\n- a [8.13.01]\n\n| Nr | Wat | Maatregelen |\n|---|---|---|\n| PRF-01 | kijk | 8.13.01, 8.13.03 |\n")
        stuk = b.genereer_stuk(d["bouwstenen"][0], d, {})
        self.assertIn("| 8.13.01 | Back-up | overheidsmaatregel | 3. Regels | PRF-01 |", stuk["markdown"])
        self.assertIn("| 8.13.02 | Back-up | overheidsmaatregel | niet ingevuld | geen |", stuk["markdown"])
        self.assertIn("| 8.13.03 | Back-up | ISO-beheersmaatregel | niet ingevuld | PRF-01 |", stuk["markdown"])
        self.assertEqual(stuk["controles"], ["8.13.01", "8.13.03"])
        self.assertEqual(stuk["eigen"], ["8.13.01", "8.13.02", "8.13.03"])
        self.assertEqual(stuk["overheid"], ["8.13.01", "8.13.02"])

    def test_nummering_per_paragraaf_ook_in_kader(self):
        tekst = KOP + "### 3.1 A\n\n- een [8.13.01]\n  vervolg\n- twee [8.13.02]\n\n::: als beheer=eigen\n- drie [8.13.03]\n:::\n\n### 3.2 B\n\n- een\n"
        d = data_met(tekst)
        md = b.genereer_stuk(d["bouwstenen"][0], d, {})["markdown"]
        self.assertIn("1. een [8.13.01]\n   vervolg\n2. twee [8.13.02]", md)
        self.assertIn("> 3. drie [8.13.03]", md)
        self.assertIn("### 3.2 B\n\n1. een", md)

    def test_titelblad_en_afkortingen(self):
        d = data_met(KOP + "- de CISO doet het [8.13.01]\n")
        md = b.genereer_stuk(d["bouwstenen"][0], d, {})["markdown"]
        self.assertIn("| Eigenaar | **[eigenaar van dit beleid]** |", md)
        self.assertIn("- **eigenaar van dit beleid**: de manager", md)
        self.assertIn("| CISO | Chief Information Security Officer |", md)
        self.assertNotIn("| BIO |", md)

    def test_maatregel_van_ander_domein_apart_genoemd(self):
        d = data_met(KOP + "- a [8.13.01, 8.13.02, 5.01.01]\n")
        md = b.genereer_stuk(d["bouwstenen"][0], d, {})["markdown"]
        self.assertIn("mee in: 5.01.01 (Beleid)", md)


def vorm(regels: str, controle: str = "| PRF-01 | kijk | 8.13.01, 8.13.02, 8.13.03 |") -> str:
    """Een bouwsteen in de vaste vorm, met `regels` als inhoud van hoofdstuk 3."""
    return (KOP + "## 1. Doel en reikwijdte\n\ntekst\n\n## 2. Uitgangspunten\n\n- x\n\n## 3. Beleidsregels\n\n"
            + regels + "\n\n## 4. Rollen en verantwoordelijkheden\n\n| Rol | Wat |\n|---|---|\n| CISO | kijkt |\n\n"
            "## 5. Naleving en controle\n\n| Nr | Controle | Maatregelen |\n|---|---|---|\n" + controle + "\n\n"
            "## 6. Samenhang\n\ntekst\n")


def meldingen(tekst: str) -> list[str]:
    return [m for m in b.toets(data_met(tekst)) if "vraag '" not in m]


class Dekking(unittest.TestCase):
    def test_gat_bij_een_profiel_wordt_gevonden(self):
        tekst = vorm("- a [8.13.01, 8.13.03]\n::: als beheer=uitbesteed\n- b [8.13.02]\n:::")
        self.assertTrue(any("8.13.02" in m and '"beheer": "eigen"' in m for m in meldingen(tekst)), meldingen(tekst))

    def test_gat_bij_een_combinatie_van_meer_antwoorden(self):
        # met 'niet' valt een regel weg zodra saas meedoet, ook naast eigen-dc
        tekst = vorm("- a [8.13.01, 8.13.03]\n::: als hosting!=saas\n- b [8.13.02]\n:::\n::: als hosting=saas en hosting!=eigen-dc\n- c [8.13.02]\n:::")
        self.assertTrue(any('"eigen-dc", "saas"' in m for m in meldingen(tekst)), meldingen(tekst))

    def test_volledige_dekking_geeft_geen_meldingen(self):
        tekst = vorm("- a [8.13.01, 8.13.03]\n::: als beheer=uitbesteed\n- b [8.13.02]\n:::\n::: als beheer!=uitbesteed\n- c [8.13.02]\n:::")
        self.assertEqual(meldingen(tekst), [])

    def test_onbekend_nummer(self):
        self.assertTrue(any("9.99.99" in m for m in meldingen(vorm("- a [8.13.01, 8.13.02, 9.99.99]"))))

    def test_inhoudsvraag_die_nergens_iets_doet(self):
        self.assertTrue(any("vraag 'beheer'" in m for m in b.toets(data_met(vorm("- a [8.13.01, 8.13.02]")))))

    def test_iso_maatregel_zonder_regel_of_controle(self):
        self.assertTrue(any("niet ingevuld: 8.13.03" in m for m in meldingen(vorm("- a [8.13.01, 8.13.02]"))))
        tekst = vorm("- a [8.13.01, 8.13.02, 8.13.03]", "| PRF-01 | kijk | 8.13.01, 8.13.02 |")
        self.assertTrue(any("zonder controle: 8.13.03" in m for m in meldingen(tekst)), meldingen(tekst))


class Vorm(unittest.TestCase):
    GOED = vorm("- a [8.13.01, 8.13.02, 8.13.03]")

    def test_goede_vorm_geeft_niets(self):
        self.assertEqual(meldingen(self.GOED), [])

    def test_hoofdstukken_vast(self):
        self.assertTrue(any("hoofdstukken" in m for m in meldingen(self.GOED.replace("## 6. Samenhang", "## 6. Relaties"))))

    def test_regel_in_hoofdstuk_3_zonder_maatregel(self):
        tekst = vorm("- a [8.13.01, 8.13.02, 8.13.03]\n- los\n  vervolg")
        self.assertTrue(any("regel zonder maatregel" in m and "los" in m for m in meldingen(tekst)), meldingen(tekst))

    def test_regel_buiten_hoofdstuk_3_mag_zonder_maatregel(self):
        self.assertEqual(meldingen(self.GOED.replace("- x", "- x\n  vervolg\n- y")), [])

    def test_geen_controleraamwerk(self):
        self.assertTrue(any("geen controleraamwerk" in m for m in meldingen(vorm("- a [8.13.01, 8.13.02, 8.13.03]", ""))))

    def test_onbekende_afkorting(self):
        self.assertTrue(any("afkorting" in m and "OWASP" in m for m in meldingen(self.GOED.replace("tekst\n", "OWASP\n", 1))))

    def test_controle_id_en_invulveld_zijn_geen_afkorting(self):
        self.assertEqual(meldingen(self.GOED.replace("| CISO | kijkt |", "| [[rol: de ROL]] | kijkt |")), [])


class EchteSet(unittest.TestCase):
    """De set zoals hij in de kennisbank staat."""

    @classmethod
    def setUpClass(cls):
        cls.data = b.laad()

    def test_elke_bouwsteen_dekt_zijn_domein_bij_elk_profiel(self):
        self.assertEqual(b.toets(self.data), [])

    def test_elk_domein_een_bouwsteen(self):
        self.assertEqual(len(self.data["bouwstenen"]), len(self.data["profiel"]["domeinen"]))

    def test_geen_lange_streepjes(self):
        for s in self.data["bouwstenen"]:
            for deel in s["delen"]:
                for r in deel["regels"]:
                    self.assertNotIn("—", r, s["bestand"])
                    self.assertNotIn("–", r, s["bestand"])

    def test_generatorpagina_heeft_instructies_voor_een_ai_assistent_zonder_javascript(self):
        pagina = b.pagina(self.data)
        statisch = pagina.split("<script")[0]  # wat een assistent ziet die geen JavaScript draait
        self.assertIn('id="voor-ai"', statisch)
        self.assertIn(b.LIVE + "profiel.json", statisch)
        self.assertIn(b.LIVE + "beleidsset.json", statisch)
        for s in self.data["bouwstenen"]:
            self.assertIn(b.LIVE + b.bestandsnaam(s), statisch, s["bestand"])
            self.assertIn(b.LIVE + "data/" + s["bestand"], statisch, s["bestand"])
        self.assertNotIn("/*AGENTLIJST*/", pagina)
        self.assertNotIn("—", statisch)

    def test_maatregelkopie_gelijk_aan_normen(self):
        normen = b.ROOT.parent / "normen" / "bio2.json"
        if not normen.exists():
            self.skipTest("normen-repo niet naast de kennisbank; CI vergelijkt niet")
        bron = json.loads(normen.read_text(encoding="utf-8"))
        kopie = self.data["maatregelen"]
        self.assertEqual(kopie["versie"], bron["versie"])
        self.assertEqual(kopie["maatregelen"], [{k: m[k] for k in ("id", "titel", "thema", "soort")} for m in bron["maatregelen"]])


class Spiegel(unittest.TestCase):
    """De generatorpagina rekent in JavaScript; die moet woord voor woord hetzelfde maken."""

    def test_python_en_javascript_gelijk(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("node ontbreekt")
        data = b.laad()
        rnd = random.Random(14102026)
        profielen = [{}]
        for _ in range(40):
            p = {}
            for v in data["profiel"]["vragen"]:
                keuze = rnd.random()
                ids = [a["id"] for a in v["antwoorden"]]
                if keuze < 0.25:
                    continue
                p[v["id"]] = rnd.sample(ids, rnd.randint(1, len(ids))) if v.get("meerdere") else rnd.choice(ids)
            profielen.append(p)
        script = ("const B=require(process.argv[1]);const fs=require('fs');"
                  "const inv=JSON.parse(fs.readFileSync(0,'utf8'));"
                  "process.stdout.write(JSON.stringify(inv.profielen.map(p=>B.genereer(inv.data,p))));")
        uit = subprocess.run([node, "-e", script, str(b.JS)], input=json.dumps({"data": data, "profielen": profielen}),
                             capture_output=True, text=True, encoding="utf-8", check=True).stdout
        js = json.loads(uit)
        for p, j in zip(profielen, js):
            py = b.genereer(data, copy.deepcopy(p))
            for domein in py:
                self.assertEqual(py[domein]["markdown"], j[domein]["markdown"], f"{domein} bij {p}")
                self.assertEqual(py[domein]["gedekt"], j[domein]["gedekt"], f"{domein} bij {p}")


if __name__ == "__main__":
    unittest.main(verbosity=1)
