---
titel: Microsegmentatie
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Segmentatie doortrekken tot op werklastniveau, zodat ook binnen een zone niet alles met alles kan praten. Verdieping voor wie de zones al op orde heeft. Met de aanpak, de valkuilen en het bewijs van de afgedwongen regels.
barrieres: [segment]
rol: verdieping
---

# Microsegmentatie

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/microsegmentatie](https://security-commons-nl.github.io/kennisbank/security/microsegmentatie/)

> **Barriere:** beperk lateral movement met segmentatie en minimale rechten. Binnen zones wordt per workload of service geregeld welk verkeer is toegestaan, server-A spreekt alleen met server-B als dat expliciet is afgesproken, niet 'omdat ze in dezelfde zone staan'.

Klassieke segmentatie houdt op bij zone-grenzen. Binnen een zone (bijvoorbeeld de serverlaag) kunnen workloads vrijuit met elkaar praten, wat ransomware-verspreiding en laterale beweging mogelijk maakt.

## Wanneer wel, wanneer niet

Past in volwassen organisaties met goed gedocumenteerde service-architectuur. Wanneer niet zonder eerst klassieke segmentatie: microsegmentatie zonder zonering is dweilen met de kraan open.

## Zo richt je het in

Een microsegmentatie-platform (Illumio, NSX, cloud-native zoals security-groups) past beleid op workload-niveau toe. Per workload: welke andere workloads/services zijn toegestaan. Discovery-mode bouwt eerst een beeld van bestaande flows; enforcement volgt.

1. Zorg dat klassieke segmentatie staat (eerste patroon).
2. Kies een microsegmentatie-platform passend bij hosting (on-prem, cloud, beide).
3. Plaats agents/sensors op alle workloads.
4. Loop discovery-fase: leer de bestaande flows.
5. Stel beleid op per workload-tier; ga van audit naar enforce in fasen.
6. Onderhoud beleid bij wijzigingen, automatisering via labels en tags.

## Wat het kost en wat het oplevert

Kosten: hoog.

**Wat het oplevert**

- Laterale beweging binnen zones wordt drastisch beperkt.
- Ransomware kan zich veel moeilijker verspreiden.
- Maakt service-afhankelijkheden zichtbaar, een bijproduct van waarde.

**Waar je op moet letten**

- Significant project: licentie-, agent- en inrichtings-investering.
- Vereist gedisciplineerd label-/tag-beleid om schaalbaar te zijn.
- Verkeerd uitgevoerd raakt productie, fasering verplicht.

## Bewijs

- Het beleid per werklast of applicatiegroep, met wat er wel en niet mag.
- Een meting van het werkelijke verkeer voordat je afdwingt, zodat je legitieme stromen niet breekt.
- De regels in afdwingstand, met de dekking.
- Een toets waaruit blijkt dat verkeer dat niet mag, ook echt wordt geblokkeerd.

## Zo leg je het uit

**Aan de directie.** Binnen onze server-zone kunnen aanvallers nog steeds laterally bewegen. Microsegmentatie sluit dat, substantieel werk, ook substantieel effect bij grotere incidenten.

**Aan de informatiemanager.** Architectuur-investering en operationeel een platform erbij. Labels en tags worden noodzakelijke discipline.

**Aan het MT.** Workload- en applicatieteams werken volgens labels en flows. Eenmalige inrichting, doorlopende discipline.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `segment` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

Zonder [Netwerksegmentatie](../netwerksegmentatie/) is dit niet de volgende stap maar de eerste, en dan is het te duur.

## Licentie

[EUPL-1.2](../../LICENSE).
