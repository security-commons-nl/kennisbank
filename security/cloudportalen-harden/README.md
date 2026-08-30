---
titel: Cloud-beheerportalen dichtzetten
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: De beheerportalen van je clouddiensten dichtzetten: wie mag erbij, vanaf welk apparaat, en met welke authenticatie. Een cloudportaal is bereikbaar vanaf elke plek ter wereld, dus de toegangsvoorwaarden zijn je enige grens. Met de inrichting en het bewijs dat de beperking geldt.
barrieres: [consent]
rol: fundering
---

# Cloud-beheerportalen dichtzetten

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/cloudportalen-harden](https://security-commons-nl.github.io/kennisbank/security/cloudportalen-harden/)

> **Barriere:** beperk app-toestemming en richt gecontroleerde admin consent in. Cloud-beheerportalen zijn alleen toegankelijk vanaf beheerwerkplekken, met phishingbestendige authenticatie en strakke Conditional Access, niet vanaf willekeurige plekken.

Cloud-beheerportalen zijn vanaf internet bereikbaar. Een gecompromitteerd beheeraccount geeft direct toegang tot de hele tenant, vanaf een internetcafé, een telefoon, een Tor-uitgang. Niets stopt het.

## Wanneer wel, wanneer niet

Past zodra er beheer-toegang tot cloud is. Wanneer niet zonder phishingbestendige MFA, het toegangsbeleid heeft daarop te leunen.

## Zo richt je het in

Conditional Access voor de beheerportalen: alleen vanaf compliant device + PAW, alleen met phishingbestendige MFA, alleen vanuit een beperkt aantal locaties. Beheerportalen zijn niet toegankelijk vanaf reguliere medewerker-laptops.

1. Identificeer welke portalen onder 'cloud-beheer' vallen.
2. Stel Conditional Access in: compliant device, PAW, phishingbestendige MFA.
3. Beperk locatie/IP-range waar mogelijk.
4. Activeer logging van toegangsmogingen op de beheerportalen.
5. Monitor afwijkende toegangsmogingen via SOC-functie.
6. Bekijk en herzie periodiek welke accounts toegang hebben.

## Wat het kost en wat het oplevert

Kosten: laag.

**Wat het oplevert**

- Een gestolen sessie of cookie elders werkt niet op het beheerportaal.
- Brengt cloud-beheer in lijn met PAW/tier-0-aanpak.
- Geen aparte licenties nodig in de meeste cloud-providers.

**Waar je op moet letten**

- Beheerders ervaren minder flexibiliteit (niet vanaf telefoon).
- Vereist dat PAW al ingericht is voor optimale werking.
- Te strakke locatie-restricties kunnen legitiem werk hinderen.

## Bewijs

- De toegangsvoorwaarden voor de beheerportalen: welke authenticatie, welk apparaat, welke locatie of welk netwerk.
- Een overzicht van accounts met beheertoegang tot elk portaal.
- De uitzonderingen, met reden en termijn.
- Monitoring op aanmeldingen bij de beheerportalen die buiten het beleid vallen.

## Zo leg je het uit

**Aan de directie.** Een Azure of AWS Portal-login vanaf een internetcafé moet niet kunnen, terwijl het standaard wel kan. Hardening sluit dat gat met de tools die we al hebben.

**Aan de informatiemanager.** Conditional Access op de beheerportalen, gekoppeld aan PAW en compliant device.

**Aan het MT.** Beheerders kunnen niet meer vanaf telefoon de cloud-portal in. Vraagt eenmalige uitleg en discipline.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `consent` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

Werkt samen met [Least privilege in de cloud](../least-privilege-cloud/) en [Just-in-time beheerrechten](../just-in-time-beheerrechten/).

## Licentie

[EUPL-1.2](../../LICENSE).
