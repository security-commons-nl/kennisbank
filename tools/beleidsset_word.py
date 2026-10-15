"""Een Word-bestand (.docx) uit de markdown van de beleidsset, zonder externe bibliotheek.

Kent precies wat de generator maakt: koppen, alinea's, genummerde en gewone lijsten, tabellen, kaders
(regels met '> ') en vet, cursief, code en links binnen een regel. De spiegel staat in
tools/beleidsset-word.js voor de generatorpagina; tools/test_beleidsset.py houdt de twee gelijk.

    from beleidsset_word import docx
    open("stuk.docx", "wb").write(docx([markdown]))
"""
from __future__ import annotations

import io
import re
import zipfile

INLINE = re.compile(r"\*\*(.+?)\*\*|\*(.+?)\*|`(.+?)`|\[([^\]]+)\]\((https?:[^)\s]+|[^)\s]+)\)")
STIJLEN = {1: "Title", 2: "Heading1", 3: "Heading2", 4: "Heading3"}


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def run(tekst: str, eigen: str = "") -> str:
    if not tekst:
        return ""
    rpr = f"<w:rPr>{eigen}</w:rPr>" if eigen else ""
    return f'<w:r>{rpr}<w:t xml:space="preserve">{esc(tekst)}</w:t></w:r>'


def runs(tekst: str, basis: str = "") -> str:
    """Vet, cursief, code en links als losse runs; een link wordt 'tekst (adres)'."""
    uit, pos = [], 0
    for m in INLINE.finditer(tekst):
        uit.append(run(tekst[pos:m.start()], basis))
        if m.group(1) is not None:
            uit.append(runs(m.group(1), basis + "<w:b/>"))
        elif m.group(2) is not None:
            uit.append(runs(m.group(2), basis + "<w:i/>"))
        elif m.group(3) is not None:
            uit.append(run(m.group(3), basis + '<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/>'))
        else:
            uit.append(run(m.group(4), basis))
            uit.append(run(f" ({m.group(5)})", basis))
        pos = m.end()
    uit.append(run(tekst[pos:], basis))
    return "".join(uit)


def alinea(stijl: str, inhoud: str) -> str:
    return f'<w:p><w:pPr><w:pStyle w:val="{stijl}"/></w:pPr>{inhoud}</w:p>'


def cellen(regel: str) -> list[str]:
    return [c.strip() for c in regel.strip().strip("|").split("|")]


def tabel(rijen: list[str]) -> str:
    kop = cellen(rijen[0])
    # Kolombreedte naar de langste tekst in de kolom, tussen 8 en 60 tekens: een nummer smal, een omschrijving breed.
    gewicht = [min(max(max(len(cellen(r)[k]) if k < len(cellen(r)) else 0 for r in [rijen[0]] + rijen[2:]), 8), 60)
               for k in range(len(kop))]
    uit = ['<w:tbl><w:tblPr><w:tblStyle w:val="Tabel"/><w:tblW w:w="5000" w:type="pct"/></w:tblPr><w:tblGrid>'
           + "".join(f'<w:gridCol w:w="{9638 * g // sum(gewicht)}"/>' for g in gewicht) + "</w:tblGrid>"]
    for i, r in enumerate([rijen[0]] + rijen[2:]):
        c = cellen(r)
        if i == 0 and not any(c):
            continue  # een lege kopregel, zoals boven het titelblad
        c = (c + [""] * len(kop))[:len(kop)]
        uit.append("<w:tr>" + ("<w:trPr><w:tblHeader/></w:trPr>" if i == 0 else "")
                   + "".join('<w:tc><w:tcPr><w:tcW w:w="0" w:type="auto"/></w:tcPr>'
                             + alinea("Tabeltekst", runs(x, "<w:b/>" if i == 0 else "")) + "</w:tc>" for x in c)
                   + "</w:tr>")
    return "".join(uit) + "</w:tbl>" + alinea("Tabeleinde", "")


