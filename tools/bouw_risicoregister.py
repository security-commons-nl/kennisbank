"""Bouwt het voorbeeld bij "Risicogestuurd managementsysteem" uit de gegevens van het register.

Gebruik:
    python tools/bouw_risicoregister.py            # schrijft de markdown en de verkenner
    python tools/bouw_risicoregister.py --check    # exit 1 als een van beide achterloopt op de gegevens
    python tools/bouw_risicoregister.py pad/naar/register.json uitmap/   # een eigen register

Invoer is een register in JSON (zie `voorbeeld-register.json`): strategische risico's (SR), operationele
risico's (OR), maatregelen, controls en bevindingen. Uitvoer:

- `voorbeeld-register.md`: alle tabellen, met de afgeleide waarden. De kennisbank maakt er zelf een
  leesversie van (`tools/build.py`), dus niet met de hand bewerken.
- `voorbeeld-register-verkenner.html`: dezelfde uitkomst als pagina met tabbladen en een filter op
  kader. De pagina rekent niet: ze toont wat dit script heeft berekend, zodat er maar één rekenregel is.

De regels staan in `model.md` naast het voorbeeld. Kort:

1. Een bevinding noemt maatregelen. Het primaire OR is het OR van de eerste maatregel, de overige
   maatregelen geven de secundaire OR's, het SR volgt uit het primaire OR. Niemand typt een OR of SR bij
   een bevinding, behalve als uitzondering met motivering.
2. Alleen bevindingen met status open of in behandeling tellen mee.
3. Niveau per maatregel: 0 niet in orde of onbekend, 1 opzet, 2 bestaan, 3 werking. Eerst uit de stand
   in de bron; heeft de maatregel getoetste controls, dan de zwakste control; werking vervalt als de toets
   ouder is dan de frequentie; een meetellende bevinding zet het niveau op hooguit 2.
4. Prioriteit: eerst maatregelen onder een OR met een meetellende bevinding, op score van dat OR en
   dan van het SR; daarna de rest op score van het SR (buiten de SRA telt als nul); bij gelijke stand het
   laagste niveau eerst.

Het script weigert een register dat niet klopt en zegt waarom. Het bedenkt geen bevindingen.
"""
from __future__ import annotations

import datetime as dt
import html
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import huisstijl  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ITEM = ROOT / "governance" / "risicogestuurd-managementsysteem"
INVOER = ITEM / "voorbeeld-register.json"

STATUSSEN = ("kandidaat", "open", "in behandeling", "geaccepteerd", "gesloten")
MEETELLEND = ("open", "in behandeling")
BRONSOORTEN = ("toets", "incident", "meting", "test", "analyse")
NIVEAUS = ("0 · niet in orde", "1 · opzet", "2 · bestaan", "3 · werking")
VERLOOPT_NA_DAGEN = 365  # een bevinding zonder herbevestiging na twaalf maanden wordt gemeld


class RegisterFout(Exception):
    """Het register klopt niet; de tekst zegt wat en waar."""


# ---------------------------------------------------------------------------------------------
# Toetsen
# ---------------------------------------------------------------------------------------------

def datum(waarde: object, waar: str) -> dt.date:
    try:
        return dt.date.fromisoformat(str(waarde))
    except ValueError:
        raise RegisterFout(f"{waar}: '{waarde}' is geen datum (JJJJ-MM-DD)") from None


