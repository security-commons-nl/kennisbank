# Beleid logische toegangsbeveiliging

| | |
|---|---|
| Documenttype | Beleid informatiebeveiliging onder het strategisch informatiebeveiligingsbeleid; BIO 2.0-domein *Logische toegangsbeveiliging* |
| Status | Concept, vast te stellen door de organisatie |
| Eigenaar | **[eigenaar van dit beleid]** |
| Vaststeller | **[vaststeller]** |
| Evaluatie | Jaarlijks, in de plan-do-check-act-cyclus van het managementsysteem voor informatiebeveiliging |

Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor de toegang tot informatiesystemen,
netwerken en gegevens. Het legt vast hoe accounts ontstaan en vervallen, hoe gebruikers zich aanmelden, wie
welke rechten krijgt en hoe de organisatie dat controleert. Het gaat over de ISO-beheersmaatregelen 5.15
tot en met 5.18, 6.7, 8.2 tot en met 8.5 en 8.18.

**Voor wie.** Het beleid is primair bedoeld voor de afdeling die de identiteitsvoorziening beheert, voor
systeemeigenaren en voor leidinggevenden die rechten aanvragen. De gedragsregels gelden voor iedereen met
een account: medewerkers, inhuur, stagiairs, vrijwilligers en leveranciers.

**Waarop.** Alle accounts op systemen waarvan de organisatie eigenaar is, ook als een leverancier ze beheert
of host: persoonlijke, gedeelde, technische en beheeraccounts, noodaccounts en accounts van leveranciers. Is
het beheer van de identiteitsvoorziening of van een systeem uitbesteed, dan gelden de eisen uit dit beleid als minimumeis voor die partij. De organisatie legt
dat vast in het contract en toetst de naleving met een onafhankelijke verklaring, zoals een ISO
27001-certificaat of een ISAE 3402- of ISAE 3000-rapport; het vastleggen loopt via het beleid
informatiebeveiliging bij inkoop, het toetsen via het beleid contractbeheer.

Buiten dit beleid vallen de netwerkscheiding en de beheerinterfaces (beleid netwerkbeveiliging), de
logging zelf (beleid logging en monitoring) en de vergrendeling van werkplekken (beleid IT-compliance).

> **Alleen als: Wie beheert je IT? «Regie: eigen organisatie stuurt, beheer is uitbesteed» of «Volledig uitbesteed»**
>
> De organisatie beheert haar IT niet zelf. Waar dit beleid een eis stelt aan beheerders of aan het
> beheerproces, geldt die eis voor de beheerpartij via het contract. De toekenning van rechten aan eigen
> medewerkers blijft een besluit van de organisatie zelf.

## 2. Uitgangspunten

1. Elke handeling op een systeem is herleidbaar tot één natuurlijke persoon. Accounts zijn persoonsgebonden;
   gedeelde accounts zijn een gemotiveerde uitzondering.
2. Iemand krijgt alleen de rechten die nodig zijn voor de eigen taak, en niet langer dan nodig (need-to-know
   en least privilege).
3. Rechten volgen een rol uit een autorisatiematrix. Losse rechten buiten een rol zijn een uitzondering met
   een einddatum.
4. Beschikken, uitvoeren en controleren liggen niet bij dezelfde persoon. Beheerders hebben geen toegang tot
   de inhoud van de gegevens die ze beheren, tenzij de systeemeigenaar dat vastlegt en erop toeziet.
5. Hoe zwaarder de rechten of hoe hoger het vertrouwelijkheidslabel van de informatie, hoe sterker de
   authenticatie en hoe vaker de controle.
6. Termijnen en frequenties in dit beleid die niet uit een wet of uit de BIO 2.0 komen, zijn standaardwaarden.
   De organisatie past ze aan op haar eigen risicoafweging en legt de keuze vast bij de vaststelling van dit beleid.

## 3. Beleidsregels

### 3.1 Identiteiten en accounts

1. **[lijneigenaar logische toegang]**
   richt één accountproces in, gekoppeld aan de personeelsadministratie en de registratie van inhuur:
   indiensttreding of start van een opdracht levert een account op, een functiewijziging past de rechten aan
   en vertrek blokkeert het account uiterlijk op de laatste werkdag. Elke stap staat in het ticketsysteem.
   [5.16.01]