LIJST = re.compile(r"^(- |\d+\. )")


def blokken(md: str, kader: bool = False) -> str:
    """Dezelfde indeling als de html-functie op de generatorpagina."""
    regels, uit, i = md.split("\n"), [], 0
    tekststijl, lijststijl = ("Kader", "Kaderlijst") if kader else ("Normal", "Lijst")
    while i < len(regels):
        r = regels[i]
        if r.startswith(">"):
            blok = []
            while i < len(regels) and regels[i].startswith(">"):
                blok.append(re.sub(r"^> ?", "", regels[i]))
                i += 1
            uit.append(blokken("\n".join(blok), True))
            continue
        k = re.match(r"^(#{1,4}) (.*)$", r)
        if k:
            uit.append(alinea(STIJLEN[len(k.group(1))], runs(k.group(2))))
            i += 1
            continue
        if r.startswith("|"):
            rijen = []
            while i < len(regels) and regels[i].startswith("|"):
                rijen.append(regels[i])
                i += 1
            uit.append(tabel(rijen))
            continue
        if LIJST.match(r):
            genummerd = not r.startswith("- ")
            nummer = int(r.split(".", 1)[0]) if genummerd else 1
            items = []
            while i < len(regels) and re.match(r"^(- |\d+\. |  +\S)", regels[i]):
                if LIJST.match(regels[i]):
                    items.append(LIJST.sub("", regels[i], count=1))
                else:
                    items[-1] += " " + regels[i].strip()
                i += 1
            for n, item in enumerate(items):
                teken = f"{nummer + n}." if genummerd else "•"
                uit.append(alinea(lijststijl, run(teken) + "<w:r><w:tab/></w:r>" + runs(item)))
            continue
        if not r.strip():
            i += 1
            continue
        tekst = []
        while i < len(regels) and regels[i].strip() and not re.match(r"^(#|>|\||- |\d+\. )", regels[i]):
            tekst.append(regels[i])
            i += 1
        uit.append(alinea(tekststijl, runs(" ".join(tekst))))
    return "".join(uit)


NS = ('xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
      'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"')
PAGINA = ('<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1134" w:right="1134" w:bottom="1134" '
          'w:left="1134" w:header="567" w:footer="567" w:gutter="0"/></w:sectPr>')
NIEUWE_PAGINA = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'


def document_xml(stukken: list[str]) -> str:
    body = NIEUWE_PAGINA.join(blokken(md.strip("\n")) for md in stukken)
    return f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document {NS}><w:body>{body}{PAGINA}</w:body></w:document>'


def stijl(sid: str, naam: str, ppr: str = "", rpr: str = "", basis: str = "Normal", soort: str = "paragraph") -> str:
    return (f'<w:style w:type="{soort}" w:styleId="{sid}"><w:name w:val="{naam}"/>'
            + (f'<w:basedOn w:val="{basis}"/>' if basis else "") + '<w:qFormat/>'
            + (f"<w:pPr>{ppr}</w:pPr>" if ppr else "") + (f"<w:rPr>{rpr}</w:rPr>" if rpr else "") + "</w:style>")


BLAUW = '<w:color w:val="1F4E79"/>'
LIJN = '<w:{k} w:val="single" w:sz="4" w:space="0" w:color="C9D1DC"/>'
KADER = ('<w:pBdr><w:left w:val="single" w:sz="18" w:space="6" w:color="B9770E"/></w:pBdr>'
         '<w:shd w:val="clear" w:color="auto" w:fill="FDF6E3"/>')
