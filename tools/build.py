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
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://security-commons-nl.github.io/kennisbank"
REPO = "https://github.com/security-commons-nl/kennisbank"

VAKGEBIEDEN = ["security", "privacy", "bcm", "governance"]
TYPES = ["beleid", "sjabloon", "lesmateriaal", "dataset", "referentie", "aanpak", "rapportage"]
STATUSSEN = ["concept", "in gebruik", "sjabloon", "gearchiveerd"]
VERPLICHT = ["titel", "vakgebied", "type", "normen", "herkomst", "status", "samenvatting"]
TOEGESTAAN = set(VERPLICHT) | {"peildatum", "versie", "licentie"}

# Mappen op root die geen vakgebied zijn maar wel mogen bestaan.
ROOT_MAPPEN_OK = {".git", ".github", ".codesight", "tools"}
ROOT_BESTANDEN_OK = {"README.md", "CONTRIBUTING.md", "ROADMAP.md", "LICENSE", "index.html", ".gitignore", ".nojekyll"}

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
    for bestand in map_.rglob("*"):
        if bestand.suffix in (".md", ".html", ".txt", ".json"):
            controleer_tekst(bestand)
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
    if any(p.suffix == ".md" and p.name != "README.md" for p in map_.iterdir()):
        return "markdown", f"{REPO}/tree/main/{vak}/{map_.name}"
    if any(p.suffix in (".pptx", ".docx", ".xlsx", ".pdf", ".zip") for p in map_.iterdir()):
        return "download", f"{REPO}/tree/main/{vak}/{map_.name}"
    return "markdown", f"{REPO}/tree/main/{vak}/{map_.name}"


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
            "lead": lead.group(1).strip().replace("\n", " ") if lead else "", "hoort": hoort}


def controleer_alles() -> dict[str, list[dict]]:
    items: dict[str, list[dict]] = {v: [] for v in VAKGEBIEDEN}
    for kind in ROOT.iterdir():
        if kind.is_dir():
            if kind.name not in VAKGEBIEDEN and kind.name not in ROOT_MAPPEN_OK:
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
.backlink{font-size:13px;margin:0 0 14px}
.backlink a{color:var(--muted);text-decoration:none}
.backlink a:hover{color:var(--accent)}
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


def pagina(titel: str, beschrijving: str, canonical: str, body: str, backlink: bool) -> str:
    terug = '<p class="backlink"><a href="../">← Kennisbank</a></p>\n\n' if backlink else ""
    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(titel)}</title>
<meta name="description" content="{e(beschrijving)}">
<link rel="canonical" href="{canonical}">
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
    kaarten = "".join(kaart(i, "", False).replace(f'href="{vak}/', 'href="') for i in items)
    grid = f'<div class="grid">\n\n{kaarten}\n</div>' if items else '<p class="h2sub">Nog geen stukken. Heb je iets liggen? Zie hieronder.</p>'
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
    return pagina(f"{sectie['titel']} · Kennisbank · Security Commons NL", sectie["lead"], f"{SITE}/{vak}/", body, True)


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
                  f"{SITE}/", body, False)


def schrijf(pad: Path, inhoud: str) -> bool:
    oud = pad.read_text(encoding="utf-8") if pad.exists() else None
    if oud == inhoud:
        return False
    pad.write_bytes(inhoud.encode("utf-8"))
    return True


def main() -> int:
    alleen_check = "--check" in sys.argv
    items = controleer_alles()
    secties = {v: lees_sectie(v) for v in VAKGEBIEDEN if (ROOT / v).is_dir()}
    if fouten:
        print(f"Redactiestatuut: {len(fouten)} overtreding(en). Niets gebouwd.\n")
        for f in fouten:
            print("  " + f)
        print("\nRegels: https://github.com/security-commons-nl/.github/blob/main/REDACTIESTATUUT.md")
        return 1
    totaal = sum(len(v) for v in items.values())
    print(f"Redactiestatuut: geen overtredingen ({totaal} items).")
    if alleen_check:
        return 0
    gewijzigd = []
    for vak in VAKGEBIEDEN:
        if schrijf(ROOT / vak / "index.html", bouw_sectie(vak, secties[vak], items[vak])):
            gewijzigd.append(f"{vak}/index.html")
    if schrijf(ROOT / "index.html", bouw_root(secties, items)):
        gewijzigd.append("index.html")
    print("Gebouwd: " + (", ".join(gewijzigd) if gewijzigd else "niets gewijzigd"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
