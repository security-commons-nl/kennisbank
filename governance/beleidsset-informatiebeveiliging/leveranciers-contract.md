# Beleid informatiebeveiliging in contractbeheer

Beleid informatiebeveiliging, BIO 2.0-domein *Leveranciersbeheer - contractbeheer*. Status: concept, vast te stellen door de organisatie zelf.

Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor de looptijd van contracten met
leveranciers die informatie voor de organisatie verwerken. Het regelt hoe de organisatie zicht houdt op haar
leveranciers en hun toeleveranciers, hoe ze jaarlijks beoordeelt of de afspraken worden nagekomen, hoe ze
clouddiensten selecteert en beheert, en wanneer ze een contract beëindigt. Het gaat over de
ISO-beheersmaatregelen 5.21 (voor zover tijdens de looptijd), 5.22 en 5.23.

De eisen vóór het contract (uitvraag, voorwaarden, bewijs, exitregeling) staan in het beleid informatiebeveiliging
bij inkoop.

> **Alleen als: Hoe is je bedrijfsvoering georganiseerd? «Centrumorganisatie die de bedrijfsvoering ook voor anderen doet»**
>
> De organisatie sluit contracten ook namens de deelnemers. Het register en de jaarlijkse beoordeling vermelden
> per contract voor welke deelnemers het geldt, en de deelnemers krijgen de uitkomst van de beoordeling.

## 2. Uitgangspunten

1. Elk contract met een informatiecomponent heeft een contracteigenaar en een proceseigenaar. De
   proceseigenaar is verantwoordelijk voor de beveiligingsrisico's van de dienst.
2. De beoordeling van een leverancier steunt op bewijs: rapporten van onafhankelijke derden, rapportages uit
   het contract en eigen onderzoek. Een gesprek alleen is geen bewijs.
3. De risico's in de keten van toeleveranciers horen bij de risico's van de organisatie zelf.

## 3. Beleidsregels

### 3.1 Register van leveranciers en contracten

- De organisatie houdt een register bij van alle leveranciers en contracten met een informatiecomponent. Per
  contract staat erin: de dienst, de contracteigenaar, de proceseigenaar, het classificatieniveau van de
  informatie, of er een verwerkersovereenkomst is, de belangrijkste toeleveranciers, de datum van de laatste
  beoordeling en de einddatum. [5.22.02]
- Een nieuw contract staat binnen een maand na ondertekening in het register. Een beëindigd contract blijft
  erin staan tot de exit is afgerond en de leverancier de verwijdering van gegevens heeft bevestigd. [5.22.02]
- Het register staat in **[register leveranciers]**. [5.22.02]

### 3.2 Jaarlijkse beoordeling van de leverancier

- De proceseigenaar beoordeelt elk jaar of de leverancier aan de afgesproken beveiligingseisen voldoet. Hij
  gebruikt daarvoor het bewijs dat de leverancier volgens het contract aanlevert (zie het beleid
  informatiebeveiliging bij inkoop) en de rapportages uit de looptijd. [5.22.01]
- De beoordeling stelt de beveiligingsrisico's vast, bijvoorbeeld een voorbehoud in het rapport, een
  verlopen certificaat of een reikwijdte die de dienst niet meer dekt. De proceseigenaar laat maatregelen
  nemen, door de leverancier of door de organisatie zelf, of accepteert een restrisico en legt dat vast. [5.22.01]
- De CISO adviseert over de beoordeling. Bij een contract voor een kritiek proces of met vertrouwelijke
  informatie is dat advies verplicht. [5.22.01]
- De beoordeling volgt een vast format:
  **[format leveranciersbeoordeling]**. [5.22.01]

> **Alleen als: Wie beheert je IT? «Regie: eigen organisatie stuurt, beheer is uitbesteed» of «Volledig uitbesteed»**
>
> - Bij beheer- en hostingpartijen bespreekt de regieorganisatie de beveiligingsrapportage ten minste elk
>   kwartaal in het reguliere leveranciersoverleg: incidenten, kwetsbaarheden, patchstand, wijzigingen en
>   back-uptests. De verslagen zijn bewijs bij de jaarlijkse beoordeling. [5.22.01]

