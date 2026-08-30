---
titel: Kwetsbaarheden scannen en opvolgen
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Continu scannen op kwetsbaarheden met een spoedprocedure voor wat actief wordt misbruikt, en gemeten doorlooptijden per risicoklasse. Een jaarlijkse scan is geen kwetsbaarhedenbeheer. Met de inrichting, de opvolging en het bewijs dat bevindingen ook echt dichtgaan.
barrieres: [vuln]
rol: fundering
---

# Kwetsbaarheden scannen en opvolgen

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/kwetsbaarheden-scannen](https://security-commons-nl.github.io/kennisbank/security/kwetsbaarheden-scannen/)

> **Barriere:** borg continu kwetsbaarhedenbeheer en spoedpatching. Alle systemen worden periodiek gescand op bekende kwetsbaarheden, werkplekken, servers, netwerkapparatuur, applicaties, met triage en SLA per severity.

Patchbeheer is reactief en gedeeltelijk. Niemand weet welke systemen welke kwetsbaarheden hebben. Een Log4Shell of Citrix-Bleed sluipt erin omdat het audit-overzicht ontbreekt.

## Wanneer wel, wanneer niet

Voor elke organisatie. Wanneer niet zonder eigenaarschap per bevinding: een dashboard zonder triage wordt een 'altijd-rood-dashboard'.

## Zo richt je het in

Een vulnerability-scanner (Tenable, Qualys, Rapid7, open-source als OpenVAS) draait periodiek over alle assets. Bevindingen krijgen severity (CVSS) en eigenaar. SLA's per severity sturen de afhandeling. Patchcyclus en uitzonderingen worden gedocumenteerd.

1. Inventariseer welke assets in scope zijn (intern, extern, cloud).
2. Implementeer de scanner met geauthenticeerde scans waar mogelijk.
3. Beleg eigenaarschap per asset-categorie of -team.
4. Stel SLA's per severity in (kritiek 7 dagen, hoog 30 dagen, etc.).
5. Integreer met patch-management en exposure-management.
6. Rapporteer periodiek aan CISO/MT op trends en achterstand.

## Wat het kost en wat het oplevert

Kosten: laag.

**Wat het oplevert**

- Bekende kwetsbaarheden worden zichtbaar in plaats van per nieuws-incident.
- Sluit aan op NIS2-kwetsbaarheidsbeheer-eis en BIO-maatregelen.
- Maakt patch-prioritering inhoudelijk in plaats van willekeurig.

**Waar je op moet letten**

- Scans zonder eigenaarschap leveren rapportages zonder herstel.
- Geauthenticeerde scans kunnen tijdelijk performance raken, planning vereist.
- Bevindingen op systemen die niet meer in beheer zijn, opruim-werk.

## Bewijs

- De scanfrequentie en de dekking: welk deel van het landschap wordt gescand, en wat niet.
- De doorlooptijden per risicoklasse, gemeten en niet alleen afgesproken.
- De lijst openstaande kritieke bevindingen met eigenaar en termijn.
- De spoedprocedure voor actief misbruikte kwetsbaarheden, met een voorbeeld waarin hij is gebruikt.

## Zo leg je het uit

**Aan de directie.** Welke kwetsbaarheden zitten er in onze systemen? Vandaag is het antwoord vaak 'we weten het niet'. Vulnerability scanning levert dat antwoord en dwingt opvolging af.

**Aan de informatiemanager.** Scanner over alle assets; integratie met patch-management en de asset-administratie.

**Aan het MT.** Asset-eigenaren krijgen bevindingen; SLA-bewaking is doorlopende taak.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `vuln` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

De verdieping erop is [Exposure management](../exposure-management/): niet alles wat kwetsbaar is, is ook bereikbaar.

## Licentie

[EUPL-1.2](../../LICENSE).
