"""Bouwt de platensets bij governance/quantumveilig-per-laag uit data/platen.json.

Gebruik:  python tools/bouw_quantumplaten.py           schrijft platen-<id>.html en img/<beeld>.svg
          python tools/bouw_quantumplaten.py --check   blokkeert als een bestand achterloopt op de data

Een set platen is een gewone html-pagina zonder externe bronnen: scroll-snap per plaat, bladeren met de
pijltjestoetsen, een knop die de feiten onthult. De opener van elke set is een beeld als inline svg; dezelfde
svg staat los in img/, zodat hij in een eigen presentatie te gebruiken is (in PowerPoint: invoegen als
afbeelding, daarna converteren naar vorm). De tekst in de beelden is echte tekst, geen pixels.

De beelden zijn hier getekend, niet in een tekenprogramma, zodat ze reproduceerbaar zijn en de test de
plaatsing van elk label kan narekenen (tools/test_quantumplaten.py).
"""
from __future__ import annotations

import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT / "governance" / "quantumveilig-per-laag"
DATA = MAP / "data" / "platen.json"

# Kleuren van de huisstijl (tools/huisstijl.py), plus een lichtblauw voor 'nog veilig'.
INKT, BLAUW, DONKER, ORANJE = "#14202b", "#154273", "#0d2b4d", "#e17000"
VLAK, LICHT, VEILIG = "#f4f6f9", "#c9d6e4", "#6fa8dc"
LETTER = "system-ui, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
B, H = 800, 450


def e(s: object) -> str:
    return html.escape(str(s), quote=True)


# ---------------------------------------------------------------- svg-bouwstenen

def tekst(x: float, y: float, s: str, maat: int = 17, vet: bool = False, kleur: str = LICHT,
          anker: str = "middle") -> str:
    return (f'<text x="{x:g}" y="{y:g}" font-size="{maat}" font-weight="{700 if vet else 400}" '
            f'text-anchor="{anker}" fill="{kleur}">{e(s)}</text>')


def vlak(x: float, y: float, b: float, h: float, kleur: str, rand: str | None = None, r: float = 0,
         extra: str = "") -> str:
    lijn = f' stroke="{rand}" stroke-width="2"' if rand else ""
    return f'<rect x="{x:g}" y="{y:g}" width="{b:g}" height="{h:g}" rx="{r:g}" fill="{kleur}"{lijn}{extra}/>'


def lijn(x1: float, y1: float, x2: float, y2: float, kleur: str = LICHT, dikte: float = 2,
         streep: bool = False) -> str:
    s = ' stroke-dasharray="7 6"' if streep else ""
    return (f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" stroke="{kleur}" '
            f'stroke-width="{dikte:g}"{s}/>')


def pijl(x1: float, x2: float, y: float) -> str:
    return (lijn(x1, y, x2 - 10, y, LICHT, 3) +
            f'<polygon points="{x2:g},{y:g} {x2 - 14:g},{y - 8:g} {x2 - 14:g},{y + 8:g}" fill="{LICHT}"/>')


def slot(cx: float, top: float, b: float, kleur: str, open_: bool) -> str:
    """Hangslot met de beugel boven het lichaam; open = beugel aan een kant los en omhoog."""
    h = b * 0.8
    r = b * 0.3
    links, rechts = cx - r, cx + r
    lichaam = vlak(cx - b / 2, top, b, h, kleur, r=b * 0.12)
    if open_:
        beugel = f"M{rechts:g} {top:g} v{-r * 1.4:g} a{r:g} {r:g} 0 0 0 {-2 * r:g} 0 v{-r * 0.2:g}"
    else:
        beugel = f"M{links:g} {top:g} v{-r * 0.6:g} a{r:g} {r:g} 0 0 1 {2 * r:g} 0 v{r * 0.6:g}"
    return (f'<path d="{beugel}" fill="none" stroke="{kleur}" stroke-width="{max(3, b * 0.15):g}" '
            f'stroke-linecap="round"/>' + lichaam)


