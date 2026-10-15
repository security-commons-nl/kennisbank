# Beleid beveiligingsincidenten

Word nodig? Kies dit stuk in de [generator](beleidsset-generator.html) en download het daar, zonder of met je eigen antwoorden.

| | |
|---|---|
| Documenttype | Beleid informatiebeveiliging onder het strategisch informatiebeveiligingsbeleid; BIO 2.0-domein *Security Incident Management* |
| Status | Concept, vast te stellen door de organisatie |
| Eigenaar | **[eigenaar van dit beleid]** |
| Vaststeller | **[vaststeller]** |
| Evaluatie | Jaarlijks, in de plan-do-check-act-cyclus van het managementsysteem voor informatiebeveiliging |

**In het kort.** Over het melden, beoordelen, afhandelen en leren van beveiligingsincidenten en datalekken. Behandelt het meldloket, de classificatie, detectie en escalatie, de afhandeling, meldingen aan externe partijen, coordinated vulnerability disclosure, het veiligstellen van bewijs en de evaluatie achteraf.

**Onderwerpen.** 3. Meldloket en meldprocedure; 4. Beoordelen en classificeren; 5. Detectie en escalatie; 6. Afhandelen; 7. Melden aan externe partijen; 8. Coordinated vulnerability disclosure; 9. Bewijs verzamelen en bewaren; 10. Leren van incidenten.

Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor het melden, beoordelen, afhandelen en
leren van informatiebeveiligingsincidenten. Het doel is dat een incident snel bij de juiste mensen ligt, dat
de schade beperkt blijft, dat wettelijke meldingen op tijd gebeuren en dat hetzelfde incident niet opnieuw
voorkomt. Het gaat over de ISO-beheersmaatregelen 5.24 tot en met 5.28 en 6.8.

**Voor wie.** Het beleid is primair bedoeld voor het meldloket, de CISO, de privacy officer en de
proceseigenaren die incidenten in hun proces afhandelen. De meldplicht geldt voor iedereen die voor de
organisatie werkt: medewerkers, inhuur, stagiairs, vrijwilligers en leveranciers die met informatie of
systemen van de organisatie werken.

**Waarop.** Alle gebeurtenissen die de beschikbaarheid, integriteit of vertrouwelijkheid van informatie of
systemen van de organisatie raken of kunnen raken, ongeacht of de informatie op eigen systemen, bij een
leverancier of op papier staat. Een datalek onder de AVG is ook een informatiebeveiligingsincident; de melding
aan de Autoriteit Persoonsgegevens en aan betrokkenen loopt via dezelfde procedure, met de privacy officer en
de FG als vaste deelnemers. Is de detectie, de eerste beoordeling of de incidentrespons uitbesteed,
bijvoorbeeld aan een SOC- of MDR-dienstverlener, dan gelden de eisen uit dit beleid als minimumeis voor die
partij. De organisatie legt dat vast in het contract en toetst de naleving met een onafhankelijke verklaring,
zoals een ISO 27001-certificaat of een ISAE 3402- of ISAE 3000-rapport; het vastleggen loopt via het beleid
informatiebeveiliging bij inkoop, het toetsen via het beleid contractbeheer.

Buiten dit beleid vallen het verzamelen en bewaren van logbestanden (beleid logging en monitoring), het
oplossen van technische kwetsbaarheden die geen incident zijn (beleid kwetsbaarheden en patchmanagement), de
crisisorganisatie zelf en het herstel van kritieke processen (continuïteitsbeleid) en fysieke incidenten voor
zover ze geen informatie raken (beleid fysieke toegang en beveiliging).

## 2. Uitgangspunten

1. Elke medewerker meldt een vermoed incident direct. Twijfel is geen reden om te wachten; een melding die
   achteraf geen incident blijkt, kost weinig.
2. Er is één meldloket en één incidentprocedure voor beveiligingsincidenten en datalekken.
3. De proceseigenaar is eigenaar van het incident in zijn proces; de CISO coördineert en adviseert.
4. Wettelijke meldtermijnen gaan vóór interne afstemming. Een melding die later moet worden aangevuld, is
   beter dan een te late melding.
5. De ernst van een incident volgt het impactniveau van de geraakte informatie en processen (beleid
   informatieclassificatie): verwaarloosbaar, gering, gemiddeld, ernstig, catastrofaal.