STYLES = (
    f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:styles {NS}>'
    '<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:eastAsia="Calibri" '
    'w:cs="Calibri"/><w:sz w:val="22"/><w:szCs w:val="22"/><w:lang w:val="nl-NL"/></w:rPr></w:rPrDefault>'
    '<w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="264" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>'
    + stijl("Normal", "Normal", basis="")
    + stijl("Title", "Title", '<w:spacing w:after="240"/><w:pBdr><w:bottom w:val="single" w:sz="12" w:space="4" '
            'w:color="1F4E79"/></w:pBdr>', '<w:b/>' + BLAUW + '<w:sz w:val="40"/>')
    + stijl("Heading1", "heading 1", '<w:keepNext/><w:spacing w:before="360" w:after="120"/><w:outlineLvl w:val="0"/>',
            '<w:b/>' + BLAUW + '<w:sz w:val="28"/>')
    + stijl("Heading2", "heading 2", '<w:keepNext/><w:spacing w:before="240" w:after="80"/><w:outlineLvl w:val="1"/>',
            '<w:b/><w:sz w:val="24"/>')
    + stijl("Heading3", "heading 3", '<w:keepNext/><w:spacing w:before="200" w:after="60"/><w:outlineLvl w:val="2"/>',
            '<w:b/>')
    + stijl("Lijst", "Lijst", '<w:tabs><w:tab w:val="left" w:pos="425"/></w:tabs><w:spacing w:after="60"/>'
            '<w:ind w:left="425" w:hanging="425"/>')
    + stijl("Kader", "Kader", KADER + '<w:ind w:left="170" w:right="170"/>')
    + stijl("Kaderlijst", "Kaderlijst", KADER + '<w:tabs><w:tab w:val="left" w:pos="595"/></w:tabs>'
            '<w:spacing w:after="60"/><w:ind w:left="595" w:right="170" w:hanging="425"/>')
    + stijl("Tabeltekst", "Tabeltekst", '<w:spacing w:after="0" w:line="240" w:lineRule="auto"/>', '<w:sz w:val="18"/>')
    + stijl("Tabeleinde", "Tabeleinde", '<w:spacing w:after="0" w:line="120" w:lineRule="exact"/>')
    + '<w:style w:type="table" w:styleId="Tabel"><w:name w:val="Tabel"/><w:tblPr><w:tblBorders>'
    + "".join(LIJN.format(k=k) for k in ("top", "left", "bottom", "right", "insideH", "insideV"))
    + '</w:tblBorders><w:tblCellMar><w:top w:w="40" w:type="dxa"/><w:left w:w="80" w:type="dxa"/>'
    '<w:bottom w:w="40" w:type="dxa"/><w:right w:w="80" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>'
    "</w:styles>"
)
CONTENT_TYPES = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    '<Default Extension="xml" ContentType="application/xml"/>'
    '<Override PartName="/word/document.xml" '
    'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
    '<Override PartName="/word/styles.xml" '
    'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/></Types>'
)
RELS = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
    'Target="word/document.xml"/></Relationships>'
)
DOC_RELS = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" '
    'Target="styles.xml"/></Relationships>'
)


def delen(stukken: list[str]) -> dict[str, str]:
    """De onderdelen van het Word-bestand, in vaste volgorde."""
    return {"[Content_Types].xml": CONTENT_TYPES, "_rels/.rels": RELS, "word/document.xml": document_xml(stukken),
            "word/_rels/document.xml.rels": DOC_RELS, "word/styles.xml": STYLES}


def docx(stukken: list[str]) -> bytes:
    """Een .docx met elk stuk op een nieuwe pagina. Vaste datum in het zip-bestand, zodat dezelfde tekst
    hetzelfde bestand geeft."""
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for naam, inhoud in delen(stukken).items():
            info = zipfile.ZipInfo(naam, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, inhoud.encode("utf-8"))
    return buf.getvalue()


def zelfde_inhoud(a: bytes, b: bytes) -> bool:
    """Twee .docx-bestanden met dezelfde onderdelen; de compressie mag verschillen per zlib-versie."""
    try:
        with zipfile.ZipFile(io.BytesIO(a)) as x, zipfile.ZipFile(io.BytesIO(b)) as y:
            return (x.namelist() == y.namelist()
                    and all(x.read(n) == y.read(n) for n in x.namelist()))
    except zipfile.BadZipFile:
        return False
