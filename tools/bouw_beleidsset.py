"""Bouwt de beleidsset informatiebeveiliging uit de bouwstenen en de contextvragen.

Gebruik:
    python tools/bouw_beleidsset.py            # schrijft de leesversies, de data en de generatorpagina
    python tools/bouw_beleidsset.py --check    # exit 1 als iets achterloopt of een maatregel niet gedekt is
    python tools/bouw_beleidsset.py --profiel antwoorden.json uitmap/   # een set voor een eigen profiel
    python tools/bouw_beleidsset.py --normen ../normen/bio2.json        # de maatregelkopie bijwerken

Per BIO 2.0-domein staat in `data/` één markdownbestand. Daarin:

- staan in de frontmatter domein, titel, samenvatting en onder `invoeren` een lijst met wat de organisatie
  moet inrichten, elk eindigend op `(hoofdstuk N).`;
- begint elk stuk met doel en reikwijdte en uitgangspunten, staat daarna elk onderwerp als eigen hoofdstuk
  en eindigt het met rollen, naleving en controle, en samenhang (VOOR en ACHTER hieronder), doorlopend
  genummerd;
- eindigt een beleidsregel op de nummers van de maatregelen die hij invult: `[8.13.01]` of
  `[8.13.01, 8.13.02]`. In een onderwerphoofdstuk moet elke regel zo'n nummer hebben;
- is een regel een opsommingsteken (`- `); de generator nummert ze per hoofdstuk, zodat een reviewer of
  een controle naar "eis 5.4" kan wijzen;
- staat bij naleving en controle een controleraamwerk: een tabel met per rij een controle `XXX-01`, en in de
  laatste kolom de maatregelen die de controle aantoont (zonder haken);
- staat tekst die van een contextvraag afhangt tussen `::: als vraag=antwoord` en `:::`. Meer antwoorden
  scheid je met een komma (`hosting=saas,hostingpartij`), meer voorwaarden met ` en `, en `!=` keert om.
  Blokken nesten niet;
- is `[[label: toelichting]]` een invulveld: wat de organisatie zelf moet invullen;
- staat elke afkorting die een stuk gebruikt in `data/afkortingen.json`; de generator zet de gebruikte
  onder het stuk.

Een profiel is een JSON-object met per vraag-id uit `profiel.json` een antwoord-id of, bij een vraag met
meer antwoorden, een lijst. Een vraag zonder antwoord laat het blok staan, met de vraag erboven: zo is de
set zonder antwoorden de leesversie met alle varianten.

Dezelfde rekenregel staat in `tools/beleidsset.js` voor de generatorpagina; `tools/test_beleidsset.py`
houdt de twee gelijk en toetst de dekking: voor elk volledig profiel op de vragen die een domein raakt,
vult de tekst elke maatregel van dat domein (overheidsmaatregel én ISO-beheersmaatregel zonder
overheidsmaatregel) met minstens één regel in, en toont minstens één controle hem aan.
"""
from __future__ import annotations

import itertools
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import beleidsset_word as word  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ITEM = ROOT / "governance" / "beleidsset-informatiebeveiliging"
BOUWSTENEN = ITEM / "data"
PROFIEL = ITEM / "profiel.json"
MAATREGELEN = BOUWSTENEN / "bio2-maatregelen.json"
DATA = ITEM / "beleidsset.json"
PAGINA = ITEM / "beleidsset-generator.html"
SJABLOON = ROOT / "tools" / "beleidsset-generator-sjabloon.html"
JS = ROOT / "tools" / "beleidsset.js"
WORD_JS = ROOT / "tools" / "beleidsset-word.js"

TAG = re.compile(r"\[(\d\.\d{2}\.\d{2}(?:,\s*\d\.\d{2}\.\d{2})*)\]")
NUMMER = re.compile(r"(?<![\d.])(\d\.\d{2}\.\d{2})(?![\d.])")
VELD = re.compile(r"\[\[([^\]:]+?)(?::\s*([^\]]+?))?\]\]")
OPEN = re.compile(r"^::: als (.+)$")
VOORWAARDE = re.compile(r"^([a-z0-9-]+)\s*(!?=)\s*([a-z0-9-]+(?:,[a-z0-9-]+)*)$")
CONTROLE = re.compile(r"^\|\s*([A-Z]{2,5}-\d{2,3})\s*\|")
AFKORTING = re.compile(r"(?<![\w&])([A-Z][A-Z&]{1,7})(?![\w])")
MAX_PROFIELEN = 20000  # bovengrens per domein bij het toetsen van de dekking
# De vaste hoofdstukken: twee vooraan, drie achteraan. Daartussen staan de onderwerpen van het domein, elk als
# eigen hoofdstuk met de beleidsregels.
VOOR = ["Doel en reikwijdte", "Uitgangspunten"]
ACHTER = ["Rollen en verantwoordelijkheden", "Naleving en controle", "Samenhang"]
HOOFDSTUK = re.compile(r"^## (\d+)\. (.+)$")


class BouwsteenFout(Exception):
    """Een bouwsteen klopt niet; de tekst zegt wat en waar."""


# ---------------------------------------------------------------------------------------------
# Inlezen
# ---------------------------------------------------------------------------------------------

def lees_json(pad: Path):
    return json.loads(pad.read_text(encoding="utf-8"))


def frontmatter(tekst: str, waar: str) -> tuple[dict, str]:
    tekst = tekst.replace("\r\n", "\n")
    if not tekst.startswith("---\n"):
        raise BouwsteenFout(f"{waar}: frontmatter ontbreekt")
    kop, _, romp = tekst[4:].partition("\n---\n")
    fm, laatste = {}, None
    for regel in kop.split("\n"):
        if regel.startswith("  - ") and laatste:
            # Een lijst onder een sleutel zonder waarde, zoals invoeren.
            if not isinstance(fm[laatste], list):
                fm[laatste] = []
            fm[laatste].append(regel[4:].strip())
        elif regel.strip():
            sleutel, _, waarde = regel.partition(":")
            laatste = sleutel.strip()
            fm[laatste] = waarde.strip()
    return fm, romp.lstrip("\n")