def toets(reg: dict) -> list[str]:
    """Controleer het register. Gooit RegisterFout bij de eerste harde fout."""
    fouten: list[str] = []
    for veld in ("peildatum", "sr", "or", "maatregelen", "bevindingen", "kaders", "klassen"):
        if veld not in reg:
            fouten.append(f"register: veld '{veld}' ontbreekt")
    if fouten:
        raise RegisterFout("; ".join(fouten))
    datum(reg["peildatum"], "register.peildatum")

    def uniek(lijst: list[dict], sleutel: str, soort: str) -> set[str]:
        gezien: set[str] = set()
        for x in lijst:
            code = x.get(sleutel)
            if not code:
                fouten.append(f"{soort}: een regel zonder {sleutel}")
            elif code in gezien:
                fouten.append(f"{soort} {code}: dubbele code")
            gezien.add(code)
        return gezien

    srs = uniek(reg["sr"], "code", "SR")
    ors = uniek(reg["or"], "code", "OR")
    sleutels = uniek(reg["maatregelen"], "sleutel", "maatregel")
    uniek(reg.get("controls", []), "code", "control")
    uniek(reg["bevindingen"], "code", "bevinding")

    for s in reg["sr"]:
        for v in ("kans", "impact"):
            if not isinstance(s.get(v), int) or not 1 <= s[v] <= 5:
                fouten.append(f"SR {s.get('code')}: {v} moet een geheel getal van 1 tot en met 5 zijn")
    for o in reg["or"]:
        if o.get("kader") not in reg["kaders"]:
            fouten.append(f"OR {o['code']}: kader '{o.get('kader')}' onbekend")
        if o.get("sr") is not None and o["sr"] not in srs:
            fouten.append(f"OR {o['code']}: SR '{o['sr']}' bestaat niet")
    for m in reg["maatregelen"]:
        kader = str(m.get("sleutel", "")).split(":")[0]
        if kader not in reg["kaders"]:
            fouten.append(f"maatregel {m.get('sleutel')}: sleutel begint niet met een kader ({', '.join(reg['kaders'])})")
        if m.get("or") not in ors:
            fouten.append(f"maatregel {m.get('sleutel')}: OR '{m.get('or')}' bestaat niet")
        else:
            or_kader = next(o["kader"] for o in reg["or"] if o["code"] == m["or"])
            if or_kader != kader:
                fouten.append(f"maatregel {m['sleutel']}: hangt onder {m['or']} uit kader {or_kader}; "
                              "een maatregel hangt onder een OR uit de standaardlijst van zijn eigen kader")
    for c in reg.get("controls", []):
        for s in c.get("maatregelen", []):
            if s not in sleutels:
                fouten.append(f"control {c['code']}: maatregel '{s}' bestaat niet")
        t = c.get("toets")
        if t:
            datum(t.get("datum"), f"control {c['code']}.toets.datum")
            if not isinstance(c.get("frequentie_dagen"), int):
                fouten.append(f"control {c['code']}: frequentie_dagen ontbreekt; zonder frequentie vervalt werking nooit")
    for b in reg["bevindingen"]:
        code = b.get("code")
        for v in ("titel", "aangetoond", "bron"):
            if not str(b.get(v) or "").strip():
                fouten.append(f"bevinding {code}: '{v}' ontbreekt")
        if b.get("bronsoort") not in BRONSOORTEN:
            fouten.append(f"bevinding {code}: bronsoort '{b.get('bronsoort')}' is niet een van {', '.join(BRONSOORTEN)}")
        if not b.get("peildatum"):
            fouten.append(f"bevinding {code}: peildatum ontbreekt")
        else:
            datum(b["peildatum"], f"bevinding {code}.peildatum")
        if b.get("status") not in STATUSSEN:
            fouten.append(f"bevinding {code}: status '{b.get('status')}' is niet een van {', '.join(STATUSSEN)}")
        for v in ("kans", "impact"):
            if not isinstance(b.get(v), int) or not 1 <= b[v] <= 5:
                fouten.append(f"bevinding {code}: {v} moet een geheel getal van 1 tot en met 5 zijn")
        maatr = b.get("maatregelen") or []
        uitz = b.get("uitzondering")
        if not maatr and not uitz:
            fouten.append(f"bevinding {code}: noemt geen maatregel en geen uitzondering met motivering")
        if uitz and (uitz.get("or") not in ors or not str(uitz.get("motivering") or "").strip()):
            fouten.append(f"bevinding {code}: uitzondering vraagt een bestaand OR en een motivering")
        for m in maatr:
            if m.get("sleutel") not in sleutels:
                fouten.append(f"bevinding {code}: maatregel '{m.get('sleutel')}' bestaat niet in het register")
            if not str(m.get("reden") or "").strip():
                fouten.append(f"bevinding {code}: maatregel '{m.get('sleutel')}' zonder reden")
        if b.get("status") == "geaccepteerd" and not str(b.get("acceptatie") or "").strip():
            fouten.append(f"bevinding {code}: geaccepteerd zonder besluit van de risico-eigenaar")
    if fouten:
        raise RegisterFout("\n".join(fouten))

    meldingen = []
    peil = datum(reg["peildatum"], "peildatum")
    met_or = {o.get("sr") for o in reg["or"]}
    for s in reg["sr"]:
        if s["code"] not in met_or:
            meldingen.append(f"{s['code']}: geen operationeel risico eronder; dit strategische risico is niet onderbouwd")
    for b in reg["bevindingen"]:
        if b["status"] in MEETELLEND and (peil - datum(b["peildatum"], "")).days > VERLOOPT_NA_DAGEN:
            meldingen.append(f"{b['code']}: feit is ouder dan twaalf maanden; herbevestigen of sluiten")
        if b.get("uitzondering"):
            meldingen.append(f"{b['code']}: hangt direct onder {b['uitzondering']['or']} (uitzondering); "
                             "wijst op een gat in de standaardlijst of de maatregelset")
    return meldingen


# ---------------------------------------------------------------------------------------------
# Afleiden en rekenen
# ---------------------------------------------------------------------------------------------

def klasse(score: int, klassen: list[dict]) -> str:
    naam = klassen[0]["naam"]
    for k in sorted(klassen, key=lambda k: k["vanaf"]):
        if score >= k["vanaf"]:
            naam = k["naam"]
    return naam


