"""Bouwt de beleidsset informatiebeveiliging uit de bouwstenen en de contextvragen.

Gebruik:
    python tools/bouw_beleidsset.py            # schrijft de leesversies, de data en de generatorpagina
    python tools/bouw_beleidsset.py --check    # exit 1 als iets achterloopt of een maatregel niet gedekt is
    python tools/bouw_beleidsset.py --profiel antwoorden.json uitmap/   # een set voor een eigen profiel
    python tools/bouw_beleidsset.py --normen ../normen/bio2.json        # de maatregelkopie bijwerken

Per BIO 2.0-domein staat in `data/` één markdownbestand. Daarin:

- eindigt een beleidsregel op de nummers van de overheidsmaatregelen die hij invult: `[8.13.01]` of
  `[8.13.01, 8.13.02]`;
- staat tekst die van een contextvraag afhangt tussen `::: als vraag=antwoord` en `:::`. Meer antwoorden
  scheid je met een komma (`hosting=saas,hostingpartij`), meer voorwaarden met ` en `, en `!=` keert om.
  Blokken nesten niet;
- is `[[label: toelichting]]` een invulveld: wat de organisatie zelf moet invullen.

Een profiel is een JSON-object met per vraag-id uit `profiel.json` een antwoord-id of, bij een vraag met
meer antwoorden, een lijst. Een vraag zonder antwoord laat het blok staan, met de vraag erboven: zo is de
set zonder antwoorden de leesversie met alle varianten.

Dezelfde rekenregel staat in `tools/beleidsset.js` voor de generatorpagina; `tools/test_beleidsset.py`
houdt de twee gelijk en toetst de dekking: voor elk volledig profiel op de vragen die een domein raakt,
vult de tekst elke overheidsmaatregel van dat domein met minstens één regel in.
"""
from __future__ import annotations

import itertools
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ITEM = ROOT / "governance" / "beleidsset-informatiebeveiliging"
BOUWSTENEN = ITEM / "data"
PROFIEL = ITEM / "profiel.json"
MAATREGELEN = BOUWSTENEN / "bio2-maatregelen.json"
DATA = ITEM / "beleidsset.json"
PAGINA = ITEM / "beleidsset-generator.html"
SJABLOON = ROOT / "tools" / "beleidsset-generator-sjabloon.html"
JS = ROOT / "tools" / "beleidsset.js"

TAG = re.compile(r"\[(\d\.\d{2}\.\d{2}(?:,\s*\d\.\d{2}\.\d{2})*)\]")
VELD = re.compile(r"\[\[([^\]:]+?)(?::\s*([^\]]+?))?\]\]")
OPEN = re.compile(r"^::: als (.+)$")
VOORWAARDE = re.compile(r"^([a-z0-9-]+)\s*(!?=)\s*([a-z0-9-]+(?:,[a-z0-9-]+)*)$")
MAX_PROFIELEN = 20000  # bovengrens per domein bij het toetsen van de dekking


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
    fm = {}
    for regel in kop.split("\n"):
        if regel.strip():
            sleutel, _, waarde = regel.partition(":")
            fm[sleutel.strip()] = waarde.strip()
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
    return {"domein": fm["domein"], "titel": fm["titel"], "delen": delen}


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
    vragen = {v["id"]: v for v in profiel["vragen"]}
    domeinen = {d["id"]: d for d in profiel["domeinen"]}
    stenen = []
    for pad in sorted((map_ / "data").glob("*.md")):
        steen = parse_bouwsteen(pad.read_text(encoding="utf-8"), vragen, pad.name)
        if steen["domein"] not in domeinen:
            raise BouwsteenFout(f"{pad.name}: domein '{steen['domein']}' staat niet in profiel.json")
        steen["bestand"] = pad.name
        stenen.append(steen)
    return {"profiel": profiel, "maatregelen": maatregelen, "bouwstenen": stenen}


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


def genereer_stuk(steen: dict, data: dict, profiel: dict) -> dict:
    """Markdown van één domein voor één profiel, plus de maatregelen die erin staan."""
    vragen = {v["id"]: v for v in data["profiel"]["vragen"]}
    domein = next(d for d in data["profiel"]["domeinen"] if d["id"] == steen["domein"])
    regels, velden, gedekt = [], [], {}
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
        if oordeel == "open":
            while inhoud and not inhoud[-1].strip():
                inhoud.pop()
            while inhoud and not inhoud[0].strip():
                inhoud.pop(0)
            regels += [kop_van_blok(deel["als"], vragen), ">"] + [("> " + r) if r.strip() else ">" for r in inhoud] + [""]
        else:
            regels += inhoud
    tekst = "\n".join(regels).strip("\n")
    tekst = re.sub(r"\n{3,}", "\n\n", tekst)

    eigen = [m for m in data["maatregelen"]["maatregelen"]
             if m["thema"] == domein["naam"] and m["soort"] == "overheid"]
    titels = {m["id"]: m["titel"] for m in data["maatregelen"]["maatregelen"]}
    beantwoord = [(vragen[k]["vraag"], ", ".join(label(vragen, k, a) for a in antwoorden_van(profiel, k)))
                  for k in vragen if antwoorden_van(profiel, k) is not None]

    uit = [f"# {steen['titel']}", ""]
    uit.append(f"Beleid informatiebeveiliging, BIO 2.0-domein *{domein['naam']}*. Status: concept, vast te "
               "stellen door de organisatie zelf.")
    uit.append("")
    if beantwoord:
        uit.append("Opgesteld voor dit profiel: " + "; ".join(f"{v} {a}" for v, a in beantwoord) + ".")
    else:
        uit.append("Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.")
    uit += ["", tekst, "", "## Bijlage: BIO 2.0-maatregelen", ""]
    uit.append(f"De overheidsmaatregelen van dit domein ({len(eigen)}) en waar dit stuk ze invult. Nummers volgens "
               f"{data['maatregelen']['versie']}; de tekst van de maatregel staat bij het CIP.")
    uit += ["", "| Maatregel | Titel | In dit stuk |", "|---|---|---|"]
    for m in eigen:
        uit.append(f"| {m['id']} | {m['titel']} | {gedekt.get(m['id'], 'niet ingevuld')} |")
    thema = {m["id"] for m in data["maatregelen"]["maatregelen"] if m["thema"] == domein["naam"]}
    iso = sorted(nr for nr in gedekt if nr in thema and nr not in {m['id'] for m in eigen})
    if iso:
        uit += ["", "Ook ingevuld, ISO-beheersmaatregelen van dit domein zonder overheidsmaatregel: "
                + ", ".join(f"{nr} ({titels.get(nr, '?')})" for nr in iso) + "."]
    anders = sorted(nr for nr in gedekt if nr not in thema)
    if anders:
        uit += ["", "Daarnaast vult dit stuk maatregelen van andere domeinen mee in: "
                + ", ".join(f"{nr} ({titels.get(nr, '?')})" for nr in anders) + "."]
    if velden:
        uit += ["", "## Nog in te vullen", ""]
        uit += [f"- **{naam}**" + (f": {uitleg}" if uitleg else "") for naam, uitleg in velden]
    return {"markdown": "\n".join(uit) + "\n", "gedekt": sorted(gedekt), "eigen": [m["id"] for m in eigen]}


