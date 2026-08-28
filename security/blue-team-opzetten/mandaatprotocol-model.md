---
titel: Mandaatprotocol blue team (model)
vakgebied: security
type: sjabloon
normen: [BIO2]
versie: 2026-08
herkomst: bijlage bij "Een blue team opzetten"; modelprotocol met voorbeeldclausules
status: sjabloon
samenvatting: Modelprotocol voor het mandaat van een tijdelijk interventieteam. Trigger, drie bevoegdheden zonder akkoord per geval, financiële drempels, drie escalatieniveaus, vier ogen en vastlegging. Door het eigen bestuur of de CIO vast te stellen vóór de eerste ingreep.
---

# Mandaatprotocol (model)

Bijlage bij [Een blue team opzetten](README.md), stap 4. Dit is een model met voorbeeldclausules, geen
vastgesteld protocol. Laat het door je eigen bestuur of CIO vaststellen vóór de eerste ingreep. Vul de
drempels tussen `[ ]` in met bedragen die bij jouw organisatie passen.

## 1. Trigger: de Rood-score

Een mandaat-actie wordt geactiveerd door een R/E/C-score **Rood** (R = ja, E = direct, C = niets).
Geldige bronnen voor een Rood-score:

- een spoedadvies van het nationale CSIRT of het sector-CERT;
- een bevestigde exploited-in-the-wild-melding op een component die in gebruik is;
- een kill-chain-run met driemaal ontbrekende dekking op een bereikbare cel;
- een signaal van mogelijke compromittering;
- een pentest met directe exploiteerbaarheid.

## 2. Bevoegdheden zonder akkoord per geval

*Modelclausule.* Het team mag, na een vier-ogen-besluit en met melding aan de beslisser:

1. kritieke beveiligingsupdates uitrollen buiten reguliere change-vensters, ook bij tijdelijke
   dienstimpact;
2. een dienst of systeem tijdelijk afschakelen bij een actieve dreiging; bij OT altijd samen met de
   proceseigenaar en met een veilige terugval;
3. externe partijen raadplegen zonder aparte opdracht.

Met vooraf vastgestelde technische toegang, read-only waar mogelijk, in zes categorieën: identity,
monitoring en logging, netwerk, kwetsbaarheden, endpoints, back-up.

## 3. Financieel mandaat

| Bedrag | Procedure |
|---|---|
| < `[lage grens]` | team beslist; maandelijkse verantwoording |
| `[lage grens]` tot `[plafond]` | beslisser vooraf akkoord |
| > `[plafond]` | formeel akkoord beslisser; opdrachtgever geïnformeerd |

## 4. Drie escalatieniveaus

**Niveau 1, kernteam beslist.** Bij Rood, geen merkbare impact bij ketenpartners, impact van ten hoogste
vier uur en budget onder de lage grens. Vier-ogen-vereiste. Melding: beslisser zo snel mogelijk; tweede
lijn cc binnen 24 uur; derde lijn via steekproef. Register binnen 24 uur.

**Niveau 2, beslisser of CIO beslist.** Bij impact langer dan vier uur, een ketenpartner merkbaar
geraakt, of budget boven de lage grens. Opdrachtgever binnen twee uur geïnformeerd.

**Niveau 3, calamiteitenteam.** De opdrachtgever activeert. Bij een bevestigde aanval, ernstige
verstoring, datalek met meldplicht, of brede of onduidelijke scope. Overdracht telefonisch; het kernteam
blijft beschikbaar onder die aansturing. Heeft de organisatie geen calamiteitenteam, dan geldt de
bestaande crisisroute, hoe die ook heet.

## 5. Vier ogen en vastlegging

- **Vier ogen:** minimaal twee kernteamleden zijn het eens dat R = ja, E = direct, C = niets.
- **Besluitenregister**, binnen 24 uur: datum · besluit · onderbouwing · hersteltijd · betrokkenen ·
  bewijslink.
- **Reguliere registratie:** change- of incidentregistratie in het gewone systeem, ook voor de
  mandaat-bypass.

## 6. Looptijd

Dit protocol geldt van `[startdatum]` tot `[einddatum venster]`. Uiterlijk `[datum, ruim vóór einde]`
besluit de opdrachtgever over afbouw, overdracht aan de lijn of verlenging.

## 7. Vaststelling

| Rol | Naam of functie | Datum | Paraaf |
|---|---|---|---|
| Opdrachtgever | `[ ]` | | |
| Beslisser en budgethouder | `[ ]` | | |
| Tweede lijn (risico-advies) | `[ ]` | | |
| Derde lijn (onafhankelijke toets) | `[ ]` | | |
