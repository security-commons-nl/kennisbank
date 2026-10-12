# Beleid logische toegangsbeveiliging

> **Concept, niet vastgesteld.** Dit stuk staat hier als voorbeeld van een uitgewerkt concept. Neem het niet over als vastgesteld beleid.

### Afkortingen

| Afkorting | Omschrijving |
|---|---|
| BIO | Baseline Informatiebeveiliging Overheid |
| BRP | Basisregistratie Personen |
| CISO | Chief Information Security Officer |
| DAP | Document Afspraken en Procedures |
| ISO | Information Security Officer |

### Relevante beleidsdocumenten

- Baseline Informatiebeveiliging Overheid (BIO)

- Strategisch Gemeentelijk Informatiebeveiligingsbeleid

- Procedure Autorisatiebeheer

- Controleprocedure

- Wachtwoordbeleid

- Telewerkbeleid

- Beleid dataclassificatie

## Inleiding

Logische toegangsbeveiliging vormt een belangrijk aspect van de gemeentelijke informatiebeveiliging. Logische toegangsbeveiliging zorgt ervoor dat onbevoegden minder makkelijk toegang kunnen krijgen tot gemeentelijke informatiesystemen en de informatie binnen deze gemeentelijke informatiesystemen. Het kan hierbij ook gaan om bedrijfsinformatie van derde partijen, waarvan de gemeente niet de bronhouder is, indien deze via het gemeentelijk platform ontsloten en beschikbaar gesteld wordt, bijvoorbeeld Basisregistratie Personen (BRP) en Suwinet. Alle gebruikers van gemeentelijke informatiesystemen dienen, volgens logische toegangsbeveiliging procedures, geautoriseerd te worden.

Risico’s

Door het ontbreken van adequate logische toegangsbeveiliging bestaat het risico dat onbevoegden (hieronder vallen ook exmedewerkers en externen) zich toegang kunnen verschaffen tot gemeentelijke informatiesystemen en de informatie binnen deze gemeentelijke informatiesystemen, waardoor ongewenste acties op de diensten kunnen plaatsvinden en/of informatie kan worden ontvreemd of verminkt.

Onduidelijke of niet gevolgde logische toegangsbeveiliging procedures zijn niet alleen een bedreiging voor de vertrouwelijkheid en integriteit van gemeentelijke informatie, maar uiteindelijk ook slecht voor het imago.

## Uitgangspunten

De organisatie hanteert de volgende beleidsuitgangspunten uit de BIO:

### Eigenaarschap

- Het beleid logische toegangsbeveiliging is van toepassing op informatiesystemen waarvan de uitvoeringsorganisatie-gemeenten eigenaar zijn. Ook als informatiesystemen niet intern, of intern door externe partijen beheerd worden is het beleid logische toegangsbeveiliging van toepassing.

- Voor elk bedrijfsproces, informatiesysteem, gegevensverzameling is een verantwoordelijke systeemeigenaar benoemd.

- Iedere systeemeigenaar is verplicht tot het uitvoeren van een baselinetoets BIO en, afhankelijk van de uitkomsten van deze baselinetoetsook nog voor een diepgaande risicoanalyse voor de informatiesystemen waarvan hij eigenaar is.

- Iedere systeemeigenaar is verplicht tot het maken van een specifieke autorisatieprocedure voor elk informatiesysteem waarvan hij eigenaar is.

- Iedere systeemeigenaar is verplicht tot het toepassen van de specifieke autorisatieprocedures voor de informatiesystemen waarvan hij eigenaar is.

- De systeemeigenaar dient bij het opstellen en uitvoeren van een specifieke autorisatieprocedure de volgende uitgangspunten te hanteren:

- De autorisatiestructuur van een informatiesysteem is uniform voor alle gebruikers.

- De autorisatiestructuur van een informatiesysteem sluit aan bij de goedgekeurde procesbeschrijvingen.

