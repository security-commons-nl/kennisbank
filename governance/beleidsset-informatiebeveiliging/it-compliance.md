# Beleid IT-compliance

Word nodig? Kies dit stuk in de [generator](beleidsset-generator.html) en download het daar, zonder of met je eigen antwoorden.

| | |
|---|---|
| Documenttype | Beleid informatiebeveiliging onder het strategisch informatiebeveiligingsbeleid; BIO 2.0-domein *IT-Compliance* |
| Status | Concept, vast te stellen door de organisatie |
| Eigenaar | **[eigenaar van dit beleid]** |
| Vaststeller | **[vaststeller]** |
| Evaluatie | Jaarlijks, in de plan-do-check-act-cyclus van het managementsysteem voor informatiebeveiliging |

**In het kort.** Over de naleving van wet- en regelgeving en contractuele eisen voor informatie en systemen. Behandelt het register van eisen, licenties, bewaartermijnen, privacy en testgegevens, clear desk en clear screen, capaciteit en kloksynchronisatie, en audits op productiesystemen.

**Onderwerpen.** 3. Wettelijke en contractuele eisen; 4. Registraties en bewaartermijnen; 5. Privacy en persoonsgegevens; 6. Clear desk en clear screen; 7. Techniek ter ondersteuning van naleving; 8. Audits op informatiesystemen.

Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor de naleving van wet- en regelgeving
en contractuele eisen die op informatie en informatiesystemen van de organisatie rusten. Het regelt hoe de
organisatie weet welke eisen gelden, hoe registraties en bewaartermijnen zijn ingericht, hoe
persoonsgegevens en intellectueel eigendom worden beschermd, hoe werkplekken en schermen worden
afgeschermd, welke technische voorzieningen de naleving ondersteunen en hoe systemen tijdens audits
beschermd blijven. Het gaat over de ISO-beheersmaatregelen 5.31 tot en met 5.34, 7.7, 8.6, 8.11, 8.12,
8.17 en 8.34.

**Voor wie.** Het beleid is primair bedoeld voor proceseigenaren, de archieffunctie, de privacy officer,
de juridische functie, de IT-organisatie en de CISO. De regels over clear desk en clear screen gelden voor
iedereen die onder verantwoordelijkheid van de organisatie met informatie werkt: medewerkers, inhuur,
stagiairs en vrijwilligers.

**Waarop.** Alle informatiesystemen in de scope van het managementsysteem, de registraties die de
organisatie wettelijk of contractueel moet bijhouden, de werkplekken en vergaderruimten waar informatie
wordt gebruikt, en de test- en ontwikkelomgevingen. Is het beheer van systemen, de archivering of de
bewaking van capaciteit uitbesteed, dan gelden de eisen uit dit beleid als minimumeis voor die partij. De
organisatie legt dat vast in het contract en toetst de naleving met een onafhankelijke verklaring, zoals
een ISO 27001-certificaat of een ISAE 3402- of ISAE 3000-rapport; het vastleggen loopt via het beleid
informatiebeveiliging bij inkoop, het toetsen via het beleid contractbeheer.

Buiten dit beleid vallen de privacymaatregelen zelf (privacybeleid), de inhoud en bewaring van logging
(beleid logging en monitoring), het toekennen van toegangsrechten (beleid logische toegangsbeveiliging), de
fysieke beveiliging van ruimten (beleid fysieke toegang en beveiliging) en het auditplan van het
managementsysteem (strategisch informatiebeveiligingsbeleid).

## 2. Uitgangspunten

1. De proceseigenaar weet welke wettelijke en contractuele eisen op zijn proces rusten en is verantwoordelijk
   voor de naleving.
2. Informatie wordt niet langer bewaard dan nodig, en niet korter dan de wet voorschrijft.
3. Naleving is aantoonbaar met registraties die de organisatie zelf bijhoudt.
4. Echte gegevens horen in productie; test- en ontwikkelomgevingen werken met gemaskeerde of fictieve
   gegevens.
