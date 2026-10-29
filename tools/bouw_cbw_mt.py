"""Bouwt de platen bij governance/cbw-uitleggen-aan-het-mt uit data/platen.json.

Gebruik:  python tools/bouw_cbw_mt.py                 schrijft platen.html, draaiboek.md en img/<beeld>.svg
          python tools/bouw_cbw_mt.py --check         blokkeert als een bestand achterloopt op de data
          python tools/bouw_cbw_mt.py --invul eigen.json --uit eigen-platen.html
                                                      maakt een versie voor de eigen organisatie

De platen zijn een sjabloon. Tekst tussen accolades ({gemeente}, {datum}, {contact}) en de drie platen
'Waar staan we nu?' vult een organisatie zelf in, met een kopie van data/invulblok.json. Zonder invulblok
staan op die plekken zichtbare invulvelden. Een foto (gemeentehuis, een eigen proces) gaat als data-URI in
de pagina, zodat het bestand op zichzelf blijft staan.

De beelden zijn hier getekend en niet in een tekenprogramma, zodat ze reproduceerbaar zijn en de test de
plaatsing van elk label kan narekenen (tools/test_cbw_mt.py). Elke svg staat ook los in img/, om in een
eigen presentatie te gebruiken (in PowerPoint: invoegen als afbeelding, daarna converteren naar vorm).
"""
from __future__ import annotations

import base64
import html
import json
import mimetypes
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP = ROOT / "governance" / "cbw-uitleggen-aan-het-mt"
DATA = MAP / "data" / "platen.json"
INVUL_SJABLOON = MAP / "data" / "invulblok.json"
LIVE = "https://security-commons-nl.github.io/kennisbank/governance/cbw-uitleggen-aan-het-mt/"

# Kleuren van de huisstijl (tools/huisstijl.py), plus lichtblauw voor water en groen voor een park.
INKT, BLAUW, DONKER, ORANJE = "#14202b", "#154273", "#0d2b4d", "#e17000"
VLAK, LICHT, VEILIG, GROEN = "#f4f6f9", "#c9d6e4", "#6fa8dc", "#2e6b4f"
WEG, RAND = "#244a73", "#2f5682"
LETTER = "system-ui, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
B, H = 800, 450

BIV = {"B": "beschikbaarheid", "I": "integriteit", "V": "vertrouwelijkheid"}
STATUS = {"groen": "op orde", "oranje": "deels", "rood": "niet op orde", "onbekend": "nog in te vullen"}
INVULVELDEN = ("gemeente", "datum", "contact")


def e(s: object) -> str:
    return html.escape(str(s), quote=True)


# ---------------------------------------------------------------- svg-bouwstenen

def tekst(x: float, y: float, s: str, maat: int = 17, vet: bool = False, kleur: str = LICHT,
          anker: str = "middle") -> str:
    return (f'<text x="{x:g}" y="{y:g}" font-size="{maat}" font-weight="{700 if vet else 400}" '
            f'text-anchor="{anker}" fill="{kleur}">{e(s)}</text>')


def vlak(x: float, y: float, b: float, h: float, kleur: str, rand: str | None = None, r: float = 0,
         extra: str = "") -> str:
    lijn_ = f' stroke="{rand}" stroke-width="2"' if rand else ""
    return f'<rect x="{x:g}" y="{y:g}" width="{b:g}" height="{h:g}" rx="{r:g}" fill="{kleur}"{lijn_}{extra}/>'


def lijn(x1: float, y1: float, x2: float, y2: float, kleur: str = LICHT, dikte: float = 2,
         streep: bool = False) -> str:
    s = ' stroke-dasharray="7 6"' if streep else ""
    return (f'<line x1="{x1:g}" y1="{y1:g}" x2="{x2:g}" y2="{y2:g}" stroke="{kleur}" '
            f'stroke-width="{dikte:g}" stroke-linecap="round"{s}/>')


def pijl(x1: float, y1: float, x2: float, y2: float, kleur: str = LICHT) -> str:
    """Pijl van (x1,y1) naar (x2,y2); de punt is een driehoek in de looprichting."""
    dx, dy = x2 - x1, y2 - y1
    lengte = (dx * dx + dy * dy) ** 0.5 or 1
    ux, uy = dx / lengte, dy / lengte
    bx, by = x2 - ux * 14, y2 - uy * 14
    px, py = -uy * 8, ux * 8
    return (lijn(x1, y1, bx, by, kleur, 3) +
            f'<polygon points="{x2:g},{y2:g} {bx + px:g},{by + py:g} {bx - px:g},{by - py:g}" fill="{kleur}"/>')


def label(x: float, y: float, s: str, maat: int = 15, vet: bool = True, achter: str = VLAK,
          kleur: str = DONKER) -> str:
    """Tekst op een eigen plaatje, zodat een weg of lijn eronder het woord niet raakt.

    De breedte is een ruime schatting; de test meet met een echte letter of het woord erin past.
    """
    b = len(s) * maat * (0.68 if vet else 0.58) + 20
    h = maat + 12
    return (f'<rect x="{x - b / 2:g}" y="{y - h + 6:g}" width="{b:g}" height="{h:g}" rx="{h / 2:g}" '
            f'fill="{achter}" data-label="1"/>' + tekst(x, y, s, maat, vet, kleur))


def gevaar(cx: float, top: float, s: float = 40) -> str:
    """Waarschuwingsdriehoek met uitroepteken, als vormen en niet als letter (dan meet de test hem als vlak)."""
    h = s * 0.87
    punten = f"{cx:g},{top:g} {cx - s / 2:g},{top + h:g} {cx + s / 2:g},{top + h:g}"
    return (f'<g data-gevaar="{cx - s / 2:g} {top:g} {cx + s / 2:g} {top + h:g}">'
            f'<polygon points="{punten}" fill="{ORANJE}" stroke="{DONKER}" stroke-width="2" '
            f'stroke-linejoin="round"/>'
            f'<rect x="{cx - s * 0.055:g}" y="{top + h * 0.33:g}" width="{s * 0.11:g}" height="{h * 0.36:g}" '
            f'rx="{s * 0.04:g}" fill="{DONKER}"/>'
            f'<circle cx="{cx:g}" cy="{top + h * 0.83:g}" r="{s * 0.065:g}" fill="{DONKER}"/></g>')


def persoon(cx: float, top: float, kleur: str = LICHT, streep: bool = False) -> str:
    s = ' stroke-dasharray="5 4" fill="none"' if streep else f' fill="{kleur}"'
    rand = f' stroke="{kleur}" stroke-width="2"' if streep else ""
    return (f'<circle cx="{cx:g}" cy="{top + 18:g}" r="18"{s}{rand}/>'
            f'<path d="M{cx - 32:g} {top + 92:g} q0 -50 32 -50 q32 0 32 50 z"{s}{rand}/>')


def svg(titel: str, beschrijving: str, delen: list[str], naam: str) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {B} {H}" role="img" '
            f'aria-labelledby="t-{naam} d-{naam}" font-family="{LETTER}">'
            f'<title id="t-{naam}">{e(titel)}</title><desc id="d-{naam}">{e(beschrijving)}</desc>'
            + vlak(1, 1, B - 2, H - 2, DONKER, RAND, r=16) + "".join(delen) + "</svg>")


def gebouw(x: float, y: float, b: float, h: float, kleur: str = BLAUW, ramen: int = 3) -> str:
    d = [vlak(x, y, b, h, kleur, LICHT, 3)]
    for i in range(ramen):
        rx = x + (i + 1) * b / (ramen + 1) - 7
        d.append(vlak(rx, y + 12, 14, 12, LICHT, r=2))
    return "".join(d)