> **Alleen als: Wie beheert je IT? «Eigen beheer»**
>
> - Bij eigen beheer zijn de meeste contracten licentie- en ondersteuningscontracten. Daarvoor volstaat een
>   lichtere jaarlijkse beoordeling: geldigheid van het bewijs, ondersteuningstermijn van de software en de
>   meldingen van de leverancier over kwetsbaarheden. [5.22.01]

### 3.3 Keten van toeleveranciers

- Het contract verplicht de leverancier om de beveiligingseisen ook op zijn toeleveranciers toe te passen.
  Laat hij een eis voor een toeleverancier vallen omdat die eis voor diens rol niet relevant is, dan meldt hij
  dat met een onderbouwing. De proceseigenaar beoordeelt die onderbouwing bij de jaarlijkse beoordeling. [5.21.03]
- De leverancier meldt tijdens de looptijd elke wijziging in de keten van toeleveranciers die de dienst
  raakt, met de risico's die hij erin ziet. Ook kwetsbaarheden en incidenten bij een toeleverancier die de
  dienst kunnen raken, meldt hij. [5.21.04]
- Bij een melding over de keten beoordeelt de CISO binnen
  **[beoordelingstermijn ketenwijziging]**
  of de risico's acceptabel zijn. De proceseigenaar besluit en legt dat vast. [5.21.04]
- De risicoanalyse van de organisatie neemt de toeleveringsketen mee. Per directe leverancier van een
  kritieke dienst gaat het over de bekende kwetsbaarheden van de leverancier en zijn producten, de kwaliteit
  van zijn producten en de beveiligingspraktijk van zijn eigen leveranciers, inclusief hun manier van veilig
  ontwikkelen. De analyse wordt jaarlijks bijgewerkt. [5.21.05]

> **Alleen als: Op welke landelijke voorzieningen ben je aangesloten? «DigiD» of «Suwinet» of «BRP (als bronhouder of afnemer)» of «Andere ketens met eigen beveiligingseisen»**
>
> - Bij leveranciers van diensten voor een landelijke voorziening (zoals DigiD, Suwinet of de BRP) regelt het
>   contract dat de leverancier meewerkt aan de audits van dat stelsel en de rapporten op tijd levert. De
>   jaarlijkse beoordeling toetst ook of de leverancier aan de eisen van het stelsel voldoet. [5.22.01]
> - De keten van toeleveranciers voor die diensten staat apart in het register, omdat het stelsel eigen
>   voorwaarden stelt aan locatie en uitbesteding. [5.22.02]

### 3.4 Clouddiensten

- De organisatie past een vaste werkwijze toe voor clouddiensten. Die beschrijft hoe de organisatie
  clouddiensten inventariseert, classificeert op de informatie die ze verwerken, selecteert, beoordeelt en
  beheert, en hoe ze de dienst beëindigt. Deze paragraaf en het beleid informatiebeveiliging bij inkoop zijn
  samen dat beleid. [5.23.01]
- Inventariseren: elke clouddienst staat in het register, ook gratis diensten en diensten die een afdeling
  zelf afneemt. Een clouddienst die niet in het register staat, wordt gemeld bij de CISO. [5.23.01]
- Selecteren en beoordelen: welke informatie in welke soort clouddienst mag, volgt uit het
  classificatiebeleid. De jaarlijkse beoordeling geldt ook voor clouddiensten. [5.23.01]
- Beëindigen: elk cloudcontract noemt de situaties waarin de organisatie het contract kan ontbinden,
  bijvoorbeeld een ernstig of herhaald beveiligingsincident, verplaatsing van gegevens naar een land buiten de
  afspraken, overname van de leverancier of het niet leveren van het bewijs. [5.23.01]