def niveau_uit_bron(m: dict) -> int:
    """Het niveau dat de bron zelf opgeeft, per kader."""
    kader = m["sleutel"].split(":")[0]
    stand = m.get("stand")
    if kader == "AVG" and isinstance(stand, dict):
        if stand.get("werking") == "groen" and stand.get("bestaan") == "groen" and stand.get("opzet") == "groen":
            return 3
        if stand.get("bestaan") == "groen" and stand.get("opzet") == "groen":
            return 2
        if stand.get("opzet") == "groen":
            return 1
        return 0
    if kader == "BCM":
        return {"voltooid": 2, "deels": 1}.get(str(stand), 0)
    if kader == "BIO2":
        return 2 if stand == "geïmplementeerd" else 0
    return 0


def control_niveau(c: dict, peil: dt.date) -> tuple[int, str]:
    """Niveau van een control uit zijn laatste toets, en een korte reden."""
    t = c.get("toets")
    if not t:
        return 0, "niet getoetst"
    n = 0
    for i, aspect in enumerate(("opzet", "bestaan", "werking"), 1):
        if t.get(aspect) is True:
            n = i
        else:
            break
    reden = f"toets {datum(t['datum'], '').strftime('%d-%m-%Y')}"
    if n == 3 and (peil - datum(t["datum"], "")).days > c["frequentie_dagen"]:
        return 2, reden + ", werking verlopen (cyclus gemist)"
    return n, reden


def reken(reg: dict) -> dict:
    """Leid alles af wat het register niet zelf vastlegt."""
    peil = datum(reg["peildatum"], "peildatum")
    klassen = reg["klassen"]
    sr = {s["code"]: {**s, "score": s["kans"] * s["impact"]} for s in reg["sr"]}
    for s in sr.values():
        s["klasse"] = klasse(s["score"], klassen)
    ors = {o["code"]: {**o} for o in reg["or"]}
    mt = {m["sleutel"]: {**m} for m in reg["maatregelen"]}

    # Bevindingen: OR en SR uit de maatregel.
    bev = []
    for b in reg["bevindingen"]:
        b = {**b, "score": b["kans"] * b["impact"]}
        b["klasse"] = klasse(b["score"], klassen)
        if b.get("maatregelen"):
            or_lijst = [mt[m["sleutel"]]["or"] for m in b["maatregelen"]]
            b["or_primair"] = or_lijst[0]
            b["or_secundair"] = sorted(set(or_lijst[1:]) - {or_lijst[0]})
        else:
            b["or_primair"] = b["uitzondering"]["or"]
            b["or_secundair"] = []
        b["sr"] = ors[b["or_primair"]]["sr"]
        b["telt"] = b["status"] in MEETELLEND
        bev.append(b)

    # OR-score: hoogste score van de meetellende bevindingen waarvan dit OR het primaire is.
    for o in ors.values():
        scores = [b["score"] for b in bev if b["telt"] and b["or_primair"] == o["code"]]
        o["score"] = max(scores) if scores else None
        o["klasse"] = klasse(o["score"], klassen) if scores else None
        o["sr_score"] = sr[o["sr"]]["score"] if o["sr"] else 0
        o["bevindingen"] = [b["code"] for b in bev if b["or_primair"] == o["code"]]
        o["beoordeeld"] = bool(scores)

    # Niveau per maatregel.
    controls = reg.get("controls", [])
    for m in mt.values():
        n = niveau_uit_bron(m)
        herkomst = "stand in de bron"
        getoetst = [(c["code"], *control_niveau(c, peil)) for c in controls
                    if m["sleutel"] in c["maatregelen"] and c.get("toets")]
        if getoetst:
            code, n, reden = min(getoetst, key=lambda x: x[1])
            herkomst = f"{'zwakste control' if len(getoetst) > 1 else 'control'} {code} ({reden})"
        m["bevindingen"] = [b["code"] for b in bev if b["telt"]
                            and any(x["sleutel"] == m["sleutel"] for x in b.get("maatregelen", []))]
        if m["bevindingen"] and n > 2:
            n = 2
            herkomst += f"; werking weerlegd door {', '.join(m['bevindingen'])}"
        m["niveau"] = n
        m["niveau_herkomst"] = herkomst
        m["controls"] = [c["code"] for c in controls if m["sleutel"] in c["maatregelen"]]

    # Prioriteit.
    rij = []
    for m in mt.values():
        o = ors[m["or"]]
        groep = 1 if o["beoordeeld"] else 2
        sleutel = (groep, -(o["score"] or 0), -o["sr_score"], m["niveau"], m["sleutel"])
        if groep == 1:
            waarom = f"{o['code']} heeft een aangetoond gat (score {o['score']})"
        elif o["sr"]:
            waarom = f"{o['code']} niet beoordeeld; gewicht van {o['sr']} (score {o['sr_score']})"
        else:
            waarom = f"{o['code']} niet beoordeeld en buiten de SRA; laagste gewicht"
        rij.append((sleutel, {**m, "groep": groep, "waarom": waarom}))
    prioriteit = [r for _, r in sorted(rij, key=lambda x: x[0])]
    for i, r in enumerate(prioriteit, 1):
        r["plek"] = i

    cs = []
    for c in controls:
        n, reden = control_niveau(c, peil)
        cs.append({**c, "niveau": n, "niveau_reden": reden})

    return {"peildatum": reg["peildatum"], "organisatie": reg.get("organisatie", ""), "sr": sr, "or": ors,
            "maatregelen": mt, "bevindingen": bev, "controls": cs, "prioriteit": prioriteit,
            "kaders": reg["kaders"]}


