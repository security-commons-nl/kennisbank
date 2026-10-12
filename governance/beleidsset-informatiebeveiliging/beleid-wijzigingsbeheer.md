# Beleid wijzigingsbeheer (sjabloon)

> **Sjabloon.** Dit stuk is geen vastgesteld beleid van een organisatie. Het volgt de BIO 2.0-indeling en
> zet per maatregel de eis klaar; de beleidsregel vul je zelf in: wie, wat, hoe vaak, waarmee. Waar de
> beleidsset al een regel heeft, staat die als vertrekpunt bij de eis.

| | |
|---|---|
| Documenttype | Materie-specifiek beleid onder het strategisch informatiebeveiligingsbeleid |
| BIO 2.0-domein | Wijzigingsbeheer |
| Versie | 0.1 (sjabloon) |
| Lijneigenaar | [eigenaar volgens de verklaring van toepasselijkheid] |
| Vaststeller | [volgens de procedure voor het vaststellen van beleid] |
| Evaluatie | Jaarlijks, in de PDCA-cyclus van het ISMS |

## Relevante beleidsdocumenten

| Document | Verhouding tot dit beleid |
|---|---|
| [Strategisch informatiebeveiligingsbeleid](strategisch-ib-beleid.md) | Bovenliggend kader; dit document werkt het uit voor wijzigingsbeheer. |
| Verklaring van toepasselijkheid BIO 2.0 versie 1.3 | Bepaalt welke maatregelen in dit document zijn belegd, met eigenaar en status. |
| Controleraamwerk (controls per maatregel) | De controles waarmee de naleving van dit beleid wordt aangetoond; zie het [controleraamwerk fysieke toegang en beveiliging](controls-fysieke-toegang-en-beveiliging.md) voor de opzet. |
| [Functionele accounts en postbussen](functionele-accounts-en-postbussen.md) | Wijzigingen door leveranciers. |
| [Testdata](testdata.md) | Welke gegevens in test en acceptatie mogen worden gebruikt. |

## 1 Inleiding

Dit materie-specifieke beleidsdocument beschrijft de uitgangspunten en eisen die de organisatie
hanteert voor wijzigingsbeheer, vanuit de context van informatiebeveiliging. Het is de vertaalslag
van het strategisch informatiebeveiligingsbeleid naar dit deelgebied en maakt deel uit van het ISMS.
De naleving wordt aangetoond met het controleraamwerk en jaarlijks getoetst in de PDCA-cyclus.

### 1.1 Doel en doelgroep

Dit beleid legt de minimale eisen vast voor wijzigingen in informatiesystemen, infrastructuur en software, inclusief testen, acceptatie en scheiding van ontwikkel-, test-, acceptatie- en productieomgevingen. Het richt zich op de volgende deelgebieden,
die overeenkomen met de ISO 27001-controls uit de verklaring van toepasselijkheid:

1. Gedocumenteerde bedieningsprocedures (5.37)
2. Installeren van software op operationele systemen (8.19)
3. Testen van de beveiliging tijdens ontwikkeling en acceptatie (8.29)
4. Scheiden van ontwikkel-, test- en productieomgevingen (8.31)
5. Wijzigingsbeheer (8.32)
6. Testgegevens (8.33)

Dit beleidsdocument is bedoeld voor de IT-organisatie, functioneel beheer, leveranciers die wijzigingen doorvoeren en het change advisory board.

### 1.2 Reikwijdte

