"""Huisstijl op het scherm: de kleuren en de letter van de voorpagina (site/thema.css in de root-site).

Een plek voor de opmaak die `build.py`, `bouw_beleidsset.py` en `bouw_risicoregister.py` in hun pagina's
zetten. Twee soorten:

- **leesversie**: een pagina met de standaard leesopmaak (het Calibri-sjabloon). Krijgt de volle huisstijl:
  letter, koppen, tabellen, kaders en het kruimelpad als donkere balk.
- **instrument**: een pagina met een eigen ontwerp (een toets, een generator, een verkenner). Krijgt alleen
  de letter, de kleurtokens en de balk; de eigen opbouw blijft staan.

Alles staat binnen `@media screen`: afdrukken en plakken in Word gebruiken de eigen opmaak van de pagina
(statuut B3). Het blok brengt een viewport-regel mee als de pagina er geen heeft; zonder die regel toont een
telefoon de pagina verkleind op desktopbreedte.
"""
from __future__ import annotations

import re

START = "<!-- huisstijl -->"
EIND = "<!-- /huisstijl -->"
VIEWPORT = '<meta name="viewport" content="width=device-width, initial-scale=1">'

# De standaard leesopmaak van een leesversie; daaraan herken je een leesversie.
LEESKOLOM = "font-family:Calibri"

BLAUW = "#154273"
TOKENS = (
    ":root{--inkt:#14202b;--blauw:#154273;--blauw-donker:#0d2b4d;--oranje:#e17000;--vlak:#f4f6f9;"
    "--lijn:#dde3ea;--grijs:#4b5563;--sans:system-ui,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif}"
)
# html body ervoor: de eigen stijl van het kruimelpad staat later in de pagina en zou anders winnen.
# De balk loopt naar links, rechts en boven door tot de rand van het venster (box-shadow, door clip-path
# alleen onderaan afgesneden): staat het kruimelpad in een kop met eigen bovenruimte, dan blijft er geen witte
# strook boven de balk. Staat het kruimelpad buiten de inhoudskolom (over de volle breedte), dan zet de pagina
# zelf --kruimel-breedte (breedte van de tekstkolom) en --kruimel-rand (minimale rand op een smal scherm); de
# tekst in de balk lijnt dan uit met de titel. Zonder die variabelen is de binnenruimte nul.
KRUIMEL = (
    "html body .kruimel{background:var(--blauw-donker);color:#c9d6e4;margin:0 0 2.8rem;padding-top:1.05rem;"
    "padding-bottom:1.05rem;padding-left:max(var(--kruimel-rand,0px),calc((100% - var(--kruimel-breedte,100%))/2));"
    "padding-right:max(var(--kruimel-rand,0px),calc((100% - var(--kruimel-breedte,100%))/2));"
    "box-shadow:0 0 0 100vmax var(--blauw-donker);clip-path:inset(-100vmax -100vmax 0 -100vmax);"
    "font:14px/1.5 var(--sans)}"
    "html body .kruimel a{color:#fff;text-decoration:none}html body .kruimel a:hover{text-decoration:underline}"
    "html body .kruimel span{color:#c9d6e4}"
)

LEESVERSIE_CSS = (
    "@media screen{" + TOKENS +
    "html{background:#fff}"
    "body{font:17px/1.65 var(--sans);color:var(--inkt);max-width:46rem;box-sizing:border-box;"
    "margin:0 auto;padding:0 1.25rem 4rem}" + KRUIMEL +
    "h1{font-family:var(--sans);font-size:clamp(1.9rem,4.2vw,2.6rem);font-weight:800;line-height:1.15;"
    "letter-spacing:-.025em;color:var(--inkt);border:0;padding:0;margin:0 0 .5rem;hyphens:auto;"
    "overflow-wrap:break-word}"
    "h1::after{content:'';display:block;width:3.5rem;height:4px;border-radius:2px;"
    "background:var(--oranje);margin-top:.9rem}"
    "h2{font-family:var(--sans);font-size:1.45rem;font-weight:750;letter-spacing:-.02em;color:var(--inkt);"
    "margin:2.6rem 0 .6rem;padding-top:1.3rem;border-top:1px solid var(--lijn)}"
    "h3{font-family:var(--sans);font-size:1.12rem;font-weight:700;color:var(--inkt);margin:1.7rem 0 .4rem}"
    "p{margin:.7em 0}li{margin:.3em 0}"
    "a{color:var(--blauw);text-underline-offset:2px}"
    # Een tabel die niet in de kolom past, scrolt binnen zichzelf, op elke breedte. Als blok met
    # fit-content: een tabel met lange tekst vult de kolom en breekt af, alleen een tabel waarvan de
    # kleinst mogelijke breedte niet past krijgt een schuifbalk. De pagina zelf scrolt nooit zijwaarts.
    "table{font-size:.88rem;border:1px solid var(--lijn);border-radius:8px;border-collapse:separate;"
    "border-spacing:0;margin:1em 0;display:block;overflow-x:auto;max-width:100%;width:fit-content}"
    "p,li,th,td{overflow-wrap:break-word}"
    "pre{white-space:pre-wrap;overflow-wrap:anywhere;max-width:100%}"
    "th,td{border:0;border-bottom:1px solid var(--lijn);padding:.55em .75em}"
    "tr:last-child td{border-bottom:0}th{background:var(--vlak);font-weight:650;color:var(--inkt)}"
    "blockquote{border-left:4px solid var(--oranje);background:#fff7ef;border-radius:0 8px 8px 0;"
    "padding:.8em 1.1em;margin:1.3em 0}"
    "code{font-family:ui-monospace,Consolas,'Cascadia Mono',monospace;font-size:.88em;"
    "background:var(--vlak);padding:.1em .35em;border-radius:4px}"
    "@media (max-width:620px){body{font-size:16px;padding:0 1rem 3rem}}"
    "}"
)

# Een instrument houdt zijn eigen opbouw; alleen letter, tokens en balk. De letter op body en op de
# formulierelementen, die de letter van de pagina niet vanzelf erven.
INSTRUMENT_CSS = (
    "@media screen{" + TOKENS +
    "body,button,input,select,textarea{font-family:var(--sans)}"
    # De paginatitel in inkt, zoals op de voorpagina; de eigen kleur van het instrument blijft voor de rest.
    "h1{color:var(--inkt)}" + KRUIMEL +
    "}"
)


def blok(soort: str, met_viewport: bool) -> str:
    css = LEESVERSIE_CSS if soort == "leesversie" else INSTRUMENT_CSS
    return f"{START}{VIEWPORT if met_viewport else ''}<style>{css}</style>{EIND}"


def soort_van(tekst: str) -> str:
    return "leesversie" if LEESKOLOM in tekst else "instrument"


def zet(tekst: str, soort: str | None = None) -> str:
    """Zet het huisstijlblok in de </head>, of vervang het bestaande. Idempotent.

    Een viewport-regel komt alleen mee als de pagina er buiten het blok nog geen heeft.
    """
    zonder = re.sub(re.escape(START) + ".*?" + re.escape(EIND), "", tekst, flags=re.S)
    nieuw = blok(soort or soort_van(zonder), 'name="viewport"' not in zonder)
    if START in tekst:
        return re.sub(re.escape(START) + ".*?" + re.escape(EIND), lambda _: nieuw, tekst, count=1, flags=re.S)
    return tekst.replace("</head>", nieuw + "</head>", 1)
