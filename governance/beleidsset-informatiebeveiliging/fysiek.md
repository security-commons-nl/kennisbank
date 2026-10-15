# Beleid fysieke toegang en beveiliging

[Download als Word](fysiek.docx) · [Maak je eigen versie in de generator](beleidsset-generator.html)

| | |
|---|---|
| Documenttype | Beleid informatiebeveiliging onder het strategisch informatiebeveiligingsbeleid; BIO 2.0-domein *Fysieke toegang & beveiliging* |
| Status | Concept, vast te stellen door de organisatie |
| Eigenaar | **[eigenaar van dit beleid]** |
| Vaststeller | **[vaststeller]** |
| Evaluatie | Jaarlijks, in de plan-do-check-act-cyclus van het managementsysteem voor informatiebeveiliging |

**In het kort.** Regelt de fysieke beveiliging van locaties en ruimten waar informatie wordt verwerkt of bewaard. Gaat over de indeling in vier beveiligingszones, de eisen per zone, de omgang met incidenten, monitoring en waarschuwingen, en het dragen van toegangspassen.

**Onderwerpen.** 3. Beveiligingszones; 4. Eisen voor zone 1, openbaar; 5. Eisen voor zone 2, kantoor; 6. Eisen voor zone 3, beperkt; 7. Eisen voor zone 4, kritiek; 8. Incidenten, monitoring en waarschuwingen; 9. Toegangspassen dragen.

Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor de fysieke beveiliging van de locaties,
ruimten en voorzieningen waar de organisatie informatie verwerkt of bewaart. Het legt vast in welke zones de
ruimten vallen, welke eisen per zone gelden en wie daarop toeziet, zodat onbevoegde toegang, schade en uitval
van voorzieningen de beschikbaarheid, integriteit en vertrouwelijkheid van informatie niet aantasten. Het gaat
over de ISO-beheersmaatregelen 7.1 tot en met 7.5 en 7.12.

**Voor wie.** Het beleid is primair bedoeld voor de afdeling die de gebouwen en de toegangsmiddelen beheert en
voor de eigenaren van beveiligde zones. De gedragsregels gelden voor iedereen die een locatie van de
organisatie betreedt: medewerkers, inhuur, stagiairs, vrijwilligers, bezoekers en leveranciers.

**Waarop.** Alle locaties en terreinen die de organisatie gebruikt voor haar processen, met de nadruk op de
ruimten waar informatie wordt opgeslagen of geautomatiseerd verwerkt en op de opslag van waardedocumenten
zoals identiteitsbewijzen. Zijn ruimten of voorzieningen uitbesteed, bijvoorbeeld een datacenter, dan gelden
de eisen uit dit beleid als minimumeis voor die partij. De organisatie legt dat vast in het contract en
toetst de naleving met een onafhankelijke verklaring, zoals een ISO 27001-certificaat of een ISAE 3402- of
ISAE 3000-rapport; het vastleggen loopt via het beleid informatiebeveiliging bij inkoop, het toetsen via het
beleid contractbeheer.

Buiten dit beleid vallen het werken in beveiligde zones, het plaatsen en onderhouden van apparatuur en de
nutsvoorzieningen voor apparatuur (beleid bedrijfsmiddelenbeheer), clear desk en clear screen (beleid
IT-compliance) en het afvoeren van opslagmedia (beleid afvoer en hergebruik van gegevensdragers).

> **Alleen als: Waar draaien je systemen? «Vooral SaaS en publieke cloud»**
>
> De organisatie heeft geen eigen datacenter en geen serverruimte bij een hostingpartij. De fysieke
> beveiliging van de systemen ligt bij de SaaS-leveranciers; dit beleid regelt de kantoorlocaties, de
> netwerk- en stroomvoorzieningen op die locaties en de eisen die de organisatie aan leveranciers stelt.

## 2. Uitgangspunten

1. Fysieke beveiliging is risicogestuurd: hoe groter de gevolgen van onbevoegde toegang voor beschikbaarheid,
   integriteit en vertrouwelijkheid, hoe zwaarder de maatregelen.
2. Elke ruimte valt in een beveiligingszone. De zone volgt uit de classificatie van de informatie en de
   systemen in die ruimte (beleid informatieclassificatie). De eisen van een hogere zone komen bovenop die
   van de lagere.