6. Termijnen en frequenties in dit beleid die niet uit een wet of uit de BIO 2.0 komen, zijn standaardwaarden.
   De organisatie past ze aan op haar eigen risicoafweging en legt de keuze vast bij de vaststelling van dit beleid.

## 3. Meldloket en meldprocedure

1. Medewerkers en externen melden een vermoed incident direct bij
   **[meldloket incidenten]**.
   Het loket is tijdens kantoortijd bereikbaar en heeft daarbuiten een bereikbaarheidsregeling. Het loket
   registreert elke melding met een registratienummer, datum en tijd. [5.24.01]
2. De CISO is eigenaar van de incidentprocedure. Die beschrijft wat het loket doet: registreren, eerste
   beoordeling, doorzetten naar de CISO of de privacy officer, en terugkoppelen aan de melder. De procedure
   noemt per stap de rol en de termijn, en de CISO stelt haar jaarlijks opnieuw vast. Een intern gemeld incident
   ligt binnen 24 uur bij de CISO. [5.24.02]
3. De CISO zorgt dat de rollen in de incidentprocedure zijn belegd en dat elke rol een vervanger heeft, ook
   buiten kantoortijd. De bezetting staat in de procedure. [5.24.01]
4. Iedere nieuwe medewerker en iedere externe met een account krijgt de meldprocedure bij indiensttreding
   en bevestigt dat hij die kent. De CISO laat de procedure jaarlijks terugkomen in de bewustwordingscampagne.
   **[lijneigenaar personeel]** registreert de
   bevestiging. [6.08.01]
5. Wie een incident meldt, meldt alleen wat hij zelf heeft waargenomen en onderneemt geen eigen onderzoek of
   herstelactie, tenzij het loket of de CISO daarom vraagt. [6.08.01]

## 4. Beoordelen en classificeren

1. De CISO, of bij afwezigheid de vervanger, beoordeelt elke melding binnen één werkdag: is dit een incident,
   welke categorie en welke ernst. De CISO legt het besluit met de onderbouwing vast bij de melding; een
   melding die geen incident is, krijgt dat oordeel ook. [5.25.02]
2. De indeling in categorieën en ernstniveaus staat in de incidentprocedure en volgt de impactniveaus van het
   beleid informatieclassificatie. Per ernstniveau staat erbij wie wordt geïnformeerd, binnen welke termijn
   en of het incident naar crisisbeheersing gaat. [5.25.02]
3. Bij elk incident beoordeelt de privacy officer binnen één werkdag of er persoonsgegevens zijn geraakt. Zo
   ja, dan volgt de beoordeling of het een meldplichtig datalek is, vastgelegd in het incidentdossier.
   [5.25.02]

> **Alleen als: Welke eigen security-capaciteit heb je? «Geen eigen ISO; informatiebeveiliging is een neventaak»**
>
> 4. Er is geen eigen security officer. De beoordeling ligt bij
>    **[incidentcoördinator]**, die voor de
>    technische analyse een externe partij inschakelt waarmee vooraf een raamafspraak is gemaakt, met een
>    afgesproken reactietijd. [5.24.01, 5.25.02]

> **Alleen als: Welke eigen security-capaciteit heb je? «Een ISO of CISO in deeltijd»**
>
> 5. De CISO coördineert de afhandeling. Voor forensisch onderzoek en voor incidenten buiten kantoortijd is een
>    externe incidentrespons-partij gecontracteerd, met een afgesproken reactietijd. [5.24.01]

