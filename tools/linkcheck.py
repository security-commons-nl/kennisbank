#!/usr/bin/env python3
"""Loopt elk adres in bronnen.json en de adressen van de partijen in de stelselkaart na.

Draaien:  python tools/linkcheck.py                  (rapport op het scherm)
          python tools/linkcheck.py --rapport r.md   (rapport als markdown, voor het issue)

Een verwijzing naar het werk van een ander is alleen iets waard zolang hij werkt, en overheidssites
verhuizen hun stukken vaak. Dit script draait maandelijks als GitHub Action en opent een issue als er
iets mis is. Het wijzigt zelf niets: of een stuk echt weg is of alleen verhuisd, beslist een mens.
Die zet dan een nieuw adres in bronnen.json, of `vervallen` met de datum, waarna de leesversie naar
de partij zelf wijst.

Vier uitkomsten per adres:
  ok            het adres antwoordt zoals verwacht
  dood          404 of 410: het stuk is weg of verhuisd; exitcode 1
  muur          een open bron vraagt nu om een inlog (401/403); controleer of de toegang veranderd is
  onbereikbaar  time-out, serverfout of geweigerd; vaak tijdelijk of een blokkade van de runner

Bij een bron met toegang `inlog` is 401 of 403 juist goed: de ingang leeft. Wat erachter staat kan
een script niet zien; daarvoor staat de datum `gezien` in het register. Bij het adres van een partij
betekent 403 meestal dat de site scripts weert (politie.nl en z-cert.nl doen dat); ook dat telt als goed.

Alleen **dood** en **muur** openen een issue. **Onbereikbaar** staat erin als er toch een issue is, maar
opent er zelf geen: een melding die elke maand terugkomt om een certificaatfout bij een ander, leert
iedereen het issue te negeren.
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parent.parent
PARTIJEN_REL = Path("security") / "stelselkaart-security-gremia" / "data" / "partijen.json"
# Sommige overheidssites weigeren een kale Python-client; met een gewone browser-UA niet.
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36"
TIMEOUT = 25

Ophaler = Callable[[str], int]


def haal_status(url: str) -> int:
    """HTTP-status na redirects; 0 bij time-out of een netwerkfout."""
    verzoek = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,*/*"})
    try:
        with urllib.request.urlopen(verzoek, timeout=TIMEOUT) as antwoord:
            return antwoord.status
    except urllib.error.HTTPError as fout:
        return fout.code
    except Exception:
        return 0


def beoordeel(status: int, toegang: str) -> str:
    if status in (404, 410):
        return "dood"
    if 200 <= status < 300:
        return "ok"
    if status in (401, 403):
        return "ok" if toegang in ("inlog", "partij") else "muur"
    return "onbereikbaar"


def te_controleren(root: Path = ROOT) -> list[dict]:
    """Alle adressen met wat erbij hoort: welke bron, welk veld, welke toegang."""
    lijst: list[dict] = []
    pad = root / "bronnen.json"
    bronnen = json.loads(pad.read_text(encoding="utf-8")).get("bronnen", {}) if pad.is_file() else {}
    for bid, bron in bronnen.items():
        if bron.get("url") and not bron.get("vervallen"):
            lijst.append({"wat": f"bron {bid}", "url": bron["url"], "toegang": bron.get("toegang", "open")})
        if bron.get("archief"):
            lijst.append({"wat": f"bron {bid} (archief)", "url": bron["archief"], "toegang": "open"})
    ppad = root / PARTIJEN_REL
    if ppad.is_file():
        for p in json.loads(ppad.read_text(encoding="utf-8"))["partijen"]:
            if p.get("url"):
                lijst.append({"wat": f"partij {p['id']}", "url": p["url"], "toegang": "partij"})
    return lijst


def controleer(lijst: list[dict], ophaler: Ophaler = haal_status) -> list[dict]:
    uit = []
    for regel in lijst:
        status = ophaler(regel["url"])
        uit.append({**regel, "status": status, "oordeel": beoordeel(status, regel["toegang"])})
    return uit


def heeft_melding(uitslag: list[dict]) -> bool:
    """Alleen wat een mens moet oppakken, opent een issue."""
    return any(r["oordeel"] in ("dood", "muur") for r in uitslag)


def rapport(uitslag: list[dict]) -> str:
    fout = [r for r in uitslag if r["oordeel"] != "ok"]
    kop = f"Linkcheck: {len(uitslag)} adressen, {len(fout)} met een melding."
    if not heeft_melding(uitslag):
        onbereikbaar = ", ".join(r["wat"] for r in fout)
        return kop + (f" Onbereikbaar, vaak tijdelijk: {onbereikbaar}." if fout else "") + "\n"
    regels = [kop, "",
              "Wat te doen: bij **dood** een nieuw adres in `bronnen.json` zetten, of `vervallen` met de "
              "datum als het stuk echt weg is. Bij **muur** nagaan of de toegang veranderd is. "
              "**Onbereikbaar** is vaak tijdelijk; staat hij er de volgende maand weer, dan met de hand openen.",
              "", "| Oordeel | Wat | Status | Adres |", "|---|---|---|---|"]
    volgorde = {"dood": 0, "muur": 1, "onbereikbaar": 2}
    for r in sorted(fout, key=lambda r: (volgorde[r["oordeel"]], r["wat"])):
        regels.append(f"| {r['oordeel']} | {r['wat']} | {r['status'] or 'geen antwoord'} | {r['url']} |")
    return "\n".join(regels) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--rapport", help="schrijf het rapport als markdown naar dit bestand")
    args = ap.parse_args()
    uitslag = controleer(te_controleren())
    tekst = rapport(uitslag)
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print(tekst)
    if args.rapport:
        Path(args.rapport).write_text(tekst, encoding="utf-8")
    return 1 if any(r["oordeel"] == "dood" for r in uitslag) else 0


if __name__ == "__main__":
    sys.exit(main())
