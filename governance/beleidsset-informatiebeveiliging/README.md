---
titel: Beleidsset informatiebeveiliging volgens de BIO 2.0-indeling
vakgebied: governance
type: beleid
normen: [BIO2, BIO, ISO 27001, ISO 27002, Cbw]
peildatum: 2026-10-12
herkomst: vastgestelde thema-beleidsstukken (2020-2025) en concepten (2025-2026) van het team informatiebeveiliging en privacy (IB&P) van een regionale samenwerking van gemeenten, geordend en getoetst naar de 21 domeinen van de BIO 2.0; een deel bouwt voort op de handreikingen van de IBD
status: in gebruik
samenvatting: Een complete beleidsset geordend naar de 21 BIO 2.0-domeinen. Per domein het beleidsstuk van een regionale samenwerking (vastgesteld onder BIO 1 of als concept al op BIO 2.0), een toets van alle 117 overheidsmaatregelen (70 gedekt, 31 deels, 16 niet) en voor de vijf domeinen zonder stuk een sjabloon met de BIO 2.0-eisen klaar om in te vullen. Met een uitgewerkt beleid en controleraamwerk voor fysieke toegang als voorbeeld.
bronnen: [ibd-bio2-template-strategisch-informatiebeveiligings-en-privacybeleid, ibd-bio2-handreiking-strategisch-informatiebeveiligings-en-privacybeleid, ibd-bio2-rasci-tabel-controls-informatieveiligheid-en-privacy, ibd-bio2-gap-analyse, ibd-beleid-logische-toegangsbeveiliging-v1-0, ibd-dataclassificatie-bio2, ibd-encryptiebeleid-pki-gemeente-v1-0, ibd-hardening-beleid-voor-gemeenten, ibd-back-up-en-recovery-gemeente, ibd-personeelsbeleid, ibd-voorbeeld-incidentmanagement-en-response-beleid-2, ibd-wachtwoordbeleid-2]
---

# Beleidsset informatiebeveiliging volgens de BIO 2.0-indeling