def svg(titel: str, beschrijving: str, delen: list[str]) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {B} {H}" role="img" '
            f'aria-labelledby="t d" font-family="{LETTER}">'
            f'<title id="t">{e(titel)}</title><desc id="d">{e(beschrijving)}</desc>'
            + vlak(1, 1, B - 2, H - 2, DONKER, "#2f5682", r=16) + "".join(delen) + "</svg>")


# ---------------------------------------------------------------- de vijf beelden

def beeld_op_straat() -> str:
    d = [lijn(40, 376, 760, 376, LICHT, 2)]
    # 2026: envelop met dicht slot
    d += [vlak(95, 165, 110, 72, VLAK, r=4),
          f'<polyline points="95,165 150,207 205,165" fill="none" stroke="{BLAUW}" stroke-width="3"/>',
          slot(198, 222, 30, VEILIG, open_=False),
          tekst(150, 305, "2026", 30, True, "#ffffff"), tekst(150, 334, "versleuteld verstuurd", 19)]
    d.append(pijl(240, 318, 205))
    # bewaard: archiefdoos vol enveloppen
    d += [vlak(345, 170, 110, 80, BLAUW, LICHT, 4), vlak(338, 156, 124, 18, BLAUW, LICHT, 3)]
    for i in range(3):
        d.append(vlak(362 + i * 6, 186 + i * 16, 64, 14, VLAK, r=2))
    d += [tekst(400, 305, "bewaard", 30, True, "#ffffff"), tekst(400, 334, "door de aanvaller", 19)]
    d.append(pijl(482, 560, 205))
    # 2030: open slot, papieren op straat
    d += [slot(650, 196, 56, ORANJE, open_=True),
          tekst(650, 305, "2030", 30, True, ORANJE), tekst(650, 334, "open op straat", 19)]
    for x, y, hoek in ((588, 352, -12), (628, 358, 8), (668, 350, -4), (708, 356, 14)):
        d.append(vlak(x, y, 34, 14, VLAK, r=2, extra=f' transform="rotate({hoek} {x + 17} {y + 7})"'))
    return svg("Wat je vandaag versleutelt, ligt in 2030 op straat",
               "Een envelop met een dicht slot wordt in 2026 verstuurd, door een aanvaller onderschept en "
               "bewaard, en in 2030 met een open slot geopend: de papieren liggen op straat.", d)


def beeld_verbouwing() -> str:
    d = [f'<polygon points="205,92 370,48 535,92" fill="{BLAUW}" stroke="{LICHT}" stroke-width="2"/>']
    for i, naam in enumerate(("ICT en beheer", "Bedrijfsvoering", "Sociaal domein", "Dienstverlening")):
        top = 92 + i * 55
        d += [vlak(220, top, 300, 55, BLAUW, LICHT), tekst(240, top + 34, naam, 17, anker="start")]
    d += [vlak(470, 262, 36, 48, DONKER, LICHT, 2), vlak(408, 272, 52, 20, ORANJE, r=3),
          tekst(434, 287, "OPEN", 12, True, "#ffffff")]
    # steiger
    for x in (545, 595):
        d.append(lijn(x, 70, x, 310, ORANJE, 4))
    for y in (92, 147, 202, 257):
        d.append(lijn(535, y, 605, y, ORANJE, 4))
    d += [tekst(625, 182, "vijf jaar", 26, True, ORANJE, "start"), tekst(625, 207, "verbouwen", 17, anker="start")]
    d.append(lijn(120, 310, 680, 310, LICHT, 2))
    # tijdbalk
    d += [vlak(220, 342, 380, 10, ORANJE, r=5), tekst(220, 382, "2026", 16, True, "#ffffff"),
          tekst(600, 382, "2030", 16, True, "#ffffff"), tekst(410, 420, "en de winkel blijft open")]
    return svg("Een verbouwing van het hele pand, terwijl de winkel open blijft",
               "Een gebouw met vier verdiepingen (ICT en beheer, bedrijfsvoering, sociaal domein, "
               "dienstverlening) staat in de steigers van 2026 tot 2030; beneden hangt een bordje open.", d)