> **Alleen als: Welke eigen security-capaciteit heb je? «Een eigen team (CISO met ISO's)»**
>
> 6. Het securityteam heeft een bereikbaarheidsdienst buiten kantoortijd en een vaste incidentrespons-rol
>    per dienst. Voor forensisch onderzoek dat het team niet zelf kan doen, is een externe partij
>    gecontracteerd. [5.24.01]

## 5. Detectie en escalatie

> **Alleen als: Wie bewaakt je omgeving op aanvallen? «Eigen SOC»**
>
> 1. Het eigen SOC beoordeelt meldingen uit de detectievoorzieningen binnen de termijn per ernstniveau uit de
>    incidentprocedure en werkt met vastgelegde draaiboeken. Het SOC mag zelf een systeem of account isoleren
>    als het draaiboek dat toelaat, en meldt dat direct aan de CISO. [5.24.03, 5.25.02]

> **Alleen als: Wie bewaakt je omgeving op aanvallen? «Uitbesteed SOC of MDR-dienst»**
>
> 2. De SOC- of MDR-dienstverlener escaleert volgens het contract: per ernstniveau de termijn, het kanaal en
>    de contactpersoon bij de organisatie, ook buiten kantoortijd. Het contract regelt welke ingrepen de
>    dienstverlener zelf mag doen (zoals een apparaat isoleren) en welke toestemming vragen. [5.24.03, 5.25.02]
> 3. De CISO toetst de escalatieketen elk jaar met een test-alarm en legt de uitkomst vast. [5.24.03]

> **Alleen als: Wie bewaakt je omgeving op aanvallen? «Geen structurele detectie»**
>
> 4. Er is geen structurele detectie. Incidenten komen binnen via medewerkers, leveranciers, waarschuwingen
>    van de sectorale CERT en meldingen van buiten. De CISO zet het ontbreken van detectie als risico in het
>    risicoregister, met een besluit van de directie over de aanpak. [5.24.03]

## 6. Afhandelen

1. De proceseigenaar handelt elk incident in zijn proces af via het incidentbeheerproces en wijst daarvoor
   direct na de beoordeling een behandelaar aan. De behandelaar beperkt eerst de schade, stelt daarna de
   oorzaak vast en herstelt, en legt elke stap vast in het incidentdossier. [5.24.03, 5.26.02]
2. De incidentprocedure verwijst naar de procedure voor crisisbeheersing en zegt wanneer een incident
   overgaat naar crisisbeheersing: bij langdurige uitval van kritieke processen, bij een groot datalek of
   bij een aanval met losgeld. De CISO besluit over de overgang en meldt dat aan
   **[eindverantwoordelijke bedrijfsvoering]**. [5.24.05]
3. De CISO beoordeelt bij elk incident met ernst kritiek of hoger of de organisatie andere partijen moet
   waarschuwen die hetzelfde risico lopen, zoals samenwerkingspartners of leveranciers. [5.26.02]

> **Alleen als: Hoe is je crisis- en continuïteitsorganisatie geregeld? «Geen»**
>
> 4. De organisatie heeft geen vaste crisisorganisatie. Bij een incident dat de grens voor crisis haalt, roept
>    de CISO de eindverantwoordelijke bedrijfsvoering op, die een ad-hoc crisisteam samenstelt. Het opzetten van
>    een crisisprocedure staat als actie in het jaarplan informatiebeveiliging. [5.24.05]

> **Alleen als: Hoe is je crisis- en continuïteitsorganisatie geregeld? «Een crisisteam, zonder BCM-functie» of «Een BCM-functie met continuïteitsplannen en een BIA»**
>
> 5. Het crisisteam neemt het incident over volgens de crisisprocedure; de CISO schuift aan als adviseur.
>    [5.24.05]

> **Alleen als: Hoe is je crisis- en continuïteitsorganisatie geregeld? «Een BCM-functie met continuïteitsplannen en een BIA»**
>
> 6. Bij uitval van een kritiek proces start de proceseigenaar het continuïteitsplan van dat proces. De
>    hersteltijden uit de BIA bepalen de volgorde van herstel. [5.24.05]

7. De proceseigenaar rapporteert maandelijks de stand van de incidenten in zijn proces: wat is open, wat is
   opgelost, welke maatregelen lopen nog. De CISO bundelt dit tot een maandrapport voor de
   eindverantwoordelijke bedrijfsvoering. [5.24.04]

## 7. Melden aan externe partijen

1. De incidentprocedure regelt de meldingen buiten de organisatie, elk met eigen termijn en eigenaar:
   het CSIRT en de toezichthouder volgens de Cyberbeveiligingswet waar die van toepassing is, de Autoriteit
   Persoonsgegevens bij een meldplichtig datalek (binnen 72 uur na ontdekking), de politie bij een strafbaar
   feit, en betrokkenen als het incident hun rechten of belangen raakt. De CISO registreert elke externe
   melding met datum en tijd in het incidentdossier. [5.24.07, 5.26.02, 5.27.01]
2. Meldingen en waarschuwingen die het CSIRT of de sectorale CERT aan de organisatie stuurt, komen binnen
   op een vast adres. De CISO beoordeelt ze binnen één werkdag en neemt ze op in de risicobehandeling,
   bijvoorbeeld als kwetsbaarheid die moet worden verholpen. [5.24.07]
3. Betrokkenen worden binnen de wettelijke termijn geïnformeerd. De privacy officer stelt de tekst op, de
   proceseigenaar beslist over verzending en de beslissing staat in het incidentdossier. [5.24.07]

> **Alleen als: Wat is je status onder de Cyberbeveiligingswet? «Essentiële entiteit» of «Belangrijke entiteit»**
>
> 4. De organisatie valt onder de Cyberbeveiligingswet. Een significant incident meldt de CISO aan het
>    aangewezen CSIRT en de toezichthouder in drie stappen: een vroegtijdige waarschuwing binnen 24 uur na
>    kennisname, een incidentmelding binnen 72 uur en een eindrapport binnen een maand. De incidentprocedure
>    legt vast wat significant is en wie de melding mag doen als de CISO afwezig is. [5.24.07, 5.26.02]
> 5. Waar een significant incident de dienstverlening aan afnemers kan raken, informeert de proceseigenaar die
>    afnemers zonder onnodige vertraging, met de maatregelen die zij zelf kunnen nemen. [5.24.07]
> 6. De CISO informeert de bestuurders bij elk significant incident direct; zij zijn persoonlijk
>    verantwoordelijk voor het toezicht op het risicobeheer onder de wet. [5.24.07]

> **Alleen als: Wat is je status onder de Cyberbeveiligingswet? «Essentiële entiteit»**
>
> 7. Als essentiële entiteit staat de organisatie onder proactief toezicht. De CISO houdt het incidentregister
>    en de meldingen zo bij dat ze op verzoek van de toezichthouder direct beschikbaar zijn. [5.24.07]

> **Alleen als: Wat is je status onder de Cyberbeveiligingswet? «Niet aangewezen»**
>
> 8. De organisatie is niet aangewezen onder de Cyberbeveiligingswet. De CISO meldt ernstige incidenten
>    vrijwillig aan de sectorale CERT, zodat andere overheden gewaarschuwd kunnen worden. [5.24.07]

## 8. Coordinated vulnerability disclosure

1. De CISO is eigenaar van de CVD-procedure volgens de leidraad van het NCSC, gepubliceerd op de website met
   een meldadres en een security.txt-bestand. De procedure noemt de reactietermijn, de afspraken over openbaar
   maken en de voorwaarden waaronder de organisatie geen aangifte doet. De CISO controleert jaarlijks dat de
   publicatie en het security.txt-bestand actueel zijn. [5.24.08]
2. Het meldloket registreert een CVD-melding als beveiligingsmelding, en de CISO bevestigt de ontvangst aan
   de melder binnen de reactietermijn uit de procedure. De meldingen en hun afhandeling zijn onderdeel van het
   maandrapport incidenten. [5.24.08]

## 9. Bewijs verzamelen en bewaren

1. Bij een vermoed incident stelt de behandelaar eerst bewijs veilig en herstelt daarna pas, tenzij de schade
   dat niet toelaat. Wie bewijs verzamelt, legt vast wat, wanneer, door wie en waar het is opgeslagen, zodat de
   keten van bewaring aantoonbaar is. [5.28.01]
2. Bij een mogelijk strafbaar feit of een mogelijke juridische procedure laat de CISO het veiligstellen doen
   door een forensisch onderzoeker, en legt dat besluit vast in het incidentdossier. [5.28.01]
3. Het incidentdossier bevat de melding, de beoordeling, de analyse, de gebruikte logging, de genomen
   maatregelen, de externe meldingen en het advies. De CISO bewaart het dossier ten minste drie jaar na
   afsluiting, ook als het vermoeden ongegrond bleek. [5.28.01]

## 10. Leren van incidenten

1. Na elk incident met ernst kritiek of hoger, en na elk meldplichtig datalek, organiseert de CISO binnen een
   maand een evaluatie met de proceseigenaar: oorzaak, wat werkte, wat niet, en welke maatregelen nodig zijn.
   Verbetermaatregelen krijgen een eigenaar en een datum en gaan naar het risicoregister. [5.27.01, 5.27.02]
2. De CISO analyseert elk kwartaal alle incidenten samen op patronen en herhalingen en neemt de uitkomst op
   in de rapportage aan de directie, met een voorstel voor aanpassing van maatregelen of van dit beleid.
   [5.27.02]
3. Lessen die voor andere overheden waardevol zijn, deelt de CISO geanonimiseerd met de sectorale CERT of
   samenwerkingspartners, na toestemming van de proceseigenaar. [5.27.02]

## 11. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| **[eindverantwoordelijke bedrijfsvoering]** | Ontvangst van het maandrapport, besluit over escalatie naar crisisbeheersing |
| Proceseigenaar | Oplossen van incidenten in het eigen proces, aanwijzen van de behandelaar, maandelijkse rapportage, informeren van afnemers en betrokkenen, uitvoeren van verbetermaatregelen |
| CISO | Eigenaar van dit beleid, de incidentprocedure en de CVD-procedure; beoordeling en classificatie, coördinatie, externe meldingen, bewijs, evaluaties en kwartaalanalyse; jaarlijkse toetsing van opzet en werking |
| Privacy officer en FG | Beoordeling datalekken, melding aan de Autoriteit Persoonsgegevens, tekst voor betrokkenen (de FG adviseert en houdt toezicht) |
| **[meldloket incidenten]** | Registratie, eerste beoordeling, doorzetten en terugkoppelen |
| **[lijneigenaar personeel]** | Registratie van de bevestiging van de meldprocedure door medewerkers en externen |
| Medewerkers en externen | Direct melden van een vermoed incident, geen eigen onderzoek, meewerken aan het onderzoek |

## 12. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in **[registratie van controles]**;
afwijkingen gaan als bevinding naar het risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| SIM-01 | Het maandrapport incidenten, inclusief CVD-meldingen, is opgesteld en aan de eindverantwoordelijke bedrijfsvoering verzonden | CISO | Maandelijks | Het rapport en de verzendregistratie | 5.24.04, 5.24.08 |
| SIM-02 | De kwartaalanalyse op patronen is uitgevoerd en in de rapportage aan de directie opgenomen | CISO | Elk kwartaal | De rapportage aan de directie | 5.27.02 |
| SIM-03 | Steekproef van tien incidenten: beoordeling binnen één werkdag met vastgelegd besluit, volledigheid van het dossier, keten van bewaring van het bewijs, tijdigheid van de interne en externe meldingen, evaluatie en opvolging van de verbetermaatregelen | CISO | Jaarlijks | Verslag van de steekproef met de bevindingen per incident | 5.24.01, 5.24.02, 5.24.03, 5.24.07, 5.25.02, 5.26.02, 5.27.01, 5.28.01 |
| SIM-04 | Alle medewerkers en externen met een account hebben de meldprocedure bevestigd | **[lijneigenaar personeel]** | Jaarlijks | Vergelijking van de registratie met de lijst van actieve accounts, met de afhandeling van de verschillen | 6.08.01 |
| SIM-05 | Een oefening met een incidentscenario is uitgevoerd, inclusief de beoordeling van de ernst, de overgang naar crisisbeheersing en het opstellen van een externe melding binnen de wettelijke termijn, en de verbeterpunten zijn belegd | CISO | Jaarlijks | Oefenverslag met de verbeterpunten en hun eigenaar | 5.24.05, 5.24.07, 5.25.02 |
| SIM-06 | De incidentprocedure en de CVD-procedure zijn opnieuw vastgesteld, de rollen en vervangers zijn belegd, en de publicatie van de CVD-procedure en het security.txt-bestand zijn actueel | CISO | Jaarlijks | Vastgestelde versies met datum, bezettingsoverzicht, schermafdruk van de publicatie | 5.24.01, 5.24.02, 5.24.08 |
| SIM-07 | Meldingen van het CSIRT of de sectorale CERT zijn binnen één werkdag beoordeeld en opgenomen in de risicobehandeling | CISO | Elk kwartaal | Overzicht van de ontvangen meldingen met datum van ontvangst, beoordeling en opvolging | 5.24.07 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De
proceseigenaar dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de looptijd. De
afwijking geldt pas na acceptatie van het risico door **[risico-eigenaar]**
en staat in het risicoregister; afwijkingen worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 13. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. De ernstniveaus volgen het beleid
informatieclassificatie. Het beleid raakt het beleid logging en monitoring (detectie en bewijs), het beleid
kwetsbaarheden en patchmanagement (opvolging van CERT-waarschuwingen en CVD-meldingen), het
continuïteitsbeleid (crisisbeheersing en herstel), het beleid fysieke toegang en beveiliging (fysieke
incidenten), het privacybeleid (datalekken), het beleid screening, bewustzijn en opleiding (de meldprocedure
in de bewustwording) en het beleid informatiebeveiliging bij inkoop en contractbeheer (meldplicht van
leveranciers).

## Bijlage A: BIO 2.0-maatregelen

De maatregelen van dit domein (13, waarvan 12 overheidsmaatregelen), waar dit stuk ze invult en welke controle ze aantoont. Nummers volgens BIO2 v1.3 definitief - 9 januari 2026; de tekst van de maatregel staat bij het CIP. Waar de BIO 2.0 geen overheidsmaatregel kent, geldt de ISO 27002-beheersmaatregel.

| Maatregel | Titel | Soort | In dit stuk | Controle |
|---|---|---|---|---|
| 5.24.01 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | overheidsmaatregel | 3. Meldloket en meldprocedure | SIM-03, SIM-06 |
| 5.24.02 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | overheidsmaatregel | 3. Meldloket en meldprocedure | SIM-03, SIM-06 |
| 5.24.03 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | overheidsmaatregel | 5. Detectie en escalatie | SIM-03 |
| 5.24.04 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | overheidsmaatregel | 6. Afhandelen | SIM-01 |
| 5.24.05 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | overheidsmaatregel | 6. Afhandelen | SIM-05 |
| 5.24.07 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | overheidsmaatregel | 7. Melden aan externe partijen | SIM-03, SIM-05, SIM-07 |
| 5.24.08 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | overheidsmaatregel | 8. Coordinated vulnerability disclosure | SIM-01, SIM-06 |
| 5.25.02 | Beoordelen van en besluiten over informatiebeveiligingsgebeurtenissen | ISO-beheersmaatregel | 4. Beoordelen en classificeren | SIM-03, SIM-05 |
| 5.26.02 | Reageren op informatiebeveiligings-incidenten | overheidsmaatregel | 6. Afhandelen | SIM-03 |
| 5.27.01 | Leren van informatiebeveiligingsincidenten | overheidsmaatregel | 7. Melden aan externe partijen | SIM-03 |
| 5.27.02 | Leren van informatiebeveiligingsincidenten | overheidsmaatregel | 10. Leren van incidenten | SIM-02 |
| 5.28.01 | Verzamelen van bewijsmateriaal | overheidsmaatregel | 9. Bewijs verzamelen en bewaren | SIM-03 |
| 6.08.01 | Melden van informatiebeveiligings-gebeurtenissen | overheidsmaatregel | 3. Meldloket en meldprocedure | SIM-04 |

## Bijlage B: Afkortingen

| Afkorting | Betekenis |
|---|---|
| AVG | Algemene verordening gegevensbescherming |
| BCM | Business continuity management, het beheer van bedrijfscontinuïteit |
| BIA | Business impact analyse |
| BIO | Baseline Informatiebeveiliging Overheid |
| CERT | Computer emergency response team |
| CISO | Chief Information Security Officer |
| CSIRT | Computer security incident response team |
| CVD | Coordinated vulnerability disclosure, het gecoördineerd melden van kwetsbaarheden |
| FG | Functionaris gegevensbescherming |
| ISAE | International Standard on Assurance Engagements |
| ISO | International Organization for Standardization |
| MDR | Managed detection and response |
| NCSC | Nationaal Cyber Security Centrum |
| SOC | Security operations center |

## Nog in te vullen

- **meldloket incidenten**: het loket, bijvoorbeeld de servicedesk, met telefoonnummer en mailadres
- **lijneigenaar personeel**: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd HR
- **incidentcoördinator**: de functionaris die informatiebeveiliging als neventaak heeft
- **eindverantwoordelijke bedrijfsvoering**: de functie, bijvoorbeeld de secretaris of directeur
- **registratie van controles**: het systeem waarin controles worden vastgelegd, bijvoorbeeld het ticketsysteem of het managementsysteem
- **risico-eigenaar**: de manager die restrisico's accepteert
- **eigenaar van dit beleid**: de manager die dit beleid uitvoert en laat naleven
- **vaststeller**: wie het beleid vaststelt, bijvoorbeeld de directie of het bestuur
