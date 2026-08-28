# Externe referenties: security-tooling & kennisbanken

Verwijzingen naar open resources met een specifiek, afgebakend doel. Geen eigen werk van
security-commons-nl; wel de moeite waard voor publieke-sector-teams.

## LOLCreds · lolcreds.haxx.it

Credential-kennisbank voor defenders en geautoriseerd security-testen, analoog aan LOLBAS en
GTFOBins. Kernobservatie: aanvallers loggen vaak gewoon in via achtergebleven credentials
(API-keys, service-accounts, default-wachtwoorden, secrets in config of code) in plaats van
exploits te gebruiken. Bevat checklists voor zowel red- als blue-team. Bruikbaar bij
credential-exposure-analyses en continuous threat exposure management (CTEM).

## Threat Tiger · github.com/jozeta/threat-tiger

Offline-first threat-modeling tool (STRIDE) in één HTML-bestand: drag-and-drop
architectuurdiagrammen plus documentatie van risico's, zonder externe diensten of database.
MIT-licentie. Laagdrempelig alternatief voor zwaardere threat-modeling-suites; sluit aan op de
commons-principes (open source, geen cloud-afhankelijkheid, auditbaar).

## FinalRecon · web-reconnaissance in één CLI

Open-source Python-CLI die losse recon-stappen bundelt achter één target-URL: HTTP- en security-headers,
WHOIS met domeinverloopdatum, SSL-certificaatinformatie, ruim veertig DNS-recordtypes, subdomeinen uit
vijftien bronnen, interne en externe links, JavaScript, images, `robots.txt` en sitemaps, directory- en
file-enumeratie, de top duizend poorten, en URL's uit de Wayback Machine. De poster claimt dat het tot
50.000 historische URL's ophaalt en die triageert op wat de moeite van het bekijken waard is.

**Verhouding tot SCOPTIX hieronder.** Beide komen via dezelfde LinkedIn-bron en beide doen passieve
verkenning, maar ze zitten op een ander niveau. SCOPTIX is een zelf-hostbare webapplicatie met
asset-categorisatie en scan-vergelijking, gericht op doorlopend beheer van het aanvalsoppervlak. FinalRecon
is een losse CLI voor één doelwit op één moment: sneller in te zetten, geen state, geen historie. Voor CTEM
is SCOPTIX de logische keus; FinalRecon past bij een gerichte eenmalige verkenning of als tweede bron naast
een bestaande scan.

⚠️ **Twee dingen om te wegen.** Het gaat verder dan passief: directory- en file-enumeratie en een
poortscan raken het doelwit actief, dus dit hoort alleen ingezet te worden met aantoonbare autorisatie.
En de subdomein- en Wayback-bronnen zijn externe diensten, dus dezelfde soevereiniteitsweging geldt als
bij SCOPTIX.

Gevonden 10-08-2026 via LinkedIn. De post verwees door via een verkorte
`lnkd.in`-link die niet is geresolved, dus **de repo-URL is nog niet geverifieerd**; controleer die vóór
gebruik.

## SCOPTIX · github.com/Omnitarium/scoptix

Passieve-reconnaissance- en exposure-discovery-tool (Apache-2.0, TypeScript/Next.js, zelf-hostbaar via
Docker Compose). Brengt de internet-facing footprint in kaart uit publieke bronnen: subdomeinen, URL's,
gearchiveerde web-assets en mogelijke informatie-exposures, met asset-categorisatie, endpoint-discovery
en scan-vergelijking. Nuttig als startpunt voor attack surface management / continuous threat exposure
management (CTEM) en als input voor verdere handmatige of AI-ondersteunde assessments. Identificeert
alleen; valideert of exploiteert niets. **Let op de soevereiniteitsweging:** leunt op externe API's
(VirusTotal-key vereist, freemium/gerate-limit; Wayback Machine; optioneel Wappalyzer + NVD/CVE-correlatie)
in plaats van puur lokaal te draaien. Via LinkedIn, gevonden 23-07-2026.

## darknetlist · darknetlist.is

Gratis directory van Tor-bereikbare diensten, die elke 30 minuten de live status van elke vermelde
site controleert. Lost een praktisch probleem op bij dark-web-monitoring: het vinden van bronnen is
niet het lastige deel, het bíjhouden wel. Hidden services verdwijnen zonder aankondiging,
onion-adressen wijzigen, mirrors komen en gaan en sites zijn tijdelijk offline, waardoor een
handmatige bronnenlijst binnen weken veroudert. Bruikbaar als **bron-inventaris** bij het in kaart
brengen van wat er over een organisatie buiten de eigen logs en securitytools rondzwerft
(domeinen, e-mailadressen, gelekte credentials), als vroege indicator vóórdat losse stukjes een
incident worden. Aanvulling op de EASM-lijn in `cisochat/docs/vciso/research/identify.md` §6:
SCOPTIX en OWASP Amass brengen het eigen aanvalsoppervlak in kaart, dit dekt de kant van het
publieke internet die niet geïndexeerd is.

