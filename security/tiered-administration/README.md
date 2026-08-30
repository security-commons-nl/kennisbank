---
titel: Beheerrechten scheiden in tiers
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Beheerders krijgen aparte accounts per tier: identity en kroonjuwelen, servers en infrastructuur, werkplekken. Een account uit de ene tier kan niet inloggen op een lagere, zodat een gecompromitteerde werkplek geen beheerrechten oplevert. Met de indeling, de logon-beperkingen en het bewijs dat de scheiding technisch is afgedwongen.
barrieres: [model]
rol: fundering
---

# Beheerrechten scheiden in tiers

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/tiered-administration](https://security-commons-nl.github.io/kennisbank/security/tiered-administration/)

> **Barriere:** scheid privileged access technisch van dagelijks gebruik. Beheerders krijgen aparte accounts per beheer-tier (tier-0/1/2). Een account uit één tier kan niet inloggen op een lagere tier.

Eén beheerder heeft vaak één account dat overal mag, van het werkstation tot identity-beheer tot tenant-admin. Een compromittering op de laagste tier (dagelijks werkstation) levert direct het hoogste niveau. Laterale beweging is gratis.

## Wanneer wel, wanneer niet

Past in organisaties met een herkenbare beheer-hiërarchie (workstations, servers, identity). Wanneer niet: als de organisatie zo klein is dat één persoon alles doet, dan is JIT effectiever dan strakke tiering.

## Zo richt je het in

Het beheer wordt opgedeeld in tiers: tier-0 (identity, kroonjuwelen), tier-1 (servers, infra), tier-2 (workstations). Elke beheerder krijgt aparte accounts per tier. Een tier-0-account mag alleen op tier-0-systemen inloggen, een tier-2-account kan geen identity-beheer.

1. Definieer de tiers en welke systemen in elke tier vallen.
2. Maak per beheerder de benodigde tier-accounts aan, met aparte naamgeving.
3. Configureer logon-beperkingen: tier-0-accounts inloggen alleen op tier-0-systemen.
4. Pas Conditional Access aan: tier-0 verplicht via PAW en met JIT.
5. Train beheerders op het juiste account voor de juiste taak.
6. Monitor logins van tier-accounts op niet-passende systemen.

## Wat het kost en wat het oplevert

Kosten: laag.

**Wat het oplevert**

- Een compromittering op de werkplek-tier komt niet automatisch bij identity-beheer.
- Maakt de scope van een incident inschatbaar: welke tier is geraakt.
- Sluit aan op de gangbare tier-modellen (Microsoft, ISACA).

**Waar je op moet letten**

- Vereist meerdere accounts per beheerder, extra registratie en beheer.
- Bij krap bezet IT-team voelt het bureaucratisch.
- Strak afdwingen vraagt configuratie van de identity-provider die niet triviaal is.

## Bewijs

- De tierindeling met per tier de systemen die erin vallen.
- De logon-beperkingen per tier, als configuratie-export, met de uitzonderingen en hun reden.
- Een overzicht van beheerders met hun accounts per tier, zodat zichtbaar is dat niemand een gecombineerd account houdt.
- Monitoring op inlogpogingen van een tier-account op een systeem uit een andere tier.

## Zo leg je het uit

**Aan de directie.** Eén beheerder, één account dat overal mag, dat is het breekpunt waar elke aanvaller op rekent. Beheer in lagen knippen beperkt de schade van een gecompromitteerd account tot één laag.

**Aan de informatiemanager.** Past binnen het bestaande identity-platform en sluit aan op het tier-model. Vraagt inrichting van logon-restricties en accountnaamgeving.

**Aan het MT.** Beheerders krijgen meerdere accounts en moeten leren welk account voor welke taak. Een korte handleiding en oefening lossen het meeste op.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `model` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

De volgende stap na tiering is de beheerwerkplek zelf: zie [Beheerwerkplek voor administratieve taken](../beheerwerkplek/) en [Just-in-time beheerrechten](../just-in-time-beheerrechten/).

## Licentie

[EUPL-1.2](../../LICENSE).
