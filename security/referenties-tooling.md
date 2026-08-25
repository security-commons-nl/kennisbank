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

**Verhouding tot SCOPTIX hieronder.** Beide komen via Meisam Eslahi (LinkedIn) en beide doen passieve
verkenning, maar ze zitten op een ander niveau. SCOPTIX is een zelf-hostbare webapplicatie met
asset-categorisatie en scan-vergelijking, gericht op doorlopend beheer van het aanvalsoppervlak. FinalRecon
is een losse CLI voor één doelwit op één moment: sneller in te zetten, geen state, geen historie. Voor CTEM
is SCOPTIX de logische keus; FinalRecon past bij een gerichte eenmalige verkenning of als tweede bron naast
een bestaande scan.

⚠️ **Twee dingen om te wegen.** Het gaat verder dan passief: directory- en file-enumeratie en een
poortscan raken het doelwit actief, dus dit hoort alleen ingezet te worden met aantoonbare autorisatie.
En de subdomein- en Wayback-bronnen zijn externe diensten, dus dezelfde soevereiniteitsweging geldt als
bij SCOPTIX.

Gevonden 10-08-2026 via een LinkedIn-post van Meisam Eslahi. De post verwees door via een verkorte
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
in plaats van puur lokaal te draaien. Via Meisam Eslahi (LinkedIn), gevonden 23-07-2026.

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
afweging, geen technische vanzelfsprekendheid. Via Meisam Eslahi (LinkedIn), "blue team energy only",
gevonden 10-08-2026.