def parse_voorwaarden(tekst: str, vragen: dict, waar: str) -> list[dict]:
    uit = []
    for deel in tekst.split(" en "):
        m = VOORWAARDE.match(deel.strip())
        if not m:
            raise BouwsteenFout(f"{waar}: voorwaarde '{deel.strip()}' is niet te lezen; schrijf vraag=antwoord")
        vraag, teken, antwoorden = m.group(1), m.group(2), m.group(3).split(",")
        if vraag not in vragen:
            raise BouwsteenFout(f"{waar}: vraag '{vraag}' staat niet in profiel.json")
        geldig = {a["id"] for a in vragen[vraag]["antwoorden"]}
        for a in antwoorden:
            if a not in geldig:
                raise BouwsteenFout(f"{waar}: '{a}' is geen antwoord op '{vraag}' (wel: {', '.join(sorted(geldig))})")
        uit.append({"vraag": vraag, "niet": teken == "!=", "antwoorden": antwoorden})
    return uit


def parse_bouwsteen(tekst: str, vragen: dict, waar: str) -> dict:
    """Een bouwsteen als lijst delen: vaste tekst of een blok met voorwaarden."""
    fm, romp = frontmatter(tekst, waar)
    for veld in ("domein", "titel"):
        if not fm.get(veld):
            raise BouwsteenFout(f"{waar}: frontmatter mist '{veld}'")
    delen, huidig, blok = [], [], None
    for nr, regel in enumerate(romp.split("\n"), 1):
        m = OPEN.match(regel.strip())
        if m:
            if blok is not None:
                raise BouwsteenFout(f"{waar} r.{nr}: blok binnen een blok; blokken nesten niet")
            if huidig:
                delen.append({"als": None, "regels": huidig})
            huidig, blok = [], parse_voorwaarden(m.group(1), vragen, f"{waar} r.{nr}")
            continue
        if regel.strip() == ":::":
            if blok is None:
                raise BouwsteenFout(f"{waar} r.{nr}: ':::' sluit niets af")
            delen.append({"als": blok, "regels": huidig})
            huidig, blok = [], None
            continue
        if regel.count("[[") != regel.count("]]"):
            raise BouwsteenFout(f"{waar} r.{nr}: invulveld loopt over de regel heen; zet [[...]] op één regel")
        if regel.startswith(":::"):
            raise BouwsteenFout(f"{waar} r.{nr}: '{regel.strip()}' is geen blok; schrijf '::: als vraag=antwoord'")
        huidig.append(regel)
    if blok is not None:
        raise BouwsteenFout(f"{waar}: blok zonder afsluitende ':::'")
    if huidig:
        delen.append({"als": None, "regels": huidig})
    invoeren = fm.get("invoeren") or []
    return {"domein": fm["domein"], "titel": fm["titel"], "samenvatting": fm.get("samenvatting", ""),
            "invoeren": invoeren if isinstance(invoeren, list) else [], "delen": delen}


def laad(map_: Path = ITEM) -> dict:
    """Profiel, maatregelen en bouwstenen in één object; dit gaat ook als data naar de pagina."""
    profiel = lees_json(map_ / "profiel.json")
    # Een subvraag (zoals eigen apparaten onder werkplek) wordt een gewone vraag direct na zijn hoofdvraag,
    # zodat een bouwsteen er een blok aan kan hangen en de pagina hem gewoon toont.
    vlak = []
    for v in profiel["vragen"]:
        vlak.append({k: w for k, w in v.items() if k != "subvraag"})
        if v.get("subvraag"):
            vlak.append({"meerdere": False, "doel": "inhoud", **v["subvraag"], "hoort_bij": v["id"]})
    profiel = {**profiel, "vragen": vlak}
    maatregelen = lees_json(map_ / "data" / "bio2-maatregelen.json")
    afkortingen = lees_json(map_ / "data" / "afkortingen.json")
    vragen = {v["id"]: v for v in profiel["vragen"]}
    domeinen = {d["id"]: d for d in profiel["domeinen"]}
    stenen = []
    for pad in sorted((map_ / "data").glob("*.md")):
        steen = parse_bouwsteen(pad.read_text(encoding="utf-8"), vragen, pad.name)
        if steen["domein"] not in domeinen:
            raise BouwsteenFout(f"{pad.name}: domein '{steen['domein']}' staat niet in profiel.json")
        steen["bestand"] = pad.name
        stenen.append(steen)
    return {"profiel": profiel, "maatregelen": maatregelen, "afkortingen": afkortingen, "bouwstenen": stenen}


# ---------------------------------------------------------------------------------------------
# Genereren. Elke stap hier staat ook in tools/beleidsset.js; wijzig ze samen.
# ---------------------------------------------------------------------------------------------

def antwoorden_van(profiel: dict, vraag: str) -> list[str] | None:
    waarde = profiel.get(vraag)
    if waarde is None or waarde == [] or waarde == "":
        return None
    return list(waarde) if isinstance(waarde, list) else [waarde]


def beoordeel(als: list[dict], profiel: dict) -> str:
    """'ja', 'nee' of 'open' (een vraag zonder antwoord, en geen voorwaarde die al 'nee' zegt)."""
    uitkomst = "ja"
    for v in als:
        gegeven = antwoorden_van(profiel, v["vraag"])
        if gegeven is None:
            uitkomst = "open"
            continue
        raak = any(a in v["antwoorden"] for a in gegeven)
        if raak == v["niet"]:
            return "nee"
    return uitkomst


