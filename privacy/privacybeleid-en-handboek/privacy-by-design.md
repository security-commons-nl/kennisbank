# Beleid privacy by design

### Afkortingen

| AVG | Algemene Verordening Gegevensbescherming |
|---|---|
| PbD | Privacy by Design |

### Definities

| Anonimiseren | Het verwijderen van alle (combinaties van) attributen uit de gegevensset die het mogelijk maken om de gegevens te herleiden tot een individu. Herleidbaarheid moet blijvend onmogelijk gemaakt zijn. |
|---|---|
| Betrokkene | Degene wiens persoonsgegevens worden verwerkt. |
| Persoonsgegevens | Alle informatie over een geïdentificeerde of identificeerbare natuurlijke persoon (‘’de betrokkene”); als identificeerbaar wordt beschouwd een natuurlijke persoon die direct of indirect kan worden geïdentificeerd, met name aan de hand van een identificator zoals een naam, een identificatienummer, locatiegegevens, een online identificator of van een of meer elementen die kenmerkend zijn voor de fysieke, fysiologische, genetische, psychische, economische, culturele of sociale identiteit van die natuurlijke persoon. |
| Pseudonimiseren | Het verwerken van persoonsgegevens op zodanige wijze dat deze niet meer aan een specifieke betrokkene kunnen worden gekoppeld zonder dat er aanvullende gegevens worden gebruikt, mits deze aanvullende gegevens apart worden bewaard en maatregelen worden genomen om eerdergenoemde koppeling te voorkomen. |
| Verwerkings-verantwoordelijke | Een natuurlijke persoon of rechtspersoon, een overheidsinstantie, een dienst of een ander orgaan die/dat, alleen of samen met anderen, het doel van en de middelen voor de verwerking van persoonsgegevens vaststelt; wanneer de doelstellingen van en de middelen voor deze verwerking in het Unierecht of het lidstatelijke recht worden vastgesteld, kan daarin worden bepaald wie de verwerkingsverantwoordelijke is of volgens welke criteria deze wordt aangewezen. |
| Verwerking/ verwerken (van persoonsgegevens) | Een bewerking of een geheel van bewerkingen met betrekking tot persoonsgegevens of een geheel van persoonsgegevens, al dan niet uitgevoerd via geautomatiseerde procedés, zoals het verzamelen, vastleggen, ordenen, structureren, opslaan, bijwerken of wijzigen, opvragen, raadplegen, gebruiken, verstrekken door middel van doorzending, verspreiden of op andere wijze ter beschikking stellen, aligneren of combineren, afschermen, wissen of vernietigen van gegevens. |

## 1. Inleiding

De Algemene Verordening Gegevensbescherming (AVG) verplicht expliciet tot toepassen van het beginsel van ‘gegevensbescherming door ontwerp’ in het algemeen spraakgebruik vaak aangeduid als ‘Privacy by Design’ (PbD), de term die in dit document ook gebruikt zal worden.

Dit document is bedoeld om een meer concrete invulling te geven aan deze verplichting. De AVG verwoordt de verplichting tot toepassen van PbD als volgt:

| Rekening houdend met de stand van de techniek, de uitvoeringskosten, en de aard, de omvang, de context en het doel van de verwerking alsook met de qua waarschijnlijkheid en ernst uiteenlopende risico's voor de rechten en vrijheden van natuurlijke personen welke aan de verwerking zijn verbonden, treft de verwerkingsverantwoordelijke, zowel bij de bepaling van de verwerkingsmiddelen als bij de verwerking zelf, passende technische en organisatorische maatregelen, zoals pseudonimisering, die zijn opgesteld met als doel de gegevensbeschermingsbeginselen, zoals minimale gegevensverwerking, op een doeltreffende manier uit te voeren en de nodige waarborgen in de verwerking in te bouwen ter naleving van de voorschriften van deze verordening en ter bescherming van de rechten van de betrokkenen. |
|---|

Kort gezegd komt het neer op het volgende: aan de bescherming van persoonsgegevens moet bij de (door)ontwikkeling van (nieuwe) producten, diensten, procedures etc. zo vroeg mogelijk – liefst reeds in de ontwerpfase – aandacht geschonken worden. Daarbij moeten maatregelen worden genomen om de bescherming van persoonsgegevens zo optimaal mogelijk in te richten.

Maar welke maatregelen komen daarvoor in aanmerking?

