---
titel: De vijf aanvalspaden voor lokale overheid
vakgebied: security
type: referentie
normen: [BIO2]
peildatum: 2026-08
herkomst: bijlage bij "Risicoanalyse langs aanvalspaden"; gebaseerd op publieke incidentrapporten en adviezen van nationale en Europese CSIRT's
status: concept
samenvatting: Vijf generieke aanvalspaden die dekken wat er de afgelopen jaren bij gemeenten en waterschappen daadwerkelijk gebeurde. Per pad een halve pagina: hoe het loopt, de chokepoints, en de bewijsvragen voor de dekkingsmeting.
---

# De vijf aanvalspaden voor lokale overheid

Bijlage bij [Risicoanalyse langs aanvalspaden](README.md), stap 2. Vijf paden, elk in hetzelfde
formaat: **hoe het loopt** (vijf stappen, geen techniektabellen), **de chokepoints** (waar je het kunt
zien of stoppen), en **de bewijsvragen** voor de dekkingsmeting in stap 3. Neem de paden zoals ze zijn;
een pad schrappen omdat het "bij ons niet speelt" is de aanname die je wilt toetsen.

De paden zijn geordend op wat gemeenten en waterschappen nu het meest raakt. Ze overlappen bewust:
een echte aanval loopt vaak over twee of drie paden (binnen via 1 of 2, verder via 5). Dat is geen
dubbeltelling; het betekent dat één dicht chokepoint meerdere paden breekt.

---

## Pad 1. Gecompromitteerd account

**Kern.** De aanvaller logt gewoon in. Niet met een exploit, maar met de inloggegevens van een
medewerker, verkregen via phishing, een adversary-in-the-middle-pagina, een hergebruikt wachtwoord uit
een eerder lek, of door de gebruiker net zo lang MFA-verzoeken te sturen tot hij op "ja" drukt.

**Hoe het loopt.**
1. Een mail, een Teams-bericht of een QR-code leidt naar een inlogpagina die de echte nabootst.
2. De gebruiker logt in; de proxy ertussen vangt wachtwoord én de sessiecookie na de MFA-stap.
3. De aanvaller gebruikt de sessie: mailbox, SharePoint, Teams, alles wat het account mag.
4. Vanuit de mailbox: nieuwe phishing naar collega's en ketenpartners, met de geloofwaardigheid van
   een echte afzender; regels die antwoorden verbergen; facturen omleiden.
5. Bij een account met rechten: verder langs pad 5.

**Waarom het lukt.** MFA via pushnotificatie of een tweecijferige number match is niet bestand tegen
adversary-in-the-middle. Wachtwoorden worden hergebruikt. Sessies blijven lang geldig. En de
gecompromitteerde mailbox is de perfecte springplank naar de volgende organisatie.

**Chokepoints.**
- Phishing-resistente authenticatie (FIDO2, passkeys) voor iedereen die het aankan, en verplicht voor
  beheer- en gevoelige accounts.
- Conditional access: geen sessie vanaf een onbekend apparaat of een onmogelijke locatie.
- Detectie op inlogafwijkingen: nieuw land, nieuw apparaat, onmogelijke reis, nieuwe mailregels.
- Sessieduur en token-intrekking bij verdenking.

**Bewijsvragen (D/R/P).**
- D: hebben we een regel die een inlog vanaf een nieuw land of een nieuwe mailregel meldt, en is die de
  afgelopen zes maanden ooit afgegaan of getest?
- R: wat doen we bij een bevestigd gecompromitteerd account: wie trekt sessies in, wie kijkt in de
  mailbox, wie waarschuwt de ketenpartners die een mail kregen? Is dat één keer geoefend?
- P: export uit de identity provider: welk percentage van de beheeraccounts dwingt FIDO2 af? Welk
  percentage van alle accounts? Hoeveel accounts hebben nog sms of push als enige tweede factor?

---

## Pad 2. Werkplek via de gebruiker

