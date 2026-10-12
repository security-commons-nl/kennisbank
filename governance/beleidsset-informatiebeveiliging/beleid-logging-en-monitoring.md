# Beleid logging en monitoring (sjabloon)

> **Sjabloon.** Dit stuk is geen vastgesteld beleid van een organisatie. Het volgt de BIO 2.0-indeling en
> zet per maatregel de eis klaar; de beleidsregel vul je zelf in: wie, wat, hoe vaak, waarmee. Waar de
> beleidsset al een regel heeft, staat die als vertrekpunt bij de eis.

| | |
|---|---|
| Documenttype | Materie-specifiek beleid onder het strategisch informatiebeveiligingsbeleid |
| BIO 2.0-domein | Logging & monitoring |
| Versie | 0.1 (sjabloon) |
| Lijneigenaar | [eigenaar volgens de verklaring van toepasselijkheid] |
| Vaststeller | [volgens de procedure voor het vaststellen van beleid] |
| Evaluatie | Jaarlijks, in de PDCA-cyclus van het ISMS |

## Relevante beleidsdocumenten

| Document | Verhouding tot dit beleid |
|---|---|
| [Strategisch informatiebeveiligingsbeleid](strategisch-ib-beleid.md) | Bovenliggend kader; dit document werkt het uit voor logging en monitoring. |
| Verklaring van toepasselijkheid BIO 2.0 versie 1.3 | Bepaalt welke maatregelen in dit document zijn belegd, met eigenaar en status. |
| Controleraamwerk (controls per maatregel) | De controles waarmee de naleving van dit beleid wordt aangetoond; zie het [controleraamwerk fysieke toegang en beveiliging](controls-fysieke-toegang-en-beveiliging.md) voor de opzet. |
| [Netwerkbeveiliging](netwerkbeveiliging.md) | Bewaking van dataverkeer en het delen van dreigingen. |
| [Beveiligingsincidenten](beveiligingsincidenten.md) | Afhandeling van incidenten die uit monitoring voortkomen. |

## 1 Inleiding

Dit materie-specifieke beleidsdocument beschrijft de uitgangspunten en eisen die de organisatie
hanteert voor logging en monitoring, vanuit de context van informatiebeveiliging. Het is de vertaalslag
van het strategisch informatiebeveiligingsbeleid naar dit deelgebied en maakt deel uit van het ISMS.
De naleving wordt aangetoond met het controleraamwerk en jaarlijks getoetst in de PDCA-cyclus.

### 1.1 Doel en doelgroep

Dit beleid legt de minimale eisen vast voor het vastleggen, bewaren, beschermen en bewaken van logbestanden, en de detectie van en reactie op afwijkingen, ook als die door een SOC of MDR-dienstverlener worden uitgevoerd. Het richt zich op de volgende deelgebieden,
die overeenkomen met de ISO 27001-controls uit de verklaring van toepasselijkheid:

1. Logging (8.15)
2. Monitoren van activiteiten (8.16)

Dit beleidsdocument is bedoeld voor de IT-organisatie, systeemeigenaren, het securityteam en de SOC-dienstverlener.

### 1.2 Reikwijdte

