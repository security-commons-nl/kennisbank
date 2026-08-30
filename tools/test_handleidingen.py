"""Tests voor het type handleiding en de export van het handelingsperspectief.

Apart van test_build.py omdat het een eigen onderwerp is: de koppeling tussen de kennisbank en de
barrieres uit paden.json. Draai beide:

    python tools/test_build.py
    python tools/test_handleidingen.py
"""
from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("build", Path(__file__).resolve().parent / "build.py")
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)

FM = """---
titel: Richt centrale logverzameling in
vakgebied: security
type: {type}
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus, herschreven als handleiding
status: concept
samenvatting: Logs van systemen, applicaties en netwerk centraal verzamelen en bewaren, zodat je bij een incident zicht en bewijs hebt. Met de stappen, de kosten en het bewijs dat je aan het eind kunt laten zien.
{extra}---

# Richt centrale logverzameling in

{body}
"""

BODY = """## Wanneer wel, wanneer niet

Altijd zinvol; dit is de fundering onder elke vorm van detectie.

## Bewijs

Een export waaruit blijkt welke bronnen aangesloten zijn, met de retentietermijn erbij.

## Zo leg je het uit

**Aan de directie.** Zonder centrale logverzameling is er bij een incident geen zicht en geen bewijs.
"""


class Basis(unittest.TestCase):
    def setUp(self) -> None:
        build.fouten.clear()
        self.map = Path(tempfile.mkdtemp())
        self.oude_root, build.ROOT = build.ROOT, self.map
        # De barrieres komen normaal uit paden.json; hier zetten we ze vast, zodat de test niet
        # afhangt van een repo die er wel of niet naast staat.
        self.oude_cache = build._barrieres_cache
        build._barrieres_cache = {"soc": "Borg 24/7 opvolging en escalatie van kritieke meldingen",
                                  "pr": "Dwing phishingbestendige authenticatie af"}

    def tearDown(self) -> None:
        build.ROOT = self.oude_root
        build._barrieres_cache = self.oude_cache
        build.fouten.clear()

    @property
    def meldingen(self) -> str:
        return "\n".join(build.fouten)


class Handleiding(Basis):
    """Een handleiding hoort bij een barriere en zegt welk bewijs hij oplevert."""

    def maak(self, *, type_="handleiding", extra="barrieres: [soc]\nrol: fundering\n", body=BODY):
        map_ = self.map / "security" / "centrale-logverzameling"
        map_.mkdir(parents=True)
        (map_ / "README.md").write_text(FM.format(type=type_, extra=extra, body=body), encoding="utf-8")
        (map_ / "index.html").write_text("<html><body><h1>x</h1></body></html>", encoding="utf-8")
        return build.controleer_item("security", map_)

    def test_geldige_handleiding_geeft_geen_melding(self):
        self.maak()
        self.assertEqual(self.meldingen, "")

    def test_zonder_barrieres_is_een_fout(self):
        self.maak(extra="")
        self.assertIn("barrieres", self.meldingen)

    def test_onbekende_barriere_is_een_fout(self):
        self.maak(extra="barrieres: [bestaatniet]\n")
        self.assertIn("bestaat niet in paden.json", self.meldingen)

    def test_zonder_bewijskop_is_een_fout(self):
        zonder = BODY.replace("## Bewijs\n\nEen export waaruit blijkt welke bronnen aangesloten zijn, met de retentietermijn erbij.\n\n", "")
        self.maak(body=zonder)
        self.assertIn("Bewijs", self.meldingen)

    def test_zonder_uitlegkop_is_een_fout(self):
        zonder = BODY.split("## Zo leg je het uit")[0]
        self.maak(body=zonder)
        self.assertIn("Zo leg je het uit", self.meldingen)

    def test_onbekende_rol_is_een_fout(self):
        self.maak(extra="barrieres: [soc]\nrol: hoofdgerecht\n")
        self.assertIn("rol", self.meldingen)

    def test_barrieres_bij_een_ander_type_is_een_fout(self):
        self.maak(type_="aanpak", extra="barrieres: [soc]\n")
        self.assertIn("alleen bij type handleiding", self.meldingen)

    def test_pijler_moet_bestaan(self):
        self.maak(extra="barrieres: [soc]\npijler: bestaat-niet\n")
        self.assertIn("pijler", self.meldingen)

    def test_zonder_padenjson_meldt_de_ontbrekende_bron(self):
        build._barrieres_cache = {}
        self.maak()
        self.assertIn("paden.json niet gevonden", self.meldingen)


class Export(Basis):
    """handelingsperspectief.json: de kennisbank is de bron, aanvalspaden de afnemer."""

    def fm(self, naam: str, rol: str) -> dict:
        return {"titel": naam, "type": "handleiding", "barrieres": ["soc"], "rol": rol,
                "_map": self.map / "security" / naam, "_vak": "security"}

    def data(self) -> dict:
        return json.loads((self.map / "handelingsperspectief.json").read_text(encoding="utf-8"))

    def test_elke_handleiding_krijgt_een_regel_per_barriere(self):
        items = {v: [] for v in build.VAKGEBIEDEN}
        items["security"] = [self.fm("mdr-dienst", "alternatief"), self.fm("centrale-logverzameling", "fundering")]
        build.schrijf_handelingsperspectief(items)
        d = self.data()
        self.assertEqual(len(d["handleidingen"]), 2)
        self.assertEqual([h["rol"] for h in d["handleidingen"]], ["fundering", "alternatief"],
                         "de fundering hoort bovenaan te staan, daarna de alternatieven")
        self.assertEqual(d["zonder_handleiding"], ["pr"])

    def test_de_url_wijst_naar_de_site(self):
        items = {v: [] for v in build.VAKGEBIEDEN}
        items["security"] = [self.fm("centrale-logverzameling", "fundering")]
        build.schrijf_handelingsperspectief(items)
        self.assertEqual(self.data()["handleidingen"][0]["url"],
                         f"{build.SITE}/security/centrale-logverzameling/")

    def test_zonder_handleidingen_staat_elke_barriere_open(self):
        build.schrijf_handelingsperspectief({v: [] for v in build.VAKGEBIEDEN})
        d = self.data()
        self.assertEqual(d["handleidingen"], [])
        self.assertEqual(sorted(d["zonder_handleiding"]), ["pr", "soc"])


class GeenDodeVerwijzingen(unittest.TestCase):
    """Geen enkele pagina verwijst nog naar een gearchiveerde repo.

    Draait op de echte kennisbank, niet op een tijdelijke map: dit gaat over de inhoud die live staat.
    """

    @unittest.expectedFailure  # Taak 2 repareert de laatste verwijzing; daarna deze regel weghalen.
    def test_geen_link_naar_gearchiveerde_repos(self):
        root = Path(__file__).resolve().parent.parent
        fout = []
        for vak in build.VAKGEBIEDEN:
            for pad in (root / vak).rglob("*"):
                if pad.suffix not in (".md", ".html"):
                    continue
                tekst = pad.read_text(encoding="utf-8", errors="replace")
                for weg in ("github.io/Handelingsperspectief", "security-commons-nl/Handelingsperspectief"):
                    if weg in tekst:
                        fout.append(f"{pad.relative_to(root)} -> {weg}")
        self.assertEqual(fout, [], "verwijzing naar een gearchiveerde repo; vervang die door de opvolger")


if __name__ == "__main__":
    unittest.main(verbosity=2)