# ---------------------------------------------------------------------------------------------
# Schrijven
# ---------------------------------------------------------------------------------------------

def nl_datum(s: str) -> str:
    return dt.date.fromisoformat(s).strftime("%d-%m-%Y")


def cel(x: object) -> str:
    return str(x).replace("|", "/").replace("\n", " ")


def tabel(koppen: list[str], rijen: list[list[object]]) -> str:
    regels = ["| " + " | ".join(koppen) + " |", "|" + "---|" * len(koppen)]
    regels += ["| " + " | ".join(cel(c) for c in r) + " |" for r in rijen]
    return "\n".join(regels) + "\n"


def markdown(u: dict, meldingen: list[str]) -> str:
    sr, ors, mt = u["sr"], u["or"], u["maatregelen"]
    telt = [b for b in u["bevindingen"] if b["telt"]]
    d = []
    d.append(f"# Voorbeeld: het register van {u['organisatie'].replace('Gemeente ', 'gemeente ')}\n")
    d.append("<!-- Gegenereerd door tools/bouw_risicoregister.py uit voorbeeld-register.json; niet met de hand bewerken. -->\n")
    d.append(f"Bijlage bij [GRC voor security, privacy en continuïteit](README.md). Gemeente Duinstad bestaat niet; alle "
             f"risico's, bevindingen en getallen zijn verzonnen. De sleutels van de maatregelen zijn echt. Peildatum "
             f"{nl_datum(u['peildatum'])}. De gegevens staan in [`voorbeeld-register.json`](voorbeeld-register.json), de "
             f"regels in [het model](model.md), en dezelfde uitkomst is door te klikken in "
             f"[de verkenner](voorbeeld-register-verkenner.html).\n")
    d.append(f"**Stand.** {len(sr)} strategische risico's, {len(ors)} operationele risico's, {len(mt)} maatregelen, "
             f"{len(u['controls'])} controls en {len(u['bevindingen'])} bevindingen, waarvan {len(telt)} meetellen. "
             f"{sum(1 for o in ors.values() if o['beoordeeld'])} van de {len(ors)} operationele risico's hebben een "
             f"aangetoond gat; de andere zijn niet beoordeeld.\n")

    d.append("## Prioriteit: wat eerst\n")
    d.append("De lijst die je aan de directie laat zien. Eerst de maatregelen onder een risico met een aangetoond gat, "
             "dan de rest op het gewicht van het strategische risico. Bij gelijke stand het laagste niveau eerst.\n")
    d.append(tabel(["#", "Maatregel", "Wat", "Risico", "Niveau", "Bevinding", "Waarom hier"],
                   [[r["plek"], r["sleutel"], r["titel"], r["or"], NIVEAUS[r["niveau"]],
                     ", ".join(r["bevindingen"]) or "", r["waarom"]] for r in u["prioriteit"]]))

    d.append("## Van strategisch risico naar maatregel\n")
    for s in list(sr.values()) + [None]:
        onder = [o for o in ors.values() if (o["sr"] == (s["code"] if s else None))]
        if not onder:
            continue
        if s:
            d.append(f"### {s['code']} · {s['titel']}\n")
            d.append(f"Kans {s['kans']} × impact {s['impact']} = {s['score']} ({s['klasse']}).\n")
        else:
            d.append("### Buiten de strategische risicoanalyse\n")
            d.append("Risico's uit de standaardlijst zonder passend strategisch risico. Dat is een bevinding over de "
                     "risicoanalyse zelf: ontbreekt er een strategisch risico, of hoort dit erbij?\n")
        for o in onder:
            stand = f"score {o['score']} ({o['klasse']})" if o["beoordeeld"] else "niet beoordeeld"
            d.append(f"- **{o['code']}** {o['titel']} · {u['kaders'][o['kader']]['naam']}, {o['standaard']} · {stand}")
            for m in [m for m in mt.values() if m["or"] == o["code"]]:
                extra = f" · {', '.join(m['bevindingen'])}" if m["bevindingen"] else ""
                d.append(f"  - {m['sleutel']} {m['titel']} · {NIVEAUS[m['niveau']]}{extra}")
        d.append("")

    d.append("## Bevindingen\n")
    d.append("Een bevinding is een aangetoond feit over een maatregel die niet werkt. Het risico volgt uit de "
             "maatregel: de eerste maatregel bepaalt het primaire risico. Alleen open en in behandeling tellen mee.\n")
    for b in u["bevindingen"]:
        sec = f"; secundair {', '.join(b['or_secundair'])}" if b["or_secundair"] else ""
        d.append(f"### {b['code']} · {b['titel']}\n")
        d.append(f"- **Aangetoond:** {b['aangetoond']}")
        d.append(f"- **Bronsoort en bron:** {b['bronsoort']}, {b['bron']} (peildatum {nl_datum(b['peildatum'])})")
        for m in b.get("maatregelen", []):
            d.append(f"- **Maatregel {m['sleutel']}:** {m['reden']}")
        d.append(f"- **Afgeleid:** {b['or_primair']}{sec}, {b['sr'] or 'buiten de SRA'}")
        d.append(f"- **Score:** kans {b['kans']} × impact {b['impact']} = {b['score']} ({b['klasse']})")
        status = f"{b['status']} sinds {nl_datum(b['statusdatum'])}" if b.get("statusdatum") else b["status"]
        d.append(f"- **Status:** {status}{'' if b['telt'] else ', telt niet mee'}")
        if b.get("acceptatie"):
            d.append(f"- **Besluit risico-eigenaar:** {b['acceptatie']}")
        d.append("")

    d.append("## Maatregelen\n")
    d.append(tabel(["Maatregel", "Wat", "Risico", "Stand in de bron", "Niveau", "Waar het niveau vandaan komt",
                    "Beheerseigenaar"],
                   [[m["sleutel"], m["titel"], m["or"], stand_tekst(m), NIVEAUS[m["niveau"]], m["niveau_herkomst"],
                     m.get("eigenaar", "")] for m in mt.values()]))

    d.append("## Controls\n")
    d.append("Een control is de toetsbare activiteit die laat zien dat een maatregel werkt. De zwakste getoetste "
             "control bepaalt het niveau van de maatregel. Werking vervalt als de volgende toets niet op tijd komt.\n")
    d.append(tabel(["Control", "Wat", "Toetst", "Frequentie", "Laatste toets", "Niveau", "Bewijs"],
                   [[c["code"], c["titel"], ", ".join(c["maatregelen"]), f"elke {c['frequentie_dagen']} dagen",
                     f"{nl_datum(c['toets']['datum'])}, {c['toets']['toetser']}" if c.get("toets") else "geen",
                     f"{NIVEAUS[c['niveau']]} ({c['niveau_reden']})", (c.get("toets") or {}).get("bewijs", "")]
                    for c in u["controls"]]))

    d.append("## Meldingen van de generator\n")
    d.append("\n".join(f"- {x}" for x in meldingen) + "\n" if meldingen else "Geen.\n")
    return "\n".join(d).rstrip() + "\n"