2. Een geblokkeerd account wordt na **[termijn verwijderen accounts]**
   verwijderd. Accounts van inhuur en stagiairs hebben een einddatum gelijk aan het einde van de opdracht.
   [5.16.01]
3. De identiteitsvoorziening blokkeert automatisch elk account dat
   **[termijn inactiviteit]** niet is gebruikt. [5.16.01]
4. De systeemeigenaar stelt per systeem een autorisatieprocedure en een autorisatiematrix op met de
   proceseigenaren en beoordeelt die jaarlijks. De CISO toetst de procedure voor vaststelling. Een
   mandaatregister legt vast wie rechten mag aanvragen en goedkeuren. [5.16.01]
5. De proceseigenaar gebruikt een gedeeld account alleen als een persoonlijk account aantoonbaar niet kan.
   Hij motiveert dat schriftelijk, stemt het af met de CISO en wijst een leidinggevende aan die
   verantwoordelijk is voor gebruik en tijdig opzeggen. [5.16.02]
6. Een gedeeld account krijgt een herkenbare naam, geen toegang van buiten en geen beheerrechten.
   **[lijneigenaar logische toegang]** loopt het register van gedeelde accounts jaarlijks door. [5.16.02]
7. Een functionele postbus (op naam van een team, project of product) heeft een eigenaar en wordt geopend
   met persoonlijke accounts die rechten op de postbus krijgen. Niemand meldt zich met een gedeeld wachtwoord
   op de postbus zelf aan. [5.16.02]
8. De beheerder schakelt standaardaccounts uit of hernoemt ze en geeft ze een nieuw wachtwoord voor
   ingebruikname. Een technisch account heeft een eigenaar, kan niet interactief aanmelden en staat in het
   register van accounts met bijzondere rechten. [5.16.02, 5.18.01]

### 3.2 Authenticatie en MFA

1. MFA is verplicht bij het aanmelden op de digitale werkomgeving, bij elk account op een voorziening die via
   internet bereikbaar is en bij elk account met beheerrechten. Waar de risicoanalyse van een systeem dat
   vraagt, geldt MFA ook voor andere accounts. [5.17.01]
2. De voorkeur gaat naar wachtwoordloze authenticatie met een persoonsgebonden sleutel, zoals een passkey of
   een hardwaretoken met pincode; anders een wachtwoord met een tweede factor. Een sms-code is alleen
   toegestaan als er geen andere tweede factor beschikbaar is. [5.17.01]
3. Waar het kan, loopt aanmelden via de centrale identiteitsvoorziening met SSO. Beheerders bereiken
   beheeromgevingen via een beveiligde tussenstap (jumpserver) waarop ook MFA geldt. [5.17.01]
4. Kan een systeem geen MFA, dan stelt de systeemeigenaar met de CISO aanvullende maatregelen op, zoals
   toegang alleen vanaf beheerde apparaten. De proceseigenaar keurt ze goed; het systeem staat ermee in het
   risicoregister. [5.17.01]
5. De servicedesk reikt inloggegevens, tokens en resets pas uit nadat de identiteit van de ontvanger is
   vastgesteld, en legt dat vast in het ticket. [5.17.01]
6. De identiteitsvoorziening meldt ten minste: aanmelden vanaf een ongebruikelijke locatie of een
   onmogelijke reisafstand, en een piek in mislukte aanmeldingen.
   **[bewaking aanmeldingen]**
   beoordeelt elke melding en handelt haar zo nodig af als beveiligingsincident. [5.17.01]
7. Na **[aantal mislukte pogingen]** mislukte aanmeldingen blokkeert het systeem het account
   tijdelijk. [5.17.03]

> **Alleen als: Hoe ziet je werkplek eruit? «Cloudwerkplek (bijvoorbeeld Microsoft 365)» of «Hybride: cloud naast een virtuele of lokale werkplek»**
>
> 8. Op de cloudwerkplek dwingt de identiteitsvoorziening MFA af met regels voor voorwaardelijke toegang.
>    Verouderde aanmeldprotocollen zonder MFA staan uit. [5.17.01]

> **Alleen als: Hoe ziet je werkplek eruit? «On-premises»**
>
> 9. Op de on-premises werkplek geldt MFA bij elke toegang van buiten het kantoornetwerk (VPN of remote
>    desktop) en bij elk beheeraccount. Op kantoor loopt het primaire aanmelden met een pas of token. [5.17.01]