# ---------------------------------------------------------------- beelden deel 1 en 2

def beeld_wetketen() -> str:
    treden = [("NIS2", "Europese richtlijn"), ("Cyberbeveiligingswet", "sinds 15 augustus 2026"),
              ("Regeling sector overheid", "wijst de norm aan"), ("BIO2 en ISO 27001", "de maatregelen")]
    d = []
    for i, (kop, sub) in enumerate(treden):
        x, y = 40 + i * 100, 34 + i * 76
        kleur = ORANJE if i == 3 else BLAUW
        d += [vlak(x, y, 290, 60, kleur, LICHT, 8), tekst(x + 16, y + 26, kop, 18, True, "#ffffff", "start"),
              tekst(x + 16, y + 49, sub, 15, False, "#ffffff" if i == 3 else LICHT, "start")]
        if i < 3:
            d += [lijn(x + 50, y + 60, x + 50, y + 106), pijl(x + 50, y + 106, x + 98, y + 106)]
    # het gemeentehuis rechtsonder: daar landt het
    d += [f'<polygon points="650,348 710,318 770,348" fill="{BLAUW}" stroke="{LICHT}" stroke-width="2"/>',
          gebouw(660, 348, 100, 52), pijl(632, 292, 688, 322),
          tekst(710, 428, "jullie gemeente", 16, True, "#ffffff")]
    return svg("Van Europese richtlijn tot jullie organisatie",
               "Een trap van vier treden: NIS2, de Cyberbeveiligingswet, de regeling sector overheid en de BIO2 "
               "met ISO 27001. Onderaan staat het gemeentehuis.", d, "wetketen")


def beeld_tijdlijn() -> str:
    def x(jaar: float) -> float:
        return 40 + (jaar - 2026) * 230

    wet, college = x(2026 + 7.5 / 12), x(2028 + 7.5 / 12)
    d = [tekst(wet, 100, "15 augustus 2026", 16, True, "#ffffff"),
         tekst(college, 100, "15 augustus 2028", 16, True, ORANJE),
         lijn(wet, 110, wet, 226, LICHT, 2, streep=True), lijn(college, 110, college, 226, ORANJE, 3, streep=True),
         vlak(wet, 124, college - wet, 44, ORANJE, r=6),
         tekst((wet + college) / 2, 152, "het college: tijd voor de training", 17, True, "#ffffff"),
         lijn(30, 230, 770, 230, LICHT, 2),
         vlak(wet, 268, 770 - wet, 46, VEILIG, r=6),
         tekst((wet + 770) / 2, 297, "zorgplicht en meldplicht: elke dag", 17, True, DONKER),
         tekst(wet, 378, "registratie bijhouden: elke wijziging binnen twee weken", 16, False, LICHT, "start")]
    for jaar in (2027, 2028, 2029):
        d += [lijn(x(jaar), 224, x(jaar), 236, LICHT, 2), tekst(x(jaar), 256, str(jaar), 16)]
    # een kleine lus voor het bijhouden
    d.append(f'<path d="M{wet - 30:g} 372 a10 10 0 1 1 6 8" fill="none" stroke="{LICHT}" stroke-width="2"/>')
    return svg("De klok loopt al",
               "Een tijdlijn van 2026 tot 2029. Zorgplicht en meldplicht gelden vanaf 15 augustus 2026 elke dag. "
               "Het college heeft tot 15 augustus 2028 voor de training.", d, "tijdlijn")


