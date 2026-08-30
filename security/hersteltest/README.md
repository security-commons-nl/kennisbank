---
titel: Hersteltest tegen RTO en RPO
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Periodiek daadwerkelijk terugzetten en meten of je de afgesproken hersteltijd en het maximale dataverlies haalt. Een back-up die nooit is teruggezet, is een aanname. Met de opzet van de test, de RTO en RPO uit de BIA, en het testverslag als bewijs.
barrieres: [restore]
rol: fundering
---

# Hersteltest tegen RTO en RPO

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/hersteltest](https://security-commons-nl.github.io/kennisbank/security/hersteltest/)

> **Barriere:** test herstel tegen de afgesproken RTO en RPO. Herstel- en disaster-recovery-procedures worden minimaal jaarlijks geoefend met een realistisch scenario, papier wint niet van bewijs.

DR-procedures bestaan op papier maar zijn nooit getest. Bij een echte verstoring blijken back-ups corrupt, runbooks verouderd, contactgegevens onjuist en de hersteltijd veel langer dan beloofd.

## Wanneer wel, wanneer niet

Voorwaarde voor elke organisatie die op herstel-toezeggingen vertrouwt, intern of contractueel (RTO/RPO). Wanneer niet zonder bestuurlijke commitment: oefenen kost tijd en frustreert; zonder ruggesteun stopt het na de eerste keer.

## Zo richt je het in

Een gepland oefenmoment per jaar (minimaal) met een realistisch scenario: volledig herstel van een kritieke dienst vanaf back-up, met klok erop. Resultaten worden vastgelegd; afwijkingen op de toezegging worden opgelost vóór de volgende oefening.

1. Stel per kritieke dienst de RTO/RPO-toezeggingen vast.
2. Schrijf het recovery-runbook per dienst, concreet, met commando's en eigenaren.
3. Plan een jaarlijkse oefening met een realistisch scenario.
4. Voer de oefening uit met klok; meet of de toezegging wordt gehaald.
5. Documenteer afwijkingen en knelpunten; los ze op vóór de volgende oefening.
6. Rapporteer resultaten aan directie en (indien van toepassing) opdrachtgevers.

## Wat het kost en wat het oplevert

Kosten: laag.

**Wat het oplevert**

- Brengt afstand tussen toezegging en realiteit aan het licht, vóór er een echte crisis is.
- Maakt back-ups bruikbaar in plaats van alleen aanwezig.
- Voldoet aan de NIS2-eis voor periodieke effectiviteitsbeoordeling.

**Waar je op moet letten**

- Vraagt productietijd of een test-omgeving die representatief is.
- Het runbook moet onderhouden worden, verouderd vergroot het risico.
- Bestuurlijke commitment is voorwaarde; zonder die wordt geoefend overgeslagen.

## Bewijs

- Het testverslag: welk systeem, welke datum, hoe lang het herstel duurde en hoeveel data verloren ging.
- De afgesproken RTO en RPO uit de business impact analyse, en of ze gehaald zijn.
- Wat er misging tijdens de test en wat daarmee is gedaan; een test zonder bevindingen is verdacht.
- De frequentie waarmee dit herhaald wordt.

## Zo leg je het uit

**Aan de directie.** De back-up is er, maar werkt hij ook? Pas een oefening levert dat bewijs. Eén jaar zonder oefening is voldoende om de back-up technisch wel maar feitelijk niet meer betrouwbaar te hebben.

**Aan de informatiemanager.** Vraagt een test-/herstel-omgeving en runbook-onderhoud per kritieke dienst. Resultaten gaan in de rapportage richting opdrachtgevers en directie.

**Aan het MT.** Eén keer per jaar een geplande oefening, productietijd waar wat tegenover staat: bewijs van werkbaarheid, en een lijst echte fouten die op tijd worden opgelost.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `restore` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

Bouwt op [Onveranderbare back-ups](../onveranderbare-backups/) en voedt [Crisisoefening](../crisisoefening/).

## Licentie

[EUPL-1.2](../../LICENSE).