def beeld_mosca() -> str:
    x0, px = 110, 38  # 2026 op x0, 38 pixels per jaar

    def x(jaar: float) -> float:
        return x0 + (jaar - 2026) * px

    d = [tekst(x0, 108, "jouw gegevens", 17, anker="start"),
         vlak(x(2026), 120, x(2031) - x(2026), 48, VEILIG, r=4),
         tekst((x(2026) + x(2031)) / 2, 150, "overstap: 5 jaar", 17, True, DONKER),
         vlak(x(2031), 120, x(2041) - x(2031), 48, VLAK, r=4),
         tekst((x(2031) + x(2041)) / 2, 150, "moet geheim blijven: 10 jaar", 17, True, DONKER),
         # rechts uitgelijnd vlak voor de stippellijn van 2030, zodat een bredere letter er niet doorheen loopt
         tekst(x(2030) - 10, 222, "quantumcomputer", 17, anker="end"),
         vlak(x(2026), 234, x(2030) - x(2026), 48, BLAUW, LICHT, 4),
         tekst((x(2026) + x(2030)) / 2, 264, "2030", 17, True, "#ffffff"),
         # de stippellijn van 2030 loopt van onder de bovenste balk naar de as, niet door een label
         lijn(x(2030), 172, x(2030), 322, ORANJE, 3, streep=True),
         # haak onder de rij: het deel na 2030 is nu al kwetsbaar
         lijn(x(2030), 186, x(2041), 186, ORANJE, 4), lijn(x(2041), 178, x(2041), 194, ORANJE, 4),
         tekst((x(2030) + x(2041)) / 2 + 40, 214, "nu al kwetsbaar", 20, True, ORANJE),
         lijn(x0, 322, x(2042), 322, LICHT, 2)]
    for jaar in (2026, 2030, 2035, 2040):
        d += [lijn(x(jaar), 316, x(jaar), 328, LICHT, 2), tekst(x(jaar), 350, str(jaar), 17)]
    d.append(tekst(400, 405, "overstap + geheimhouding  >  tijd tot de quantumcomputer", 18, True, "#ffffff"))
    return svg("De ongelijkheid van Mosca",
               "Twee balken. Jouw gegevens: vijf jaar overstap plus tien jaar geheimhouding, tot 2041. De "
               "quantumcomputer: 2030. Alles na 2030 in de bovenste balk is nu al kwetsbaar.", d)


def beeld_inventaris() -> str:
    d = [vlak(60, 70, 320, 300, BLAUW, r=12), vlak(420, 70, 320, 300, BLAUW, r=12)]
    for cx in (120, 220, 320):
        for cy in (150, 245):
            d += [vlak(cx - 32, cy - 24, 64, 40, VLAK, r=3), vlak(cx - 40, cy + 16, 80, 8, LICHT, r=2),
                  f'<circle cx="{cx + 30}" cy="{cy - 24}" r="11" fill="{VEILIG}"/>',
                  f'<path d="M{cx + 24} {cy - 24} l4 5 l8 -10" fill="none" stroke="{DONKER}" stroke-width="3"/>']
    for cx in (480, 580, 680):
        for cy in (150, 245):
            d += [vlak(cx - 28, cy - 22, 56, 40, VLAK, r=3),
                  lijn(cx - 20, cy - 10, cx + 8, cy - 10, BLAUW, 3), lijn(cx - 20, cy, cx + 2, cy, BLAUW, 3),
                  f'<circle cx="{cx + 16}" cy="{cy + 10}" r="7" fill="{ORANJE}"/>',
                  tekst(cx + 38, cy - 14, "?", 26, True, ORANJE)]
    d += [tekst(220, 322, "laptops", 22, True, "#ffffff"), tekst(220, 348, "allemaal in beeld", 19),
          tekst(580, 322, "certificaten en sleutels", 22, True, "#ffffff"), tekst(580, 348, "niemand weet waar", 19)]
    return svg("Van elke laptop weet je waar hij is, van geen enkel certificaat",
               "Links zes laptops met een vinkje. Rechts zes certificaten met een vraagteken.", d)


