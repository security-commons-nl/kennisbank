---
titel: MFA afdwingen en zwakke routes saneren
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: De zwakke routes naast je sterke authenticatie opruimen: verouderde protocollen, herstelroutes en accounts die nog zonder sterke methode inloggen. Een sterke voordeur naast een open achterdeur is geen maatregel. Met de sanering en het bewijs dat er geen omweg meer is.
barrieres: [fallback, legacy]
rol: verdieping
---

# MFA afdwingen en zwakke routes saneren

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/mfa-handhaving](https://security-commons-nl.github.io/kennisbank/security/mfa-handhaving/)

> **Barriere:** verwijder zwakke fallback- en herstelroutes; blokkeer legacy authentication. De sluiproutes dichten die elke MFA-verplichting ondermijnen: bypass-groepen, zelfbediening-verwijdering van MFA, en het ontbreken van zicht op MFA-wijzigingen.

Een MFA- of passkey-verplichting is alleen zo sterk als de routes eromheen. In de praktijk ondermijnen drie structurele lekken de handhaving: dynamische uitzonderingsgroepen die ongemerkt groeien, een zelfbedieningspagina waar gebruikers hun eigen sterke methode kunnen verwijderen, en het volledig ontbreken van zicht, niemand merkt het wanneer de MFA-status van een account verandert. Nieuwe authenticatietechniek bovenop deze lekken levert nieuwe techniek en dezelfde gaten.

## Wanneer wel, wanneer niet

Altijd nodig, naast elk van de andere twee patronen. Het sluiten van de lekken hoort in dezelfde opdracht als het invoeren van phishingbestendige authenticatie, niet als losse vervolgstap. Wanneer niet als zelfstandige eindstap: lekken dichten zonder ook de authenticatiemethode te versterken laat de phishbare methode in stand.

## Zo richt je het in

Drie maatregelen. Dynamische uitzonderingsgroepen worden vervangen door een statisch beheerde lijst met per account een eigenaar, motivatie en einddatum, en een vaste reviewcyclus. De zelfbedieningspagina wordt zo ingericht dat een gebruiker een sterke methode niet kan verwijderen zonder eerst een vervangende sterke methode te registreren. En de identity-provider stuurt gebeurtenissen over MFA-statuswijzigingen naar de centrale logverzameling, met een alert wanneer een phishingbestendige methode wordt verwijderd.

1. Inventariseer de bestaande uitzonderings- en bypass-groepen; beoordeel elk lidmaatschap op nut en eigenaar.
2. Vervang dynamische uitzonderingsgroepen door een statisch beheerde lijst: per account eigenaar, motivatie en einddatum.
3. Richt een vaste reviewcyclus in voor de uitzonderingenlijst, gezamenlijk door beheer en de IB-functie.
4. Pas de zelfbedieningspagina aan: een sterke methode verwijderen kan alleen na registratie van een vervangende sterke methode.
5. Laat de identity-provider gebeurtenissen over MFA-statuswijzigingen naar de centrale logverzameling sturen.
6. Richt een alert in op het verwijderen of verzwakken van een phishingbestendige methode.
7. Rapporteer de MFA- en passkey-dekking periodiek, zodat erosie zichtbaar wordt.

## Wat het kost en wat het oplevert

Kosten: laag.

**Wat het oplevert**

- Maakt elke MFA- of passkey-verplichting daadwerkelijk afdwingbaar.
- Het systeem produceert voortaan zelf een signaal bij erosie, geen blind vertrouwen meer.
- Lage drempel: vooral configuratie en governance, geen nieuwe techniek.
- Voorkomt dat een nieuwe authenticatiemethode op oude gaten wordt gebouwd.

**Waar je op moet letten**

- Vraagt discipline: een statische uitzonderingenlijst moet ook echt periodiek herzien worden.
- Het strakker zetten van de zelfbedieningspagina kan tot meer supportvragen leiden.
- Levert op zichzelf geen sterkere authenticatie op, het is een randvoorwaarde, geen eindstap.
- Vereist dat centrale logverzameling op orde is om de wijzigingen te kunnen opvangen.

## Bewijs

- Het beleid dat verouderde authenticatie blokkeert, in afdwingstand en niet in report-only, met de uitzonderingen.
- Een overzicht van accounts die nog zonder sterke methode kunnen inloggen, idealiter leeg.
- De herstel- en registratieroutes: hoe komt iemand weer binnen na verlies van zijn middel, en waarom is dat geen zwakkere ingang.
- De dekking van de sterke methode als teller en noemer.

## Zo leg je het uit

**Aan de directie.** Een verplichting tot sterke authenticatie is waardeloos als er sluiproutes omheen liggen. Deze maatregel dicht die routes en zorgt dat het systeem voortaan zelf waarschuwt wanneer de bescherming afbrokkelt. Lage kosten, en een voorwaarde voor het slagen van de andere stappen.

**Aan de informatiemanager.** Het raakt de uitzonderingsgroepen, de zelfbedieningsinstellingen en de koppeling met de centrale logverzameling. Belangrijk: het eigenaarschap van de uitzonderingenlijst hoort bij een aanwijsbare interne rol, niet bij een uitvoerende beheerpartij.

**Aan het MT.** Het strakker afdwingen kan kortdurend meer vragen opleveren. Er is een vaste, terugkerende reviewtaak nodig, gezamenlijk belegd bij beheer en de IB-functie.

## Hoe dit samenhangt

Deze handleiding hoort bij de barrieres `fallback`, `legacy` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

De fundering is [Passkeys invoeren](../passkeys-invoeren/); deze handleiding gaat over wat daarnaast nog open kan staan.

## Licentie

[EUPL-1.2](../../LICENSE).