3. Kritieke informatie en kritieke systemen liggen achter minstens twee opeenvolgende zones met elk een
   eigen toegangscontrole.
4. Beveiligingsmaatregelen zijn niet zichtbaar voor wie ze niet hoeft te kennen: beveiligde ruimten zijn niet
   als zodanig aangeduid.
5. Termijnen en frequenties in dit beleid die niet uit een wet of uit de BIO 2.0 komen, zijn standaardwaarden.
   De organisatie past ze aan op haar eigen risicoafweging en legt de keuze vast bij de vaststelling van dit beleid.

## 3. Beveiligingszones

1. De organisatie deelt elke locatie in in vier zones en legt dat vast in een zoneringsplan per locatie,
   beheerd door **[lijneigenaar fysieke beveiliging]**.
   De zones volgen de impactniveaus van het classificatieschema: [7.01.02]

   | Zone | Impactniveau | Voorbeelden van ruimten |
   |---|---|---|
   | 1 openbaar | verwaarloosbaar | buitenterrein, ontvangsthal, gedeelde ruimten in een gebouw met andere gebruikers |
   | 2 kantoor | gering | kantoor- en werkruimten, opslag van niet-kritieke apparatuur |
   | 3 beperkt | gemiddeld | knooppunten voor netwerk en stroom, noodstroomvoorziening, opslag van kritieke of kostbare apparatuur, statisch archief |
   | 4 kritiek | ernstig | serverruimte, opslag van identiteitsbewijzen en andere waardedocumenten |

2. Het classificatieschema kent ook het niveau catastrofaal. Daarvoor voorziet de organisatie geen zones op haar
   eigen locaties; blijkt uit het zoneringsplan dat een ruimte dat niveau toch vraagt, dan stelt de CISO de
   eisen voor die ruimte vast op basis van een eigen risicoanalyse. [7.01.02]
3. Het zoneringsplan noemt per zone de eigenaar: de primaire gebruiker van de ruimte. De eigenaar keurt
   toegangsverzoeken goed, controleert periodiek wie toegang heeft en beoordeelt jaarlijks of het niveau van
   de zone nog klopt. [7.01.02]
4. Een ruimte van zone 4 ligt altijd binnen een zone 3, zodat kritieke informatie en kritieke systemen nooit
   via één beveiligde zone bereikbaar zijn: wie binnenkomt, passeert ten minste twee toegangscontroles met elk
   een eigen controle op de persoon. [7.01.02]

> **Alleen als: Waar draaien je systemen? «Eigen datacenter of serverruimte»**
>
> 5. De eigen serverruimte is een zone 4 binnen een zone 3. De tweede controle is persoonsgebonden (pas met
>    pincode of biometrie) en elke binnenkomst wordt gelogd. [7.01.02]

> **Alleen als: Waar draaien je systemen? «Hostingpartij (IaaS, gedeeld datacenter)» of «Vooral SaaS en publieke cloud»**
>
> 6. Waar systemen bij een hostingpartij of SaaS-leverancier staan, eist de organisatie in het contract een
>    zonering met ten minste twee opeenvolgende beveiligde zones voor de ruimte met de systemen, en een
>    verklaring (ISO 27001-certificaat of ISAE 3402-rapport) die dat aantoont. [7.01.02]
> 7. Ook op de eigen locaties liggen de netwerk- en stroomknooppunten in zone 3, binnen zone 2. [7.01.02]

## 4. Eisen voor zone 1, openbaar

1. Vrije toegang voor bezoekers en leveranciers tot het terrein en de ontvangsthal is er alleen tijdens
   openingstijden. [7.03.01]
2. Tijdens openingstijden controleert een bemande receptie de toegang en let op afwijkend gedrag; waar geen
   receptie is, regelen toegangspoortjes of een gelijkwaardige voorziening de toegang. [7.02.01, 7.03.01]
3. Noodprocedures en vluchtroutes zijn zichtbaar aangegeven op het terrein en in de gebouwen. [7.05.01]
4. De buitenschil van een gebouw (daken, buitenmuren, plafonds, vloeren) biedt geen zwakke plekken die
   inbraak eenvoudig maken. Een laad- en losplaats geeft geen directe toegang tot zone 2 of hoger. [7.03.01]