def beeld_levensduur() -> str:
    x0, px = 100, 600 / 19  # 2026 tot 2045 over 600 pixels; ruimte aan beide kanten voor de jaarlabels

    def x(jaar: float) -> float:
        return x0 + (jaar - 2026) * px

    d = [  # gemaal: gebouw, dak, uitstroombuis, water
        f'<polygon points="410,112 470,84 530,112" fill="{BLAUW}" stroke="{LICHT}" stroke-width="2"/>',
        vlak(420, 112, 100, 70, BLAUW, LICHT), vlak(456, 142, 28, 40, DONKER, LICHT),
        vlak(520, 150, 60, 12, LICHT), vlak(568, 150, 12, 44, LICHT),
        f'<path d="M550 200 q15 -10 30 0 t30 0 t30 0 t30 0 t30 0" fill="none" stroke="{VEILIG}" stroke-width="4"/>',
        tekst(400, 152, "gemaal", 20, True, "#ffffff", "end"),
        slot(x(2030), 200, 32, ORANJE, open_=True),
        vlak(x(2026), 250, x(2030) - x(2026), 40, VEILIG, r=4),
        tekst((x(2026) + x(2030)) / 2, 276, "veilig", 17, True, DONKER),
        vlak(x(2030), 250, x(2045) - x(2030), 40, ORANJE, r=4),
        tekst((x(2030) + x(2045)) / 2, 276, "slot kan open: vijftien jaar", 17, True, "#ffffff")]
    for jaar, onder in ((2026, "aanschaf"), (2030, "quantumcomputer"), (2045, "einde levensduur")):
        d += [lijn(x(jaar), 294, x(jaar), 304, LICHT, 2), tekst(x(jaar), 324, str(jaar), 16, True, "#ffffff"),
              tekst(x(jaar), 348, onder, 17)]
    return svg("Een gemaal dat tot 2045 draait, met een slot dat in 2030 open kan",
               "Een gemaal gekocht in 2026 draait tot 2045. Tot 2030 is de versleuteling veilig, daarna "
               "vijftien jaar niet meer.", d)


BEELDEN = {"op-straat": beeld_op_straat, "verbouwing": beeld_verbouwing, "mosca": beeld_mosca,
           "inventaris": beeld_inventaris, "levensduur": beeld_levensduur}


# ---------------------------------------------------------------- de platen

CSS = """
:root{--inkt:#14202b;--blauw:#154273;--donker:#0d2b4d;--oranje:#e17000;--vlak:#f4f6f9;--licht:#c9d6e4;
--sans:system-ui,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif}
[hidden]{display:none!important}
*{box-sizing:border-box}
html{scroll-snap-type:y mandatory;scroll-behavior:smooth;background:var(--donker)}
body{margin:0;font:18px/1.5 var(--sans);color:#fff;background:var(--donker)}
.balk{position:fixed;top:0;left:0;right:0;z-index:2;display:flex;gap:.75rem;align-items:center;
padding:.55rem 16px;background:rgba(13,43,77,.92);color:var(--licht);font-size:14px}
.balk a{color:#fff;text-decoration:none;font-weight:600}.balk a:hover{text-decoration:underline}
.balk .publiek{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.teller{font-variant-numeric:tabular-nums}
.plaat{min-height:100vh;min-height:100svh;scroll-snap-align:start;display:flex;flex-direction:column;
justify-content:center;padding:4.5rem 16px 3rem;max-width:72rem;margin:0 auto;position:relative}
.plaat h1{font-size:clamp(2rem,5vw,3.4rem);line-height:1.1;letter-spacing:-.02em;margin:0 0 1rem}
.plaat h1::after{content:'';display:block;width:3.5rem;height:4px;border-radius:2px;background:var(--oranje);
margin-top:1rem}
.plaat h2{font-size:clamp(1.8rem,4.6vw,3.3rem);line-height:1.15;letter-spacing:-.02em;margin:0 0 1.2rem;
max-width:24ch;overflow-wrap:break-word}
.plaat.vraag h2{color:var(--oranje)}
.plaat p{max-width:40rem}
.sub{color:var(--licht);font-size:1.15rem}
.hulp{color:var(--licht);font-size:.95rem;margin-top:2rem}
kbd{border:1px solid var(--licht);border-radius:4px;padding:0 .35em;font:inherit;font-size:.9em}
.onthul-knop{align-self:flex-start;font:inherit;font-size:1rem;font-weight:600;color:var(--donker);
background:var(--oranje);border:0;border-radius:999px;padding:.55rem 1.2rem;cursor:pointer;margin-top:.4rem}
.onthul-knop:focus-visible,.nav button:focus-visible{outline:3px solid #fff;outline-offset:3px}
.onthul{list-style:none;padding:0;margin:1.2rem 0 0;max-width:46rem}
.onthul li{border-left:4px solid var(--oranje);padding:.35rem 0 .35rem 1rem;margin:.6rem 0;font-size:1.2rem}
.plaat.beeld .raster{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr);gap:2.5rem;align-items:center}
.plaat.beeld h2{font-size:clamp(1.6rem,3.4vw,2.6rem)}
.beeld-svg svg{width:100%;height:auto;display:block;border-radius:16px}
.bron{position:absolute;left:16px;right:16px;bottom:.9rem;margin:0;color:var(--licht);font-size:.8rem}
.nav{position:fixed;right:16px;bottom:16px;z-index:2;display:flex;gap:.5rem}
.nav button{font:inherit;font-size:1.1rem;width:2.6rem;height:2.6rem;border-radius:50%;border:1px solid var(--licht);
background:var(--donker);color:#fff;cursor:pointer}
@media (max-width:820px){
html{scroll-snap-type:y proximity}
.plaat.beeld .raster{grid-template-columns:1fr;gap:1.2rem}
.plaat{padding-bottom:4.5rem}
.onthul li{font-size:1.05rem}
.bron{bottom:4rem}
}
@media print{
@page{size:A4 landscape;margin:12mm}
html,body{background:#fff;color:var(--inkt)}
.balk,.nav,.onthul-knop,.hulp{display:none!important}
.onthul[hidden]{display:block!important}
.plaat{min-height:0;height:auto;padding:0;page-break-after:always;break-after:page}
.plaat h2,.plaat h1{color:var(--donker)}.plaat.vraag h2{color:var(--oranje)}
.sub,.bron{color:#4b5563}.bron{position:static;margin-top:1.5rem}
}
"""

