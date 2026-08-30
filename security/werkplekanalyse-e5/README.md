---
titel: Werkplekanalyse op het Microsoft-platform
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: gegeneraliseerd uit een casus bij een gemeentelijke organisatie
status: in gebruik
samenvatting: Meet met Defender for Endpoint en Advanced Hunting wat er op je werkplekken feitelijk draait, en beperk daarna pas. Met zes KQL-query's voor PowerShell, Win+R, mshta en ClickFix, een configuratiecheck die "aan" onderscheidt van "gekoppeld en actief", en het advies om PowerShell te beheersen met Constrained Language Mode in plaats van te blokkeren.
barrieres: [execution]
rol: fundering
pijler: meten-voordat-je-ingrijpt
---

# Werkplekanalyse op het Microsoft-platform

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/werkplekanalyse-e5](https://security-commons-nl.github.io/kennisbank/security/werkplekanalyse-e5/)

> **Barriere:** beperk software- en scriptuitvoering met application control en ASR. Deze handleiding
> laat zien hoe je eerst meet wat er draait, zodat je daarna kunt beperken zonder legitiem werk te breken.

Vrijwel elke gemeente heeft Microsoft 365 E5 en daarmee Defender for Endpoint (MDE) en Advanced Hunting.
Deze handleiding beschrijft welke analyses je daarmee doet, en hoe je "aan" onderscheidt van "gekoppeld
en actief".

De query's staan in [`data/`](data/). Pas de parent-processen en uitsluitingen aan op je eigen omgeving.

## Wanneer wel, wanneer niet

Altijd zinvol als je werkplekken via Intune beheerd zijn, zodat de telemetrie in het Defender-portaal
landt. Sta je nog onbeheerde BYOD toe zonder enige regelset (MAM en conditional access), dan is er echt
nog veel werk aan de winkel. Start dan zeker hier, maar besef dat je een groot blind gat hebt.

Deze handleiding hoort bij de methode [Meten voordat je ingrijpt](../meten-voordat-je-ingrijpt/): meet
eerst, grijp daarna pas in. Sla je het meten over en zet je alles in blokkeerstand, dan breek je werk dat
er wel toe doet en draai je de maatregel binnen een week weer terug.

## Zo richt je het in

### A. Configuratie verifieren (aan is niet gekoppeld en actief)

Loop deze punten langs. Het zijn veelvoorkomende blinde vlekken in endpoint-detectie.

- **ASR (Attack Surface Reduction).** Bestaan er regels, staan ze in **block**-modus, en zijn ze gekoppeld
  aan de **juiste gebruikersgroep**? Het komt voor dat er regels bestaan die aan geen of een verkeerde
  groep hangen en dus niets doen. Controleer specifiek of er een regel is tegen *credential stealing from
  LSASS*. De configuratiestatus is per device zichtbaar via
  `DeviceTvmSecureConfigurationAssessment` in het security-portaal.
- **AMSI.** Script scanning staat standaard aan, maar wordt vaak niet bewust ingericht of geverifieerd.
  Bevestig en leg vast.
- **LSA protection.** Vaak niet geconfigureerd. Zet aan en zorg dat misbruik een signaal oplevert.
- **Script-block-logging (EID 4104).** Vaak niet ingericht. Voeg toe als aanvullende bron naar de SIEM;
  MDE heeft bekende blinde vlekken die je hiermee afdekt.
- **Autorun en autoplay op endpoints.** Controleer de feitelijke stand, niet de aanname. Op servers is dit
  vaak uit via een hardening-baseline; op endpoints staat het regelmatig nog op default aan.

### B. PowerShell, meet voordat je beperkt

PowerShell wil je beheersen, niet bot blokkeren. De reden blijkt vaak uit de data.

1. Draai [`data/powershell-totaal-categorisatie.kql`](data/powershell-totaal-categorisatie.kql). Dit geeft
   de **exacte** verhouding automatisering tegenover interactief (server-side geaggregeerd, dus zonder
   exportlimiet). Verwacht beeld: het overgrote deel is automatisering, namelijk Intune en remediation,
   de eigen Defender-sensor en overige SYSTEM-processen. Interactief mensgebruik is doorgaans een fractie
   van een procent.
2. Draai [`data/powershell-interactief.kql`](data/powershell-interactief.kql) om de ruis weg te filteren
   en te zien wie interactief gebruikt. Vaak is dat een kleine groep ontwikkelaars met moderne tooling
   (terminals, editors, AI-assistenten) die op de achtergrond PowerShell aanroepen.

**Advies:** beheers PowerShell met **Constrained Language Mode (CLM), afgedwongen via WDAC**, in plaats
van een procesblokkade. CLM laat PowerShell draaien maar ontneemt scripts de bouwstenen (reflectie,
willekeurige code laden, directe API-aanroepen) die aanvalspayloads nodig hebben. Een trustmodel
(ondertekening plus WDAC) beslist automatisch of een script volledig of beperkt draait, in plaats van een
handmatige uitzonderingenlijst. Geef de ontwikkelaarsgroep een afgebakende, tijdelijke uitzondering.
Begin in **auditmodus**.

### C. Win+R, het uitvoeren-venster

Draai [`data/winr-runmru-top.kql`](data/winr-runmru-top.kql) en
[`data/winr-categorisatie.kql`](data/winr-categorisatie.kql). Deze lezen de RunMRU-registersleutel uit:
wat typen gebruikers werkelijk in Win+R.

Verwacht beeld: een laag volume, vrijwel uitsluitend beheer- en power-usergebruik (beheerconsoles,
netwerkshares, applicaties). Veel gebruikers zullen het niet leuk vinden, maar er breekt vaak niets als je
het uitzet, terwijl het wel een essentiele stap **voorkomt** die ClickFix nodig heeft om voet aan de grond
te krijgen.

**Advies:** schakel Win+R uit via beleid (NoRun, via Intune of GPO). Stem vooraf af met beheer of er
workflows zijn die op Win+R leunen, bijvoorbeeld het springen naar uitrol- of softwaremappen.

### D. mshta

Draai [`data/mshta-gebruik.kql`](data/mshta-gebruik.kql). mshta is een veelgebruikt ClickFix-kanaal en in
moderne kantooromgevingen zelden nog nodig. Vaak vind je nul of een handvol goedaardige events.

**Advies:** blokkeer mshta via AppLocker of WDAC (beide paden, 32- en 64-bits), met een detectieregel als
achtervang. De impact is doorgaans verwaarloosbaar.

### E. Detectie op ClickFix

Draai [`data/clickfix-detectie.kql`](data/clickfix-detectie.kql). Deze correleert een verdacht commando in
de Run-dialoog met een kort daarna gestart proces (PowerShell, mshta, cmd, curl) vanuit explorer.exe.

Let op de bewuste beperkingen: de detectie ziet alleen het Win+R-pad, alleen de genoemde binaries en
alleen een explorer-parent. Verbreed de binary-lijst (rundll32, regsvr32, wscript en cscript, certutil,
bitsadmin) en overweeg een lichtere variant die alleen op de verdachte RunMRU-waarde alarmeert, als
aanvulling.

### Interpretatiehulp

- **Filter automatisering weg voordat je conclusies trekt.** Intune- en remediation-scripts, de
  Defender-sensor en installers domineren het beeld. Zonder filtering lijkt er veel interactief gebruik
  dat er niet is.
- **Ontwikkeltooling veroorzaakt veel tellingen, weinig personen.** Een AI-assistent of editor die elke
  handeling met een korte PowerShell-controle valideert, telt zwaar maar betreft een handvol gebruikers.

## Wat het kost en wat het oplevert

De analyses zelf kosten alleen tijd: de query's draaien op telemetrie die je al hebt. De uitvoering kost
meer, vooral het WDAC-trustmodel; begin daarom in auditmodus en pak Win+R en mshta eerst, want die zijn
goedkoop en breken zelden iets.

Wat het oplevert is dat je maatregelen kunt verdedigen. Niet "wij blokkeren PowerShell", maar "van de
uitvoeringen is 99,4 procent automatisering, het interactieve deel komt van zes ontwikkelaars, en die
houden een afgebakende uitzondering". Dat is een gesprek dat je wint.

## Bewijs

Export of configuratie waaruit blijkt dat de maatregel technisch is afgedwongen, met de dekking en de
uitzonderingen erbij. Concreet:

- De ASR-regelstatus per device uit `DeviceTvmSecureConfigurationAssessment`, met het aantal devices in
  block-modus tegenover het totaal, en de gebruikersgroep waaraan de regels hangen.
- De WDAC- of AppLocker-configuratie met de uitzonderingen, en de auditbevindingen van voor de omzetting
  naar blokkeren.
- Het beleid dat Win+R uitschakelt en de blokkade van mshta, elk met de dekking.
- De uitkomst van de categorisatie-query's als onderbouwing waarom de uitzonderingen zijn wat ze zijn.

## Zo leg je het uit

**Aan de directie.** ClickFix en soortgelijke aanvallen beginnen bijna altijd met een gebruiker die zelf
een commando plakt of uitvoert. We meten eerst wat er echt gebeurt en sluiten daarna de routes die niemand
nodig heeft. Zo halen we een aanvalsroute weg zonder het werk te breken.

**Aan de informatiemanager.** De analyse draait op telemetrie die er al is; er komt geen nieuw product
bij. De ingrepen (Win+R uit, mshta blokkeren, PowerShell in Constrained Language Mode) raken een klein
aantal gebruikers, en die krijgen een afgebakende uitzondering.

**Aan het MT.** Een handvol ontwikkelaars merkt hier iets van en krijgt een uitzondering met een termijn.
Voor de rest van de organisatie verandert er niets zichtbaars.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `execution` uit de
[zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/), en is een uitwerking van de
methode [Meten voordat je ingrijpt](../meten-voordat-je-ingrijpt/). Wat je hiermee aantoont in BIO 2.0,
NIST CSF, het Wpg-kader en de AVG staat op
[Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

De ClickFix-killchain waar deze analyses op aansluiten, staat in de pijler onder *Killchain en
chokepoints*.

## Licentie

[EUPL-1.2](../../LICENSE).