**Kern.** De gebruiker voert zelf de code van de aanvaller uit. Een nepfoutmelding ("uw browser moet
geverifieerd worden") vraagt om een toetscombinatie en een plakactie in het Uitvoeren-venster;
daarmee start een PowerShell-commando dat de eigenlijke lading ophaalt. Bekend als ClickFix, met
varianten via valse CAPTCHA's, valse updates en valse Teams-vergaderingen.

**Hoe het loopt.**
1. Een gecompromitteerde of vervalste website, een advertentie of een mailbijlage toont de nepmelding.
2. De gebruiker volgt de instructie: Windows+R, Ctrl+V, Enter.
3. Het commando haalt een infostealer of remote-access-tool binnen, buiten de browser om.
4. Inloggegevens en sessiecookies van alles wat op de werkplek is opgeslagen gaan naar buiten.
5. Met die gegevens: pad 1 en pad 5.

**Waarom het lukt.** De gebruiker doet het zelf, dus de browserbeveiliging ziet geen download. De
werkplek staat toe dat een gebruiker willekeurige scripts start. En de melding ziet er precies uit
als de echte foutmeldingen die mensen dagelijks wegklikken.

**Chokepoints.**
- Werkplekhardening: geen lokale beheerrechten, PowerShell en scripting beperkt tot wie het nodig
  heeft, attack surface reduction-regels aan.
- Endpointdetectie die de keten "Uitvoeren-venster, PowerShell, download" ziet.
- DNS- en webfiltering, zodat de lading niet opgehaald kan worden.
- Bij de mens: niet "let op phishing", maar de concrete instructie: niets plakken in het
  Uitvoeren-venster, nooit, ook niet als de melding het vraagt.

**Bewijsvragen (D/R/P).**
- D: draait er een detectieregel op het gebruik van het Uitvoeren-venster gevolgd door PowerShell met
  een downloadcommando? Hoeveel keer ging die af, en was dat terecht?
- R: wat doen we als een werkplek een infostealer had: welke wachtwoorden en sessies worden
  ingetrokken, en hoe snel?
- P: hoeveel werkplekken hebben nog lokale beheerrechten voor de gebruiker? Staan de
  ASR-regels aan, en is dat te zien in een export?

Dit pad is volledig uitgewerkt, tot aan de query's, in
[Handelingsperspectief](https://security-commons-nl.github.io/Handelingsperspectief/).

---

## Pad 3. Kwetsbare internetgerichte dienst

**Kern.** Iets wat aan het internet hangt heeft een bekende kwetsbaarheid, en de patch is er wel
maar staat nog niet. VPN-concentrators, firewalls, mailgateways, portalen, een vergeten testserver.
De tijd tussen "kwetsbaarheid bekend" en "actief misbruikt" is teruggelopen van weken naar dagen,
soms uren.

**Hoe het loopt.**
1. Een kwetsbaarheid wordt gepubliceerd, vaak met werkende exploitcode.
2. Aanvallers scannen het hele internet; alles wat reageert, wordt binnen een dag geprobeerd.
3. De exploit geeft toegang tot het apparaat of de dienst, meestal met hoge rechten.
4. Vanaf daar: het interne netwerk, inloggegevens die op het apparaat staan, verder langs pad 5.
5. Vaak wordt de toegang pas weken later gebruikt, als de patch allang is gezet en niemand meer kijkt.

**Waarom het lukt.** Patchen buiten het change-venster is niet geregeld. Niemand weet precies wat er
allemaal aan het internet hangt. En een apparaat dat gepatcht is, is niet automatisch schoon.

**Chokepoints.**
- Weten wat er aan het internet hangt: een actueel overzicht van het externe aanvalsoppervlak.
- Kritieke patches op internetgerichte systemen binnen dagen, met een mandaat om buiten het
  change-venster te handelen.
- Beheerinterfaces nooit direct aan het internet.
- Na een kritieke kwetsbaarheid: niet alleen patchen maar ook controleren op sporen van misbruik.

**Bewijsvragen (D/R/P).**
- D: zien we een inlog op de beheerinterface van de firewall of VPN vanaf een onbekend adres? Zien we
  uitgaand verkeer van een apparaat dat normaal niets naar buiten stuurt?
- R: bij een spoedadvies van het nationale CSIRT: wie beslist over patchen buiten het venster, en
  binnen hoeveel uur is dat de laatste keer gebeurd?
- P: het overzicht van internetgerichte systemen met per systeem de laatste patchdatum, en het aantal
  kritieke kwetsbaarheden ouder dan een week.

---

## Pad 4. Leverancier en keten

**Kern.** De aanvaller komt niet bij jou binnen maar bij je leverancier, en gebruikt diens toegang,
account of omgeving als opstap. Een beheerder van de leverancier met een gecompromitteerd account, een
SaaS-dienst die jouw gegevens verwerkt, een ontwikkelstraat waar de code voor jouw applicatie vandaan
komt, een remote-beheerkoppeling die altijd aanstaat.

**Hoe het loopt.**
1. Bij de leverancier gebeurt pad 1, 2 of 3.
2. De aanvaller vindt de klantenlijst en de toegangen: VPN-accounts, beheerwachtwoorden, API-sleutels.
3. Met de toegang van de leverancier logt hij bij jou in, langs een route die vertrouwd is en zelden
   bekeken wordt.
4. Of: de aanvaller past de software of de dienst aan, en jij haalt de besmette versie zelf binnen.
5. Vaak meerdere klanten tegelijk; jij bent er een van.

**Waarom het lukt.** Leverancierstoegang is breed, permanent en vertrouwd. Wat de leverancier zelf
aan beveiliging doet, is contractueel zelden hard gemaakt en bijna nooit getoetst. En als de
leverancier een incident heeft, hoor je het te laat.

**Chokepoints.**
- Leverancierstoegang op maat: alleen wat nodig is, alleen wanneer nodig, phishing-resistent
  ingelogd, en gelogd.
- Contractuele eisen die op deze risico's slaan, met bewijs: phishing-resistente authenticatie bij de
  leverancier, gehardende werkplekken, pentest en kwetsbaarheidsbeheer van de applicatie en de
  ontwikkelstraat, en een meldplicht binnen uren.
- Weten welke leveranciers welke toegang hebben, en dat periodiek nalopen.

**Bewijsvragen (D/R/P).**
- D: zien we een leveranciersaccount dat inlogt buiten de afgesproken tijden of vanaf een nieuw adres?
- R: als een leverancier meldt dat hij gecompromitteerd is: welke toegangen zetten we binnen een uur
  uit, en weten we welke dat zijn?
- P: de lijst leveranciers met toegang, en per leverancier: dwingt de toegang phishing-resistente
  authenticatie af, en hebben we het bewijs (assurance, pentestrapport) van het afgelopen jaar?

De contractuele kant van dit pad is uitgewerkt in de
[Security Annex voor leveranciers](../security-annex-leveranciers/), die precies deze drie eisen
centraal stelt.

---

## Pad 5. Misbruik van beheerrechten

**Kern.** Dit is het pad na de voordeur. Eenmaal binnen met een gewoon account of op een gewone
werkplek zoekt de aanvaller de weg naar beheerrechten: opgeslagen wachtwoorden, service-accounts met
te veel rechten, beheerders die met hun beheeraccount ook mail lezen, een werkplek waar een
domeinbeheerder ooit is ingelogd. Met domeinbeheer is alles bereikbaar, en dan pas komt de ransomware.

**Hoe het loopt.**
1. Een voet binnen via pad 1, 2, 3 of 4.
2. Verkenning: welke accounts bestaan, wie is beheerder, waar staan de wachtwoorden.
3. Een tussenstap omhoog: een lokaal beheerderswachtwoord dat overal hetzelfde is, een
   service-account met domeinrechten, een kwetsbaarheid in een interne server.
4. Domeinbeheer: back-ups eerst vernietigen of versleutelen, daarna de rest.
5. Afpersing, vaak met gestolen gegevens als tweede drukmiddel.

**Waarom het lukt.** Beheerrechten zijn permanent en breed uitgedeeld. Beheer gebeurt vanaf dezelfde
werkplek als het gewone werk. Lokale beheerderswachtwoorden zijn gedeeld. En back-ups staan in
hetzelfde domein als wat ze moeten beschermen.

**Chokepoints.**
- Beheerrechten alleen tijdelijk en per taak (just-in-time), tenant-brede rollen tot een handvol
  beperkt, nooit dezelfde identiteit voor beheer en mail.
- Beheer alleen vanaf gehardende beheerwerkplekken, gescheiden van het gebruikersnetwerk.
- Lokale beheerderswachtwoorden uniek per apparaat (LAPS of gelijkwaardig).
- Back-ups die niet vanuit het domein te wijzigen of te verwijderen zijn, en een hersteltest die echt
  is gedaan.

**Bewijsvragen (D/R/P).**
- D: zien we het als een account voor het eerst een domeinbeheerder-groep aanraakt, als een
  service-account interactief inlogt, of als iemand de back-upserver benadert?
- R: hebben we ooit een volledige hersteltest gedaan vanaf een back-up die niet vanuit het domein
  bereikbaar was, en hoe lang duurde dat?
- P: hoeveel accounts hebben permanente domein- of tenantbeheerrechten? Hoeveel beheerders gebruiken
  een aparte beheeridentiteit? Staat LAPS op alle werkplekken en servers? Voor Linux-servers beantwoordt
  [iamscan](https://github.com/security-commons-nl/iamscan) de vraag "wie kan root worden" uit de
  configuratie.

---

## Wat hier bewust niet bij staat

**DDoS en hacktivisme.** Dat is geen pad naar binnen maar uitval van buitenaf, en het raakt vooral de
publieke website en online dienstverlening. Het hoort in je continuïteitsplan en bij je hostingpartij,
niet in deze matrix. Wil je het toch meenemen, dan als kolom 6 met alleen R en P: is er een wasstraat,
en is de omschakeling geoefend.

**Insider.** Een kwaadwillende medewerker loopt langs pad 5 zonder de voordeur nodig te hebben. De
chokepoints van pad 5 zijn precies de maatregelen die ook daar werken; een apart pad voegt niets toe.

## Bronnen

De paden zijn een samenvatting van wat publiek is over incidenten bij Nederlandse gemeenten en
waterschappen sinds 2023, en van de adviezen van het Nationaal Cyber Security Centrum, de
Informatiebeveiligingsdienst voor gemeenten en ENISA over dezelfde periode. Per pad zijn de technieken
terug te vinden in MITRE ATT&CK; die verwijzingen zijn hier bewust weggelaten, omdat de bewijsvragen
belangrijker zijn dan de techniekcodes.
