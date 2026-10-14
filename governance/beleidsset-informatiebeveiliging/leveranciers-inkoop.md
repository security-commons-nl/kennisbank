# Beleid informatiebeveiliging bij inkoop

| | |
|---|---|
| Documenttype | Beleid informatiebeveiliging onder het strategisch informatiebeveiligingsbeleid; BIO 2.0-domein *Leveranciersbeheer - Inkoop* |
| Status | Concept, vast te stellen door de organisatie |
| Eigenaar | **[eigenaar van dit beleid]** |
| Vaststeller | **[vaststeller]** |
| Evaluatie | Jaarlijks, in de plan-do-check-act-cyclus van het managementsysteem voor informatiebeveiliging |

Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor de inkoop van producten en diensten
waarbij een leverancier informatie van de organisatie verwerkt, opslaat of ontsluit, of toegang krijgt tot
haar systemen. Het legt vast wat de organisatie regelt voordat een contract wordt getekend: de risicoafweging,
de eisen in de uitvraag, de voorwaarden in het contract, het bewijs dat de leverancier levert, de meldplicht
van de leverancier, de exit en de keten van toeleveranciers. Het gaat over de ISO-beheersmaatregelen 5.19,
5.20 en 5.21, voor zover die vóór het contract spelen.

**Voor wie.** Het beleid is primair bedoeld voor de inkoopfunctie, de proceseigenaren die een inkoop starten
en de CISO die adviseert. Het geldt voor iedereen die namens de organisatie een contract met een
informatiecomponent voorbereidt of tekent, ook bij een onderhandse opdracht, een verlenging, een uitbreiding
of een gratis dienst.

**Waarop.** Elke inkoop waarbij de leverancier informatie van de organisatie verwerkt of bij haar systemen
kan: software, clouddiensten, hosting, beheerdiensten, koppelingen, hardware met onderhoud op afstand en
adviesdiensten met toegang tot informatie. Is het inkoopproces zelf uitbesteed, bijvoorbeeld aan een
inkoopbureau of een samenwerkingsverband, dan gelden de eisen uit dit beleid als minimumeis voor die partij.
De organisatie legt dat vast in het contract en toetst de naleving met een onafhankelijke verklaring, zoals
een ISO 27001-certificaat of een ISAE 3402- of ISAE 3000-rapport; het vastleggen loopt via dit beleid, het
toetsen via het beleid contractbeheer.

Buiten dit beleid vallen het beheer van de leverancier tijdens de looptijd, het register van contracten, de
jaarlijkse beoordeling en de werkwijze voor clouddiensten (beleid contractbeheer), de inhoud van de
verwerkersovereenkomst (privacybeleid) en de eisen aan software die een leverancier voor de organisatie
ontwikkelt (beleid secure software development).

> **Alleen als: Wie beheert je IT? «Regie: eigen organisatie stuurt, beheer is uitbesteed» of «Volledig uitbesteed»**
>
> De organisatie heeft het beheer van haar IT uitbesteed. De contracten met beheer- en hostingpartijen zijn
> daarmee de zwaarste inkopen onder dit beleid: wat daar niet in staat, kan de organisatie later niet afdwingen.

## 2. Uitgangspunten

1. De organisatie blijft verantwoordelijk voor de informatie die een leverancier voor haar verwerkt. Een
   certificaat of verklaring van de leverancier verandert daar niets aan.
2. Beveiligingseisen staan in de uitvraag. Wat pas na de gunning wordt bedacht, is in de onderhandeling niet
   meer te krijgen.
3. De zwaarte van de eisen volgt uit een risicoafweging per inkoop, op basis van het impactniveau en het
   vertrouwelijkheidslabel van de informatie (beleid informatieclassificatie) en het belang van het proces.
4. Bij IT-inkoop gebruikt de organisatie een standaardset inkoopvoorwaarden voor IT, bijvoorbeeld de GIBIT
   voor gemeenten of de ARBIT voor het Rijk, en vult die per inkoop aan.

## 3. Beleidsregels