def label(vragen: dict, vraag: str, antwoord: str) -> str:
    for a in vragen[vraag]["antwoorden"]:
        if a["id"] == antwoord:
            return a["label"]
    return antwoord


def kop_van_blok(als: list[dict], vragen: dict) -> str:
    delen = []
    for v in als:
        labels = " of ".join(f"«{label(vragen, v['vraag'], a)}»" for a in v["antwoorden"])
        delen.append(f"{vragen[v['vraag']]['vraag']} {'niet ' if v['niet'] else ''}{labels}")
    return "> **Alleen als: " + "; ".join(delen) + "**"


def vul_velden(regel: str, velden: list[list[str]]) -> str:
    def vervang(m: re.Match) -> str:
        naam = m.group(1).strip()
        if not any(v[0] == naam for v in velden):
            velden.append([naam, (m.group(2) or "").strip()])
        return f"**[{naam}]**"
    return VELD.sub(vervang, regel)


def nummer_regels(regels: list[str]) -> list[str]:
    """Opsommingstekens worden per hoofdstuk genummerde eisen; ook in een kader (regels met '> ').
    Vervolgregels van een eis krijgen één spatie extra, zodat ze onder het nummer blijven hangen."""
    uit, teller = [], 0
    for r in regels:
        kader = r.startswith("> ")
        kern = r[2:] if kader else r
        if kern.startswith("#"):
            teller = 0
            uit.append(r)
        elif kern.startswith("- "):
            teller += 1
            uit.append(("> " if kader else "") + f"{teller}. " + kern[2:])
        elif kern.startswith("  ") and teller:
            uit.append(("> " if kader else "") + " " + kern)
        else:
            uit.append(r)
    return uit


def genereer_stuk(steen: dict, data: dict, profiel: dict) -> dict:
    """Markdown van één domein voor één profiel, plus de maatregelen die erin staan en die een controle aantoont."""
    vragen = {v["id"]: v for v in data["profiel"]["vragen"]}
    domein = next(d for d in data["profiel"]["domeinen"] if d["id"] == steen["domein"])
    regels, velden, gedekt, controles = [], [], {}, {}
    kop = steen["titel"]
    for deel in steen["delen"]:
        oordeel = "ja" if deel["als"] is None else beoordeel(deel["als"], profiel)
        if oordeel == "nee":
            continue
        inhoud = [vul_velden(r, velden) for r in deel["regels"]]
        for r in deel["regels"]:
            if r.startswith("#"):
                kop = r.lstrip("#").strip()
            for m in TAG.finditer(r):
                for nr in re.split(r",\s*", m.group(1)):
                    gedekt.setdefault(nr, kop)
            c = CONTROLE.match(r)
            if c:
                for nr in NUMMER.findall(r):
                    controles.setdefault(nr, []).append(c.group(1))
        if oordeel == "open":
            while inhoud and not inhoud[-1].strip():
                inhoud.pop()
            while inhoud and not inhoud[0].strip():
                inhoud.pop(0)
            regels += [kop_van_blok(deel["als"], vragen), ">"] + [("> " + r) if r.strip() else ">" for r in inhoud] + [""]
        else:
            regels += inhoud
    tekst = "\n".join(nummer_regels(regels)).strip("\n")
    tekst = re.sub(r"\n{3,}", "\n\n", tekst)

    alle = data["maatregelen"]["maatregelen"]
    eigen = [m for m in alle if m["thema"] == domein["naam"]]
    overheid = [m["id"] for m in eigen if m["soort"] == "overheid"]
    titels = {m["id"]: m["titel"] for m in alle}
    beantwoord = [(vragen[k]["vraag"], ", ".join(label(vragen, k, a) for a in antwoorden_van(profiel, k)))
                  for k in vragen if antwoorden_van(profiel, k) is not None]

    uit = [f"# {steen['titel']}", ""]
    titelblad = [
        "| | |", "|---|---|",
        f"| Documenttype | Beleid informatiebeveiliging onder het strategisch informatiebeveiligingsbeleid; BIO 2.0-domein *{domein['naam']}* |",
        "| Status | Concept, vast te stellen door de organisatie |",
        "| Eigenaar | [[eigenaar van dit beleid: de manager die dit beleid uitvoert en laat naleven]] |",
        "| Vaststeller | [[vaststeller: wie het beleid vaststelt, bijvoorbeeld de directie of het bestuur]] |",
        "| Evaluatie | Jaarlijks, in de plan-do-check-act-cyclus van het managementsysteem voor informatiebeveiliging |",
    ]
    uit += [vul_velden(r, velden) for r in titelblad]
    uit.append("")
    if steen.get("samenvatting"):
        uit += ["**In het kort.** " + steen["samenvatting"], ""]
    koppen = [m for m in map(HOOFDSTUK.match, (r for deel in steen["delen"] for r in deel["regels"])) if m]
    onderwerpen = koppen[len(VOOR):len(koppen) - len(ACHTER)]
    if onderwerpen:
        uit += ["**Onderwerpen.** " + "; ".join(f"{m.group(1)}. {m.group(2)}" for m in onderwerpen) + ".", ""]
    if beantwoord:
        uit.append("Opgesteld voor dit profiel: " + "; ".join(f"{v} {a}" for v, a in beantwoord) + ".")
    else:
        uit.append("Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.")
    uit += ["", tekst, "", "## Bijlage A: BIO 2.0-maatregelen", ""]
    uit.append(f"De maatregelen van dit domein ({len(eigen)}, waarvan {len(overheid)} overheidsmaatregelen), waar dit "
               f"stuk ze invult en welke controle ze aantoont. Nummers volgens {data['maatregelen']['versie']}; de "
               "tekst van de maatregel staat bij het CIP. Waar de BIO 2.0 geen overheidsmaatregel kent, geldt de "
               "ISO 27002-beheersmaatregel.")
    uit += ["", "| Maatregel | Titel | Soort | In dit stuk | Controle |", "|---|---|---|---|---|"]
    for m in eigen:
        soort = "overheidsmaatregel" if m["soort"] == "overheid" else "ISO-beheersmaatregel"
        uit.append(f"| {m['id']} | {m['titel']} | {soort} | {gedekt.get(m['id'], 'niet ingevuld')} | "
                   f"{', '.join(controles.get(m['id'], [])) or 'geen'} |")
    thema = {m["id"] for m in eigen}
    anders = sorted(nr for nr in gedekt if nr not in thema)
    if anders:
        uit += ["", "Daarnaast vult dit stuk maatregelen van andere domeinen mee in: "
                + ", ".join(f"{nr} ({titels.get(nr, '?')})" for nr in anders) + "."]
    woorden = set(re.findall(r"[\w&]+", tekst, flags=re.ASCII))
    gebruikt = [k for k in sorted(data["afkortingen"]) if k in woorden]
    if gebruikt:
        uit += ["", "## Bijlage B: Afkortingen", "", "| Afkorting | Betekenis |", "|---|---|"]
        uit += [f"| {k} | {data['afkortingen'][k]} |" for k in gebruikt]
    if velden:
        uit += ["", "## Nog in te vullen", ""]
        uit += [f"- **{naam}**" + (f": {uitleg}" if uitleg else "") for naam, uitleg in velden]
    return {"markdown": "\n".join(uit) + "\n", "gedekt": sorted(gedekt), "controles": sorted(controles),
            "eigen": [m["id"] for m in eigen], "overheid": overheid, "waar": gedekt, "controle_per": controles}


