---
domein: logische-toegang
titel: Beleid logische toegangsbeveiliging
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor de toegang tot informatiesystemen,
netwerken en gegevens. Het geldt voor alle accounts op
systemen waarvan de organisatie eigenaar is, ook als een leverancier ze beheert of host: accounts van
medewerkers, inhuur, stagiairs, leveranciers, functionele accounts en technische (service)accounts. Het gaat
over de ISO-beheersmaatregelen 5.15 tot en met 5.18, 6.07, 8.02 tot en met 8.05 en 8.18.

Buiten dit beleid vallen de netwerkscheiding en de beheerinterfaces (beleid netwerkbeveiliging), de
logging zelf (beleid logging en monitoring) en de vergrendeling van werkplekken (beleid IT-compliance).

::: als beheer=regie,uitbesteed
De organisatie beheert haar IT niet zelf. Waar dit beleid een eis stelt aan beheerders of aan het
beheerproces, legt de organisatie die eis vast in het contract en de dienstverleningsovereenkomst met de
beheerpartij en controleert ze de naleving met de rapportages en verklaringen die de leverancier aanlevert.
De toekenning van rechten aan eigen medewerkers blijft een besluit van de organisatie zelf.
:::

## 2. Uitgangspunten

1. Elke handeling op een systeem is herleidbaar tot één natuurlijke persoon. Accounts zijn persoonsgebonden;
   gedeelde accounts zijn een gemotiveerde uitzondering.
2. Iemand krijgt alleen de rechten die nodig zijn voor de eigen taak, en niet langer dan nodig
   (need-to-know en least privilege).
3. Rechten volgen een rol uit een autorisatiematrix. Losse rechten buiten een rol zijn een uitzondering met
   een einddatum.
4. Beschikken, uitvoeren en controleren liggen niet bij dezelfde persoon. Beheerders hebben geen toegang tot
   de inhoud van de gegevens die ze beheren, tenzij de systeemeigenaar dat vastlegt en er apart toezicht op
   houdt.
5. Hoe zwaarder de rechten of hoe gevoeliger de informatie, hoe sterker de authenticatie en hoe vaker de
   controle.

## 3. Beleidsregels

### 3.1 Identiteiten en accounts

- Accounts ontstaan, wijzigen en vervallen via één vastgelegd proces dat gekoppeld is aan de
  personeelsadministratie en de registratie van inhuur: indiensttreding of start van een opdracht levert een
  account op, een functiewijziging past de rechten aan en uitdiensttreding of einde opdracht blokkeert het
  account uiterlijk op de laatste werkdag. Het account wordt na
  [[termijn verwijderen accounts: bijvoorbeeld 90 dagen na blokkade]]
  verwijderd. Accounts van inhuur en stagiairs hebben een einddatum gelijk aan het einde van de opdracht. [5.16.01]
- Een account dat
  [[termijn inactiviteit: bijvoorbeeld 60 dagen]]
  niet is gebruikt, wordt automatisch geblokkeerd. [5.16.01]
- Elk systeem heeft een autorisatieprocedure en een autorisatiematrix die de systeemeigenaar opstelt met de
  proceseigenaren. De CISO toetst de procedure voor vaststelling. Een mandaatregister legt vast wie rechten
  mag aanvragen en goedkeuren. [5.16.01]
- Gedeelde accounts (groepsaccounts) gebruikt de organisatie alleen als een persoonlijk account aantoonbaar
  niet kan. De proceseigenaar motiveert het gebruik schriftelijk, stemt het af met de CISO en wijst een
  leidinggevende aan die verantwoordelijk is voor het gebruik en het tijdig opzeggen. [5.16.02]
- Een gedeeld account krijgt een herkenbare naam, geen toegang van buiten en geen beheerrechten. Het
  register van gedeelde accounts wordt jaarlijks doorgelopen. [5.16.02]
- Een functionele postbus (op naam van een team, project of product) heeft een eigenaar en wordt geopend
  met persoonlijke accounts die toegang krijgen tot de postbus. Er wordt niet met een gedeeld wachtwoord op de
  postbus zelf aangemeld. [5.16.02]
- Standaardaccounts van leveranciers en systemen worden uitgeschakeld of hernoemd en krijgen een nieuw
  wachtwoord voor ingebruikname. Technische accounts (serviceaccounts) hebben een eigenaar, kunnen niet
  interactief aanmelden en staan in het register van accounts met bijzondere rechten. [5.16.02, 5.18.01]

### 3.2 Authenticatie en MFA

- Meervoudige authenticatie (MFA) is verplicht bij het aanmelden op de digitale werkomgeving, bij elk account
  op een voorziening die via internet bereikbaar is en bij elk account met beheerrechten. Waar de
  risicoanalyse van een systeem dat vraagt, komt MFA er ook bij andere accounts bij. [5.17.01]
