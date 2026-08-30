#!/usr/bin/env python3
"""Kennisbank: controleer het redactiestatuut en genereer de indexpagina's.

Gebruik:  python tools/build.py            (controleren + bouwen)
          python tools/build.py --check    (alleen controleren)

Regels: https://github.com/security-commons-nl/.github/blob/main/REDACTIESTATUUT.md
Elke melding noemt het regelnummer (A1..A10, B1..B7). Bij één of meer fouten stopt het
script met exitcode 1 en wordt er niets geschreven.

Alleen standaardbibliotheek; geen pip nodig.
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://security-commons-nl.github.io/kennisbank"
REPO = "https://github.com/security-commons-nl/kennisbank"
HOOFDPAGINA = "https://security-commons-nl.github.io/"

# Kruimelpad (statuut B10). In de gegenereerde indexpagina's zit het in de opmaak; in een
# item-leesversie wordt het tussen deze markeringen gezet, zodat herhaald bouwen niets stapelt.
KRUIMEL_START = "<!-- kruimelpad -->"
INHOUD_START = "<!-- inhoudsopgave -->"
INHOUD_EIND = "<!-- /inhoudsopgave -->"
# Vanaf hier is scrollen zonder overzicht vervelend; korte stukken krijgen geen inhoudsopgave.
INHOUD_VANAF_WOORDEN = 2500
KRUIMEL_EIND = "<!-- /kruimelpad -->"
# Bronvoet (statuut B10): de regel onderaan een leesversie die naar de bronbestanden wijst.
BRON_START = "<!-- bronvoet -->"
BRON_EIND = "<!-- /bronvoet -->"

VAKGEBIEDEN = ["security", "privacy", "bcm", "governance"]
TYPES = ["beleid", "sjabloon", "lesmateriaal", "dataset", "referentie", "aanpak", "rapportage", "handleiding"]
STATUSSEN = ["concept", "in gebruik", "sjabloon", "gearchiveerd"]
VERPLICHT = ["titel", "vakgebied", "type", "normen", "herkomst", "status", "samenvatting"]
TOEGESTAAN = set(VERPLICHT) | {"peildatum", "versie", "licentie", "barrieres", "rol", "pijler"}
ROLLEN = ["fundering", "alternatief", "verdieping"]
# Types die aan een barriere uit de zelfcheck mogen hangen. Een handleiding moet het, een aanpak of
# sjabloon mag het: die richten net zo goed een maatregel in, alleen in een andere vorm.
MET_BARRIERES = {"handleiding", "aanpak", "sjabloon"}
NL = chr(10)

# Mappen die op de root mogen staan naast de vakgebieden. Alles wat met een punt begint is
# tooling (.git, .pytest_cache, .venv) en telt nooit als inhoud.
ROOT_MAPPEN_OK = {".github", "tools", "_aanvalspaden"}
ROOT_BESTANDEN_OK = {"README.md", "CONTRIBUTING.md", "ROADMAP.md", "LICENSE", "index.html", ".gitignore",
                     ".nojekyll", "handelingsperspectief.json"}

# De barrieres komen uit paden.json in de aanvalspaden-repo. Lokaal staat die ernaast; in CI wordt hij
# naar _aanvalspaden uitgecheckt. Een handleiding mag alleen naar een barriere verwijzen die bestaat,
# anders belooft de site een koppeling die nergens op uitkomt.
PADEN_KANDIDATEN = (ROOT.parent / "aanvalspaden" / "paden.json", ROOT / "_aanvalspaden" / "paden.json")
_barrieres_cache: dict[str, str] | None = None


def barrieres() -> dict[str, str]:
    """vraag_id -> titel, uit paden.json. Leeg als het bestand nergens staat; de aanroeper meldt dat."""
    global _barrieres_cache
    if _barrieres_cache is not None:
        return _barrieres_cache
    for pad in PADEN_KANDIDATEN:
        if pad.is_file():
            data = json.loads(pad.read_text(encoding="utf-8"))
            uit: dict[str, str] = {}
            for blad in data["bladeren"]:
                for cp in blad["chokepoints"]:
                    uit.setdefault(cp["vraag_id"], cp["titel"])
            for rv in data.get("randvoorwaarden", []):
                uit.setdefault(rv["vraag_id"], rv["titel"])
            _barrieres_cache = uit
            return uit
    _barrieres_cache = {}
    return _barrieres_cache

SOCIALE_MEDIA = re.compile(r"https?://(?:[a-z0-9-]+\.)*(linkedin\.com|x\.com|twitter\.com|substack\.com|medium\.com|facebook\.com|instagram\.com|threads\.net|tiktok\.com)", re.I)
EMAIL = re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b")
EMAIL_PLACEHOLDER = re.compile(r"^[A-Z0-9_.-]+@[A-Z0-9_.-]+\.[a-z]{2,}$")  # AI@REGIO.nl: placeholder in kapitalen
# Functiepostbussen van organisaties mogen (A3); een adres dat op een persoon lijkt niet (A2).
EMAIL_PERSOON = re.compile(r"^[a-z]+[._-][a-z]+@|^[a-z]{2,}\d*@(gmail|hotmail|outlook|live|icloud|yahoo|proton|kpn|ziggo|xs4all)\.", re.I)
VERBODEN_ZINNEN = [
    (re.compile(r"\baangedragen door\b", re.I), "A1"),
    (re.compile(r"\bopgenomen op \d", re.I), "A6"),
    (re.compile(r"\bgevonden op \d", re.I), "A6"),
    (re.compile(r"\bgevonden \d{2}-\d{2}-\d{4}", re.I), "A6"),
    (re.compile(r"^##+\s*auteurs?\s*$", re.I | re.M), "A1"),
]
DATUM = re.compile(r"^\d{4}-\d{2}(-\d{2})?$")
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

fouten: list[str] = []


def fout(pad: Path | str, regel: str, tekst: str) -> None:
    rel = pad.relative_to(ROOT) if isinstance(pad, Path) else pad
    fouten.append(f"[{regel}] {rel}: {tekst}")


# ----------------------------------------------------------------------------- frontmatter
def lees_frontmatter(tekst: str) -> tuple[dict | None, str]:
    """Minimale YAML-lezer: 'sleutel: waarde', lijsten als '- x' of '[a, b]'."""
    if not tekst.startswith("---\n"):
        return None, tekst
    einde = tekst.find("\n---", 4)
    if einde < 0:
        return None, tekst
    blok = tekst[4:einde]
    body = tekst[einde + 4:].lstrip("\n")
    data: dict = {}
    sleutel = None
    for regel in blok.split("\n"):
        if not regel.strip() or regel.lstrip().startswith("#"):
            continue
        if regel.startswith((" ", "\t")) and regel.strip().startswith("- ") and sleutel:
            data.setdefault(sleutel, [])
            if not isinstance(data[sleutel], list):
                data[sleutel] = []
            data[sleutel].append(regel.strip()[2:].strip().strip('"\''))
            continue
        if ":" not in regel:
            continue
        sleutel, _, waarde = regel.partition(":")
        sleutel = sleutel.strip()
        waarde = waarde.split(" #")[0].strip()
        if waarde.startswith("[") and waarde.endswith("]"):
            binnen = waarde[1:-1].strip()
            data[sleutel] = [w.strip().strip('"\'') for w in binnen.split(",")] if binnen else []
        elif waarde == "":
            data[sleutel] = []
        else:
            data[sleutel] = waarde.strip('"\'')
    return data, body


# ----------------------------------------------------------------------------- controles
def controleer_tekst(pad: Path) -> None:
    tekst = pad.read_text(encoding="utf-8", errors="replace")
    for nr, regel in enumerate(tekst.split("\n"), 1):
        for m in SOCIALE_MEDIA.finditer(regel):
            fout(pad, "A5", f"r.{nr}: link naar sociale media ({m.group(1)}); maak er tekst van zonder link")
        for m in EMAIL.finditer(regel):
            adres = m.group(0)
            if EMAIL_PLACEHOLDER.match(adres) or "[" in regel[max(0, m.start() - 2):m.end() + 2]:
                continue  # placeholder in kapitalen of tussen [ ]
            if EMAIL_PERSOON.search(adres):
                fout(pad, "A2", f"r.{nr}: e-mailadres '{adres}' lijkt van een persoon; vervang door functie of placeholder")
    for patroon, regelnr in VERBODEN_ZINNEN:
        for m in patroon.finditer(tekst):
            nr = tekst.count("\n", 0, m.start()) + 1
            fout(pad, regelnr, f"r.{nr}: '{m.group(0).strip()}' hoort hier niet (zie statuut {regelnr})")
    if "<a " in tekst and pad.suffix == ".html":
        # geneste anchors: <a ...> ... <a ...> zonder tussenliggende </a>
        for m in re.finditer(r"<a\b[^>]*>(?:(?!</a>).)*?<a\b", tekst, re.S):
            nr = tekst.count("\n", 0, m.start()) + 1
            fout(pad, "B4", f"r.{nr}: geneste <a>; een kaart of link mag geen link bevatten")


# Een verwijzing in markdown: [tekst](doel). En in HTML: href="doel".
LINK_MD = re.compile(r"\]\(([^)\s]+)\)")
LINK_HTML = re.compile(r'href="([^"]+)"')


def links_in(pad: Path) -> set[str]:
    tekst = pad.read_text(encoding="utf-8", errors="replace")
    patroon = LINK_HTML if pad.suffix == ".html" else LINK_MD
    return {m.group(1) for m in patroon.finditer(tekst)}


def bereikbaar(doel: str, links: set[str]) -> bool:
    """Telt een doel als gelinkt? Ook als de link naar een anker in dat bestand wijst."""
    return any(link == doel or link.startswith(doel + "#") for link in links)


def controleer_bestandslinks(map_: Path, readme: Path) -> None:
    """Statuut B3: wat naast de README in de map staat, is bereikbaar vanaf de README en de pagina.

    De README is de bron, de leesversie is wat een lezer op de site ziet. Noemt die een bijlage
    alleen als code, dan staat het bestand er wel maar kan niemand erbij. Dat overkwam de pptx van
    de awareness-sessie: de hele inhoud van het item, nergens klikbaar.
    """
    pagina_pad = map_ / "index.html"
    bronnen = [readme] + ([pagina_pad] if pagina_pad.exists() else [])
    links = {pad: links_in(pad) for pad in bronnen}
    for bestand in sorted(map_.rglob("*")):
        if not bestand.is_file() or bestand.name.startswith("."):
            continue
        rel = bestand.relative_to(map_).as_posix()
        if rel in ("README.md", "index.html"):
            continue
        for pad in bronnen:
            if not bereikbaar(rel, links[pad]):
                waar = "de README" if pad.suffix == ".md" else "de leesversie"
                fout(pad, "B3", f"'{rel}' staat in de map maar nergens als link in {waar}; "
                                "op de site kan een lezer er dan niet bij")


def controleer_dode_links(map_: Path) -> None:
    """Statuut B3: een link naar een bestand in de kennisbank wijst naar iets dat bestaat.

    Hernoemen is de valkuil: de README werd bijgewerkt, de leesversie niet, en de pagina hield een
    link naar een bestandsnaam die niet meer bestond.
    """
    for pad in sorted(map_.glob("*.md")) + sorted(map_.glob("*.html")):
        for doel in sorted(links_in(pad)):
            kaal = doel.split("#")[0].split("?")[0]
            if not kaal or kaal.startswith(("http://", "https://", "mailto:", "data:")):
                continue
            if kaal.startswith("/"):
                continue  # wortel van de site, niet van deze repo (bijvoorbeeld /favicon.svg)
            plek = (pad.parent / kaal).resolve()
            if not plek.exists():
                fout(pad, "B3", f"link naar '{doel}' wijst naar een bestand dat niet bestaat")
            elif ROOT not in plek.parents and plek != ROOT:
                fout(pad, "B3", f"link naar '{doel}' wijst buiten de kennisbank; "
                                "op de site loopt dat dood")


def controleer_handleiding(vak: str, readme: Path, fm: dict) -> None:
    """Een handleiding hoort bij een barriere en zegt welk bewijs hij oplevert.

    Zonder `barrieres:` is een handleiding niet vindbaar vanaf de zelfcheck, en dat is precies waarvoor
    hij bestaat. Zonder de kop Bewijs mist de lezer wat hij aan het eind kan laten zien; dat is de
    scheidslijn tussen een antwoord en bewijs die de hele keten aanhoudt.

    Een aanpak of een sjabloon mag ook aan een barriere hangen: de passkeys-aanpak en de Security Annex
    richten net zo goed een maatregel in. Het `type` blijft dan zeggen wat de lezer krijgt, want een
    contractbijlage voer je anders uit dan een inrichtingshandleiding.
    """
    if fm.get("barrieres") is not None and fm.get("type") not in MET_BARRIERES:
        fout(readme, "B2", f"veld 'barrieres' hoort bij type {' of '.join(sorted(MET_BARRIERES))}")
    if fm.get("type") not in MET_BARRIERES:
        return

    bar = fm.get("barrieres")
    if fm.get("type") == "handleiding" and (not isinstance(bar, list) or not bar):
        fout(readme, "B2", "type handleiding vereist barrieres: [vraag_id, ...] uit paden.json")
    elif bar is not None:
        if not isinstance(bar, list) or not bar:
            fout(readme, "B2", "barrieres is een niet-lege lijst met vraag_id's uit paden.json")
        else:
            bekend = barrieres()
            if not bekend:
                fout(readme, "B2", "paden.json niet gevonden; zet de aanvalspaden-repo ernaast of in _aanvalspaden")
            else:
                for b in bar:
                    if b not in bekend:
                        fout(readme, "B2", f"barriere '{b}' bestaat niet in paden.json")

    if fm.get("rol") is not None and fm["rol"] not in ROLLEN:
        fout(readme, "B2", f"rol '{fm['rol']}' moet een van {ROLLEN} zijn")

    if fm.get("pijler") and not (ROOT / vak / str(fm["pijler"]) / "README.md").is_file():
        fout(readme, "B2", f"pijler '{fm['pijler']}' bestaat niet in {vak}/")

    if fm.get("type") != "handleiding":
        return

    body = lees_frontmatter(readme.read_text(encoding="utf-8"))[1].lower()
    for kop, naam in (("## bewijs", "Bewijs"), ("## zo leg je het uit", "Zo leg je het uit")):
        if kop not in body:
            fout(readme, "B3", f"een handleiding heeft de kop '{naam}' nodig")


def controleer_item(vak: str, map_: Path) -> dict | None:
    if not SLUG.match(map_.name):
        fout(map_, "B1", "mapnaam: alleen kleine letters, cijfers en koppeltekens")
    readme = map_ / "README.md"
    if not readme.exists():
        fout(map_, "B1", "geen README.md; elk item is een map met README")
        return None
    for sub in map_.iterdir():
        if sub.is_dir() and sub.name not in {"data", "img", "assets"}:
            fout(sub, "B1", "derde laag; alleen data/, img/ of assets/ mogen als submap")
    fm, _ = lees_frontmatter(readme.read_text(encoding="utf-8"))
    if fm is None:
        fout(readme, "B2", "geen frontmatter; acht velden verplicht")
        return None
    for veld in VERPLICHT:
        if veld not in fm or fm[veld] in ("", None):
            fout(readme, "B2", f"veld '{veld}' ontbreekt")
    for veld in fm:
        if veld == "auteur":
            fout(readme, "A1", "veld 'auteur' bestaat niet; gebruik 'herkomst' als rol of organisatietype")
        elif veld not in TOEGESTAAN:
            fout(readme, "B2", f"veld '{veld}' is niet toegestaan (alleen de acht vaste velden en 'licentie')")
    if ("peildatum" in fm) == ("versie" in fm):
        fout(readme, "B2", "precies één van 'peildatum' of 'versie' is verplicht")
    if "peildatum" in fm and not DATUM.match(str(fm["peildatum"])):
        fout(readme, "A6", f"peildatum '{fm['peildatum']}' niet in JJJJ-MM-DD of JJJJ-MM")
    if fm.get("vakgebied") != vak:
        fout(readme, "B2", f"vakgebied '{fm.get('vakgebied')}' klopt niet met de map '{vak}'")
    if fm.get("type") not in TYPES:
        fout(readme, "B2", f"type '{fm.get('type')}' niet in {TYPES}")
    if fm.get("status") not in STATUSSEN:
        fout(readme, "B2", f"status '{fm.get('status')}' niet in {STATUSSEN}")
    if not isinstance(fm.get("normen"), list):
        fout(readme, "B2", "normen moet een lijst zijn (mag leeg: [])")
    if isinstance(fm.get("samenvatting"), str) and len(fm["samenvatting"]) < 60:
        fout(readme, "B2", "samenvatting te kort; twee tot vier zinnen, dit wordt de kaarttekst")
    controleer_handleiding(vak, readme, fm)
    for bestand in map_.rglob("*"):
        if bestand.suffix in (".md", ".html", ".txt", ".json"):
            controleer_tekst(bestand)
    controleer_bestandslinks(map_, readme)
    controleer_dode_links(map_)
    fm["_map"] = map_
    fm["_vak"] = vak
    fm["_weergave"], fm["_link"] = bepaal_weergave(vak, map_)
    return fm


def bepaal_weergave(vak: str, map_: Path) -> tuple[str, str]:
    """live = opent in de browser; markdown = alleen tekst; download = binair."""
    if (map_ / "index.html").exists():
        return "live", f"{vak}/{map_.name}/"
    htmls = sorted(p for p in map_.glob("*.html"))
    if htmls:
        # Een HTML-leesversie moet index.html heten, anders geeft de map-URL een 404
        # op GitHub Pages en lopen sitemap en llms.txt stuk (statuut B3).
        fout(htmls[0], "B3", "HTML-leesversie moet index.html heten, anders geeft de map-URL een 404")
        return "live", f"{vak}/{map_.name}/{htmls[0].name}"
    # B3: elk tekstitem hoort een leesversie te hebben. Zonder index.html heeft het item geen
    # live URL, staat het niet in de sitemap en loopt een verwijzing ernaartoe dood op een 404.
    fout(map_, "B3", "geen index.html; elk tekstitem heeft een self-contained HTML-leesversie")
    if any(p.suffix == ".md" and p.name != "README.md" for p in map_.iterdir()):
        return "markdown", f"{REPO}/tree/main/{vak}/{map_.name}"
    if any(p.suffix in (".pptx", ".docx", ".xlsx", ".pdf", ".zip") for p in map_.iterdir()):
        return "download", f"{REPO}/tree/main/{vak}/{map_.name}"
    return "markdown", f"{REPO}/tree/main/{vak}/{map_.name}"


def lees_volgorde(tekst: str) -> list[str]:
    """De mapnamen onder '## Volgorde' in de README van een sectie, in de volgorde van de lijst."""
    if "## Volgorde" not in tekst:
        return []
    blok = tekst.split("## Volgorde", 1)[1].split("\n## ")[0]
    return [m.group(1).rstrip("/") for m in re.finditer(r"^\s*\d+\.\s*\[[^\]]+\]\(([^)]+)\)", blok, re.M)]


def lees_sectie(vak: str) -> dict:
    readme = ROOT / vak / "README.md"
    if not readme.exists():
        fout(ROOT / vak, "B1", "vakgebied zonder README.md")
        return {"titel": vak.title(), "lead": "", "hoort": []}
    tekst = readme.read_text(encoding="utf-8")
    titel = re.search(r"^# ([^\n]+)$", tekst, re.M)
    lead = re.search(r"^# [^\n]+\n\n((?:[^\n]+\n?)+?)\n\n", tekst)
    hoort = re.findall(r"^- (.+)$", tekst.split("## Wat hoort hier")[-1].split("\n## ")[0], re.M) if "## Wat hoort hier" in tekst else []
    controleer_tekst(readme)
    return {"titel": titel.group(1).strip() if titel else vak.title(),
            "lead": lead.group(1).strip().replace("\n", " ") if lead else "", "hoort": hoort,
            "volgorde": lees_volgorde(tekst)}


def zet_op_volgorde(vak: str, items: list[dict], sectie: dict) -> list[dict]:
    """Statuut B4: de volgorde is redactioneel en staat in de README van de sectie.

    Alfabetisch sorteren zet toevallige mapnamen bovenaan; deze lijst zet er een oordeel in. Wat in
    de lijst ontbreekt of niet bestaat, blokkeert de build: stil onderaan belanden is erger dan een
    rode melding.
    """
    if not items:
        return items
    readme = ROOT / vak / "README.md"
    lijst = sectie.get("volgorde") or []
    if not lijst:
        fout(readme, "B4", "geen '## Volgorde' met de items van deze sectie; de volgorde is redactioneel")
        return items
    op_naam = {fm["_map"].name: fm for fm in items}
    for naam in lijst:
        if naam not in op_naam:
            fout(readme, "B4", f"'{naam}' staat in de volgorde maar is geen item in deze sectie")
    for naam in sorted(op_naam):
        if naam not in lijst:
            fout(readme, "B4", f"'{naam}' ontbreekt in de volgorde; zet het item op zijn plek in de lijst")
    return [op_naam[n] for n in lijst if n in op_naam] + [fm for n, fm in sorted(op_naam.items()) if n not in lijst]


def controleer_alles() -> dict[str, list[dict]]:
    items: dict[str, list[dict]] = {v: [] for v in VAKGEBIEDEN}
    for kind in ROOT.iterdir():
        if kind.is_dir():
            if (kind.name not in VAKGEBIEDEN and kind.name not in ROOT_MAPPEN_OK
                    and not kind.name.startswith(".")):
                fout(kind, "B1", f"map op root is geen vakgebied {VAKGEBIEDEN}")
        elif kind.name not in ROOT_BESTANDEN_OK:
            fout(kind, "B1", "los bestand op root; hoort in een item-map")
    for bestand in ("README.md", "CONTRIBUTING.md", "ROADMAP.md"):
        if (ROOT / bestand).exists():
            controleer_tekst(ROOT / bestand)
    for vak in VAKGEBIEDEN:
        vakmap = ROOT / vak
        if not vakmap.is_dir():
            fout(vakmap, "B1", "vakgebied-map ontbreekt")
            continue
        for kind in sorted(vakmap.iterdir()):
            if kind.is_dir():
                fm = controleer_item(vak, kind)
                if fm:
                    items[vak].append(fm)
            elif kind.name not in ("README.md", "index.html"):
                fout(kind, "B1", "los bestand in vakgebied-map; maak er een item-map met README van")
    return items


# ----------------------------------------------------------------------------- genereren
CSS = """
:root{--bg:#f6f7f9;--card:#fff;--ink:#1a1d21;--muted:#5c6570;--line:#dfe3e8;--accent:#1f4e79;--accent2:#2e7d68}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
  font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
.wrap{max-width:960px;margin:0 auto;padding:24px 20px 80px}
.backlink{font-size:13px;margin:0 0 14px;color:var(--muted)}
.backlink a{color:var(--muted);text-decoration:none}
.backlink a:hover{color:var(--accent);text-decoration:underline}
.backlink span{color:var(--muted)}
header.top{border-bottom:3px solid var(--accent);padding-bottom:14px;margin-bottom:22px}
h1{font-size:26px;margin:0 0 4px;letter-spacing:-.3px}
.sub{color:var(--muted);font-size:13.5px}
.lead{font-size:16px;color:#33383e;border-left:3px solid var(--accent);padding-left:14px;margin:0 0 26px}
h2{font-size:19px;margin:34px 0 6px;letter-spacing:-.2px}
h2:first-of-type{margin-top:0}
.h2sub{color:var(--muted);font-size:13.5px;margin:0 0 14px}
p{margin:0 0 11px}
a{color:var(--accent)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px}
a.item{display:block;background:var(--card);border:1px solid var(--line);border-radius:8px;
  padding:16px 18px;text-decoration:none;color:inherit;transition:border-color .12s,box-shadow .12s}
a.item:hover{border-color:var(--accent);box-shadow:0 1px 6px rgba(31,78,121,.10)}
.itemtop{display:flex;align-items:baseline;justify-content:space-between;gap:10px;margin-bottom:5px}
h3.groep{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:26px 0 8px}
.itemtitle{font-size:15.5px;font-weight:600;color:var(--accent);letter-spacing:-.1px}
.itemdesc{font-size:13.5px;color:#3c434b;margin:0}
.meta{font-size:12px;color:var(--muted);margin-top:8px}
.tag{display:inline-block;border-radius:4px;padding:2px 8px;font-size:11.5px;font-weight:600;
  white-space:nowrap;border:1px solid transparent}
.tag-live{background:#e6f2ee;color:var(--accent2);border-color:#a8d5bd}
.tag-repo{background:#eef1f5;color:var(--muted);border-color:var(--line)}
.tag-leeg{background:#f7f8fa;color:#9aa2ad;border-color:var(--line)}
ul.hoort{margin:0 0 14px;padding-left:20px;color:#3c434b;font-size:14px}
ul.hoort li{margin-bottom:3px}
.note{background:#fffbe9;border:1px solid #ecd98a;border-radius:6px;padding:11px 14px;font-size:13.5px;margin:16px 0}
.cta{display:inline-block;background:var(--accent);color:#fff;text-decoration:none;font-weight:600;
  font-size:14px;border-radius:6px;padding:9px 18px;margin-top:4px}
.cta:hover{background:#17608f}
.cta.alt{background:#fff;color:var(--accent);border:1px solid var(--line);margin-left:8px}
.cta.alt:hover{border-color:var(--accent)}
footer{border-top:1px solid var(--line);margin-top:44px;padding-top:16px;font-size:12.5px;color:var(--muted)}
footer a{color:var(--muted)}
@media (max-width:600px){.cta.alt{margin-left:0;margin-top:8px}}
"""

FOOTER = f"""<footer>
  <p>Onderdeel van <a href="https://security-commons-nl.github.io/">Security Commons NL</a> ·
  Bron: <a href="{REPO}">github.com/security-commons-nl/kennisbank</a> ·
  Licentie <a href="{REPO}/blob/main/LICENSE">EUPL-1.2</a> ·
  Gegenereerd door <code>tools/build.py</code>; niet met de hand bewerken.</p>
</footer>"""


def e(s: object) -> str:
    return html.escape(str(s), quote=True)


def meta_regel(fm: dict, met_vak: bool) -> str:
    delen = []
    if met_vak:
        delen.append(fm["_vak"])
    delen.append(fm["type"])
    if "versie" in fm:
        delen.append(f"versie {fm['versie']}")
    elif "peildatum" in fm:
        delen.append(f"peildatum {fm['peildatum']}")
    delen.append(fm["status"])
    # Bij een handleiding is de barriere het belangrijkste etiket: daarmee vindt een lezer hem terug
    # vanuit de zelfcheck. De rol zegt of het de basis is of een alternatief ernaast.
    if fm.get("barrieres"):
        bekend = barrieres()
        delen.append("barriere: " + ", ".join(bekend.get(b, b) for b in fm["barrieres"]))
    if fm.get("rol"):
        delen.append(fm["rol"])
    return " · ".join(e(d) for d in delen)


def kaart(fm: dict, basis: str, met_vak: bool) -> str:
    link = fm["_link"] if fm["_link"].startswith("http") else basis + fm["_link"]
    tag = {"live": ("tag-live", "live"), "markdown": ("tag-repo", "markdown"), "download": ("tag-repo", "download")}[fm["_weergave"]]
    return f"""  <a class="item" href="{e(link)}">
    <span class="itemtop">
      <span class="itemtitle">{e(fm['titel'])}</span>
      <span class="tag {tag[0]}">{tag[1]}</span>
    </span>
    <p class="itemdesc">{e(fm['samenvatting'])}</p>
    <div class="meta">{meta_regel(fm, met_vak)}</div>
  </a>
"""


def kruimels_html(kruimels: list[tuple[str, str]], klasse: str = "backlink") -> str:
    """Kruimelpad: elk paar is (tekst, href); een lege href is de huidige pagina."""
    delen = []
    for tekst, href in kruimels:
        delen.append(f'<a href="{href}">{e(tekst)}</a>' if href else f"<span>{e(tekst)}</span>")
    binnen = " \u203a ".join(delen)
    return f'<nav class="{klasse}" aria-label="Kruimelpad">{binnen}</nav>'


def pagina(titel: str, beschrijving: str, canonical: str, body: str, kruimels: list[tuple[str, str]]) -> str:
    terug = kruimels_html(kruimels) + "\n\n" if kruimels else ""
    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titel)}</title>
<meta name="description" content="{e(beschrijving)}">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="alternate icon" href="/favicon.ico" sizes="32x32">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">

{terug}{body}

{FOOTER}

</div>
</body>
</html>
"""


def bouw_sectie(vak: str, sectie: dict, items: list[dict]) -> str:
    n = len(items)
    live = sum(1 for i in items if i["_weergave"] == "live")
    telling = {0: "Nog leeg.", 1: "Eén stuk."}.get(n, f"{n} stukken.")
    if live == n and n > 0:
        telling += " Alle openen direct in de browser." if n > 1 else " Opent direct in de browser."
    elif live:
        telling += f" {live} {'openen' if live > 1 else 'opent'} direct in de browser."
    def blok(kop, sub, anker=""):
        """Een groep kaarten met een kopje erboven; een leeg blok levert niets op."""
        if not sub:
            return ""
        ks = "".join(kaart(x, "", False).replace(f'href="{vak}/', 'href="') for x in sub)
        id_attr = f' id="{anker}"' if anker else ""
        return f'<h3 class="groep"{id_attr}>{e(kop)}</h3>' + NL + f'<div class="grid">{NL}{NL}{ks}{NL}</div>' + NL

    # Handleidingen apart: dat worden er straks meer dan al het andere bij elkaar, en het is een ander
    # soort stuk. Een methode lees je, een handleiding voer je uit.
    handleidingen = [x for x in items if x.get("type") == "handleiding"]
    overig = [x for x in items if x.get("type") != "handleiding"]
    grid = (blok("Aanpakken, sjablonen en naslag", overig)
            + blok("Handleidingen: een maatregel inrichten, per barriere uit de zelfcheck",
                   handleidingen, "handleidingen"))
    if not items:
        grid = '<p class="h2sub">Nog geen stukken. Heb je iets liggen? Zie hieronder.</p>'
    hoort = "".join(f"  <li>{e(h)}</li>\n" for h in sectie["hoort"])
    body = f"""<header class="top">
  <h1>{e(sectie['titel'])}</h1>
  <div class="sub">Kennisbank · Security Commons NL</div>
</header>

<p class="lead">{e(sectie['lead'])}</p>

<h2>Wat hier staat</h2>
<p class="h2sub">{e(telling)}</p>

{grid}

<h2>Wat hier thuishoort</h2>
<ul class="hoort">
{hoort}</ul>
<p><a class="cta" href="{REPO}/issues/new/choose">Bijdrage aanbieden</a></p>"""
    return pagina(f"{sectie['titel']} · Kennisbank · Security Commons NL", sectie["lead"], f"{SITE}/{vak}/", body,
                  [("Security Commons NL", HOOFDPAGINA), ("Kennisbank", "../"), (sectie["titel"], "")])


def bouw_root(secties: dict[str, dict], items: dict[str, list[dict]]) -> str:
    live = [i for v in VAKGEBIEDEN for i in items[v] if i["_weergave"] == "live"]
    kaarten_live = "".join(kaart(i, "", True) for i in live)
    kaarten_secties = ""
    for vak in VAKGEBIEDEN:
        n = len(items[vak])
        tag = '<span class="tag tag-leeg">nog leeg</span>' if n == 0 else f'<span class="tag tag-repo">{n} {"stuk" if n == 1 else "stukken"}</span>'
        kaarten_secties += f"""  <a class="item" href="{vak}/">
    <span class="itemtop">
      <span class="itemtitle">{e(secties[vak]['titel'])}</span>
      {tag}
    </span>
    <p class="itemdesc">{e(secties[vak]['lead'])}</p>
  </a>
"""
    body = f"""<header class="top">
  <h1>Kennisbank</h1>
  <div class="sub">Security Commons NL · werkende kennis uit de publieke sector</div>
</header>

<p class="lead">Memo's, rapportages, aanpakken, trainingen en datasets die al gebruikt zijn in echte
organisaties, geanonimiseerd gedeeld door professionals. Geen theorie. Alles herbruikbaar onder EUPL-1.2.</p>

<h2>Direct te lezen</h2>
<p class="h2sub">Publicaties met een eigen pagina. Openen in de browser, geen installatie, geen externe afhankelijkheden.</p>

<div class="grid">

{kaarten_live}
</div>

<p class="h2sub">Handleidingen per barriere uit de zelfcheck staan bij <a href="security/#handleidingen">Security</a>, en met de alternatieven ernaast op <a href="https://security-commons-nl.github.io/aanvalspaden/normen/">Van aanvalspad naar norm</a>.</p>

<h2>Secties</h2>
<p class="h2sub">De kennisbank is ingedeeld op vakgebied. Elke sectie beschrijft wat er thuishoort.</p>

<div class="grid">

{kaarten_secties}
</div>

<h2>Meedoen</h2>
<p>Eén regel corrigeren is genoeg om bij te dragen, je hoeft geen visualisatie te bouwen. Ook zonder
schrijfrechten: GitHub maakt van je wijziging automatisch een voorstel.</p>
<p>
  <a class="cta" href="{REPO}/issues/new/choose">Bijdrage aanbieden</a>
  <a class="cta alt" href="{REPO}">Repository op GitHub</a>
</p>
<div class="note">
  Bevat je document persoonsgegevens? Meld het in het formulier. Scrubben kan met de
  <a href="https://github.com/security-commons-nl/anonimizer-local">anonimizer</a> vóór publicatie.
  De spelregels staan in het <a href="https://github.com/security-commons-nl/.github/blob/main/REDACTIESTATUUT.md">redactiestatuut</a>.
</div>"""
    return pagina("Kennisbank · Security Commons NL",
                  "Werkende kennis uit de publieke sector: security, privacy, continuïteit en governance. Open herbruikbaar onder EUPL-1.2.",
                  f"{SITE}/", body,
                  [("Security Commons NL", HOOFDPAGINA), ("Kennisbank", "")])


KRUIMEL_CSS = (
    ".kruimel{font:13px/1.5 system-ui,'Segoe UI',Arial,sans-serif;margin:0 0 1.2em;color:#5a6675}"
    ".kruimel a{color:#1f4e79;text-decoration:none}"
    ".kruimel a:hover{text-decoration:underline}"
)


def kruimelblok(kruimels: list[tuple[str, str]]) -> str:
    return (KRUIMEL_START + f"<style>{KRUIMEL_CSS}</style>"
            + kruimels_html(kruimels, "kruimel") + KRUIMEL_EIND)


def verwijder_zelflink(tekst: str, eigen_url: str) -> str:
    """Haal een blockquote weg die naar de eigen pagina verwijst.

    In de README wijst die regel de lezer naar de leesversie, en een workflow bewaakt dat hij er
    staat. In de leesversie zelf is het een link naar de pagina waar je al bent.
    """
    kern = re.escape(eigen_url.rstrip("/"))
    patroon = re.compile(r"<blockquote>(?:(?!</blockquote>).)*?" + kern + r"/?\"(?:(?!</blockquote>).)*?</blockquote>\s*", re.S)
    return patroon.sub("", tekst)


FAVICON_START = "<!-- favicon -->"
FAVICON_EIND = "<!-- /favicon -->"
FAVICON = (FAVICON_START
           + '<link rel="icon" href="/favicon.svg" type="image/svg+xml">'
           + '<link rel="alternate icon" href="/favicon.ico" sizes="32x32">'
           + FAVICON_EIND)


def verwijder_dubbele_titel(tekst: str) -> str:
    """Haal de titelkop weg die pandoc bij --standalone toevoegt als de tekst zelf al een h1 heeft.

    Anders staat de titel twee keer boven elkaar: een keer uit de metadata, een keer uit de markdown.
    """
    m = re.search(r"<header id=\"title-block-header\">.*?</header>\s*", tekst, re.S)
    if m and re.search(r"<h1\b", tekst[m.end():]):
        return tekst[: m.start()] + tekst[m.end():]
    return tekst


def zet_favicon(tekst: str) -> str:
    """Verwijs naar het favicon in de </head>; zonder dit vraagt elke browser /favicon.ico op."""
    if FAVICON_START in tekst:
        return re.sub(re.escape(FAVICON_START) + ".*?" + re.escape(FAVICON_EIND), FAVICON, tekst, flags=re.S)
    return tekst.replace("</head>", FAVICON + "</head>", 1)


# De standaard leesopmaak van een leesversie: Calibri in een kolom van 19cm, gecentreerd. Alleen daar
# past een zijbalk naast. Pagina's met een eigen, bredere opmaak krijgen het blok bovenaan.
LEESKOLOM = "font-family:Calibri"

INHOUD_CSS = (
    # Blok bovenaan: werkt op elke pagina en op elke breedte.
    ".inhoud{font:13px/1.5 system-ui,'Segoe UI',Arial,sans-serif;margin:1.4em auto 1.6em;max-width:19cm;"
    "border:1px solid #d7dee7;border-radius:8px;padding:.7em 1em;background:#f8fafc}"
    ".inhoud ol{margin:.4em 0 0;padding:0;list-style:none;columns:2;column-gap:1.5em}"
    ".inhoud li{margin:.25em 0;break-inside:avoid}"
    # Zwevend naast de tekst, maar alleen bij de standaard leeskolom en genoeg ruimte ernaast:
    # 19cm tekst plus twee keer 8cm marge is ongeveer 1450px.
    "@media (min-width:1450px){"
    ".inhoud.zijbalk{position:fixed;top:2cm;left:calc(50vw - 18.6cm);width:8cm;max-height:78vh;"
    "overflow:auto;font-size:12px;margin:0;border:0;border-radius:0;background:none;"
    "padding:0 .5em 0 0}"
    ".inhoud.zijbalk ol{columns:auto}"
    ".inhoud.zijbalk li{margin:.3em 0}"
    "}"
    ".inhoud b{display:block;color:#5a6675;font-size:11px;letter-spacing:.08em;text-transform:uppercase}"
    ".inhoud a{color:#1f4e79;text-decoration:none}"
    ".inhoud a:hover{text-decoration:underline}"
    "@media print{.inhoud{display:none}}"
)


def zorg_voor_ids(tekst: str) -> str:
    """Geef elke h2 zonder id er een, afgeleid van de koptekst. Idempotent en botsingsvrij."""
    gebruikt = set(re.findall(r'id="([^"]+)"', tekst))

    def slug(kop: str) -> str:
        s = re.sub(r"<[^>]+>", "", kop).lower().strip()
        s = re.sub(r"[^a-z0-9]+", "-", s).strip("-") or "sectie"
        basis, n = s, 2
        while s in gebruikt:
            s = f"{basis}-{n}"
            n += 1
        gebruikt.add(s)
        return s

    return re.sub(r"<h2(?![^>]*\bid=)([^>]*)>(.*?)</h2>",
                  lambda m: f'<h2 id="{slug(m.group(2))}"{m.group(1)}>{m.group(2)}</h2>',
                  tekst, flags=re.S)


def inhoudsopgave(tekst: str) -> str:
    """Een lijst met de h2-koppen van de leesversie, als navigatie naast de tekst."""
    koppen = re.findall(r'<h2 id="([^"]+)"[^>]*>(.*?)</h2>', tekst, re.S)
    if not koppen:
        return ""
    items = "".join(
        f'<li><a href="#{h}">{re.sub(r"<[^>]+>", "", k).strip()}</a></li>' for h, k in koppen
    )
    klasse = "inhoud zijbalk" if LEESKOLOM in tekst else "inhoud"
    return (INHOUD_START + f"<style>{INHOUD_CSS}</style>"
            + f'<nav class="{klasse}" aria-label="Inhoudsopgave"><b>Op deze pagina</b>'
            + f"<ol>{items}</ol></nav>" + INHOUD_EIND)


def zet_inhoudsopgave(tekst: str) -> str:
    """Zet of vernieuw de inhoudsopgave, maar alleen bij een lang stuk.

    Een bestaand blok wordt eerst weggehaald en daarna opnieuw geplaatst. Anders blijft het staan
    waar een vorige versie het zette, ook als de plaatsingsregel intussen beter is geworden.
    """
    tekst = re.sub(re.escape(INHOUD_START) + ".*?" + re.escape(INHOUD_EIND), "", tekst, flags=re.S)
    zonder = re.sub(r"<[^>]+>", " ", tekst)
    if len(zonder.split()) < INHOUD_VANAF_WOORDEN:
        return tekst
    blok = inhoudsopgave(tekst)
    if not blok:
        return tekst
    m = re.search(r"<h1[^>]*>.*?</h1>", tekst, re.S)
    if not m:
        return tekst
    # Staat de titel in een paginakop met eigen opmaak, dan hoort het blok daar niet in: het krijgt
    # de kleuren van die kop en breekt hem doormidden. Dan pas na de kop.
    kop = re.search(r"<header\b[^>]*>.*?</header>", tekst, re.S)
    plek = kop.end() if kop and kop.start() < m.start() < kop.end() else m.end()
    return tekst[:plek] + blok + tekst[plek:]


BRON_CSS = (
    ".bronvoet{border-top:1px solid #d7dee7;margin:3em 0 0;padding-top:1em;"
    "font:12.5px/1.6 system-ui,'Segoe UI',Arial,sans-serif;color:#5a6675}"
    ".bronvoet a{color:#1f4e79}"
    "@media print{.bronvoet{display:none}}"
)


def bronvoet(vak: str, item: str) -> str:
    """De afsluiting van een leesversie: waar de bronbestanden staan, onder welke licentie.

    De gegenereerde indexpagina's hebben zo'n voet al; leesversies komen uit pandoc en hadden hem
    niet. Daardoor was een itempagina een doodlopend eind: wel de tekst, geen route naar de map
    met de bijlagen.
    """
    map_url = f"{REPO}/tree/main/{vak}/{item}"
    return (BRON_START + f"<style>{BRON_CSS}</style>"
            + '<footer class="bronvoet"><p>Onderdeel van '
            + f'<a href="{HOOFDPAGINA}">Security Commons NL</a> \u00b7 '
            + f'Bronbestanden van dit item: <a href="{map_url}">{vak}/{item}</a> \u00b7 '
            + f'Licentie <a href="{REPO}/blob/main/LICENSE">EUPL-1.2</a> \u00b7 '
            + f'<a href="{REPO}/issues/new/choose">Verbetering voorstellen</a>'
            + "</p></footer>" + BRON_EIND)


def zet_bronvoet(tekst: str, vak: str, item: str) -> str:
    """Zet of vernieuw de bronvoet vlak voor </body>. Idempotent."""
    blok = bronvoet(vak, item)
    if BRON_START in tekst:
        return re.sub(re.escape(BRON_START) + ".*?" + re.escape(BRON_EIND),
                      lambda _: blok, tekst, flags=re.S)
    if "</body>" not in tekst:
        return tekst
    return tekst.replace("</body>", blok + "</body>", 1)


def zet_kruimelpad(pad: Path, kruimels: list[tuple[str, str]], alleen_check: bool) -> bool:
    """Maak de leesversie klaar: geen link naar zichzelf, wel een kruimelpad, favicon,
    inhoudsopgave bij een lang stuk en een bronvoet. Idempotent."""
    origineel = pad.read_text(encoding="utf-8")
    eigen = f"{SITE}/{pad.parent.parent.name}/{pad.parent.name}/"
    vak, item = pad.parent.parent.name, pad.parent.name
    tekst = zet_bronvoet(zet_inhoudsopgave(zorg_voor_ids(
        zet_favicon(verwijder_dubbele_titel(verwijder_zelflink(origineel, eigen))))), vak, item)
    if BRON_START not in tekst:
        fout(pad, "B10", "geen </body> gevonden; de bronvoet kan er niet in")
        return False
    if tekst != origineel and alleen_check:
        fout(pad, "B3", "leesversie is niet bijgewerkt (zelflink, dubbele titel, favicon, "
                          "inhoudsopgave of bronvoet); draai python tools/build.py")
        return False

    blok = kruimelblok(kruimels)
    if KRUIMEL_START in tekst:
        tekst = re.sub(re.escape(KRUIMEL_START) + ".*?" + re.escape(KRUIMEL_EIND), blok, tekst, flags=re.S)
    else:
        m = re.search(r"<body[^>]*>", tekst)
        if not m:
            fout(pad, "B10", "geen <body> gevonden; kruimelpad kan er niet in")
            return False
        tekst = tekst[: m.end()] + blok + tekst[m.end():]

    if tekst == origineel:
        return False
    if alleen_check:
        fout(pad, "B10", "kruimelpad ontbreekt of is verouderd; draai python tools/build.py")
        return False
    pad.write_text(tekst, encoding="utf-8", newline="\n")
    return True


def kruimels_van_item(fm: dict, sectie: dict) -> list[tuple[str, str]]:
    return [("Security Commons NL", HOOFDPAGINA), ("Kennisbank", "../../"),
            (sectie["titel"], "../"), (str(fm["titel"]), "")]


def schrijf(pad: Path, inhoud: str) -> bool:
    oud = pad.read_text(encoding="utf-8") if pad.exists() else None
    if oud == inhoud:
        return False
    pad.write_bytes(inhoud.encode("utf-8"))
    return True


def schrijf_handelingsperspectief(items: dict[str, list[dict]]) -> bool:
    """De kennisbank is de bron: per handleiding de barrieres en de rol. aanvalspaden kopieert dit.

    Zo staat een handleiding op een plek. Zou aanvalspaden de koppeling zelf bijhouden, dan loopt die
    lijst achter zodra hier een artikel bijkomt, en dat is precies het probleem dat de normverankering
    voor de kaders al heeft opgelost.
    """
    bekend = barrieres()
    hl = []
    for vak in VAKGEBIEDEN:
        for fm in items[vak]:
            if not fm.get("barrieres"):
                continue
            for b in fm["barrieres"]:
                hl.append({
                    "barriere": b,
                    "item": f"{vak}/{fm['_map'].name}",
                    "titel": fm["titel"],
                    "rol": fm.get("rol", "fundering"),
                    "url": f"{SITE}/{vak}/{fm['_map'].name}/",
                })
    hl.sort(key=lambda h: (h["barriere"], ROLLEN.index(h["rol"]), h["titel"]))
    gedekt = {h["barriere"] for h in hl}
    data = {
        "versie": "gegenereerd door kennisbank/tools/build.py; wijzig de frontmatter van de items, niet dit bestand",
        "handleidingen": hl,
        "zonder_handleiding": sorted(b for b in bekend if b not in gedekt),
    }
    return schrijf(ROOT / "handelingsperspectief.json", json.dumps(data, ensure_ascii=False, indent=2) + NL)


def main() -> int:
    alleen_check = "--check" in sys.argv
    items = controleer_alles()
    secties = {v: lees_sectie(v) for v in VAKGEBIEDEN if (ROOT / v).is_dir()}
    for vak, sectie in secties.items():
        items[vak] = zet_op_volgorde(vak, items[vak], sectie)
    if fouten:
        print(f"Redactiestatuut: {len(fouten)} overtreding(en). Niets gebouwd.\n")
        for f in fouten:
            print("  " + f)
        print("\nRegels: https://github.com/security-commons-nl/.github/blob/main/REDACTIESTATUUT.md")
        return 1
    totaal = sum(len(v) for v in items.values())

    # Kruimelpad in elke item-leesversie (B10). In --check wordt een ontbrekend of verouderd
    # kruimelpad een fout; bij bouwen wordt het geschreven.
    kruimel_gewijzigd = []
    for vak in VAKGEBIEDEN:
        for fm in items[vak]:
            html_pad = fm["_map"] / "index.html"
            if html_pad.exists() and zet_kruimelpad(html_pad, kruimels_van_item(fm, secties[vak]), alleen_check):
                kruimel_gewijzigd.append(f"{vak}/{fm['_map'].name}/index.html")
    if fouten:
        print(f"Redactiestatuut: {len(fouten)} overtreding(en). Niets gebouwd.\n")
        for f in fouten:
            print("  " + f)
        return 1

    print(f"Redactiestatuut: geen overtredingen ({totaal} items).")
    if alleen_check:
        return 0
    gewijzigd = list(kruimel_gewijzigd)
    for vak in VAKGEBIEDEN:
        if schrijf(ROOT / vak / "index.html", bouw_sectie(vak, secties[vak], items[vak])):
            gewijzigd.append(f"{vak}/index.html")
    if schrijf(ROOT / "index.html", bouw_root(secties, items)):
        gewijzigd.append("index.html")
    if schrijf_handelingsperspectief(items):
        gewijzigd.append("handelingsperspectief.json")
    print("Gebouwd: " + (", ".join(gewijzigd) if gewijzigd else "niets gewijzigd"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