def stand_tekst(m: dict) -> str:
    s = m.get("stand")
    if isinstance(s, dict):
        return f"opzet {s.get('opzet')}, bestaan {s.get('bestaan')}, werking {s.get('werking')}"
    return str(s)


# ---- verkenner -------------------------------------------------------------------------------

CSS = """
:root{--tekst:#111;--zacht:#5a6675;--lijn:#c9d1dc;--vlak:#f3f6fa;--accent:#154273;--achter:#fff;
--n0:#fbe3e1;--n1:#fdf0d5;--n2:#e6effa;--n3:#e2f3e6;--rand-n0:#c0392b;--rand-n1:#b9770e;--rand-n2:#154273;--rand-n3:#1e7b3a}
@media (prefers-color-scheme:dark){:root{--tekst:#e8ecf1;--zacht:#a7b2bf;--lijn:#3a4654;--vlak:#1c2530;--accent:#8db8e8;
--achter:#11161c;--n0:#3d1f1c;--n1:#3a2f17;--n2:#18283a;--n3:#17301f;--rand-n0:#e57367;--rand-n1:#e0a64a;--rand-n2:#8db8e8;--rand-n3:#6cc68a}}
*{box-sizing:border-box}
body{font-family:Calibri,Arial,sans-serif;font-size:11pt;line-height:1.45;color:var(--tekst);background:var(--achter);
max-width:27cm;margin:1.5em auto;padding:0 16px}
h1{font-size:20pt;border-bottom:2px solid var(--accent);padding-bottom:.2em;color:var(--accent);margin:.4em 0 .3em}
h2{font-size:14pt;color:var(--accent);margin:1.2em 0 .4em}
p{margin:.5em 0}a{color:var(--accent)}
.kruimel{font-size:10pt;color:var(--zacht);margin-bottom:.6em}
.kruimel a{color:var(--zacht)}
.uitleg{color:var(--zacht);font-size:10.5pt}
.balk{display:flex;flex-wrap:wrap;gap:.4em;align-items:center;margin:1em 0 .6em}
.tab{border:1px solid var(--lijn);background:var(--vlak);color:var(--tekst);padding:.35em .8em;border-radius:4px;
font:inherit;cursor:pointer}
.tab[aria-selected=true]{background:var(--accent);color:var(--achter);border-color:var(--accent)}
.filter{margin-left:auto;display:flex;gap:.4em;align-items:center;font-size:10pt}
.filter select{font:inherit;padding:.2em .3em;background:var(--achter);color:var(--tekst);border:1px solid var(--lijn)}
[hidden]{display:none!important}
.rol{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:10pt;margin:.4em 0}
th,td{border:1px solid var(--lijn);padding:.35em .5em;vertical-align:top;text-align:left}
th{background:var(--vlak)}
.nw{white-space:nowrap}
.niveau{display:inline-block;padding:0 .4em;border-radius:3px;border-left:3px solid;white-space:nowrap}
.n0{background:var(--n0);border-color:var(--rand-n0)}.n1{background:var(--n1);border-color:var(--rand-n1)}
.n2{background:var(--n2);border-color:var(--rand-n2)}.n3{background:var(--n3);border-color:var(--rand-n3)}
.groep{font-size:9.5pt;color:var(--zacht)}
.boom ul{list-style:none;margin:.2em 0 .2em 1.1em;padding:0}
.boom>ul{margin-left:0}
.boom li{margin:.25em 0}
.sr{font-weight:bold;color:var(--accent);margin-top:.8em}
.or{font-weight:bold}
.zacht{color:var(--zacht)}
.kaart{border:1px solid var(--lijn);border-radius:4px;padding:.6em .8em;margin:.6em 0;background:var(--vlak)}
.kaart h3{margin:0 0 .3em;font-size:11.5pt}
.kaart dl{display:grid;grid-template-columns:max-content 1fr;gap:.15em .8em;margin:0;font-size:10pt}
.kaart dt{color:var(--zacht)}
.kaart dd{margin:0}
.voet{margin-top:2em;font-size:9.5pt;color:var(--zacht);border-top:1px solid var(--lijn);padding-top:.5em}
@media (max-width:640px){.filter{margin-left:0;width:100%}.kaart dl{grid-template-columns:1fr}.kaart dt{margin-top:.3em}}
@media print{body{max-width:none;margin:0}.balk{display:none}[data-paneel]{display:block!important}
[data-paneel]+[data-paneel]{page-break-before:always}@page{size:A4 landscape;margin:1.5cm}}
"""