def genereer(data: dict, profiel: dict) -> dict[str, dict]:
    return {s["domein"]: genereer_stuk(s, data, profiel) for s in data["bouwstenen"]}


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
                for m in TAG.finditer(r):
                    for nr in re.split(r",\s*", m.group(1)):
                        if nr not in bekend:
                            meldingen.append(f"{s['bestand']}: [{nr}] is geen BIO 2.0-maatregel")
        for profiel in profielen_voor(s, data):
            stuk = genereer_stuk(s, data, profiel)
            mist = [nr for nr in stuk["eigen"] if nr not in stuk["gedekt"]]
            if mist:
                meldingen.append(f"{s['bestand']}: bij profiel {json.dumps(profiel, ensure_ascii=False)} "
                                 f"is niet ingevuld: {', '.join(mist)}")
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


def pagina(data: dict) -> str:
    sjabloon = SJABLOON.read_text(encoding="utf-8")
    code = JS.read_text(encoding="utf-8")
    gegevens = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return sjabloon.replace("/*CODE*/", code).replace("/*DATA*/", gegevens)


BEGIN, EINDE = "<!-- stukken:begin -->", "<!-- stukken:einde -->"


def stukkenblok(data: dict, stukken: dict) -> str:
    """De tabel in de README: per domein de leesversie, de bouwsteen en de dekking."""
    regels = ["| BIO 2.0-domein | Stuk | Bouwsteen | Overheidsmaatregelen |", "|---|---|---|---|"]
    domeinen = {d["id"]: d["naam"] for d in data["profiel"]["domeinen"]}
    for s in data["bouwstenen"]:
        stuk = stukken[s["domein"]]
        regels.append(f"| {domeinen[s['domein']]} | [{s['titel']}]({bestandsnaam(s)}) | "
                      f"[{s['bestand']}](data/{s['bestand']}) | {len(stuk['eigen'])} |")
    totaal = sum(len(stukken[s["domein"]]["eigen"]) for s in data["bouwstenen"])
    regels.append(f"| **Totaal** | | | **{totaal}** |")
    return "\n".join(regels)


def met_blok(readme: str, blok: str) -> str:
    if BEGIN not in readme or EINDE not in readme:
        return readme
    voor, rest = readme.split(BEGIN, 1)
    na = rest.split(EINDE, 1)[1]
    nl = "\r\n" if "\r\n" in readme else "\n"  # een checkout op Windows houdt zijn regeleinden
    return voor + BEGIN + nl + blok.replace("\n", nl) + nl + EINDE + na


def uitvoer(data: dict) -> dict[Path, str]:
    stukken = genereer(data, {})
    uit = {}
    readme = ITEM / "README.md"
    if readme.exists():
        uit[readme] = met_blok(readme.read_bytes().decode("utf-8"), stukkenblok(data, stukken))
    for s in data["bouwstenen"]:
        uit[ITEM / bestandsnaam(s)] = stukken[s["domein"]]["markdown"]
    uit[DATA] = json.dumps(data, ensure_ascii=False, indent=1) + "\n"
    uit[PAGINA] = pagina(data)
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
        for s in data["bouwstenen"]:
            (map_ / bestandsnaam(s)).write_text(genereer_stuk(s, data, profiel)["markdown"], encoding="utf-8")
        print(f"{len(data['bouwstenen'])} stukken in {map_}")
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
        oud = pad.read_bytes().decode("utf-8") if pad.exists() else None
        if oud == inhoud:
            continue
        if "--check" in argv:
            achter.append(pad.relative_to(ROOT).as_posix())
        else:
            pad.write_bytes(inhoud.encode("utf-8"))
            print(f"geschreven: {pad.relative_to(ROOT).as_posix()}")
    if achter:
        print("Loopt achter op de bouwstenen, draai python tools/bouw_beleidsset.py: " + ", ".join(achter))
        return 1
    print(f"Beleidsset: {len(data['bouwstenen'])} bouwstenen, dekking getoetst op elk profiel.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