def genereer(data: dict, profiel: dict) -> dict[str, dict]:
    return {s["domein"]: genereer_stuk(s, data, profiel) for s in data["bouwstenen"]}


LIJSTKOP = "\n## Nog in te vullen\n"


def vul_waarden(markdown: str, waarden: dict, herkomst: dict | None = None) -> str:
    """Zet waarden in de invulvelden van een gegenereerd stuk: `**[naam]**` wordt de waarde, het veld gaat
    van de lijst *Nog in te vullen* af, en met een herkomst (een AI-voorstel) komt er een regel onder het stuk
    die zegt welke velden zo zijn ingevuld. Spiegel: vulWaarden in tools/beleidsset.js."""
    gevuld = []
    for naam in sorted(waarden):
        waarde = str(waarden[naam]).strip()
        doel = f"**[{naam}]**"
        if waarde and doel in markdown:
            markdown = markdown.replace(doel, waarde)
            gevuld.append(naam)
    if not gevuld:
        return markdown
    if LIJSTKOP in markdown:
        voor, lijst = markdown.split(LIJSTKOP, 1)
        blijft = [r for r in lijst.split("\n")
                  if r.startswith("- **") and r[4:].split("**", 1)[0] not in gevuld]
        markdown = voor.rstrip("\n") + "\n"
        if blijft:
            markdown += LIJSTKOP + "\n" + "\n".join(blijft) + "\n"
    if herkomst:
        markdown += ("\n## Herkomst van ingevulde waarden\n\n"
                     f"Ingevuld uit een AI-voorstel ({herkomst.get('leverancier', '?')}, model "
                     f"{herkomst.get('model', '?')}, {herkomst.get('gemaakt', '?')}, invoer sha256 "
                     f"{str(herkomst.get('sha256', ''))[:12]}): {', '.join(gevuld)}. Controleer elke waarde "
                     "voordat je het stuk vaststelt.\n")
    return markdown


def profielzin(data: dict, profiel: dict) -> str:
    vragen = {v["id"]: v for v in data["profiel"]["vragen"]}
    beantwoord = [(vragen[k]["vraag"], ", ".join(label(vragen, k, a) for a in antwoorden_van(profiel, k)))
                  for k in vragen if antwoorden_van(profiel, k) is not None]
    if beantwoord:
        return "Opgesteld voor dit profiel: " + "; ".join(f"{v} {a}" for v, a in beantwoord) + "."
    return "Zonder profiel: tekst die van een contextvraag afhangt, telt mee."


RIJ = re.compile(r"^(?:> )?\|\s*([A-Z]{2,5}-\d{2,3})\s*\|")
WEBPLEK = "https://security-commons-nl.github.io/kennisbank/governance/"


def cellen(regel: str) -> list[str]:
    regel = regel[2:] if regel.startswith("> ") else regel
    return [c.strip() for c in regel.strip().strip("|").split("|")]


def velden_van(markdown: str) -> list[str]:
    """De namen onder Nog in te vullen van een gegenereerd stuk."""
    if LIJSTKOP not in markdown:
        return []
    lijst = markdown.split(LIJSTKOP, 1)[1].split("\n## ", 1)[0]
    return [r[4:].split("**", 1)[0] for r in lijst.split("\n") if r.startswith("- **")]


