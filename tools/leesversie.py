"""Maakt de leesversie (index.html) van een item uit zijn README.md.

Gebruik:  python tools/leesversie.py security/<item>
Daarna:   python tools/build.py   (zet kruimelpad, bronvoet, favicon en inhoudsopgave)

Statuut B3: elk tekstitem heeft een self-contained HTML-leesversie. Die werd tot nu toe met de hand
gemaakt, waardoor er drie opmaken naast elkaar staan. Dit script maakt ze allemaal met hetzelfde
sjabloon: Calibri in een kolom van 19 cm. Dat is niet willekeurig, build.py herkent die kolom en zet
de inhoudsopgave dan als zijbalk naast de tekst in plaats van als blok erboven.

De frontmatter gaat er eerst af. Zonder dat zet pandoc hem als metadatablok boven de tekst, en dan
staat de hele YAML op de pagina.

**Bedoeld voor nieuwe items.** Een paar bestaande leesversies zijn met de hand gemaakt en bevatten een
handgeschreven metaregel onder de titel. Dit script reproduceert die niet, dus overschrijf een bestaande
leesversie alleen als je hebt gecontroleerd wat je kwijtraakt. Zo'n regel is trouwens een reden om hem
juist wel te vervangen: bij passkeys-invoeren stond er "handleiding" terwijl het type aanpak is. Wat met
de hand wordt bijgehouden, loopt achter.
"""
from __future__ import annotations

import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SJABLOON = pathlib.Path(__file__).resolve().parent / "leesversie-sjabloon.html"


def pandoc_pad() -> str:
    gevonden = shutil.which("pandoc")
    if gevonden:
        return gevonden
    vast = pathlib.Path(r"X:\TOOLS\pandoc\pandoc.exe")
    if vast.is_file():
        return str(vast)
    sys.exit("pandoc niet gevonden; zet het op het PATH")


def bouw(item: pathlib.Path) -> pathlib.Path:
    readme = item / "README.md"
    if not readme.is_file():
        sys.exit(f"{readme} bestaat niet")

    tekst = re.sub(r"\A---\n.*?\n---\n", "", readme.read_text(encoding="utf-8"), count=1, flags=re.S)
    kop = re.search(r"^# (.+)$", tekst, re.M)
    if not kop:
        sys.exit(f"{readme}: geen h1-kop gevonden; de leesversie heeft een titel nodig")

    uit = subprocess.run(
        [pandoc_pad(), "--from", "gfm", "--to", "html5", "--standalone",
         "--template", str(SJABLOON), "--metadata", f"title={kop.group(1).strip()}"],
        input=tekst, capture_output=True, text=True, encoding="utf-8", check=True,
    )
    doel = item / "index.html"
    doel.write_text(uit.stdout, encoding="utf-8")
    return doel


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    doel = bouw(ROOT / sys.argv[1])
    print(f"{doel}: {len(doel.read_text(encoding='utf-8')) // 1024} kB; draai nu python tools/build.py")