JS = """
(function(){
var platen=[].slice.call(document.querySelectorAll('.plaat'));
var teller=document.querySelector('.teller');
var huidig=0;
function zet(i){huidig=i;teller.textContent=(i+1)+' / '+platen.length;}
function ga(i){if(i<0||i>=platen.length)return;platen[i].scrollIntoView({behavior:'smooth',block:'start'});zet(i);}
function onthul(p,toon){var lijst=p.querySelector('.onthul'),knop=p.querySelector('.onthul-knop');
if(!lijst)return false;var open=toon===undefined?lijst.hidden:toon;lijst.hidden=!open;
knop.setAttribute('aria-expanded',open?'true':'false');knop.textContent=open?'Verberg':'Onthul';return true;}
platen.forEach(function(p){var k=p.querySelector('.onthul-knop');if(k)k.addEventListener('click',function(){onthul(p);});});
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(en){
if(en.isIntersecting&&en.intersectionRatio>=.5)zet(platen.indexOf(en.target));});},{threshold:[.5]});
platen.forEach(function(p){io.observe(p);});}
document.addEventListener('keydown',function(ev){
if(ev.altKey||ev.ctrlKey||ev.metaKey)return;
var t=ev.target&&ev.target.tagName;
if(['ArrowDown','ArrowRight','PageDown',' '].indexOf(ev.key)>-1){
var p=platen[huidig],l=p.querySelector('.onthul');
if(ev.key!=='PageDown'&&l&&l.hidden){onthul(p,true);}else{ga(huidig+1);}ev.preventDefault();}
else if(['ArrowUp','ArrowLeft','PageUp'].indexOf(ev.key)>-1){ga(huidig-1);ev.preventDefault();}
else if(ev.key==='Home'){ga(0);ev.preventDefault();}
else if(ev.key==='End'){ga(platen.length-1);ev.preventDefault();}
else if((ev.key==='o'||ev.key==='O'||ev.key==='Enter')&&t!=='BUTTON'&&t!=='A'){onthul(platen[huidig]);ev.preventDefault();}
});
document.querySelector('.nav .vorige').addEventListener('click',function(){ga(huidig-1);});
document.querySelector('.nav .volgende').addEventListener('click',function(){ga(huidig+1);});
zet(0);
})();
"""


