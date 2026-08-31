#!/usr/bin/env python3
"""Kondigt een nieuw kennisbankitem aan in Discussions van de organisatie.

De aankondiging wordt niet geschreven maar afgeleid: titel, samenvatting, vakgebied, type en barrieres
staan al verplicht in de frontmatter (statuut B2) en zijn door `build.py` gecontroleerd. Wat gepubliceerd
is, is dus ook wat er in de aankondiging staat. Dat scheelt een tweede tekst die kan gaan afwijken.

Gebruik:
    python tools/aankondigen.py bcm/kritieke-processen-vaststellen --toon
    python tools/aankondigen.py bcm/kritieke-processen-vaststellen bcm/ander-item
    python tools/aankondigen.py --nieuw-sinds HEAD~1 --toon

`--toon` schrijft de aankondiging naar het scherm en plaatst niets. Doe dat eerst.

Het token komt uit `AANKONDIG_TOKEN` (in een workflow) of anders uit de git-credential-helper (lokaal).
Een gewoon workflow-token werkt niet: dat mag alleen in zijn eigen repo, en de aankondiging landt in
`.github`.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://security-commons-nl.github.io/kennisbank"
ORG, PROFIEL_REPO, CATEGORIE = "security-commons-nl", ".github", "Aankondigingen"

_spec = importlib.util.spec_from_file_location("build", Path(__file__).resolve().parent / "build.py")
_build = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_build)


def token() -> str:
    uit_omgeving = os.environ.get("AANKONDIG_TOKEN")
    if uit_omgeving:
        return uit_omgeving
    gevuld = subprocess.run(["git", "credential", "fill"], input="protocol=https\nhost=github.com\n\n",
                            capture_output=True, text=True, check=True).stdout
    for regel in gevuld.splitlines():
        if regel.startswith("password="):
            return regel[len("password="):]
    sys.exit("geen token: zet AANKONDIG_TOKEN of log in met git")


def graphql(query: str, variabelen: dict) -> dict:
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variabelen}).encode(),
        headers={"Authorization": f"bearer {token()}", "User-Agent": "aankondigen",
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        antwoord = json.loads(r.read())
    if "errors" in antwoord:
        sys.exit("GraphQL-fout: " + json.dumps(antwoord["errors"], ensure_ascii=False))
    return antwoord["data"]


def nieuw_sinds(basis: str) -> list[str]:
    """Itemmappen die sinds `basis` zijn toegevoegd. Alleen toevoegingen, geen wijzigingen.

    Een wijziging aankondigen maakt het kanaal ruis, en dan klikt niemand meer op een aankondiging.
    """
    uit = subprocess.run(["git", "diff", "--name-only", "--diff-filter=A", basis, "HEAD"],
                         cwd=ROOT, capture_output=True, text=True, check=True).stdout
    items = []
    for regel in uit.splitlines():
        delen = regel.split("/")
        if len(delen) == 3 and delen[2] == "README.md" and delen[0] in _build.VAKGEBIEDEN:
            items.append(f"{delen[0]}/{delen[1]}")
    return sorted(set(items))


def aankondiging(item: str) -> tuple[str, str]:
    readme = ROOT / item / "README.md"
    if not readme.is_file():
        sys.exit(f"{readme} bestaat niet")
    fm, _ = _build.lees_frontmatter(readme.read_text(encoding="utf-8"))
    if not fm:
        sys.exit(f"{readme}: geen frontmatter gevonden")

    vak, naam = item.split("/", 1)
    url = f"{SITE}/{vak}/{naam}/"
    titel = f"Nieuw in de kennisbank: {fm['titel']}"

    regels = [f"**{fm['titel']}** staat vanaf nu in de kennisbank, onder {vak}.", "",
              str(fm["samenvatting"]).strip(), "", f"Lees het hier: {url}", ""]

    feiten = [f"soort: {fm['type']}", f"status: {fm['status']}"]
    if fm.get("normen"):
        feiten.append("normen: " + ", ".join(fm["normen"]))
    regels.append("*" + " · ".join(feiten) + "*")

    if fm.get("barrieres"):
        bekend = _build.barrieres()
        namen = ", ".join(bekend.get(b, b) for b in fm["barrieres"])
        rol = fm.get("rol")
        zin = f"Hangt aan de zelfcheck bij: {namen}"
        if rol:
            zin += f", als {rol}"
        regels += ["", zin + "."]

    regels += ["", "---", "",
               "Werkt dit bij jou, of moest je het aanpassen? Dat horen we graag in "
               "*Hoe ging het bij jou?*. Mis je iets, stel dan een vraag in "
               "*Hulpvraag uit de praktijk*; je naam en je organisatie hoeven daar niet bij."]
    return titel, "\n".join(regels)


VRAAG_IDS = """
query($org:String!, $repo:String!) { repository(owner:$org, name:$repo) {
  id discussionCategories(first:25) { nodes { id name } } } }
"""
MAAK = """
mutation($repo:ID!, $cat:ID!, $titel:String!, $tekst:String!) {
  createDiscussion(input:{repositoryId:$repo, categoryId:$cat, title:$titel, body:$tekst}) {
    discussion { number url } } }
"""


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("items", nargs="*", help="itemmappen, bijvoorbeeld bcm/kritieke-processen-vaststellen")
    p.add_argument("--nieuw-sinds", metavar="COMMIT", help="leid de items af uit wat er sinds COMMIT is toegevoegd")
    p.add_argument("--toon", action="store_true", help="alleen tonen, niets plaatsen")
    a = p.parse_args()

    items = list(a.items)
    if a.nieuw_sinds:
        items += nieuw_sinds(a.nieuw_sinds)
    items = sorted(set(items))
    if not items:
        print("Geen nieuwe items; niets aan te kondigen.")
        return 0

    opgesteld = [(item, *aankondiging(item)) for item in items]

    if a.toon:
        for item, titel, tekst in opgesteld:
            print("=" * 90)
            print(f"[{item}]  {titel}")
            print("-" * 90)
            print(tekst)
            print()
        print(f"{len(opgesteld)} aankondiging(en) opgesteld, niets geplaatst (--toon).")
        return 0

    data = graphql(VRAAG_IDS, {"org": ORG, "repo": PROFIEL_REPO})["repository"]
    cats = {c["name"]: c["id"] for c in data["discussionCategories"]["nodes"]}
    if CATEGORIE not in cats:
        sys.exit(f"categorie '{CATEGORIE}' bestaat niet in {ORG}/{PROFIEL_REPO}: {sorted(cats)}")

    for item, titel, tekst in opgesteld:
        d = graphql(MAAK, {"repo": data["id"], "cat": cats[CATEGORIE], "titel": titel, "tekst": tekst})
        print(f"  {item} -> {d['createDiscussion']['discussion']['url']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
