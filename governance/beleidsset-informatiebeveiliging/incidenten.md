# Beleid beveiligingsincidenten

Beleid informatiebeveiliging, BIO 2.0-domein *Security Incident Management*. Status: concept, vast te stellen door de organisatie zelf.

Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor het melden, beoordelen, afhandelen en
leren van informatiebeveiligingsincidenten. Het doel is dat een incident snel bij de juiste mensen ligt, dat
de schade beperkt blijft, dat wettelijke meldingen op tijd gebeuren en dat hetzelfde incident niet opnieuw
voorkomt. Het gaat over de ISO-beheersmaatregelen 5.24 tot en met 5.28 en 6.08.

Het beleid geldt voor iedereen die voor de organisatie werkt: medewerkers, inhuur, stagiairs en leveranciers
die met informatie of systemen van de organisatie werken. Een datalek onder de AVG is ook een
informatiebeveiligingsincident; de melding aan de Autoriteit Persoonsgegevens en aan betrokkenen loopt via
dezelfde procedure, met de privacy officer en de FG als vaste deelnemers.

Buiten dit beleid vallen het verzamelen en bewaren van logbestanden (beleid logging en monitoring) en het
oplossen van technische kwetsbaarheden die geen incident zijn (beleid kwetsbaarheden en patchmanagement).

## 2. Uitgangspunten

1. Elke medewerker meldt een vermoed incident direct. Twijfel is geen reden om te wachten; een melding die
   achteraf geen incident blijkt, kost weinig.
2. Er is één meldloket en één incidentprocedure voor beveiligingsincidenten en datalekken.
3. De proceseigenaar is eigenaar van het incident in zijn proces; de CISO coördineert en adviseert.
4. Wettelijke meldtermijnen gaan vóór interne afstemming. Een melding die later moet worden aangevuld, is
   beter dan een te late melding.

## 3. Beleidsregels

### 3.1 Meldloket en meldprocedure

- Medewerkers en externen melden een vermoed incident bij
  **[meldloket incidenten]**.
  Het loket is tijdens kantoortijd bereikbaar en heeft daarbuiten een bereikbaarheidsregeling. Elke melding
  krijgt een registratienummer. [5.24.01]
- De meldprocedure beschrijft wat het loket doet: registreren, eerste beoordeling, doorzetten naar de CISO
  of de privacy officer, en terugkoppelen aan de melder. De procedure noemt per stap de rol en de termijn.
  Een intern gemeld incident ligt binnen 24 uur bij de CISO. [5.24.02]
- Iedere nieuwe medewerker en iedere externe met een account krijgt de meldprocedure bij indiensttreding
  en bevestigt dat hij die kent. Jaarlijks komt de procedure terug in de bewustwordingscampagne. De
  bevestiging wordt geregistreerd. [6.08.01]

### 3.2 Beoordelen en classificeren

- De CISO, of bij afwezigheid de vervanger, beoordeelt elke melding: is dit een incident, welke categorie
  en welke ernst. De indeling in categorieën en ernstniveaus staat in de incidentprocedure en sluit aan op
  de classificatie van informatie.
- Bij elk incident beoordeelt de privacy officer of er persoonsgegevens zijn geraakt. Zo ja, dan volgt de
  beoordeling of het een meldplichtig datalek is.

> **Alleen als: Welke eigen security-capaciteit heb je? «Geen eigen ISO; informatiebeveiliging is een neventaak»**
>
> - Er is geen eigen ISO. De beoordeling ligt bij
>   **[incidentcoördinator]**, die voor de
>   technische analyse een externe partij inschakelt waarmee vooraf een raamafspraak is gemaakt, met een
>   afgesproken reactietijd.

> **Alleen als: Welke eigen security-capaciteit heb je? «Een ISO of CISO in deeltijd»**
>
> - De ISO of CISO coördineert de afhandeling. Voor forensisch onderzoek en voor incidenten buiten
>   kantoortijd is een externe incidentrespons-partij gecontracteerd, met een afgesproken reactietijd.