### 3.1 Risicoafweging en eisen in de uitvraag

1. Bij elke inkoop met een informatiecomponent stelt de proceseigenaar vóór de uitvraag, samen met
   **[inkoopadviseur]** en de CISO, vast welke informatie de
   leverancier verwerkt, welk impactniveau en welk vertrouwelijkheidslabel die heeft en welke eisen aan
   beschikbaarheid, integriteit en vertrouwelijkheid daaruit volgen. De afweging staat in het inkoopdossier.
   [5.19.01]
2. De inkoopadviseur neemt de eisen uit die afweging op in de offerteaanvraag of uitvraag, naast de
   functionele eisen, en laat ze meewegen in de beoordeling van de inschrijvingen. Een inschrijver die niet
   aan een eis kan voldoen, zegt dat in de inschrijving; de proceseigenaar legt vast of dat aanvaardbaar is.
   [5.19.01]
3. Bij een inkoop onder de drempel voor een risicoafweging, bijvoorbeeld een dienst zonder persoonsgegevens
   en zonder koppeling met eigen systemen, past de inkoopadviseur de standaardset eisen toe en legt dat vast
   in het inkoopdossier. De drempel staat in
   **[drempel risicoafweging inkoop]**.
   [5.19.01]
4. De CISO houdt de standaardset eisen bij en stelt die jaarlijks opnieuw vast, zodat nieuwe dreigingen en
   nieuwe wettelijke eisen erin landen. [5.19.01]

> **Alleen als: Wat is je status onder de Cyberbeveiligingswet? «Essentiële entiteit» of «Belangrijke entiteit»**
>
> 5. De organisatie valt onder de Cyberbeveiligingswet. De zorgplicht omvat de beveiliging van de
>    toeleveringsketen. Bij inkoop van een dienst die een rol speelt in de dienstverlening onder die wet, legt de
>    proceseigenaar in de risicoafweging ook vast hoe de leverancier bijdraagt aan het voldoen aan de meldplicht
>    en welke eisen de bestuurder daarvoor heeft goedgekeurd. [5.19.01]

### 3.2 Voorwaarden in het contract

1. De inkoopadviseur zet alle beveiligingseisen uit de uitvraag letterlijk of als verwijzing in het contract,
   met de afspraken uit de onderhandeling. Een eis die in de uitvraag stond en niet in het contract, geldt als
   vervallen en vraagt een vastgelegd besluit van de proceseigenaar vóór ondertekening. [5.20.01]
2. De organisatie verklaart haar eigen inkoopvoorwaarden van toepassing en wijst de algemene voorwaarden van
   de leverancier in het contract uitdrukkelijk van de hand. [5.20.02]
3. Lukt dat niet, bijvoorbeeld bij een standaarddienst van een grote aanbieder, dan beoordeelt de CISO de
   voorwaarden van de leverancier vóór ondertekening. De beoordeling noemt welke gevolgen de organisatie
   accepteert, welke ze met eigen maatregelen afdekt en welke voorwaarden ze nooit accepteert. De
   proceseigenaar tekent voor de geaccepteerde risico's en de beoordeling gaat in het inkoopdossier. [5.20.02]
4. Voorwaarden die de organisatie nooit accepteert, staan in
   **[lijst onaanvaardbare voorwaarden]**.
   De CISO stelt die lijst jaarlijks opnieuw vast. [5.20.02]
5. Verwerkt de leverancier persoonsgegevens, of kan hij erbij, dan sluit de proceseigenaar een
   verwerkersovereenkomst volgens het privacybeleid voordat de verwerking begint. De inkoopadviseur legt in
   het inkoopdossier vast dat die overeenkomst er is. [5.20.01]

### 3.3 Bewijs van de leverancier en eigen onderzoek

1. Het contract verplicht de leverancier om aan te tonen dat hij aan de eisen voldoet, in opzet, bestaan en
   werking, met een rapport van een onafhankelijke derde. Voorbeelden zijn een ISAE 3000- of ISAE
   3402-rapport van type 2 of een ISO 27001-certificaat met een verklaring van toepasselijkheid. [5.20.03]