[Waarom dit thema voor de eigen organisatie ertoe doet, in een of twee alinea's.]

#### 1.2.1 Organisatorisch toepassingsgebied

[Op wie het beleid van toepassing is: medewerkers, inhuur, leveranciers.]

#### 1.2.2 Technisch toepassingsgebied

[Op welke systemen, omgevingen en gegevens; beperk tot de scope van het ISMS.]

## 2 Eisen

### 2.1 Gedocumenteerde bedieningsprocedures (5.37)

**Eis 5.37.01 (ISO 27002).** Voor deze maatregel kent de BIO 2.0 geen overheidsmaatregel; de eis is ISO/IEC 27002:2022, maatregel 5.37 (Gedocumenteerde bedieningsprocedures).

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

### 2.2 Installeren van software op operationele systemen (8.19)

**Eis 8.19.01 (BIO 2.0).** Het risico van installatie door gebruikers van niet geautoriseerde software wordt beheerst.

Vertrekpunt in de set (gedekt): [hardening](hardening.md) maatregelen.

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

### 2.3 Testen van de beveiliging tijdens ontwikkeling en acceptatie (8.29)

**Eis 8.29.01 (BIO 2.0).** Voor acceptatietesten van systemen worden gestructureerde testmethodieken gebruikt. De testen worden waar mogelijk geautomatiseerd uitgevoerd. Van de resultaten van de testen wordt verslag gemaakt.

Vertrekpunt in de set (deels): [testdata](testdata.md) formulier. Testtypes genoemd; geen eis aan methodiek en verslag.

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

### 2.4 Scheiden van ontwikkel-, test- en productieomgevingen (8.31)

**Eis 8.31.01 (BIO 2.0).** In de productieomgeving wordt niet getest. Alleen met voorafgaande goedkeuring door de proceseigenaar kan hiervan worden afgeweken.

Vertrekpunt in de set (deels): [testdata](testdata.md) uitzondering 3; [webapplicaties](webapplicaties.md) eis 46. Scheiding OTA en strenge eisen aan productiedata; het verbod zelf staat er niet zo.

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

**Eis 8.31.02 (BIO 2.0).** Significante wijzigingen in de productieomgeving worden altijd getest voordat zij in productie gebracht worden. Alleen met voorafgaande goedkeuring door de proceseigenaar kan hiervan worden afgeweken.

Vertrekpunt in de set (deels): [functionele accounts en postbussen](functionele-accounts-en-postbussen.md) 3.1. Alleen voor wijzigingen door leveranciers.

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

### 2.5 Wijzigingsbeheer (8.32)

**Eis 8.32.01 (BIO 2.0).** In het wijzigingsbeheerproces is minimaal aandacht besteed aan: • het administreren van wijzigingen, met de resultaten van het testplan; • een risicoafweging van mogelijke gevolgen van de wijzigingen, inclusief een beschreven rollback-plan; • de goedkeuringsprocedure voor wijzigingen.

Vertrekpunt in de set (deels): [functionele accounts en postbussen](functionele-accounts-en-postbussen.md) 3.1; [netwerkbeveiliging](netwerkbeveiliging.md) 2.1.8. Voor leverancierswijzigingen en het netwerk; geen algemeen wijzigingsbeleid.

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

**Eis 8.32.02 (BIO 2.0).** Wijzigingsbeheer vindt plaats op basis van een algemeen geaccepteerd beheerraamwerk.

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

### 2.6 Testgegevens (8.33)

**Eis 8.33.01 (ISO 27002).** Voor deze maatregel kent de BIO 2.0 geen overheidsmaatregel; de eis is ISO/IEC 27002:2022, maatregel 8.33 (Testgegevens).

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

## Bijlage A Normen

De maatregelen uit de BIO 2.0 versie 1.3 die in dit document zijn belegd.

| Maatregel | ISO 27001-control | Bron van de eis | Waar in dit beleid | Control |
|---|---|---|---|---|
| 5.37.01 | Gedocumenteerde bedieningsprocedures | ISO 27002 | 2.1 | [control] |
| 8.19.01 | Installeren van software op operationele systemen | BIO 2.0 | 2.2 | [control] |
| 8.29.01 | Testen van de beveiliging tijdens ontwikkeling en acceptatie | BIO 2.0 | 2.3 | [control] |
| 8.31.01 | Scheiden van ontwikkel-, test- en productieomgevingen | BIO 2.0 | 2.4 | [control] |
| 8.31.02 | Scheiden van ontwikkel-, test- en productieomgevingen | BIO 2.0 | 2.4 | [control] |
| 8.32.01 | Wijzigingsbeheer | BIO 2.0 | 2.5 | [control] |
| 8.32.02 | Wijzigingsbeheer | BIO 2.0 | 2.5 | [control] |
| 8.33.01 | Testgegevens | ISO 27002 | 2.6 | [control] |

## Bijlage B Controleraamwerk

Per eis een control met risico, beheersdoelstelling, beschrijving, eigenaar, frequentie en bewijslast.
Zie het [controleraamwerk fysieke toegang en beveiliging](controls-fysieke-toegang-en-beveiliging.md) als voorbeeld.

| Control | Onderwerp | Eigenaar | Frequentie | Maatregelen |
|---|---|---|---|---|
| [CODE]-001 | [onderwerp] | [eigenaar] | [frequentie] | [n.nn.nn] |