5. Informatie is alleen zichtbaar voor wie haar nodig heeft, ook op het bureau en op het scherm.
6. Termijnen en frequenties in dit beleid die niet uit een wet of uit de BIO 2.0 komen, zijn standaardwaarden.
   De organisatie past ze aan op haar eigen risicoafweging en legt de keuze vast bij de vaststelling van dit beleid.

## 3. Wettelijke en contractuele eisen

1. De CISO houdt samen met de privacy officer en de juridische functie een register bij van de wet- en
   regelgeving en de contractuele eisen die gelden voor informatiebeveiliging, met per eis de eigenaar en het
   beleidsstuk waarin hij is uitgewerkt. Het register wordt jaarlijks en bij elke relevante wetswijziging
   bijgewerkt; de versie met datum is het bewijs. [5.31.01]
2. Het register bevat ten minste de AVG, de Archiefwet, de Wet open overheid, de Cyberbeveiligingswet waar
   die geldt, de sectorale wetgeving van de eigen taken en de beveiligingseisen uit contracten met
   leveranciers en ketenpartners. [5.31.01]
3. De proceseigenaar stelt jaarlijks vast welke eisen uit het register op het eigen proces rusten en toont
   met de controleraamwerken van de materie-specifieke stukken aan dat ze worden nageleefd. Een eis zonder
   beleidsstuk of controle meldt de proceseigenaar als bevinding bij de CISO. [5.31.01]
4. Bij een nieuw systeem of een nieuwe verwerking beoordeelt de proceseigenaar met de risicoafweging uit het
   beleid informatiebeveiliging in projecten welke eisen uit het register gelden en neemt ze op in het
   programma van eisen. [5.31.01]
5. De organisatie gebruikt alleen software waarvoor zij een geldige licentie heeft. De IT-organisatie houdt
   een licentieregister bij, vergelijkt het jaarlijks met de geïnstalleerde software en verwijdert of
   legaliseert wat niet klopt. [5.32.01]
6. Medewerkers installeren geen software en gebruiken geen inhoud (teksten, beelden, muziek, broncode)
   waarvoor de organisatie geen gebruiksrecht heeft. De gedragsregels voor informatiegebruik noemen dit; de
   IT-organisatie staat alleen installatie toe vanuit de goedgekeurde bronnen uit het beleid
   bedrijfsmiddelenbeheer. [5.32.01]
7. Voor software, documenten en gegevens die de organisatie zelf laat maken, legt de opdrachtgever in het
   contract vast wie de eigenaar is en welke gebruiksrechten de organisatie heeft. Bij open-sourcesoftware
   legt de IT-organisatie vast onder welke licentie die wordt gebruikt en of de organisatie aan de
   voorwaarden voldoet. [5.32.01]