5. Buiten openingstijden zijn locaties afgesloten en bewaakt door een alarmsysteem met een passende
   combinatie van contactmelders, geluidsmelders, bewegingsmelders en camera's. Het alarm is aangesloten op
   een gecertificeerde particuliere alarmcentrale en de opvolging van meldingen staat in een procedure.
   [7.04.01]
6. Huurt de organisatie een bewakingsdienst in, dan is vooraf gecontroleerd en in het contract vastgelegd dat
   die voldoet aan de Wet particuliere beveiligingsorganisaties en recherchebureaus. [7.03.01]
7. Voedingskabels en kabels voor gegevens lopen waar mogelijk door afgesloten kabelgoten of leidingen.
   Aansluitpunten in openbaar toegankelijke ruimten zijn uitgeschakeld of afgeschermd, en patchkasten zijn
   afgesloten. [7.12.01]

## 5. Eisen voor zone 2, kantoor

Bovenop de eisen voor zone 1:

1. Medewerkers en leveranciers met een doorlopende opdracht krijgen toegang met een op naam geregistreerd
   toegangsmiddel. Rechten volgen de functie; bij uitdiensttreding, einde van de opdracht of functiewijziging
   wordt het toegangsmiddel ingenomen en zijn de rechten uiterlijk op de laatste werkdag ingetrokken of
   aangepast. [7.02.01]
2. Nog niet uitgegeven toegangsmiddelen liggen achter slot, bij de receptie of in een afgesloten kast. [7.02.01]
3. Bezoekers en leveranciers zonder eigen toegangsrecht komen alleen binnen met toestemming van een medewerker
   en onder begeleiding. Ze worden bij binnenkomst geregistreerd, dragen zichtbaar een bezoekerspas en leveren
   die bij vertrek in. [7.02.01]
4. Verlies of diefstal van een toegangsmiddel wordt direct gemeld en het middel wordt direct geblokkeerd.
   [7.02.01]

## 6. Eisen voor zone 3, beperkt

Bovenop de eisen voor zone 2:

1. Toegang vraagt doelbinding: alleen wie de ruimte voor zijn werk nodig heeft, krijgt toegang, na
   goedkeuring van de eigenaar van de zone en met een op naam geregistreerd toegangsmiddel. [7.02.01]
2. De ruimte is afgesloten met een elektronisch toegangssysteem dat geslaagde en mislukte toegangspogingen
   logt. De logging wordt bewaard gedurende
   **[bewaartermijn toegangslogging]**. [7.02.01, 7.04.01]
3. Bezoekers en leveranciers zonder eigen toegangsrecht komen alleen binnen onder toezicht van een bevoegde
   medewerker, voor noodzakelijke werkzaamheden. [7.02.01]
4. De eigenaar van de zone stelt elk halfjaar vast dat de uitgegeven toegangsmiddelen alleen in gebruik zijn
   bij bevoegde personen met een geldige doelbinding. [7.02.01]
5. Foto-, video- en geluidsopnamen zijn niet toegestaan zonder toestemming van de eigenaar van de zone.
   [7.03.01]
6. Toegangsdeuren sluiten automatisch en geven een signaal als ze langer openstaan dan nodig. Het signaal komt
   binnen kantoortijd bij de receptie en daarbuiten bij de alarmcentrale. [7.04.01]
7. De ruimte draagt geen aanduiding die de aard of het belang ervan prijsgeeft en staat niet op openbare
   plattegronden. [7.03.01]
8. Gevaarlijke of brandbare stoffen worden zo ver van de ruimte opgeslagen dat ze geen gevolgen hebben voor de
   ruimte. [7.05.01]
9. Netwerk- en stroombekabeling naar de ruimte loopt niet door openbare ruimten, of is daar afgeschermd.
   [7.12.01]

## 7. Eisen voor zone 4, kritiek

Bovenop de eisen voor zone 3. Is de ruimte uitbesteed, dan voldoet de leverancier aan deze eisen via het
contract en een onafhankelijke verklaring (hoofdstuk 1).

1. Toegang loopt via een toegangssysteem met een autorisatiestructuur en persoonlijke toegangsmiddelen.
   [7.02.01]