[Waarom dit thema voor de eigen organisatie ertoe doet, in een of twee alinea's.]

#### 1.2.1 Organisatorisch toepassingsgebied

[Op wie het beleid van toepassing is: medewerkers, inhuur, leveranciers.]

#### 1.2.2 Technisch toepassingsgebied

[Op welke systemen, omgevingen en gegevens; beperk tot de scope van het ISMS.]

## 2 Eisen

### 2.1 Logging (8.15)

**Eis 8.15.01 (BIO 2.0).** Een logregel bevat minimaal: • Actie: de gebeurtenis of handeling die heeft plaatsgevonden. • Object: waarop de gebeurtenis of handeling effect had (bijvoorbeeld welk bestand, proces of systeem). • Resultaat: het resultaat van de gebeurtenis of handeling. • Oorsprong: het apparaat of de netwerklocatie van waaruit de gebeurtenis of handeling in gang is gezet. • Actor: identificatie van de persoon die of het proces dat de gebeurtenis in gang heeft gezet. • Tijdstempel: datum en tijdstip waarop de gebeurtenis of handeling plaatsvond.

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

**Eis 8.15.02 (BIO 2.0).** Een logregel bevat nooit gegevens die tot het doorbreken van de beveiliging kunnen leiden.

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

**Eis 8.15.03 (BIO 2.0).** Er is een overzicht van logbestanden die worden gegenereerd.

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

**Eis 8.15.04 (BIO 2.0).** De bewaartermijn van logbestanden en gegevens in het Security Incident en Event Monitoring (SIEM) worden risicogericht bepaald, rekening houdend met het scenario dat aanvallers langdurig binnen zijn.

Vertrekpunt in de set (deels): [dataclassificatie](dataclassificatie.md) 4.2.2; [beveiligingsincidenten](beveiligingsincidenten.md) 2.7. Bewaartermijnen per classificatieniveau; SIEM niet.

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

**Eis 8.15.05 (BIO 2.0).** Oneigenlijk wijzigen, verwijderen of pogingen daartoe van loggegevens worden zo snel mogelijk gemeld als informatiebeveiligingsincident via de procedure voor informatiebeveiligingsincidenten volgens beheersmaatregel 5.24 uit NEN-EN-ISO/IEC 27002:2022.

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

**Eis 8.15.06 (BIO 2.0).** Op basis van een expliciete risicoafweging bepaalt de entiteit de periodieke toetsing op het ongewijzigd bestaan van logbestanden gedurende de bewaartermijn. Toetsing wordt uitgevoerd door een ten opzichte van de uitvoering onafhankelijke functionaris.

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

### 2.2 Monitoren van activiteiten (8.16)

**Eis 8.16.01 (BIO 2.0).** Bij ontdekte nieuwe dreigingen (aanvallen) via overheidsmaatregel 8.16.03 worden deze binnen geldende juridische kaders verplicht gedeeld met de daarvoor aangewezen Computer Emergency Response Team (CERT).

Vertrekpunt in de set (gedekt): [kwetsbaarheidsmanagement](kwetsbaarheidsmanagement.md) 2.1.4; [netwerkbeveiliging](netwerkbeveiliging.md) 2.1.3.

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

**Eis 8.16.02 (BIO 2.0).** Het SIEM- en/of het SOC-monitoring-proces hebben eenduidige regels over wanneer een incident moet worden gerapporteerd aan het verantwoordelijke management.

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

**Eis 8.16.03 (BIO 2.0).** De informatieverwerkende omgeving wordt gemonitord met een detectie- en response-oplossing, waarmee aanvallen kunnen worden gedetecteerd en afwijkingen adequaat en tijdig worden behandeld.

Vertrekpunt in de set (gedekt): [netwerkbeveiliging](netwerkbeveiliging.md) 2.1.3.

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

**Eis 8.16.04 (BIO 2.0).** Actieve netwerkcomponenten zijn voorzien van logging en monitoring van die logging om afwijkende gebeurtenissen te kunnen waarnemen en daarop te reageren.

Vertrekpunt in de set (gedekt): [netwerkbeveiliging](netwerkbeveiliging.md) 2.1.3.

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

## Bijlage A Normen

De maatregelen uit de BIO 2.0 versie 1.3 die in dit document zijn belegd.

| Maatregel | ISO 27001-control | Bron van de eis | Waar in dit beleid | Control |
|---|---|---|---|---|
| 8.15.01 | Logging | BIO 2.0 | 2.1 | [control] |
| 8.15.02 | Logging | BIO 2.0 | 2.1 | [control] |
| 8.15.03 | Logging | BIO 2.0 | 2.1 | [control] |
| 8.15.04 | Logging | BIO 2.0 | 2.1 | [control] |
| 8.15.05 | Logging | BIO 2.0 | 2.1 | [control] |
| 8.15.06 | Logging | BIO 2.0 | 2.1 | [control] |
| 8.16.01 | Monitoren van activiteiten | BIO 2.0 | 2.2 | [control] |
| 8.16.02 | Monitoren van activiteiten | BIO 2.0 | 2.2 | [control] |
| 8.16.03 | Monitoren van activiteiten | BIO 2.0 | 2.2 | [control] |
| 8.16.04 | Monitoren van activiteiten | BIO 2.0 | 2.2 | [control] |

## Bijlage B Controleraamwerk

Per eis een control met risico, beheersdoelstelling, beschrijving, eigenaar, frequentie en bewijslast.
Zie het [controleraamwerk fysieke toegang en beveiliging](controls-fysieke-toegang-en-beveiliging.md) als voorbeeld.

| Control | Onderwerp | Eigenaar | Frequentie | Maatregelen |
|---|---|---|---|---|
| [CODE]-001 | [onderwerp] | [eigenaar] | [frequentie] | [n.nn.nn] |