2. De CISO controleert vóór ondertekening dat de reikwijdte van dat rapport de gecontracteerde dienst dekt,
   inclusief de manier waarop de leverancier zijn eigen toeleveranciers beheert. Valt een deel van de dienst
   buiten de reikwijdte, dan levert de leverancier voor dat deel ander bewijs, en de CISO legt vast of dat
   volstaat. [5.20.03]
3. Het contract verplicht de leverancier om het bewijs bij het sluiten van het contract te leveren en daarna
   elk jaar opnieuw. De jaarlijkse levering wordt bewaakt volgens het beleid contractbeheer. [5.20.03]
4. Het contract geeft de organisatie het recht om zelf een audit of een technisch onderzoek te laten doen,
   bijvoorbeeld een penetratietest, ook om de rapporten van de leverancier te controleren. De verdeling van de
   kosten staat in het contract. [5.20.04]
5. Restrisico's uit het bewijs of het eigen onderzoek zet de proceseigenaar vóór ondertekening in het
   risicoregister en behandelt ze volgens de risicomanagementmethodiek van de organisatie. [5.20.04]

### 3.4 Transparantie over kwetsbaarheden en incidenten

1. Het contract verplicht de leverancier om beveiligingsincidenten, datalekken en kwetsbaarheden die de dienst
   aan de organisatie kunnen raken, te melden bij het meldloket van de organisatie (beleid
   beveiligingsincidenten). De termijn staat in het contract en is kort genoeg om de wettelijke meldtermijnen
   van de organisatie te halen; voor een datalek is dat ten hoogste 24 uur na ontdekking, zodat de melding
   aan de Autoriteit Persoonsgegevens binnen 72 uur kan. [5.20.05]
2. Het contract legt vast wat de leverancier bij een melding aanlevert: wat er is gebeurd, welke gegevens en
   welke gebruikers geraakt zijn, welke maatregelen hij neemt en wanneer hij de melding aanvult. [5.20.05]

> **Alleen als: Wat is je status onder de Cyberbeveiligingswet? «Essentiële entiteit» of «Belangrijke entiteit»**
>
> 3. Voor diensten die onder de Cyberbeveiligingswet vallen, is de meldtermijn van de leverancier ten hoogste
>    **[meldtermijn leverancier]**
>    na ontdekking. Het contract regelt ook dat de leverancier meewerkt aan de vervolgmeldingen binnen 72 uur en
>    aan het eindrapport binnen een maand. [5.20.05]

### 3.5 Afhankelijkheid en exit

1. Vóór het contract beoordeelt de proceseigenaar of de afhankelijkheid van de leverancier beheersbaar is: zijn
   er alternatieven, hoe lang duurt een overstap en kan de organisatie haar gegevens in een bruikbaar formaat
   terugkrijgen. De uitkomst staat in het inkoopdossier. [5.20.06]
2. Elk contract voor een dienst die een kritiek proces ondersteunt of informatie met het label vertrouwelijk
   of hoger verwerkt, bevat een uitgewerkte exitregeling: het teruggeven van gegevens in een open of
   gedocumenteerd formaat, de medewerking bij overdracht aan een opvolger, de termijn waarin de leverancier
   gegevens verwijdert en het bewijs daarvan. De inkoopadviseur controleert vóór ondertekening dat de regeling
   erin staat. [5.20.06]
3. Bij software die de organisatie in eigen beheer draait en die niet makkelijk te vervangen is, regelt het
   contract een escrow of een gelijkwaardige continuïteitsregeling. [5.20.06]

### 3.6 Keten van toeleveranciers

1. Vóór het contract geeft de leverancier een overzicht van de toeleveranciers die bij de dienst betrokken
   zijn, met hun rol, de locatie van de verwerking en de risico's die hij daarin ziet. De inkoopadviseur
   neemt het overzicht op in het inkoopdossier. [5.21.02]