- Er worden in de regel geen ‘algemene’ (ongepersonaliseerde) identiteiten gebruikt; Activiteiten zijn altijd te herleiden tot één persoon.

- Gegevens worden alleen gemuteerd door de gegevenseigenaar of de daartoe, door de gegevenseigenaar, gemachtigde functionarissen.

- De systeemeigenaar overlegt met de betrokken gegevenseigenaren en proceseigenaren over de vraag wie geautoriseerd wordt en op welke manier dat gebeurt.

- De systeemeigenaar is verplicht de autorisatieprocedure te laten toetsen door de aangewezen beveiligingsfunctionaris/het team IB&P binnen de uitvoeringsorganisatie.

- De systeemeigenaar dient bij het opstellen van een autorisatieprocedure rekening te houden met mogelijk van toepassing zijnde wet- en regelgeving.

- De systeemeigenaar moet bij het maken van een systeemspecifieke autorisatieprocedure aangeven welke detailnormen hij wel of niet van toepassing wil laten zijn.

### Functiescheiding

- De beschikkende, bewarende en controlerende taken worden in beginsel nooit in de rol van één functionaris tezamen gebracht. Indien dit toch noodzakelijk is dan wordt door de systeemeigenaar apart toezicht georganiseerd op de betreffende functionaris om een 4-ogen principe te handhaven.

- (Technische) beheerders mogen geen toegang hebben tot de data van het informatiesysteem waar zij (technisch) beheerder van zijn. Indien dit toch noodzakelijk is dan wordt door de systeemeigenaar apart toezicht georganiseerd.

### Autorisatie en Toegang

- de uitvoeringsorganisatie autoriseert en registreert gebruikers/beheerders die toegang hebben tot informatiesystemen op basis van een formele autorisatieprocedure. waarin is opgenomen:

- Elke gebruiker/beheerder dient zich te authentiseren voordat er op een informatiesysteem activiteiten kunnen worden uitgevoerd.

- Gebruikers- en beheeraccounts worden na een vast gedefinieerd aantal, bijvoorbeeld drie, foutieve/ongeldige inlogpogingen (al dan niet tijdelijk) geblokkeerd.

- Het gebruik van groepsaccounts dient zo veel mogelijk worden beperkt. Indien deze toch gebruikt wordt dient het gebruik ervan te worden gemotiveerd en worden vastgelegd door de proceseigenaar.

- Er is een autorisatiematrix aanwezig, waarin gebruikers/beheerders, gebruik- en beheerprofielen en te beheren objecten beschreven worden en aan elkaar worden gekoppeld.

- Er is een actueel mandaatregister aanwezig waaruit blijkt welke personen bevoegdheden hebben voor het verlenen van toegangsrechten dan wel functieprofielen.

- Gebruikers- en beheeraccounts zijn niet voorzien van meer rechten dan strikt noodzakelijk is voor het uitvoeren van de noodzakelijke taken.

- Identificatie, authenticatie en autorisatie vinden plaats met behulp van een toegangbeveiligingstool. Bijvoorbeeld Identity & Access Management (I&AM).

- Ongeautoriseerde toegangspogingen en essentiële activiteiten worden gedetecteerd, geanalyseerd en tegen inbreuken wordt actie ondernomen.

- Bij functiewijzingen van personeel en uitdiensttreding worden autorisaties zo spoedig mogelijk volgens bestaande procedures aangepast.

- Controle op verleende toegangsrechten en gebruik van informatiesystemen en gegevens vindt meerdere keren per jaar plaats, in opdracht van de CISO of de systeem-, gegevens-, of proceseigenaren.

- De toegang tot programmabroncode is beperkt. Alleen gebruikers met speciale toegangsrechten dienen de broncode te kunnen inzien.

