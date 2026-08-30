---
titel: Deel een SOC met andere organisaties
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Meerdere organisaties delen een SOC: gedeelde kosten, gedeelde schaarse expertise, en de regie blijft publiek. Past bij kleine en middelgrote organisaties die al samenwerken of dat willen. Met de governance, de verwerkersafspraken tussen deelnemers en het bewijs dat de opvolging binnen de afgesproken tijd gebeurt.
barrieres: [soc]
rol: alternatief
---

# Deel een SOC met andere organisaties

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/regionaal-soc](https://security-commons-nl.github.io/kennisbank/security/regionaal-soc/)

> **Barriere:** borg 24/7 opvolging en escalatie van kritieke meldingen. Dit is de manier waarbij je de
> kosten deelt zonder de regie uit handen te geven.

Een eigen SOC is te duur voor een enkele, zeker kleine, organisatie. Volledig uitbesteden aan een
commerciele partij voelt te ver van huis, of past niet bij de wens om de regie publiek te houden.

## Wanneer wel, wanneer niet

Past bij kleine en middelgrote organisaties die al in een samenwerkingsverband zitten of er een willen
vormen.

Wanneer niet: als er geen samenwerkingspartners zijn, of als de bestuurlijke bereidheid om governance te
delen ontbreekt. Dat laatste is de echte drempel; de techniek is het probleem niet.

## Zo richt je het in

De deelnemers brengen logs en middelen samen in een gedeelde SOC-functie. Die kan bestaan uit eigen
personeel, een gezamenlijk ingekochte dienst, of een functie die bij een gastorganisatie is
ondergebracht. De governance loopt via een samenwerkingsovereenkomst.

1. Zorg dat [centrale logverzameling](../centrale-logverzameling/) bij elke deelnemer op orde is.
2. Bepaal de partners en de samenwerkingsvorm.
3. Spreek governance en kostenverdeling af.
4. Bepaal een gezamenlijke scope en gedeelde use-cases.
5. Maak verwerkers- en uitwisselingsafspraken tussen de deelnemers. Logs bevatten persoonsgegevens; wie
   wat mag zien van wie, is een AVG-vraag en geen technische.
6. Richt de gedeelde SOC-functie in.
7. Evalueer en stuur gezamenlijk bij.

## Wat het kost en wat het oplevert

**Wat het oplevert**

- Kosten en schaarse expertise worden gedeeld.
- De regie blijft publiek.
- Kennisdeling tussen de deelnemers: wat de een ziet, leert de ander.

**Waar je op moet letten**

- Governance-overhead.
- Besluitvorming is trager met meerdere partijen.
- De samenwerking is zo sterk als de zwakste schakel.
- Het opstarten kost tijd; reken in kwartalen, niet in weken.

## Bewijs

- De samenwerkingsovereenkomst met de governance en de kostenverdeling.
- De verwerkers- en uitwisselingsafspraken tussen de deelnemers, inclusief wie welke gegevens mag inzien.
- De afgesproken triage-, reactie- en escalatietijden, en een meting of ze gehaald worden. Een melding
  zonder tijdige actie is nog geen bescherming, ook niet als hij bij een partner ligt.
- De gedeelde use-cases met de datum van de laatste gezamenlijke evaluatie.

## Zo leg je het uit

**Aan de directie.** We kunnen dit niet alleen betalen en de mensen zijn schaars. Samen met andere
organisaties krijgen we wel een volwaardige functie, en de regie blijft in publieke handen.

**Aan de informatiemanager.** Onze logs gaan naar een gedeelde omgeving. Dat vraagt afspraken over wie wat
mag zien, en die leggen we vast voordat er een byte verstuurd wordt.

**Aan het MT.** Besluiten over detectie nemen we voortaan samen met de partners. Dat gaat trager, maar het
levert een functie op die we alleen niet zouden hebben.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `soc` uit de
[zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/), en is een **alternatief**
naast [Co-managed SIEM](../co-managed-siem/), [Uitbestede SOC](../uitbestede-soc/) en
[MDR-dienst](../mdr-dienst/). De fundering onder alle vier is
[Richt centrale logverzameling in](../centrale-logverzameling/).

Wie de gremia in kaart wil brengen waarmee zo'n samenwerking kan lopen, vindt die in de
[Stelselkaart security-gremia](../stelselkaart-security-gremia/).

Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op
[Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

## Licentie

[EUPL-1.2](../../LICENSE).