Dit document biedt een achttal maatregelen (gebaseerd op een Privacy-by-design-framework, opgenomen in Bijlage 2) die, wanneer ze zo veel als mogelijk toegepast worden, voldoende invulling geven aan de verplichting tot het toepassen van het principe van PbD. Niet alle acht maatregelen zullen in alle gevallen kunnen worden toegepast. Zo zal het doel van een verwerking vaak niet langer bereikt kunnen worden als de gegevens geanonimiseerd zijn. Deze maatregel kan in dat geval redelijkerwijs niet toegepast worden. Indien wordt beargumenteerd waarom dit het geval is, wordt toch aangetoond dat de mogelijkheid in overweging genomen is, waarmee (ten minste deels) aan het principe van PbD wordt voldaan. Om dergelijke overwegingen te documenteren is in Bijlage 1 een (voorstel tot een) formulier opgenomen.

Voor concrete toepassing kan je doorbladeren naar hoofdstuk 2.

### De acht maatregelen van het PbD-framework

De acht maatregelen uit het framework (zie bijlage 2) worden hieronder kort toegelicht.

❶ Anonimiseren Het verwijderen van alle attributen/velden uit de gegevensset die het mogelijk maken om de gegevens te herleiden tot een persoon. Herleidbaarheid moet blijvend onmogelijk gemaakt zijn (hier onderscheidt anonimiseren zich van pseudonimiseren). Let op dat wanneer alle direct-identificerende gegevens zijn verwijderd, dit niet meteen leidt tot het blijvend onmogelijk zijn van herleiden. Ook de combinatie van (bijvoorbeeld) geboortedata en postcodes kan de groep mogelijke betrokkenen zodanig beperken dat herleidbaarheid aangenomen moet worden.

❷ Dataminimalisatie Alleen die persoonsgegevens die strikt noodzakelijk zijn om het doel van de verwerking te verwezenlijken, mogen worden (verzameld en) verwerkt. Bijvoorbeeld: om een burger van een paspoort te voorzien is diens lichaamsgewicht geen noodzakelijk gegeven. Dit gegeven mag in dat kader dan ook niet (verzameld en) verwerkt worden.

❸ Pseudonimiseren Bij pseudonimiseren worden datasets ontdaan van alle direct identificerende gegevens (denk aan namen, postcode-huisnummercombinaties, BSN). Het doel is om de gegevensset (of record) pas weer herleidbaar te maken, op het moment dat je daadwerkelijk iemands identiteit nodig hebt. Om dat te realiseren wordt per record een sleutelveld toegevoegd. Daarmee kan men de gegevens via een andere database, correspondentietabel of gegevensset weer kan koppelen aan iemands identiteit. Het grote verschil met anonimiseren is dat herleidbaarheid dus niet blijvend onmogelijk gemaakt is.

❹ Encryptie Door gegevens te versleutelen, kunnen onbevoegden er geen kennis van nemen. Mits de sleutel natuurlijk niet is gecompromitteerd. Het versleutelen van gegevens gaat in veel gevallen ten koste van de performance (de prestatie van een IT-systeem). In sommige gevallen is dat onacceptabel, in andere niet. Bij verwerkingen als archivering speelt performance een minder grote rol.

❺ Access control (toegangsbeperking) Niet iedereen mag toegang hebben tot alle gegevens. Zo mag niet iedereen inzage hebben in personeelsdossiers. De toegang tot personeelsdossiers is daarom beperkt tot die medewerkers die daar uit hoofde van hun functie toegang toe moeten hebben. Dit principe moet bij alle verwerkingen van persoonsgegevens worden toegepast. Toegangsbeperkingen variëren van een slot op de deur en toegangspasjes (fysieke toegangsbeperking) tot authenticatie en autorisatie (technische toegangsbeperking).

❻ Privacy by default Privacy by default houdt in dat de standaardinstellingen voor de betrokkenen zo privacy-vriendelijk mogelijk moeten zijn. Met andere woorden: standaardinstellingen van de verwerking bieden een zo hoog mogelijk niveau van gegevensbescherming voor de betrokkene. Een voorbeeld – dat weliswaar weinig raakvlakken heeft met de gemeentelijke praktijk maar wel een goede illustratie is van het principe van privacy by default – is dat van Facebook. Bij nieuwe gebruikers van Facebook zou de standaardinstelling moeten zijn dat berichten slechts met vrienden worden gedeeld (en dus niet met vrienden-van-vrienden of met iedereen). Indien bij de gebruiker een behoefte bestaat om berichten breder te delen, kan hij of zij dat zelf instellen.

Onderdeel van privacy by default is ook dat je betrokkene goede mogelijkheden biedt om zijn privacy-instellingen aan te passen. Dit kan bijvoorbeeld door een transparante user interface te hanteren en de privacy-instellingen niet moeilijk vindbaar te maken door ze diep in een instellingenmenu te verstoppen.

