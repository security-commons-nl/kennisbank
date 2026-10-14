# Beleid wijzigingsbeheer

Beleid informatiebeveiliging, BIO 2.0-domein *Wijzigingsbeheer*. Status: concept, vast te stellen door de organisatie zelf.

Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor wijzigingen in informatiesystemen,
infrastructuur, software en configuratie in de productieomgeving. Het regelt hoe een wijziging wordt
aangevraagd, beoordeeld, getest, goedgekeurd en doorgevoerd, hoe omgevingen gescheiden zijn en wie software
mag installeren. Het geldt voor de eigen IT-organisatie, functioneel beheer en leveranciers die wijzigingen
doorvoeren op systemen van de organisatie. Het gaat over de ISO-beheersmaatregelen 5.37, 8.19, 8.29, 8.31,
8.32 en 8.33.

Buiten dit beleid vallen de eisen aan het bouwen van software (beleid veilige softwareontwikkeling) en het
installeren van beveiligingsupdates binnen de termijnen voor kwetsbaarheden (beleid vulnerability- en
patchmanagement); die updates lopen wel via dit proces, als standaardwijziging.

> **Alleen als: Wie beheert je IT? «Regie: eigen organisatie stuurt, beheer is uitbesteed»**
>
> De organisatie stuurt, een leverancier voert het beheer uit. Het wijzigingsproces van de leverancier
> is leidend voor de uitvoering; de organisatie houdt de goedkeuring van wijzigingen met gevolgen voor haar
> processen of informatie, en legt dit beleid als eis in het contract.

> **Alleen als: Wie beheert je IT? «Volledig uitbesteed»**
>
> Het beheer is volledig uitbesteed. De leverancier voert wijzigingsbeheer uit volgens dit beleid, zoals
> vastgelegd in het contract. De organisatie keurt wijzigingen goed die haar processen of informatie
> raken en ontvangt elke maand een overzicht van alle doorgevoerde wijzigingen.

## 2. Uitgangspunten

1. Elke wijziging in productie is vastgelegd, beoordeeld en goedgekeurd voordat hij wordt doorgevoerd.
   Spoedwijzigingen worden achteraf binnen vijf werkdagen beoordeeld.
2. Er wordt niet getest in productie.
3. Elke wijziging heeft een weg terug.
4. Hoe groter het risico van een wijziging, hoe zwaarder de beoordeling en de goedkeuring.

## 3. Beleidsregels

### 3.1 Het wijzigingsproces

- De organisatie richt wijzigingsbeheer in volgens een algemeen geaccepteerd beheerraamwerk, bijvoorbeeld
  ITIL of ISO/IEC 20000 voor technisch beheer en BiSL voor functioneel beheer, en legt vast welk raamwerk
  geldt. [8.32.02]
- Elke wijziging staat in het wijzigingsregister met: omschrijving, aanvrager, betrokken systemen,
  risicoklasse, testplan en testresultaten, besluit en datum van doorvoeren. [8.32.01]
- Elke wijziging krijgt een risicoafweging van de mogelijke gevolgen voor beschikbaarheid, integriteit en
  vertrouwelijkheid, inclusief een beschreven plan om terug te gaan naar de vorige situatie (rollback).
  [8.32.01]
- Wijzigingen vallen in drie soorten, elk met een eigen goedkeuring: [8.32.01]
  - standaardwijzigingen: vooraf beoordeelde, terugkerende wijzigingen met laag risico (zoals reguliere
    updates), goedgekeurd als type en uitgevoerd volgens een vast draaiboek;
  - normale wijzigingen: beoordeeld en goedgekeurd door het wijzigingsoverleg (change advisory board), met
    de systeemeigenaar en, bij een hoog risico of informatie met classificatie hoog, advies van de CISO;
  - spoedwijzigingen: goedgekeurd door
    **[spoedgoedkeurder]**
    en achteraf in het eerstvolgende wijzigingsoverleg beoordeeld.