- De voorkeur gaat naar wachtwoordloze authenticatie met een persoonsgebonden sleutel, zoals een passkey of
  een hardwaretoken met pincode. Anders combineert de organisatie een wachtwoord met ten minste een tweede
  factor. Een sms-code is alleen toegestaan als er geen andere tweede factor beschikbaar is. [5.17.01]
- Waar het kan, loopt aanmelden via de centrale identiteitsvoorziening met single sign-on. Beheerders bereiken beheeromgevingen via een beveiligde
  tussenstap (een stepping stone of jumpserver) waarop ook MFA geldt. [5.17.01]
- Kan een systeem geen MFA, dan stelt de systeemeigenaar met de CISO aanvullende maatregelen op, zoals
  toegang alleen vanaf het interne netwerk of vanaf beheerde apparaten. De proceseigenaar keurt die
  maatregelen goed; het systeem staat met die maatregelen in het risicoregister. [5.17.01]
- Inloggegevens, tokens en resets worden pas uitgereikt nadat de identiteit van de ontvanger is vastgesteld.
  [5.17.01]
- De organisatie bewaakt de aanmeldingen op misbruik. Ten minste deze signalen leiden tot een melding:
  aanmelden vanaf een ongebruikelijke locatie of een onmogelijke reisafstand, en een plotselinge piek in
  mislukte aanmeldingen. Elke melding wordt beoordeeld en zo nodig als beveiligingsincident afgehandeld. [5.17.01]
- Na
  [[aantal mislukte pogingen: bijvoorbeeld 5]]
  mislukte aanmeldingen wordt het account tijdelijk geblokkeerd. [5.17.03]

::: als werkplek=cloud,hybride
- Op de cloudwerkplek dwingt de organisatie MFA af met beleidsregels voor voorwaardelijke toegang in de
  identiteitsvoorziening. Verouderde aanmeldprotocollen die geen MFA ondersteunen, staan uit. [5.17.01]
:::

::: als werkplek=on-premises
- Op de on-premises werkplek geldt MFA bij elke toegang van buiten het kantoornetwerk (VPN of remote
  desktop) en bij elk beheeraccount. Op kantoor is MFA voor het primaire aanmelden ingericht met een pas of
  token. [5.17.01]
:::

### 3.3 Wachtwoorden

- Elke medewerker krijgt een wachtwoordmanager die de organisatie beheert. Wachtwoorden voor werk staan niet
  in browsers op privéapparaten, in documenten of op papier. [5.17.02]
- De eisen aan wachtwoorden worden technisch afgedwongen in de identiteitsvoorziening en in elk systeem met
  een eigen accountbeheer: minimaal
  [[minimale wachtwoordlengte: bijvoorbeeld 12 tekens voor gebruikers en 16 voor beheerders]],
  controle tegen lijsten van gelekte en veelgebruikte wachtwoorden en geen hergebruik van eerdere
  wachtwoorden. [5.17.03]
- Wachtwoorden verlopen niet periodiek. Bij een vermoeden van lekken wordt het wachtwoord direct
  vervangen. [5.17.03]

### 3.4 Toegang tot de vertrouwde zone en werken op afstand

- Toegang tot het interne netwerk en de interne systemen krijgt alleen apparatuur die de organisatie kent en
  heeft geauthenticeerd, of programmatuur die draait in een afgeschermde omgeving zoals een virtuele
  werkplek of een beveiligde browser. Een onbekend of privéapparaat komt niet rechtstreeks in de vertrouwde
  zone. [5.15.01]
- Werken op afstand gebeurt via de voorzieningen die de organisatie daarvoor biedt, met MFA. Informatie met
  een hoge classificatie wordt op afstand alleen geopend op een apparaat van de organisatie. [6.07.01]

::: als werkplek=cloud,hybride
- In de cloudomgeving geldt een apparaat als geauthenticeerd als het in het apparaatbeheer staat en aan het
  nalevingsbeleid voldoet. Andere apparaten krijgen hooguit de webversie zonder downloaden. [5.15.01]
:::

::: als werkplek=on-premises,hybride
- Op het interne netwerk krijgt een apparaat pas toegang na authenticatie met een apparaatcertificaat
  (netwerktoegangscontrole). Toegang van buiten loopt via een VPN of virtuele werkplek die ook het apparaat
  controleert. [5.15.01]
:::

### 3.5 Toegangsrechten en periodieke beoordeling

- Een bevoegde leidinggevende vraagt rechten aan; ze worden getoetst aan de autorisatiematrix en daarna
  ingericht, met een vastgelegd spoor. [5.18.02, 8.03.02]