❼ Verwijderen/ bewaartermijnen Persoonsgegevens mogen slechts bewaard worden (in een vorm die het mogelijk maakt de betrokkenen te identificeren) zo lang dat noodzakelijk is voor de doeleinden waarvoor de gegevens verwerkt worden. Met andere woorden: zodra het verwerkingsdoel bereikt is – en er geen verplichtingen of andere zwaarwegende redenen zijn om de gegevens te bewaren – moeten de gegevens gewist of geanonimiseerd worden.

❽ Faciliteren rechten van betrokkenen Betrokkenen moeten zoveel mogelijk in staat gesteld worden om hun rechten uit hoofde van de AVG uit te oefenen. Dit kan proactief gefaciliteerd worden door bijvoorbeeld een dashboard aan te bieden waar een betrokkene inzage kan verkrijgen in zijn persoonsgegevens, zijn persoonsgegevens kan wijzigen, downloaden of verwijderen en waar hij zijn privacy-instellingen kan wijzigen.

Hoe deze maatregelen kunnen worden toegepast van de organisatie, wordt in het volgende hoofdstuk besproken.

## 2. Privacy by Design bij de organisatie

### Privacy by Design

Het principe van Privacy by Design (PbD) komt erop neer dat je, vooraan in het (ontwerp)proces, al nagedacht moet hebben over de consequenties die bepaalde (ontwerp)keuzes hebben voor de bescherming van persoonsgegevens. Vervolgens moet het uiteindelijke ontwerp zo min mogelijk inbreuk maken op de bescherming van persoonsgegevens; het ontwerp moet zo ‘privacy-vriendelijk’ mogelijk worden. Dit heeft voordelen: hoe eerder privacy-risico’s worden onderkend en maatregelen worden genomen, hoe minder ‘pleisters’ achteraf hoeven te worden geplakt ter beperking van eventuele privacy-risico’s. Hierdoor worden uiteindelijk tijd en kosten bespaard.

### Uitleg framework

De acht maatregelen die in het framework (zie bijlage 2) zijn voorgeschreven, moeten in de ontwerpfase in overweging worden genomen en zoveel mogelijk toegepast zodat een zo privacy-vriendelijk mogelijk(e) dienst/product/proces ontstaat. Hierbij kan een vooraf vastgesteld formulier worden gebruikt om in dit stadium vast te leggen welke maatregelen (al dan niet) op welke wijze zijn toegepast en welke overwegingen ten grondslag liggen aan de gemaakte ontwerpkeuzes (zie Bijlage 2).

Samengevat werkt het framework als volgt. Indien je anonimiseren kan toepassen en dit ook daadwerkelijk doet, is je oplossing optimaal privacy by design: de gegevens zijn niet langer als persoonsgegevens aan te merken en de AVG is niet van toepassing op de verwerking. De maatregelen ❷ t/m ❽ kan je in dat geval overslaan.

Anonimiseren zal echter niet in alle gevallen mogelijk zijn. Kan het doel van de verwerking niet worden bereikt wanneer de gegevens geanonimiseerd worden en kan het dus niet toegepast worden? Dan moet je onderzoeken in hoeverre je de maatregelen ❷ t/m ❽ kan toepassen. Het is de bedoeling dat je de bij de stappen horende maatregelen steeds zo vergaand als mogelijk toepast. Als ervoor wordt gekozen een maatregel niet of deels toe te passen, dan moet steeds beargumenteerd worden waarom dat het geval is. Deze overwegingen moeten gedocumenteerd worden.

### Toepassing framework

Zoals hiervoor reeds aangehaald: doorloop de stappen ❶ t/m ❽. Hierbij dien je de genoemde maatregelen steeds zo vergaand mogelijk toe te passen op je ontwerp, of te beargumenteren waarom toepassen ervan niet mogelijk is. Let op: aan de stappen ❷, ❺ & ❼ valt niet te ontkomen – deze moeten hoe dan ook worden toegepast omdat de AVG dit vereist.

Omdat je als verwerkingsverantwoordelijke aan moet kunnen tonen dat je de AVG naleeft, zal dossieropbouw moeten plaatsvinden. Per maatregel staat achter ‘þ Noteer’ wat je moet documenteren. Hiervoor kan je het formulier uit Bijlage 1 gebruiken.

Omschrijf het doel van de voorgenomen verwerking zo volledig mogelijk. Dit is het toetsingskader waarbinnen de toepassing van PbD (binnen het project) beoordeeld zal worden.

### ❶ Anonimiseren