def beeld_mijnncsc() -> str:
    paars = "#3c1a5b"
    d = [vlak(30, 22, 740, 406, VLAK, r=10),
         vlak(30, 22, 740, 44, "#ffffff", r=10), vlak(30, 54, 740, 12, "#ffffff"),
         # huisje en naam van het portaal
         f'<polygon points="56,46 66,37 76,46" fill="{BLAUW}"/>', vlak(59, 46, 14, 10, BLAUW),
         tekst(86, 51, "MijnNCSC", 17, True, BLAUW, "start"),
         tekst(184, 51, "Mijn producten en diensten", 15, False, INKT, "start"),
         f'<circle cx="456" cy="44" r="7" fill="#c62828"/>',
         label(546, 50, "geregistreerd", 13, True, ORANJE, "#ffffff"),
         tekst(756, 51, "[naam], [organisatie]", 14, False, INKT, "end"),
         tekst(52, 96, "Goedemiddag,", 20, True, paars, "start"),
         vlak(46, 108, 708, 34, "#fbf1c4", r=4),
         tekst(62, 131, "Direct hulp nodig bij een incident? Bel het NCSC: 070 751 5555", 15, False, INKT, "start")]
    kaarten = [("Cyberbeeld", "Je eigen netwerk in beeld", "Cyberbeeld bekijken", None),
               ("Direct naar", "Vragen en meer over de Cbw", "Ik heb een vraag", None),
               ("Flash-reports", "Actuele incidenten ontleed", "Overzicht", "waarschuwen"),
               ("Meldingen", "Incidenten melden en bijhouden", None, "melden"),
               ("Beveiligingsadviezen", "Wat te doen bij een nieuw lek", "Alle adviezen", None),
               ("Data-analyse", "Malware laten onderzoeken", "Mijn analyses", None)]
    for i, (kop, regel, link, pil) in enumerate(kaarten):
        kx, ky = 46 + (i % 3) * 239, 154 + (i // 3) * 134
        d += [vlak(kx, ky, 228, 122, "#ffffff", LICHT, 6), tekst(kx + 14, ky + 30, kop, 17, True, BLAUW, "start"),
              tekst(kx + 14, ky + 56, regel, 13, False, INKT, "start")]
        if link:
            d.append(tekst(kx + 14, ky + 100, "› " + link, 14, False, BLAUW, "start"))
        else:
            d += [vlak(kx + 14, ky + 80, 128, 28, ORANJE, r=3), tekst(kx + 78, ky + 99, "Melding maken", 14, True, "#ffffff")]
        if pil:
            d.append(label(kx + 228 - 10 - (len(pil) * 13 * 0.68 + 20) / 2, ky + 100, pil, 13, True, ORANJE, "#ffffff"))
            d.append(f'<rect x="{kx}" y="{ky}" width="228" height="122" rx="6" fill="none" stroke="{ORANJE}" '
                     f'stroke-width="3"/>')
    return svg("Het portaal MijnNCSC, nagebouwd",
               "Een nagebouwde startpagina van het NCSC-portaal met zes tegels. Gemarkeerd: de geregistreerde "
               "organisatie, de tegel Meldingen met de knop Melding maken, en de Flash-reports.", d, "mijnncsc")


def beeld_meldklok() -> str:
    d = [f'<circle cx="80" cy="112" r="40" fill="none" stroke="{LICHT}" stroke-width="4"/>',
         vlak(72, 62, 16, 10, LICHT, r=2), lijn(80, 112, 80, 84, ORANJE, 4), lijn(80, 112, 100, 122, LICHT, 4),
         tekst(140, 108, "de klok loopt vanaf het moment dat je het weet", 19, True, "#ffffff", "start"),
         tekst(140, 134, "niet vanaf het moment dat je het zeker weet", 16, False, LICHT, "start"),
         lijn(40, 304, 770, 304, LICHT, 3)]
    stappen = [(92, "ontdekt", "significant?", "T = 0"), (262, "waarschuwen", "vroegtijdig", "24 uur"),
               (432, "melden", "eerste beoordeling", "72 uur"), (668, "eindverslag", "oorzaak en herstel", "1 maand")]
    for i, (cx, kop, sub, tijd) in enumerate(stappen):
        kleur = ORANJE if i == 0 else BLAUW
        d += [vlak(cx - 80, 196, 160, 74, kleur, LICHT, 8), tekst(cx, 228, kop, 19, True, "#ffffff"),
              tekst(cx, 254, sub, 15, False, "#ffffff"), lijn(cx, 270, cx, 304, LICHT, 2),
              f'<circle cx="{cx:g}" cy="304" r="7" fill="{ORANJE if i == 0 else LICHT}"/>',
              tekst(cx, 336, tijd, 18, True, "#ffffff")]
    d += [gevaar(160, 160, 34),
          tekst(400, 404, "Melden bij het CSIRT en de toezichthouder, via één portaal", 17, False, LICHT)]
    return svg("Melden is een klok",
               "Een tijdlijn met vier stappen: ontdekt (is het significant?), binnen 24 uur waarschuwen, binnen 72 "
               "uur melden en binnen een maand het eindverslag.", d, "meldklok")


def beeld_refrein() -> str:
    d = [gevaar(150, 64, 120)]
    # persoon met pen: wie koos
    d += [persoon(400, 62, LICHT), vlak(434, 120, 46, 8, ORANJE, r=3, extra=' transform="rotate(-35 457 124)"')]
    # document met regels: waar staat het
    d += [vlak(612, 58, 84, 110, VLAK, r=4)] + [vlak(626, 78 + i * 18, 56 - (i % 2) * 14, 7, LICHT, r=2) for i in range(4)]
    d += [f'<path d="M628 150 l10 10 l22 -24" fill="none" stroke="{ORANJE}" stroke-width="5"/>']
    d += [pijl(222, 120, 330, 120), pijl(478, 120, 590, 120)]
    for cx, kop, sub in ((150, "Welk risico?", "wat kan er misgaan"), (400, "Wie koos?", "met naam en datum"),
                         (654, "Waar staat het?", "terug te vinden")):
        d += [tekst(cx, 222, kop, 26, True, "#ffffff"), tekst(cx, 250, sub, 16, False, LICHT)]
    d.append(tekst(400, 306, "bij elk risico: werkt het, klopt het, blijft het binnen?", 17, False, LICHT))
    for i, (letter, woord) in enumerate(BIV.items()):
        cx = 150 + i * 252
        d += [vlak(cx - 112, 330, 224, 56, BLAUW, LICHT, 28), f'<circle cx="{cx - 82:g}" cy="358" r="20" fill="{ORANJE}"/>',
              tekst(cx - 82, 366, letter, 20, True, "#ffffff"), tekst(cx - 54, 364, woord, 17, False, "#ffffff", "start")]
    return svg("Welk risico? Wie koos? Waar staat het?",
               "Drie stappen: een waarschuwingsdriehoek (welk risico), een persoon met een pen (wie koos) en een "
               "document met een vinkje (waar staat het). Daaronder beschikbaarheid, integriteit en vertrouwelijkheid.",
               d, "refrein")


# ---------------------------------------------------------------- beelden van de tien vereisten

def beeld_luchtfoto() -> str:
    d = [vlak(40, 34, 190, 70, GROEN, r=10)]
    # wegen en het water als vlakken, zodat een label erop geen lijn raakt
    d += [vlak(20, 118, 760, 18, WEG), vlak(292, 20, 18, 410, WEG), vlak(548, 20, 18, 410, WEG),
          f'<polygon points="20,312 780,232 780,276 20,356" fill="{VEILIG}" opacity=".85"/>']
    blokken = [(250, 40, 30, 60), (330, 40, 90, 60), (440, 40, 90, 60), (40, 160, 110, 50), (40, 222, 110, 40),
               (590, 160, 70, 46), (690, 160, 70, 40), (330, 290, 80, 50), (590, 330, 170, 70), (330, 380, 190, 44)]
    d += [vlak(x, y, b, h, BLAUW, RAND, 3) for x, y, b, h in blokken]
    # de plekken waar het pijn doet
    d += [gebouw(352, 190, 120, 70, BLAUW, 4), f'<rect x="466" y="160" width="3" height="32" fill="{LICHT}"/>',
          f'<polygon points="469,160 490,166 469,172" fill="{ORANJE}"/>', label(412, 172, "gemeentehuis"),
          gebouw(176, 190, 92, 58, BLAUW, 3), label(222, 172, "stembureau"),
          gebouw(630, 222, 64, 44, BLAUW, 2), vlak(694, 236, 24, 10, LICHT), label(662, 212, "gemaal"),
          gebouw(70, 380, 80, 44, BLAUW, 2), label(110, 370, "wijkteam"),
          vlak(600, 34, 160, 66, DONKER, LICHT, 6, ' stroke-dasharray="6 5"'),
          tekst(680, 64, "leverancier", 17, True, "#ffffff"), tekst(680, 88, "buiten de gemeente", 13, False, LICHT)]
    d += [gevaar(500, 196, 38), gevaar(276, 190, 34), gevaar(736, 196, 34), gevaar(180, 388, 34), gevaar(770 - 26, 106, 30)]
    return svg("Luchtfoto van een gemeente met waarschuwingen",
               "Een gemeente van bovenaf: wegen, water, een park en gebouwen. Waarschuwingsdriehoeken staan bij het "
               "gemeentehuis, het stembureau, het gemaal, het wijkteam en een leverancier buiten de gemeente.",
               d, "luchtfoto")


def beeld_kcc() -> str:
    d = [vlak(40, 34, 250, 40, VLAK, r=20), tekst(165, 60, "Mijn aanvraag is weg?", 16, False, DONKER),
         vlak(60, 86, 230, 40, VLAK, r=20), tekst(175, 112, "De site doet raar.", 16, False, DONKER),
         persoon(110, 176, LICHT), f'<path d="M86 194 a24 24 0 0 1 48 0" fill="none" stroke="{ORANJE}" stroke-width="5"/>',
         vlak(40, 276, 300, 16, LICHT, r=3), vlak(170, 170, 160, 100, VLAK, LICHT, 6),
         tekst(250, 212, "storing", 18, True, ORANJE), tekst(250, 240, "webformulier", 15, False, DONKER),
         gevaar(328, 150, 36)]
    for i, naam in enumerate(("servicedesk", "webbeheer", "leverancier")):
        y = 110 + i * 92
        d += [vlak(520, y, 230, 54, BLAUW, LICHT, 8), tekst(635, y + 34, naam, 18, True, "#ffffff"),
              lijn(348, 226, 512, y + 27, LICHT, 2, streep=True)]
    d.append(tekst(400, 418, "drie loketten, geen eigenaar", 18, True, LICHT))
    return svg("Het klantcontactcentrum hoort het als eerste",
               "Een medewerker met headset krijgt telefoontjes van inwoners over een storing in het webformulier. "
               "Stippellijnen lopen naar drie loketten: servicedesk, webbeheer en leverancier.", d, "kcc")


def beeld_gemaal() -> str:
    d = [f'<circle cx="560" cy="86" r="34" fill="{LICHT}"/>', f'<circle cx="610" cy="74" r="42" fill="{LICHT}"/>',
         f'<circle cx="660" cy="90" r="30" fill="{LICHT}"/>', vlak(530, 86, 160, 34, LICHT, r=16)]
    for i in range(6):
        x = 548 + i * 24
        d.append(lijn(x, 134, x - 8, 154, VEILIG, 3))
    d += [tekst(610, 196, "het blijft regenen", 17, True, "#ffffff"),
          f'<polygon points="290,170 390,120 490,170" fill="{BLAUW}" stroke="{LICHT}" stroke-width="2"/>',
          vlak(300, 170, 180, 150, BLAUW, LICHT, 3), tekst(390, 216, "gemaal", 22, True, "#ffffff"),
          tekst(390, 250, "pomp staat stil", 17, False, "#ffffff"), vlak(372, 268, 36, 52, DONKER, LICHT, 2),
          vlak(480, 286, 90, 14, LICHT), vlak(556, 286, 14, 52, LICHT),
          f'<circle cx="526" cy="252" r="24" fill="{ORANJE}" stroke="{DONKER}" stroke-width="2"/>',
          vlak(512, 247, 28, 10, "#ffffff", r=2),
          f'<path d="M20 352 q20 -12 40 0{" t40 0" * 18} L780 430 L20 430 z" fill="{VEILIG}" opacity=".9"/>',
          tekst(120, 400, "water stijgt", 18, True, DONKER), gevaar(318, 128, 40)]
    return svg("Een gemaal dat stilvalt terwijl het regent",
               "Een gemaal met een pomp die stilstaat. Rechtsboven regent het, onderaan stijgt het water.", d, "gemaal")


def beeld_leverancier() -> str:
    d = [vlak(60, 70, 150, 160, VLAK, r=8), vlak(60, 70, 150, 40, ORANJE, r=8), vlak(60, 98, 150, 12, ORANJE),
         tekst(135, 97, "betaaldag", 17, True, "#ffffff"), tekst(135, 196, "1", 70, True, DONKER),
         tekst(135, 262, "de eerste van de maand", 15, False, LICHT)]
    for i, (cx, cy) in enumerate(((100, 320), (135, 334), (170, 320))):
        d += [f'<circle cx="{cx}" cy="{cy}" r="22" fill="{ORANJE if i == 1 else VEILIG}" stroke="{DONKER}" stroke-width="2"/>',
              tekst(cx, cy + 7, "€", 20, True, DONKER)]
    d.append(tekst(135, 392, "uitkeringen", 17, True, "#ffffff"))
    for i in range(4):
        x = 250 + i * 64
        kleur = ORANJE if i == 3 else LICHT
        verschuif = ' transform="rotate(18 {0} 160)"'.format(x + 34) if i == 3 else ""
        d.append(f'<rect x="{x}" y="146" width="68" height="28" rx="14" fill="none" stroke="{kleur}" '
                 f'stroke-width="6"{verschuif}/>')
    d += [tekst(378, 214, "de keten", 16, False, LICHT),
          vlak(560, 70, 170, 230, BLAUW, LICHT, 6)]
    for i in range(5):
        y = 90 + i * 40
        d += [vlak(578, y, 134, 26, DONKER, r=3), f'<circle cx="{596}" cy="{y + 13}" r="5" fill="{ORANJE if i == 2 else VEILIG}"/>']
    d += [tekst(645, 336, "leverancier", 19, True, "#ffffff"), tekst(645, 362, "uitkeringssysteem", 15, False, LICHT),
          gevaar(740, 40, 40)]
    return svg("De leverancier van het uitkeringssysteem ligt eruit",
               "Een kalender met de eerste van de maand en munten voor de uitkeringen, een keten van schakels waarvan "
               "de laatste breekt, en het serverrek van de leverancier.", d, "leverancier")


def beeld_formulier() -> str:
    d = [vlak(50, 40, 470, 370, VLAK, r=8), vlak(50, 40, 470, 34, LICHT, r=8), vlak(50, 62, 470, 12, LICHT)]
    d += [f'<circle cx="{70 + i * 18}" cy="57" r="5" fill="{BLAUW}"/>' for i in range(3)]
    d += [tekst(80, 116, "Online aanvraag", 21, True, DONKER, "start")]
    for i, veld in enumerate(("Naam", "Burgerservicenummer", "Bijlage")):
        y = 150 + i * 70
        d += [tekst(80, y, veld, 15, False, INKT, "start"), vlak(80, y + 10, 320, 30, "#ffffff", LICHT, 3)]
    d += [vlak(80, 360, 130, 34, BLAUW, r=4), tekst(145, 383, "Verzenden", 15, True, "#ffffff"),
          vlak(560, 100, 200, 84, ORANJE, r=8), tekst(660, 136, "kritiek lek", 20, True, "#ffffff"),
          tekst(660, 164, "update beschikbaar", 15, False, "#ffffff"), pijl(556, 142, 524, 142, ORANJE),
          gevaar(560, 38, 40),
          vlak(608, 222, 104, 130, VLAK, r=4)]
    d += [vlak(622, 244 + i * 20, 76 - (i % 2) * 20, 7, LICHT, r=2) for i in range(4)]
    d += [tekst(660, 384, "het bestek", 17, True, "#ffffff"), tekst(660, 408, "eisen erin gezet?", 15, False, LICHT)]
    return svg("Een lek in de software achter de online formulieren",
               "Een online aanvraagformulier met naam, burgerservicenummer en bijlage. Rechts een melding over een "
               "kritiek lek met een update, en het bestek waarin de eisen hadden moeten staan.", d, "formulier")


def beeld_verkiezing() -> str:
    d = [tekst(400, 64, "getest vóór de verkiezingsdag?", 21, True, "#ffffff"),
         vlak(140, 110, 40, 66, VLAK, r=2), lijn(148, 128, 172, 152, ORANJE, 4), lijn(172, 128, 148, 152, ORANJE, 4),
         vlak(80, 196, 160, 130, BLAUW, LICHT, 4), vlak(130, 190, 60, 10, DONKER, LICHT, 2),
         tekst(160, 364, "stembus", 19, True, "#ffffff"), pijl(256, 260, 336, 260),
         vlak(350, 140, 140, 190, VLAK, r=4)]
    for i in range(6):
        y = 160 + i * 26
        d += [vlak(364, y, 70, 12, LICHT, r=2), vlak(446, y, 30, 12, BLAUW, r=2)]
    d += [tekst(420, 364, "telling", 19, True, "#ffffff"), pijl(504, 260, 584, 260)]
    for i, h in enumerate((60, 110, 84, 150)):
        x = 600 + i * 38
        d.append(vlak(x, 330 - h, 28, h, ORANJE if i == 3 else VEILIG, r=2))
    d += [lijn(592, 330, 760, 330, LICHT, 2), tekst(675, 364, "uitslag", 19, True, "#ffffff"),
          tekst(728, 164, "?", 30, True, ORANJE), gevaar(700, 92, 36)]
    return svg("Klopt de uitslag?",
               "Een stembus, een telling en een staafdiagram met de uitslag waarvan een staaf afwijkt. Bovenaan de vraag "
               "of het vóór de verkiezingsdag getest is.", d, "verkiezing")


def beeld_keukentafel() -> str:
    d = [persoon(200, 186, LICHT), persoon(600, 186, VEILIG),
         vlak(110, 280, 580, 18, LICHT, r=4), vlak(150, 298, 14, 110, LICHT), vlak(636, 298, 14, 110, LICHT),
         vlak(330, 196, 140, 84, BLAUW, LICHT, 4), vlak(318, 276, 164, 8, LICHT, r=2),
         vlak(520, 250, 26, 30, VLAK, r=4),
         vlak(380, 40, 330, 104, VLAK, r=10), tekst(545, 76, "Uw account verloopt vandaag", 17, True, DONKER),
         vlak(490, 92, 110, 32, ORANJE, r=4), tekst(545, 114, "Klik hier", 15, True, "#ffffff"),
         lijn(440, 146, 410, 192, ORANJE, 3, streep=True), gevaar(750, 64, 40),
         tekst(400, 436, "aan de keukentafel, met een laptop vol zorggegevens", 17, False, LICHT)]
    return svg("Een nepmail aan de keukentafel",
               "Een consulent en een inwoner aan de keukentafel. Op de laptop verschijnt een nepmail: uw account "
               "verloopt vandaag, klik hier.", d, "keukentafel")


def beeld_envelop() -> str:
    d = [vlak(356, 70, 88, 64, BLAUW, LICHT, 4), vlak(356, 60, 40, 14, BLAUW, LICHT, 3),
         tekst(400, 166, "jeugddossier", 18, True, "#ffffff"),
         pijl(380, 180, 300, 226), pijl(420, 180, 500, 226)]
    # dicht en versleuteld
    d += [vlak(100, 230, 200, 130, VLAK, r=6),
          f'<polyline points="100,230 200,300 300,230" fill="none" stroke="{BLAUW}" stroke-width="3"/>',
          f'<path d="M186 214 v-12 a14 14 0 0 1 28 0 v12" fill="none" stroke="{VEILIG}" stroke-width="5"/>',
          vlak(178, 212, 44, 34, VEILIG, r=5), tekst(200, 398, "versleuteld", 19, True, "#ffffff")]
    # open, papieren eruit
    d += [vlak(500, 260, 200, 100, VLAK, r=6),
          f'<polygon points="500,260 600,200 700,260" fill="{LICHT}" stroke="{BLAUW}" stroke-width="2"/>']
    for x, y, hoek in ((520, 214, -18), (590, 196, 6), (650, 214, 20)):
        d.append(vlak(x, y, 46, 58, "#ffffff", LICHT, 2, f' transform="rotate({hoek} {x + 23} {y + 29})"'))
    d += [tekst(600, 398, "onversleuteld", 19, True, ORANJE), gevaar(730, 186, 40)]
    return svg("Een jeugddossier, versleuteld of niet",
               "Een jeugddossier gaat in twee enveloppen de deur uit: links dicht met een slot, rechts open met de "
               "papieren eruit.", d, "envelop")


def beeld_balie() -> str:
    d = [persoon(190, 150, LICHT), vlak(250, 140, 150, 96, VLAK, LICHT, 4),
         tekst(325, 184, "basisregistratie", 15, True, DONKER), tekst(325, 208, "personen", 15, True, DONKER),
         vlak(488, 156, 54, 80, DONKER, LICHT, 4), f'<circle cx="515" cy="176" r="7" fill="{VEILIG}"/>',
         vlak(498, 196, 34, 24, LICHT, r=3), tekst(515, 128, "pas", 15, False, LICHT),
         persoon(660, 150, LICHT, streep=True),
         tekst(660, 84, "oud-collega", 17, True, "#ffffff"), tekst(660, 108, "account nog actief", 15, True, ORANJE),
         gevaar(744, 34, 38),
         vlak(50, 252, 700, 26, LICHT, r=4), vlak(70, 278, 660, 140, BLAUW, LICHT, 4),
         tekst(400, 354, "balie burgerzaken", 22, True, "#ffffff")]
    return svg("De balie van burgerzaken",
               "Een medewerker achter de balie met toegang tot de basisregistratie personen en een pasjeslezer. "
               "Rechts het silhouet van een oud-collega wiens account nog actief is.", d, "balie")


def beeld_crisisruimte() -> str:
    d = [vlak(230, 36, 340, 110, "#081d33", LICHT, 6), tekst(400, 86, "alles ligt plat", 22, True, ORANJE),
         tekst(400, 116, "geen netwerk, geen mail", 15, False, LICHT),
         vlak(210, 196, 380, 150, BLAUW, LICHT, 60), tekst(400, 278, "crisisteam", 20, True, "#ffffff")]
    for x, y in ((250, 222), (530, 222), (250, 290), (530, 290)):
        d.append(vlak(x, y, 22, 36, VLAK, r=4))
    d += [vlak(612, 180, 160, 40, VEILIG, r=18), tekst(692, 206, "wie belt wie?", 16, True, DONKER),
          vlak(612, 232, 160, 40, VEILIG, r=18), tekst(692, 258, "via mijn privé-app", 15, False, DONKER),
          gevaar(140, 70, 44),
          vlak(56, 252, 92, 120, VLAK, LICHT, 10), tekst(102, 312, "123 456", 17, True, DONKER),
          tekst(102, 404, "tweede factor", 16, True, "#ffffff")]
    return svg("De crisisruimte als alles plat ligt",
               "Een crisisteam rond de tafel, het scherm aan de muur meldt dat alles plat ligt. Berichten over wie wie "
               "belt via een privé-app, en links een telefoon met een inlogcode als tweede factor.", d, "crisisruimte")


BEELDEN = {"wetketen": beeld_wetketen, "tijdlijn": beeld_tijdlijn, "mijnncsc": beeld_mijnncsc,
           "meldklok": beeld_meldklok, "refrein": beeld_refrein, "luchtfoto": beeld_luchtfoto, "kcc": beeld_kcc,
           "gemaal": beeld_gemaal, "leverancier": beeld_leverancier, "formulier": beeld_formulier,
           "verkiezing": beeld_verkiezing, "keukentafel": beeld_keukentafel, "envelop": beeld_envelop,
           "balie": beeld_balie, "crisisruimte": beeld_crisisruimte}


# ---------------------------------------------------------------- invullen

def laad_invul(pad: Path | None) -> dict:
    if pad is None:
        return {}
    data = json.loads(pad.read_text(encoding="utf-8"))
    data["_map"] = pad.parent
    return data


def vul(s: str, invul: dict, refrein: str, als_html: bool = True) -> str:
    """Vervangt {veld} door de waarde uit het invulblok, of door een zichtbaar invulveld."""
    def vervang(m: re.Match) -> str:
        naam = m.group(1)
        if naam == "refrein":
            return e(refrein) if als_html else refrein
        waarde = str(invul.get(naam, "") or "").strip()
        if waarde:
            return e(waarde) if als_html else waarde
        return f'<span class="invul">[{naam}]</span>' if als_html else f"[{naam}]"
    tekst_ = e(s) if als_html else s
    patroon = r"\{(" + "|".join(INVULVELDEN + ("refrein",)) + r")\}"
    return re.sub(patroon, vervang, tekst_)


def foto_html(soort: str, invul: dict) -> str:
    bijschrift = {"gemeentehuis": "Foto: jullie gemeentehuis", "proces": "Foto: een eigen kritiek proces"}[soort]
    pad = str((invul.get("fotos") or {}).get(soort, "") or "").strip()
    if pad:
        bestand = (invul["_map"] / pad).resolve()
        mime = mimetypes.guess_type(bestand.name)[0] or "image/jpeg"
        data = base64.b64encode(bestand.read_bytes()).decode("ascii")
        return f'<figure class="foto"><img src="data:{mime};base64,{data}" alt="{e(bijschrift[6:])}"></figure>'
    return f'<figure class="foto leeg"><span class="invul">[{e(bijschrift)}]</span></figure>'


def stip(status: str) -> str:
    status = status if status in STATUS else "onbekend"
    return f'<span class="stip {status}" title="{e(STATUS[status])}"></span>'


def stand_html(soort: str, invul: dict, data: dict) -> str:
    stand = invul.get("stand") or {}

    def regel(waarde: dict | None, kop: str) -> str:
        waarde = waarde or {}
        status = waarde.get("status", "onbekend")
        uitleg = str(waarde.get("tekst", "") or "").strip()
        uitleg_html = e(uitleg) if uitleg else '<span class="invul">[toelichting]</span>'
        return (f'<li class="standregel">{stip(status)}<span class="standkop">{e(kop)}</span>'
                f'<span class="standtekst">{uitleg_html}</span></li>')

    if soort == "plichten":
        p = stand.get("plichten") or {}
        rijen = [("registratie", "Geregistreerd bij het NCSC, gegevens actueel"),
                 ("contactpersonen", "Contactpersonen weten dat zij het zijn"),
                 ("meldroute", "Melden: wie beslist of het significant is, ook 's nachts"),
                 ("college", "Het college weet wanneer het wordt gebeld")]
        return '<ul class="stand">' + "".join(regel(p.get(k), kop) for k, kop in rijen) + "</ul>"
    if soort == "zorgplicht":
        z = stand.get("zorgplicht") or {}
        eisen = [p for p in data["platen"] if p["soort"] == "eis"]
        return ('<ul class="stand tien">' + "".join(regel(z.get(p["letter"]), f'{p["letter"]}. {p["kop"]}')
                                                   for p in eisen) + "</ul>")
    if soort == "processen":
        p = stand.get("processen") or {}
        rijen = [("lijst", "Lijst met kritieke processen vastgesteld"),
                 ("eigenaren", "Per proces een eigenaar uit de lijn"),
                 ("hersteltijden", "Per proces een hersteltijd, gekozen en vastgelegd"),
                 ("afstemming", "Afgestemd met samenwerkingspartners")]
        return '<ul class="stand">' + "".join(regel(p.get(k), kop) for k, kop in rijen) + "</ul>"
    raise ValueError(soort)


# ---------------------------------------------------------------- de platen

CSS = """
:root{--inkt:#14202b;--blauw:#154273;--donker:#0d2b4d;--oranje:#e17000;--vlak:#f4f6f9;--licht:#c9d6e4;
--veilig:#6fa8dc;--sans:system-ui,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif}
[hidden]{display:none!important}
*{box-sizing:border-box}
html{scroll-snap-type:y mandatory;scroll-behavior:smooth;background:var(--donker)}
body{margin:0;font:18px/1.5 var(--sans);color:#fff;background:var(--donker)}
.balk{position:fixed;top:0;left:0;right:0;z-index:2;display:flex;gap:.75rem;align-items:center;
padding:.55rem 16px;background:rgba(13,43,77,.92);color:var(--licht);font-size:14px}
.balk a{color:#fff;text-decoration:none;font-weight:600}.balk a:hover{text-decoration:underline}
.balk .deel{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.teller{font-variant-numeric:tabular-nums}
.plaat{min-height:100vh;min-height:100svh;scroll-snap-align:start;display:flex;flex-direction:column;
justify-content:center;padding:4.5rem 16px 4rem;max-width:76rem;margin:0 auto;position:relative}
.oog{color:var(--oranje);font-weight:700;letter-spacing:.06em;text-transform:uppercase;font-size:.85rem;margin:0 0 .6rem}
.plaat h1{font-size:clamp(2rem,5vw,3.4rem);line-height:1.1;letter-spacing:-.02em;margin:0 0 1rem}
.plaat h1::after{content:'';display:block;width:3.5rem;height:4px;border-radius:2px;background:var(--oranje);margin-top:1rem}
.plaat h2{font-size:clamp(1.7rem,4.2vw,3rem);line-height:1.15;letter-spacing:-.02em;margin:0 0 1rem;max-width:26ch;
overflow-wrap:break-word}
.plaat.p-slot h2{color:var(--oranje);max-width:none}
.plaat p{max-width:42rem}
.sub{color:var(--licht);font-size:1.15rem}
.hulp{color:var(--licht);font-size:.95rem;margin-top:2rem}
kbd{border:1px solid var(--licht);border-radius:4px;padding:0 .35em;font:inherit;font-size:.9em}
.invul{color:var(--oranje);border:2px dashed var(--oranje);border-radius:6px;padding:0 .3em;font-weight:600}
.titelraster{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:2.5rem;align-items:center}
.foto{margin:0;border-radius:16px;overflow:hidden;aspect-ratio:4/3;display:flex;align-items:center;justify-content:center}
.foto img{width:100%;height:100%;object-fit:cover;display:block}
.foto.leeg{border:2px dashed var(--oranje);background:rgba(255,255,255,.03);padding:1rem;text-align:center}
.foto.leeg .invul{border:0}
.onthul-knop{align-self:flex-start;font:inherit;font-size:1rem;font-weight:600;color:var(--donker);
background:var(--oranje);border:0;border-radius:999px;padding:.55rem 1.2rem;cursor:pointer;margin-top:.6rem}
.onthul-knop:focus-visible,.nav button:focus-visible,.tegel-knop:focus-visible{outline:3px solid #fff;outline-offset:3px}
.onthul{list-style:none;padding:0;margin:1rem 0 0;max-width:46rem}
.onthul li{border-left:4px solid var(--oranje);padding:.3rem 0 .3rem 1rem;margin:.5rem 0;font-size:1.1rem}
.raster{display:grid;grid-template-columns:minmax(0,1.45fr) minmax(0,1fr);gap:2.2rem;align-items:center}
.beeld-svg svg{width:100%;height:auto;display:block;border-radius:16px}
.tegels{display:grid;grid-template-columns:repeat(auto-fit,minmax(14rem,1fr));gap:1rem;margin:.6rem 0 .4rem}
.tegel{border:1px solid var(--licht);border-radius:12px;padding:1rem 1.1rem;background:rgba(255,255,255,.03)}
.tegel h3{margin:0 0 .35rem;font-size:1.25rem;color:#fff}
.tegel p{margin:0;color:var(--licht)}
.tegel.nadruk{border:2px solid var(--oranje)}.tegel.nadruk h3{color:var(--oranje)}
.tien{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:.8rem;margin:.6rem 0}
.tegel-knop{font:inherit;text-align:left;color:#fff;cursor:pointer;border:1px solid var(--licht);border-radius:12px;
padding:.8rem .9rem;background:rgba(255,255,255,.03);display:flex;flex-direction:column;gap:.25rem;min-height:7.5rem}
.tegel-knop:hover{border-color:var(--oranje)}
.tegel-knop .letter{color:var(--oranje);font-weight:800;font-size:1.6rem;line-height:1}
.tegel-knop .naam{font-weight:700;line-height:1.25}
.tegel-knop .waar{color:var(--licht);font-size:.85rem;line-height:1.3}
.eiskop{color:var(--licht);font-size:.9rem;margin:0 0 .3rem}
.eiskop b{color:var(--oranje)}
.biv{display:flex;gap:.4rem;flex-wrap:wrap;margin:0 0 .8rem}
.biv span{border:1px solid var(--licht);border-radius:999px;padding:.1rem .7rem;font-size:.85rem;color:var(--licht)}
.biv span.aan{background:var(--oranje);border-color:var(--oranje);color:var(--donker);font-weight:700}
.drie{margin:0;display:grid;grid-template-columns:auto 1fr;gap:.35rem .9rem;font-size:1.05rem;max-width:40rem}
.drie dt{color:var(--oranje);font-weight:700;white-space:nowrap}
.drie dd{margin:0}
.wettekst{color:var(--licht);font-size:.95rem;font-style:italic;margin:.2rem 0 0}
.refrein{margin:1.6rem 0 0;color:var(--oranje);font-weight:700;font-size:1.05rem;letter-spacing:.01em}
.bron{margin:.5rem 0 0;color:var(--licht);font-size:.8rem}
.stand{list-style:none;padding:0;margin:.6rem 0;display:grid;gap:.6rem;max-width:56rem}
.stand.tien{grid-template-columns:repeat(2,minmax(0,1fr));gap:.5rem 1.4rem}
.standregel{display:grid;grid-template-columns:auto 1fr;gap:.1rem .7rem;align-items:baseline;
border-bottom:1px solid rgba(201,214,228,.25);padding:.35rem 0}
.standkop{font-weight:700}
.standtekst{grid-column:2;color:var(--licht);font-size:.95rem}
.stip{width:1rem;height:1rem;border-radius:50%;display:inline-block;align-self:center;border:2px solid var(--licht)}
.stip.groen{background:#3fa66b;border-color:#3fa66b}.stip.oranje{background:var(--oranje);border-color:var(--oranje)}
.stip.rood{background:#d64545;border-color:#d64545}.stip.onbekend{background:transparent;border-style:dashed}
.legenda{color:var(--licht);font-size:.85rem;display:flex;gap:1rem;flex-wrap:wrap;margin:.4rem 0 0}
.legenda span{display:inline-flex;gap:.35rem;align-items:center}
.nav{position:fixed;right:16px;bottom:16px;z-index:2;display:flex;gap:.5rem}
.nav button{font:inherit;font-size:1.1rem;width:2.6rem;height:2.6rem;border-radius:50%;border:1px solid var(--licht);
background:var(--donker);color:#fff;cursor:pointer}
@media (max-width:900px){
html{scroll-snap-type:y proximity}
.raster,.titelraster{grid-template-columns:1fr;gap:1.2rem}
.tien{grid-template-columns:repeat(2,minmax(0,1fr))}
.stand.tien{grid-template-columns:1fr}
.plaat{padding-bottom:5rem}
}
@media print{
@page{size:A4 landscape;margin:12mm}
html,body{background:#fff;color:var(--inkt)}
.balk,.nav,.onthul-knop,.hulp{display:none!important}
.onthul[hidden]{display:block!important}
.plaat{min-height:0;height:auto;padding:0;page-break-after:always;break-after:page}
.plaat h2,.plaat h1,.tegel h3,.tegel-knop{color:var(--donker)}
.sub,.bron,.tegel p,.standtekst,.wettekst{color:#4b5563}
}
"""

JS = """
(function(){
var platen=[].slice.call(document.querySelectorAll('.plaat'));
var teller=document.querySelector('.teller'),deel=document.querySelector('.balk .deel');
var huidig=0;
function zet(i){huidig=i;teller.textContent=(i+1)+' / '+platen.length;deel.textContent=platen[i].getAttribute('data-deel')||'';}
function ga(i){if(i<0||i>=platen.length)return;platen[i].scrollIntoView({behavior:'smooth',block:'start'});zet(i);}
function onthul(p,toon){var lijst=p.querySelector('.onthul'),knop=p.querySelector('.onthul-knop');
if(!lijst)return false;var open=toon===undefined?lijst.hidden:toon;lijst.hidden=!open;
knop.setAttribute('aria-expanded',open?'true':'false');knop.textContent=open?'Verberg':knop.getAttribute('data-label');return true;}
platen.forEach(function(p){var k=p.querySelector('.onthul-knop');if(k)k.addEventListener('click',function(){onthul(p);});});
[].forEach.call(document.querySelectorAll('[data-ga]'),function(k){k.addEventListener('click',function(){
var doel=document.getElementById(k.getAttribute('data-ga'));if(doel)ga(platen.indexOf(doel));});});
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


def onthul_html(plaat: dict, nr: int, knoplabel: str = "Onthul") -> str:
    if not plaat.get("onthul"):
        return ""
    oid = f"o{nr}"
    lijst = "".join(f"<li>{e(r)}</li>" for r in plaat["onthul"])
    return (f'<button type="button" class="onthul-knop" aria-expanded="false" aria-controls="{oid}" '
            f'data-label="{e(knoplabel)}">{e(knoplabel)}</button><ul class="onthul" id="{oid}" hidden>{lijst}</ul>')


def plaat_html(nr: int, totaal: int, plaat: dict, data: dict, invul: dict) -> str:
    soort = plaat["soort"]
    refrein = data["refrein"]
    deelnaam = next(d["naam"] for d in data["delen"] if d["nr"] == plaat["deel"])
    v = lambda s: vul(s, invul, refrein)  # noqa: E731
    kop = v(plaat["kop"])
    sub = f'<p class="sub">{v(plaat["tekst"])}</p>' if plaat.get("tekst") else ""
    bron = f'<p class="bron">Bron: {e(plaat["bron"])}</p>' if plaat.get("bron") else ""
    oog = f'<p class="oog">Deel {plaat["deel"]} &middot; {e(deelnaam)}</p>'
    refreinregel = ""

    if soort == "titel":
        binnen = (f'<div class="titelraster"><div><p class="oog">MT-sessie &middot; {v("{datum}")}</p>'
                  f'<h1>{kop}</h1>{sub}'
                  f'<p class="hulp">Bladeren met <kbd>↓</kbd> en <kbd>↑</kbd>. Op een plaat met een knop onthult '
                  f'<kbd>↓</kbd> eerst de rest. <kbd>O</kbd> onthult of verbergt.</p></div>'
                  f'{foto_html(plaat["foto"], invul)}</div>')
    elif soort == "zin":
        binnen = oog + f"<h2>{kop}</h2>{sub}" + onthul_html(plaat, nr)
    elif soort == "tegels":
        tegels = "".join(f'<div class="tegel{" nadruk" if t.get("nadruk") else ""}"><h3>{e(t["kop"])}</h3>'
                         f'<p>{e(t["tekst"])}</p></div>' for t in plaat["tegels"])
        binnen = oog + f'<h2>{kop}</h2><div class="tegels">{tegels}</div>' + onthul_html(plaat, nr)
    elif soort == "beeld":
        binnen = (f'<div class="raster"><div class="beeld-svg">{BEELDEN[plaat["beeld"]]()}</div>'
                  f'<div class="tekst">{oog}<h2>{kop}</h2>{sub}{onthul_html(plaat, nr)}</div></div>')
    elif soort == "raster":
        eisen = [p for p in data["platen"] if p["soort"] == "eis"]
        knoppen = "".join(f'<button type="button" class="tegel-knop" data-ga="eis-{p["letter"]}">'
                          f'<span class="letter">{e(p["letter"])}</span><span class="naam">{e(p["kop"])}</span>'
                          f'<span class="waar">{e(p["proces"])}</span></button>' for p in eisen)
        binnen = oog + f'<h2>{kop}</h2>{sub}<div class="tien">{knoppen}</div>'
        refreinregel = f'<p class="refrein">{e(refrein)}</p>'
    elif soort == "eis":
        chips = "".join(f'<span class="{"aan" if k in plaat["biv"] else ""}">{k} &middot; {BIV[k]}</span>'
                        for k in BIV)
        drie = (f'<dl class="drie"><dt>Wat als</dt><dd>{e(plaat["watals"])}</dd>'
                f'<dt>De keuze</dt><dd>{e(plaat["keuze"])}</dd>'
                f'<dt>Waar gepast</dt><dd>{e(plaat["gepast"])}</dd></dl>')
        wet = dict(plaat, onthul=[f'De wet: {plaat["wet"]}'] + plaat.get("onthul", []))
        binnen = (f'<div class="raster"><div class="beeld-svg">{BEELDEN[plaat["beeld"]]()}</div>'
                  f'<div class="tekst"><p class="eiskop">Zorgplicht <b>{e(plaat["letter"])}</b> van a tot j '
                  f'&middot; {e(plaat["proces"])}</p><h2>{kop}</h2><div class="biv">{chips}</div>{drie}'
                  f'{onthul_html(wet, nr, "Wat de wet vraagt")}</div></div>')
        refreinregel = f'<p class="refrein">{e(refrein)}</p>'
    elif soort == "stand":
        legenda = "".join(f"<span>{stip(k)}{e(t)}</span>" for k, t in STATUS.items())
        lijst = stand_html(plaat["stand"], invul, data)
        if plaat.get("foto"):
            lijst = (f'<div class="titelraster"><div>{lijst}</div>{foto_html(plaat["foto"], invul)}</div>')
        binnen = oog + f'<h2>{kop}</h2>{lijst}<p class="legenda">{legenda}</p>'
    elif soort == "vraag":
        binnen = oog + f"<h2>{kop}</h2>{sub}" + onthul_html(plaat, nr)
        refreinregel = f'<p class="refrein">{e(refrein)}</p>'
    elif soort == "slot":
        binnen = f"<h2>{kop}</h2>{sub}"
    else:
        raise ValueError(f"onbekende soort plaat: {soort}")
    anker = f'eis-{plaat["letter"]}' if soort == "eis" else f"plaat-{nr}"
    return (f'<section class="plaat p-{soort}" id="{anker}" data-deel="Deel {plaat["deel"]}: {e(deelnaam)}" '
            f'aria-label="Plaat {nr} van {totaal}">{binnen}{refreinregel}{bron}</section>\n')


def deck_html(data: dict, invul: dict) -> str:
    platen = data["platen"]
    totaal = len(platen)
    body = "".join(plaat_html(i + 1, totaal, p, data, invul) for i, p in enumerate(platen))
    gemeente = str(invul.get("gemeente", "") or "").strip()
    titel = data["titel"] + (f" - {gemeente}" if gemeente else "")
    terug = "./" if not invul else LIVE
    herkomst = ("Gegenereerd door tools/bouw_cbw_mt.py uit data/platen.json; niet met de hand wijzigen."
                if not invul else "Gegenereerd door tools/bouw_cbw_mt.py met een eigen invulblok.")
    return (
        "<!doctype html>\n<html lang=\"nl\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
        f"<title>{e(titel)}</title>\n"
        "<meta name=\"description\" content=\"Platen voor een sessie met het managementteam over de "
        "Cyberbeveiligingswet: de wet, de plichten en de tien vereisten van de zorgplicht.\">\n"
        f"<!-- {herkomst} -->\n"
        f"<style>{CSS.strip()}</style>\n</head>\n<body>\n"
        f'<header class="balk"><a href="{terug}">De Cbw uitgelegd aan het MT</a>'
        f'<span class="deel"></span><span class="teller" aria-live="polite">1 / {totaal}</span>'
        "</header>\n<main>\n" + body + "</main>\n"
        '<nav class="nav" aria-label="Bladeren"><button type="button" class="vorige" aria-label="Vorige plaat">↑</button>'
        '<button type="button" class="volgende" aria-label="Volgende plaat">↓</button></nav>\n'
        f"<script>{JS.strip()}</script>\n</body>\n</html>\n")


def kale_tekst(s: str, data: dict) -> str:
    return vul(s, {}, data["refrein"], als_html=False)


def draaiboek_md(data: dict) -> str:
    totaal = sum(p.get("minuten", 0) for p in data["platen"])
    regels = [
        "# Draaiboek: de Cyberbeveiligingswet uitgelegd aan het MT",
        "",
        "Gegenereerd uit [data/platen.json](data/platen.json) door `tools/bouw_cbw_mt.py`; wijzig de notities daar.",
        "Terug naar [het item](README.md) of naar [de platen](platen.html).",
        "",
        f"Een sessie van {totaal} minuten met het managementteam of directieteam. Tekst tussen haken, zoals "
        "[gemeente], vult de eigen organisatie in. De drie platen in deel 4 zijn helemaal eigen invulling.",
        "",
        f"**Het refrein.** Bij elk vereiste van de zorgplicht dezelfde drie vragen: *{data['refrein']}* Ze komen "
        "terug tot vervelens toe, en dat is de bedoeling: na afloop stelt het MT ze zelf.",
        "",
    ]
    for deel in data["delen"]:
        platen = [(i + 1, p) for i, p in enumerate(data["platen"]) if p["deel"] == deel["nr"]]
        minuten = sum(p.get("minuten", 0) for _, p in platen)
        regels += [f"## Deel {deel['nr']}: {deel['naam']} ({minuten} minuten)", "",
                   "| Plaat | Kop | Min. | Wat je doet |", "|---|---|---|---|"]
        for nr, p in platen:
            kop = kale_tekst(p["kop"], data)
            if p["soort"] == "eis":
                kop = f"{p['letter']}. {kop}"
            notitie = p.get("notitie", "").replace("|", "/")
            regels.append(f"| {nr} | {kop} | {p.get('minuten', 0)} | {notitie} |")
        regels.append("")
    regels += ["## Antwoordlijnen", ""]
    for vraag, antwoord in data.get("antwoordlijnen", []):
        regels += [f"**{vraag}**", antwoord, ""]
    return "\n".join(regels).rstrip() + "\n"


def doelen(invul_pad: Path | None = None, uit: Path | None = None) -> dict[Path, str]:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    if invul_pad is not None:
        return {uit: deck_html(data, laad_invul(invul_pad))}
    uitvoer: dict[Path, str] = {MAP / "platen.html": deck_html(data, {}), MAP / "draaiboek.md": draaiboek_md(data)}
    for p in data["platen"]:
        if p.get("beeld"):
            uitvoer[MAP / "img" / f"{p['beeld']}.svg"] = BEELDEN[p["beeld"]]() + "\n"
    return uitvoer


def main(argv: list[str]) -> int:
    check = "--check" in argv
    invul_pad = uit = None
    if "--invul" in argv:
        invul_pad = Path(argv[argv.index("--invul") + 1])
        if "--uit" not in argv:
            print("Geef met --uit aan waar de eigen versie heen moet.")
            return 2
        uit = Path(argv[argv.index("--uit") + 1])
    achter = []
    for pad, inhoud in doelen(invul_pad, uit).items():
        oud = pad.read_text(encoding="utf-8") if pad.exists() else None
        if oud == inhoud:
            continue
        if check:
            achter.append(pad.relative_to(ROOT).as_posix())
        else:
            pad.parent.mkdir(parents=True, exist_ok=True)
            pad.write_text(inhoud, encoding="utf-8", newline="\n")
            print("geschreven:", pad.as_posix())
    if achter:
        print("Loopt achter op data/platen.json; draai python tools/bouw_cbw_mt.py:")
        for p in achter:
            print("  ", p)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