def overzichten(data: dict, profiel: dict, stukken: dict) -> dict[str, str]:
    """Twee overzichten over de hele set, uit de gegenereerde stukken: welke maatregel waar staat, en wat er
    moet gebeuren om het beleid in te voeren. Spiegel: overzichten in tools/beleidsset.js."""
    domeinen = {d["id"]: d["naam"] for d in data["profiel"]["domeinen"]}
    thema = {domeinen[s["domein"]]: s for s in data["bouwstenen"]}
    zin = profielzin(data, profiel)

    m = ["# Maatregelenoverzicht", "", zin, "",
         "Per BIO 2.0-maatregel het beleidsstuk dat hem invult, het hoofdstuk waar dat gebeurt en de controle die de "
         f"naleving aantoont. Nummers volgens {data['maatregelen']['versie']}. Komt een maatregel ook in een ander stuk "
         "terug, dan staat dat in de laatste kolom.", "",
         "| Maatregel | Titel | Soort | Beleidsstuk | Hoofdstuk | Controle | Ook in |", "|---|---|---|---|---|---|---|"]
    for mr in sorted(data["maatregelen"]["maatregelen"], key=lambda x: x["id"]):
        steen = thema.get(mr["thema"])
        if not steen:
            continue
        stuk = stukken[steen["domein"]]
        ook = [s["titel"] for s in data["bouwstenen"] if s is not steen and mr["id"] in stukken[s["domein"]]["waar"]]
        m.append(f"| {mr['id']} | {mr['titel']} | {'overheid' if mr['soort'] == 'overheid' else 'ISO'} | "
                 f"{steen['titel']} | {stuk['waar'].get(mr['id'], 'niet ingevuld')} | "
                 f"{', '.join(stuk['controle_per'].get(mr['id'], [])) or 'geen'} | {', '.join(ook)} |")

    v = ["# Invoeren: wat er nog moet gebeuren", "", zin, "",
         "Een vastgesteld beleid werkt pas als de organisatie het inricht. Deze lijst zet per stuk op een rij wat "
         "daarvoor nodig is: wat de organisatie inricht, welke controles zij gaat uitvoeren en wat zij nog moet "
         "invullen. Een plan met volgorde, eigenaar per thema en urenraming staat in "
         f"[BIO 2.0 invoeren]({WEBPLEK}bio2-implementeren/).", "",
         "## Voor de hele set", "",
         "- Wijs per stuk de eigenaar aan en laat het stuk vaststellen.",
         "- Richt één registratie van controles in: per controle de uitvoerder, de frequentie, het bewijs en de uitkomst.",
         "- Richt het risicoregister in voor afwijkingen en bevindingen, met een risico-eigenaar die restrisico's accepteert.",
         "- Zet alle controles in een jaarkalender, zodat elke controle op tijd wordt uitgevoerd."]
    for nr, s in enumerate(data["bouwstenen"], 1):
        md = stukken[s["domein"]]["markdown"]
        rijen = [cellen(r) for r in md.split("\n") if RIJ.match(r)]
        v += ["", f"## {nr}. {s['titel']}", ""]
        if s.get("invoeren"):
            v += ["**Inrichten**", ""] + [f"- {a}" for a in s["invoeren"]] + [""]
        if rijen:
            v += [f"**Controles inrichten ({len(rijen)})**", "", "| Nr | Controle | Uitvoerder | Frequentie |",
                  "|---|---|---|---|"] + [f"| {c[0]} | {c[1]} | {c[2]} | {c[3]} |" for c in rijen] + [""]
        velden = velden_van(md)
        v.append(f"**Nog in te vullen ({len(velden)}).** " + ("; ".join(velden) + "." if velden else "Niets."))
    return {"maatregelen": "\n".join(m) + "\n", "invoeren": "\n".join(v) + "\n"}


def invulvelden(data: dict) -> list[dict]:
    """Alle invulvelden van de set, met de eerste toelichting die erbij staat; ook die van het titelblad."""
    velden: dict[str, str] = {}
    for s in data["bouwstenen"]:
        stuk = genereer_stuk(s, data, {})["markdown"]
        lijst = stuk.split(LIJSTKOP, 1)[1] if LIJSTKOP in stuk else ""
        for r in lijst.split("\n"):
            m = re.match(r"^- \*\*(.+?)\*\*(?:: (.*))?$", r)
            if m and (m.group(1) not in velden or not velden[m.group(1)]):
                velden[m.group(1)] = m.group(2) or ""
    return [{"naam": n, "toelichting": velden[n]} for n in sorted(velden)]


# ---------------------------------------------------------------------------------------------
# Toetsen
# ---------------------------------------------------------------------------------------------

def vragen_in(steen: dict) -> list[str]:
    gezien = []
    for deel in steen["delen"]:
        for v in deel["als"] or []:
            if v["vraag"] not in gezien:
                gezien.append(v["vraag"])
    return gezien


def profielen_voor(steen: dict, data: dict):
    """Elk volledig profiel op de vragen die deze bouwsteen raakt. Bij meer antwoorden: elke niet-lege
    combinatie, want 'als' en 'niet' gedragen zich anders bij een combinatie dan bij één antwoord."""
    vragen = {v["id"]: v for v in data["profiel"]["vragen"]}
    assen = []
    for q in vragen_in(steen):
        ids = [a["id"] for a in vragen[q]["antwoorden"]]
        if vragen[q].get("meerdere"):
            keuzes = [list(c) for n in range(1, len(ids) + 1) for c in itertools.combinations(ids, n)]
        else:
            keuzes = ids
        assen.append((q, keuzes))
    aantal = 1
    for _, k in assen:
        aantal *= len(k)
    if aantal > MAX_PROFIELEN:
        raise BouwsteenFout(f"{steen['bestand']}: {aantal} profielen te toetsen; raakt deze bouwsteen te veel vragen?")
    for combinatie in itertools.product(*[k for _, k in assen]):
        yield dict(zip([q for q, _ in assen], combinatie))


def regelhoofdstukken(regels: list[str]) -> list[str]:
    """De nummers van de hoofdstukken met beleidsregels: alles tussen de vaste hoofdstukken voor en achter."""
    nummers = [m.group(1) for m in map(HOOFDSTUK.match, regels) if m]
    return nummers[len(VOOR):len(nummers) - len(ACHTER)]