Wanneer de voorgenomen verwerking geen doel dient waarvoor identificatie van de betrokkene noodzakelijk is, dan kan de gegevensset worden geanonimiseerd. Als voorbeeld van een verwerking die kan plaatsvinden op basis van een geanonimiseerde gegevensset kan gedacht worden aan het genereren van statistiek. Hiervoor is het vaak niet nodig om gegevens te verwerken die tot individuen te herleiden zijn. Wanneer het anonimiseren goed wordt toegepast, is de AVG niet langer van toepassing.

Anonimiseren is de meest vergaande privacymaatregel die genomen kan worden. Bij het op juiste wijze toepassen van anonimiseren, is het volgende niet meer mogelijk:

- Singling out het o.b.v. gegevens kunnen onderscheiden van een persoon van andere personen;

- Linkability het leggen van relaties tussen records met persoonsgegevens in dezelfde dan wel verschillende databases; en

- Inference het deduceren met een grote mate van zekerheid van de waarde van een attribuut op basis van de waarde van de andere attributen.

Nb. Wanneer het anonimiseren kan worden toegepast, hoeft de rest van het schema niet te worden toegepast. Als anonimiseren niet mogelijk is, dienen alle andere stappen wél doorlopen te worden.

þ Noteer: Noteer de wijze waarop je anonimiseren gaat toepassen (welke velden worden er uit de dataset verwijderd en waarom is herleidbaarheid daarmee onmogelijk gemaakt) of waarom anonimiseren geen mogelijkheid is.

### ❷ Dataminimalisatie (verplicht)

Er is geen ontkomen aan het toepassen van het beginsel van dataminimalisatie. Het is een wettelijk vereiste waarvan niet afgeweken kan worden: men mag slechts die persoonsgegevens verzamelen en gebruiken die noodzakelijk zijn om het doel van de verwerking te bereiken. þ Noteer: beargumenteer welke overwegingen er ten grondslag liggen aan de gekozen gegevensset: waarom zijn de gekozen gegevens (of attributen) noodzakelijk om het doel v/d verwerking te bereiken?

### ❸ Pseudonimiseren

Voor sommige verwerkingen is het niet nodig dat gegevens direct aan een identificerend of identificeerbaar gegeven worden gekoppeld. Indien en zodra dat het geval is, kan de gegevensset worden gepseudonimiseerd.

þ Noteer: Omschrijf op welke wijze wordt gepseudonimiseerd, of, wanneer pseudonimiseren niet mogelijk is: beargumenteer waarom pseudonimiseren niet mogelijk is.

### ❹ Encryptie

Door persoonsgegevens te versleutelen (te encrypten), kan bijvoorbeeld de schade als gevolg van het uitlekken van persoonsgegevens worden beperkt. Encryptie is de conversie van een leesbaar formaat van gegevens naar een gecodeerd formaat, dat alleen na decryptie weer gelezen of verwerkt kan worden.

þ Noteer: Omschrijf de wijze van encryptie, of, wanneer encrypten niet mogelijk is: beargumenteer waarom encryptie niet mogelijk is.

### ❺ Access control (verplicht)

Persoonsgegevens mogen alleen toegankelijk zijn voor personen die deze gegevens ook daadwerkelijk nodig hebben gelet op het doel van de verwerking. Dit kan bereikt worden door onder meer authenticatie, autorisatie en logging van de toegang.

Zie ook het Beleid logische toegangsbeveiliging v1.0 (pdf) bij de beleidsstukken Informatiebeveiliging op het intranet.

þ Noteer: Wie (personen of categorieën van personen) toegang hebben tot de persoonsgegevens en op welke wijze anderen de toegang tot de gegevens wordt bemoeilijkt of onmogelijk gemaakt.

### ❻ Privacy by default

Standaardinstellingen moeten zo ‘privacy-vriendelijk’ mogelijk zijn en deze instellingen moeten door de betrokkene eenvoudig te wijzigen zijn.

þ Noteer: De wijze waarop de gekozen standaardinstellingen blijk geven dat er rekening is gehouden met het beginsel van privacy by default. Indien dit niet mogelijk of niet aan de orde is: beargumenteer waarom niet.

### ❼ Bewaartermijnen (verplicht)

Persoonsgegevens mogen slechts voor een beperkte periode worden bewaard. Hoe lang dit is, is afhankelijk van het doel van de verwerking. De keuze voor een bewaartermijn moet kunnen worden onderbouwd. Men moet zich ook aan de gekozen bewaartermijn houden. Kies een methode om de gegevens na de bewaartermijn ook daadwerkelijk te wissen (bijv. automatisch vernietigen, flaggen na verstrijken bewaartermijn, sticky policies, data fading etc.).