- Na het doorvoeren controleert de uitvoerder of de wijziging werkt zoals bedoeld en sluit hij de
  wijziging pas af na die controle. Een mislukte wijziging wordt teruggedraaid volgens het rollbackplan. [8.32.01]
- Wijzigingen door leveranciers op systemen van de organisatie lopen via hetzelfde register en dezelfde
  goedkeuring, ook als de leverancier eigen accounts gebruikt. [8.32.01]

> **Alleen als: Wie beheert je IT? «Eigen beheer»**
>
> - Het wijzigingsoverleg komt ten minste wekelijks bijeen, onder voorzitterschap van de wijzigingsmanager van
>   de eigen IT-afdeling. De uitvoerder van een wijziging keurt zijn eigen wijziging niet goed. [8.32.01]

> **Alleen als: Wie beheert je IT? «Regie: eigen organisatie stuurt, beheer is uitbesteed» of «Volledig uitbesteed»**
>
> - In het contract staat welke wijzigingen de leverancier zelf mag goedkeuren (standaardwijzigingen) en welke
>   de organisatie vooraf goedkeurt. De organisatie heeft een vaste vertegenwoordiger in het wijzigingsoverleg
>   van de leverancier. Het wijzigingsregister van de leverancier is voor de organisatie in te zien. [8.32.01, 8.32.02]

### 3.2 Bedieningsprocedures

- Voor terugkerende beheertaken (starten en stoppen van systemen, back-up en herstel, standaardwijzigingen,
  afhandelen van storingen) zijn werkinstructies vastgelegd. Ze zijn beschikbaar voor wie ze nodig heeft en
  worden na elke relevante wijziging bijgewerkt. [5.37.01]

### 3.3 Software installeren

- Gebruikers hebben geen lokale beheerrechten op hun werkplek. Software komt alleen op werkplekken en
  servers via de softwarecatalogus of een goedgekeurde wijziging. [8.19.01]
- De organisatie houdt een lijst bij van toegestane software. Het installeren of uitvoeren van software buiten
  die lijst wordt technisch tegengehouden, bijvoorbeeld met applicatiewhitelisting, of minstens gedetecteerd
  en binnen
  **[termijn verwijderen software]**
  verwijderd. [8.19.01]
- Een verzoek om nieuwe software wordt getoetst op leverancier, licentie, beveiliging en privacy voordat de
  software in de catalogus komt. [8.19.01]

### 3.4 Scheiding van omgevingen

- Ontwikkeling, test, acceptatie en productie zijn gescheiden omgevingen. Voor een systeem zonder eigen
  test- of acceptatieomgeving legt de systeemeigenaar vast hoe wijzigingen wel vooraf worden getest. [8.31.01]
- In de productieomgeving wordt niet getest. Is een test in productie onvermijdelijk, dan keurt de
  proceseigenaar die vooraf schriftelijk goed, met de omvang, het tijdvak en de maatregelen om schade te
  voorkomen. [8.31.01]
- Significante wijzigingen worden getest in een omgeving buiten productie voordat ze in productie gaan.
  Afwijken kan alleen met voorafgaande goedkeuring van de proceseigenaar, die het risico vastlegt. [8.31.02]
- Testgegevens volgen de regels in het beleid veilige softwareontwikkeling: fictieve gegevens, en
  persoonsgegevens alleen als onderbouwde uitzondering met advies van de privacy officer en de CISO. [8.33.01]

### 3.5 Testen en acceptatie

- Acceptatietesten volgen een vaste testmethode: een testplan met testgevallen afgeleid van de functionele
  eisen en de beveiligingseisen, uitgevoerd door of namens de systeemeigenaar. [8.29.01]
- Tests die vaker terugkomen (regressietests, controles op beveiligingsinstellingen) worden waar het kan
  geautomatiseerd. [8.29.01]