- Het toepassen van schermbeveiligingsprogrammatuur (een screensaver) maakt na een periode van inactiviteit van maximaal 15 minuten alle informatie op het beeldscherm onleesbaar en ontoegankelijk. Ook een remote desktop sessie dient na 15 minuten inactiviteit te worden vergrendeld.

- Systemen die een chipcardtoken gebruiken worden bij het verwijderen van de chipcardtoken automatisch vergrendeld.

- Een onbeheerde werkplek is in een ongecontroleerde omgeving altijd vergrendeld.

- Het gebruik van wachtwoorden is gebaseerd op het wachtwoordbeleid van de gemeente. Het binnen de gemeente geldende wachtwoordbeleid wordt, waar mogelijk, technisch afgedwongen.

- Er is voor de medewerkers een wachtwoordkluis (password manager) beschikbaar ter ondersteuning van het beheren van hun wachtwoorden.

- Nadat een vooraf vastgestelde periode van inactiviteit is overschreden wordt de sessie automatisch afgesloten.

- Beheersessies worden versleuteld.

- Beheerdiensten zijn netwerktechnisch enkel toegankelijk voor geautoriseerde beheerders.

- Voordat er succesvol is ingelogd op een informatiesysteem, wordt een inlogbericht getoond, waarin wordt gewezen op het feit dat alle activiteiten op het informatiesysteem worden vastgelegd en waar nodig voor onderzoek en bewijsvoering kunnen worden overgedragen aan geselecteerde instanties.

### Inhuur externen

- Inhuurpersoneel valt onverkort onder het beleid logische toegangsbeveiliging en dient conform deze regels te handelen.

- Aan de hand van hun taken/functie zal hun toegang verleend worden tot de gegevens en informatiesystemen.

### Uitbesteding aan een ICT-dienstverlener

- De ICT-dienstverlener heeft een beveiligingsbeleid en geëffectueerde maatregelen, die zij aan de uitvoeringsorganisatie inzichtelijk maakt die in lijn zijn met dit logisch toegangsbeveiligingbeleid.

- De ICT-dienstverlener is verantwoordelijk voor een correcte inrichting van het beleid en naleving hiervan binnen de eigen organisatie. De ICT-dienstverlener voldoet aan de normen en eisen die gesteld zijn in het informatiebeveiligingsbeleid casu quo beleid logische toegangsbeveiliging en de van toepassing zijnde wet- en regelgeving.

- Binnen de ICT-dienstverlener is een Securitymanager aanwezig die verantwoordelijk is voor het informatiebeveiligingsbeleid van de ICT-dienstverlener en die contactpersoon is voor de ISO’s en CISO van de organisatie.

- De normen en eisen aangaande de beveiliging maken onderdeel uit van het servicecontract (mantelovereenkomst, nadere overeenkomsten en diensten niveau overeenkomsten), dat de uitvoeringsorganisatie en de ICT-dienstverlener afgesproken is.

- De ICT-dienstverlener stelt uitsluitend in opdracht van de uitvoeringsorganisatie gegevens en systemen beschikbaar aan medewerkers uit de gemeente, de ICT-dienstverlener en aan derde partijen.

- De ICT-dienstverlener stelt capaciteit en informatie beschikbaar aan audits op gebied van autorisaties, die in opdracht van de uitvoeringsorganisatie en de gemeenten uitgevoerd worden.

- Voor de dagelijkse operatie is er bij de ICT-dienstverlener een autorisatiebeheerder aanwezig die verantwoordelijk is voor een correcte inrichting van de autorisaties en die aanspreekpunt is voor de CISO. De autorisatiebeheerder ressorteert onder de Securitymanager.

- De operationele afspraken en geldende procedures tussen opdrachtgever en ICT-dienstverlener worden vastgelegd in een dossier afspraken en procedures (DAP).

### Beoordeling van de uitvoering van het beleid

