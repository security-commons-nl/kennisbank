---
titel: Kies voor een co-managed SIEM
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Een SIEM die je zelf bezit maar samen met een externe partij beheert: jij houdt de regie en het eigendom van data en detectieregels, de partij brengt schaal en dekking buiten kantooruren. Past bij organisaties die zelf securitycapaciteit hebben of opbouwen. Met de taakverdeling, de use-cases en het bewijs dat de opvolging binnen de afgesproken tijd gebeurt.
barrieres: [soc]
rol: alternatief
---

# Kies voor een co-managed SIEM

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/co-managed-siem](https://security-commons-nl.github.io/kennisbank/security/co-managed-siem/)

> **Barriere:** borg 24/7 opvolging en escalatie van kritieke meldingen. Dit is een van de vier manieren
> om die opvolging te organiseren, en de manier waarbij je zelf het meeste in handen houdt.

De logs zijn er, maar niemand analyseert ze. Aanvallen en verdacht gedrag worden niet opgemerkt, omdat er
geen correlatie en geen alerting op de verzamelde gegevens draait.

## Wanneer wel, wanneer niet

Past bij middelgrote en grote organisaties die regie willen houden over hun detectie en die zelf, geheel
of deels, security-analisten in huis hebben of opbouwen.

Wanneer niet: voor kleine organisaties zonder eigen securitycapaciteit. Een SIEM zonder mensen die hem
bedienen en tunen levert vooral ruis op, en die ruis kost meer dan hij oplevert.

## Zo richt je het in

Een SIEM-platform verzamelt en correleert de logs en genereert alerts op basis van detectieregels. Het
beheer is verdeeld: jij doet een deel zelf, de partner neemt een deel over, vaak de dekking buiten
kantooruren. Eigendom van het platform, de data en de detectieregels blijft bij jou.

1. Zorg dat [centrale logverzameling](../centrale-logverzameling/) op orde is. Dat is de basis; zonder
   verzamelde logs valt er niets te correleren.
2. Kies een SIEM-platform dat past bij de schaal en het landschap.
3. Bepaal de taakverdeling tussen jou en de partner, inclusief de dekking buiten kantooruren.
4. Stel use-cases en detectieregels op, beginnend bij de meest waarschijnlijke dreigingen.
5. Richt de alert-afhandeling in: triage, escalatie en opvolging.
6. Oefen het proces met een realistisch scenario.
7. Evalueer de use-cases periodiek en stuur bij. Een SIEM veroudert zonder onderhoud.

## Wat het kost en wat het oplevert

**Wat het oplevert**

- Maximale eigen regie; eigendom van data en detectieregels.
- Opbouw van eigen kennis en detectievermogen.
- Flexibiliteit: use-cases zijn aan te passen aan de lokale context.

**Waar je op moet letten**

- Het vereist eigen capaciteit en een zekere volwassenheid.
- Platformkosten en tuning zijn fors en doorlopend.
- Bij slechte tuning ontstaat alertmoeheid, en dan verdwijnen echte signalen in de ruis.

## Bewijs

- De vastgelegde taakverdeling met de partner, inclusief wie buiten kantooruren welke melding oppakt.
- De afgesproken triage-, reactie- en escalatietijden, en een meting of ze in de praktijk gehaald worden.
  Een melding zonder tijdige actie is nog geen bescherming.
- De lijst use-cases met de datum van de laatste evaluatie.
- Het verslag van de oefening met een realistisch scenario.

## Zo leg je het uit

**Aan de directie.** We houden zelf de regie over wat we detecteren en hoe we reageren, en kopen alleen
de schaal en de nachtdekking in. Onze data en onze detectieregels blijven van ons.

**Aan de informatiemanager.** Het platform komt bij ons te staan en vraagt doorlopend onderhoud: use-cases
verouderen. Reken op structurele inzet, niet op een project met een einddatum.

**Aan het MT.** Er is eigen capaciteit nodig om de alerts te bedienen en de regels te tunen. Zonder die
mensen levert het platform vooral ruis op.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `soc` uit de
[zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/), en is een **alternatief**
naast [Uitbestede SOC](../uitbestede-soc/), [MDR-dienst](../mdr-dienst/) en
[Regionaal of gedeeld SOC](../regionaal-soc/). De fundering onder alle vier is
[Richt centrale logverzameling in](../centrale-logverzameling/).

Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op
[Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

## Licentie

[EUPL-1.2](../../LICENSE).