- Van elke acceptatietest wordt een verslag gemaakt met de uitgevoerde tests, de resultaten, de openstaande
  bevindingen en het besluit tot acceptatie. Het verslag hoort bij de wijziging in het register. [8.29.01]

> **Alleen als: Bouwt je organisatie zelf software, apps of koppelingen? «Ja»**
>
> - Voor eigen software voert de bouwstraat bij elke wijziging automatisch unit-, integratie- en
>   beveiligingstests uit. Uitrol naar productie gebeurt alleen via de bouwstraat, na goedkeuring in het
>   wijzigingsregister; ontwikkelaars hebben geen schrijfrechten in productie. [8.29.01, 8.31.01, 8.32.01]

> **Alleen als: Bouwt je organisatie zelf software, apps of koppelingen? «Nee, alleen inkoop en configuratie»**
>
> - Bij een nieuwe versie van een leverancier test de organisatie zelf in de acceptatieomgeving de eigen
>   processen, koppelingen en autorisaties, naast het testverslag van de leverancier. [8.29.01, 8.31.02]

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| **[lijneigenaar wijzigingsbeheer]** | Uitvoering van dit beleid en het wijzigingsproces |
| Wijzigingsmanager | Het wijzigingsregister, het wijzigingsoverleg en de rapportage |
| Systeemeigenaar | Beoordeling van wijzigingen op zijn systeem, acceptatietests |
| Proceseigenaar | Goedkeuring van afwijkingen: testen in productie of niet vooraf testen |
| CISO | Advies bij wijzigingen met een hoog risico, toetsing van dit beleid |
| Leveranciers | Wijzigingen aanmelden en doorvoeren volgens dit beleid |

## 5. Naleving en bewaking

- Maandelijks: rapportage over het aantal wijzigingen per soort, mislukte en teruggedraaide wijzigingen en
  spoedwijzigingen; bewijs is de rapportage aan de lijneigenaar.
- Elk kwartaal: steekproef van wijzigingen op volledigheid van risicoafweging, rollbackplan, testverslag en
  goedkeuring.
- Elk kwartaal: vergelijking van de geïnstalleerde software met de lijst van toegestane software.
- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid veilige
softwareontwikkeling (testgegevens en bouwstraat), het beleid vulnerability- en patchmanagement (updates als
standaardwijziging), het beleid leveranciersbeheer (afspraken over wijzigingen door leveranciers) en het
beleid logische toegangsbeveiliging (rechten in productie).

## Bijlage: BIO 2.0-maatregelen

De overheidsmaatregelen van dit domein (6) en waar dit stuk ze invult. Nummers volgens BIO2 v1.3 definitief - 9 januari 2026; de tekst van de maatregel staat bij het CIP.

| Maatregel | Titel | In dit stuk |
|---|---|---|
| 8.19.01 | Installeren van software op operationele systemen | 3.3 Software installeren |
| 8.29.01 | Testen van de beveiliging tijdens ontwikkeling en acceptatie | 3.5 Testen en acceptatie |
| 8.31.01 | Scheiding van ontwikkel-, test- en productieomgevingen | 3.4 Scheiding van omgevingen |
| 8.31.02 | Scheiding van ontwikkel-, test- en productieomgevingen | 3.4 Scheiding van omgevingen |
| 8.32.01 | Wijzigingsbeheer | 3.1 Het wijzigingsproces |
| 8.32.02 | Wijzigingsbeheer | 3.1 Het wijzigingsproces |

Ook ingevuld, ISO-beheersmaatregelen van dit domein zonder overheidsmaatregel: 5.37.01 (Gedocumenteerde bedieningsprocedures), 8.33.01 (Testgegevens).

## Nog in te vullen

- **spoedgoedkeurder**: de functie die buiten het overleg mag goedkeuren, bijvoorbeeld de dienstdoende IT-manager
- **termijn verwijderen software**: bijvoorbeeld vijf werkdagen
- **lijneigenaar wijzigingsbeheer**: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd IT