- Gebruikers zien en bewerken alleen de informatie die ze voor hun taak nodig hebben. Een systeem met
  informatie met specifiek belang beperkt de toegang tot de dossiers of zaken waar de gebruiker bij
  betrokken is, waar het systeem dat ondersteunt. [8.03.02]
- De systeemeigenaar beoordeelt ten minste eens per jaar alle uitgegeven rechten van een systeem, met een
  overzicht dat functioneel beheer aanlevert. De risicoanalyse van het systeem kan een hogere frequentie
  voorschrijven; voor systemen met informatie met specifiek belang is dat elk halfjaar. Onjuiste rechten
  worden binnen
  [[hersteltermijn rechten: bijvoorbeeld tien werkdagen]]
  ingetrokken. [5.18.02]
- Kan functiescheiding door een kleine bezetting niet, dan legt de systeemeigenaar vast wie welke rollen
  combineert en waarom, en controleert hij elk kwartaal de handelingen van die persoon. [5.18.02]

::: als ketens=digid,suwinet,brp,bag,anders
- Voor elke aansluiting op een landelijke voorziening geldt aanvullend het normenkader van die voorziening.
  De organisatie houdt per aansluiting bij welke autorisatie-eisen gelden en toetst die in de verantwoording
  over de aansluiting. [5.18.02]
:::

::: als ketens=suwinet
- Toegang tot Suwinet-Inkijk verloopt per rol die aansluit op de taak (bijvoorbeeld werk en inkomen of
  schuldhulpverlening). De systeemeigenaar beoordeelt de Suwinet-autorisaties elk kwartaal en laat het
  gebruik steekproefsgewijs controleren op raadplegingen zonder dossier of zaak. [5.18.02, 8.03.02]
:::

::: als ketens=brp
- Raadpleging en wijziging van de BRP gebeuren alleen met rechten per rol volgens de autorisatie van de
  organisatie als afnemer of bronhouder. Rechten om persoonslijsten te wijzigen worden elk kwartaal
  beoordeeld. [5.18.02, 8.03.02]
:::

::: als ketens=digid
- Beheerrechten op de webapplicaties en infrastructuur achter de DigiD-aansluiting worden elk kwartaal
  beoordeeld, als voorbereiding op het DigiD-assessment. [8.02.01]
:::

