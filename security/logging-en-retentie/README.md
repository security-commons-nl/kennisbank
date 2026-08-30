---
titel: Bewaartermijnen voor logging en forensiek
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Beheerhandelingen, rolwijzigingen en privileged activiteiten worden vastgelegd, lang genoeg bewaard om een incident te reconstrueren, en er wordt op gealarmeerd. Zonder deze laag is achteraf niet vast te stellen wie wat deed. Met de retentiekeuze, de alerting en het bewijs dat de escalatie is getest.
barrieres: [adminmonitor]
rol: fundering
---

# Bewaartermijnen voor logging en forensiek

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/logging-en-retentie](https://security-commons-nl.github.io/kennisbank/security/logging-en-retentie/)

> **Barriere:** monitor privileged activiteiten en rolwijzigingen. Beveiligingsrelevante logs worden lang genoeg bewaard om aanvalsreconstructie en juridische bewijsvoering mogelijk te maken, met integriteit en toegangsbeperking.

Logs worden 30 of 90 dagen bewaard, want anders wordt het duur. Aanvallen blijken pas na maanden uit te komen, tegen die tijd is de bewijsvoering weg. Reconstructie van een aanval die zes maanden eerder begon is dan onmogelijk.

## Wanneer wel, wanneer niet

Past op de centrale logverzameling (zie het Visibility-cluster). Wanneer niet als losse keuze zonder budget voor opslag: een retentietermijn die niet wordt gehaald is geen retentietermijn.

## Zo richt je het in

Per logtype een retentietermijn afgestemd op (a) de reconstructie-behoefte (typisch 12-24 maanden voor identity- en endpoint-logs), (b) de AVG-bewaartermijn voor persoonsgegevens, (c) juridische bewijsbehoefte. Logs worden geschreven naar opslag met integriteits-bescherming; toegang is beperkt en gelogd.

1. Inventariseer welke logs beveiligingsrelevant zijn (identity, endpoint, netwerk, applicatie).
2. Stel per type een retentietermijn vast met onderbouwing.
3. Borg integriteit: hash, write-once of vergelijkbaar.
4. Beperk en log toegang tot de logopslag, dit zijn ook gevoelige gegevens.
5. Toets jaarlijks dat retentie wordt gehaald (opslag groeit; oude logs blijven echt staan).
6. Voeg de retentie-eisen toe aan de Annex voor leveranciers die voor ons loggen.

## Wat het kost en wat het oplevert

Kosten: laag.

**Wat het oplevert**

- Maakt reconstructie van trage aanvallen mogelijk.
- Levert bewijsmateriaal voor juridische opvolging en aansprakelijkheid.
- Sluit aan op AVG (33 lid 5: documentatieplicht) en NIS2 (incidentafhandeling).

**Waar je op moet letten**

- Opslag groeit; capaciteit moet vooruit worden gepland.
- Logs bevatten persoonsgegevens, bewaartermijnen moeten ook AVG-proof zijn.
- Toegangsbeperking op de logopslag vraagt zelfdiscipline; uitzonderingen sluipen er anders in.

## Bewijs

- Welke gebeurtenissen worden vastgelegd: rolactiveringen, rolwijzigingen, wijzigingen in beheerrechten en gebruik van speciale systeemhulpmiddelen.
- De retentietermijn per brontype, met de onderbouwing vanuit de reconstructiebehoefte en de AVG.
- De alertregels op privileged activiteit, en een testverslag waaruit blijkt dat de melding aankomt en wordt opgevolgd.
- Bescherming van de loggegevens zelf: een beheerder mag zijn eigen sporen niet kunnen wissen.

## Zo leg je het uit

**Aan de directie.** Trage aanvallen worden pas na maanden zichtbaar. Zonder voldoende lange logretentie kunnen we dan niet reconstrueren wat er gebeurd is, en daarmee niet leren of bewijzen.

**Aan de informatiemanager.** Inpassing op de centrale logverzameling; retentietermijnen per logtype. Toegang tot logopslag is een beperkte, beheerde rol.

**Aan het MT.** De SOC-functie weet welke logs hoe lang beschikbaar zijn voor onderzoek. Geen wijziging in dagelijkse handelingen.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `adminmonitor` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

Bouwt op [Richt centrale logverzameling in](../centrale-logverzameling/); wat je hier vastlegt, komt daar binnen.

## Licentie

[EUPL-1.2](../../LICENSE).
