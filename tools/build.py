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
# Pijlerblok: op de leesversie van een pijler de stukken die eronder hangen. Zonder dit blok bestaat
# het verband alleen in de frontmatter en komt de lezer het nooit tegen.
PIJLER_START = "<!-- pijler-kinderen -->"
PIJLER_EIND = "<!-- /pijler-kinderen -->"
# Normenregel: het veld `normen` boven aan een leesversie. Het is een verplicht veld (B2), maar het
# kwam nergens op een pagina terecht; wie op NIS2 of de Cbw zocht, vond het stuk alleen bij toeval.
NORM_START = "<!-- normen -->"
NORM_EIND = "<!-- /normen -->"
# Bronnenblok (statuut B15): wat andere partijen over hetzelfde onderwerp al hebben, onderaan een
# leesversie. De verwijzingen staan per item als id in de frontmatter; titel, adres en toegang staan
# een keer in bronnen.json, zodat een verhuisd stuk op een plek wordt bijgewerkt.
ELDERS_START = "<!-- elders -->"
ELDERS_EIND = "<!-- /elders -->"

VAKGEBIEDEN = ["security", "privacy", "bcm", "governance"]
TYPES = ["beleid", "sjabloon", "lesmateriaal", "dataset", "referentie", "aanpak", "rapportage", "handleiding"]
STATUSSEN = ["concept", "in gebruik", "sjabloon", "gearchiveerd"]
VERPLICHT = ["titel", "vakgebied", "type", "normen", "herkomst", "status", "samenvatting"]
TOEGESTAAN = set(VERPLICHT) | {"peildatum", "versie", "licentie", "barrieres", "rol", "pijler", "bronnen"}
ROLLEN = ["fundering", "alternatief", "verdieping"]
# Types die aan een barriere uit de zelfcheck mogen hangen. Een handleiding moet het, een aanpak of
# sjabloon mag het: die richten net zo goed een maatregel in, alleen in een andere vorm.
MET_BARRIERES = {"handleiding", "aanpak", "sjabloon"}
# Twee schrijfwijzen voor dezelfde norm zijn onzichtbaar zolang het veld nergens getoond wordt; zodra
# het op de kaart staat en meetelt bij het zoeken, splitst het de vindbaarheid. Dit is geen gesloten
# register: een norm die hier niet in staat mag gewoon, alleen een bekende variant wordt afgekeurd.
NORM_ALIAS = {
    "cyberbeveiligingswet": "Cbw",
    "cbw 2025": "Cbw",
    "bio 2.0": "BIO2",
    "bio2.0": "BIO2",
    "bio 2": "BIO2",
    "nis 2": "NIS2",
    "nis-2": "NIS2",
    "avg/gdpr": "AVG",
    "gdpr": "AVG",
    "iso27001": "ISO 27001",
    "iso 27001:2022": "ISO 27001",
}
NL = chr(10)

# Mappen die op de root mogen staan naast de vakgebieden. Alles wat met een punt begint is
# tooling (.git, .pytest_cache, .venv) en telt nooit als inhoud.
ROOT_MAPPEN_OK = {".github", "tools", "_aanvalspaden"}
# `.git` is in een git-worktree een bestand in plaats van een map; het is tooling, geen inhoud.
ROOT_BESTANDEN_OK = {"README.md", "CONTRIBUTING.md", "ROADMAP.md", "LICENSE", "index.html", ".gitignore",
                     ".nojekyll", "handelingsperspectief.json", "llms.txt", "sitemap.xml", "bronnen.json", ".git"}

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


# ----------------------------------------------------------------------------- bronnen (B15)
# Een item verwijst naar het werk van andere partijen via id's uit bronnen.json. De partij komt uit
# de stelselkaart: zo is elke verwijzing te herleiden tot een partij in het stelsel, en heeft elke
# verwijzing een terugval als het specifieke stuk verdwijnt (het adres van de partij zelf).
BRONNEN_PAD_NAAM = "bronnen.json"
PARTIJEN_REL = Path("security") / "stelselkaart-security-gremia" / "data" / "partijen.json"
TOEGANG = {
    "open": "vrij toegankelijk",
    "inlog": "achter een inlog",
    "onbekend": "toegang niet vastgesteld",
}
BRON_VELDEN_VERPLICHT = ("titel", "url", "partij", "toegang", "gezien")
BRON_VELDEN_OPTIONEEL = ("kring", "archief", "vervallen")
BRON_ID = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
TLP = re.compile(r"\btlp\s*[:_-]?\s*(green|amber|amber\+strict|red|groen|rood)\b", re.I)
_register_cache: tuple[dict, dict] | None = None


def partijen() -> dict[str, dict]:
    """id -> partij uit de stelselkaart. Leeg als de dataset er niet is; de aanroeper meldt dat."""
    pad = ROOT / PARTIJEN_REL
    if not pad.is_file():
        return {}
    return {p["id"]: p for p in json.loads(pad.read_text(encoding="utf-8"))["partijen"]}


def register() -> tuple[dict[str, dict], dict[str, dict]]:
    """(bronnen, partijen), gecontroleerd. Fouten landen in `fouten`; een kapotte bron valt weg.

    Een keer lezen en een keer melden: het register wordt door elk item geraadpleegd, en zonder cache
    zou een fout in een bron net zo vaak gemeld worden als er items naar verwijzen.
    """
    global _register_cache
    if _register_cache is not None:
        return _register_cache
    pad = ROOT / BRONNEN_PAD_NAAM
    ptn = partijen()
    if not pad.is_file():
        _register_cache = ({}, ptn)
        return _register_cache
    try:
        data = json.loads(pad.read_text(encoding="utf-8"))
    except json.JSONDecodeError as fout_:
        fout(pad, "B15", f"geen geldige JSON: {fout_}")
        _register_cache = ({}, ptn)
        return _register_cache
    if not ptn:
        fout(pad, "B15", f"stelselkaart niet gevonden ({PARTIJEN_REL.as_posix()}); elke bron hoort bij een partij daaruit")
    # Zoekwoorden per partij: wie "VNG" typt moet ook de IBD vinden, die onderdeel van de VNG is. De
    # afkorting in de stelselkaart is de naam, maar niet het woord waarmee iedereen zoekt.
    for pid, woorden in (data.get("zoekwoorden") or {}).items():
        if ptn and pid not in ptn:
            fout(pad, "B15", f"zoekwoorden: partij '{pid}' staat niet in de stelselkaart")
        if not isinstance(woorden, list) or not all(isinstance(w, str) and w.strip() for w in woorden):
            fout(pad, "B15", f"zoekwoorden: '{pid}' moet een lijst met woorden zijn")
    for nr, groep in enumerate(data.get("synoniemen") or [], 1):
        if (not isinstance(groep, list) or len(groep) < 2
                or not all(isinstance(w, str) and w.strip() for w in groep)):
            fout(pad, "B15", f"synoniemen: groep {nr} moet een lijst van minstens twee woorden zijn")
    goed: dict[str, dict] = {}
    gezien_urls: dict[str, str] = {}
    for bid, bron in (data.get("bronnen") or {}).items():
        voor = len(fouten)
        waar = f"bron '{bid}'"
        if not BRON_ID.match(bid):
            fout(pad, "B15", f"{waar}: id alleen kleine letters, cijfers en koppeltekens")
        for veld in BRON_VELDEN_VERPLICHT:
            if not bron.get(veld):
                fout(pad, "B15", f"{waar}: veld '{veld}' ontbreekt")
        for veld in bron:
            if veld not in BRON_VELDEN_VERPLICHT + BRON_VELDEN_OPTIONEEL:
                fout(pad, "B15", f"{waar}: veld '{veld}' bestaat niet")
        for veld in ("url", "archief"):
            if bron.get(veld) and not str(bron[veld]).startswith("https://"):
                fout(pad, "B15", f"{waar}: {veld} moet met https:// beginnen")
        if bron.get("url") and SOCIALE_MEDIA.search(str(bron["url"])):
            fout(pad, "A5", f"{waar}: geen links naar sociale media")
        # Een stuk met een TLP-markering mag niet publiek, ook de titel niet: het bestaan van een
        # TLP:GREEN-advisory noemen op een open pagina doorbreekt de markering al.
        if TLP.search(f"{bron.get('titel', '')} {bron.get('url', '')}"):
            fout(pad, "B15", f"{waar}: verwijst naar een stuk met een TLP-markering; dat hoort niet in een publiek register")
        url = str(bron.get("url", "")).rstrip("/")
        if url and url in gezien_urls:
            fout(pad, "B15", f"{waar}: zelfde adres als bron '{gezien_urls[url]}'; een stuk staat een keer in het register")
        gezien_urls.setdefault(url, bid)
        if bron.get("toegang") and bron["toegang"] not in TOEGANG:
            fout(pad, "B15", f"{waar}: toegang '{bron['toegang']}' moet een van {list(TOEGANG)} zijn")
        if bron.get("toegang") == "inlog" and not bron.get("kring"):
            fout(pad, "B15", f"{waar}: bij toegang inlog hoort 'kring' (wie er wel bij kan)")
        for veld in ("gezien", "vervallen"):
            if bron.get(veld) and not DATUM.match(str(bron[veld])):
                fout(pad, "A6", f"{waar}: {veld} '{bron[veld]}' niet in JJJJ-MM-DD of JJJJ-MM")
        partij = ptn.get(str(bron.get("partij")))
        if ptn and bron.get("partij") and partij is None:
            fout(pad, "B15", f"{waar}: partij '{bron['partij']}' staat niet in de stelselkaart")
        elif partij is not None and not str(partij.get("url", "")).startswith("https://"):
            fout(pad, "B15", f"{waar}: partij '{bron['partij']}' heeft geen url in de stelselkaart; "
                              "die is de terugval als dit stuk verdwijnt")
        if len(fouten) == voor:
            goed[bid] = bron
    _register_cache = (goed, ptn)
    return _register_cache