def toets_vorm(steen: dict, data: dict) -> list[str]:
    """De vaste opbouw van een bouwsteen: doel en uitgangspunten, dan elk onderwerp als hoofdstuk met regels die
    elk een maatregel noemen, dan rollen, naleving met een controleraamwerk en samenhang; doorlopend genummerd,
    bekende afkortingen."""
    meldingen, waar = [], steen["bestand"]
    regels = [r for deel in steen["delen"] for r in deel["regels"]]
    koppen = [r[3:].strip() for r in regels if r.startswith("## ")]
    titels = [HOOFDSTUK.match("## " + k).group(2) if HOOFDSTUK.match("## " + k) else k for k in koppen]
    nummers = [HOOFDSTUK.match("## " + k).group(1) if HOOFDSTUK.match("## " + k) else "?" for k in koppen]
    verwacht = f"{', '.join(VOOR)}, de onderwerpen, {', '.join(ACHTER)}"
    if (len(titels) < len(VOOR) + len(ACHTER) + 1 or titels[:len(VOOR)] != VOOR
            or titels[len(titels) - len(ACHTER):] != ACHTER):
        meldingen.append(f"{waar}: de hoofdstukken zijn {koppen}; verwacht {verwacht}")
    if nummers != [str(i) for i in range(1, len(koppen) + 1)]:
        meldingen.append(f"{waar}: de hoofdstukken zijn niet doorlopend genummerd: {', '.join(nummers)}")
    for r in regels:
        if r.startswith("### "):
            meldingen.append(f"{waar}: '{r.strip()}' is een subkop; maak er een eigen hoofdstuk van")
    met_regels = set(regelhoofdstukken(regels))
    if not steen.get("samenvatting"):
        meldingen.append(f"{waar}: frontmatter mist 'samenvatting' (twee of drie zinnen over waar het stuk over gaat)")
    if not steen.get("invoeren"):
        meldingen.append(f"{waar}: frontmatter mist 'invoeren' (wat de organisatie moet doen om het beleid in te voeren)")
    for actie in steen.get("invoeren", []):
        h = re.search(r"\(hoofdstuk (\d+)\)\.$", actie)
        if not h or h.group(1) not in nummers:
            meldingen.append(f"{waar}: invoeren '{actie[:60]}' eindigt niet op een bestaand '(hoofdstuk N).'")
    hoofdstuk, item, items = "", None, []
    for r in regels + ["## einde"]:
        if r.startswith("## "):
            if item:
                items.append((hoofdstuk, item))
            m = HOOFDSTUK.match(r)
            hoofdstuk, item = (m.group(1) if m else ""), None
            continue
        if r.startswith("- "):
            if item:
                items.append((hoofdstuk, item))
            item = r
        elif r.startswith("  ") and item:
            item += " " + r.strip()
        else:
            if item:
                items.append((hoofdstuk, item))
            item = None
    for h, tekst in items:
        if h in met_regels and not TAG.search(tekst):
            meldingen.append(f"{waar}: regel zonder maatregel in hoofdstuk {h}: '{tekst[:70]}'")
    controles = [CONTROLE.match(r).group(1) for r in regels if CONTROLE.match(r)]
    if not controles:
        meldingen.append(f"{waar}: geen controleraamwerk (rijen die beginnen met een controle zoals XXX-01)")
    dubbel = sorted({c for c in controles if controles.count(c) > 1})
    if dubbel:
        meldingen.append(f"{waar}: controle meer dan eens: {', '.join(dubbel)}")
    for r in regels:
        if CONTROLE.match(r) and not NUMMER.search(r):
            meldingen.append(f"{waar}: controle {CONTROLE.match(r).group(1)} noemt geen maatregel")
    zonder_velden = VELD.sub(" ", "\n".join(regels))
    zonder_velden = re.sub(r"\b[A-Z]{2,5}-\d{2,3}\b", " ", zonder_velden)  # controles zoals FYS-01
    onbekend = sorted({a for a in AFKORTING.findall(zonder_velden) if a not in data["afkortingen"]})
    if onbekend:
        meldingen.append(f"{waar}: afkorting niet in afkortingen.json: {', '.join(onbekend)}")
    return meldingen


def toets(data: dict) -> list[str]:
    """Alles wat niet klopt, als lijst meldingen. Leeg is goed."""
    meldingen = []
    domeinen = {d["id"]: d for d in data["profiel"]["domeinen"]}
    bekend = {m["id"] for m in data["maatregelen"]["maatregelen"]}
    per_domein = {}
    for s in data["bouwstenen"]:
        if s["domein"] in per_domein:
            meldingen.append(f"{s['bestand']}: domein '{s['domein']}' heeft al een bouwsteen ({per_domein[s['domein']]})")
        per_domein[s["domein"]] = s["bestand"]
        for deel in s["delen"]:
            for r in deel["regels"]:
                nummers = [nr for m in TAG.finditer(r) for nr in re.split(r",\s*", m.group(1))]
                if CONTROLE.match(r):
                    nummers += NUMMER.findall(r)
                for nr in nummers:
                    if nr not in bekend:
                        meldingen.append(f"{s['bestand']}: [{nr}] is geen BIO 2.0-maatregel")
        meldingen += toets_vorm(s, data)
        for profiel in profielen_voor(s, data):
            stuk = genereer_stuk(s, data, profiel)
            mist = [nr for nr in stuk["eigen"] if nr not in stuk["gedekt"]]
            if mist:
                meldingen.append(f"{s['bestand']}: bij profiel {json.dumps(profiel, ensure_ascii=False)} "
                                 f"is niet ingevuld: {', '.join(mist)}")
                break
            zonder = [nr for nr in stuk["eigen"] if nr not in stuk["controles"]]
            if zonder:
                meldingen.append(f"{s['bestand']}: bij profiel {json.dumps(profiel, ensure_ascii=False)} "
                                 f"zonder controle: {', '.join(zonder)}")
                break
    for d in domeinen:
        if d not in per_domein:
            meldingen.append(f"domein '{d}' heeft geen bouwsteen")
    thema = {m["thema"] for m in data["maatregelen"]["maatregelen"]}
    for d in domeinen.values():
        if d["naam"] not in thema:
            meldingen.append(f"domein '{d['naam']}' staat niet als thema in bio2-maatregelen.json")
    gebruikt = {q for s in data["bouwstenen"] for q in vragen_in(s)}
    for v in data["profiel"]["vragen"]:
        if v.get("doel") == "inhoud" and v["id"] not in gebruikt:
            meldingen.append(f"vraag '{v['id']}' heeft doel inhoud maar verandert in geen enkele bouwsteen tekst")
    return meldingen