::: als politiegegevens=ja
- Politiegegevens (bijvoorbeeld van boa's) staan in een omgeving die alleen toegankelijk is voor
  medewerkers die de organisatie daartoe schriftelijk heeft geautoriseerd onder de Wet politiegegevens. De
  autorisatie noemt per persoon het doel en de categorie gegevens. [8.03.01, 8.03.02]
- De autorisaties voor politiegegevens worden elk halfjaar beoordeeld en elke raadpleging wordt vastgelegd,
  zodat de periodieke Wpg-audit kan aantonen wie wat heeft ingezien. [5.18.02]
:::

### 3.6 Accounts met bijzondere rechten

- Een beheerder heeft een apart beheeraccount, zonder mail en internettoegang. [8.02.01]
- Beheerrechten worden waar het kan alleen voor de duur van een taak toegekend (just-in-time), met een
  aanvraag en een vastgelegde reden. Permanente rechten op het hoogste niveau (bijvoorbeeld domein- of
  tenantbeheer) hebben ten hoogste
  [[maximum aantal hoogste beheerders: bijvoorbeeld drie benoemde personen plus een noodaccount]].
  [8.02.01]
- Er is een register van accounts met bijzondere rechten: beheeraccounts, technische accounts,
  noodaccounts en accounts van leveranciers. De systeemeigenaar en de CISO beoordelen elk kwartaal of de
  rechten in opzet kloppen, of ze bestaan zoals geregistreerd en of ze alleen zijn gebruikt waarvoor ze
  bedoeld zijn. [8.02.01]
- Het aanmaken van een account met bijzondere rechten en elke wijziging van zijn rechten levert automatisch
  een melding op. Een wijziging zonder goedgekeurde aanvraag is een beveiligingsincident en wordt als zodanig
  geregistreerd en afgehandeld. [5.18.01]
- Een noodaccount ligt in een kluis met vier-ogentoegang; elk gebruik levert een melding op. [5.18.01]
- Systeemhulpmiddelen die beveiligingsmaatregelen kunnen omzeilen (bijvoorbeeld beheerconsoles,
  scripttools, debuggers en tools voor het lezen van geheugen of register) staan alleen ter beschikking van
  bevoegde beheerders en alleen op het moment dat hun taak dat vraagt. Op werkplekken van gebruikers zijn
  ze geblokkeerd. [8.18.01]
- Het gebruik van systeemhulpmiddelen wordt gelogd. De logging blijft ten minste zes maanden beschikbaar voor
  onderzoek. [8.18.02]

::: als beheer=eigen
- De eigen IT-afdeling houdt het register van accounts met bijzondere rechten bij en richt de meldingen bij
  aanmaken en wijzigen in. De beoordeling per kwartaal gebeurt door iemand buiten het beheerteam. [5.18.01, 8.02.01]
:::

::: als beheer=regie,uitbesteed
- De beheerpartij levert elk kwartaal een overzicht van alle accounts met bijzondere rechten op de systemen
  van de organisatie, met wijzigingen sinds het vorige overzicht. De organisatie beoordeelt dat overzicht en
  laat de beheerpartij een niet goedgekeurde wijziging melden als beveiligingsincident binnen de termijn uit
  het contract. [5.18.01, 8.02.01]
- In het contract staat dat de beheerpartij systeemhulpmiddelen alleen inzet voor de afgesproken
  dienstverlening en de logging daarvan zes maanden bewaart en op verzoek aanlevert. [8.18.01, 8.18.02]
:::

### 3.7 Toegang voor leveranciers

- Een leverancier krijgt toegang tot het netwerk of een systeem pas na een risicoafweging door de
  systeemeigenaar. Die afweging legt vast welke systemen, welke rechten, vanaf waar en voor hoe lang. Een
  leidinggevende van de organisatie is verantwoordelijk voor het account en zegt het op als het werk klaar
  is. [8.05.01]
- Een leveranciersaccount staat standaard uit en wordt per werkzaamheid geactiveerd, voor ten hoogste
  [[maximale activeringsduur: bijvoorbeeld 14 dagen]].
  Toegang loopt altijd met MFA en via een afgeschermde beheeromgeving. [8.05.01]
- Het register van leveranciersaccounts laat zien wie toegang heeft, wie die heeft goedgekeurd en wanneer
  ze is geactiveerd en beëindigd. [8.05.01]

### 3.8 Informatie met specifiek belang

- De organisatie bepaalt welke informatie een specifiek belang heeft, op basis van het classificatiebeleid.
  Die informatie staat in aparte systemen, databases of omgevingen die fysiek of logisch gescheiden zijn
  van de algemene werkomgeving, met een eigen autorisatie. [8.03.01]

::: als gevoelig=sociaal,jeugd,gezondheid
- Dossiers in het sociaal domein, over jeugd of over gezondheid staan in een zaak- of dossiersysteem met
  autorisatie per dossier of per team. Ze staan niet op gedeelde netwerkschijven of in algemene teamsites.
  Inzage buiten de eigen caseload wordt gelogd en steekproefsgewijs gecontroleerd. [8.03.01, 8.03.02]
:::

### 3.9 Broncode

- Toegang tot broncode, scripts en configuratiebestanden in een repository is beperkt tot de ontwikkelaars
  en beheerders die eraan werken. Schrijfrechten op de hoofdtak vragen een review door een tweede persoon.
  [8.04.01]

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| [[lijneigenaar logische toegang: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd IT of informatievoorziening]] | Uitvoering van dit beleid, de identiteitsvoorziening en het accountproces |
| Systeemeigenaar | Autorisatieprocedure en autorisatiematrix per systeem, jaarlijkse beoordeling van rechten, risicoafweging voor leveranciers |
| Proceseigenaar | Motivering van gedeelde accounts en goedkeuring van maatregelen waar MFA niet kan |
| Leidinggevende | Aanvragen en tijdig intrekken van rechten van eigen medewerkers en van leveranciersaccounts |
| CISO | Toetsing van autorisatieprocedures, afstemming over gedeelde accounts, kwartaalbeoordeling van bijzondere rechten |
| Medewerkers | Persoonlijk gebruik van hun account en tweede factor, melden van verlies of misbruik |

## 5. Naleving en bewaking

- Elk kwartaal: beoordeling van het register van accounts met bijzondere rechten; bewijs is het getekende
  verslag met afwijkingen en hun afhandeling.
- Elk kwartaal: steekproef op accounts van uit dienst getreden medewerkers en beëindigde opdrachten tegen de
  personeelsadministratie; bewijs is de vergelijking.
- Jaarlijks per systeem: beoordeling van alle rechten door de systeemeigenaar; bewijs is het overzicht met
  akkoord en de doorgevoerde correcties.
- Jaarlijks: controle dat MFA geldt voor alle accounts waar dit beleid het eist, met de lijst van
  uitzonderingen en hun aanvullende maatregelen.
- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid screening en
bewustzijn (in- en uitdiensttreding), het classificatiebeleid (informatie met specifiek belang), het beleid
leveranciersbeheer (afspraken met beheerpartijen), het beleid logging en monitoring (vastleggen en bewaken
van aanmeldingen en beheerhandelingen), het beleid netwerkbeveiliging (beheerinterfaces en netwerkscheiding)
en het beleid mobile device management (apparaten die toegang krijgen).