def synoniemen() -> list[list[str]]:
    """Groepen woorden die bij het zoeken als hetzelfde tellen (cbw en Cyberbeveiligingswet)."""
    pad = ROOT / BRONNEN_PAD_NAAM
    if not pad.is_file():
        return []
    groepen = json.loads(pad.read_text(encoding="utf-8")).get("synoniemen") or []
    return [[str(w) for w in g] for g in groepen if isinstance(g, list)]


def synoniemen_blok() -> str:
    # Als JSON in de pagina, zodat het zoekscript ze kan lezen zonder iets van buiten te laden.
    # "</" kan de script-tag niet sluiten: de woorden bevatten dat niet, en json.dumps escapet geen
    # slash, dus het wordt hier voor de zekerheid vervangen.
    data = json.dumps(synoniemen(), ensure_ascii=False).replace("</", "<\\/")
    return f'<script type="application/json" id="synoniemen">{data}</script>'


def zoekwoorden() -> dict[str, list[str]]:
    pad = ROOT / BRONNEN_PAD_NAAM
    if not pad.is_file():
        return {}
    data = json.loads(pad.read_text(encoding="utf-8"))
    return {k: [str(w) for w in v] for k, v in (data.get("zoekwoorden") or {}).items() if isinstance(v, list)}


def bron_zoektekst(bron: dict, partij: dict | None, extra: list[str]) -> str:
    """De tekst waarop het zoekvak een bron vergelijkt: titel, partij en haar zoekwoorden."""
    delen = [bron.get("titel", ""), bron.get("partij", "")]
    if partij:
        delen.append(partij.get("naam", ""))
    delen += extra
    return " ".join(str(d) for d in delen).lower()


def controleer_bronnen(readme: Path, fm: dict) -> None:
    """Het veld `bronnen` is een niet-lege lijst met id's die in het register staan."""
    if "bronnen" not in fm:
        return
    ids = fm["bronnen"]
    if not isinstance(ids, list) or not ids:
        fout(readme, "B2", "bronnen is een niet-lege lijst met id's uit bronnen.json")
        return
    if len(set(ids)) != len(ids):
        fout(readme, "B2", "bronnen noemt een id twee keer")
    pad = ROOT / BRONNEN_PAD_NAAM
    if not pad.is_file():
        fout(readme, "B15", "bronnen.json ontbreekt op de root van de kennisbank")
        return
    register()  # meldt fouten in de bronnen zelf, een keer
    # Tegen de ruwe lijst, niet tegen de goedgekeurde: een bron met een fout wordt al bij het register
    # gemeld, en hier nog eens "bestaat niet" zeggen stuurt de schrijver de verkeerde kant op.
    ruw = json.loads(pad.read_text(encoding="utf-8")).get("bronnen") or {}
    for bid in ids:
        if bid not in ruw:
            fout(readme, "B15", f"bron '{bid}' staat niet in bronnen.json")

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
        if regel.startswith((" ", "	")) and sleutel:
            # Vervolgregel van een waarde over meerdere regels. Zonder dit viel alles na de eerste
            # regel stil weg (een samenvatting werd afgekapt), en een vervolgregel met een dubbele
            # punt erin werd als een verzonnen veld gelezen en dan geweigerd door B2.
            if isinstance(data.get(sleutel), str):
                data[sleutel] = (data[sleutel] + " " + regel.strip()).strip()
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
        # Een stuk en zijn leesversie zijn één bestand in twee vormen: de README linkt de markdown,
        # de pagina de leesversie, en de leesversie linkt zelf terug naar de markdown.
        tweeling = None
        if "/" not in rel and rel.endswith(".md"):
            tweeling = rel[:-3] + ".html"
        elif "/" not in rel and rel.endswith(".html") and (map_ / (rel[:-5] + ".md")).is_file():
            tweeling = rel[:-5] + ".md"
        for pad in bronnen:
            if tweeling and bereikbaar(tweeling, links[pad]):
                continue
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
            # De leesversie van een los stuk maakt deze build zelf (bouw_stukken). Een link ernaar is
            # dus goed zodra de markdown ernaast staat, ook bij de eerste build van een nieuw item.
            wordt_gebouwd = (plek.suffix == ".html" and plek.with_suffix(".md").is_file()
                             and plek.parent == map_ and plek.with_suffix(".md").name != "README.md")
            if not plek.exists() and not wordt_gebouwd:
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
    else:
        for norm in fm["normen"]:
            juist = NORM_ALIAS.get(str(norm).strip().lower())
            if juist and str(norm) != juist:
                fout(readme, "B2", f"norm '{norm}' is een variant van '{juist}'; schrijf hem overal "
                                   "hetzelfde, anders vindt de zoeker maar de helft")
    if isinstance(fm.get("samenvatting"), str) and len(fm["samenvatting"]) < 60:
        fout(readme, "B2", "samenvatting te kort; twee tot vier zinnen, dit wordt de kaarttekst")
    controleer_handleiding(vak, readme, fm)
    controleer_bronnen(readme, fm)
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


# Een item met losse stukken naast de README (een procedure, een brief, een beleidsstuk per domein)
# had alleen een leesversie van de README. Klikte een lezer op een stuk, dan kreeg hij kale markdown
# als platte tekst in de browser. Nu krijgt elk stuk een eigen leesversie met dezelfde naam en .html,
# gemaakt door dit script, zodat hij niet achter kan lopen op de markdown (statuut B3).
STUKBRON_CSS = (
    ".stukbron{font:13px/1.5 system-ui,'Segoe UI',Arial,sans-serif;color:#5a6675;margin:-.2em 0 1.4em}"
    ".stukbron a{color:#154273}"
)


def stukken(map_: Path) -> list[Path]:
    """De losse markdownstukken naast de README, alleen op het niveau van het item zelf."""
    return sorted(p for p in map_.glob("*.md") if p.name != "README.md")


def losse_paginas(map_: Path) -> list[tuple[str, Path]]:
    """HTML-bijlagen zonder markdownbron naast zich, zoals een gegenereerde verkenner: (titel, pad).

    Een leesversie van een stuk staat al via stukken() in de sitemap en llms.txt; een pagina zonder
    markdowntweeling viel daar buiten en was alleen te vinden via de link op de itempagina.
    """
    uit = []
    for p in sorted(map_.glob("*.html")):
        if p.name == "index.html" or p.with_suffix(".md").is_file():
            continue
        m = re.search(r"<title>(.*?)</title>", p.read_text(encoding="utf-8", errors="replace"), re.S)
        uit.append((html.unescape(m.group(1).strip()) if m else p.stem.replace("-", " ").capitalize(), p))
    return uit


def koppel_stukken(tekst: str, map_: Path) -> str:
    """Laat links naar een stuk in dezelfde map naar zijn leesversie wijzen, en README.md naar de pagina."""
    namen = {p.name for p in stukken(map_)}

    def vervang(m: re.Match) -> str:
        kaal, haak, anker = m.group(1).partition("#")
        staart = haak + anker
        if kaal in namen:
            return f'href="{kaal[:-3]}.html{staart}"'
        if kaal == "README.md":
            return f'href="./{staart}"'
        return m.group(0)

    return LINK_HTML.sub(vervang, tekst)


def stuktitel(md: Path) -> tuple[str, str]:
    """De titel van een stuk en de tekst zonder frontmatter; zonder h1 komt de titel erbij."""
    fm, tekst = lees_frontmatter(md.read_text(encoding="utf-8"))
    kop = re.search(r"^# (.+)$", tekst, re.M)
    if kop:
        return kop.group(1).strip(), tekst
    titel = str((fm or {}).get("titel") or md.stem.replace("-", " ").capitalize())
    return titel, f"# {titel}\n\n{tekst.lstrip()}"


def stukpagina(md: Path, vak: str, fm: dict, sectie: dict) -> str:
    """De leesversie van een los stuk: zelfde sjabloon, kruimelpad, favicon, inhoudsopgave en bronvoet
    als de itempagina, met onder de titel de weg terug naar het item en naar de markdown."""
    try:
        import markdown
    except ImportError:
        sys.exit("python-markdown ontbreekt; draai: pip install markdown (nodig voor de leesversie per stuk)")
    titel, tekst = stuktitel(md)
    lichaam = markdown.markdown(tekst, extensions=["tables", "fenced_code", "sane_lists"])
    lichaam = koppel_stukken(lichaam, md.parent)
    item_titel = html.escape(str(fm["titel"]))
    bronregel = (f"<style>{STUKBRON_CSS}</style>"
                 f'<p class="stukbron">Onderdeel van <a href="./">{item_titel}</a> · '
                 f'<a href="{md.name}">Markdown-bron</a></p>')
    sjabloon = (Path(__file__).resolve().parent / "leesversie-sjabloon.html").read_text(encoding="utf-8")
    pagina = sjabloon.replace("$title$", html.escape(titel)).replace("$body$", lichaam)
    pagina = zet_bronvoet(zet_inhoudsopgave(zet_ankers(zorg_voor_ids(zet_huisstijl(zet_favicon(pagina))))), vak,
                          md.parent.name)
    # Na de inhoudsopgave gezet, zodat de weg terug direct onder de titel staat en het blok erna.
    pagina = re.sub(r"(</h1>)", lambda m: m.group(1) + bronregel, pagina, count=1)
    kruimels = kruimels_van_item(fm, sectie)[:-1] + [(str(fm["titel"]), "./"), (titel, "")]
    m = re.search(r"<body[^>]*>", pagina)
    return pagina[: m.end()] + kruimelblok(kruimels) + pagina[m.end():]