Zie ook het Selectielijst gemeenten en intergemeentelijke organen van de Vereniging van Nederlandse Gemeenten (VNG).

þ Noteer: De van toepassing zijnde bewaartermijnen, waar deze op zijn gebaseerd en de wijze waarop gewaarborgd wordt dat de gegevens niet langer worden bewaard dan de voorgeschreven bewaartermijn.

### ❽ Faciliteren van rechten van betrokkenen

Faciliteer betrokkenen zoveel mogelijk in het uitoefenen van hun rechten uit hoofde van de AVG. Dat betekent in eerste instantie dat het mogelijk moet zijn om een overzicht van de van een betrokkene verwerkte persoonsgegevens te genereren (t.b.v. recht op inzage) maar ook dat de gegevens desgewenst handmatig gewist kunnen worden (t.b.v. recht op gegevenswissing). In voorkomende gevallen kan betrokkenen een dashboard aangeboden worden waarbinnen zij zelf inzage kunnen krijgen in hun persoonsgegevens en deze persoonsgegevens kunnen wijzigen en (verzoeken om te) wissen

þ Noteer: De wijze waarop gekozen is de rechten van betrokkenen te faciliteren.

## Bijlage 1: Voorgesteld formulier Privacy by design (PbD)

Gebruik onderstaand formulier om de wijze waarop je PbD hebt toegepast te documenteren.

Geef per maatregel (❶ t/m ❽) aan:

- of toepassen ervan mogelijk is (A); indien dat het geval is:

- hoe je het concreet toegepast is (B); en, indien toepassing ervan niet mogelijk is:

- waarom dit het geval is (C).

| Naam project | Datum |
|---|---|
| Invuldatum |  |
| Naam invuller |  |
| Doel van de verwerking |  |

|  | A | B | C |
|---|---|---|---|
|  | Mogelijk? | Uitleg toepassing | Uitleg onmogelijkheid/ n.v.t. |
| ❶ |  |  |  |
| ❷ | JA |  | Verplicht onderdeel |
| ❸ |  |  |  |
| ❹ |  |  |  |
| ❺ | JA |  | verplicht onderdeel |
| ❻ |  |  |  |
| ❼ | JA |  | verplicht onderdeel |
| ❽ |  |  |  |

| Maatreg.à ↓ Invulling | ❶ | ❷ | ❸ | ❹ | ❺ | ❻ | ❼ | ❽ |
|---|---|---|---|---|---|---|---|---|
|  | Anonimiseren | Data-minimalisatie | Pseudo-nimiseren | Encryptie | Access control | privacy by default | bewaar-termijnen | Faciliteren rechten |
| Techniek | Anonimiseren en aggregeren (bijv. differential privacy) | Alleen strikt noodzakelijke gegevens verwerken (verzamelen) of overbodig direct verwijderen, (web) invulformulieren aanpassen | Ontdoen van direct identificerende kenmerken, hashing, polymorfe pseudo-ID | Versleutelen, bijvoorbeeld public-key-encryptie, diskencryptie | Beperken van toegang bijv. d.m.v. Digitale gegevenskluis, fysieke & logische toegangscontrole, authenticatie en autorisatie | Privacy-vriendelijke standaard-instellingen, transparante user interface, permission-management | Automatisch vernietigen, ‘flaggen’ data na verstrijken bewaartermijn, sticky policies, data fading | Privacydashboard, communicatie / support (art. 5 lid 1 sub a) |
| documentatie | Geen extra maatregelen nodig, want geen persoons gegevens. | Doelomschrijving met opsomming noodzakelijke gegevens. Eventuele argumentatie per gegevenstype. | Beleid voor gescheiden houden van identificerende gegevens en overige gegevens, contracten | Informatie-beveiligings-standaarden | Bijhouden autorisatiematrix en logging, op basis van least privileged, need to know en need to access | Registraties opt-in en opt-out en van permissies | Beleid en overzicht bewaartermijnen, omgang met e- waste (oude documenten en devices) | Privacy statement, beleid bij verzoeken tot inzage/correctie/ verwijderen gegevens |
| Alternatief | Welke van de stappen 2 t/m 8 kan je doorvoeren? | Waar mogelijk deel gegevensset anonimiseren/ aggregeren, data fading | Andere beveiligings-maatregelen | Andere beveiligings-maatregelen (bijv. stand-alone server) | Access logs met controle achteraf | Geen alternatief, is verplicht | Anonimiseren en aggregeren, (archiveren indien wettelijk toegestaan) | Geen alternatief, wettelijke plicht |

## Bijlage 2: het Privacy-by-design-framework bron: Privacy Company