> **Alleen als: Welke eigen security-capaciteit heb je? «Een eigen team (CISO met ISO's)»**
>
> - Het securityteam heeft een bereikbaarheidsdienst buiten kantoortijd en een vaste incidentrespons-rol
>   per dienst. Voor forensisch onderzoek dat het team niet zelf kan doen, is een externe partij
>   gecontracteerd.

### 3.3 Detectie en escalatie

> **Alleen als: Wie bewaakt je omgeving op aanvallen? «Eigen SOC»**
>
> - Het eigen SOC beoordeelt meldingen uit de detectievoorzieningen en werkt met vastgelegde
>   draaiboeken. Het SOC mag zelf een systeem of account isoleren als het draaiboek dat toelaat, en meldt
>   dat direct aan de CISO.

> **Alleen als: Wie bewaakt je omgeving op aanvallen? «Uitbesteed SOC of MDR-dienst»**
>
> - De SOC- of MDR-dienstverlener escaleert volgens het contract: per ernstniveau de termijn, het kanaal en
>   de contactpersoon bij de organisatie, ook buiten kantoortijd. Het contract regelt welke ingrepen de
>   dienstverlener zelf mag doen (zoals een apparaat isoleren) en welke toestemming vragen.
> - De organisatie toetst de escalatieketen elk jaar met een test-alarm.

> **Alleen als: Wie bewaakt je omgeving op aanvallen? «Geen structurele detectie»**
>
> - Er is geen structurele detectie. Incidenten komen binnen via medewerkers, leveranciers, waarschuwingen
>   van de sectorale CERT en meldingen van buiten. Het ontbreken van detectie staat als risico in het
>   risicoregister, met een besluit van de directie over de aanpak.

### 3.4 Afhandelen

- Incidenten worden afgehandeld via het incidentbeheerproces. De proceseigenaar is verantwoordelijk voor
  het oplossen van het incident in zijn proces en wijst daarvoor een behandelaar aan. [5.24.03, 5.26.02]
- De incidentprocedure verwijst naar de procedure voor crisisbeheersing en zegt wanneer een incident
  overgaat naar crisisbeheersing: bij langdurige uitval van kritieke processen, bij een groot datalek of
  bij een aanval met losgeld. [5.24.05]

> **Alleen als: Hoe is je crisis- en continuïteitsorganisatie geregeld? «Geen»**
>
> - De organisatie heeft geen vaste crisisorganisatie. Bij een incident dat de grens voor crisis haalt,
>   roept de CISO **[eindverantwoordelijke bedrijfsvoering]**
>   op, die een ad-hoc crisisteam samenstelt. Het opzetten van een crisisprocedure staat als actie in het
>   jaarplan informatiebeveiliging.

> **Alleen als: Hoe is je crisis- en continuïteitsorganisatie geregeld? «Een crisisteam, zonder BCM-functie» of «Een BCM-functie met continuïteitsplannen en een BIA»**
>
> - Het crisisteam neemt het incident over volgens de crisisprocedure; de CISO schuift aan als adviseur.

> **Alleen als: Hoe is je crisis- en continuïteitsorganisatie geregeld? «Een BCM-functie met continuïteitsplannen en een BIA»**
>
> - Bij uitval van een kritiek proces start de proceseigenaar het continuïteitsplan van dat proces. De
>   hersteltijden uit de BIA bepalen de volgorde van herstel.

- De proceseigenaar rapporteert maandelijks de stand van de incidenten in zijn proces: wat is open, wat is
  opgelost, welke maatregelen lopen nog. De CISO bundelt dit tot een maandrapport voor
  **[eindverantwoordelijke bedrijfsvoering]**. [5.24.04]

### 3.5 Melden aan externe partijen

- De incidentprocedure regelt de meldingen buiten de organisatie, elk met eigen termijn en eigenaar:
  het CSIRT en de toezichthouder volgens de Cyberbeveiligingswet waar die van toepassing is, de Autoriteit
  Persoonsgegevens bij een meldplichtig datalek (binnen 72 uur na ontdekking), de politie bij een strafbaar
  feit, en betrokkenen als het incident hun rechten of belangen raakt. [5.24.07, 5.26.02, 5.27.01]
- Meldingen en waarschuwingen die het CSIRT of de sectorale CERT aan de organisatie stuurt, komen binnen
  op een vast adres. De CISO beoordeelt ze binnen één werkdag en neemt ze op in de risicobehandeling,
  bijvoorbeeld als kwetsbaarheid die moet worden verholpen. [5.24.07]
- Betrokkenen worden binnen de wettelijke termijn geïnformeerd. De privacy officer stelt de tekst op, de
  proceseigenaar beslist over verzending. [5.24.07]

> **Alleen als: Wat is je status onder de Cyberbeveiligingswet? «Essentiële entiteit» of «Belangrijke entiteit»**
>
> - De organisatie valt onder de Cyberbeveiligingswet. Een significant incident meldt de CISO aan het
>   aangewezen CSIRT en de toezichthouder in drie stappen: een vroegtijdige waarschuwing binnen 24 uur na
>   kennisname, een incidentmelding binnen 72 uur en een eindrapport binnen een maand. De incidentprocedure
>   legt vast wat significant is en wie de melding mag doen als de CISO afwezig is. [5.24.07, 5.26.02]
> - Waar een significant incident de dienstverlening aan afnemers kan raken, informeert de organisatie die
>   afnemers zonder onnodige vertraging, met de maatregelen die zij zelf kunnen nemen. [5.24.07]
> - De bestuurders worden bij elk significant incident direct geïnformeerd; zij zijn persoonlijk
>   verantwoordelijk voor het toezicht op het risicobeheer onder de wet.

> **Alleen als: Wat is je status onder de Cyberbeveiligingswet? «Essentiële entiteit»**
>
> - Als essentiële entiteit staat de organisatie onder proactief toezicht. Het incidentregister en de
>   meldingen zijn op verzoek van de toezichthouder direct beschikbaar.

> **Alleen als: Wat is je status onder de Cyberbeveiligingswet? «Niet aangewezen»**
>
> - De organisatie is niet aangewezen onder de Cyberbeveiligingswet. Zij meldt ernstige incidenten
>   vrijwillig aan de sectorale CERT, zodat andere overheden gewaarschuwd kunnen worden. [5.24.07]

### 3.6 Coordinated Vulnerability Disclosure

- De organisatie heeft een CVD-procedure volgens de NCSC-leidraad, gepubliceerd op de website met een
  meldadres en een security.txt-bestand. De procedure noemt de reactietermijn, de afspraken over openbaar
  maken en de voorwaarden waaronder de organisatie geen aangifte doet. [5.24.08]
- Een CVD-melding wordt geregistreerd als beveiligingsmelding. De meldingen en hun afhandeling zijn
  onderdeel van het maandrapport incidenten. [5.24.08]

### 3.7 Bewijs verzamelen en bewaren

- Bij een vermoed incident wordt eerst bewijs veiliggesteld, daarna pas hersteld, tenzij de schade dat
  niet toelaat. Wie bewijs verzamelt, legt vast wat, wanneer, door wie en waar het is opgeslagen.
- Bij een mogelijk strafbaar feit of een mogelijke juridische procedure laat de CISO het veiligstellen
  doen door een forensisch onderzoeker.
- Het incidentdossier bevat de melding, de analyse, de gebruikte logging, de genomen maatregelen en het
  advies. Het dossier wordt ten minste drie jaar na afsluiting bewaard, ook als het vermoeden ongegrond
  bleek. [5.28.01]

### 3.8 Leren van incidenten

- Na elk incident met ernst hoog of kritiek, en na elk meldplichtig datalek, volgt binnen een maand een
  evaluatie: oorzaak, wat werkte, wat niet, en welke maatregelen nodig zijn. Verbetermaatregelen krijgen
  een eigenaar en een datum en gaan naar het risicoregister. [5.27.02]
- De CISO analyseert elk kwartaal alle incidenten samen op patronen en herhalingen en neemt de uitkomst op
  in de rapportage aan de directie. [5.27.02]
- Lessen die voor andere overheden waardevol zijn, deelt de organisatie geanonimiseerd met de sectorale
  CERT of samenwerkingspartners.

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| **[eindverantwoordelijke bedrijfsvoering]** | Ontvangst van het maandrapport, besluit over escalatie naar crisisbeheersing |
| Proceseigenaar | Oplossen van incidenten in het eigen proces, maandelijkse rapportage, uitvoeren van verbetermaatregelen |
| CISO | Beoordeling, coördinatie, externe meldingen, CVD-procedure, evaluaties en kwartaalanalyse |
| Privacy officer en FG | Beoordeling datalekken, melding aan de Autoriteit Persoonsgegevens, informeren van betrokkenen (FG adviseert en houdt toezicht) |
| **[meldloket incidenten]** | Registratie, eerste beoordeling, doorzetten en terugkoppelen |
| Medewerkers en externen | Direct melden van een vermoed incident en meewerken aan het onderzoek |

## 5. Naleving en bewaking

- Maandelijks: maandrapport incidenten met CVD-meldingen aan de eindverantwoordelijke bedrijfsvoering;
  bewijs is het rapport en de verzendregistratie.
- Per kwartaal: analyse op patronen; bewijs is de rapportage aan de directie.
- Jaarlijks: steekproef van tien incidenten op volledigheid van het dossier, tijdigheid van de interne en
  externe meldingen en opvolging van de verbetermaatregelen.
- Jaarlijks: controle dat alle medewerkers en externen met een account de meldprocedure hebben bevestigd,
  door de registratie te vergelijken met de lijst van actieve accounts.
- Jaarlijks: een oefening met een incidentscenario, inclusief de overgang naar crisisbeheersing en het
  opstellen van een externe melding; bewijs is het oefenverslag met verbeterpunten.
- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid logging en
monitoring (detectie en bewijs), het beleid kwetsbaarheden en patchmanagement (opvolging van
CERT-waarschuwingen en CVD-meldingen), het continuïteitsbeleid (crisisbeheersing en herstel), het
privacybeleid (datalekken) en het beleid leveranciersbeheer (meldplicht van leveranciers).

## Bijlage: BIO 2.0-maatregelen

De overheidsmaatregelen van dit domein (12) en waar dit stuk ze invult. Nummers volgens BIO2 v1.3 definitief - 9 januari 2026; de tekst van de maatregel staat bij het CIP.

| Maatregel | Titel | In dit stuk |
|---|---|---|
| 5.24.01 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | 3.1 Meldloket en meldprocedure |
| 5.24.02 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | 3.1 Meldloket en meldprocedure |
| 5.24.03 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | 3.4 Afhandelen |
| 5.24.04 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | 3.4 Afhandelen |
| 5.24.05 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | 3.4 Afhandelen |
| 5.24.07 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | 3.5 Melden aan externe partijen |
| 5.24.08 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | 3.6 Coordinated Vulnerability Disclosure |
| 5.26.02 | Reageren op informatiebeveiligings-incidenten | 3.4 Afhandelen |
| 5.27.01 | Leren van informatiebeveiligingsincidenten | 3.5 Melden aan externe partijen |
| 5.27.02 | Leren van informatiebeveiligingsincidenten | 3.8 Leren van incidenten |
| 5.28.01 | Verzamelen van bewijsmateriaal | 3.7 Bewijs verzamelen en bewaren |
| 6.08.01 | Melden van informatiebeveiligings-gebeurtenissen | 3.1 Meldloket en meldprocedure |

## Nog in te vullen

- **meldloket incidenten**: het loket, bijvoorbeeld de servicedesk, met telefoonnummer en mailadres
- **incidentcoördinator**: de functionaris die informatiebeveiliging als neventaak heeft
- **eindverantwoordelijke bedrijfsvoering**: de functie, bijvoorbeeld de secretaris of directeur