def bouw_stukken(items: dict[str, list[dict]], secties: dict, alleen_check: bool) -> list[str]:
    """Schrijf of controleer de leesversie van elk los stuk. Geeft de gewijzigde paden terug."""
    gewijzigd = []
    for vak in VAKGEBIEDEN:
        for fm in items.get(vak, []):
            for md in stukken(fm["_map"]):
                doel = md.with_suffix(".html")
                inhoud = stukpagina(md, vak, fm, secties[vak])
                oud = doel.read_text(encoding="utf-8") if doel.exists() else None
                if oud == inhoud:
                    continue
                if alleen_check:
                    fout(doel, "B3", "de leesversie van dit stuk ontbreekt of loopt achter op de markdown; "
                                     "draai python tools/build.py")
                    continue
                doel.write_bytes(inhoud.encode("utf-8"))
                gewijzigd.append(doel.relative_to(ROOT).as_posix())
    return gewijzigd


def lees_volgorde(tekst: str) -> list[str]:
    """De mapnamen onder '## Volgorde' in de README van een sectie, in de volgorde van de lijst."""
    if "## Volgorde" not in tekst:
        return []
    blok = tekst.split("## Volgorde", 1)[1].split("\n## ")[0]
    return [m.group(1).rstrip("/") for m in re.finditer(r"^\s*\d+\.\s*\[[^\]]+\]\(([^)]+)\)", blok, re.M)]


# Een stuk staat in een sectie, maar hoort soms ook bij een andere: een aanpak over quantumveilige
# cryptografie staat onder governance omdat hij over rollen en besluiten gaat, en een CISO zoekt hem onder
# security. Zo'n verwijzing staat in de README van de sectie onder '## Elders in de kennisbank', als
# lijstregel met een link naar ../<vakgebied>/<item>/. De build controleert dat het doel bestaat en zet
# het als kaart op de sectiepagina.
SECTIE_VERWIJZING = re.compile(r"^\s*-\s*\[[^\]]+\]\(\.\./([a-z0-9-]+)/([a-z0-9-]+)/?\)", re.M)


def lees_elders(tekst: str) -> list[tuple[str, str]]:
    """(vakgebied, item) per verwijzing onder '## Elders in de kennisbank', in de volgorde van de lijst."""
    if "## Elders in de kennisbank" not in tekst:
        return []
    blok = tekst.split("## Elders in de kennisbank", 1)[1].split("\n## ")[0]
    return SECTIE_VERWIJZING.findall(blok)


def controleer_elders(vak: str, sectie: dict, items: dict[str, list[dict]]) -> list[dict]:
    """De items waar een sectie naar verwijst; een verwijzing die nergens heen wijst, blokkeert."""
    readme = ROOT / vak / "README.md"
    uit = []
    for ander, naam in sectie.get("elders") or []:
        if ander == vak:
            fout(readme, "B4", f"'{naam}' staat onder Elders maar hoort in deze sectie zelf; zet het in de volgorde")
            continue
        doel = next((fm for fm in items.get(ander, []) if fm["_map"].name == naam), None)
        if doel is None:
            fout(readme, "B4", f"'../{ander}/{naam}/' onder Elders is geen item in de kennisbank")
        else:
            uit.append(doel)
    return uit