2. De CISO beoordeelt vóór ondertekening of de risico's in de keten aanvaardbaar zijn. De proceseigenaar
   besluit en legt het besluit vast in het inkoopdossier. [5.21.02]
3. Het contract verbiedt de leverancier om zonder schriftelijke toestemming van de organisatie werk aan een
   nieuwe toeleverancier over te dragen, en verplicht hem om de beveiligingseisen aan zijn toeleveranciers
   door te geven. [5.21.02]

### 3.7 Eisen per soort dienst

> **Alleen als: Waar draaien je systemen? «Eigen datacenter of serverruimte»**
>
> 1. Bij inkoop van hardware en software voor het eigen datacenter regelt het contract hoe de leverancier op
>    afstand toegang krijgt voor onderhoud (alleen na aanvraag, met persoonsgebonden accounts en logging) en
>    hoelang hij beveiligingsupdates levert. [5.20.01]

> **Alleen als: Waar draaien je systemen? «Hostingpartij (IaaS, gedeeld datacenter)»**
>
> 2. Bij een hostingpartij legt het contract de locatie van de datacenters vast, de fysieke beveiliging, de
>    scheiding tussen klanten, de uitwijkvoorziening en de back-updiensten die de organisatie afneemt. [5.20.01]

> **Alleen als: Waar draaien je systemen? «Vooral SaaS en publieke cloud»**
>
> 3. Bij SaaS en publieke cloud gelden aanvullend: inloggen via de eigen identiteitsvoorziening met
>    meerfactorauthenticatie, een jaarlijkse penetratietest door een externe partij met de reikwijdte van de
>    geleverde dienst, het delen van de bevindingen en de hersteltermijnen, afspraken over de locatie van de
>    gegevens, en de mogelijkheid om gegevens zelf te exporteren. [5.20.01, 5.20.03]

> **Alleen als: Stel je eisen aan Europese of soevereine cloud? «Ja: alleen EU of soevereine dienstverlening»**
>
> 4. Bij clouddiensten eist de uitvraag dat gegevens, back-ups en beheer binnen de Europese Economische Ruimte
>    blijven, en dat de leverancier niet onder een buitenlandse wet valt die hem kan dwingen gegevens af te
>    staan zonder tussenkomst van een Europese rechter. De leverancier geeft daarover een verklaring, en het
>    contract regelt wat er gebeurt als dat verandert. [5.20.01]
> 5. Waar de markt geen dienst levert die hieraan voldoet, legt de proceseigenaar de afwijking met het restrisico
>    vast, beoordeelt de CISO die en keurt
>    **[besluitvormer afwijking soevereiniteit]** de afwijking goed vóór
>    ondertekening. [5.20.01]

> **Alleen als: Wie beheert je IT? «Eigen beheer»**
>
> 6. Bij inkoop van beheertools en ondersteuning blijft het beheer bij eigen medewerkers. Het contract regelt
>    dat de leverancier geen standaardtoegang tot de omgeving heeft. [5.20.01]

> **Alleen als: Wie beheert je IT? «Regie: eigen organisatie stuurt, beheer is uitbesteed» of «Volledig uitbesteed»**
>
> 7. Bij inkoop van beheerdiensten regelt het contract ook: screening van het beheerpersoneel van de
>    leverancier, beheertoegang alleen via persoonsgebonden accounts met meerfactorauthenticatie, logging van
>    beheerhandelingen die de organisatie kan inzien, en rapportage over de afgesproken beveiligingsprocessen
>    (patchen, kwetsbaarheden, wijzigingen, back-up). [5.20.01]

### 3.8 Inkoopdossier en overdracht

1. Elk inkoopdossier bevat vóór ondertekening: de risicoafweging, de eisen, de beoordeling van de voorwaarden,
   het eerste bewijs van de leverancier, het overzicht en de beoordeling van de keten, de exitregeling en, waar
   nodig, de verwerkersovereenkomst. Zonder die stukken geeft de CISO geen positief advies en tekent de
   proceseigenaar niet. [5.19.01, 5.20.01]