- De systeemeigenaar dient het toezicht op de uitvoering van de autorisatieprocedure goed te regelen en te documenteren. Hij neemt interne beheersmaatregelen die in overeenstemming zijn met de eisen die uit de baselinetoets BIO of risicoanalyse voortvloeien.

- De uitvoering van het beleid logische toegangsbeveiliging wordt periodiek beoordeeld door de (interne) accountantsdienst. Het initiatief voor de uitvoering van de controles ligt bij de CISO of de systeem-, gegevens-, of proceseigenaren.

- Tussentijdse controles kunnen plaatsvinden door de interne accountantsdienst van de uitvoeringsorganisatie. De bevindingen en verbeteringen zijn onderdeel van de jaarlijkse controle door de onafhankelijke partij.

- Beoordeling vindt plaats op de volgende punten/onderdelen:

- Of het beleid logische toegangsbeveiliging in overeenstemming is met de wet- en regelgeving en ander beleidsstukken.

- Of de maatregelen passend zijn voor het beleid logische toegangsbeveiliging.

- Of de organisatie in voldoende mate het beleid naleeft.

## BIJLAGEN

### 3.1 Voorbeeld autorisatieprocedure tot [informatiesysteem]

Inleiding

De inhoud van deze autorisatieprocedure moet bekend zijn bij alle medewerkers die bij deze procedure betrokken zijn.

Doel

Deze autorisatieprocedure voorziet in het vastleggen van de verschillende stappen die noodzakelijk zijn voor het autoriseren van personen voor [informatiesysteem]. Hiermee wordt de logische toegangsbeveiliging geregeld voor de gegevens van [informatiesysteem] en de vertrouwelijkheid hiervan gewaarborgd.

Definitie

Met een autorisatie wordt een ‘door het bevoegd gezag gelegitimeerde toegang’ tot één of meerdere informatiesystemen van de gemeente bedoeld. De procedure bestaat uit drie afzonderlijke deelprocedures die gescheiden kunnen worden uitgevoerd:

- Autorisatie tot het netwerk

- Autorisatie tot [informatiesysteem]

- Periodieke controle autorisaties en rapportage

Verantwoordelijkheid

Voor elk bedrijfsproces, informatiesysteem, gegevensverzameling en ICT-faciliteit is een verantwoordelijke lijnmanager benoemd.

Beheer

Om toegang te kunnen krijgen tot de gegevens is naast de specifieke autorisatie in het desbetreffende informatiesysteem tevens een bevoegdheid nodig op netwerk- en/of systeemniveau. Deze bevoegdheden worden beheerd door de netwerk- en/of systeembeheerder. De bevoegdheden binnen [informatiesysteem] worden beheerd door de functioneel beheerder van [informatiesysteem].

Proceseigenaar

De proceseigenaar is de manager van de afdeling [afdeling].

Verantwoordelijkheden

De verantwoordelijkheid voor deze autorisatieprocedure ligt bij het college van burgemeester en wethouders (college van B&W) en namens deze, bij de systeemeigenaar van het [informatiesysteem]. De systeemeigenaar stelt in overleg met de functioneel beheerder de autorisatiematrix op die als bijlage aan deze autorisatieprocedure wordt toegevoegd.

De verantwoordelijkheid om toegang te verlenen tot de gegevens behorend bij [informatiesysteem] berust bij de gegevenseigenaar. De uitvoering hiervan ligt bij de functioneel beheerder van [informatiesysteem].

Actualiteit

De systeemeigenaar is verantwoordelijk voor het actueel houden van deze autorisatieprocedure.

Autorisatie tot [informatiesysteem]

- De autorisatiebevoegde medewerker van [informatiesysteem] dient, met behulp van het daarvoor bestemde aanvraag- of wijzigingsformulier, schriftelijk een autorisatieverzoek in voor een nieuwe of gewijzigde autorisatie voor [informatiesysteem] bij de servicedesk.