def plaat_html(nr: int, totaal: int, plaat: dict) -> str:
    soort = plaat["soort"]
    oid = f"o{nr}"
    lijst = "".join(f"<li>{e(r)}</li>" for r in plaat["onthul"])
    knop = (f'<button type="button" class="onthul-knop" aria-expanded="false" aria-controls="{oid}">Onthul</button>'
            f'<ul class="onthul" id="{oid}" hidden>{lijst}</ul>')
    bron = f'<p class="bron">Bron: {e(plaat["bron"])}</p>'
    kop = f'<h2>{e(plaat["kop"])}</h2>'
    if soort == "beeld":
        uitleg = f'<p class="sub">{e(plaat["tekst"])}</p>' if plaat.get("tekst") else ""
        binnen = (f'<div class="raster"><div class="beeld-svg">{BEELDEN[plaat["beeld"]]()}</div>'
                  f'<div class="tekst">{kop}{uitleg}{knop}</div></div>')
    else:
        binnen = kop + knop
    return (f'<section class="plaat {soort}" id="plaat-{nr}" aria-label="Plaat {nr} van {totaal}">'
            f'{binnen}{bron}</section>\n')


def deck_html(deck: dict) -> str:
    platen = deck["platen"]
    totaal = len(platen) + 1
    titelplaat = (f'<section class="plaat titel" id="plaat-1" aria-label="Plaat 1 van {totaal}">'
                  f'<h1>{e(deck["titel"])}</h1><p class="sub">Voor: {e(deck["publiek"])}</p>'
                  f'<p class="hulp">Bladeren met <kbd>↓</kbd> en <kbd>↑</kbd>. Op een plaat met feiten '
                  f'onthult <kbd>↓</kbd> eerst de feiten. <kbd>O</kbd> onthult of verbergt.</p></section>\n')
    body = titelplaat + "".join(plaat_html(i + 2, totaal, p) for i, p in enumerate(platen))
    return (
        "<!doctype html>\n<html lang=\"nl\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        f"<title>{e(deck['titel'])}</title>\n"
        f"<meta name=\"description\" content=\"Platen bij Quantumveilig per laag, voor {e(deck['publiek'])}.\">\n"
        "<!-- Gegenereerd door tools/bouw_quantumplaten.py uit data/platen.json; niet met de hand wijzigen. -->\n"
        f"<style>{CSS.strip()}</style>\n</head>\n<body>\n"
        f'<header class="balk"><a href="./">Quantumveilig per laag</a>'
        f'<span class="publiek">{e(deck["publiek"])}</span><span class="teller" aria-live="polite">1 / {totaal}</span>'
        "</header>\n<main>\n" + body + "</main>\n"
        '<nav class="nav" aria-label="Bladeren"><button type="button" class="vorige" aria-label="Vorige plaat">↑</button>'
        '<button type="button" class="volgende" aria-label="Volgende plaat">↓</button></nav>\n'
        f"<script>{JS.strip()}</script>\n</body>\n</html>\n")


def doelen() -> dict[Path, str]:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    uit: dict[Path, str] = {}
    for deck in data["decks"]:
        uit[MAP / f"platen-{deck['id']}.html"] = deck_html(deck)
        for p in deck["platen"]:
            if p["soort"] == "beeld":
                uit[MAP / "img" / f"{p['beeld']}.svg"] = BEELDEN[p["beeld"]]() + "\n"
    return uit


def main(argv: list[str]) -> int:
    check = "--check" in argv
    achter = []
    for pad, inhoud in doelen().items():
        oud = pad.read_text(encoding="utf-8") if pad.exists() else None
        if oud == inhoud:
            continue
        if check:
            achter.append(pad.relative_to(ROOT).as_posix())
        else:
            pad.parent.mkdir(parents=True, exist_ok=True)
            pad.write_text(inhoud, encoding="utf-8", newline="\n")
            print("geschreven:", pad.relative_to(ROOT).as_posix())
    if achter:
        print("Loopt achter op data/platen.json; draai python tools/bouw_quantumplaten.py:")
        for p in achter:
            print("  ", p)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
