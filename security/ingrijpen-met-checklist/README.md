---
titel: Ingrijpen met een checklist, voordat je de knop omzet
vakgebied: security
type: aanpak
normen: [BIO2]
peildatum: 2026-10-20
herkomst: actie-checklist van het interventieteam van een gemeente, opgesteld met de concernadviseur risicomanagement, mei 2026
status: in gebruik
route: geen
samenvatting: Een vaste vragenlijst die een team langsloopt voordat het een beveiligingsmaatregel doorvoert die gebruikers raakt, als aanvulling op het gewone wijzigingsbeheer. Dreiging en impact, aanpak en mandaat, terugdraaien, communicatie en evaluatie, zodat de tweede en derde lijn zien dat de afwegingen zijn gemaakt zonder bij elk overleg te zitten. Met een leeg sjabloon, een ingevuld voorbeeld voor ClickFix en de registerinstelling om Windows + R uit te zetten.
barrieres: [execution]
rol: verdieping
pijler: meten-voordat-je-ingrijpt
---

# Ingrijpen met een checklist, voordat je de knop omzet

> **Lees de checklist online:** [security-commons-nl.github.io/kennisbank/security/ingrijpen-met-checklist](https://security-commons-nl.github.io/kennisbank/security/ingrijpen-met-checklist/)

Een team dat snel ingrijpt, heeft twee risico's: dat het te laat is, en dat het iets kapotmaakt. De
tweede wordt vaak vergeten. Een PowerShell-blokkade die de salarisrun stopt of een regel die de helft van
de werkplekken platlegt, is ook een incident, alleen dan zelf veroorzaakt.

Deze checklist komt uit een gemeente die een klein interventieteam inzette om hardening snel door te voeren.
Het team liep hem langs vóór elk moment waarop een maatregel live ging (T-0). Zo konden de
risicomanager (tweede lijn) en de auditor (derde lijn) zien dat de afwegingen gemaakt waren, zonder dat
ze bij elke vergadering hoefden te zitten.

## Wat er in deze map staat

- [actie-checklist-sjabloon.md](actie-checklist-sjabloon.md): het lege sjabloon, vijf blokken.
- [actie-checklist-voorbeeld-clickfix.md](actie-checklist-voorbeeld-clickfix.md): ingevuld voor ClickFix,
  de aanval waarbij een gebruiker zelf een commando plakt na een nep-CAPTCHA.
- [windows-r-uitschakelen.md](windows-r-uitschakelen.md): de registerinstelling die het
  Uitvoeren-venster uitschakelt, een van de maatregelen tegen ClickFix.

## BIO 2.0

De checklist helpt bewijs leveren voor **8.32** *Wijzigingsbeheer* (een ingreep met afweging, terugdraaiplan en
vastlegging) en, bij een actief incident, **5.26** *Reageren op informatiebeveiligingsincidenten*. De ClickFix-maatregelen
zelf horen bij **8.7** *Bescherming tegen malware* en **8.19** *Installeren van software op operationele systemen*.

## De vijf blokken

1. **Dreiging en impact.** Wat is de aanleiding, wordt het elders al misbruikt, welke processen lopen
   risico, en wat gebeurt er als het misgaat.
2. **Aanpak en mandaat.** Wat staat er al en waarom volstaat dat niet, wat doen we in welke volgorde, wie
   beslist, en loopt dit via de reguliere change of via een spoedbevoegdheid. Beide mag; onbewust mengen
   niet.
3. **Veiligheid van de actie zelf.** Wie draait terug, hoe snel, en is dat getest. Wie breed uitrolt
   zonder pilot, heeft alleen het terugdraaien als vangnet, en dat moet dan vóór T-0 echt gedraaid zijn,
   niet alleen op papier.
4. **Stakeholders en communicatie.** Wie is ingelicht, welke externen zijn geraakt, ligt de tekst voor
   gebruikers klaar en weet de servicedesk ervan.
5. **Vastlegging en evaluatie.** Wie schrijft het besluit op, wat leren we, en wanneer evalueren we.

## Hoe je hem gebruikt

Kopieer het sjabloon per actie en vul elk punt in. Geen antwoord is geen lege regel maar "nog open", met
een eigenaar en een datum. De verwijzingen naar het plan van aanpak, het communicatieplan en de
R/E/C-rubriek (terugdraaibaar, explosief, containment) zijn van het oorspronkelijke team; vervang ze door
je eigen stukken of laat ze weg.

Zie ook [Meten voordat je ingrijpt](../meten-voordat-je-ingrijpt/) voor de stap ervoor.