# ---------------------------------------------------------------------------------------------
# Schrijven
# ---------------------------------------------------------------------------------------------

def bestandsnaam(steen: dict) -> str:
    return steen["bestand"].split("-", 1)[1] if re.match(r"^\d+-", steen["bestand"]) else steen["bestand"]


LIVE = "https://security-commons-nl.github.io/kennisbank/governance/beleidsset-informatiebeveiliging/"


def agentlijst(data: dict) -> str:
    """De stukken als vaste HTML-lijst, zodat een AI-assistent die geen JavaScript draait ze ook ziet."""
    import html as h
    domeinen = {d["id"]: d["naam"] for d in data["profiel"]["domeinen"]}
    regels = []
    for s in data["bouwstenen"]:
        naam = bestandsnaam(s)
        regels.append(f'<li>{h.escape(s["titel"])} ({h.escape(domeinen[s["domein"]])}): '
                      f'<a href="{LIVE}{naam}">{naam}</a>, bouwsteen '
                      f'<a href="{LIVE}data/{s["bestand"]}">data/{s["bestand"]}</a></li>')
    return "\n".join(regels)


def pagina(data: dict) -> str:
    sjabloon = SJABLOON.read_text(encoding="utf-8")
    code = JS.read_text(encoding="utf-8") + "\n" + WORD_JS.read_text(encoding="utf-8")
    gegevens = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return (sjabloon.replace("/*AGENTLIJST*/", agentlijst(data))
            .replace("/*CODE*/", code).replace("/*DATA*/", gegevens))


AI_MAP = ROOT / "tools" / "beleidsset-ai"
AI_PAGINA = ITEM / "beleidsset-ai.html"
CONNECT_SRC = "https: http://localhost:* http://127.0.0.1:*"


def csp_hash(inhoud: str) -> str:
    import base64
    import hashlib
    return base64.b64encode(hashlib.sha256(inhoud.encode("utf-8")).digest()).decode()