2. Leveranciers krijgen geen toegang zonder toezicht van een bevoegde medewerker, tenzij de eigenaar van de
   zone daar uitdrukkelijk toestemming voor geeft. [7.02.01]
3. De identiteit van bezoekers en leveranciers wordt vastgesteld aan de hand van een identiteitsbewijs voordat
   zij toegang krijgen. De begeleidende medewerker registreert datum en tijd van binnenkomst en vertrek.
   [7.02.01]
4. Camera's registreren de toegang tot de ruimte. De beelden staan in het verwerkingsregister en worden niet
   langer bewaard dan **[bewaartermijn camerabeelden]**,
   tenzij een incident langer bewaren rechtvaardigt. [7.04.01]
5. De ruimte heeft een noodstroomvoorziening (UPS) tegen stroomuitval en storingen in de nutsvoorzieningen,
   en een voorziening die bij een langdurige storing stroom levert, zoals een aggregaat. Beide worden getest volgens
   **[testschema noodstroom]**.
   [7.05.01]
6. Een klimaatinstallatie regelt en bewaakt temperatuur en luchtvochtigheid. [7.05.01]
7. De ruimte is beschermd tegen wateroverlast en tegen stroompieken, met een voorziening die waterschade
   signaleert en beperkt. [7.05.01]
8. Automatische branddetectie is aangesloten op de alarmcentrale en er is een blusvoorziening die geschikt is
   voor ICT-apparatuur. Beide worden jaarlijks gecontroleerd en onderhouden. [7.05.01]
9. De eigenaar van de zone voert jaarlijks een risicobeoordeling uit op omgevingsdreigingen (oproer,
   terrorisme, explosies), brand, overstroming en aardbeving, en op de ligging van de ruimte ten opzichte van
   water, breuklijnen en hoogte, en volgt de uitkomsten op. [7.05.01]

> **Alleen als: Heb je operationele technologie (OT)? «Beperkt: gebouwbeheer, toegang, camera's» of «Substantieel: bruggen, gemalen, verkeer, zuivering»**
>
> 10. Ruimten met operationele technologie (gemalen, sluizen, installaties, gebouwbeheer) staan in het
>    zoneringsplan, in zone 3 of hoger. Besturingskasten en lokale bedieningspanelen zitten achter slot en
>    worden bij elke inspectie gecontroleerd op sporen van openbreken. [7.01.02, 7.03.01]

## 8. Incidenten, monitoring en waarschuwingen

Ongeacht de zone:

1. Fysieke beveiligingsincidenten, zoals een inbraak of een poging daartoe, onbevoegde toegang, verlies of
   diefstal van een toegangsmiddel en uitval van een beveiligingsvoorziening, worden direct gemeld en
   afgehandeld volgens het beleid beveiligingsincidenten. [7.04.01]
2. **[lijneigenaar fysieke beveiliging]** beoordeelt elke maand de logging van het toegangssysteem en de
   alarmmeldingen op afwijkingen, zoals herhaalde mislukte toegangspogingen of toegang buiten de reguliere
   werktijden. [7.04.01]
3. Bij een concreet beveiligingsrisico voor een locatie, zoals een dreiging, een inbraak of een verdachte
   situatie, waarschuwt **[meldpunt fysieke beveiliging]**
   volgens de gemaakte afspraken de relevante collega's in het beveiligingsdomein van de overheid: de CISO, de
   beveiligingscoördinatoren van samenwerkingspartners op dezelfde locatie en, bij een strafbaar feit, de
   politie. [7.02.01]
4. De afspraken over wie wie waarschuwt, met welk kanaal en binnen welke tijd, staan in
   **[afsprakenlijst waarschuwingen]** en worden
   jaarlijks gecontroleerd. [7.02.01]

## 9. Toegangspassen dragen

1. Bezoekers, leveranciers en andere externen dragen hun pas zichtbaar zolang zij in een gebouw van de
   organisatie zijn. De pas laat alleen zien dat de drager een externe is, bijvoorbeeld met de tekst
   "Bezoeker". [7.02.01]
2. Of medewerkers hun pas zichtbaar dragen, staat in **[pasregels medewerkers]**.
   Op de pas staat zo min mogelijk informatie, zodat een verloren of gestolen pas weinig prijsgeeft. [7.02.01]