JS = """
(function(){
  var tabs=[].slice.call(document.querySelectorAll('.tab'));
  var panelen=[].slice.call(document.querySelectorAll('[data-paneel]'));
  function toon(naam){
    tabs.forEach(function(t){t.setAttribute('aria-selected',t.dataset.tab===naam?'true':'false');});
    panelen.forEach(function(p){p.hidden=p.dataset.paneel!==naam;});
    try{history.replaceState(null,'','#'+naam);}catch(e){}
  }
  tabs.forEach(function(t){t.addEventListener('click',function(){toon(t.dataset.tab);});});
  var start=(location.hash||'').slice(1);
  toon(tabs.some(function(t){return t.dataset.tab===start;})?start:tabs[0].dataset.tab);
  var kies=document.getElementById('kader');
  kies.addEventListener('change',function(){
    var k=kies.value;
    [].slice.call(document.querySelectorAll('[data-kader]')).forEach(function(el){
      el.hidden=!(k==='alle'||el.dataset.kader.split(' ').indexOf(k)!==-1);
    });
  });
})();
"""


def e(x: object) -> str:
    return html.escape(str(x), quote=True)


def niveau_html(n: int) -> str:
    return f'<span class="niveau n{n}">{e(NIVEAUS[n])}</span>'


def verkenner(u: dict) -> str:
    sr, ors, mt = u["sr"], u["or"], u["maatregelen"]
    kader_van = {code: o["kader"] for code, o in ors.items()}
    titel = f"Verkenner: het register van {u['organisatie'].replace('Gemeente ', 'gemeente ')}"
    h = []
    h.append('<!doctype html><html lang="nl"><head><meta charset="utf-8">'
             '<meta name="viewport" content="width=device-width,initial-scale=1">'
             f'<title>{e(titel)}</title>'
             '<link rel="icon" href="https://security-commons-nl.github.io/favicon.svg" type="image/svg+xml">'
             f'<style>{CSS}</style></head><body>')
    h.append('<nav class="kruimel" aria-label="Kruimelpad"><a href="https://security-commons-nl.github.io/">Security '
             'Commons NL</a> › <a href="../../">Kennisbank</a> › <a href="../">Governance</a> › <a href="./">'
             'GRC voor security, privacy en continuïteit</a> › <span>Verkenner</span></nav>')
    h.append(f"<h1>{e(titel)}</h1>")
    h.append(f'<p class="uitleg">Gemeente Duinstad bestaat niet; alles hieronder is verzonnen, behalve de sleutels van '
             f'de maatregelen. Peildatum {e(nl_datum(u["peildatum"]))}. Deze pagina rekent niet zelf: ze toont wat '
             f'<code>tools/bouw_risicoregister.py</code> uit <a href="voorbeeld-register.json">de gegevens</a> heeft '
             f'afgeleid. Dezelfde uitkomst als tekst: <a href="voorbeeld-register.html">het voorbeeld</a>. De regels: '
             f'<a href="model.html">het model</a>.</p>')
    tabs = [("prioriteit", "Prioriteit"), ("boom", "Risico naar maatregel"), ("bevindingen", "Bevindingen"),
            ("maatregelen", "Maatregelen"), ("controls", "Controls")]
    h.append('<div class="balk" role="tablist">')
    for k, naam in tabs:
        h.append(f'<button class="tab" role="tab" data-tab="{k}" aria-selected="false">{e(naam)}</button>')
    h.append('<label class="filter">Kader <select id="kader"><option value="alle">alle</option>')
    for k, kd in u["kaders"].items():
        h.append(f'<option value="{e(k)}">{e(kd["naam"])}</option>')
    h.append("</select></label></div>")

    # Prioriteit
    h.append('<section data-paneel="prioriteit"><h2>Prioriteit: wat eerst</h2><p class="uitleg">Eerst de maatregelen '
             'onder een risico met een aangetoond gat, dan de rest op het gewicht van het strategische risico. Bij '
             'gelijke stand het laagste niveau eerst.</p><div class="rol"><table><thead><tr><th>#</th><th>Maatregel'
             '</th><th>Wat</th><th>Risico</th><th>Niveau</th><th>Bevinding</th><th>Waarom hier</th></tr></thead><tbody>')
    for r in u["prioriteit"]:
        h.append(f'<tr data-kader="{e(kader_van[r["or"]])}" data-sleutel="{e(r["sleutel"])}"><td>{r["plek"]}</td>'
                 f'<td class="nw">{e(r["sleutel"])}</td><td>{e(r["titel"])}</td><td class="nw">{e(r["or"])}</td><td>{niveau_html(r["niveau"])}'
                 f'</td><td>{e(", ".join(r["bevindingen"]))}</td><td class="groep">{e(r["waarom"])}</td></tr>')
    h.append("</tbody></table></div></section>")

    # Boom
    h.append('<section data-paneel="boom" class="boom"><h2>Van strategisch risico naar maatregel</h2><ul>')
    for s in list(sr.values()) + [None]:
        onder = [o for o in ors.values() if o["sr"] == (s["code"] if s else None)]
        if not onder:
            continue
        kaders = " ".join(sorted({o["kader"] for o in onder}))
        if s:
            kop = f'{e(s["code"])} · {e(s["titel"])} <span class="zacht">· score {s["score"]} ({e(s["klasse"])})</span>'
        else:
            kop = 'Buiten de strategische risicoanalyse <span class="zacht">· laagste gewicht</span>'
        h.append(f'<li data-kader="{e(kaders)}"><div class="sr">{kop}</div><ul>')
        for o in onder:
            stand = f'score {o["score"]} ({e(o["klasse"])})' if o["beoordeeld"] else "niet beoordeeld"
            bev = f' · {e(", ".join(o["bevindingen"]))}' if o["bevindingen"] else ""
            h.append(f'<li data-kader="{e(o["kader"])}"><span class="or">{e(o["code"])}</span> {e(o["titel"])} '
                     f'<span class="zacht">· {e(u["kaders"][o["kader"]]["naam"])} · {stand}{bev}</span><ul>')
            for m in [m for m in mt.values() if m["or"] == o["code"]]:
                b = f' <span class="zacht">· {e(", ".join(m["bevindingen"]))}</span>' if m["bevindingen"] else ""
                h.append(f'<li>{niveau_html(m["niveau"])} {e(m["sleutel"])} {e(m["titel"])}{b}</li>')
            h.append("</ul></li>")
        h.append("</ul></li>")
    h.append("</ul></section>")

    # Bevindingen
    h.append('<section data-paneel="bevindingen"><h2>Bevindingen</h2><p class="uitleg">Het risico volgt uit de '
             'maatregel: de eerste maatregel bepaalt het primaire risico. Alleen open en in behandeling tellen mee.</p>')
    for b in u["bevindingen"]:
        kaders = " ".join(sorted({kader_van[b["or_primair"]]} | {kader_van[x] for x in b["or_secundair"]}))
        sec = f'; secundair {", ".join(b["or_secundair"])}' if b["or_secundair"] else ""
        rijen = [("Aangetoond", e(b["aangetoond"])),
                 ("Bron", f'{e(b["bronsoort"])}, {e(b["bron"])} (peildatum {e(nl_datum(b["peildatum"]))})')]
        rijen += [(f'Maatregel {e(m["sleutel"])}', e(m["reden"])) for m in b.get("maatregelen", [])]
        rijen += [("Afgeleid", e(f'{b["or_primair"]}{sec}, {b["sr"] or "buiten de SRA"}')),
                  ("Score", e(f'kans {b["kans"]} × impact {b["impact"]} = {b["score"]} ({b["klasse"]})')),
                  ("Status", e(b["status"] + ("" if b["telt"] else ", telt niet mee")))]
        if b.get("acceptatie"):
            rijen.append(("Besluit", e(b["acceptatie"])))
        h.append(f'<article class="kaart" data-kader="{e(kaders)}"><h3>{e(b["code"])} · {e(b["titel"])}</h3><dl>'
                 + "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in rijen) + "</dl></article>")
    h.append("</section>")

    # Maatregelen
    h.append('<section data-paneel="maatregelen"><h2>Maatregelen</h2><div class="rol"><table><thead><tr><th>Maatregel'
             '</th><th>Wat</th><th>Risico</th><th>Stand in de bron</th><th>Niveau</th><th>Waar het niveau vandaan komt'
             '</th><th>Beheerseigenaar</th></tr></thead><tbody>')
    for m in mt.values():
        h.append(f'<tr data-kader="{e(kader_van[m["or"]])}"><td class="nw">{e(m["sleutel"])}</td><td>{e(m["titel"])}</td>'
                 f'<td class="nw">{e(m["or"])}</td><td>{e(stand_tekst(m))}</td><td>{niveau_html(m["niveau"])}</td>'
                 f'<td>{e(m["niveau_herkomst"])}</td><td>{e(m.get("eigenaar", ""))}</td></tr>')
    h.append("</tbody></table></div></section>")

    # Controls
    h.append('<section data-paneel="controls"><h2>Controls</h2><p class="uitleg">De zwakste getoetste control bepaalt '
             'het niveau van de maatregel. Werking vervalt als de volgende toets niet op tijd komt.</p><div class="rol">'
             '<table><thead><tr><th>Control</th><th>Wat</th><th>Toetst</th><th>Frequentie</th><th>Laatste toets</th>'
             '<th>Niveau</th><th>Bewijs</th></tr></thead><tbody>')
    for c in u["controls"]:
        kaders = " ".join(sorted({kader_van[mt[s]["or"]] for s in c["maatregelen"]}))
        t = c.get("toets") or {}
        h.append(f'<tr data-kader="{e(kaders)}"><td class="nw">{e(c["code"])}</td><td>{e(c["titel"])}</td>'
                 f'<td>{e(", ".join(c["maatregelen"]))}</td><td>elke {c["frequentie_dagen"]} dagen</td>'
                 f'<td>{e(nl_datum(t["datum"]) + ", " + t["toetser"]) if t else "geen"}</td>'
                 f'<td>{niveau_html(c["niveau"])} <span class="zacht">{e(c["niveau_reden"])}</span></td>'
                 f'<td>{e(t.get("bewijs", ""))}</td></tr>')
    h.append("</tbody></table></div></section>")

    h.append('<p class="voet">Gegenereerd door <code>tools/bouw_risicoregister.py</code> in de '
             '<a href="https://github.com/security-commons-nl/kennisbank">kennisbank</a> van Security Commons NL. '
             'EUPL-1.2.</p>')
    h.append(f"<script>{JS}</script></body></html>")
    return "\n".join(h) + "\n"


# ---------------------------------------------------------------------------------------------

def bouw(invoer: Path, uitmap: Path) -> dict[Path, str]:
    reg = json.loads(invoer.read_text(encoding="utf-8"))
    meldingen = toets(reg)
    u = reken(reg)
    return {uitmap / "voorbeeld-register.md": markdown(u, meldingen),
            # Huisstijl van de voorpagina op het scherm (tools/huisstijl.py); de eigen opbouw blijft staan.
            uitmap / "voorbeeld-register-verkenner.html": huisstijl.zet(verkenner(u), "instrument")}


def main(argv: list[str]) -> int:
    check = "--check" in argv
    pos = [a for a in argv if not a.startswith("--")]
    invoer = Path(pos[0]) if pos else INVOER
    uitmap = Path(pos[1]) if len(pos) > 1 else invoer.parent
    try:
        uit = bouw(invoer, uitmap)
    except RegisterFout as f:
        print(f"Register klopt niet:\n{f}")
        return 1
    achter = []
    for pad, inhoud in uit.items():
        oud = pad.read_text(encoding="utf-8") if pad.exists() else None
        if oud == inhoud:
            continue
        if check:
            achter.append(pad.name)
        else:
            pad.write_bytes(inhoud.encode("utf-8"))
            print(f"geschreven: {pad.name}")
    if achter:
        print(f"loopt achter op de gegevens: {', '.join(achter)}; draai python tools/bouw_risicoregister.py")
        return 1
    if check:
        print("risicoregister: voorbeeld en verkenner kloppen met de gegevens")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