def ai_pagina(data: dict) -> str:
    """De AI-hulp: zelfde recept als procescheck/ai/bouw.py. Opdrachten, de vragen en de invulvelden als JSON
    in dezelfde scripttag als kern.js en ai.js, en een CSP op de sha256 van script en stijl."""
    import hashlib
    opdrachten = lees_json(AI_MAP / "opdrachten.json")
    opdrachten["vragen"] = [{"id": v["id"], "vraag": v["vraag"], "meerdere": bool(v.get("meerdere")),
                             "antwoorden": [{"id": a["id"], "label": a["label"]} for a in v["antwoorden"]]}
                            for v in data["profiel"]["vragen"]]
    opdrachten["velden"] = invulvelden(data)
    opdrachten["set_vingerafdruk"] = hashlib.sha256(
        json.dumps(data, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()
    lees = lambda naam: (AI_MAP / naam).read_bytes().decode("utf-8").replace("\r\n", "\n")
    css, kern, ai, sjabloon = lees("ai.css").strip(), lees("kern.js").strip(), lees("ai.js").strip(), lees("pagina.html")
    if "fetch(" in kern:
        raise BouwsteenFout("kern.js mag geen netwerk kennen")
    json_bron = json.dumps(opdrachten, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    script = "window.__OPDRACHTEN__ = " + json_bron + ";\n" + kern + "\n" + ai
    html = (sjabloon.replace("__CSS__", css).replace("__SCRIPT__", script)
            .replace("__SCRIPT_HASH__", csp_hash(script)).replace("__STYLE_HASH__", csp_hash(css))
            .replace("__CONNECT_SRC__", CONNECT_SRC))
    for rest in ("__CSS__", "__SCRIPT__", "__SCRIPT_HASH__", "__STYLE_HASH__", "__CONNECT_SRC__"):
        if rest in html:
            raise BouwsteenFout(f"AI-pagina: {rest} niet ingevuld")
    return html


BEGIN, EINDE = "<!-- stukken:begin -->", "<!-- stukken:einde -->"


def stukkenblok(data: dict, stukken: dict) -> str:
    """De tabel in de README: per domein de leesversie, de bouwsteen en de dekking."""
    regels = ["| BIO 2.0-domein | Stuk | Waar het over gaat | Overheidsmaatregelen | ISO-maatregelen |",
              "|---|---|---|---|---|"]
    domeinen = {d["id"]: d["naam"] for d in data["profiel"]["domeinen"]}
    for s in data["bouwstenen"]:
        stuk, naam = stukken[s["domein"]], bestandsnaam(s)[:-3]
        regels.append(f"| {domeinen[s['domein']]} | [{s['titel']}]({naam}.md) ([Word]({naam}.docx), "
                      f"[bouwsteen](data/{s['bestand']})) | {s.get('samenvatting', '')} | {len(stuk['overheid'])} | "
                      f"{len(stuk['eigen']) - len(stuk['overheid'])} |")
    overheid = sum(len(stukken[s["domein"]]["overheid"]) for s in data["bouwstenen"])
    totaal = sum(len(stukken[s["domein"]]["eigen"]) for s in data["bouwstenen"])
    regels.append(f"| **Totaal** | | | **{overheid}** | **{totaal - overheid}** |")
    return "\n".join(regels)


def met_blok(readme: str, blok: str) -> str:
    if BEGIN not in readme or EINDE not in readme:
        return readme
    voor, rest = readme.split(BEGIN, 1)
    na = rest.split(EINDE, 1)[1]
    nl = "\r\n" if "\r\n" in readme else "\n"  # een checkout op Windows houdt zijn regeleinden
    return voor + BEGIN + nl + blok.replace("\n", nl) + nl + EINDE + na


SET_DOCX = "beleidsset-informatiebeveiliging.docx"
OVERZICHTEN = {"maatregelen": "maatregelenoverzicht", "invoeren": "invoeren"}


def met_downloadregel(markdown: str, naam: str) -> str:
    """De leesversie in de kennisbank: onder de titel een link naar het Word-bestand en naar de generator."""
    kop, rest = markdown.split("\n\n", 1)
    return (f"{kop}\n\n[Download als Word]({naam}.docx) · [Maak je eigen versie in de generator]"
            f"(beleidsset-generator.html)\n\n{rest}")


def uitvoer(data: dict) -> dict[Path, str | bytes]:
    stukken = genereer(data, {})
    over = overzichten(data, {}, stukken)
    uit: dict[Path, str | bytes] = {}
    readme = ITEM / "README.md"
    if readme.exists():
        uit[readme] = met_blok(readme.read_bytes().decode("utf-8"), stukkenblok(data, stukken))
    for s in data["bouwstenen"]:
        naam = bestandsnaam(s)[:-3]
        uit[ITEM / f"{naam}.md"] = met_downloadregel(stukken[s["domein"]]["markdown"], naam)
        uit[ITEM / f"{naam}.docx"] = word.docx([stukken[s["domein"]]["markdown"]])
    for sleutel, naam in OVERZICHTEN.items():
        uit[ITEM / f"{naam}.md"] = met_downloadregel(over[sleutel], naam)
        uit[ITEM / f"{naam}.docx"] = word.docx([over[sleutel]])
    uit[ITEM / SET_DOCX] = word.docx([stukken[s["domein"]]["markdown"] for s in data["bouwstenen"]])
    uit[DATA] = json.dumps(data, ensure_ascii=False, indent=1) + "\n"
    uit[PAGINA] = pagina(data)
    uit[AI_PAGINA] = ai_pagina(data)
    return uit


def kopieer_normen(bron: Path) -> None:
    """Neem nummers, titels en thema's over uit bio2.json van de normen-repo; de tekst blijft daar."""
    data = lees_json(bron)
    oud = lees_json(MAATREGELEN)
    oud.update({"versie": data["versie"], "vingerafdruk": data.get("vingerafdruk"),
                "maatregelen": [{k: m[k] for k in ("id", "titel", "thema", "soort")} for m in data["maatregelen"]]})
    MAATREGELEN.write_bytes((json.dumps(oud, ensure_ascii=False, indent=1) + "\n").encode("utf-8"))


def main(argv: list[str]) -> int:
    if "--normen" in argv:
        kopieer_normen(Path(argv[argv.index("--normen") + 1]))
        print(f"bijgewerkt: {MAATREGELEN.relative_to(ROOT).as_posix()}")
        return 0
    if "--profiel" in argv:
        i = argv.index("--profiel")
        profiel, map_ = lees_json(Path(argv[i + 1])), Path(argv[i + 2])
        map_.mkdir(parents=True, exist_ok=True)
        data = laad()
        stukken = genereer(data, profiel)
        for s in data["bouwstenen"]:
            md = stukken[s["domein"]]["markdown"]
            (map_ / bestandsnaam(s)).write_text(md, encoding="utf-8")
            (map_ / (bestandsnaam(s)[:-3] + ".docx")).write_bytes(word.docx([md]))
        for sleutel, inhoud in overzichten(data, profiel, stukken).items():
            (map_ / f"{OVERZICHTEN[sleutel]}.md").write_text(inhoud, encoding="utf-8")
        print(f"{len(data['bouwstenen'])} stukken, met Word-versie en de twee overzichten, in {map_}")
        return 0
    try:
        data = laad()
    except BouwsteenFout as e:
        print(f"Bouwsteen klopt niet: {e}")
        return 1
    meldingen = toets(data)
    for m in meldingen:
        print("  " + m)
    if meldingen:
        print(f"{len(meldingen)} melding(en). Niets gebouwd.")
        return 1
    achter = []
    for pad, inhoud in uitvoer(data).items():
        if isinstance(inhoud, bytes):
            # Een Word-bestand: dezelfde onderdelen tellen, de compressie verschilt per zlib-versie.
            if pad.exists() and word.zelfde_inhoud(pad.read_bytes(), inhoud):
                continue
            nieuw = inhoud
        else:
            oud = pad.read_bytes().decode("utf-8") if pad.exists() else None
            if oud == inhoud:
                continue
            nieuw = inhoud.encode("utf-8")
        if "--check" in argv:
            achter.append(pad.relative_to(ROOT).as_posix())
        else:
            pad.write_bytes(nieuw)
            print(f"geschreven: {pad.relative_to(ROOT).as_posix()}")
    if achter:
        print("Loopt achter op de bouwstenen, draai python tools/bouw_beleidsset.py: " + ", ".join(achter))
        return 1
    print(f"Beleidsset: {len(data['bouwstenen'])} bouwstenen, dekking getoetst op elk profiel.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
