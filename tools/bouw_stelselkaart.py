#!/usr/bin/env python3
"""Bouwt de data in de stelselkaart opnieuw uit de dataset.

De bron van de stelselkaart is `data/partijen.json` en `data/diensten.json` in de map
`security/stelselkaart-security-gremia/`. De pagina `index.html` in die map heeft de data als
JavaScript ingebakken, zodat hij offline werkt. Dit script schrijft die twee blokken (`const P` en
`const D`) opnieuw uit de JSON. De rest van de pagina (opmaak, weergaven, tekst) is het sjabloon en
blijft staan; het kruimelpad en de voet zet `build.py`.

Wijzig dus de JSON, nooit de blokken in de pagina, en draai daarna:

    python tools/bouw_stelselkaart.py           # schrijft index.html bij als de data veranderd is
    python tools/bouw_stelselkaart.py --check   # exit 1 als de pagina niet bij de data past

De dataset wordt eerst gecontroleerd: unieke id's, codes uit het vocabulaire in `meta`, het aantal
klopt, elke partij in een dienst bestaat. Een fout blokkeert, er wordt dan niets geschreven.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT / "security" / "stelselkaart-security-gremia"
PAGINA = MAP / "index.html"
PARTIJEN = MAP / "data" / "partijen.json"
DIENSTEN = MAP / "data" / "diensten.json"

# De pagina gebruikt voor de toegang de codes van de eerste versie (AC in index.html).
TOEGANG_PAGINA = {"direct": "haal", "indirect": "indirect", "gesloten": "geen"}

BLOK_P = re.compile(r"(\nconst P=\[\n)(.*?)(\n\];)", re.S)
BLOK_D = re.compile(r"(\nconst D=\[\n)(.*?)(\n\];)", re.S)
KOP_P = "// gegenereerd door tools/bouw_stelselkaart.py uit data/partijen.json; wijzig de JSON, niet dit blok"
KOP_D = "// gegenereerd door tools/bouw_stelselkaart.py uit data/diensten.json; wijzig de JSON, niet dit blok"


def lees(pad: Path) -> dict:
    return json.loads(pad.read_text(encoding="utf-8"))


def controleer(partijen: dict, diensten: dict) -> list[str]:
    fouten = []
    voc = partijen["meta"]["vocabulaire"]
    lijst = partijen["partijen"]
    ids = [p["id"] for p in lijst]
    dubbel = sorted({i for i in ids if ids.count(i) > 1})
    if dubbel:
        fouten.append(f"dubbele id's: {dubbel}")
    if partijen.get("aantal") != len(lijst):
        fouten.append(f"partijen.json: aantal is {partijen.get('aantal')}, er staan {len(lijst)} partijen in")
    for p in lijst:
        waar = f"partij '{p.get('id')}'"
        for veld in ("id", "naam", "laag", "mandaat", "functies", "toegang_gemeente", "omschrijving", "toelichting"):
            if veld not in p:
                fouten.append(f"{waar}: veld '{veld}' ontbreekt")
        if p.get("laag") not in voc["lagen"]:
            fouten.append(f"{waar}: laag '{p.get('laag')}' staat niet in het vocabulaire")
        if p.get("mandaat") not in voc["mandaat"]:
            fouten.append(f"{waar}: mandaat '{p.get('mandaat')}' staat niet in het vocabulaire")
        for f in p.get("functies", []):
            if f not in voc["functies"]:
                fouten.append(f"{waar}: functie '{f}' staat niet in het vocabulaire")
        if p.get("toegang_gemeente") not in TOEGANG_PAGINA:
            fouten.append(f"{waar}: toegang_gemeente '{p.get('toegang_gemeente')}' is onbekend")
        url = p.get("url")
        if url is not None and not url.startswith("https://"):
            fouten.append(f"{waar}: url hoort met https:// te beginnen")
    bekend = set(ids)
    dl = diensten["diensten"]
    if diensten.get("aantal") != len(dl):
        fouten.append(f"diensten.json: aantal is {diensten.get('aantal')}, er staan {len(dl)} diensten in")
    for d in dl:
        for pid in d["partijen"] + d.get("werk_in_uitvoering", []):
            if pid not in bekend:
                fouten.append(f"dienst '{d['dienst']}': partij '{pid}' staat niet in partijen.json")
    return fouten


def rij(waarden: list) -> str:
    return json.dumps(waarden, ensure_ascii=False, separators=(",", ":"))


def blok_partijen(partijen: dict) -> str:
    """Een regel per partij: id, naam, laag, mandaat, functies, toegang, omschrijving, toelichting, url."""
    regels = [KOP_P]
    for p in partijen["partijen"]:
        regels.append(rij([p["id"], p["naam"], p["laag"], p["mandaat"], p["functies"],
                           TOEGANG_PAGINA[p["toegang_gemeente"]], p["omschrijving"], p["toelichting"],
                           p.get("url") or ""]) + ",")
    regels[-1] = regels[-1].rstrip(",")
    return "\n".join(regels)


def blok_diensten(diensten: dict) -> str:
    """Een regel per dienst: naam, leveranciers, duiding, en zo nodig wie eraan werkt."""
    regels = [KOP_D]
    for d in diensten["diensten"]:
        waarden = [d["dienst"], d["partijen"], d["duiding"]]
        if d.get("werk_in_uitvoering"):
            waarden.append(d["werk_in_uitvoering"])
        regels.append(rij(waarden) + ",")
    regels[-1] = regels[-1].rstrip(",")
    return "\n".join(regels)


def bouw(html: str, partijen: dict, diensten: dict) -> str:
    for patroon, inhoud, naam in ((BLOK_P, blok_partijen(partijen), "const P"),
                                  (BLOK_D, blok_diensten(diensten), "const D")):
        treffers = patroon.findall(html)
        if len(treffers) != 1:
            raise SystemExit(f"index.html: blok '{naam}' {len(treffers)} keer gevonden, verwacht 1")
        html = patroon.sub(lambda m: m.group(1) + inhoud + m.group(3), html)
    return html


def main(argv: list[str]) -> int:
    alleen_check = "--check" in argv
    partijen, diensten = lees(PARTIJEN), lees(DIENSTEN)
    fouten = controleer(partijen, diensten)
    if fouten:
        print(f"Stelselkaart: {len(fouten)} fout(en) in de dataset. Niets gebouwd.")
        for f in fouten:
            print("  " + f)
        return 1
    oud = PAGINA.read_text(encoding="utf-8")
    nieuw = bouw(oud, partijen, diensten)
    n_p, n_d = len(partijen["partijen"]), len(diensten["diensten"])
    if nieuw == oud:
        print(f"Stelselkaart: pagina past bij de data ({n_p} partijen, {n_d} diensten).")
        return 0
    if alleen_check:
        print("Stelselkaart: index.html past niet bij data/*.json. Draai python tools/bouw_stelselkaart.py")
        return 1
    PAGINA.write_text(nieuw, encoding="utf-8", newline="\n")
    print(f"Stelselkaart: index.html bijgewerkt ({n_p} partijen, {n_d} diensten).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