- Bij een belangrijke wijziging bij de leverancier, zoals een overname, een nieuwe verwerkingslocatie of een
  ingrijpende wijziging van de dienst, beoordeelt de proceseigenaar met de CISO de risico's en neemt passende
  maatregelen, tot en met het uitvoeren van de exitregeling. [5.23.01]
- De CISO herziet deze werkwijze ten minste eens per drie jaar. [5.23.01]

### 3.5 Beëindigen van een contract

- Bij het einde van een contract voert de contracteigenaar de exitregeling uit: gegevens terug, overdracht aan
  de opvolger, intrekken van alle toegang van de leverancier en een schriftelijke bevestiging van de
  verwijdering van gegevens.

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| Proceseigenaar | Jaarlijkse beoordeling, besluit over restrisico's en wijzigingen in de keten |
| **[contracteigenaar]** | Register, rapportages van de leverancier, uitvoering van de exit |
| **[lijneigenaar leveranciersmanagement]** | Werkwijze, format en planning van de beoordelingen |
| CISO | Advies bij beoordelingen en ketenwijzigingen, herziening van de werkwijze voor clouddiensten |
| Privacy officer of FG | Toezicht op verwerkersovereenkomsten en meldingen van datalekken door leveranciers |

## 5. Naleving en bewaking

- Elk kwartaal: controle of nieuwe en beëindigde contracten in het register staan; bewijs is de vergelijking
  met de contractadministratie van inkoop.
- Jaarlijks: overzicht van de leveranciersbeoordelingen van dat jaar, met de leveranciers waarvoor de
  beoordeling ontbreekt of te laat is; bewijs is het overzicht met de afhandeling.
- Jaarlijks: steekproef op de kwaliteit van ten minste
  **[aantal steekproef beoordelingen]**;
  bewijs is het verslag van de steekproef.
- Eens per drie jaar: herziening van de werkwijze voor clouddiensten, met vaststelling door de directie.
- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid en volgt op het beleid
informatiebeveiliging bij inkoop. Het raakt het classificatiebeleid (welke informatie waar mag), het
incidentbeleid (meldingen van leveranciers), het beleid kwetsbaarheden en patchmanagement, het
continuïteitsbeleid (exit en afhankelijkheid) en het privacybeleid (verwerkersovereenkomsten).

## Bijlage: BIO 2.0-maatregelen

De overheidsmaatregelen van dit domein (6) en waar dit stuk ze invult. Nummers volgens BIO2 v1.3 definitief - 9 januari 2026; de tekst van de maatregel staat bij het CIP.

| Maatregel | Titel | In dit stuk |
|---|---|---|
| 5.21.03 | Beheren van informatiebeveiliging in de ICT-toeleveringsketen | 3.3 Keten van toeleveranciers |
| 5.21.04 | Beheren van informatiebeveiliging in de ICT-toeleveringsketen | 3.3 Keten van toeleveranciers |
| 5.21.05 | Beheren van informatiebeveiliging in de ICT-toeleveringsketen | 3.3 Keten van toeleveranciers |
| 5.22.01 | Monitoren, beoordelen en het beheren van wijzigingen van leveranciersdiensten | 3.2 Jaarlijkse beoordeling van de leverancier |
| 5.22.02 | Monitoren, beoordelen en het beheren van wijzigingen van leveranciersdiensten | 3.1 Register van leveranciers en contracten |
| 5.23.01 | Informatiebeveiliging voor het gebruik van clouddiensten | 3.4 Clouddiensten |

## Nog in te vullen

- **register leveranciers**: de plaats of het systeem waar het register wordt bijgehouden
- **format leveranciersbeoordeling**: het sjabloon met de vragen en het bewijs per vraag
- **beoordelingstermijn ketenwijziging**: bijvoorbeeld tien werkdagen
- **contracteigenaar**: de functie die het contract beheert
- **lijneigenaar leveranciersmanagement**: de manager die het contractmanagement uitvoert
- **aantal steekproef beoordelingen**: bijvoorbeeld drie beoordelingen van kritieke diensten