### 3.3 Wachtwoorden

1. Elke medewerker krijgt een wachtwoordmanager van de organisatie. Wachtwoorden voor werk staan niet in
   browsers op privéapparaten, in documenten of op papier. [5.17.02]
2. De beheerder dwingt de eisen aan wachtwoorden technisch af in de identiteitsvoorziening en in elk systeem
   met een eigen accountbeheer: minimaal
   **[minimale wachtwoordlengte]**,
   controle tegen lijsten van gelekte en veelgebruikte wachtwoorden en geen hergebruik van eerdere
   wachtwoorden. [5.17.03]
3. Wachtwoorden verlopen niet periodiek. Bij een vermoeden van lekken vervangt de gebruiker het wachtwoord
   direct. [5.17.03]

### 3.4 Toegang tot de vertrouwde zone en werken op afstand

1. Toegang tot het interne netwerk en de interne systemen krijgt alleen apparatuur die de organisatie kent en
   heeft geauthenticeerd, of programmatuur in een afgeschermde omgeving zoals een virtuele werkplek of een
   beveiligde browser. Een onbekend of privéapparaat komt niet rechtstreeks in de vertrouwde zone. [5.15.01]
2. Werken op afstand gebeurt alleen via de voorzieningen die de organisatie daarvoor biedt, met MFA. De
   medewerker opent informatie met het label vertrouwelijk of hoger op afstand alleen op een apparaat van de
   organisatie en werkt niet op een plek waar anderen kunnen meekijken. **[lijneigenaar logische toegang]**
   legt in de regeling thuiswerken vast welke apparatuur en werkplekken zijn toegestaan en beoordeelt die
   regeling jaarlijks. [6.07.01]

> **Alleen als: Hoe ziet je werkplek eruit? «Cloudwerkplek (bijvoorbeeld Microsoft 365)» of «Hybride: cloud naast een virtuele of lokale werkplek»**
>
> 3. In de cloudomgeving geldt een apparaat als geauthenticeerd als het in het apparaatbeheer staat en aan het
>    nalevingsbeleid voldoet. Andere apparaten krijgen hooguit de webversie zonder downloaden. [5.15.01]

> **Alleen als: Hoe ziet je werkplek eruit? «On-premises» of «Hybride: cloud naast een virtuele of lokale werkplek»**
>
> 4. Op het interne netwerk krijgt een apparaat pas toegang na authenticatie met een apparaatcertificaat
>    (netwerktoegangscontrole). Toegang van buiten loopt via een VPN of virtuele werkplek die ook het apparaat
>    controleert. [5.15.01]

### 3.5 Toegangsrechten en periodieke beoordeling

1. Een bevoegde leidinggevende vraagt rechten aan via het ticketsysteem; functioneel beheer toetst de aanvraag
   aan de autorisatiematrix en richt de rechten in. Het ticket toont aanvraag, goedkeuring en inrichting.
   [5.18.02, 8.03.02]
2. Gebruikers zien en bewerken alleen de informatie die ze voor hun taak nodig hebben. Een systeem met het
   label vertrouwelijk of hoger beperkt de toegang tot de dossiers of zaken waar de gebruiker bij betrokken
   is, waar het systeem dat ondersteunt. [8.03.02]
3. De systeemeigenaar beoordeelt jaarlijks alle uitgegeven rechten van zijn systeem, met een overzicht van
   functioneel beheer, en legt de uitkomst vast. Voor systemen met het label vertrouwelijk of hoger is dat
   elk halfjaar. Onjuiste rechten worden binnen
   **[hersteltermijn rechten]** ingetrokken. [5.18.02]
4. Kan functiescheiding door een kleine bezetting niet, dan legt de systeemeigenaar vast wie welke rollen
   combineert en waarom, en controleert hij elk kwartaal de handelingen van die persoon in de logging.
   [5.18.02]

> **Alleen als: Op welke landelijke voorzieningen ben je aangesloten? «DigiD» of «Suwinet» of «BRP (als bronhouder of afnemer)» of «BAG of andere basisregistraties» of «Andere ketens met eigen beveiligingseisen»**
>
> 5. Voor elke aansluiting op een landelijke voorziening geldt aanvullend het normenkader van die voorziening.
>    De systeemeigenaar toont de naleving van de autorisatie-eisen aan in de jaarlijkse verantwoording over de
>    aansluiting. [5.18.02]

