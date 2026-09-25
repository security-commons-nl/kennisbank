#!/usr/bin/env python3
"""Haalt de openbare productcatalogi van de IBD en CIP op en vult bronnen.json aan.

Draaien:  python tools/haal_catalogi.py            (laat zien wat er nieuw is, schrijft niets)
          python tools/haal_catalogi.py --schrijf  (zet de nieuwe stukken in bronnen.json)

Waarom: een ISO die "iets van de VNG over beleid" zoekt, moet het in de kennisbank vinden, ook als er
nog geen wegwijzer of handleiding naar verwijst (besluit 25-09-2026). De twee partijen die voor
gemeenten het meest leveren, hebben hun catalogus volledig openbaar staan; die gaat in zijn geheel het
register in. Het script voegt alleen toe en wijzigt niets bestaands: een titel die met de hand is
aangepast blijft staan, en wat uit een catalogus verdwijnt vangt de maandelijkse linkcheck.

Alleen openbare pagina's. Niets achter MijnIBD of CIP.Pleio.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36"
IBD = "https://www.informatiebeveiligingsdienst.nl/producten/"
CIP = "https://www.cip-overheid.nl"
IBD_KAART = re.compile(r'<div class="post-meta">\s*[A-Z]+\s*\|[^<]*</div>\s*<h3>\s*(.*?)\s*</h3>.*?'
                       r'<a class="clickable" href="(https://www\.informatiebeveiligingsdienst\.nl/product/[^"]+)"', re.S)
IBD_LAATSTE = re.compile(r"/producten/page/(\d+)/")
CIP_PAD = re.compile(r'href="(/producten-en-diensten/[^"?#]+)"')


def haal(url: str) -> str:
    for poging in range(3):
        try:
            verzoek = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(verzoek, timeout=30) as antwoord:
                return antwoord.read().decode("utf-8", "replace")
        except Exception:
            if poging == 2:
                raise
            time.sleep(2)
    return ""


def schoon(tekst: str) -> str:
    return " ".join(html.unescape(re.sub(r"<[^>]+>", "", tekst)).split())


def slug(url: str) -> str:
    laatste = url.rstrip("/").rsplit("/", 1)[-1].lower()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", laatste)).strip("-")


def ibd() -> list[dict]:
    eerste = haal(IBD)
    laatste = max([int(n) for n in IBD_LAATSTE.findall(eerste)] or [1])
    with ThreadPoolExecutor(6) as pool:
        paginas = [eerste] + list(pool.map(haal, [f"{IBD}page/{n}/" for n in range(2, laatste + 1)]))
    gezien: dict[str, dict] = {}
    for tekst in paginas:
        for titel, url in IBD_KAART.findall(tekst):
            gezien.setdefault(url, {"id": f"ibd-{slug(url)}", "titel": schoon(titel), "url": url, "partij": "ibd"})
    return list(gezien.values())


def cip() -> list[dict]:
    paden: set[str] = set()
    for n in range(1, 20):
        nieuw = set(CIP_PAD.findall(haal(f"{CIP}/producten-en-diensten/?page={n}"))) - paden
        if not nieuw:
            break
        paden |= nieuw

    def detail(pad: str) -> dict:
        tekst = haal(CIP + pad)
        kop = re.search(r"<h1[^>]*>(.*?)</h1>", tekst, re.S)
        return {"id": f"cip-{slug(pad)}", "titel": schoon(kop.group(1)) if kop else slug(pad),
                "url": CIP + pad, "partij": "cip"}

    with ThreadPoolExecutor(6) as pool:
        return list(pool.map(detail, sorted(paden)))


def nieuwe(register: dict, gevonden: list[dict]) -> list[dict]:
    """Wat nog niet in het register staat, op adres en op id. Bestaande regels blijven onaangeroerd."""
    bestaand_url = {str(b.get("url", "")).rstrip("/") for b in register.values()}
    uit, ids = [], set(register)
    for b in gevonden:
        if b["url"].rstrip("/") in bestaand_url or b["id"] in ids:
            continue
        ids.add(b["id"])
        uit.append(b)
    return uit


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--schrijf", action="store_true", help="zet de nieuwe stukken in bronnen.json")
    args = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    pad = ROOT / "bronnen.json"
    data = json.loads(pad.read_bytes().decode("utf-8"))
    gevonden = ibd() + cip()
    toe = nieuwe(data["bronnen"], gevonden)
    print(f"Gevonden: {len(gevonden)} stukken (IBD en CIP); nieuw voor het register: {len(toe)}.")
    for b in toe[:10]:
        print(f"  + {b['id']}: {b['titel']}")
    if len(toe) > 10:
        print(f"  ... en {len(toe) - 10} meer")
    if args.schrijf and toe:
        vandaag = date.today().isoformat()
        for b in toe:
            data["bronnen"][b["id"]] = {"titel": b["titel"], "url": b["url"], "partij": b["partij"],
                                        "toegang": "open", "gezien": vandaag}
        pad.write_bytes((json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
        print(f"Geschreven: {len(toe)} bronnen erbij. Draai nu python tools/build.py.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