- De servicedesk beoordeelt het autorisatieverzoek. Hierbij wordt gecontroleerd of het aanvraag- of wijzigingsformulier op de juiste manier is ingevuld en of het formulier door een autorisatiebevoegde medewerker is ingediend. Tevens wordt gecontroleerd of de aanvraag in overeenstemming is met de autorisatiematrix behorende bij [informatiesysteem].

- De functioneel beheerder [informatiesysteem] die het bericht van de servicedesk ontvangt regelt vervolgens de autorisatie in [informatiesysteem].

- De systemen zijn voor geautoriseerde gebruikers slechts toegankelijk met gebruik van persoonlijke toegangscodes (bijvoorbeeld wachtwoorden). Deze wachtwoorden dienen te voldoen aan de richtlijnen zoals vermeld in het wachtwoordbeleid van de gemeente.

- De servicedesk krijgt van de functioneel beheerder [informatiesysteem] die het autorisatieverzoek heeft verwerkt een terugmelding over het autorisatieverzoek. De servicedesk koppelt dit terug aan de gebruiker en tevens krijgt de gebruiker een korte instructie hoe deze zich aan kan melden en hoe om te gaan met [informatiesysteem].

- Bij vertrek of wijziging van de functie van een medewerker geeft de verantwoordelijk manager van de medewerker dit door aan de servicedesk, waarna de functioneel beheerder de autorisatie intrekt of wijzigt.

Periodieke controle autorisaties en rapportage

De functioneel beheerder [informatiesysteem] zorgt minmaal één keer per kwartaal voor een overzicht van de in het informatiesysteem toegekende autorisaties. Mede op basis van dit overzicht controleert het management of de systeem-, gegevens-, of proceseigenaren of de toegangsrechten van medewerkers nog juist zijn binnen de informatiesystemen waar zij verantwoordelijk voor zijn, en brengt een rapportage uit aan de CISO.

In deze rapportage wordt aangegeven:

- Of de geïmplementeerde autorisaties overeenkomen met de toegekende autorisaties.

- Of de geregistreerde gebruikers en de aan hen toegekende autorisaties correct zijn. Hierbij wordt het controleverslag vergeleken met de autorisatieformulieren en tevens vergeleken met wat is vastgelegd in de autorisatiematrix [informatiesysteem].

- Of bij tussentijdse wijzigingen in taak/functie de verantwoordelijke manager van de medewerker de servicedesk hierover informeert, en of bij ontslag of vertrek de autorisatie direct wordt geblokkeerd.

Indien de uitgevoerde controle hiertoe aanleiding geeft, geeft de CISO opdracht aan de functioneel beheerder [informatiesysteem], om de nodige correcties aan te brengen. De functioneel beheerder [informatiesysteem] past zo nodig de autorisatie(s) aan en stelt de betreffende gebruiker op de hoogte van een wijziging in zijn bevoegdheidsprofiel.

Aldus vastgesteld door [proceseigenaar] van [gemeente] op [datum],

[Naam. Functie] [Naam. Functie]

_______________ _______________

### 3.2 Voorbeeld procedure ontbreken voldoende functiescheiding

Inleiding

De inhoud van deze procedure moet bekend zijn bij alle medewerkers die bij deze procedure betrokken zijn. Deze procedure wordt alleen toegepast als niet voldaan kan worden aan de functiescheiding zoals de wet- en regelgeving dit voorschrijft.

Doel

Doel van deze procedure is om bij het niet kunnen voldoen aan de vereiste functiescheiding toch de werkzaamheden, verband houdende met de [omschrijving uit te voeren activiteiten] te kunnen uitvoeren.

Definitie

Gelet op de personele bezetting van [aantal] personen op de afdeling [afdelingsnaam] is het niet mogelijk de vereiste functiescheiding (te allen tijde) door te voeren tussen de betrokken medewerkers bij [aangeven welke activiteiten het hier betreft]. Door het toepassen van deze procedure wordt aan de (wettelijke) verantwoordingsplicht voldaan.