> **Alleen als: Op welke landelijke voorzieningen ben je aangesloten? «Suwinet»**
>
> 6. Toegang tot Suwinet-Inkijk verloopt per rol die aansluit op de taak (bijvoorbeeld werk en inkomen of
>    schuldhulpverlening). De systeemeigenaar beoordeelt de Suwinet-autorisaties elk kwartaal en laat het
>    gebruik steekproefsgewijs controleren op raadplegingen zonder dossier of zaak. [5.18.02, 8.03.02]

> **Alleen als: Op welke landelijke voorzieningen ben je aangesloten? «BRP (als bronhouder of afnemer)»**
>
> 7. Raadpleging en wijziging van de BRP gebeuren alleen met rechten per rol volgens de autorisatie van de
>    organisatie als afnemer of bronhouder. De systeemeigenaar beoordeelt de rechten om persoonslijsten te
>    wijzigen elk kwartaal. [5.18.02, 8.03.02]

> **Alleen als: Op welke landelijke voorzieningen ben je aangesloten? «DigiD»**
>
> 8. De systeemeigenaar beoordeelt elk kwartaal de beheerrechten op de webapplicaties en infrastructuur achter
>    de DigiD-aansluiting, als voorbereiding op het DigiD-assessment. [8.02.01]

> **Alleen als: Verwerk je politiegegevens (boa's, opsporing, handhaving)? «Ja»**
>
> 9. Politiegegevens (bijvoorbeeld van boa's) staan in een omgeving die alleen toegankelijk is voor
>    medewerkers die de organisatie daartoe schriftelijk heeft geautoriseerd onder de Wpg. De autorisatie
>    noemt per persoon het doel en de categorie gegevens. [8.03.01, 8.03.02]
> 10. De systeemeigenaar beoordeelt de autorisaties voor politiegegevens elk halfjaar, en elke raadpleging wordt
>    vastgelegd, zodat de periodieke Wpg-audit kan aantonen wie wat heeft ingezien. [5.18.02]

### 3.6 Accounts met bijzondere rechten

1. Een beheerder heeft een apart beheeraccount, zonder mail en internettoegang. [8.02.01]
2. Beheerrechten worden waar het kan alleen voor de duur van een taak toegekend (just-in-time), met een
   aanvraag en een reden. Permanente rechten op het hoogste niveau (domein- of tenantbeheer) hebben ten
   hoogste
   **[maximum aantal hoogste beheerders]**.
   [8.02.01]
3. **[lijneigenaar logische toegang]** houdt een register bij van accounts met bijzondere rechten:
   beheeraccounts, technische accounts, noodaccounts en accounts van leveranciers. De systeemeigenaar en de
   CISO beoordelen elk kwartaal opzet, bestaan en gebruik van die rechten en tekenen het verslag. [8.02.01]
4. Het aanmaken van een account met bijzondere rechten en elke wijziging van zijn rechten levert automatisch
   een melding op. Een wijziging zonder goedgekeurde aanvraag is een beveiligingsincident. [5.18.01]
5. Een noodaccount ligt in een kluis met vier-ogentoegang; elk gebruik levert een melding op die de CISO
   beoordeelt. [5.18.01]
6. Systeemhulpmiddelen die beveiligingsmaatregelen kunnen omzeilen (beheerconsoles, scripttools, debuggers,
   tools voor het lezen van geheugen of register) staan alleen ter beschikking van bevoegde beheerders en
   alleen als hun taak dat vraagt. Op werkplekken van gebruikers zijn ze geblokkeerd. [8.18.01]
7. Het gebruik van systeemhulpmiddelen wordt gelogd. De logging blijft ten minste zes maanden beschikbaar voor
   onderzoek. [8.18.02]

> **Alleen als: Wie beheert je IT? «Eigen beheer»**
>
> 8. De eigen IT-afdeling houdt het register van accounts met bijzondere rechten bij en richt de meldingen in.
>    De beoordeling per kwartaal gebeurt door iemand buiten het beheerteam. [5.18.01, 8.02.01]

> **Alleen als: Wie beheert je IT? «Regie: eigen organisatie stuurt, beheer is uitbesteed» of «Volledig uitbesteed»**
>
> 9. De beheerpartij levert elk kwartaal een overzicht van alle accounts met bijzondere rechten op de systemen
>    van de organisatie, met de wijzigingen. De organisatie beoordeelt dat overzicht; de beheerpartij meldt een
>    niet goedgekeurde wijziging als beveiligingsincident binnen de termijn uit het contract. [5.18.01, 8.02.01]
> 10. Het contract bepaalt dat de beheerpartij systeemhulpmiddelen alleen inzet voor de afgesproken
>    dienstverlening en de logging daarvan zes maanden bewaart en op verzoek levert. [8.18.01, 8.18.02]

### 3.7 Toegang voor leveranciers

1. Een leverancier krijgt toegang tot het netwerk of een systeem pas na een risicoafweging door de
   systeemeigenaar: welke systemen, welke rechten, vanaf waar en voor hoe lang. Een leidinggevende van de
   organisatie is verantwoordelijk voor het account en zegt het op als het werk klaar is. [8.05.01]
2. Een leveranciersaccount staat standaard uit en wordt per werkzaamheid geactiveerd, voor ten hoogste
   **[maximale activeringsduur]**, altijd met MFA en via een afgeschermde
   beheeromgeving. [8.05.01]
3. Het register van leveranciersaccounts laat zien wie toegang heeft, wie die heeft goedgekeurd en wanneer
   ze is geactiveerd en beëindigd. [8.05.01]

### 3.8 Informatie met een hoog vertrouwelijkheidslabel

1. Informatie met het label vertrouwelijk, strikt vertrouwelijk of geheim (beleid informatieclassificatie) staat in
   aparte systemen, databases of omgevingen die fysiek of logisch gescheiden zijn van de algemene
   werkomgeving, met een eigen autorisatie die de systeemeigenaar vaststelt. [8.03.01]

> **Alleen als: In welke gevoelige domeinen verwerk je persoonsgegevens? «Sociaal domein» of «Jeugd» of «Gezondheid (WvGGZ, NTA 7516)»**
>
> 2. Dossiers in het sociaal domein, over jeugd of over gezondheid staan in een zaak- of dossiersysteem met
>    autorisatie per dossier of per team, niet op gedeelde netwerkschijven of in algemene teamsites. Inzage
>    buiten de eigen caseload wordt gelogd en door de systeemeigenaar elk kwartaal steekproefsgewijs
>    gecontroleerd. [8.03.01, 8.03.02]

### 3.9 Broncode

1. Toegang tot broncode, scripts en configuratiebestanden in een repository is beperkt tot de ontwikkelaars
   en beheerders die eraan werken; de eigenaar van de repository kent lees- en schrijfrechten apart toe en
   beoordeelt elk halfjaar wie toegang heeft. [8.04.01]
2. Een wijziging op de hoofdtak komt er alleen in na review door een tweede persoon; de repository dwingt
   dat af en legt vast wie wat heeft goedgekeurd. Broncode van systemen met het label vertrouwelijk of hoger
   staat niet in een openbare repository. [8.04.01]

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| **[lijneigenaar logische toegang]** | Eigenaar van dit beleid, de identiteitsvoorziening, het accountproces, de registers van bijzondere en leveranciersaccounts, de regeling thuiswerken |
| Systeemeigenaar | Autorisatieprocedure en autorisatiematrix, periodieke beoordeling van rechten, risicoafweging voor leveranciers, maatregelen waar MFA niet kan |
| Proceseigenaar | Motivering van gedeelde accounts en goedkeuring van maatregelen waar MFA niet kan |
| Leidinggevende | Aanvragen en tijdig intrekken van rechten van eigen medewerkers en van leveranciersaccounts |
| Eigenaar van een repository | Toegang tot broncode en review van wijzigingen |
| **[bewaking aanmeldingen]** | Beoordelen van meldingen over misbruik van accounts |
| CISO | Toetsing van autorisatieprocedures, kwartaalbeoordeling van bijzondere rechten, beoordeling van afwijkingen |
| Inkoop en contractbeheer | Eisen uit dit beleid vastleggen bij beheerpartijen en hun verklaringen toetsen |
| Medewerkers | Persoonlijk gebruik van account en tweede factor, melden van verlies of misbruik |

## 5. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in **[registratie van controles]**;
afwijkingen gaan als bevinding naar het risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| LTB-01 | Accounts van vertrokken medewerkers en beëindigde opdrachten zijn uiterlijk op de laatste werkdag geblokkeerd en na de termijn verwijderd; inactieve accounts zijn geblokkeerd | **[lijneigenaar logische toegang]** | Per kwartaal | Vergelijking van de personeelsmutaties met de accountmutaties, rapport inactieve accounts | 5.16.01 |
| LTB-02 | Gedeelde accounts, functionele postbussen, technische accounts en standaardaccounts voldoen aan de eisen: motivering, eigenaar, geen beheerrechten, geen interactief aanmelden | **[lijneigenaar logische toegang]** | Jaarlijks | Register van gedeelde en technische accounts met de beoordeling per account | 5.16.02, 5.18.01 |
| LTB-03 | MFA geldt voor alle accounts waar dit beleid het eist; elke uitzondering heeft goedgekeurde aanvullende maatregelen en staat in het risicoregister | CISO | Jaarlijks | Rapport uit de identiteitsvoorziening, lijst van uitzonderingen met maatregelen | 5.17.01 |
| LTB-04 | De wachtwoordeisen en de blokkade na mislukte pogingen zijn technisch afgedwongen; resets volgden na identiteitsvaststelling | **[lijneigenaar logische toegang]** | Jaarlijks | Configuratierapport per systeem, steekproef van tickets | 5.17.02, 5.17.03 |
| LTB-05 | Alleen geauthenticeerde apparaten bereiken de vertrouwde zone; werken op afstand loopt via de eigen voorzieningen en de regeling thuiswerken is actueel | **[lijneigenaar logische toegang]** | Jaarlijks | Rapport uit apparaatbeheer of netwerktoegangscontrole, regeling thuiswerken | 5.15.01, 6.07.01 |
| LTB-06 | Alle uitgegeven rechten per systeem zijn beoordeeld door de systeemeigenaar en onjuiste rechten zijn binnen de hersteltermijn ingetrokken | Systeemeigenaar | Jaarlijks, halfjaarlijks voor systemen met het label vertrouwelijk of hoger | Overzicht van rechten met akkoord, doorgevoerde correcties | 5.18.02, 8.03.01, 8.03.02 |
| LTB-07 | Het register van accounts met bijzondere rechten klopt in opzet, bestaan en gebruik; elke wijziging had een aanvraag; systeemhulpmiddelen zijn alleen door bevoegde beheerders gebruikt | Systeemeigenaar en CISO | Per kwartaal | Getekend verslag, meldingen van wijzigingen, logging van systeemhulpmiddelen | 8.02.01, 5.18.01, 8.18.01, 8.18.02 |
| LTB-08 | Leveranciersaccounts hebben een risicoafweging, een verantwoordelijke leidinggevende en zijn alleen actief geweest voor de afgesproken werkzaamheden | **[lijneigenaar logische toegang]** | Per kwartaal | Register van leveranciersaccounts met activeringen en beëindigingen | 8.05.01 |
| LTB-09 | Toegang tot repositories is beperkt tot wie eraan werkt en wijzigingen op de hoofdtak hebben een review | Eigenaar van de repository | Halfjaarlijks | Toegangslijst per repository, instellingen van de hoofdtak, steekproef van reviews | 8.04.01 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De
systeemeigenaar dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de looptijd.
De afwijking geldt pas na acceptatie van het risico door **[risico-eigenaar]**
en staat in het risicoregister; afwijkingen worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid screening,
bewustzijn en opleiding (in- en uitdiensttreding), het beleid informatieclassificatie (labels), het beleid
informatiebeveiliging bij inkoop en contractbeheer (beheerpartijen), het beleid logging en monitoring
(aanmeldingen en beheerhandelingen), het beleid netwerkbeveiliging (beheerinterfaces), het beleid veilige
softwareontwikkeling (repositories) en het beleid mobile device management (apparaten).

## Bijlage A: BIO 2.0-maatregelen

De maatregelen van dit domein (16, waarvan 14 overheidsmaatregelen), waar dit stuk ze invult en welke controle ze aantoont. Nummers volgens BIO2 v1.3 definitief - 9 januari 2026; de tekst van de maatregel staat bij het CIP. Waar de BIO 2.0 geen overheidsmaatregel kent, geldt de ISO 27002-beheersmaatregel.

| Maatregel | Titel | Soort | In dit stuk | Controle |
|---|---|---|---|---|
| 5.15.01 | Toegangsbeveiliging | overheidsmaatregel | 3.4 Toegang tot de vertrouwde zone en werken op afstand | LTB-05 |
| 5.16.01 | Identiteitsbeheer | overheidsmaatregel | 3.1 Identiteiten en accounts | LTB-01 |
| 5.16.02 | Identiteitsbeheer | overheidsmaatregel | 3.1 Identiteiten en accounts | LTB-02 |
| 5.17.01 | Authenticatie-informatie | overheidsmaatregel | 3.2 Authenticatie en MFA | LTB-03 |
| 5.17.02 | Authenticatie-informatie | overheidsmaatregel | 3.3 Wachtwoorden | LTB-04 |
| 5.17.03 | Authenticatie-informatie | overheidsmaatregel | 3.2 Authenticatie en MFA | LTB-04 |
| 5.18.01 | Toegangsrechten | overheidsmaatregel | 3.1 Identiteiten en accounts | LTB-02, LTB-07 |
| 5.18.02 | Toegangsrechten | overheidsmaatregel | 3.5 Toegangsrechten en periodieke beoordeling | LTB-06 |
| 6.07.01 | Werken op afstand | ISO-beheersmaatregel | 3.4 Toegang tot de vertrouwde zone en werken op afstand | LTB-05 |
| 8.02.01 | Speciale toegangsrechten | overheidsmaatregel | 3.5 Toegangsrechten en periodieke beoordeling | LTB-07 |
| 8.03.01 | Beperking toegang tot informatie | overheidsmaatregel | 3.5 Toegangsrechten en periodieke beoordeling | LTB-06 |
| 8.03.02 | Beperking toegang tot informatie | overheidsmaatregel | 3.5 Toegangsrechten en periodieke beoordeling | LTB-06 |
| 8.04.01 | Toegangsbeveiliging op broncode | ISO-beheersmaatregel | 3.9 Broncode | LTB-09 |
| 8.05.01 | Beveiligde authenticatie | overheidsmaatregel | 3.7 Toegang voor leveranciers | LTB-08 |
| 8.18.01 | Gebruik van speciale systeemhulpmiddelen | overheidsmaatregel | 3.6 Accounts met bijzondere rechten | LTB-07 |
| 8.18.02 | Gebruik van speciale systeemhulpmiddelen | overheidsmaatregel | 3.6 Accounts met bijzondere rechten | LTB-07 |

## Bijlage B: Afkortingen

| Afkorting | Betekenis |
|---|---|
| BAG | Basisregistratie Adressen en Gebouwen |
| BIO | Baseline Informatiebeveiliging Overheid |
| BRP | Basisregistratie Personen |
| CISO | Chief Information Security Officer |
| ISAE | International Standard on Assurance Engagements |
| ISO | International Organization for Standardization |
| IT | Informatietechnologie |
| MFA | Meerfactorauthenticatie |
| NTA | Nederlandse technische afspraak |
| SSO | Single sign-on |
| VPN | Virtual private network |
| Wpg | Wet politiegegevens |
| WvGGZ | Wet verplichte geestelijke gezondheidszorg |

## Nog in te vullen

- **lijneigenaar logische toegang**: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd IT of informatievoorziening
- **termijn verwijderen accounts**: bijvoorbeeld 90 dagen na blokkade
- **termijn inactiviteit**: bijvoorbeeld 60 dagen
- **bewaking aanmeldingen**: het SOC, de SOC-dienstverlener of de beheerder die de meldingen beoordeelt
- **aantal mislukte pogingen**: bijvoorbeeld 5
- **minimale wachtwoordlengte**: bijvoorbeeld 12 tekens voor gebruikers en 16 voor beheerders
- **hersteltermijn rechten**: bijvoorbeeld tien werkdagen
- **maximum aantal hoogste beheerders**: bijvoorbeeld drie benoemde personen plus een noodaccount
- **maximale activeringsduur**: bijvoorbeeld 14 dagen
- **registratie van controles**: het systeem waarin controles worden vastgelegd, bijvoorbeeld het ticketsysteem of het managementsysteem
- **risico-eigenaar**: de manager die restrisico's accepteert
- **eigenaar van dit beleid**: de manager die dit beleid uitvoert en laat naleven
- **vaststeller**: wie het beleid vaststelt, bijvoorbeeld de directie of het bestuur