> **Alleen als: Verwerk je politiegegevens (boa's, opsporing, handhaving)? «Ja»**
>
> 8. De organisatie verwerkt politiegegevens, bijvoorbeeld door boa's of bij handhaving en opsporing. Voor die
>    verwerkingen geldt de Wet politiegegevens naast de AVG. Het register noemt per verwerking het doel uit de
>    Wpg, de geautoriseerde functies en de bewaartermijn. [5.31.01, 5.34.01]
> 9. Autorisaties voor politiegegevens worden per persoon verleend en ten minste halfjaarlijks door de
>    proceseigenaar gecontroleerd. Elke raadpleging en wijziging wordt gelogd; de logging wordt bewaard zolang
>    de Wpg voorschrijft. [5.31.01, 5.33.01]
> 10. Over de verwerking van politiegegevens laat de verwerkingsverantwoordelijke eenmaal in de vier jaar de
>    privacy-audit uitvoeren door een onafhankelijke auditor (artikel 33 Wpg, artikel 6:5 Besluit
>    politiegegevens), zendt een afschrift van de controleresultaten aan de Autoriteit Persoonsgegevens en laat
>    bij tekortkomingen binnen een jaar een hercontrole uitvoeren. [5.31.01]

> **Alleen als: Op welke landelijke voorzieningen ben je aangesloten? «DigiD» of «Suwinet» of «BRP (als bronhouder of afnemer)» of «BAG of andere basisregistraties» of «Andere ketens met eigen beveiligingseisen»**
>
> 11. De organisatie is aangesloten op landelijke voorzieningen met een eigen beveiligings- en auditregime. Het
>    register noemt per aansluiting het normenkader, de eigenaar en de termijn van de verantwoording. [5.31.01]

> **Alleen als: Op welke landelijke voorzieningen ben je aangesloten? «DigiD»**
>
> 12. Voor de DigiD-aansluiting laat de proceseigenaar jaarlijks een ICT-beveiligingsassessment door een
>    onafhankelijke auditor uitvoeren en levert het rapport op tijd aan bij de beheerder van DigiD. [5.31.01]

> **Alleen als: Op welke landelijke voorzieningen ben je aangesloten? «Suwinet»**
>
> 13. Voor Suwinet legt de organisatie jaarlijks verantwoording af over de normen voor gebruik en beveiliging.
>    De proceseigenaar controleert per kwartaal de autorisaties en steekproefsgewijs de raadplegingen op
>    doelbinding. [5.31.01]

> **Alleen als: Op welke landelijke voorzieningen ben je aangesloten? «BRP (als bronhouder of afnemer)»**
>
> 14. Voor de BRP voert de organisatie de jaarlijkse zelfevaluatie of audit uit die de beheerder van de BRP
>    voorschrijft, en controleert de proceseigenaar de autorisaties ten minste jaarlijks. [5.31.01]

> **Alleen als: Op welke landelijke voorzieningen ben je aangesloten? «BAG of andere basisregistraties»**
>
> 15. Voor de BAG en andere basisregistraties waarvoor de organisatie bronhouder is, voert de proceseigenaar de
>    verplichte kwaliteitscontroles en audits uit en volgt de bevindingen op. [5.31.01]

> **Alleen als: Op welke landelijke voorzieningen ben je aangesloten? «Andere ketens met eigen beveiligingseisen»**
>
> 16. Voor andere ketens met eigen beveiligingseisen staat het normenkader en de wijze van verantwoording in
>    **[overzicht overige ketens]**, dat de CISO
>    jaarlijks met de keteneigenaren doorneemt. [5.31.01]

## 4. Registraties en bewaartermijnen

1. De proceseigenaar legt voor elk informatiesysteem en elke categorie informatie de bewaartermijn vast, op
   basis van de geldende selectielijst, de Archiefwet, de privacywetgeving en de eigen bedrijfsdoelen. De
   termijnen staan in het verwerkingsregister of in een overzicht dat
   **[lijneigenaar archief]**
   bijhoudt. [5.33.01]
2. De proceseigenaar zorgt dat het systeem de termijnen ook uitvoert: vernietiging, overbrenging of
   anonimisering na afloop, automatisch waar het systeem dat kan en volgens een vast schema waar dat niet
   kan. Het vernietigingsverslag of de overbrengingsverklaring is het bewijs. [5.33.01]
3. De proceseigenaar toetst ten minste jaarlijks met een steekproef of informatie na afloop van de termijn
   daadwerkelijk is vernietigd of overgebracht, en legt de uitkomst vast. [5.33.01]
4. Bij aanschaf of vervanging van een systeem is de mogelijkheid om bewaartermijnen uit te voeren een eis in
   het programma van eisen. [5.33.01]
5. Registraties die als bewijs dienen, zoals logging, besluiten, contracten en audittrails, zijn beschermd
   tegen wijziging en voortijdige verwijdering: de IT-organisatie richt ze zo in dat alleen een beperkte
   groep ze kan wijzigen, dat elke wijziging wordt gelogd en dat ze in de back-up zitten volgens het beleid
   back-up en recovery. [5.33.01]
6. Registraties die de organisatie jarenlang moet bewaren, blijven leesbaar: de archieffunctie bewaakt dat
   bestandsformaten en opslagmedia bij elke systeemvervanging worden omgezet of gemigreerd, en legt dat vast
   in het overzicht van bewaartermijnen. [5.33.01]

## 5. Privacy en persoonsgegevens

1. De privacymaatregelen staan in het privacybeleid. Dit beleid regelt de raakvlakken: het register van eisen
   (hoofdstuk 3) en de bewaartermijnen (hoofdstuk 4) gelden ook voor persoonsgegevens, en de
   proceseigenaar neemt de privacyeisen mee in dezelfde jaarlijkse toets. [5.34.01]
2. De organisatie heeft een privacybeleid dat het bestuur vaststelt, een functionaris gegevensbescherming
   die onafhankelijk toezicht houdt en een verwerkingsregister dat de privacy officer bijhoudt. Elke
   verwerking van persoonsgegevens staat in dat register voordat ze start; de proceseigenaar meldt nieuwe
   verwerkingen bij de privacy officer. [5.34.01]
3. Bij elke nieuwe verwerking of wijziging van een verwerking beoordeelt de privacy officer of een DPIA
   nodig is, volgens het beleid informatiebeveiliging in projecten. Een datalek wordt gemeld en afgehandeld
   volgens het beleid beveiligingsincidenten, met de FG in de meldroute naar de Autoriteit Persoonsgegevens.
   [5.34.01]
4. De proceseigenaar beperkt de toegang tot persoonsgegevens tot de functies die ze voor hun taak nodig
   hebben en legt die functies vast in de autorisatiematrix uit het beleid logische toegangsbeveiliging; de
   privacy officer toetst de matrix jaarlijks op doelbinding. [5.34.01]
5. In test-, ontwikkel- en opleidingsomgevingen gebruikt de organisatie geen echte persoonsgegevens en geen
   andere informatie met het label vertrouwelijk of hoger. Wie zo'n omgeving vult, gebruikt fictieve
   gegevens of een gemaskeerde kopie. [8.11.01]
6. Is een gemaskeerde kopie van productiegegevens nodig, dan maskeert of pseudonimiseert de IT-organisatie
   de gegevens voordat ze de productieomgeving verlaten, zo dat een persoon of een vertrouwelijk gegeven niet
   meer te herleiden is. De privacy officer stemt vooraf in; de proceseigenaar legt vast welke velden zijn
   gemaskeerd en met welke techniek. [8.11.01]
7. Maakt een productiesysteem gegevens zichtbaar aan gebruikers die niet alles mogen zien, dan toont het
   systeem alleen het deel dat voor de taak nodig is, bijvoorbeeld een gedeeltelijk burgerservicenummer of
   bankrekeningnummer. De proceseigenaar legt bij de autorisatiematrix vast welke gegevens voor welke
   functie worden afgeschermd. [8.11.01]
8. De IT-organisatie zet technische maatregelen in tegen het onbedoeld weglekken van informatie met het
   label vertrouwelijk of hoger: ten minste een waarschuwing of blokkade bij het versturen naar externe
   adressen, bij het uploaden naar niet-goedgekeurde clouddiensten en bij het kopiëren naar verwisselbare
   media. De keuze per kanaal volgt uit de risicoanalyse en staat in
   **[overzicht DLP-maatregelen]**.
   [8.12.01]
9. De CISO beoordeelt elk kwartaal de meldingen van die maatregelen op patronen (welke kanalen, welke
   afdelingen, welke labels) en legt de uitkomst en de opvolging vast; een bevestigd lek wordt behandeld als
   incident volgens het beleid beveiligingsincidenten. [8.12.01]

> **Alleen als: Verwerk je politiegegevens (boa's, opsporing, handhaving)? «Ja»**
>
> 10. Testomgevingen bevatten nooit politiegegevens, ook niet gemaskeerd; de proceseigenaar gebruikt
>    uitsluitend fictieve gegevens. [8.11.01]

## 6. Clear desk en clear screen

1. Medewerkers laten geen informatie met het label intern of hoger onbeheerd achter op hun werkplek, in
   vergaderruimten of op gedeelde plekken. Aan het einde van de werkdag en bij het verlaten van een gedeelde
   werkplek bergen zij documenten en gegevensdragers op in een afsluitbare kast of lade. [7.07.01]
2. Wie de werkplek verlaat, vergrendelt het scherm, ook voor een korte onderbreking. Medewerkers zetten
   schermen met informatie met het label vertrouwelijk of hoger zo neer dat bezoekers en voorbijgangers niet
   kunnen meekijken; waar dat niet kan, gebruiken zij een privacyfilter. [7.07.01]
3. De IT-organisatie stelt op alle werkplekken en mobiele apparaten een automatische vergrendeling in na
   **[vergrendeltijd]**
   minuten zonder activiteit, centraal beheerd, zodat gebruikers de instelling niet kunnen uitzetten.
   [7.07.01]
4. Waar toegang tot systemen werkt met een chipcard, pas of andere fysieke token, vergrendelt de werkplek
   automatisch zodra het token wordt verwijderd. De IT-organisatie stelt dat centraal in. Werkt de
   organisatie nog niet met een fysieke token, dan is die vergrendeling een eis bij de invoering en bij de
   aanschaf. [7.07.01]
5. Afdrukken van informatie met het label intern of hoger worden direct uit de printer gehaald. Printers op
   gedeelde plekken drukken alleen af na identificatie van de gebruiker bij het apparaat. De IT-organisatie
   verwijdert afdruktaken die na
   **[bewaartermijn afdruktaken]**
   niet zijn opgehaald. [7.07.01]
6. Na een vergadering wist de voorzitter whiteboards en flip-overs en neemt hij achtergebleven documenten
   mee. Medewerkers gooien informatie met het label intern of hoger alleen weg via de afgesloten
   papiercontainer of de versnipperaar. [7.07.01]
7. **[lijneigenaar werkplek]** loopt
   elk halfjaar een rondgang clear desk over alle locaties, legt de bevindingen per afdeling vast en meldt
   ze aan de leidinggevenden, die medewerkers aanspreken. [7.07.01]

## 7. Techniek ter ondersteuning van naleving

1. De IT-organisatie bewaakt doorlopend de capaciteit van de kritieke systemen uit het overzicht van
   kritieke systemen: opslag, rekenkracht, geheugen en netwerk. De bewaking geeft een melding bij
   **[drempel capaciteit]**
   van de beschikbare capaciteit, zodat de IT-organisatie uitbreidt voordat de beschikbaarheid wordt geraakt.
   [8.06.01]
2. De IT-organisatie stelt jaarlijks met de proceseigenaren een capaciteitsprognose op voor de komende twaalf
   maanden, op basis van het gebruik van het afgelopen jaar en de verwachte veranderingen (nieuwe systemen,
   meer gebruikers, langere bewaartermijnen), en legt vast welke uitbreidingen daaruit volgen. [8.06.01]
3. Is de hosting uitbesteed, dan legt de organisatie in het contract vast welke capaciteit is afgesproken en
   hoe de leverancier dreigende tekorten meldt; contractbeheer toetst dat met de rapportage van de
   leverancier. [8.06.01]
4. Alle systemen, netwerkapparaten en werkplekken synchroniseren hun klok met
   **[tijdbron]**,
   die zelf is gekoppeld aan een betrouwbare externe bron. Alle logging gebruikt die tijd, in één
   vastgelegde tijdzone of met de tijdzone erbij, zodat logging uit verschillende systemen vergelijkbaar is.
   [8.17.01]
5. De IT-organisatie controleert elk kwartaal dat de systemen in de scope met de tijdbron synchroniseren en
   dat de afwijking kleiner is dan één seconde, en herstelt afwijkingen. De rapportage uit de bewaking is het
   bewijs. [8.17.01]

## 8. Audits op informatiesystemen

1. Audits, pentests en andere technische tests op productiesystemen worden vooraf afgestemd tussen de
   auditor, de systeemeigenaar en de IT-organisatie en vastgelegd in een testopdracht: wat wordt getest, door
   wie, wanneer, met welke rechten, vanaf welke adressen en wie bij een verstoring wordt gewaarschuwd.
   [8.34.01]
2. Auditors krijgen alleen-lezen toegang, tenzij de testopdracht anders zegt. De IT-organisatie verleent de
   rechten op een apart account voor de duur van de test en trekt ze direct na afloop in; de aanvraag en de
   intrekking staan in het ticketsysteem. [8.34.01]
3. Tests die de beschikbaarheid kunnen raken of gegevens kunnen wijzigen, gebeuren buiten piektijden, op een
   kopie of in een afgeschermde testomgeving. Een test op productie die gegevens kan wijzigen, vraagt vooraf
   toestemming van de systeemeigenaar en een actuele back-up. [8.34.01]
4. De auditor krijgt alleen kopieën of exports van de gegevens die voor de audit nodig zijn, met de
   classificatie erbij. De auditor bewaart ze volgens die classificatie en vernietigt ze na afloop van de
   audit; dat staat in de testopdracht of het contract. [8.34.01]
5. De IT-organisatie logt de handelingen van de auditor op de productiesystemen en bewaart de logging volgens
   het beleid logging en monitoring, zodat na de audit is na te gaan wat is gedaan. [8.34.01]

> **Alleen als: Welke eigen security-capaciteit heb je? «Geen eigen ISO; informatiebeveiliging is een neventaak»**
>
> 6. Zonder eigen ISO houdt
>    **[functionaris informatiebeveiliging]**
>    het register uit hoofdstuk 3 bij. De jaarlijkse controle op het register en op de steekproef
>    bewaartermijnen wordt belegd bij de CISO-invulling of de interne controle. [5.31.01, 5.33.01]

> **Alleen als: Welke eigen security-capaciteit heb je? «Een ISO of CISO in deeltijd» of «Een eigen team (CISO met ISO's)»**
>
> 7. De ISO of CISO houdt het register uit hoofdstuk 3 bij en voert de jaarlijkse controle op de
>    bewaartermijnen uit samen met de archieffunctie. [5.31.01, 5.33.01]

## 9. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| Proceseigenaar | Naleving van de eisen op het eigen proces, bewaartermijnen vastleggen, uitvoeren en toetsen, afscherming van gegevens per functie, toestemming voor tests op productie |
| **[lijneigenaar archief]** | Overzicht van bewaartermijnen, selectielijst, leesbaarheid van registraties, ondersteuning bij vernietiging en overbrenging |
| CISO of ISO | Register van eisen, beoordeling van meldingen van gegevenslekken, advies, controle op naleving |
| Privacy officer en FG | Privacyeisen, verwerkingsregister, DPIA-plicht, instemming met maskeren; de FG houdt toezicht |
| Juridische functie | Toets van het register van eisen en van de contracten over eigendom en gebruiksrechten |
| IT-organisatie | Licentieregister, automatische vergrendeling, maskeren, maatregelen tegen gegevenslekken, capaciteit, kloksynchronisatie, begeleiding van audits |
| **[lijneigenaar werkplek]** | Rondgang clear desk, afsluitbare opslag, printers en papiercontainers |
| Contractbeheer | Toets van capaciteit en naleving bij uitbestede hosting en beheer |
| Medewerkers | Clear desk en clear screen, geen software of inhoud zonder gebruiksrecht |

## 10. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in **[registratie van controles]**;
afwijkingen gaan als bevinding naar het risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| ITC-01 | Het register van wettelijke en contractuele eisen is in het afgelopen jaar bijgewerkt, elke eis heeft een eigenaar en een beleidsstuk, en elke proceseigenaar heeft de toets op het eigen proces uitgevoerd | CISO | Jaarlijks | Register met datum en lijst van wijzigingen, toetsverslagen van de proceseigenaren | 5.31.01 |
| ITC-02 | De geïnstalleerde software komt overeen met het licentieregister en voor zelf gemaakte software en inhoud is het eigendom in het contract vastgelegd | IT-organisatie | Jaarlijks | Vergelijking van de software-inventarisatie met het licentieregister, steekproef van vijf contracten | 5.32.01 |
| ITC-03 | Voor elk kritiek systeem zijn de bewaartermijnen vastgelegd en uitgevoerd, en de registraties die als bewijs dienen zijn beschermd tegen wijziging | Proceseigenaar | Jaarlijks | Steekproef per kritiek systeem: overzicht van termijnen, vernietigingsverslag of overbrengingsverklaring, autorisaties op de registraties | 5.33.01 |
| ITC-04 | Elke verwerking van persoonsgegevens staat in het verwerkingsregister, de autorisaties op persoonsgegevens zijn op doelbinding getoetst en test- en ontwikkelomgevingen bevatten geen ongemaskeerde persoonsgegevens | Privacy officer | Jaarlijks | Verwerkingsregister, toetsverslag van de autorisatiematrix, steekproef van ten minste drie testomgevingen met de maskeringsregistratie | 5.34.01, 8.11.01 |
| ITC-05 | De maatregelen tegen gegevenslekken staan aan op alle kanalen uit het overzicht en de meldingen zijn elk kwartaal beoordeeld en opgevolgd | CISO | Per kwartaal | Configuratie-export per kanaal, beoordelingsverslag met de opgevolgde meldingen | 8.12.01 |
| ITC-06 | Automatische vergrendeling op inactiviteit en bij verwijderen van een token staat aan op alle werkplekken en mobiele apparaten, en de rondgang clear desk is uitgevoerd en opgevolgd | **[lijneigenaar werkplek]** | Halfjaarlijks | Configuratie-export uit het werkplekbeheer, verslag van de rondgang met de bevindingen per afdeling | 7.07.01 |
| ITC-07 | De capaciteit van de kritieke systemen is bewaakt, meldingen boven de drempel zijn opgevolgd en de jaarlijkse capaciteitsprognose is opgesteld | IT-organisatie | Per kwartaal | Rapportage uit de bewaking, opgevolgde meldingen, capaciteitsprognose, rapportage van de hostingleverancier | 8.06.01 |
| ITC-08 | Alle systemen in de scope synchroniseren met de tijdbron en de afwijking is kleiner dan één seconde | IT-organisatie | Per kwartaal | Rapportage uit de bewaking van de kloksynchronisatie | 8.17.01 |
| ITC-09 | Elke audit of test op een productiesysteem had een testopdracht, de rechten zijn na afloop ingetrokken en de handelingen zijn gelogd | CISO | Jaarlijks | Testopdrachten van het afgelopen jaar, tickets van verlening en intrekking, logging | 8.34.01 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De
proceseigenaar dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de looptijd.
De afwijking geldt pas na acceptatie van het risico door **[risico-eigenaar]**
en staat in het risicoregister; afwijkingen worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 11. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het privacybeleid
(persoonsgegevens, verwerkingsregister en bewaartermijnen), het beleid logische toegangsbeveiliging
(vergrendeling en autorisaties), het beleid logging en monitoring (bewaren van logging en
kloksynchronisatie), het beleid informatieclassificatie (labels voor clear desk, maskeren en
gegevenslekken), het beleid bedrijfsmiddelenbeheer (goedgekeurde software en gegevensdragers), het beleid
back-up en recovery (bescherming van registraties), het beleid beveiligingsincidenten (datalekken), het
beleid informatiebeveiliging in projecten (eisen en DPIA bij nieuwe systemen), het beleid secure software
development (testdata) en het beleid informatiebeveiliging bij inkoop en het beleid contractbeheer
(capaciteit en eigendom bij leveranciers).

## Bijlage A: BIO 2.0-maatregelen

De maatregelen van dit domein (10, waarvan 2 overheidsmaatregelen), waar dit stuk ze invult en welke controle ze aantoont. Nummers volgens BIO2 v1.3 definitief - 9 januari 2026; de tekst van de maatregel staat bij het CIP. Waar de BIO 2.0 geen overheidsmaatregel kent, geldt de ISO 27002-beheersmaatregel.

| Maatregel | Titel | Soort | In dit stuk | Controle |
|---|---|---|---|---|
| 5.31.01 | Wettelijke, statutaire, regelgevende en contractuele eisen | ISO-beheersmaatregel | 3. Wettelijke en contractuele eisen | ITC-01 |
| 5.32.01 | Intellectuele-eigendomsrechten | ISO-beheersmaatregel | 3. Wettelijke en contractuele eisen | ITC-02 |
| 5.33.01 | Beschermen van registraties | overheidsmaatregel | 3. Wettelijke en contractuele eisen | ITC-03 |
| 5.34.01 | Privacy en bescherming van persoonsgegevens | ISO-beheersmaatregel | 3. Wettelijke en contractuele eisen | ITC-04 |
| 7.07.01 | ‘Clear desk’ en ‘clear screen’ | overheidsmaatregel | 6. Clear desk en clear screen | ITC-06 |
| 8.06.01 | Capaciteitsbeheer | ISO-beheersmaatregel | 7. Techniek ter ondersteuning van naleving | ITC-07 |
| 8.11.01 | Maskeren van gegevens | ISO-beheersmaatregel | 5. Privacy en persoonsgegevens | ITC-04 |
| 8.12.01 | Voorkomen van gegevenslekken (data leakage prevention) | ISO-beheersmaatregel | 5. Privacy en persoonsgegevens | ITC-05 |
| 8.17.01 | Kloksynchronisatie | ISO-beheersmaatregel | 7. Techniek ter ondersteuning van naleving | ITC-08 |
| 8.34.01 | Bescherming van informatiesystemen tijdens audits | ISO-beheersmaatregel | 8. Audits op informatiesystemen | ITC-09 |

## Bijlage B: Afkortingen

| Afkorting | Betekenis |
|---|---|
| AVG | Algemene verordening gegevensbescherming |
| BAG | Basisregistratie Adressen en Gebouwen |
| BIO | Baseline Informatiebeveiliging Overheid |
| BRP | Basisregistratie Personen |
| CISO | Chief Information Security Officer |
| DLP | Data leakage prevention, het voorkomen van gegevenslekken |
| DPIA | Data protection impact assessment, een gegevensbeschermingseffectbeoordeling |
| FG | Functionaris gegevensbescherming |
| ICT | Informatie- en communicatietechnologie |
| ISAE | International Standard on Assurance Engagements |
| ISO | International Organization for Standardization |
| IT | Informatietechnologie |
| Wpg | Wet politiegegevens |

## Nog in te vullen

- **overzicht overige ketens**: per keten het normenkader, de eigenaar en de auditcyclus
- **lijneigenaar archief**: de functie die de archieffunctie uitvoert, bijvoorbeeld de DIV-coördinator
- **overzicht DLP-maatregelen**: het overzicht van kanalen met de maatregel per kanaal, bijvoorbeeld in het beheerdossier van de werkplek
- **vergrendeltijd**: het aantal minuten inactiviteit, bijvoorbeeld 10
- **bewaartermijn afdruktaken**: de termijn waarna een niet-opgehaalde afdruktaak vervalt, bijvoorbeeld 24 uur
- **lijneigenaar werkplek**: de manager die de werkplekken beheert, bijvoorbeeld facilitaire zaken
- **drempel capaciteit**: het gebruikspercentage waarbij een melding volgt, bijvoorbeeld 80 procent
- **tijdbron**: de betrouwbare tijdbron van de organisatie, bijvoorbeeld de eigen NTP-servers of de tijdservers van de overheid
- **functionaris informatiebeveiliging**: de medewerker met de neventaak informatiebeveiliging
- **registratie van controles**: het systeem waarin controles worden vastgelegd, bijvoorbeeld het ticketsysteem of het managementsysteem
- **risico-eigenaar**: de manager die restrisico's accepteert
- **eigenaar van dit beleid**: de manager die dit beleid uitvoert en laat naleven
- **vaststeller**: wie het beleid vaststelt, bijvoorbeeld de directie of het bestuur
