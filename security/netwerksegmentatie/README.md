---
titel: Netwerksegmentatie
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Het netwerk opdelen in zones die aansluiten op je processen, met regels die daadwerkelijk worden afgedwongen in plaats van getekend. Zo komt een aanvaller die binnen is niet vanzelf overal. Met de zonebepaling, de handhaving en het bewijs dat de grenzen zijn getoetst.
barrieres: [segment]
rol: fundering
---

# Netwerksegmentatie

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/netwerksegmentatie](https://security-commons-nl.github.io/kennisbank/security/netwerksegmentatie/)

> **Barriere:** beperk lateral movement met segmentatie en minimale rechten. Het netwerk is opgedeeld in zones met expliciete grenzen tussen werkplekken, servers, beheer, OT en gastnetwerk, geen plat 'binnen-netwerk' meer.

Het netwerk is plat. Eenmaal binnen op één endpoint kan een aanvaller bij vrijwel alle systemen. Een werkstation in de publiekshal kan de domain controller bereiken; printers spreken met servers.

## Wanneer wel, wanneer niet

Past in elke organisatie met een eigen netwerk. Wanneer niet zonder beleid: segmentatie zonder duidelijk welke flows wel/niet mogen, wordt al snel teruggedraaid bij elk probleem.

## Zo richt je het in

Het netwerk wordt opgedeeld in zones: werkplek, server, beheer, OT, DMZ, gast. Tussen zones zit een firewall met expliciete regels, alleen flows die gemotiveerd zijn worden toegestaan. Inventarisatie van legitieme flows vooraf voorkomt operationele schokken.

1. Definieer de zones (werkplek, server, beheer, OT, DMZ, gast).
2. Inventariseer de huidige flows tussen die zones.
3. Stel een toelaatbare-flows-tabel op (welke flow van A naar B, met motivatie).
4. Implementeer technisch (VLAN, subnets, firewalls) in fasen.
5. Begin met audit-mode, ga over naar enforce na verificatie.
6. Monitor verkeer dat geblokkeerd wordt, voor opschoning of toevoeging.

## Wat het kost en wat het oplevert

Kosten: midden.

**Wat het oplevert**

- Een gecompromitteerd endpoint kan niet meer overal komen.
- Verlamming door één incident blijft beperkt tot één zone.
- Maakt onverwacht netwerkverkeer zichtbaar.

**Waar je op moet letten**

- Inventarisatie van flows kost tijd en levert verrassingen op.
- Verkeerd uitgevoerd breekt operationele diensten, fasering is cruciaal.
- Vraagt netwerkinrichting (firewalls, VLANs) en doorlopend beheer.

## Bewijs

- Het segmentatieoverzicht met de zones en de systemen die erin vallen.
- De regelset tussen de zones, met hit-counts, zodat zichtbaar is welke regels echt gebruikt worden en welke te breed staan.
- Een toets van de grenzen: is geprobeerd om vanuit de ene zone bij de andere te komen, en met welk resultaat.
- De uitzonderingen met hun reden.

## Zo leg je het uit

**Aan de directie.** Een aanvaller die op één werkplek binnenkomt mag niet automatisch bij de servers, dat is wat segmentatie regelt. Klassieke maatregel, fundamentele beperking van schade.

**Aan de informatiemanager.** Architectuur-werk: zones, firewalls, flow-tabel. Stem af met applicatie-eigenaren over toegestane flows.

**Aan het MT.** Lijnteams merken segmentatie alleen als ze nieuwe integraties bouwen, die moeten dan langs het flow-proces.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `segment` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

De verdieping is [Microsegmentatie](../microsegmentatie/). Voor het meten of je segmentatie werkt, staat in de pijler [Meten voordat je ingrijpt](../meten-voordat-je-ingrijpt/) een hoofdstuk over analyse uit firewall- en routerdata.

## Licentie

[EUPL-1.2](../../LICENSE).
