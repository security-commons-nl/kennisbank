# Beleid mobile device management (sjabloon)

> **Sjabloon.** Dit stuk is geen vastgesteld beleid van een organisatie. Het volgt de BIO 2.0-indeling en
> zet per maatregel de eis klaar; de beleidsregel vul je zelf in: wie, wat, hoe vaak, waarmee. Waar de
> beleidsset al een regel heeft, staat die als vertrekpunt bij de eis.

| | |
|---|---|
| Documenttype | Materie-specifiek beleid onder het strategisch informatiebeveiligingsbeleid |
| BIO 2.0-domein | Mobile Device Management |
| Versie | 0.1 (sjabloon) |
| Lijneigenaar | [eigenaar volgens de verklaring van toepasselijkheid] |
| Vaststeller | [volgens de procedure voor het vaststellen van beleid] |
| Evaluatie | Jaarlijks, in de PDCA-cyclus van het ISMS |

## Relevante beleidsdocumenten

| Document | Verhouding tot dit beleid |
|---|---|
| [Strategisch informatiebeveiligingsbeleid](strategisch-ib-beleid.md) | Bovenliggend kader; dit document werkt het uit voor mobile device management. |
| Verklaring van toepasselijkheid BIO 2.0 versie 1.3 | Bepaalt welke maatregelen in dit document zijn belegd, met eigenaar en status. |
| Controleraamwerk (controls per maatregel) | De controles waarmee de naleving van dit beleid wordt aangetoond; zie het [controleraamwerk fysieke toegang en beveiliging](controls-fysieke-toegang-en-beveiliging.md) voor de opzet. |
| [Wifi](wifi.md) | Zero footprint en toegang tot het netwerk. |
| [Beheer van bedrijfsmiddelen](beheer-van-bedrijfsmiddelen.md) | Uitgifte, inname en wissen op afstand. |

## 1 Inleiding

Dit materie-specifieke beleidsdocument beschrijft de uitgangspunten en eisen die de organisatie
hanteert voor mobile device management, vanuit de context van informatiebeveiliging. Het is de vertaalslag
van het strategisch informatiebeveiligingsbeleid naar dit deelgebied en maakt deel uit van het ISMS.
De naleving wordt aangetoond met het controleraamwerk en jaarlijks getoetst in de PDCA-cyclus.

### 1.1 Doel en doelgroep

Dit beleid legt de minimale eisen vast voor mobiele apparatuur van de organisatie en privé-apparatuur waarmee bedrijfsinformatie wordt verwerkt. Het richt zich op de volgende deelgebieden,
die overeenkomen met de ISO 27001-controls uit de verklaring van toepasselijkheid:

1. ‘User endpoint devices’ (8.01)

Dit beleidsdocument is bedoeld voor de IT-organisatie, leidinggevenden en alle medewerkers die mobiel werken.

### 1.2 Reikwijdte

[Waarom dit thema voor de eigen organisatie ertoe doet, in een of twee alinea's.]

#### 1.2.1 Organisatorisch toepassingsgebied

[Op wie het beleid van toepassing is: medewerkers, inhuur, leveranciers.]

#### 1.2.2 Technisch toepassingsgebied

[Op welke systemen, omgevingen en gegevens; beperk tot de scope van het ISMS.]

## 2 Eisen

### 2.1 ‘User endpoint devices’ (8.01)

**Eis 8.01.01 (BIO 2.0).** Mobiele apparatuur is zo ingericht dat bedrijfsinformatie niet standaard op het gebruikersdevice wordt opgeslagen (‘zero footprint’). Als (near) zero footprint (nog) niet realiseerbaar is, biedt een mobiel apparaat de mogelijkheid om de toegang te beschermen met een toegangsbeveiligingsmechanisme met minimaal versleuteling van de gegevens. Op mobiele apparatuur is ‘wissen op afstand’ mogelijk.

Vertrekpunt in de set (gedekt): [wifi](wifi.md) beleid.

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

**Eis 8.01.02 (BIO 2.0).** Bij de inzet van mobiele apparatuur zijn minimaal de volgende aspecten geïmplementeerd: • Het apparaat maakt deel uit van patchmanagement en hardening. • Er wordt gebruik gemaakt van Mobile Device Management (MDM)- of Mobile Application Management (MAM)-oplossingen. • Gebruikers tekenen een gebruikersovereenkomst voor mobiel werken, waarmee zij verklaren zich bewust te zijn van de gevaren van mobiel werken en verklaren dit veilig te zullen doen. Deze verklaring heeft betrekking op alle mobiele apparatuur die de medewerker zakelijk gebruikt. Periodiek wordt getoetst of deze drie aspecten worden nageleefd.

Vertrekpunt in de set (deels): [cryptografie](cryptografie.md) 2.2.1.2; [beheer van bedrijfsmiddelen](beheer-van-bedrijfsmiddelen.md) 2.3.2. Instellingen afdwingen en wissen op afstand; geen MDM-eis en geen gebruikersovereenkomst.

1. [beleidsregel: wie doet wat, hoe vaak, waarmee]

## Bijlage A Normen

De maatregelen uit de BIO 2.0 versie 1.3 die in dit document zijn belegd.

| Maatregel | ISO 27001-control | Bron van de eis | Waar in dit beleid | Control |
|---|---|---|---|---|
| 8.01.01 | ‘User endpoint devices’ | BIO 2.0 | 2.1 | [control] |
| 8.01.02 | ‘User endpoint devices’ | BIO 2.0 | 2.1 | [control] |

## Bijlage B Controleraamwerk

Per eis een control met risico, beheersdoelstelling, beschrijving, eigenaar, frequentie en bewijslast.
Zie het [controleraamwerk fysieke toegang en beveiliging](controls-fysieke-toegang-en-beveiliging.md) als voorbeeld.

| Control | Onderwerp | Eigenaar | Frequentie | Maatregelen |
|---|---|---|---|---|
| [CODE]-001 | [onderwerp] | [eigenaar] | [frequentie] | [n.nn.nn] |
