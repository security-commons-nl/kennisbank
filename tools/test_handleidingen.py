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

    def test_barrieres_bij_een_aanpak_mag(self):
        # De passkeys-aanpak en de Security Annex richten net zo goed een maatregel in; alleen de vorm
        # verschilt. Het type blijft dan zeggen wat de lezer krijgt, dus de koppen Bewijs en Zo leg je
        # het uit blijven een eis voor alleen de handleiding.
        self.maak(type_="aanpak", extra="barrieres: [soc]\nrol: fundering\n")
        self.assertEqual("", self.meldingen)

    def test_barrieres_bij_een_beleidsstuk_is_een_fout(self):
        self.maak(type_="beleid", extra="barrieres: [soc]\n")
        self.assertIn("veld 'barrieres' hoort bij type", self.meldingen)

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


class Pijler(Basis):
    """Een pijler toont zijn stukken, een stuk toont zijn pijler.

    Zonder deze weergave bestaat het verband alleen in de frontmatter, en dan komt geen enkele lezer
    het ooit tegen. Dat was precies de reden om het te bouwen.
    """

    def fm(self, naam: str, **extra) -> dict:
        basis = {"titel": naam.replace("-", " ").capitalize(), "type": "handleiding",
                 "status": "concept", "samenvatting": "Kort.", "_vak": "security",
                 "_map": self.map / "security" / naam, "_link": f"{naam}/", "_weergave": "live"}
        basis.update(extra)
        return basis

    def schrijf_pijler(self, mapnaam: str, titel: str) -> None:
        map_ = self.map / "security" / mapnaam
        map_.mkdir(parents=True, exist_ok=True)
        (map_ / "README.md").write_text(f"---\ntitel: {titel}\n---\n\n# {titel}\n", encoding="utf-8")

    def test_een_stuk_toont_bij_welke_pijler_het_hoort(self):
        self.schrijf_pijler("meten-voordat-je-ingrijpt", "Meten voordat je ingrijpt")
        build._pijlertitels.clear()
        regel = build.meta_regel(self.fm("werkplekanalyse-e5", pijler="meten-voordat-je-ingrijpt"), False)
        self.assertIn("hoort bij: Meten voordat je ingrijpt", regel,
                      "de titel van de pijler, niet de mapnaam")

    def test_zonder_pijler_geen_label(self):
        self.assertNotIn("hoort bij", build.meta_regel(self.fm("los-stuk"), False))

    def test_kinderen_staan_in_de_redactionele_volgorde(self):
        # De lijst komt binnen zoals main hem na zet_op_volgorde heeft: dat is de volgorde uit
        # README.md. Alfabetisch sorteren zou hier b voor a zetten.
        items = [self.fm("zzz-eerst", pijler="p"), self.fm("aaa-later", pijler="p"),
                 self.fm("ander-stuk", pijler="andere-pijler"), self.fm("zonder-pijler")]
        self.assertEqual([fm["_map"].name for fm in build.kinderen_van("p", items)],
                         ["zzz-eerst", "aaa-later"])

    def test_een_pijler_zonder_kinderen_krijgt_geen_leeg_blok(self):
        html = "<body><h1>Titel</h1><p>Tekst.</p></body>"
        self.assertEqual(build.zet_pijlerblok(html, []), html)

    def test_het_blok_komt_onder_de_titel_en_stapelt_niet(self):
        html = "<body><h1>Titel</h1><p>Tekst.</p></body>"
        kinderen = [self.fm("werkplekanalyse-e5", rol="fundering")]
        een = build.zet_pijlerblok(html, kinderen)
        self.assertIn("</h1><!-- pijler-kinderen -->", een, "het blok hoort direct onder de titel")
        self.assertIn("../werkplekanalyse-e5/", een)
        self.assertIn("fundering", een)
        twee = build.zet_pijlerblok(een, kinderen)
        self.assertEqual(een, twee, "opnieuw bouwen mag het blok niet stapelen")
        self.assertEqual(twee.count(build.PIJLER_START), 1)

    def test_het_blok_verdwijnt_als_het_laatste_kind_weg_is(self):
        html = "<body><h1>Titel</h1><p>Tekst.</p></body>"
        met = build.zet_pijlerblok(html, [self.fm("werkplekanalyse-e5", rol="fundering")])
        self.assertEqual(build.zet_pijlerblok(met, []), html,
                         "een leeg kader blijven tonen is erger dan geen kader")


class GeenDodeVerwijzingen(unittest.TestCase):
    """Geen enkele pagina verwijst nog naar een gearchiveerde repo.

    Draait op de echte kennisbank, niet op een tijdelijke map: dit gaat over de inhoud die live staat.
    """

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