**Wegingen vóór gebruik.** De site is een directory, geen scanner: hij vertelt wát bereikbaar is,
niet wat er over jóu staat. Bronvermelding, licentie en exploitant zijn niet gedocumenteerd, dus
geldt hier dezelfde peildatum-eis als bij tooldirectory's in het algemeen: **een directory is een
vindkanaal, nooit een bron.** Tor-verkeer vanaf een gemeentelijk netwerk is bovendien een eigen
afweging, geen technische vanzelfsprekendheid. Via LinkedIn, "blue team energy only",
gevonden 10-08-2026.

## ScanZeker · scanzeker.nl

Gratis Nederlandse externe-exposure-scanner van Secure Audit (IT-audit- en compliancebureau,
Eindhoven). Je voert een domein of IP in en krijgt binnen ongeveer een minuut een rapport over
twaalf modules, zonder account: SSL/TLS-configuratie (via Qualys SSL Labs), security-headers (direct,
via echte browser en via Mozilla Observatory), e-mailbeveiliging (SPF, DKIM, DMARC, MTA-STS, TLS-RPT),
server-exposure (open poorten via Shodan, verrijkt met CVE's uit de NVD), datalekken (Have I Been
Pwned en HudsonRock Cavalier), subdomeinen en takeover-risico (Certificate Transparency, Certspotter,
AlienVault OTX), DNS (DNSSEC, CAA, RPKI), certificaathistorie, technologie-stack, cookies vóór consent,
WHOIS/RDAP en reputatie (Google Safe Browsing, Spamhaus, SURBL, URIBL, SpamCop e.a.). Bevindingen
worden gecombineerd tot mogelijke aanvalspaden (account takeover, phishing, server-exploitatie), met
de eigen kanttekening dat dit "scenario's op basis van observeerbare signalen" zijn, "geen bevestigde
kwetsbaarheden".

Twee lagen die het onderscheiden van de losse scanners hierboven. De **Risicokaart** zet dezelfde
scan om in een interactieve kaart: subdomeinen als knooppunten ingedeeld naar functie (mail, beheer,
api, externe platformen), per host de poorten, technologie en TLS-stand, en de belangrijkste
risicopaden als keten eronder. Het **Compliance-overzicht** projecteert de scan op de controls van
ISO 27001, NEN 7510, NIS2/Cbw, AVG en DigiD en laat per norm zien welke controls een passieve scan
kan raken en waar bevindingen zitten. De site is er zelf helder over: "indicatief", "geen bewijs
van (non-)conformiteit", en governance- en procesmaatregelen blijven buiten beeld.

**Waarom het hier staat.** Voor gemeenten en hun ketenpartners is dit een snel nulpunt naast de
bekende internet.nl-test: die dekt standaarden (IPv6, DNSSEC, TLS, mailauthenticatie), ScanZeker legt
er exposure, datalekken en aanvalspaden naast en spreekt de taal van de normen waar de CISO op wordt
aangesproken. Bruikbaar als eerste blik op een leverancier vóór een gesprek, als check na een wijziging
in DNS of mailrouting, en als laagdrempelige manier om een bestuurder of collega te laten zíen wat er
van buiten zichtbaar is. Verhouding tot SCOPTIX en FinalRecon: die zijn zelf te hosten of te draaien en
geven meer controle en historie; ScanZeker is een dienst zonder installatie, met de normprojectie als
onderscheidende laag.

⚠️ **Wegingen vóór gebruik.** (1) Het is een SaaS van een commerciële partij, geen open source; de
gratis scan is de etalage van hun auditdiensten en het "maandrapport" is een betaald vervolg.
(2) Grotendeels passief, maar niet volledig: de methodologie beschrijft een lichte actieve
TCP-handshake op poorten die Shodan al rapporteert (maximaal twintig) en een headless browser als een
WAF de gewone request blokkeert. Scan dus alleen domeinen waarvoor je verantwoordelijk bent of
toestemming hebt; de site zelf stelt daar geen voorwaarden aan. (3) Soevereiniteitsweging als bij
SCOPTIX: de scan leunt op een reeks externe API's (Shodan, HIBP, SSL Labs, OTX, Safe Browsing), je
domeinnaam gaat dus langs die partijen. De privacybelofte is expliciet: geen registratie, geen cookies,
geen opslag van resultaten, alleen geanonimiseerde statistiek over welke domeinen worden gescand.
(4) Bevindingen op gedeelde infrastructuur (IP met meer dan tien domeinen) zijn volgens de
methodologie minder betrouwbaar; lees de exposure-module dan met die bril.

Methodologie en bronnenlijst staan open op `scanzeker.nl/methodologie`. Opgenomen 28-08-2026.
