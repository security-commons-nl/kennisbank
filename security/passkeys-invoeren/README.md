---
titel: Passkeys invoeren
vakgebied: security
type: aanpak
normen: [BIO2]
versie: 2026-08
herkomst: CISO-organisatie van een Nederlandse gemeente die organisatiebreed is overgestapt op wachtwoordloos inloggen; gedeeld met toestemming
status: in gebruik
samenvatting: Handleiding om als publieke organisatie volledig over te stappen op phishing-resistente authenticatie met passkeys (FIDO2). Waarom het de grootste aanvalsroute afsnijdt, de negen stappen van inzicht tot borging, de keuzes die het verschil maken (geen fallback, device-bound, TAP als enige herstelroute) en wat er in de praktijk tegenzat. Met directiememo, FAQ, managersmail en herstelprocedure als sjablonen.
---

# Passkeys invoeren

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/passkeys-invoeren](https://security-commons-nl.github.io/kennisbank/security/passkeys-invoeren/)

Als je digitale dreiging platslaat, komt het meestal neer op drie dingen: iemand probeert je
inloggegevens te stelen (phishing, adversary-in-the-middle, credential theft), iemand probeert je iets te
laten uitvoeren (malware, misbruik van gebruikersacties), of je hebt zelf iets openstaan wat kwetsbaar is.
De eerste categorie is in de praktijk nog steeds de meest effectieve ingang. Het is ook de plek waar je
het snelst impact maakt: wachtwoorden loslaten en overstappen op phishing-resistente authenticatie.

Deze handleiding beschrijft hoe een gemeente dat organisatiebreed heeft gedaan, welke keuzes daarbij zijn
gemaakt en waar het in de praktijk tegenzat. Geen theorie; handvatten om zelf aan de slag te gaan. De
sjablonen die bij de uitrol zijn gebruikt, staan als bijlagen in deze map:

| Bestand | Wat het is |
|---|---|
| [`directiememo.md`](directiememo.md) | Memo aan directie of MT, ter kennisgeving vóór de overstap |
| [`mail-managers.md`](mail-managers.md) | Mail aan leidinggevenden: wat hun rol is in de uitrol |
| [`faq-medewerkers.md`](faq-medewerkers.md) | Veelgestelde vragen voor het intranet, 25 stuks |
| [`herstelprocedure-tap.md`](herstelprocedure-tap.md) | De enige herstelroute na de overstap: Temporary Access Pass |
| [`index.html`](index.html) | Deze handleiding als leesversie, plakbaar in Word |

## Waarom je huidige MFA niet genoeg is

Push-notificaties en number matching zijn "MFA" op papier, maar beide vertrouwen op je sessie en je
aandacht. Een aanvaller die een proxy tussen jou en de echte inlogpagina zet (adversary-in-the-middle),
laat jou zelf de goedkeuring geven; hij logt in vóór jou, of lokt je akkoord uit. Vrijwel alle
phishingcampagnes richten zich op de Microsoft-loginflow. Wie daar nog met push of number matching
inlogt, is voor die campagnes vatbaar.

Een passkey werkt anders. Het is een cryptografisch sleutelpaar op de FIDO2-standaard: de privésleutel
staat op je apparaat en verlaat dat apparaat niet, de publieke sleutel staat bij de identity provider.
Inloggen is een lokale handeling (pincode, vingerafdruk, gezicht) die alleen werkt voor het echte domein.
Een nepsite krijgt geen geldige handtekening, hoe overtuigend hij ook is.

In de praktijk: op een beheerde laptop met Windows Hello for Business gebruik je dit principe al en log je
in zonder telefoon. Op telefoon of tablet gebruik je de Microsoft Authenticator. Log je in op een ander
apparaat (een privé-pc), dan scan je een QR-code met de Authenticator; die legt via bluetooth kort
contact om te bevestigen dat je fysiek in de buurt bent. Op afstand inloggen met jouw account kan dan
niet meer, omdat jouw apparaat er letterlijk bij moet zijn.

## De aanpak in negen stappen

### 1. Inzicht en keuze

Begin niet met techniek maar met begrijpen waar je staat.

- Draait je identity centraal via Microsoft Entra ID, en zijn je kritieke applicaties via SSO gekoppeld?
  Of is het versnipperd: alleen Microsoft centraal, de rest losse logins?
- Maak een overzicht van applicaties zonder SSO en zonder FIDO2-ondersteuning.
- Werk je met beheerde devices waar Windows Hello for Business al op staat?
- Bepaal je doel: passkeys naast de bestaande login, of passkey-only.

Vanuit dat startpunt bepaal je de route. Ga je puur voor passkeys, of gebruik je het moment om alles
richting SSO te trekken? De gemeente uit deze handleiding koos bewust voor passkeys zelf, met vooraf het
landschap in kaart zodat duidelijk was waar risico's zouden blijven. Voor de leveranciersscope werkte een
afbakening op de kritieke processen: alle leveranciers die onderdeel zijn van een kritiek proces, aan SSO.

### 2. Bestuurlijke aftrap

Zorg dat dit een organisatiebesluit wordt. Het verhaal aan de directie was simpel: makkelijker inloggen,
geen wachtwoorden meer om te vergeten, minder druk op het shared service center, meer productiviteit. Met
als bijvangst dat een hele categorie phishing- en AiTM-aanvallen wegvalt.

Haal een concreet besluit op: wat, met wie, wanneer. Maak de impact duidelijk (het inloggen verandert,
tijdelijke druk op ondersteuning) en vraag akkoord op richting, globale planning en benodigde capaciteit.
Zonder bestuurlijke steun strandt de uitrol vroeg of laat omdat het "te lastig" is of "de business door
moet". De [directiememo](directiememo.md) is het sjabloon.

### 3. Projectteam

Stel een team samen met IT, informatiebeveiliging én het shared service center: niet alleen techniek, maar
juist de mensen die dagelijks met gebruikers werken. Spreek rollen af (techniek, communicatie, support) en
neem het team mee in wat passkeys zijn en wat er voor gebruikers verandert.

### 4. Technische basis

- Zet passkey-registratie aan in de Microsoft Authenticator.
- Richt een TAP-procedure in (Temporary Access Pass): dat wordt de vervanger van "wachtwoord vergeten".
- Bouw het Conditional Access-beleid: phishing-resistente authenticatie voorbereiden, legacy authenticatie
  in kaart brengen.
- Zet FIDO2-restricties aan en houd het aantal toegestane methodes klein: alleen de Microsoft
  Authenticator en hardwaresleutels zoals een YubiKey (via toegestane AAGUID's).

**Nog niet afdwingen.** In veel handleidingen gaat Conditional Access vrij snel aan; in de praktijk breek je
dan je eigen omgeving omdat gebruikers nog niet klaar zijn. Eerst registratie, dan gebruik, pas daarna
afdwingen.

### 5. Pilot

Test niet alleen of het werkt, maar hoe het voelt in dagelijks gebruik. Begin met een kleine testgroep en
breid uit met key users uit verschillende afdelingen. Test de scenario's laptop (Windows Hello), mobiel
en privé-device. Verzamel wat stukloopt: applicaties die niet werken, devices zonder bluetooth,
leveranciers.

Wat er in de pilot naar boven kwam: leveranciers met SSO die niet goed omgaan met passkeys, cloud-pc's
zonder Windows Hello, devices zonder bluetooth, en mobiele apps met halfwerkende webviews waardoor de
authenticatieflow stukloopt.

### 6. Keuzes en uitzonderingen

Hier maak je het verschil tussen theorie en praktijk.

- **Fallback tijdens registratie: nee.** De bootstrap- en recovery-flow loopt volledig via TAP. Sta je
  wachtwoord plus Authenticator toe als registratieroute, dan kunnen gebruikers na de omzetting via die
  weg passkeys blijven registreren en val je nooit helemaal wachtwoordloos.
- **Apps zonder FIDO2-ondersteuning:** uitzonderingen op applicatie-, gebruikers- of groepsniveau, waar
  nodig beperkt met IP- of device-restricties. Niet generiek, wel gericht. Niet mooi, wel gecontroleerd.
- **Leg vast welke uitzonderingen tijdelijk zijn en wanneer je ze afbouwt.**

### 7. Voorbereiding uitrol

Zorg dat de organisatie klaar is voordat je afdwingt. Informeer managers en laat hen hun teams activeren
(de [managersmail](mail-managers.md)). Publiceer uitleg op het intranet met korte video's en een
[FAQ](faq-medewerkers.md). Organiseer inloopsessies en ga langs dagstarts. Bereid het shared service
center voor op veelgestelde vragen en registratiehulp.

In deze periode loopt het shared service center vol. Niet omdat het misgaat, maar omdat mensen het
spannend vinden en geholpen willen worden. Daar moet je capaciteit op plannen.

### 8. Gefaseerde uitrol en afdwingen

Verdeel de organisatie in groepen (per afdeling) en zet Conditional Access gefaseerd aan. Kies het moment
slim: 's avonds omzetten, want de meeste mensen loggen 's ochtends in, de sessie verloopt 's avonds, en
je ziet dus die ochtend meteen of het werkt. Zorg dat SSC en IT stand-by staan; monitor wie faalt op de
policies. Begeleid kritieke gebruikers (directie, college) persoonlijk: samen zitten, instellen, dan pas
omzetten.

Vanaf het moment dat je afdwingt, verandert er iets fundamenteels: registratie via wachtwoord en MFA kan
niet meer. De TAP-procedure, via een interne pagina alleen toegankelijk voor SSC en IT, is dan de enige
manier om nog een passkey te registreren. Zie de [herstelprocedure](herstelprocedure-tap.md).

Uiteindelijk is iedereen om. Medewerkers loggen in op hun beheerde device met Windows Hello for Business,
of via hun telefoon met een passkey in de Authenticator. Toegang verlies je alleen nog als je je device
kwijt bent of je toegangscode niet meer weet. Dat is een heel ander risicoprofiel.

### 9. Borging en doorontwikkeling

Na livegang begint het echte werk: eisen richting leveranciers (SSO verplicht, FIDO2 ondersteunen),
uitzonderingen afbouwen, gebruik en incidenten monitoren. Wat na de eigen organisatie overblijft, zijn de
leveranciers, en daar zit vaak het grootste gat. Hun incidenten eindigen vaak alsnog bij jou. Neem
passkey-eisen op in je programma van eisen en je architectuur; de
[Security Annex voor leveranciers](../security-annex-leveranciers/) in deze kennisbank doet precies dat
(artikel 14).

## Keuzes die het verschil maken

**Alleen je Microsoft-omgeving, of alles via SSO?** Idealiter werkt elke applicatie via SSO, maar dat lukt
niet altijd, omdat je organisatie er nog niet aan toe is of je leverancier niet. Twee risico's spelen:
phishing en de wildgroei aan losse inloggegevens. Vrijwel alle phishing richt zich op de
Microsoft-loginpagina; custom phishing op leveranciersportalen is in de praktijk zeldzaam. Door alleen al
op dat front passkeys af te dwingen, mitigeer je een hoog risico. De versnippering van logins blijft de
reden om leveranciers alsnog aan SSO te krijgen.

**Bootstrap en recovery: alleen TAP.** In een veelgebruikte publieke blueprint (het blog "You shall not
passkey" van een Microsoft-identity-specialist) mag ook wachtwoord plus Authenticator als registratieroute,
om bestaande gebruikers makkelijker te laten upgraden. Dat is handig tijdens de uitrol, maar laat na de
omzetting een achterdeur open. De strakke variant: registratie uitsluitend via TAP.

**FIDO2-instellingen: key restrictions aan.** Beperk welke apparaten en software passkeys mogen registreren
tot specifieke AAGUID's: de Authenticator-app en een aantal hardwaresleutels. De sleutel moet device-bound
zijn en het apparaat niet kunnen verlaten. Leveranciers vroegen om cloudopslag toe te staan (1Password en
dergelijke); daarmee creëer je een nieuw risico, omdat de sleutel dan deelbaar is en vanaf elk device
bruikbaar. Ook voor niet-geprivilegieerde accounts: niet syncable maken. Je identity is je goud; verklein
de blast radius.

**Fysieke sleutels of digitaal?** Een YubiKey voelt tastbaar en dus "extra veilig", maar de veiligheid zit
in de combinatie van factoren. Een device-bound passkey of Windows Hello for Business vraagt ook fysiek
bezit van het device én ontgrendeling met pincode of biometrie; een aanvaller moet jouw laptop of telefoon
stelen én erin komen. Losse fysieke sleutels verdwijnen in de praktijk juist in broekzakken en bureaulades.
Voor hoog-risico-accounts en beheerdersrollen kan een dedicated hardwaretoken passend zijn; voor de brede
organisatie levert een device-bound passkey op een beheerd device al een zeer hoog niveau, zonder de
adoptie te verliezen.

**Je IT-leverancier.** Ben je nog niet overgezet door je IT-leverancier, dan kan dat een veelzeggend signaal
zijn. IT-leveranciers hebben dit vaak nog niet voorhanden en maken het daardoor onnodig ingewikkeld en
duur.

## Wat er in de praktijk tegenzat

- **Printers en apps met een webview.** Een printer waarop je moet inloggen maar die geen bluetooth heeft,
  breekt de verificatieslag. Mobiele apps die via een brakke webview inloggen, ondersteunen de flow niet.
  Een webview die onderwater via Graph aanmeldt, kun je niet uitzonderen op applicatie-ID; dan blijft
  onderscheid op netwerk (een vaste uitgaande IP) over. Voor die gevallen: zeer specifieke Conditional
  Access-regels op systeem, persoon of groep, met strakke limitaties op netwerk of device. Legacy MFA
  bleef daar nodig, maar zo dichtgetimmerd dat het risico klein is.
- **Cloud-pc's zonder Windows Hello en devices zonder bluetooth.**
- **Weerstand is geen onwil.** Medewerkers vonden de overstap spannend en wilden persoonlijke hulp.
  Afdelingen verschilden in adoptiesnelheid. Wat werkte: managers vooraf informeren, korte video's,
  dagstarts langs, en hulptroepen op de vloer in de week van de omzetting.
- **Externe inhuur met een eigen laptop** logt in via de Authenticator op de telefoon; een passkey op de
  laptop van hun werkgever kan niet.
- **Windows Hello is niet hetzelfde als een passkey**, en dat moet je uitleggen: Windows Hello beveiligt het
  device, de passkey beveiligt je accounts. Wie alleen Windows Hello heeft, is veilig op de laptop, maar
  niet automatisch op de telefoon of een onbeheerd apparaat. De FAQ (vraag 25) heeft de uitleg.

## Wat het oplevert

Het lijkt een enorme technische exercitie, maar de kern is verrassend simpel: registratie mogelijk maken,
Conditional Access goed inrichten, gebruikers registreren, gefaseerd afdwingen, goed begeleiden. De praktijk
verschilt per organisatie en leveranciers, legacy en mobiele apps kunnen het weerbarstig maken. Maar zelfs
als je alleen je Microsoft 365-omgeving phishing-resistent maakt, haal je een van de grootste aanvalsroutes
van dit moment grotendeels onderuit. Perfect bestaat niet; accounts fundamenteel moeilijker overneembaar
maken is op dit moment een van de meest effectieve maatregelen die je kunt nemen.

BIO2-verankering: maatregel 5.17.01 (authenticatie-informatie) vraagt sterke, moderne
authenticatiemiddelen. Passkeys zijn daarvan op dit moment de veiligste en meest toekomstbestendige vorm.

## Bronnen

- [Passkeys registreren in de Microsoft Authenticator (Microsoft Learn)](https://learn.microsoft.com/nl-nl/entra/identity/authentication/how-to-register-passkey-authenticator)
- [Windows Hello configureren (Microsoft Support)](https://support.microsoft.com/nl-nl/windows/windows-hello-configureren-dae28983-8242-bb2a-d3d1-87c9d265a5f0)
- [FIDO2 AAGUID's van YubiKey-hardware (Yubico)](https://support.yubico.com/s/article/YubiKey-hardware-FIDO2-AAGUIDs)
- De blueprint "You shall not passkey" van een Microsoft-identity-specialist (publiek blog) is als vertrekpunt
  gebruikt, met de afwijkingen die hierboven staan.

## Licentie

[EUPL-1.2](../../LICENSE), vrij te hergebruiken en aan te passen. Feedback en verbeteringen welkom via een
[issue](https://github.com/security-commons-nl/kennisbank/issues/new/choose).