## 10. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| **[lijneigenaar fysieke beveiliging]** | Eigenaar van dit beleid en van het zoneringsplan; beheer van het toegangssysteem en van de uitgifte en inname van toegangsmiddelen; bewaking, alarmopvolging en receptie; maandelijkse beoordeling van logging en alarmmeldingen |
| Eigenaar van een zone | Goedkeuren van toegangsverzoeken, halfjaarlijkse controle van de toegangsmiddelen, jaarlijkse beoordeling van het niveau van de zone en van de omgevingsdreigingen |
| CISO | Advies over dit beleid, jaarlijkse toetsing van opzet en werking, beoordeling van afwijkingen, ontvangst van waarschuwingen bij concrete dreigingen |
| **[meldpunt fysieke beveiliging]** | Waarschuwen van de partners in het beveiligingsdomein van de overheid |
| Inkoop en contractbeheer | Vastleggen van de eisen uit dit beleid bij leveranciers die ruimten beheren of toegang krijgen, en toetsen van hun verklaringen |
| Medewerkers en inhuur | Hun toegangsmiddel persoonlijk gebruiken en niet uitlenen, niemand mee laten lopen door een beveiligde deur, bezoekers begeleiden, verlies en verdachte situaties direct melden |

## 11. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in **[registratie van controles]**;
afwijkingen gaan als bevinding naar het risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| FYS-01 | Het zoneringsplan is actueel: elke ruimte heeft een zone en een eigenaar, elke ruimte van zone 4 ligt binnen zone 3, en de zones in het toegangssysteem komen overeen met het plan | Eigenaar van elke zone van zone 3 of hoger | Jaarlijks | Zoneringsplan, rapport uit het toegangssysteem, vastgelegde beoordeling | 7.01.02 |
| FYS-02 | Toegang tot zone 3 en 4 wordt alleen toegekend na goedkeuring van de eigenaar van de zone | Eigenaar van de zone | Per aanvraag | Aanvraag en goedkeuring in de registratie | 7.02.01 |
| FYS-03 | Toegangsmiddelen worden na uitdiensttreding, einde opdracht of functiewijziging uiterlijk op de laatste werkdag ingenomen of aangepast | **[lijneigenaar fysieke beveiliging]** | Maandelijks | Vergelijking van de personeelsmutaties met de mutaties in het toegangssysteem | 7.02.01 |
| FYS-04 | De uitgegeven toegangsmiddelen per zone zijn alleen in gebruik bij bevoegde personen met een doelbinding | Eigenaar van de zone | Halfjaarlijks | Rapport uit het toegangssysteem met de beoordeling per persoon | 7.02.01 |
| FYS-05 | De fysieke voorzieningen voldoen aan de eisen per zone: bouwkundige schil, alarm, bewaking, klimaat, noodstroom, brand- en waterbeveiliging, bekabeling | **[lijneigenaar fysieke beveiliging]** | Halfjaarlijks | Ingevulde checklist per locatie, testrapporten van UPS, aggregaat en brandvoorzieningen | 7.03.01, 7.04.01, 7.05.01, 7.12.01 |
| FYS-06 | Logging van het toegangssysteem en alarmmeldingen zijn beoordeeld op afwijkingen en afwijkingen zijn opgevolgd | **[lijneigenaar fysieke beveiliging]** | Maandelijks | Beoordelingsverslag met de opgevolgde afwijkingen | 7.04.01 |
| FYS-07 | De jaarlijkse risicobeoordeling van omgevingsdreigingen voor elke zone 4 is uitgevoerd en opgevolgd | Eigenaar van de zone | Jaarlijks | Risicobeoordeling en opvolging | 7.05.01 |
| FYS-08 | Waarschuwingen bij concrete beveiligingsrisico's zijn volgens de afsprakenlijst verzonden en ontvangen waarschuwingen zijn opgevolgd; de afsprakenlijst is actueel | CISO | Jaarlijks, en na elke waarschuwing | Registratie van meldingen en waarschuwingen, afsprakenlijst | 7.02.01 |
| FYS-09 | Leveranciers die ruimten beheren leveren een geldige onafhankelijke verklaring over hun fysieke beveiliging | Contractbeheer | Jaarlijks | Verklaring per leverancier, beoordeling van de uitzonderingen | 7.01.02, 7.03.01, 7.05.01 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De eigenaar
van de zone dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de looptijd. De
afwijking geldt pas na acceptatie van het risico door **[risico-eigenaar]**
en staat in het risicoregister; afwijkingen worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 12. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. De zones volgen het beleid
informatieclassificatie. Het beleid raakt het beleid bedrijfsmiddelenbeheer (werken in beveiligde zones,
apparatuur en nutsvoorzieningen), het beleid afvoer en hergebruik van gegevensdragers, het beleid back-up en
recovery (uitwijk- en opslaglocaties), het continuïteitsbeleid (noodstroom en uitwijk), het beleid
beveiligingsincidenten (melden en afhandelen) en het beleid informatiebeveiliging bij inkoop en
contractbeheer (eisen aan en verklaringen van leveranciers).

