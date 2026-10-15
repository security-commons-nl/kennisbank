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
import beleidsset_word as word  # noqa: E402

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


KOP = ("---\ndomein: proef\ntitel: Proefbeleid\nsamenvatting: Over proeven.\ninvoeren:\n"
       "  - Richt een proefregister in (hoofdstuk 3).\n---\n\n")


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

    def test_nummering_per_hoofdstuk_ook_in_kader(self):
        tekst = KOP + "## 3. A\n\n- een [8.13.01]\n  vervolg\n- twee [8.13.02]\n\n::: als beheer=eigen\n- drie [8.13.03]\n:::\n\n## 4. B\n\n- een\n"
        d = data_met(tekst)
        md = b.genereer_stuk(d["bouwstenen"][0], d, {})["markdown"]
        self.assertIn("1. een [8.13.01]\n   vervolg\n2. twee [8.13.02]", md)
        self.assertIn("> 3. drie [8.13.03]", md)
        self.assertIn("## 4. B\n\n1. een", md)

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
    """Een bouwsteen in de vaste vorm, met `regels` als inhoud van het onderwerphoofdstuk 3."""
    return (KOP + "## 1. Doel en reikwijdte\n\ntekst\n\n## 2. Uitgangspunten\n\n- x\n\n## 3. Proefonderwerp\n\n"
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

    def test_regel_in_onderwerphoofdstuk_zonder_maatregel(self):
        tekst = vorm("- a [8.13.01, 8.13.02, 8.13.03]\n- los\n  vervolg")
        self.assertTrue(any("regel zonder maatregel" in m and "los" in m for m in meldingen(tekst)), meldingen(tekst))

    def test_regel_buiten_onderwerphoofdstuk_mag_zonder_maatregel(self):
        self.assertEqual(meldingen(self.GOED.replace("- x", "- x\n  vervolg\n- y")), [])

    def test_meer_onderwerpen_elk_eigen_hoofdstuk(self):
        tekst = self.GOED.replace("## 4. Rollen", "## 4. Tweede onderwerp\n\n- b [8.13.01]\n- los\n\n## 5. Rollen")
        tekst = tekst.replace("## 5. Naleving", "## 6. Naleving").replace("## 6. Samenhang", "## 7. Samenhang")
        self.assertTrue(any("hoofdstuk 4" in m and "los" in m for m in meldingen(tekst)), meldingen(tekst))
        self.assertEqual(meldingen(tekst.replace("- los\n", "")), [])

    def test_subkop_en_gaten_in_de_nummering(self):
        sub = self.GOED.replace("## 3. Proefonderwerp", "## 3. Proefonderwerp\n\n### 3.1 Sub")
        self.assertTrue(any("subkop" in m for m in meldingen(sub)))
        self.assertTrue(any("doorlopend" in m for m in meldingen(self.GOED.replace("## 6. Samenhang", "## 7. Samenhang"))))

    def test_zonder_onderwerphoofdstuk(self):
        zonder = self.GOED.split("## 3. Proefonderwerp")[0] + "## 3. Rollen" + self.GOED.split("## 4. Rollen")[1]
        zonder = zonder.replace("## 5. Naleving", "## 4. Naleving").replace("## 6. Samenhang", "## 5. Samenhang")
        self.assertTrue(any("hoofdstukken" in m for m in meldingen(zonder)), meldingen(zonder))

    def test_samenvatting_en_invoeren_verplicht(self):
        self.assertTrue(any("samenvatting" in m for m in meldingen(self.GOED.replace("samenvatting: Over proeven.\n", ""))))
        self.assertTrue(any("invoeren" in m for m in meldingen(self.GOED.replace("(hoofdstuk 3)", "(hoofdstuk 9)"))))
        geen = self.GOED.replace("  - Richt een proefregister in (hoofdstuk 3).\n", "")
        self.assertTrue(any("invoeren" in m for m in meldingen(geen)), meldingen(geen))

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


class AIHulp(unittest.TestCase):
    """De AI-hulp met eigen sleutel: opdrachten als data, de kern gelijk aan procescheck, de pagina dicht."""

    @classmethod
    def setUpClass(cls):
        cls.data = b.laad()
        cls.opdrachten = json.loads((b.AI_MAP / "opdrachten.json").read_text(encoding="utf-8"))
        cls.pagina = b.ai_pagina(cls.data)
        cls.generator = b.pagina(cls.data)

    def test_schemas_zijn_dicht_en_eisen_een_citaat(self):
        def dicht(schema, pad):
            if schema.get("type") == "object":
                self.assertIs(schema.get("additionalProperties"), False, pad)
                for k, sub in schema.get("properties", {}).items():
                    dicht(sub, pad + "." + k)
            if schema.get("type") == "array":
                dicht(schema["items"], pad + "[]")
        for o in self.opdrachten["opdrachten"]:
            dicht(o["schema"], o["id"])
            self.assertIn("onzeker", o["schema"]["required"], o["id"])
            self.assertIn("bronregel", o["schema"]["properties"]["items"]["items"]["required"], o["id"])
            self.assertIn(o["parameter"], ("vragen", "velden"))

    def test_prompts_verzinnen_niets_en_schrijven_geen_beleid(self):
        regels = self.opdrachten["vaste_regels"]
        self.assertIn("Verzin niets", regels)
        self.assertIn("uitsluitend met JSON", regels)
        self.assertIn("Bedenk geen beleidsregels", regels)
        for o in self.opdrachten["opdrachten"]:
            for woord in ("score", "prioriteit", "schrijf beleid"):
                self.assertNotIn(woord, o["systeemprompt"].lower(), o["id"])

    def test_kern_gelijk_aan_procescheck(self):
        bron = b.ROOT.parent / "procescheck" / "ai" / "bron" / "kern.js"
        if not bron.exists():
            self.skipTest("procescheck niet naast de kennisbank; CI draait haal_kern.py --check")
        kopie = (b.AI_MAP / "kern.js").read_bytes().replace(b"\r\n", b"\n")
        self.assertEqual(kopie, bron.read_bytes().replace(b"\r\n", b"\n"))

    def test_pagina_heeft_csp_op_de_hash_van_script_en_stijl(self):
        import re as _re
        csp = _re.search(r'http-equiv="Content-Security-Policy" content="([^"]+)"', self.pagina).group(1)
        script = _re.search(r"<script>(.*)</script>", self.pagina, _re.S).group(1)
        stijl = _re.search(r"<style>(.*)</style>", self.pagina, _re.S).group(1)
        self.assertIn("default-src 'none'", csp)
        self.assertIn("connect-src " + b.CONNECT_SRC, csp)
        self.assertIn("'sha256-" + b.csp_hash(script) + "'", csp)
        self.assertIn("'sha256-" + b.csp_hash(stijl) + "'", csp)
        self.assertEqual(self.pagina.count("<script"), 1)

    def test_sleutel_alleen_in_sessionstorage(self):
        ai = (b.AI_MAP / "ai.js").read_text(encoding="utf-8")
        self.assertIn("sessionStorage.setItem(SLEUTEL_OPSLAG", ai)
        self.assertEqual(ai.count("localStorage.setItem("), 1)
        self.assertIn("localStorage.setItem(LEVERANCIER_OPSLAG", ai)
        self.assertNotIn("console.log", ai)

    def test_generator_praat_met_niemand(self):
        self.assertNotIn("fetch(", self.generator)
        self.assertNotIn("XMLHttpRequest", self.generator)
        self.assertIn('href="beleidsset-ai.html"', self.generator)

    def test_vragen_en_velden_gaan_mee(self):
        data = json.loads(self.pagina.split("window.__OPDRACHTEN__ = ", 1)[1].split(";\n", 1)[0])
        self.assertEqual(len(data["vragen"]), len(self.data["profiel"]["vragen"]))
        namen = [v["naam"] for v in data["velden"]]
        self.assertIn("eigenaar van dit beleid", namen)
        self.assertIn("lijneigenaar fysieke beveiliging", namen)
        self.assertEqual(len(namen), len(set(namen)))
        alles = "".join(s["markdown"] for s in b.genereer(self.data, {}).values())
        for n in namen:
            self.assertIn("**[" + n + "]**", alles, n)


class VulWaarden(unittest.TestCase):
    MD = ("# T\n\nDe **[eigenaar]** doet het en **[eigenaar]** tekent; **[systeem]** logt.\n\n"
          "## Nog in te vullen\n\n- **eigenaar**: de rol\n- **systeem**: het systeem\n")

    def test_vult_in_en_haalt_van_de_lijst(self):
        md = b.vul_waarden(self.MD, {"eigenaar": "manager facilitair", "onbekend": "x"})
        self.assertIn("De manager facilitair doet het en manager facilitair tekent", md)
        self.assertNotIn("- **eigenaar**", md)
        self.assertIn("- **systeem**: het systeem", md)
        self.assertNotIn("Herkomst", md)

    def test_lijst_weg_als_alles_is_ingevuld_en_herkomst_erbij(self):
        md = b.vul_waarden(self.MD, {"eigenaar": "A", "systeem": "B"},
                           {"leverancier": "mistral", "model": "m", "gemaakt": "2026-10-15", "sha256": "abcdef0123456789"})
        self.assertNotIn("Nog in te vullen", md)
        self.assertIn("## Herkomst van ingevulde waarden", md)
        self.assertIn("(mistral, model m, 2026-10-15, invoer sha256 abcdef012345): eigenaar, systeem.", md)

    def test_lege_waarde_vult_niets(self):
        self.assertEqual(b.vul_waarden(self.MD, {"eigenaar": "  "}), self.MD)


class Spiegel(unittest.TestCase):
    def test_vul_waarden_python_en_javascript_gelijk(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("node ontbreekt")
        data = b.laad()
        stukken = b.genereer(data, {})
        velden = [v["naam"] for v in b.invulvelden(data)]
        gevallen = [({velden[0]: "A"}, None), ({n: "waarde " + n for n in velden[:9]},
                    {"leverancier": "mistral", "model": "m", "gemaakt": "2026-10-15", "sha256": "0123456789abcdef"})]
        invoer = [{"md": s["markdown"], "w": w, "h": h} for s in stukken.values() for w, h in gevallen]
        script = ("const B=require(process.argv[1]);const fs=require('fs');"
                  "const inv=JSON.parse(fs.readFileSync(0,'utf8'));"
                  "process.stdout.write(JSON.stringify(inv.map(x=>B.vulWaarden(x.md,x.w,x.h))));")
        uit = json.loads(subprocess.run([node, "-e", script, str(b.JS)], input=json.dumps(invoer), capture_output=True,
                                        text=True, encoding="utf-8", check=True).stdout)
        for x, j in zip(invoer, uit):
            self.assertEqual(b.vul_waarden(x["md"], x["w"], x["h"]), j)

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


    def test_overzichten_en_word_python_en_javascript_gelijk(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("node ontbreekt")
        data = b.laad()
        profielen = [{}, {"beheer": "uitbesteed", "hosting": ["saas"], "werkplek": "cloud"}]
        waarden = {"lijneigenaar back-up": "Hoofd ICT", "eigenaar van dit beleid": "Directeur bedrijfsvoering"}
        script = ("const B=require(process.argv[1]);const W=require(process.argv[2]);const fs=require('fs');"
                  "const inv=JSON.parse(fs.readFileSync(0,'utf8'));"
                  "process.stdout.write(JSON.stringify(inv.profielen.map(p=>{const s=B.genereer(inv.data,p);"
                  "for(const k in s)s[k].markdown=B.vulWaarden(s[k].markdown,inv.waarden,null);"
                  "const o=B.overzichten(inv.data,p,s);const mds=Object.keys(s).map(k=>s[k].markdown).concat([o.maatregelen,o.invoeren]);"
                  "return {o:o,delen:W.delen(mds),zip:Buffer.from(W.docx(mds)).toString('base64')};})));")
        uit = json.loads(subprocess.run([node, "-e", script, str(b.JS), str(b.WORD_JS)],
                                        input=json.dumps({"data": data, "profielen": profielen, "waarden": waarden}),
                                        capture_output=True, text=True, encoding="utf-8", check=True).stdout)
        import base64
        for p, j in zip(profielen, uit):
            stukken = b.genereer(data, copy.deepcopy(p))
            for k in stukken:
                stukken[k]["markdown"] = b.vul_waarden(stukken[k]["markdown"], waarden)
            over = b.overzichten(data, p, stukken)
            self.assertEqual(over, j["o"], p)
            mds = [s["markdown"] for s in stukken.values()] + [over["maatregelen"], over["invoeren"]]
            self.assertEqual(word.delen(mds), dict(j["delen"]), p)
            self.assertTrue(word.zelfde_inhoud(base64.b64decode(j["zip"]), word.docx(mds)), p)

class InHetKort(unittest.TestCase):
    """Bovenaan elk stuk: waar het over gaat en welke onderwerpen het regelt."""

    def test_samenvatting_en_onderwerpen_onder_het_titelblad(self):
        d = data_met(vorm("- a [8.13.01, 8.13.02, 8.13.03]").replace("## 4. Rollen", "## 4. Tweede\n\n- b [8.13.01]\n\n## 5. Rollen")
                     .replace("## 5. Naleving", "## 6. Naleving").replace("## 6. Samenhang", "## 7. Samenhang"))
        md = b.genereer_stuk(d["bouwstenen"][0], d, {})["markdown"]
        self.assertIn("**In het kort.** Over proeven.", md)
        self.assertIn("**Onderwerpen.** 3. Proefonderwerp; 4. Tweede.", md)
        self.assertLess(md.index("| Evaluatie |"), md.index("**In het kort.**"))
        self.assertLess(md.index("**Onderwerpen.**"), md.index("## 1. Doel"))

    def test_echte_set_heeft_bij_elk_stuk_een_samenvatting_en_onderwerpen(self):
        data = b.laad()
        for s, stuk in zip(data["bouwstenen"], b.genereer(data, {}).values()):
            self.assertIn("**In het kort.** " + s["samenvatting"], stuk["markdown"], s["bestand"])
            self.assertIn("**Onderwerpen.** 3. ", stuk["markdown"], s["bestand"])
            self.assertTrue(4 <= len(s["invoeren"]) <= 10, s["bestand"])
            self.assertNotIn("Beleidsregels", stuk["markdown"], s["bestand"])


class Overzichten(unittest.TestCase):
    """Het maatregelenoverzicht over alle stukken en de lijst met wat er moet gebeuren om in te voeren."""

    @classmethod
    def setUpClass(cls):
        cls.data = b.laad()
        cls.stukken = b.genereer(cls.data, {})
        cls.over = b.overzichten(cls.data, {}, cls.stukken)

    def test_elke_maatregel_een_regel_met_stuk_hoofdstuk_en_controle(self):
        rijen = [r for r in self.over["maatregelen"].split("\n") if b.NUMMER.match(r[2:])]
        self.assertEqual(len(rijen), len(self.data["maatregelen"]["maatregelen"]))
        rij = next(r for r in rijen if r.startswith("| 8.13.04 |"))
        self.assertEqual(rij, "| 8.13.04 | Back-up van informatie | overheid | Beleid back-up en recovery | "
                              "7. Herstel en testen | BUR-06, BUR-07 |  |")
        for r in rijen:
            self.assertNotIn("niet ingevuld", r)
            self.assertNotIn("| geen |", r)

    def test_ook_in_noemt_de_andere_stukken(self):
        # testgegevens horen bij wijzigingsbeheer en komen ook terug in veilige softwareontwikkeling
        rij = next(r for r in self.over["maatregelen"].split("\n") if r.startswith("| 8.33.01 |"))
        ook = [s["titel"] for s in self.data["bouwstenen"] if s["domein"] != "wijzigingsbeheer"
               and "8.33.01" in self.stukken[s["domein"]]["waar"]]
        self.assertTrue(ook)
        self.assertTrue(rij.endswith(" | " + ", ".join(ook) + " |"), rij)

    def test_invoeren_per_stuk_inrichten_controles_en_velden(self):
        v = self.over["invoeren"]
        self.assertIn("## Voor de hele set", v)
        for nr, s in enumerate(self.data["bouwstenen"], 1):
            self.assertIn(f"## {nr}. {s['titel']}", v)
            for a in s["invoeren"]:
                self.assertIn("- " + a, v)
        self.assertIn("| BUR-01 | Alle back-uptaken", v)
        controles = sum(len([r for r in st["markdown"].split("\n") if b.RIJ.match(r)]) for st in self.stukken.values())
        self.assertEqual(len([r for r in v.split("\n") if b.RIJ.match(r)]), controles)
        self.assertIn("lijneigenaar back-up", v)

    def test_ingevulde_velden_verdwijnen_uit_de_invoerlijst(self):
        stukken = b.genereer(self.data, {})
        for k in stukken:
            stukken[k]["markdown"] = b.vul_waarden(stukken[k]["markdown"], {"lijneigenaar back-up": "Hoofd ICT"})
        v = b.overzichten(self.data, {}, stukken)["invoeren"]
        deel = v.split("Beleid back-up en recovery")[1].split("\n## ")[0]
        self.assertNotIn("lijneigenaar back-up", deel.split("**Nog in te vullen")[1])
        self.assertIn("| Hoofd ICT |", deel)

    def test_profiel_staat_bovenaan(self):
        over = b.overzichten(self.data, {"beheer": "uitbesteed"}, b.genereer(self.data, {"beheer": "uitbesteed"}))
        self.assertIn("Opgesteld voor dit profiel: ", over["maatregelen"])
        self.assertIn("Zonder profiel", self.over["invoeren"])

    def test_leesversies_en_word_bestanden_staan_in_de_kennisbank(self):
        uit = b.uitvoer(self.data)
        for naam in list(b.OVERZICHTEN.values()) + [b.bestandsnaam(s)[:-3] for s in self.data["bouwstenen"]]:
            self.assertIn(b.ITEM / f"{naam}.md", uit)
            self.assertIn(b.ITEM / f"{naam}.docx", uit)
            self.assertIn(f"[Download als Word]({naam}.docx)", uit[b.ITEM / f"{naam}.md"])
        self.assertIn(b.ITEM / b.SET_DOCX, uit)


class Word(unittest.TestCase):
    """Het Word-bestand: geldige zip, de vaste stijlen, en wat de markdown zegt."""

    MD = ("# Titel\n\n| | |\n|---|---|\n| Status | Concept |\n\nEen **vet** en *schuin* woord en een "
          "[link](https://x.nl).\n\n## 3. Onderwerp\n\n1. een [8.13.01]\n   vervolg\n2. twee\n\n"
          "> **Alleen als: vraag «ja»**\n>\n> 3. drie\n\n- los\n")

    def test_onderdelen_en_stijlen(self):
        xml = word.document_xml([self.MD])
        self.assertIn('<w:pStyle w:val="Title"/></w:pPr><w:r><w:t xml:space="preserve">Titel</w:t></w:r>', xml)
        self.assertIn('<w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t xml:space="preserve">3. Onderwerp</w:t>', xml)
        self.assertIn('<w:t xml:space="preserve">1.</w:t></w:r><w:r><w:tab/></w:r><w:r><w:t xml:space="preserve">een [8.13.01] vervolg</w:t>', xml)
        self.assertIn('<w:pStyle w:val="Kader"/></w:pPr><w:r><w:rPr><w:b/></w:rPr><w:t xml:space="preserve">Alleen als: vraag «ja»</w:t>', xml)
        self.assertIn('<w:pStyle w:val="Kaderlijst"/></w:pPr><w:r><w:t xml:space="preserve">3.</w:t>', xml)
        self.assertIn('<w:t xml:space="preserve">\u2022</w:t>', xml)
        self.assertIn('<w:t xml:space="preserve">link</w:t></w:r><w:r><w:t xml:space="preserve"> (https://x.nl)</w:t>', xml)
        self.assertNotIn("<w:tblHeader/>", xml)  # de lege kopregel van het titelblad valt weg
        for stijl in ("Title", "Heading1", "Lijst", "Kader", "Kaderlijst", "Tabel", "Tabeltekst"):
            self.assertIn(f'w:styleId="{stijl}"', word.STYLES)

    def test_geldige_zip_met_vaste_inhoud(self):
        import io
        import zipfile
        een, twee = word.docx([self.MD, self.MD]), word.docx([self.MD, self.MD])
        z = zipfile.ZipFile(io.BytesIO(een))
        self.assertIsNone(z.testzip())
        self.assertEqual(z.namelist()[0], "[Content_Types].xml")
        self.assertEqual(z.read("word/document.xml").decode("utf-8").count('w:type="page"'), 1)
        self.assertTrue(word.zelfde_inhoud(een, twee))
        self.assertFalse(word.zelfde_inhoud(een, word.docx([self.MD])))

    def test_tekens_worden_ontsnapt(self):
        xml = word.document_xml(["Kosten < 5 & meer > 2 \"x\""])
        self.assertIn("Kosten &lt; 5 &amp; meer &gt; 2 &quot;x&quot;", xml)

if __name__ == "__main__":
    unittest.main(verbosity=1)