def lees_sectie(vak: str) -> dict:
    readme = ROOT / vak / "README.md"
    if not readme.exists():
        fout(ROOT / vak, "B1", "vakgebied zonder README.md")
        return {"titel": vak.title(), "lead": "", "kort": "", "hoort": []}
    tekst = readme.read_text(encoding="utf-8")
    titel = re.search(r"^# ([^\n]+)$", tekst, re.M)
    lead = re.search(r"^# [^\n]+\n\n((?:[^\n]+\n?)+?)\n\n", tekst)
    hoort = re.findall(r"^- (.+)$", tekst.split("## Wat hoort hier")[-1].split("\n## ")[0], re.M) if "## Wat hoort hier" in tekst else []
    controleer_tekst(readme)
    tekst_lead = lead.group(1).strip().replace("\n", " ") if lead else ""
    kort = tekst_lead.split("op het gebied van ", 1)[-1].split(".")[0].split(":")[0].strip()
    if not kort:
        kort = tekst_lead.split(".")[0].strip()
    if len(kort) > 72:
        kort = kort[:72].rsplit(" ", 1)[0].rstrip(",;")
    return {"titel": titel.group(1).strip() if titel else vak.title(),
            "lead": tekst_lead, "kort": kort[:1].upper() + kort[1:], "hoort": hoort,
            "volgorde": lees_volgorde(tekst), "elders": lees_elders(tekst)}


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
    register()  # ook zonder verwijzende items: een kapotte bron hoort niet te wachten op zijn eerste gebruiker
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
:root{--bg:#f4f6f9;--card:#fff;--ink:#14202b;--muted:#4b5563;--line:#dde3ea;--accent:#154273;--accent2:#2e7d68;
  --navy:#0d2b4d;--oranje:#e17000}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
  font:15px/1.55 system-ui,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
.wrap{max-width:960px;margin:0 auto;padding:0 20px 80px}
.backlink{font-size:14px;margin:0 0 34px;padding:16px 0;color:#c9d6e4;background:var(--navy);
  box-shadow:0 0 0 100vmax var(--navy);clip-path:inset(0 -100vmax)}
.backlink a{color:#fff;text-decoration:none}
.backlink a:hover{text-decoration:underline}
.backlink span{color:#c9d6e4}
header.top{margin-bottom:26px}
header.top::after{content:"";display:block;width:56px;height:4px;border-radius:2px;background:var(--oranje);margin-top:14px}
h1{font-size:clamp(28px,4.2vw,40px);font-weight:800;line-height:1.15;margin:0 0 6px;letter-spacing:-.025em}
.sub{color:var(--muted);font-size:13.5px}
.lead{font-size:16px;color:#33383e;border-left:3px solid var(--accent);padding-left:14px;margin:0 0 26px}
h2{font-size:21px;font-weight:750;margin:38px 0 6px;letter-spacing:-.02em}
h2:first-of-type{margin-top:0}
.h2sub{color:var(--muted);font-size:13.5px;margin:0 0 14px}
p{margin:0 0 11px}
a{color:var(--accent)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px}
a.item{display:block;background:var(--card);border:1px solid var(--line);border-radius:8px;
  padding:16px 18px;text-decoration:none;color:inherit;transition:border-color .12s,box-shadow .12s}
a.item:hover{border-color:var(--accent);box-shadow:0 1px 6px rgba(21,66,115,.10)}
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
.normen{display:flex;flex-wrap:wrap;gap:5px;margin-top:7px}
.norm{font-size:11px;line-height:1.5;color:var(--muted);background:#eef1f5;border:1px solid var(--line);
  border-radius:4px;padding:1px 7px;white-space:nowrap}
ul.hoort{margin:0 0 14px;padding-left:20px;color:#3c434b;font-size:14px}
ul.hoort li{margin-bottom:3px}
.note{background:#fffbe9;border:1px solid #ecd98a;border-radius:6px;padding:11px 14px;font-size:13.5px;margin:16px 0}
.cta{display:inline-block;background:var(--accent);color:#fff;text-decoration:none;font-weight:600;
  font-size:14px;border-radius:6px;padding:9px 18px;margin-top:4px}
.cta:hover{background:#17608f}
.cta.alt{background:#fff;color:var(--accent);border:1px solid var(--line);margin-left:8px}
.cta.alt:hover{border-color:var(--accent)}
.grid[hidden]{display:none}
.vakken{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:10px;margin:0 0 8px}
.vakken a.item{padding:11px 13px}
.vakken .itemtop{margin-bottom:2px}
.vakken .itemtitle{font-size:14.5px}
.vakken .itemdesc{font-size:12.5px;color:var(--muted)}
.filters{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 16px}
.filters[hidden]{display:none}
.filters input,.filters select{font:inherit;font-size:14px;color:var(--ink);background:var(--card);
  border:1px solid var(--line);border-radius:8px;padding:9px 12px}
.filters input{flex:1 1 260px;min-width:0}
.filters select{flex:0 1 auto;max-width:100%}
.filters input:focus,.filters select:focus{outline:2px solid var(--accent);outline-offset:1px;border-color:var(--accent)}
.filters .telling{flex-basis:100%;font-size:13px;color:var(--muted);margin:0}
a.item[hidden]{display:none}
.visueel-verborgen{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);clip-path:inset(50%);white-space:nowrap}
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


_pijlertitels: dict[tuple[str, str], str] = {}


def titel_van_pijler(vak: str, mapnaam: str) -> str:
    """De titel uit de frontmatter van het pijler-item; de mapnaam als die er niet is.

    De mapnaam tonen zou werken maar leest als een pad, en de lezer moet een stuk herkennen aan hoe
    het heet. Gecached omdat elke kaart ernaar vraagt.
    """
    sleutel = (vak, mapnaam)
    if sleutel not in _pijlertitels:
        readme = ROOT / vak / mapnaam / "README.md"
        fm = lees_frontmatter(readme.read_text(encoding="utf-8"))[0] if readme.is_file() else None
        _pijlertitels[sleutel] = str(fm["titel"]) if fm and fm.get("titel") else mapnaam
    return _pijlertitels[sleutel]


def kinderen_van(mapnaam: str, items: list[dict]) -> list[dict]:
    """De stukken die onder deze pijler hangen, in de volgorde waarin ze binnenkomen.

    Geef de lijst mee die `main` na `zet_op_volgorde` heeft; dan is de volgorde de redactionele uit
    `<vak>/README.md` en niet het alfabet.
    """
    return [fm for fm in items if fm.get("pijler") == mapnaam]


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
    # Een stuk dat onder een pijler hangt, zegt dat ook. Anders is het verband alleen zichtbaar voor
    # wie de frontmatter leest, en dat is niemand.
    if fm.get("pijler"):
        delen.append("hoort bij: " + titel_van_pijler(str(fm["_vak"]), str(fm["pijler"])))
    return " · ".join(e(d) for d in delen)


def normbadges(fm: dict) -> str:
    """De normen als losse etiketten onder de metaregel; leeg veld levert niets op."""
    normen = [str(n) for n in (fm.get("normen") or [])]
    if not normen:
        return ""
    binnen = "".join(f'<span class="norm">{e(n)}</span>' for n in normen)
    return f'{NL}    <div class="normen">{binnen}</div>'


def kaart(fm: dict, basis: str, met_vak: bool) -> str:
    link = fm["_link"] if fm["_link"].startswith("http") else basis + fm["_link"]
    tag = {"live": ("tag-live", "live"), "markdown": ("tag-repo", "markdown"), "download": ("tag-repo", "download")}[fm["_weergave"]]
    # data-zoek is de tekst waarop het zoekvak vergelijkt, data-barrieres de sleutel van de zelfcheck.
    # De normen tellen mee in data-zoek: zonder dat vindt wie op NIS2 zoekt alleen de stukken die het
    # woord toevallig in de titel of samenvatting hebben staan.
    zoek = " ".join(str(fm.get(v, "")) for v in ("titel", "samenvatting", "type", "_vak")).lower()
    zoek = (zoek + " " + " ".join(str(n) for n in (fm.get("normen") or [])).lower()).strip()
    bar = " ".join(fm.get("barrieres") or [])
    return f"""  <a class="item" href="{e(link)}" data-vak="{e(fm['_vak'])}" data-zoek="{e(zoek)}" data-barrieres="{e(bar)}">
    <span class="itemtop">
      <span class="itemtitle">{e(fm['titel'])}</span>
      <span class="tag {tag[0]}">{tag[1]}</span>
    </span>
    <p class="itemdesc">{e(fm['samenvatting'])}</p>
    <div class="meta">{meta_regel(fm, met_vak)}</div>{normbadges(fm)}
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


def zoekbalk(items: list[dict]) -> str:
    """Een zoekvak en een keuzelijst met barrieres. Geen vakgebiedfilter meer.

    Filteren op vakgebied, type of norm onderscheidt niets: die zitten allemaal in een hoek (48 van de
    51 items onder security, 41 handleidingen, BIO2 op 49). De barriere spreidt wel, en het is dezelfde
    sleutel die de zelfcheck gebruikt, dus wie daarvandaan komt herkent hem.

    Een norm blijft daarom een zoekterm en geen keuzelijst: BIO2 staat op 49 van de 52 items en zegt
    dus niets, terwijl de staart (NIS2 op 6, de rest op 1 of 2) precies is wat iemand zoekt. Die staart
    zit in `data-zoek` van elke kaart.
    """
    bekend = barrieres()
    tellingen: dict[str, int] = {}
    for fm in items:
        for b in fm.get("barrieres") or []:
            tellingen[b] = tellingen.get(b, 0) + 1
    opties = ['  <option value="">Alle barrieres</option>']
    for b in sorted(tellingen, key=lambda x: bekend.get(x, x).lower()):
        opties.append(f'  <option value="{e(b)}">{e(bekend.get(b, b))} ({tellingen[b]})</option>')
    return ('<div class="filters" id="filters" hidden>' + NL
            + '  <label class="visueel-verborgen" for="zoek">Zoeken</label>' + NL
            + '  <input type="search" id="zoek" placeholder="Bijvoorbeeld: wachtwoord, NIS2 of VNG beleid"'
            + ' autocomplete="off">' + NL
            + '  <label class="visueel-verborgen" for="barriere">Barriere</label>' + NL
            + '  <select id="barriere">' + NL + NL.join(opties) + NL + '  </select>' + NL
            + f'  <p class="telling" id="telling" aria-live="polite">{len(items)} stukken</p>' + NL
            + '</div>')


# Zonder JavaScript blijft de balk verborgen en staat gewoon alles er; het script haalt hem tevoorschijn.
FILTER_JS = """
(function () {
  var balk = document.getElementById('filters');
  var grid = document.getElementById('direct-te-lezen');
  if (!balk || !grid) return;
  var zoek = document.getElementById('zoek');
  var keuze = document.getElementById('barriere');
  var telling = document.getElementById('telling');
  var leeg = document.getElementById('filter-leeg');
  var kaarten = [].slice.call(grid.querySelectorAll('a.item'));
  var elders = document.getElementById('bij-anderen');
  var eldersKop = document.getElementById('bij-anderen-kop');
  var eldersUitleg = document.getElementById('bij-anderen-uitleg');
  var bronnen = elders ? [].slice.call(elders.querySelectorAll('li')) : [];

  // Accenten, koppeltekens en leestekens tellen niet mee: continuiteit vindt continuïteit,
  // backup vindt back-up, en "(bcm)" is gewoon het woord bcm.
  function norm(s) {
    return ' ' + (s || '').toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g, '')
      .replace(/-/g, '').replace(/[^a-z0-9]+/g, ' ').trim() + ' ';
  }
  var groepen = [];
  try {
    groepen = JSON.parse(document.getElementById('synoniemen').textContent).map(function (g) {
      return g.map(function (w) { return norm(w).trim(); });
    });
  } catch (e) { groepen = []; }
  kaarten.forEach(function (k) { k._zoek = norm(k.getAttribute('data-zoek')); });
  bronnen.forEach(function (b) { b._zoek = norm(b.getAttribute('data-zoek')); });

  // Een zoekwoord mag ook als synoniem voorkomen: cbw vindt Cyberbeveiligingswet.
  function varianten(woord) {
    var uit = [woord];
    groepen.forEach(function (g) {
      if (g.indexOf(woord) !== -1) g.forEach(function (w) { if (uit.indexOf(w) === -1) uit.push(w); });
    });
    return uit;
  }
  // Korte woorden (ai, bio, vng) alleen aan het begin van een woord, anders vindt ai elk woord
  // met die twee letters erin. Langere woorden overal, want samenstellingen moeten gevonden
  // worden: beleid in wachtwoordbeleid.
  function komtVoor(tekst, w) {
    return w.length <= 3 ? tekst.indexOf(' ' + w) !== -1 : tekst.indexOf(w) !== -1;
  }
  // Elk woord moet ergens voorkomen, in willekeurige volgorde: "vng beleid" vindt het
  // beleidssjabloon van de IBD, ook al staat er nergens "vng beleid" achter elkaar.
  function past(tekst, woorden) {
    for (var i = 0; i < woorden.length; i++) {
      var alt = woorden[i], raak = false;
      for (var j = 0; j < alt.length && !raak; j++) raak = komtVoor(tekst, alt[j]);
      if (!raak) return false;
    }
    return true;
  }

  function pas() {
    var term = norm(zoek.value).trim();
    var woorden = term === '' ? [] : term.split(' ').map(varianten);
    var bar = keuze.value;
    var n = 0;
    kaarten.forEach(function (kaart) {
      var tekst = kaart._zoek;
      var barrieres = ' ' + (kaart.getAttribute('data-barrieres') || '') + ' ';
      var mee = past(tekst, woorden) &&
                (bar === '' || barrieres.indexOf(' ' + bar + ' ') !== -1);
      kaart.hidden = !mee;
      if (mee) n++;
    });
    // De stukken van anderen verschijnen pas bij een zoekterm; een lijst van honderden regels
    // zonder vraag erbij helpt niemand. Een barriere is een sleutel van de eigen handleidingen,
    // dus met een barriere gekozen blijven ze weg.
    var m = 0;
    bronnen.forEach(function (li) {
      var mee = woorden.length > 0 && bar === '' && past(li._zoek, woorden);
      li.hidden = !mee;
      if (mee) m++;
    });
    if (elders) {
      elders.hidden = m === 0;
      eldersKop.textContent = m === 0 ? 'Bij anderen' : 'Bij anderen: ' + m + (m === 1 ? ' stuk' : ' stukken');
      eldersUitleg.hidden = m !== 0 && woorden.length > 0;
    }
    grid.hidden = n === 0;
    if (leeg) leeg.hidden = n !== 0 || m !== 0;
    telling.textContent = (n === kaarten.length
      ? kaarten.length + ' stukken'
      : n + ' van de ' + kaarten.length + ' stukken') +
      (woorden.length > 0 && bronnen.length ? ', en ' + m + ' bij anderen' : '');
  }

  zoek.addEventListener('input', pas);
  keuze.addEventListener('change', pas);
  balk.hidden = false;
  pas();
})();
"""


def bouw_sectie(vak: str, sectie: dict, items: list[dict], elders: list[dict] | None = None) -> str:
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
    if elders:
        ks = "".join(kaart(x, "../", True) for x in elders)
        grid += ('<h3 class="groep" id="elders-in-de-kennisbank">Elders in de kennisbank, ook voor dit vakgebied</h3>' + NL
                 + f'<div class="grid">{NL}{NL}{ks}{NL}</div>' + NL)
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


def bij_anderen() -> str:
    """De stukken van andere partijen uit het register, doorzoekbaar vanuit hetzelfde zoekvak.

    Een wegwijzer helpt wie een onderwerp heeft. Wie een soort stuk van een bepaalde partij zoekt
    ("iets van de VNG over beleid") vond die tot 25-09-2026 niet: de zoekbalk doorzocht alleen de
    eigen stukken. Zonder JavaScript staat de lijst gewoon open; het script verbergt hem tot er een
    zoekterm is.
    """
    bronnen, ptn = register()
    extra = zoekwoorden()
    actief = sorted(((bid, b) for bid, b in bronnen.items() if not b.get("vervallen")),
                    key=lambda x: (str(x[1].get("partij")), x[1]["titel"].lower()))
    if not actief:
        return ""
    partijen_n = len({b["partij"] for _, b in actief})
    regels = []
    for bid, b in actief:
        p = ptn.get(b["partij"])
        naam = p["naam"] if p else b["partij"]
        slot = (f' <span class="slot">inlog: {e(b.get("kring", ""))}</span>' if b.get("toegang") == "inlog" else "")
        regels.append(f'  <li data-zoek="{e(bron_zoektekst(b, p, extra.get(b["partij"], [])))}">'
                      f'<a href="{e(b["url"])}">{e(b["titel"])}</a> <span class="partij">{e(naam)}</span>{slot}</li>')
    return (f'<h2 id="bij-anderen-kop">Bij anderen</h2>' + NL
            + f'<p class="h2sub" id="bij-anderen-uitleg">Daarnaast {len(actief)} stukken van {partijen_n} andere '
            + 'partijen in het stelsel, zoals de IBD en CIP: handreikingen, sjablonen en factsheets. Typ '
            + 'hierboven een zoekterm en ze verschijnen hier, met een link naar de partij zelf.</p>' + NL
            + '<ul class="bij-anderen" id="bij-anderen">' + NL + NL.join(regels) + NL + '</ul>')


BIJ_ANDEREN_CSS = """
.bij-anderen{list-style:none;margin:0 0 18px;padding:0;border:1px solid var(--line);border-radius:8px;background:var(--card)}
.bij-anderen li{padding:9px 13px;border-top:1px solid var(--line);font-size:14px;line-height:1.45}
.bij-anderen li:first-child{border-top:0}
.bij-anderen li[hidden],.bij-anderen[hidden]{display:none}
.bij-anderen a{color:var(--accent);text-decoration:none}
.bij-anderen a:hover{text-decoration:underline}
.bij-anderen .partij{color:var(--muted);font-size:12.5px;margin-left:6px;white-space:nowrap}
.bij-anderen .slot{font-size:12px;color:#7a4b00;background:#fff4e0;border:1px solid #f0d9ad;border-radius:4px;padding:0 6px;margin-left:4px}
"""


def bouw_root(secties: dict[str, dict], items: dict[str, list[dict]]) -> str:
    live = [i for v in VAKGEBIEDEN for i in items[v] if i["_weergave"] == "live"]
    kaarten_live = "".join(kaart(i, "", True) for i in live)
    balk = zoekbalk(live)
    # De uitleg boven het zoekvak zegt wat het doorzoekt. Zonder die regel las het vak als een filter op
    # de kaarten eronder, en wist een bezoeker niet dat de stukken van de IBD en CIP er ook in zitten
    # (route-test 26-09-2026).
    bronnen_actief = [b for b in register()[0].values() if not b.get("vervallen")]
    n_partijen = len({b["partij"] for b in bronnen_actief})
    zoek_uitleg = (f"Zoek op onderwerp, norm of partij. Het zoekvak doorzoekt de {len(live)} stukken hieronder"
                   + (f" en {len(bronnen_actief)} stukken van {n_partijen} andere partijen, zoals de IBD, CIP en "
                      "het Rijk" if bronnen_actief else "")
                   + ". Zonder zoekterm zie je de stukken met een eigen pagina.")
    kaarten_secties = ""
    for vak in VAKGEBIEDEN:
        n = len(items[vak])
        tag = '<span class="tag tag-leeg">nog leeg</span>' if n == 0 else f'<span class="tag tag-repo">{n} {"stuk" if n == 1 else "stukken"}</span>'
        kaarten_secties += f"""  <a class="item" href="{vak}/">
    <span class="itemtop">
      <span class="itemtitle">{e(secties[vak]['titel'])}</span>
      {tag}
    </span>
    <p class="itemdesc">{e(secties[vak]['kort'])}</p>
  </a>
"""
    body = f"""<header class="top">
  <h1>Kennisbank</h1>
  <div class="sub">Security Commons NL · werkende kennis uit de publieke sector</div>
</header>

<p class="lead">Memo's, rapportages, aanpakken, trainingen en datasets die al gebruikt zijn in echte
organisaties, geanonimiseerd gedeeld door professionals. Geen theorie. Alles herbruikbaar onder EUPL-1.2.</p>

<h2>Waar zoek je in?</h2>
<p class="h2sub">Vier vakgebieden. De telling is de stand van vandaag; staat er "nog leeg",
dan is dat een uitnodiging en geen fout.</p>

<div class="vakken">

{kaarten_secties}
</div>

<h2>Zoek in de kennisbank</h2>
<p class="h2sub">{zoek_uitleg}</p>

{balk}

<div class="grid" id="direct-te-lezen">

{kaarten_live}
</div>

<style>{BIJ_ANDEREN_CSS}</style>
{bij_anderen()}
{synoniemen_blok()}

<p class="h2sub" id="filter-leeg" hidden>Niets gevonden. Probeer een ander woord, of zet de barriere terug op
alle. Zoek je iets dat er niet is? <a href="https://github.com/security-commons-nl/.github/discussions">Vraag het
in Halen en brengen</a>; je naam en je organisatie hoeven daar niet bij.</p>

<p class="h2sub">Handleidingen per barriere uit de zelfcheck staan bij <a href="security/#handleidingen">Security</a>, en met de alternatieven ernaast op <a href="https://security-commons-nl.github.io/aanvalspaden/normen/">Van aanvalspad naar norm</a>.</p>

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
</div>

<script>{FILTER_JS}</script>"""
    return pagina("Kennisbank · Security Commons NL",
                  "Werkende kennis uit de publieke sector: security, privacy, continuïteit en governance. Open herbruikbaar onder EUPL-1.2.",
                  f"{SITE}/", body,
                  [("Security Commons NL", HOOFDPAGINA), ("Kennisbank", "")])


KRUIMEL_CSS = (
    ".kruimel{font:13px/1.5 system-ui,'Segoe UI',Arial,sans-serif;margin:0 0 1.2em;color:#5a6675}"
    ".kruimel a{color:#154273;text-decoration:none}"
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

# Huisstijl op het scherm: zie tools/huisstijl.py, de enige plek voor die opmaak. Een leesversie krijgt de
# volle huisstijl, een instrument met eigen ontwerp alleen letter, kleurtokens en de balk met het kruimelpad.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import huisstijl  # noqa: E402

HUISSTIJL_START, HUISSTIJL_EIND, HUISSTIJL_CSS = huisstijl.START, huisstijl.EIND, huisstijl.LEESVERSIE_CSS


def zet_huisstijl(tekst: str) -> str:
    """Huisstijl en zo nodig een viewport in de </head>. Idempotent."""
    return huisstijl.zet(tekst)

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
    ".inhoud a{color:#154273;text-decoration:none}"
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

    return re.sub(r"<(h[234])(?![^>]*\bid=)([^>]*)>(.*?)</\1>",
                  lambda m: f'<{m.group(1)} id="{slug(m.group(3))}"{m.group(2)}>{m.group(3)}</{m.group(1)}>',
                  tekst, flags=re.S)


# Ankers: elke kop op niveau 2 tot en met 4 en elk punt van een genummerde lijst onder een genummerde
# kop ("5. ..." of "3.2 ...") krijgt een vaste plek waar je naar kunt linken, en een #-link die bij aanwijzen
# verschijnt en de link kopieert. Een punt dat een BIO-maatregel noemt ([8.13.01]) of onder het hoofdstuk
# Beleidsregels staat, heet een eis (eis-5-4, eis-3-2-4), elders een punt (punt-5-4).
MAATREGELTAG = re.compile(r"\[\d\.\d{2}\.\d{2}(?:,\s*\d\.\d{2}\.\d{2})*\]")
ANKER_START = "<!-- ankers -->"
ANKER_EIND = "<!-- /ankers -->"
ANKER = re.compile(r'<a class="anker" href="#[^"]*" aria-label="[^"]*">#</a>')
ANKER_CSS = (
    ".anker{margin-left:.35em;color:#8a96a3;text-decoration:none;font-weight:400;opacity:0}"
    "h2:hover>.anker,h3:hover>.anker,h4:hover>.anker,li:hover>.anker,.anker:focus{opacity:1}"
    "@media (hover:none){.anker{opacity:.45}}"
    ".anker.gekopieerd::after{content:' gekopieerd';font-size:.8em}"
    ":target{scroll-margin-top:1em}li:target{background:#fff3c4}"
    "@media print{.anker{display:none}}"
)
ANKER_JS = (
    "document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a.anker');"
    "if(!a||!navigator.clipboard)return;var u=location.href.split('#')[0]+a.getAttribute('href');"
    "navigator.clipboard.writeText(u).then(function(){a.classList.add('gekopieerd');"
    "setTimeout(function(){a.classList.remove('gekopieerd')},1500)},function(){})});"
)


def kale_kop(kop: str) -> str:
    """De tekst van een kop zonder #-link en zonder tags."""
    return re.sub(r"<[^>]+>", "", ANKER.sub("", kop)).strip()


def zet_ankers(tekst: str) -> str:
    """Ids op genummerde punten, #-links bij koppen en punten, en het stijl- en scriptblok. Idempotent."""
    tekst = re.sub(re.escape(ANKER_START) + ".*?" + re.escape(ANKER_EIND), "", tekst, flags=re.S)
    tekst = ANKER.sub("", tekst)
    gebruikt = set(re.findall(r'id="([^"]+)"', tekst))
    uit, pos = [], 0
    hoofdstuk, nummer, stapel = "", None, []
    patroon = re.compile(r"<(h[234])\b[^>]*>(.*?)</\1>|<(ol|ul)\b([^>]*)>|</(ol|ul)>|<li\b([^>]*)>", re.S)
    for m in patroon.finditer(tekst):
        uit.append(tekst[pos:m.start()])
        pos = m.end()
        stuk = m.group(0)
        if m.group(1):
            kop = kale_kop(m.group(2))
            n = re.match(r"^(\d+(?:\.\d+)*)\.?\s", kop)
            nummer = n.group(1) if n else None
            if m.group(1) == "h2":
                hoofdstuk = kop
            stapel = []
            k = re.search(r'\bid="([^"]+)"', stuk)
            if k:
                stuk = re.sub(r"(</h[234]>)$", f'<a class="anker" href="#{k.group(1)}" aria-label="Link naar deze kop">#</a>'
                              + r"\1", stuk)
        elif m.group(3):
            start = re.search(r'\bstart="(\d+)"', m.group(4) or "")
            stapel.append([m.group(3), int(start.group(1)) - 1 if start else 0])
        elif m.group(5):
            if stapel:
                stapel.pop()
        elif stapel and stapel[-1][0] == "ol" and len(stapel) == 1 and nummer:
            stapel[-1][1] += 1
            if "id=" not in (m.group(6) or ""):
                inhoud = re.split(r"</li>|<li\b|<ol\b|<ul\b", tekst[m.end():], maxsplit=1)[0]
                eis = re.search(r"beleidsregels", hoofdstuk, re.I) or MAATREGELTAG.search(inhoud)
                soort = "eis" if eis else "punt"
                anker = f"{soort}-{nummer.replace('.', '-')}-{stapel[-1][1]}"
                if anker not in gebruikt:
                    gebruikt.add(anker)
                    stuk = f'<li id="{anker}"{m.group(6) or ""}>'
        uit.append(stuk)
    uit.append(tekst[pos:])
    tekst = "".join(uit)
    # Een #-link aan het eind van elk punt met een anker, voor het sluiten van het punt.
    tekst = re.sub(r'(<li id="((?:eis|punt)-[0-9-]+)"[^>]*>)(.*?)(?=</li>|<ol\b|<ul\b)',
                   lambda m: m.group(1) + m.group(3).rstrip() +
                   f' <a class="anker" href="#{m.group(2)}" aria-label="Link naar dit punt">#</a>',
                   tekst, flags=re.S)
    # In de head: daar schuift het niet mee met wat later voor </body> wordt gezet (de bronvoet).
    if 'class="anker"' not in tekst or "</head>" not in tekst:
        return tekst
    blok = f"{ANKER_START}<style>{ANKER_CSS}</style><script data-ankers>{ANKER_JS}</script>{ANKER_EIND}"
    return tekst.replace("</head>", blok + "</head>", 1)


def inhoudsopgave(tekst: str) -> str:
    """Een lijst met de h2-koppen van de leesversie, als navigatie naast de tekst."""
    koppen = re.findall(r'<h2 id="([^"]+)"[^>]*>(.*?)</h2>', tekst, re.S)
    if not koppen:
        return ""
    items = "".join(
        f'<li><a href="#{h}">{kale_kop(k)}</a></li>' for h, k in koppen
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
    ".bronvoet a{color:#154273}"
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


PIJLER_CSS = (
    ".pijlerblok{font:14px/1.6 system-ui,'Segoe UI',Arial,sans-serif;margin:0 0 1.6em;padding:.9em 1.1em;"
    "background:#f4f7fa;border-left:3px solid #154273;border-radius:0 3px 3px 0}"
    ".pijlerblok b{display:block;margin-bottom:.4em;color:#154273}"
    ".pijlerblok ul{margin:0;padding-left:1.2em}"
    ".pijlerblok li{margin:.2em 0}"
    ".pijlerblok a{color:#154273}"
    ".pijlerblok .rol{color:#5a6675}"
)


def na_de_titel(tekst: str) -> int | None:
    """Positie vlak na de eerste </h1> die echt op de pagina staat, of None.

    Een instrument bouwt zijn kop met JavaScript; de enige </h1> in de bron staat dan in het
    <noscript>-blok of in een sjabloon binnen een <script>. Daar iets invoegen levert een etiket op
    dat niemand ziet, of erger, het komt midden in de code terecht. Zo'n pagina krijgt geen blok.
    """
    verboden = [(m.start(), m.end())
                for m in re.finditer(r"<(script|noscript)\b[^>]*>.*?</\1>", tekst, re.S | re.I)]
    for m in re.finditer(r"</h1>", tekst):
        if not any(a < m.start() < b for a, b in verboden):
            return m.end()
    return None


def pijlerblok(kinderen: list[dict]) -> str:
    """De stukken die onder deze pijler hangen, boven aan de leesversie van de pijler zelf."""
    regels = "".join(
        f'<li><a href="../{e(fm["_map"].name)}/">{e(fm["titel"])}</a>'
        + (f' <span class="rol">{e(fm["rol"])}</span>' if fm.get("rol") else "")
        + "</li>"
        for fm in kinderen
    )
    return (PIJLER_START + f"<style>{PIJLER_CSS}</style>"
            + '<aside class="pijlerblok"><b>Hieronder hangen deze stukken</b>'
            + f"<ul>{regels}</ul></aside>" + PIJLER_EIND)


def zet_pijlerblok(tekst: str, kinderen: list[dict]) -> str:
    """Zet, vernieuw of verwijder het pijlerblok onder de titel. Idempotent.

    Geen kinderen betekent geen blok: een pijler die er geen heeft, is gewoon een stuk. Zonder deze
    regel blijft een leeg kader staan zodra het laatste kind van pijler wisselt.
    """
    tekst = re.sub(re.escape(PIJLER_START) + ".*?" + re.escape(PIJLER_EIND), "", tekst, flags=re.S)
    if not kinderen:
        return tekst
    plek = na_de_titel(tekst)
    if plek is None:
        return tekst
    return tekst[:plek] + pijlerblok(kinderen) + tekst[plek:]


NORM_CSS = (
    ".normenregel{font:13px/1.6 system-ui,'Segoe UI',Arial,sans-serif;color:#5a6675;margin:0 0 1.4em}"
    ".normenregel b{color:#154273;font-weight:600}"
    ".normenregel .norm{display:inline-block;background:#eef1f5;border:1px solid #d0d7e2;border-radius:4px;"
    "padding:0 7px;margin-left:5px;white-space:nowrap}"
)


def normenregel(normen: list[str]) -> str:
    """De normen van dit stuk, onder de titel van de leesversie.

    Het veld is verplicht (statuut B2) en wordt bij elk item ingevuld, maar het stond alleen in de
    frontmatter. Wie wil weten of een stuk iets met NIS2 te maken heeft, moest de bron openen.
    """
    etiketten = "".join(f'<span class="norm">{e(n)}</span>' for n in normen)
    return (NORM_START + f"<style>{NORM_CSS}</style>"
            + f'<p class="normenregel"><b>Normen</b>{etiketten}</p>' + NORM_EIND)


def zet_normen(tekst: str, normen: list[str]) -> str:
    """Zet, vernieuw of verwijder de normenregel onder de titel. Idempotent.

    Een leeg veld levert geen regel op; anders blijft er een kop zonder inhoud staan zodra de laatste
    norm van een stuk verdwijnt.
    """
    tekst = re.sub(re.escape(NORM_START) + ".*?" + re.escape(NORM_EIND), "", tekst, flags=re.S)
    if not normen:
        return tekst
    plek = na_de_titel(tekst)
    if plek is None:
        return tekst
    return tekst[:plek] + normenregel(normen) + tekst[plek:]


ELDERS_CSS = (
    ".elders{font:14px/1.6 system-ui,'Segoe UI',Arial,sans-serif;margin:2.4em 0 1.2em;padding:.9em 1.1em;"
    "background:#f4f7fa;border-left:3px solid #154273;border-radius:0 3px 3px 0}"
    ".elders b.elders-kop{display:block;margin-bottom:.2em;color:#154273}"
    ".elders p.uitleg{margin:0 0 .5em;color:#5a6675;font-size:13px}"
    ".elders ul{margin:0;padding-left:1.2em}"
    ".elders li{margin:.3em 0}"
    ".elders a{color:#154273}"
    ".elders .partij{color:#5a6675}"
    ".elders .slot{display:inline-block;font-size:12px;color:#7a4b00;background:#fff4e0;border:1px solid #f0d9ad;"
    "border-radius:4px;padding:0 6px;margin-left:4px;white-space:nowrap}"
    "@media print{.elders{background:none;border-left:1px solid #999}}"
)


def eldersregel(bron: dict, partij: dict | None) -> str:
    """Een verwijzing: titel met link, de partij, en wat de lezer moet weten over de toegang.

    Een vervallen bron wijst naar de partij zelf, met de datum waarop het stuk er nog stond en zo
    mogelijk een archiefversie. Zo wordt een dode link een aanwijzing waar je verder moet zoeken.
    """
    naam = e(partij["naam"]) if partij else e(bron.get("partij", ""))
    if bron.get("vervallen") and partij and partij.get("url"):
        archief = (f' · <a href="{e(bron["archief"])}">archiefversie</a>' if bron.get("archief") else "")
        return (f'<li>{e(bron["titel"])} <span class="partij">stond tot {e(bron["vervallen"])} bij '
                f'<a href="{e(partij["url"])}">{naam}</a>; zoek daar verder</span>{archief}</li>')
    slot = ""
    if bron.get("toegang") == "inlog":
        slot = f'<span class="slot">\U0001F512 inlog: {e(bron.get("kring", ""))} · gezien {e(bron["gezien"])}</span>'
    elif bron.get("toegang") == "onbekend":
        slot = '<span class="slot">toegang niet vastgesteld</span>'
    return (f'<li><a href="{e(bron["url"])}">{e(bron["titel"])}</a> '
            f'<span class="partij">· {naam}</span>{slot}</li>')


def eldersblok(ids: list[str]) -> str:
    """Het blok onderaan de leesversie: wat andere partijen al hebben over hetzelfde onderwerp."""
    bronnen, ptn = register()
    regels = "".join(eldersregel(bronnen[b], ptn.get(bronnen[b]["partij"])) for b in ids if b in bronnen)
    return (ELDERS_START + f"<style>{ELDERS_CSS}</style>"
            + '<aside class="elders"><b class="elders-kop">Wat anderen al hebben</b>'
            + '<p class="uitleg">Andere partijen in het stelsel over hetzelfde onderwerp. '
            + 'Dit stuk vult ze aan en vervangt ze niet.</p>'
            + f"<ul>{regels}</ul></aside>" + ELDERS_EIND)


def zet_elders(tekst: str, ids: list[str]) -> str:
    """Zet, vernieuw of verwijder het bronnenblok vlak boven de bronvoet. Idempotent.

    Onderaan en niet onder de titel: de lezer komt voor dit stuk, en de verwijzingen zijn de volgende
    stap. Staat er geen bronvoet (een pagina zonder </body>), dan blijft het blok weg; dat meldt de
    bronvoet-controle al.
    """
    tekst = re.sub(re.escape(ELDERS_START) + ".*?" + re.escape(ELDERS_EIND), "", tekst, flags=re.S)
    if not ids or BRON_START not in tekst:
        return tekst
    return tekst.replace(BRON_START, eldersblok(ids) + BRON_START, 1)


# Bewijsregel: welke maatregelen een stuk helpt aantonen, via zijn barrieres en de mappingen van de
# aanvalspaden. Het veld `normen` zegt alleen "BIO2"; deze regel zegt welke maatregel, met een link naar
# de normwijzer. Zelfde relatie als de mappingen: levert bewijs voor, nooit voldoet aan.
BEWIJS_START = "<!-- bewijs-voor -->"
BEWIJS_EIND = "<!-- /bewijs-voor -->"
NORMWIJZER = "https://security-commons-nl.github.io/normen/normwijzer.html"
MAPPING_KADERS = (("bio2", "BIO"), ("nist-csf", "NIST CSF"), ("avg", "AVG"), ("wpg", "Wpg"))
_mappingen_cache: dict[str, dict[str, list[str]]] | None = None


def mappingen() -> dict[str, dict[str, list[str]]]:
    """kader -> barriere -> maatregelen waarvoor de barriere bewijs levert (volledig of gedeeltelijk).

    Een raakvlak telt niet: dat is in de mappingen uitdrukkelijk geen bewijs. Leeg als de aanvalspaden
    nergens staan; dan krijgt een leesversie gewoon geen bewijsregel.
    """
    global _mappingen_cache
    if _mappingen_cache is not None:
        return _mappingen_cache
    uit: dict[str, dict[str, list[str]]] = {}
    for kandidaat in (ROOT.parent / "aanvalspaden" / "mappingen", ROOT / "_aanvalspaden" / "mappingen"):
        if kandidaat.is_dir():
            for kader, _ in MAPPING_KADERS:
                pad = kandidaat / f"{kader}.json"
                if not pad.is_file():
                    continue
                per_b: dict[str, list[str]] = {}
                for r in json.loads(pad.read_text(encoding="utf-8")).get("regels", []):
                    if r.get("sterkte") in ("volledig", "gedeeltelijk"):
                        lijst = per_b.setdefault(r["barriere"], [])
                        if r["norm"] not in lijst:
                            lijst.append(r["norm"])
                uit[kader] = per_b
            break
    _mappingen_cache = uit
    return uit


def bewijs_voor(barrieres_: list[str]) -> list[tuple[str, str]]:
    """(kader, maatregel) waarvoor de barrieres van een stuk bewijs leveren, per kader op nummer."""
    maps = mappingen()
    uit: list[tuple[str, str]] = []
    for kader, _ in MAPPING_KADERS:
        gezien: list[str] = []
        for b in barrieres_:
            for n in maps.get(kader, {}).get(b, []):
                if n not in gezien:
                    gezien.append(n)
        def sleutel(n: str) -> list:
            return [int(x) if x.isdigit() else x for x in re.split(r"[.\-]", n)]
        uit += [(kader, n) for n in sorted(gezien, key=sleutel)]
    return uit


BEWIJS_CSS = (
    ".bewijsregel{font:13px/1.8 system-ui,'Segoe UI',Arial,sans-serif;color:#5a6675;margin:-.8em 0 1.4em}"
    ".bewijsregel b{color:#1c6b4a;font-weight:600;margin-right:4px}"
    ".bewijsregel a.maatregel{display:inline-block;background:#e6f2ee;border:1px solid #a8d5bd;border-radius:4px;"
    "padding:0 7px;margin:0 0 0 5px;color:#1c6b4a;text-decoration:none;white-space:nowrap;line-height:1.6}"
    ".bewijsregel a.maatregel:hover{text-decoration:underline}"
    ".bewijsregel .kader{margin-left:10px}"
)


def bewijsregel(paren: list[tuple[str, str]]) -> str:
    namen = dict(MAPPING_KADERS)
    delen = []
    for kader, _ in MAPPING_KADERS:
        nrs = [n for k, n in paren if k == kader]
        if not nrs:
            continue
        links = "".join(f'<a class="maatregel" href="{NORMWIJZER}#{kader}/{e(n)}">{e(n)}</a>' for n in nrs)
        delen.append(f'<span class="kader">{e(namen[kader])}</span>{links}')
    return (BEWIJS_START + f"<style>{BEWIJS_CSS}</style>"
            + '<p class="bewijsregel"><b>Levert bewijs voor</b>' + "".join(delen) + "</p>" + BEWIJS_EIND)


def zet_bewijs(tekst: str, paren: list[tuple[str, str]]) -> str:
    """Zet, vernieuw of verwijder de bewijsregel onder de titel. Idempotent."""
    tekst = re.sub(re.escape(BEWIJS_START) + ".*?" + re.escape(BEWIJS_EIND), "", tekst, flags=re.S)
    if not paren:
        return tekst
    plek = na_de_titel(tekst)
    if plek is None:
        return tekst
    return tekst[:plek] + bewijsregel(paren) + tekst[plek:]


def zet_kruimelpad(pad: Path, kruimels: list[tuple[str, str]], alleen_check: bool,
                   kinderen: list[dict] | None = None, normen: list[str] | None = None,
                   bronnen: list[str] | None = None, bewijs: list[tuple[str, str]] | None = None) -> bool:
    """Maak de leesversie klaar: geen link naar zichzelf, wel een kruimelpad, favicon,
    inhoudsopgave bij een lang stuk, een pijlerblok bij een pijler en een bronvoet. Idempotent.

    Alles in een functie omdat er een schrijfmoment per bestand moet zijn: twee functies die na
    elkaar hetzelfde bestand bijwerken, melden in --check dezelfde pagina twee keer als fout.
    """
    origineel = pad.read_text(encoding="utf-8")
    eigen = f"{SITE}/{pad.parent.parent.name}/{pad.parent.name}/"
    vak, item = pad.parent.parent.name, pad.parent.name
    tekst = zet_bronvoet(zet_inhoudsopgave(zet_ankers(zorg_voor_ids(
        zet_huisstijl(zet_favicon(verwijder_dubbele_titel(verwijder_zelflink(origineel, eigen))))))), vak, item)
    tekst = koppel_stukken(tekst, pad.parent)
    # Eerst het pijlerblok, dan de normenregel: beide gaan vlak achter </h1>, dus wat als laatste
    # wordt gezet staat bovenaan. De normen zijn een etiket bij de titel, het pijlerblok is een kader.
    tekst = zet_pijlerblok(tekst, kinderen or [])
    # De bewijsregel voor de normen gezet, zodat hij er direct onder komt te staan: eerst het etiket
    # (BIO2), dan welke maatregelen precies.
    tekst = zet_bewijs(tekst, bewijs or [])
    tekst = zet_normen(tekst, [str(n) for n in (normen or [])])
    tekst = zet_elders(tekst, [str(b) for b in (bronnen or [])])
    if BRON_START not in tekst:
        fout(pad, "B10", "geen </body> gevonden; de bronvoet kan er niet in")
        return False
    if tekst != origineel and alleen_check:
        fout(pad, "B3", "leesversie is niet bijgewerkt (zelflink, dubbele titel, favicon, huisstijl, "
                          "inhoudsopgave, pijlerblok, normenregel, bewijsregel, bronnenblok of bronvoet); "
                          "draai python tools/build.py")
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


def sitemap_tekst(items: dict[str, list[dict]]) -> str:
    """Elke pagina van de kennisbank voor zoekmachines: de voorpagina, de secties, elk item met een
    leesversie en de leesversie van elk los stuk. Zonder lastmod, zodat het bestand alleen verandert als
    er een pagina bijkomt of verdwijnt. De sitemap van het domein noemde maar een deel van de items, met
    de hand toegevoegd; robots.txt verwijst naar beide."""
    urls = [f"{SITE}/"]
    for vak in VAKGEBIEDEN:
        if not items.get(vak):
            continue
        urls.append(f"{SITE}/{vak}/")
        for fm in sorted(items[vak], key=lambda f: f["_map"].name):
            if fm["_weergave"] == "live" and not fm["_link"].startswith("http"):
                urls.append(f"{SITE}/{fm['_link']}")
            urls += [f"{SITE}/{vak}/{fm['_map'].name}/{md.stem}.html" for md in stukken(fm["_map"])
                     if md.with_suffix(".html").is_file()]
            urls += [f"{SITE}/{vak}/{fm['_map'].name}/{p.name}" for _, p in losse_paginas(fm["_map"])]
    regels = "".join(f"  <url><loc>{html.escape(u)}</loc></url>\n" for u in urls)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schema/sitemap/0.9">\n' + regels + "</urlset>\n")


def waarschuw_achterstand(secties: dict[str, dict], items: dict[str, list[dict]]) -> None:
    """In --check: zeg het als llms.txt of sitemap.xml achterloopt, maar blokkeer niet.

    Op main maakt de CI ze opnieuw en commit ze, dus een achterstand lost zichzelf op na de merge. De
    waarschuwing is er voor wie lokaal werkt en wil zien wat er na de merge verandert.
    """
    for naam, inhoud in (("llms.txt", llms_tekst(secties, items)), ("sitemap.xml", sitemap_tekst(items))):
        pad = ROOT / naam
        oud = pad.read_text(encoding="utf-8") if pad.exists() else None
        if oud != inhoud:
            print(f"::warning file={naam}::{naam} loopt achter op de items; wordt na de merge op main "
                  "bijgewerkt (of draai python tools/build.py)")


def llms_tekst(secties: dict[str, dict], items: dict[str, list[dict]]) -> str:
    """De hele kennisbank als een lijst voor systemen die lezen in plaats van klikken.

    De root-site had een handgeschreven lijst van veertien stukken naast een kennisbank van 52; wat
    met de hand wordt bijgehouden loopt achter. Dit bestand komt uit dezelfde frontmatter als de
    kaarten, dus het kan niet achterlopen. Per stuk de titel, de URL van de leesversie of de map, de
    samenvatting en de normen, en ingesprongen eronder de losse stukken met hun eigen leesversie.
    """
    regels = ["# Kennisbank van Security Commons NL", "",
              "> Werkende kennis uit de publieke sector: security, privacy, continuiteit en governance,",
              "> geanonimiseerd gedeeld door professionals. Alles herbruikbaar onder EUPL-1.2.", "",
              "Gegenereerd door tools/build.py uit de frontmatter van elk stuk; niet met de hand bewerken.",
              f"Bron: {REPO} . Overname en verwerking door AI-systemen is welkom; vermeld bij voorkeur de bron.", ""]
    for vak in VAKGEBIEDEN:
        lijst = items.get(vak) or []
        if not lijst:
            continue
        regels += [f"## {secties[vak]['titel']}", ""]
        for fm in lijst:
            # _link draagt het vakgebied al ("security/passkeys-invoeren/"), net als op de root-index.
            link = fm["_link"] if fm["_link"].startswith("http") else f"{SITE}/{fm['_link'].lstrip('/')}"
            samenvatting = " ".join(str(fm["samenvatting"]).split())
            normen = ", ".join(str(n) for n in (fm.get("normen") or []))
            staart = f" Normen: {normen}." if normen else ""
            # Ook een systeem dat leest in plaats van klikt, moet zien wat er elders al ligt.
            bronnen, _ = register()
            elders = [bronnen[b]["url"] for b in (fm.get("bronnen") or [])
                      if b in bronnen and not bronnen[b].get("vervallen")]
            if elders:
                staart += " Elders: " + ", ".join(elders) + "."
            regels.append(f"- [{fm['titel']}]({link}): {samenvatting}{staart}")
            # De losse stukken eronder, elk met zijn eigen leesversie: wie een brief, een procedure of
            # het beleid voor één domein zoekt, hoeft niet eerst het item te openen.
            for md in (stukken(fm["_map"]) if fm.get("_map") else []):
                if md.with_suffix(".html").is_file():
                    regels.append(f"  - [{stuktitel(md)[0]}]({SITE}/{vak}/{fm['_map'].name}/{md.stem}.html)")
            for titel, p in (losse_paginas(fm["_map"]) if fm.get("_map") else []):
                regels.append(f"  - [{titel}]({SITE}/{vak}/{fm['_map'].name}/{p.name})")
        regels.append("")
    bronnen, ptn = register()
    actief = sorted((b for b in bronnen.values() if not b.get("vervallen")),
                    key=lambda b: (str(b.get("partij")), b["titel"].lower()))
    if actief:
        regels += ["## Bij anderen", "",
                   "Stukken van andere partijen in het stelsel waar de kennisbank naar verwijst (bronnen.json).", ""]
        for b in actief:
            p = ptn.get(b["partij"])
            regels.append(f"- [{b['titel']}]({b['url']}): {p['naam'] if p else b['partij']}.")
        regels.append("")
    return NL.join(regels)


def main() -> int:
    alleen_check = "--check" in sys.argv
    items = controleer_alles()
    secties = {v: lees_sectie(v) for v in VAKGEBIEDEN if (ROOT / v).is_dir()}
    for vak, sectie in secties.items():
        items[vak] = zet_op_volgorde(vak, items[vak], sectie)
    elders = {vak: controleer_elders(vak, sectie, items) for vak, sectie in secties.items()}
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
            kinderen = kinderen_van(fm["_map"].name, items[vak])
            if html_pad.exists() and zet_kruimelpad(html_pad, kruimels_van_item(fm, secties[vak]),
                                                    alleen_check, kinderen, fm.get("normen") or [],
                                                    fm.get("bronnen") or [],
                                                    bewijs_voor(fm.get("barrieres") or [])):
                kruimel_gewijzigd.append(f"{vak}/{fm['_map'].name}/index.html")
    kruimel_gewijzigd += bouw_stukken(items, secties, alleen_check)
    if fouten:
        print(f"Redactiestatuut: {len(fouten)} overtreding(en). Niets gebouwd.\n")
        for f in fouten:
            print("  " + f)
        return 1

    print(f"Redactiestatuut: geen overtredingen ({totaal} items).")
    if alleen_check:
        waarschuw_achterstand(secties, items)
        return 0
    gewijzigd = list(kruimel_gewijzigd)
    for vak in VAKGEBIEDEN:
        if schrijf(ROOT / vak / "index.html", bouw_sectie(vak, secties[vak], items[vak], elders.get(vak))):
            gewijzigd.append(f"{vak}/index.html")
    if schrijf(ROOT / "index.html", bouw_root(secties, items)):
        gewijzigd.append("index.html")
    if schrijf_handelingsperspectief(items):
        gewijzigd.append("handelingsperspectief.json")
    if schrijf(ROOT / "llms.txt", llms_tekst(secties, items)):
        gewijzigd.append("llms.txt")
    if schrijf(ROOT / "sitemap.xml", sitemap_tekst(items)):
        gewijzigd.append("sitemap.xml")
    print("Gebouwd: " + (", ".join(gewijzigd) if gewijzigd else "niets gewijzigd"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