> **Lees de beleidsset online:** [security-commons-nl.github.io/kennisbank/governance/beleidsset-informatiebeveiliging](https://security-commons-nl.github.io/kennisbank/governance/beleidsset-informatiebeveiliging/)

Onder de BIO 2.0 en de Cyberbeveiligingswet heeft elke gemeente een strategisch beleid nodig en daaronder
materie-specifiek beleid dat de 167 maatregelen afdekt. De IBD levert templates; wat ontbreekt, is een set
zoals een gemeente die werkelijk heeft, met de gaten erin zichtbaar. Dit is zo'n set, van een samenwerking
van gemeenten met één gezamenlijke bedrijfsvoering, geordend naar de 21 domeinen waarin het controleraamwerk
de BIO 2.0-maatregelen verdeelt.

De meeste vastgestelde stukken zijn nog onder BIO 1 geschreven. Daarom staat er een toets naast: per
overheidsmaatregel of er een beleidsregel is, waar die staat en wat er ontbreekt. Waar een domein geen stuk
heeft, staat een sjabloon klaar met de eisen per maatregel.

## De set per BIO 2.0-domein

Stand: **V** vastgesteld (onder BIO 1), **C** concept, **S** sjabloon. Dekking: overheidsmaatregelen gedekt
en deels gedekt, van het totaal. Details per maatregel in de [BIO 2.0-toets](bio2-toets.md).

| BIO 2.0-domein | Stuk | Stand | Dekking |
|---|---|---|---|
| IV-beleid | [Strategisch informatiebeveiligingsbeleid](strategisch-ib-beleid.md): herschreven voor de Cbw, met samenhang IB, privacy, OT en BCM, drie lijnen, contacten met toezichthouders en een verantwoordingsbijlage | C | 7 van 7 |
| Informatiebeveiliging binnen projecten | [Sjabloon informatiebeveiliging in projecten](beleid-informatiebeveiliging-in-projecten.md) | S | 0 van 1, 1 deels |
| Screening, bewustzijn & opleiding | [Veilig personeel](veilig-personeel.md): bewustwording, opleiding en gedrag | C | 4 van 7, 1 deels |
| Bedrijfsmiddelenbeheer | [Beheer van bedrijfsmiddelen](beheer-van-bedrijfsmiddelen.md): inventaris, eigenaarschap, gebruik, teruggave, labelen | V | 2 van 3, 1 deels |
| Informatie classificatie | [Dataclassificatie](dataclassificatie.md): BIV-niveaus met BBN, eisen per niveau, classificatierapport; [e-mail en chat met gezondheidsinformatie](mail-en-chat-met-gezondheidsinformatie.md) | V | 3 van 6, 2 deels |
| Logische toegangsbeveiliging | [Logische toegangsbeveiliging](logische-toegangsbeveiliging.md) met voorbeeldprocedures; [functionele accounts en postbussen](functionele-accounts-en-postbussen.md) | C, V | 7 van 14, 3 deels |
| Leveranciersbeheer, inkoop | [Beveiliging leveranciers en relaties](beveiliging-leveranciers-en-relaties.md): eisen in inkoopvoorwaarden en GIBIT; [webapplicaties](webapplicaties.md): 57 eisen aan webapplicaties en SaaS | V | 8 van 9 |
| Leveranciersbeheer, contractbeheer | [Beveiliging leveranciers en relaties](beveiliging-leveranciers-en-relaties.md) | V | 1 van 5, 4 deels |
| Security incident management | [Beveiligingsincidenten](beveiligingsincidenten.md): melden, beoordelen, leren, bewijs bewaren | V | 10 van 12, 2 deels |
| Business continuity & disaster recovery | Geen stuk in deze set; zie de [BCM-items](../../bcm/) | | 0 van 2, 1 deels |
| IT-compliance | [Sjabloon IT-compliance](beleid-it-compliance.md) | S | 2 van 2 (via privacy en toegang) |
| Fysieke toegang & beveiliging | [Fysieke toegang en beveiliging](fysieke-toegang-en-beveiliging.md) met [controleraamwerk](controls-fysieke-toegang-en-beveiliging.md): al op BIO 2.0 gebouwd, met per eis de maatregel en de control | C | 2 van 2 |
| Afvoer en hergebruik gegevensdragers | [Beheer van bedrijfsmiddelen](beheer-van-bedrijfsmiddelen.md), paragraaf 2.3 | V | 2 van 3, 1 deels |
| Mobile device management | [Sjabloon mobile device management](beleid-mobile-device-management.md); [wifi](wifi.md) | S, V | 1 van 2, 1 deels |
| Vulnerability & patchmanagement | [Kwetsbaarheidsmanagement](kwetsbaarheidsmanagement.md); [hardening](hardening.md) | V | 5 van 9, 4 deels |
| Back-up & recovery | [Back-up en recovery](back-up-en-recovery.md): strategie in een regieorganisatie met IaaS en SaaS | C | 4 van 4 |
| Logging & monitoring | [Sjabloon logging en monitoring](beleid-logging-en-monitoring.md) | S | 3 van 10, 1 deels |
| Netwerkbeveiliging | [Netwerkbeveiliging](netwerkbeveiliging.md); [wifi](wifi.md) | V | 5 van 7, 2 deels |
| Cryptografie | [Cryptografie](cryptografie.md): versleuteling per niveau, Forum Standaardisatie, certificaatbeheer | V | 2 van 4, 2 deels |
| Secure software development | [Webapplicaties](webapplicaties.md); [testdata](testdata.md): trapsgewijs van fictief tot productie | V | 1 van 2, 1 deels |
| Wijzigingsbeheer | [Sjabloon wijzigingsbeheer](beleid-wijzigingsbeheer.md) | S | 1 van 6, 4 deels |
| **Totaal** | | | **70 van 117, 31 deels** |

## Hoe je het gebruikt

- **Je eigen set toetsen.** Leg je stukken naast de [toets](bio2-toets.md): dezelfde 117 overheidsmaatregelen,
  dezelfde vraag per maatregel. De oordelen hier laten zien waar een BIO 1-set typisch tekortschiet:
  logging en monitoring, wijzigingsbeheer, accounts met bijzondere rechten, screening en de keten van
  toeleveranciers.
- **Een ontbrekend stuk schrijven.** Begin bij het sjabloon van het domein. Elke eis staat er al, met de
  regel die elders in de set al bestaat als vertrekpunt; jij vult wie, wat, hoe vaak en waarmee in.
- **Van beleid naar control.** Het beleid fysieke toegang laat zien hoe het eruitziet als het af is: per eis
  een maatregelnummer en een control met risico, eigenaar, frequentie en bewijslast.

Namen van de organisatie, systemen en leveranciers zijn vervangen door een rol of een invulveld tussen
vierkante haken.

## Wat dit niet is

Geen vastgesteld BIO 2.0-beleid: alleen het strategisch beleid en fysieke toegang zijn al op BIO 2.0
geschreven, en beide zijn concept. De toets zegt of er een beleidsregel staat, niet of de maatregel in de
praktijk werkt. Dataclassificatie en logische toegangsbeveiliging volgen de IBD-handreiking grotendeels
letterlijk. Van maatregelen waarvoor alleen ISO 27002 geldt, is de normtekst niet overgenomen.

## Licentie

EUPL-1.2.
