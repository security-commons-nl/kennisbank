#!/usr/bin/env python3
"""Haalt routes.json (de leesroutes van de voorpagina, statuut C2) naar de root van de kennisbank.

De bron is site/routes.json in de repo security-commons-nl.github.io. Eén bron, één kopie met controle,
zoals normen/*.json bij de afnemers (ARCHITECTUUR, "wat uit wat volgt").

  python tools/haal_routes.py           kopieert (sibling-checkout of raw.githubusercontent.com)
  python tools/haal_routes.py --check   faalt als de kopie afwijkt van de bron
"""
from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOEL = ROOT / "routes.json"
SIBLING = ROOT.parent / "security-commons-nl.github.io" / "site" / "routes.json"
RAW = "https://raw.githubusercontent.com/security-commons-nl/security-commons-nl.github.io/main/site/routes.json"


def bron() -> str:
    if SIBLING.exists():
        return SIBLING.read_text(encoding="utf-8")
    with urllib.request.urlopen(RAW, timeout=20) as r:
        return r.read().decode("utf-8")


def genormaliseerd(tekst: str) -> str:
    return json.dumps(json.loads(tekst), ensure_ascii=False, sort_keys=True)


def main() -> int:
    tekst = bron()
    data = json.loads(tekst)
    ids = [r["id"] for r in data["routes"]]
    if "--check" in sys.argv:
        if not DOEL.exists():
            print("routes.json ontbreekt; draai tools/haal_routes.py")
            return 1
        if genormaliseerd(DOEL.read_text(encoding="utf-8")) != genormaliseerd(tekst):
            print("routes.json wijkt af van de bron; draai tools/haal_routes.py en commit de kopie")
            return 1
        print(f"routes.json is gelijk aan de bron ({len(ids)} routes: {', '.join(ids)})")
        return 0
    DOEL.write_text(tekst.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
    print(f"routes.json bijgewerkt ({len(ids)} routes: {', '.join(ids)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