## Bijlage A: BIO 2.0-maatregelen

De maatregelen van dit domein (6, waarvan 2 overheidsmaatregelen), waar dit stuk ze invult en welke controle ze aantoont. Nummers volgens BIO2 v1.3 definitief - 9 januari 2026; de tekst van de maatregel staat bij het CIP. Waar de BIO 2.0 geen overheidsmaatregel kent, geldt de ISO 27002-beheersmaatregel.

| Maatregel | Titel | Soort | In dit stuk | Controle |
|---|---|---|---|---|
| 7.01.02 | Fysieke beveiligingszones | overheidsmaatregel | 3. Beveiligingszones | FYS-01, FYS-09 |
| 7.02.01 | Fysieke toegangsbeveiliging | overheidsmaatregel | 4. Eisen voor zone 1, openbaar | FYS-02, FYS-03, FYS-04, FYS-08 |
| 7.03.01 | Beveiligen van kantoren, ruimten en faciliteiten | ISO-beheersmaatregel | 4. Eisen voor zone 1, openbaar | FYS-05, FYS-09 |
| 7.04.01 | Monitoren van de fysieke beveiliging | ISO-beheersmaatregel | 4. Eisen voor zone 1, openbaar | FYS-05, FYS-06 |
| 7.05.01 | Beschermen tegen fysieke en omgevingsdreigingen | ISO-beheersmaatregel | 4. Eisen voor zone 1, openbaar | FYS-05, FYS-07, FYS-09 |
| 7.12.01 | Beveiligen van bekabeling | ISO-beheersmaatregel | 4. Eisen voor zone 1, openbaar | FYS-05 |

## Bijlage B: Afkortingen

| Afkorting | Betekenis |
|---|---|
| BIO | Baseline Informatiebeveiliging Overheid |
| CISO | Chief Information Security Officer |
| ICT | Informatie- en communicatietechnologie |
| ISAE | International Standard on Assurance Engagements |
| ISO | International Organization for Standardization |
| IT | Informatietechnologie |
| IaaS | Infrastructure as a service |
| OT | Operationele technologie |
| SaaS | Software as a service |
| UPS | Uninterruptible power supply, een noodstroomvoorziening |

## Nog in te vullen

- **lijneigenaar fysieke beveiliging**: de manager van de afdeling die gebouwen en toegangsmiddelen beheert, bijvoorbeeld facilitaire zaken
- **bewaartermijn toegangslogging**: standaard een jaar
- **bewaartermijn camerabeelden**: de vastgestelde termijn, bijvoorbeeld vier weken
- **testschema noodstroom**: hoe vaak de UPS en de langdurige voorziening worden getest, bijvoorbeeld halfjaarlijks en jaarlijks
- **meldpunt fysieke beveiliging**: de functie die de waarschuwing doet, bijvoorbeeld de coördinator beveiliging
- **afsprakenlijst waarschuwingen**: document met de contactpersonen en kanalen per partner
- **pasregels medewerkers**: de huisregel over het dragen van de pas
- **registratie van controles**: het systeem waarin controles worden vastgelegd, bijvoorbeeld het ticketsysteem of het managementsysteem
- **risico-eigenaar**: de manager die restrisico's accepteert
- **eigenaar van dit beleid**: de manager die dit beleid uitvoert en laat naleven
- **vaststeller**: wie het beleid vaststelt, bijvoorbeeld de directie of het bestuur