Proceseigenaar

De proceseigenaar is de manager van de afdeling [afdeling].

Verantwoordelijkheid

De verantwoordelijkheid voor deze autorisatieprocedure ligt bij het college van burgemeester en wethouders (college van B&W) en namens deze bij de systeemeigenaar van het [informatiesysteem].

Actualiteit

De systeemeigenaar is verantwoordelijk voor het actueel houden van deze autorisatieprocedure.

Uitvoering

Gedurende de periode, dat zich de hier bovenstaande situatie voordoet (of wanneer dit continu het geval is: minimaal eenmaal per kwartaal) wordt bijgehouden, wie de medewerkers zijn die in deze periode belast zijn met de aanvraag, de controle, het toekennen en het doorvoeren van de autorisaties. Tevens wordt schriftelijk vastgelegd wat de reden is waarom (tijdelijk) niet aan de eis van functiescheiding kan worden voldaan, en de periode waarin niet aan de eis van functiescheiding kan worden voldaan.

De betreffende aanvraagformulieren en de gegevens over de in deze periode verstrekte documenten worden afzonderlijk bewaard.

Periodieke controle autorisaties en rapportage

De functioneel beheerder [informatiesysteem] zorgt direct of zo snel mogelijk na de bewuste periode of in ieder geval minimaal één keer per kwartaal voor een overzicht van de in het informatiesysteem toegekende autorisaties. Mede op basis van dit overzicht controleert het management of de toegangsrechten van medewerkers nog juist zijn binnen de informatiesystemen waar zij verantwoordelijk voor zijn en brengt een rapportage uit aan de CISO.

De controle richt zich vooral op:

- Het ontbreken van de vereiste functiescheiding.

- Of in de betreffende periode bijgehouden is wie de medewerker(s) is/zijn die in deze periode betrokken is/zijn geweest met de aanvraag, de controle, het toekennen en het doorvoeren van de autorisaties.

- Of de schriftelijke vastlegging aanwezig is en de aanvraag, controle, toekenning en het beheer op de voorgeschreven wijze hebben plaatsgevonden.

Aldus vastgesteld door [proceseigenaar] van [gemeente] op [datum],

[Naam. Functie] [Naam. Functie]

_______________ _______________

### 3.3 Voorbeeld autorisatieoverzichten

Gemeenten dienen een actueel inzicht te hebben wie, welke autorisaties heeft binnen de informatiesystemen die bij de gemeente worden gebruikt. Als gemeenten moet je daarvoor onderstaande vragen kunnen beantwoorden:

- Welke functies binnen de gemeenten worden onderkend?

- Welke taken bij een specifieke functie horen?

- Welke taken niet gecombineerd mogen worden vanuit het oogpunt functiescheiding?

- Welke functie een medewerker bekleed?

- Welke taken een medewerker vervuld?

In figuur 3 wordt de relatie weergeven tussen de functie die een medewerker bekleedt, de taken die bij deze functie horen en de benodigde autorisaties die deze medewerker in de verschillende systemen moet hebben om deze taken te kunnen uitvoeren.

Bijvoorbeeld:

- Voor het uitvoeren van ‘taak 1’ heeft deze medewerker autorisatie A1 voor systeem A nodig.

- Voor het uitvoeren van ‘taak 2’ heeft deze medewerker autorisatie A1 voor systeem A en Autorisatie B1 voor systeem B nodig.

- Voor het uitvoeren van ‘taak 3’ heeft deze medewerker autorisatie A2 voor systeem A nodig.

- Voor het uitvoeren van ‘taak 4’ heeft deze medewerker autorisatie B1 en B2 voor systeem B nodig.

Figuur 3. Relatie Functie, taken en autorisaties

Gemeenten moeten inzicht hebben in welke taken behoren bij een specifieke functie. Hiervoor kan gebruik worden gemaakt van tabel 2. Deze verschillende taken kunnen betrekking hebben op verschillende informatiesystemen. Voorbeelden van functies zijn:

- Controller

- Junior/senior inkoper

- Medewerker salarisadministratie

- Kwaliteitsmedewerker

- Lijnmanager

- Teammanager

Voorbeelden van taken zijn:

- Aanvragen bestellingen

- Accorderen bestellingen

- Invoeren betalingen

- Accorderen betalingen

| X = Taak behorende bij functie | Taak 1 | Taak 2 | Taak 3 | Taak 4 | Taak 5 | Taak 6 | Taak 7 |
|---|---|---|---|---|---|---|---|
| Functie 1 |  | X |  |  |  |  |  |
| Functie 2 | X |  |  | X |  |  |  |
| Functie 3 |  |  |  | X | X |  |  |
| Functie 4 |  | X | X |  |  |  |  |
| Functie 5 |  |  | X |  |  |  |  |
| Functie 6 |  |  |  |  |  |  |  |
| Functie 7 |  |  |  |  |  |  |  |

Tabel 2. Overzicht welke taken behoren bij een specifieke functie

Gemeenten moeten inzicht hebben welke combinaties van taken (autorisaties binnen een informatiesysteem), wel en niet mogen worden toegekend aan één functie (medewerker). Hiervoor kan gebruik worden gemaakt van tabel 3. In dit overzicht dienen de functies voor te komen die uit het oogpunt van functiescheiding belangrijk zijn.

Autorisaties waarmee het informatiesysteem alleen geraadpleegd kan worden (rapporten afdrukken, schermen bekijken) mogen met andere autorisaties worden gecombineerd.

| X = niet toegestane combinatie van autorisaties Bijvoorbeeld: Op het snijpunt van de regel taak 1 en de kolom taak 2 staat een X. Dat betekent dat een medewerker niet mag worden geautoriseerd voor deze beide rollen tegelijk. | Taak 1 | Taak 2 | Taak 3 | Taak 4 | Taak 5 | Taak 6 | Taak 7 |
|---|---|---|---|---|---|---|---|
| Taak 1 |  | X |  |  |  |  |  |
| Taak 2 | X |  |  | X |  |  |  |
| Taak 3 |  |  |  | X | X |  |  |
| Taak 4 |  | X | X |  |  |  |  |
| Taak 5 |  |  | X |  |  |  |  |
| Taak 6 |  |  |  |  |  |  |  |
| Taak 7 |  |  |  |  |  |  |  |

Tabel 3. Overzicht van wel en niet toegestane combinaties van taken

Gemeenten moeten inzicht hebben welke functie door één medewerker wordt ingevuld. Hiervoor kan gebruik worden gemaakt van tabel 4.

| X = Functie die door de medewerker wordt ingevuld | Functie 1 | Functie 2 | Functie 3 | Functie 4 | Functie 5 | Functie 6 | Functie 7 |
|---|---|---|---|---|---|---|---|
| Medewerker 1 | X |  |  | X |  |  |  |
| Medewerker 2 |  |  | X | X |  |  |  |
| Medewerker 3 |  |  |  |  |  |  | X |
| Medewerker 4 | X |  |  |  |  | X |  |
| Medewerker 5 |  |  | X |  |  |  |  |
| Medewerker 6 |  | X |  |  | X | X |  |
| Medewerker 7 |  |  |  |  |  |  |  |

Tabel 4. Overzicht welke functies worden uitgevoerd door een medewerker (autorisatiematrix)

### 3.4 Voorbeeld autorisatie aanvraagformulier [informatiesysteem]

