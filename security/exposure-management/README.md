---
titel: Kwetsbaarheden wegen op werkelijke blootstelling
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Niet elke kwetsbaarheid is even dringend: exposure management weegt bereikbaarheid, misbruik in het wild en de waarde van het systeem mee, zodat je de scanlijst omzet in een werkbare volgorde. Verdieping bovenop scannen. Met de weging, de bronnen en het bewijs dat prioriteit onderbouwd is.
barrieres: [vuln]
rol: verdieping
---

# Kwetsbaarheden wegen op werkelijke blootstelling

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/exposure-management](https://security-commons-nl.github.io/kennisbank/security/exposure-management/)

> **Barriere:** borg continu kwetsbaarhedenbeheer en spoedpatching. Niet elke kwetsbaarheid is een risico; exposure management combineert kwetsbaarheid + uitnutbaarheid + asset-criticaliteit tot een prioritering die uitvoerbaar is.

Vulnerability scanning levert duizenden bevindingen. Zonder context, is dit uitnutbaar? draait het op een kritiek systeem? staat het op internet?, is alles even urgent en wordt niets aangepakt.

## Wanneer wel, wanneer niet

Past in organisaties met substantieel asset-volume. Wanneer niet zonder asset-classificatie: zonder kennis van criticaliteit kan exposure management niet prioriteren.

## Zo richt je het in

Een platform combineert vulnerability-data met threat-intelligence (CISA KEV, exploit-prediction) en asset-criticaliteit. Resulteert in een gefocuste lijst: deze tien moeten echt deze week, de rest kan wachten.

1. Classificeer assets op criticaliteit (kritiek/standaard/laag).
2. Koppel vulnerability-scans aan threat intelligence-feeds.
3. Implementeer prioritering: criticaliteit × uitnutbaarheid × kwetsbaarheid.
4. Lever gefocuste lijst aan asset-eigenaren.
5. Monitor 'aanvalsdruk' op specifieke kwetsbaarheidsklassen.
6. Beoordeel de prioritering periodiek op effect.

## Wat het kost en wat het oplevert

Kosten: midden.

**Wat het oplevert**

- Concreet 'wat moet eerst' in plaats van overweldigende lijst.
- Sluit aan op risico-gebaseerd denken in BIO/NIS2.
- Verlaagt schade-kans tussen patch-momenten, focus op echt risico.

**Waar je op moet letten**

- Platform-keuze niet triviaal; integraties zijn werk.
- Asset-classificatie moet up-to-date blijven, anders rot prioritering mee.
- Threat-intel-feeds variëren; sommige zijn licentie-werk.

## Bewijs

- De wegingsfactoren die je gebruikt en waar ze vandaan komen: bereikbaarheid, actief misbruik, kritikaliteit van het systeem.
- Een voorbeeld van een bevinding die door de weging naar boven of naar beneden is gegaan, met de onderbouwing.
- De doorlooptijd van de bevindingen die als hoogste prioriteit uit de weging komen.

## Zo leg je het uit

**Aan de directie.** Niet elke kwetsbaarheid is gelijk; sommige zijn actief uitgenut, andere theoretisch. Exposure management richt onze tijd op wat echt risico is.

**Aan de informatiemanager.** Asset-classificatie en threat-intel-koppeling; output naar asset-eigenaren.

**Aan het MT.** Asset-eigenaren krijgen een gefocuste 'doe-deze-eerst'-lijst in plaats van een wall-of-red.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `vuln` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

Bouwt op [Kwetsbaarheden scannen](../kwetsbaarheden-scannen/); zonder scan is er niets om te wegen.

## Licentie

[EUPL-1.2](../../LICENSE).