2. Na ondertekening draagt de inkoopadviseur het inkoopdossier binnen een maand over aan
   **[contracteigenaar]**, zodat het contract in het
   register van leveranciers en contracten komt (beleid contractbeheer). [5.20.01]

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| Proceseigenaar | Risicoafweging per inkoop, besluit over vervallen eisen en restrisico's, afhankelijkheid en exit, keten van toeleveranciers, verwerkersovereenkomst |
| **[inkoopadviseur]** | Opnemen van de eisen in uitvraag en contract, van de hand wijzen van algemene voorwaarden, het inkoopdossier en de overdracht aan contractbeheer |
| CISO | Eigenaar van dit beleid, de standaardset eisen en de lijst onaanvaardbare voorwaarden; advies per inkoop; beoordeling van voorwaarden, bewijs en keten; jaarlijkse toetsing van opzet en werking |
| Privacy officer of FG | Advies over de verwerkersovereenkomst en de verwerking van persoonsgegevens |
| **[contracteigenaar]** | Ontvangst van het inkoopdossier en opname in het register van leveranciers en contracten |

## 5. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in **[registratie van controles]**;
afwijkingen gaan als bevinding naar het risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| INK-01 | Het inkoopdossier bevat vóór ondertekening de risicoafweging en de eisen, en de eisen staan in de uitvraag en het contract | CISO | Per inkoop boven de drempel | Advies van de CISO in het inkoopdossier | 5.19.01, 5.20.01 |
| INK-02 | De algemene voorwaarden van de leverancier zijn van de hand gewezen, of de beoordeling van de voorwaarden en de ondertekening voor de geaccepteerde risico's zitten in het dossier | **[inkoopadviseur]** | Per inkoop | Contract en beoordeling in het inkoopdossier | 5.20.02 |
| INK-03 | Het eerste bewijs van de leverancier is geleverd, dekt de dienst en het auditrecht staat in het contract; restrisico's staan in het risicoregister | CISO | Per inkoop boven de drempel | Rapport of certificaat, beoordeling van de reikwijdte, contract, risicoregister | 5.20.03, 5.20.04 |
| INK-04 | De meldplicht van de leverancier met termijn en inhoud, de exitregeling en, waar nodig, de escrow staan in het contract | **[inkoopadviseur]** | Per inkoop boven de drempel | Contract met de betreffende artikelen | 5.20.05, 5.20.06 |
| INK-05 | Het overzicht van toeleveranciers is geleverd en beoordeeld, en het verbod op overdracht zonder toestemming staat in het contract | CISO | Per inkoop boven de drempel | Overzicht, beoordeling en besluit in het inkoopdossier | 5.21.02 |
| INK-06 | Steekproef van ten minste **[aantal steekproef inkoop]** op volledigheid van het inkoopdossier, toepassing van de drempel en overdracht aan contractbeheer binnen een maand | CISO | Jaarlijks | Verslag van de steekproef met de bevindingen | 5.19.01, 5.20.01, 5.20.02, 5.20.03, 5.20.04, 5.20.05, 5.20.06, 5.21.02 |
| INK-07 | De standaardset eisen en de lijst onaanvaardbare voorwaarden zijn opnieuw vastgesteld | CISO | Jaarlijks | Vastgestelde versie met datum | 5.19.01, 5.20.02 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De
proceseigenaar dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de looptijd. De
afwijking geldt pas na acceptatie van het risico door **[risico-eigenaar]**
en staat in het risicoregister; afwijkingen worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid en het inkoopbeleid van de organisatie. Het
loopt door in het beleid contractbeheer (register, jaarlijkse beoordeling, clouddiensten, beëindiging). Het
raakt het beleid informatieclassificatie (niveau van de eisen), het beleid beveiligingsincidenten (meldplicht
van leveranciers), het beleid back-up en recovery (afspraken met leveranciers over back-up), het
continuïteitsbeleid (exit en uitwijk), het beleid secure software development (eisen aan ontwikkeling door
leveranciers) en het privacybeleid (verwerkersovereenkomst).