| Gegevens gebruiker |  |  |
|---|---|---|
| Naam en voorletters gebruiker | [Volledige naam van de te autoriseren medewerker.] |  |
| Voornaam gebruiker | [Voornaam van de te autoriseren medewerker.] |  |
| E-mailadres | [E-mailadres van de te autoriseren medewerker.] |  |
| Afdeling/Groep | [Organisatorische eenheid waarbij de te autoriseren medewerker werkzaam is.] |  |
| Functie | [De functie van de te autoriseren medewerker.] |  |
| Kamernummer | <Kamer waar de te autoriseren medewerker zijn vaste werkplek heeft. Dit veld kan leeg worden gelaten op het moment dat met flexibele werkplekken wordt gewerkt.> |  |
| Telefoonnummer | <Telefoonnummer van de te autoriseren medewerker. Bij calamiteiten moet de verwerkingsorganisatie direct contact op kunnen nemen met de gebruiker. Tevens kan de medewerker bij een spoed autorisatie direct op de hoogte worden gesteld dat de autorisatie is toegekend.> |  |
| Dienstverband (Tijdelijk/Vast) | Tijdelijk / Vast |  |
| Autorisatie | Nieuwe gebruiker | O |
|  | Wijzig huidige autorisaties | O |
|  | Opschorten gebruiker-ID | O |
|  | Intrekken gebruiker-ID | O |
| Gebruiker-ID | <Als het een bestaande gebruiker betreft dient hier het huidige gebruikers-ID ingevuld te worden, bij een nieuwe gebruiker wordt dit door de verwerkingsorganisatie later ingevuld. Nieuwe gebruikers krijgen meestal een gebruikersnaam die van hun eigen naam is afgeleid. Deze gebruikersnaam wordt in het vakjargon gebruikers-ID genoemd.> |  |
| Reden | [De reden van deze aanvraag/wijziging met betrekking tot de autorisaties van deze medewerker.] |  |
| Gewenste ingangsdatum | <De datum waarop de autorisatie ingaat kan afwijken van de aanmelddatum maar moet daarna liggen. Het is aan te raden om de autorisaties ruim van te voren aan te melden zodat de werkzaamheden die bij het autoriseren horen kunnen worden ingepland.> |  |
| Einddatum geldigheid | <In veel gevallen zal deze rubriek leeg worden gelaten omdat er een permanente autorisatie wordt toegekend. Het komt echter voor dat bepaalde werkzaamheden slechts van korte duur zijn, medewerkers op contract worden aangenomen of vakantiewerk komen verrichten. In die gevallen wordt de ‘Einddatum geldigheid’ toegepast.> |  |

| Autorisaties [informatiesysteem] |  |  |  |
|---|---|---|---|
| Vul de huidige, de gewenste en de te verwijderen autorisatierollen in | Huidige | Verwijderen | Nieuwe rol / Toevoegen |
| [Rol 1] | O | O | O |
| [Rol 2] | O | O | O |
| [Rol 3] | O | O | O |
| Alle autorisaties verwijderen | O |  |  |

| Gegevens Aanvrager |  |
|---|---|
| Naam en voorletters aanvrager | [Volledige naam van de autorisatiebevoegde medewerker.] |
| Voornaam aanvrager | [Voornaam van de autorisatiebevoegde medewerker.] |
| Telefoonnummer | [Telefoonnummer van de autorisatiebevoegde medewerker.] |
| E-mailadres | [E-mailadres van de autorisatiebevoegde medewerker.] |
| Functie | <De functie van de autorisatiebevoegde medewerker dient tevens ter verificatie te worden vermeld zodat wordt voorkomen dat de aanvrager autorisaties uitgeeft van informatiesystemen waarvoor hij niet geautoriseerd is.> |
| Aanmelddatum | <Datum waarop de autorisatie is aangevraagd. Aan de hand van deze datum kan achteraf worden vastgesteld hoe lang het heeft geduurd voordat de autorisatie werd ingevoerd.> |
| Handtekening | <Handtekening van de autorisatiebevoegde medewerker. Deze handtekening dient op juistheid te worden gecontroleerd aan de hand van de parafen lijst.> |