## Bijlage A: BIO 2.0-maatregelen

De maatregelen van dit domein (8, waarvan 8 overheidsmaatregelen), waar dit stuk ze invult en welke controle ze aantoont. Nummers volgens BIO2 v1.3 definitief - 9 januari 2026; de tekst van de maatregel staat bij het CIP. Waar de BIO 2.0 geen overheidsmaatregel kent, geldt de ISO 27002-beheersmaatregel.

| Maatregel | Titel | Soort | In dit stuk | Controle |
|---|---|---|---|---|
| 5.19.01 | Informatiebeveiliging in leveranciersrelaties | overheidsmaatregel | 3.1 Risicoafweging en eisen in de uitvraag | INK-01, INK-06, INK-07 |
| 5.20.01 | Adresseren van informatiebeveiliging in leveranciersovereenkomsten | overheidsmaatregel | 3.2 Voorwaarden in het contract | INK-01, INK-06 |
| 5.20.02 | Adresseren van informatiebeveiliging in leveranciersovereenkomsten | overheidsmaatregel | 3.2 Voorwaarden in het contract | INK-02, INK-06, INK-07 |
| 5.20.03 | Adresseren van informatiebeveiliging in leveranciersovereenkomsten | overheidsmaatregel | 3.3 Bewijs van de leverancier en eigen onderzoek | INK-03, INK-06 |
| 5.20.04 | Adresseren van informatiebeveiliging in leveranciersovereenkomsten | overheidsmaatregel | 3.3 Bewijs van de leverancier en eigen onderzoek | INK-03, INK-06 |
| 5.20.05 | Adresseren van informatiebeveiliging in leveranciersovereenkomsten | overheidsmaatregel | 3.4 Transparantie over kwetsbaarheden en incidenten | INK-04, INK-06 |
| 5.20.06 | Adresseren van informatiebeveiliging in leveranciersovereenkomsten | overheidsmaatregel | 3.5 Afhankelijkheid en exit | INK-04, INK-06 |
| 5.21.02 | Beheren van informatiebeveiliging in de ICT-toeleveringsketen | overheidsmaatregel | 3.6 Keten van toeleveranciers | INK-05, INK-06 |

## Bijlage B: Afkortingen

| Afkorting | Betekenis |
|---|---|
| ARBIT | Algemene Rijksvoorwaarden bij IT-overeenkomsten, de standaard inkoopvoorwaarden voor IT van het Rijk |
| CISO | Chief Information Security Officer |
| EU | Europese Unie |
| FG | Functionaris gegevensbescherming |
| GIBIT | Gemeentelijke inkoopvoorwaarden bij IT |
| ISAE | International Standard on Assurance Engagements |
| ISO | International Organization for Standardization |
| IT | Informatietechnologie |
| IaaS | Infrastructure as a service |
| SaaS | Software as a service |

## Nog in te vullen

- **inkoopadviseur**: de functie die het inkoopproces begeleidt
- **drempel risicoafweging inkoop**: de criteria waaronder een inkoop met de standaardset eisen kan
- **lijst onaanvaardbare voorwaarden**: bijvoorbeeld eenzijdig wijzigen van de beveiligingsafspraken of gebruik van gegevens voor eigen doelen van de leverancier
- **meldtermijn leverancier**: bijvoorbeeld 12 uur, zodat de vroege waarschuwing binnen 24 uur kan
- **besluitvormer afwijking soevereiniteit**: wie de afwijking goedkeurt
- **contracteigenaar**: de functie die het contract na ondertekening beheert
- **registratie van controles**: het systeem waarin controles worden vastgelegd, bijvoorbeeld het ticketsysteem of het managementsysteem
- **aantal steekproef inkoop**: bijvoorbeeld vijf inkopen met een informatiecomponent
- **risico-eigenaar**: de manager die restrisico's accepteert
- **eigenaar van dit beleid**: de manager die dit beleid uitvoert en laat naleven
- **vaststeller**: wie het beleid vaststelt, bijvoorbeeld de directie of het bestuur
