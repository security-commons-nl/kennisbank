---
titel: Meten voordat je ingrijpt
vakgebied: security
type: aanpak
normen: [BIO2]
versie: 2026-08
herkomst: gegeneraliseerd uit een casus bij een gemeentelijke organisatie
status: in gebruik
samenvatting: Verhoog je security posture met data uit je eigen omgeving in plaats van met aannames. Meet eerst wat er feitelijk draait (PowerShell, Win+R, mshta, firewallregels) en bepaal daarna pas wat je afdwingt; dat voorkomt dat je legitiem werk breekt en laat de echte impact zien. ClickFix is de casus, de aanpak werkt breder: van werkplek en identiteit tot netwerk, regie en strategie. Met herbruikbare KQL-query's voor Advanced Hunting.
---

# Meten voordat je ingrijpt

> **Lees dit stuk online:** [security-commons-nl.github.io/kennisbank/security/meten-voordat-je-ingrijpt](https://security-commons-nl.github.io/kennisbank/security/meten-voordat-je-ingrijpt/)

**De aanval waar dit mee begon.** Bij ClickFix laat een nagemaakte pagina de gebruiker zelf een commando
plakken en uitvoeren, meestal via Win+R of PowerShell. Geen exploit, geen bijlage: de gebruiker doet het
werk. Wat daarna komt is een infostealer of remote access tool, en uiteindelijk exfiltratie.

De verleiding is dan om meteen te blokkeren: Win+R uit, PowerShell dicht. Dat is precies waar dit stuk
tegen waarschuwt. Bij een gemeentelijke organisatie bleek van miljoenen PowerShell-starts in een maand
bijna 99 procent machine-automatisering, waaronder de sensor van de eigen endpointbescherming. Een botte
blokkade had de eigen beveiliging gebroken.

Vandaar de aanpak: meet eerst wat er feitelijk draait, bepaal dan wat je afdwingt. ClickFix is het
vertrekpunt, maar de werkwijze is breder toepasbaar: van de werkplek tot het netwerk, en van detectie tot
de vraag wat er in je omgeving feitelijk gebeurt.

Dit stuk is deels bestuurlijk (regie, strategie, besluitvorming) en deels technisch (analyses op het
Microsoft-platform, configuratie-analyse van firewalls en core-routers, herbruikbare query's). Lees de
managementsamenvatting als je het eerste wilt, en de hoofdstukken erna als je het tweede doet.

> Gegeneraliseerd uit een concrete casus. Pas de voorbeelden aan op je eigen organisatie, leveranciers en
> tenant. Let bij maatregelen die verkeer of gebruik inzichtelijk maken (zoals TLS-decryptie of
> script-logging) op privacy, BIO2 en eventuele medezeggenschapstrajecten.

## Wat je hier vindt

| Onderdeel | Voor wie | Waarover |
|---|---|---|
| [Managementsamenvatting](#managementsamenvatting) | Bestuur, CISO | Kernboodschap, lagenmodel, strategie in het kort |
| [De methode](#de-methode-evidence-based-posture-verhogen) | Allen | De werkwijze: IST naar SOLL, meten, aantoonbaarheid |
| [Werkplekanalyse](../werkplekanalyse-e5/) | Security, beheer | Eigen handleiding: analyses op het Microsoft-platform met KQL |
| [Identiteit en e-mail](../identiteit-en-mail-meten/) | Security, beheer | Eigen handleiding: MDO, MDI, Conditional Access, PIM, app-consent |
| [Netwerk en firewall](#netwerk-firewall-en-core-routers-analyseren-uit-data) | Security, netwerk | Firewalls en core-routers analyseren uit data |
| [Killchain en chokepoints](#killchain-en-chokepoints-clickfix) | Security | De ClickFix-keten naast je controls, met MITRE-fasen |
| [Regie en accountability](#regie-en-accountability) | Management, CISO | Resultaatverplichting, RACI, leveranciers |
| [Veilig faciliteren](#veilig-faciliteren-als-langetermijnstrategie) | Bestuur, CISO | Langetermijnstrategie in plaats van lockdown |
| [Zes KQL-query's](../werkplekanalyse-e5/data/) | Beheer, security | Verhuisd naar de handleiding Werkplekanalyse |

## Drie uitgangspunten

1. **Meet voordat je ingrijpt.** Stel het feitelijke gebruik vast voordat je iets beperkt. Dat voorkomt
   uitval en laat zien hoe groot de impact werkelijk is, meestal kleiner dan gedacht.
2. **Vertrouw op data, niet op tekeningen.** Een netwerktekening of een "we hebben het aanstaan" is een
   aanname. Toets de werkelijkheid: rule-hits, configuratie-export, telemetrie.
3. **Aangezet is niet hetzelfde als beheerd.** Een tool met standaardconfiguratie die niemand bijhoudt,
   beschermt niet aantoonbaar. Leg bestaan, opzet, werking en eigenaarschap vast.

## Volgorde van aanpak

1. Meet de werkplek: wat draait er echt, wie gebruikt wat.
2. Toets de configuratie op het Microsoft-platform: aan staan is niet hetzelfde als gekoppeld en actief.
3. Analyseer netwerk en firewall uit data: brede regels, beheertoegang, zicht, segmentatie.
4. Leg de killchain naast je controls: waar knijp je, waar zit een gat.
5. Beleg regie en resultaatverplichting, en kies een strategie.

## Managementsamenvatting

### Waarom dit onderwerp

ClickFix is een social-engineering-aanval waarbij de gebruiker zélf - misleid via een nep-melding of
nep-CAPTCHA - een geplakt commando uitvoert, vrijwel altijd via de Windows Run-dialoog (Win+R) en
PowerShell. Dat leidt tot tot een nieuwe ransomware, vaak een infostealers, remote-access-tools en in het 
ergste geval ransomware en datalekken.

Een publiek voorbeeld is de aanval op een Nederlandse gemeente in maart 2026, waarbij na een ClickFix-uitvoering
binnen twee dagen honderdduizenden bestanden werden weggesluisd / geëxfiltreerd.

Het punt is breder dan ClickFix: de werkplek is de primaire ingang, maar één maatregel houdt een aanvaller
niet tegen. De lagen sámen wel.

### Het lagenmodel (defense-in-depth)

Gebruik dit als kapstok. Elke laag vangt op wat de vorige doorlaat.

1. **Werkplek & e-mail** - waar de aanval binnenkomt.
2. **Identiteit & toegang** - wie mag wat.
3. **Netwerk** - beweging tussen werkplek en datacenter.
4. **Servers & applicaties** - het hart van de systemen.
5. **Data & detectie** - back-up, herstel en meekijken.

### De terugkerende bevinding

In de praktijk is het probleem zelden dat de middelen ontbreken. Vrijwel elke gemeente heeft Microsoft 365 E5,
endpointbescherming, firewalls en een of meer beheerpartners. Het gat zit in **inrichting, afdwinging en
eigenaarschap**:

- een beveiligingsregel die wel bestaat maar niet aan de juiste groep is gekoppeld (en dus niet werkt);
- een tool met standaardconfiguratie die niemand bijhoudt;
- een netwerktekening die niet overeenkomt met het verkeer dat de firewall daadwerkelijk ziet.
- een IT-Gap in de IT-afdeling zelf omdat "ze van het management luisteren" of "ze van de techniek neit begrijpen
  compromissen erbij horen"

De boodschap voor besluitvorming: **eerst afmaken en aantoonbaar maken wat er al is, daarna uitbreiden.**

### Strategische keuze: reguleren (lockdown) of veilig faciliteren

Er zijn grofweg twee richtingen. Reguleren (lockdown: het apparaat zoveel mogelijk beheersen/beperken) en veilig faciliteren
(de bescherming in het platform leggen en de grens verschuiven van het apparaat naar data en identiteit).

Voor een politiek-ambtelijke organisatie is veilig faciliteren vaak duurzamer, omdat het minder leunt op
"nee" en daardoor minder uitzonderingen en schaduw-IT uitlokt. Tegen ClickFix is het, mits goed ingericht,
ook gerichter - **een laptop in lockdown stopt ClickFix niet**, omdat de aanval in gebruikerscontext draait.

De eerlijke voorwaarde: veilig faciliteren is operationeel **zwaarder**, niet lichter. Het ruilt eenmalige
restrictie in voor continu beheer. Het is alleen duurzaam als de eigen capaciteit of regiecapaciteit (bij uitbestede ICT)
er werkelijk is. Ontbreekt die, dan verdient een striktere aanpak een serieuze afweging.
Zie [veilig faciliteren](#veilig-faciliteren-als-langetermijnstrategie).

### Regie en resultaatverplichting

De analyse moet landen in eigenaarschap. Beleg per onderwerp wie binnen de organisatie de regie voert en
accountable is voor het resultaat. Werk met een **resultaatverplichting**, geen inspanningsverplichting:
een onderwerp is pas klaar als de maatregel aantoonbaar werkt. Zie
[regie en accountability](#regie-en-accountability).

## De methode: evidence-based posture verhogen

Deze aanpak is opzettelijk nuchter. Geen catchy oneliners, wel toetsbare stappen.

### Drie principes

#### 1. Meet voordat je ingrijpt
Voordat je een maatregel afdwingt (Win+R uit, PowerShell beperken, een firewallregel versmallen), stel je het
feitelijke gebruik vast. Dat doet twee dingen: het laat de werkelijke impact zien (meestal kleiner dan gevreesd)
en het voorkomt dat je legitiem werk of beheer breekt. Een voorbeeld uit de praktijk: van miljoenen
PowerShell-starts in een maand bleek bij een gemeente bijna 99% machine-automatisering - waaronder de eigen sensor 
van de endpointbescherming. Een botte blokkade had de eigen beveiliging gebroken.

#### 2. Vertrouw op data, niet op tekeningen
Een netwerktekening toont de bedoeling, niet de werkelijkheid. "We hebben ASR aanstaan" is een aanname totdat
je de koppeling aan een gebruikersgroep hebt geverifieerd. Toets met:
- telemetrie (Advanced Hunting, logs);
- configuratie-export (firewallregels, hit-counts, routeringstabellen);
- de daadwerkelijke koppeling/scope van een beleidsregel.

#### 3. Aangezet is niet hetzelfde als beheerd
Toets elke maatregel op vier niveaus van oplopende zekerheid:

| Niveau | Vraag |
|---|---|
| **Bestaan** | Is de maatregel aanwezig? |
| **Opzet** | Is hij correct ingericht volgens norm? |
| **Werking** | Is hij aantoonbaar effectief in de praktijk? |
| **Config beschikbaar** | Kunnen wíj de instelling zelf inzien? |

### Managed dienstverlening is meer dan de aanknop indrukken
Een "managed" dienst omvat gedurende de hele levenscyclus: bijhouden (updates, dreigingsinfo), beheren
(configuratie, afwijkingen, prestaties), optimaliseren, functionaliteit aanpassen, en verantwoorden
(rapportage, eigenaarschap). Een tool installeren met standaardinstellingen is daarvan alleen de eerste stap.
Als de dienstverlening managed is gecontracteerd dan is de optielijst klein, een fireall waar de regelset
niet periodiek wordt gevalideerd en voorzien wordt van een risicoletter aan de klant waar nodig is **geen managed** 
dienst.

### IST → SOLL als werkvorm

Beschrijf per component de huidige stand (IST) en de gewenste stand (SOLL), met een statuskleur en een
actiehouder. Houd de SOLL-ambitie expliciet: een verdedigbare ondergrens (richting BIO2 en audit) is iets
anders dan "best-practice". Maak die keuze bewust, anders overvraag je de organisatie.

Sjabloon:

| Component | IST (stand + bewijs) | SOLL | Statuskleur | Actiehouder |
|---|---|---|---|---|
| _bijv. ASR-regels_ | _2 regels, niet gekoppeld_ | _block-modus, juiste groep, incl. LSASS_ | rood | _beheerpartner werkplek_ |

Statuskleuren: groen = ingericht · oranje = deels/aandacht · rood = nog niet ingericht · grijs = te bevestigen.

### Volgorde

1. **[Meet de werkplek](#werkplekanalyse-op-het-microsoft-platform-e5).** Daar is de meeste telemetrie en de meeste laaghangende winst.
2. **Toets de configuratie** op [de werkplek](#werkplekanalyse-op-het-microsoft-platform-e5) en bij [identiteit en e-mail](#identiteit-en-e-mail). Onderscheid "aan" van "gekoppeld en actief".
3. **[Analyseer netwerk en firewall uit data](#netwerk-firewall-en-core-routers-analyseren-uit-data).** Brede regels, beheertoegang, zicht op verkeer, segmentatie.
4. **[Leg de killchain naast je controls](#killchain-en-chokepoints-clickfix).** Waar knijp je de aanval, waar zit nog een gat.
5. **[Beleg regie](#regie-en-accountability)** en **[kies een strategie](#veilig-faciliteren-als-langetermijnstrategie)**.

### Aantoonbaarheid en herijking

Leg vast wat je hebt gemeten en wanneer. Een maatregel die ooit aanstond kan weer afvallen (drift). Plan
periodieke herijking en, waar mogelijk, een gecontroleerde aanvalssimulatie om detectie en preventie te
toetsen - niet aannemen dat het werkt, maar het laten zien.

## Werkplekanalyse op het Microsoft-platform

Deze analyses zijn een eigen handleiding geworden:
**[Werkplekanalyse op het Microsoft-platform](../werkplekanalyse-e5/)**. Daar staat hoe je met Defender
for Endpoint en Advanced Hunting meet wat er feitelijk draait (PowerShell, Win+R, mshta, ClickFix), hoe je
"aan" onderscheidt van "gekoppeld en actief", en waarom je PowerShell beter beheerst met Constrained
Language Mode dan met een procesblokkade. De zes KQL-query's staan daar in `data/`.

## Identiteit en e-mail

Ook deze laag is een eigen handleiding geworden:
**[Identiteit en e-mail meten voordat je afdwingt](../identiteit-en-mail-meten/)**. Daar staat wat je
toetst in Defender for Office, Entra ID, Conditional Access, app-consent en ADCS, met per punt wat "goed"
eruitziet. In veel gemeenten komt het merendeel van de incidenten via deze twee lagen binnen, niet via de
werkplek-uitvoering zelf; het is daarmee doorgaans de hoogste hefboom.

## Netwerk, firewall en core-routers analyseren uit data

Ook deze laag is een eigen handleiding geworden:
**[Netwerk en firewall analyseren uit data](../netwerkanalyse-uit-data/)**. Daar staat wat je exporteert
en analyseert (hit-counts, routeringstabellen, beheertoegang, zicht op versleuteld verkeer) en hoe je
brede regels veilig versmalt met schaduwregels in plaats van ze blind dicht te zetten.

## Killchain en chokepoints (ClickFix)

Leg je controls naast de aanvalsketen. Per fase is er een chokepoint: een plek waar je de aanval kunt
knijpen of zichtbaar maken. Niet elke fase hoeft preventief afgedekt; detectie + herstel kan volstaan voor de
restrisico's. Maak bewust zichtbaar wat je (nog) niet afdekt.

De keten hieronder volgt ClickFix → infostealer/RAT → exfiltratie, met MITRE ATT&CK-fasen. Per fase: het
chokepoint, en of het om preventie of detectie gaat.

| Fase (MITRE) | Voorbeeld | Chokepoint | Preventie / detectie |
|---|---|---|---|
| Initial Access | ClickFix via e-mail/website | Webproxy/SWG (URL-filter, Mark-of-the-Web), e-mailfilter | Preventie |
| Execution | `powershell -enc`, `mshta` via Win+R | EDR · AMSI · script-block-logging · PowerShell CLM · Win+R uit | Beide |
| Persistence (endpoint) | Run-key, scheduled task, startup-folder | EDR/autoruns · Sysmon (EID 13) | Detectie |
| Persistence (M365) | OAuth-consent, mailbox-forwarding | App-consent beperken · MDCA · Entra audit | Beide |
| Privilege Escalation | UAC-bypass (fodhelper/sdclt), loaders | EDR · LSA protection · ASR LSASS-regel | Preventie |
| Defense Evasion | Obfuscatie, LOLBins (regsvr32, msbuild, mshta) | ASR-regels · EDR LOLBin-detectie | Beide |
| Credential Access | Browser-SQLite, DPAPI, LSASS | ASR LSASS · browser-hardening · beheerde password manager | Beide |
| Discovery (AD) | `net group /domain`, BloodHound-collectie | Defender for Identity (AD-recon-detectie) | Detectie |
| Lateral Movement | SMB/WMI/RDP met gestolen creds, cookie-replay | Segmentatie · LAPS · Conditional Access (token binding) · SIEM | Beide |
| Collection | Browser-profielen, fileshare-mount | Audit-logging op shares (EID 4663) · DLP/UEBA | Detectie |
| Exfiltration | HTTPS POST naar C2, WebDAV-variant | Firewall-egress · TLS-inspectie · ASR 'block WebDAV' | Beide |
| Command & Control | Dead-drop resolvers, HTTPS C2 | DNS-filter · domain-reputation in SIEM | Detectie |
| Impact | Datadiefstal + leaksite | Immutable back-up · geteste restore (incl. DC) · IR-runbook · crisisplan | Herstel |

### Preventie versus detectie

- **Preventie** stopt de stap (ASR, CLM, segmentatie, egress-block).
- **Detectie** ziet de stap en maakt opvolging mogelijk (SIEM-regels, EDR, MDI, DNS-reputatie).
- **Herstel** vangt op wat doorkomt (back-up/restore, runbook).

Een gezonde posture heeft op het kritieke pad **meerdere** chokepoints, zodat het uitvallen van één laag niet
meteen de hele keten opent.

### Restrisico's die je bewust accepteert

Niet alles is realistisch af te dekken. Maak deze expliciet in plaats van ze te verzwijgen:

- **Geavanceerde C2/exfiltratie via DNS** is lastig volledig te blokkeren; leun hier op detectie en reputatie.
- **Oost-west-verkeer binnen het datacenter** valt vaak buiten de scope van een NDR rond de campus/access-laag.
  Beleg expliciet wie dit afdekt.

### Impact-anker

Het scenario dat je wilt voorkomen is publiek geïllustreerd door de aanval op een Nederlandse gemeente in
maart 2026: na een ClickFix-uitvoering werden binnen twee dagen honderdduizenden bestanden geëxfiltreerd. Eén
geslaagde keten kan dus een groot incident worden - de business case voor deze maatregelen is risicogebaseerd,
niet gebaseerd op het aantal incidenten.

### Bronnen (publiek)

- MITRE ATT&CK: T1204.004 (Malicious Copy and Paste), T1059.001 (PowerShell), T1219 (Remote Access Software),
  T1566.002 (Spearphishing Link).
- Publieke threat-intelligence over ClickFix en infostealers (o.a. Microsoft Threat Intelligence).
- Publieke berichtgeving over de gemeentelijke ClickFix-casus (maart 2026).

> **Verhouding tot de zelfcheck aanvalspaden.** De tabel hierboven volgt de volledige keten van een
> aanval, met alle MITRE-fasen. De [zelfcheck](https://security-commons-nl.github.io/aanvalspaden/) toetst
> per pad een handvol barrieres; ClickFix is daar AP09, met application control en ASR, browserhardening,
> lokale administratorrechten en EDR als chokepoints. Deze tabel is dus de uitgewerkte keten, de zelfcheck
> de snelle toets. Wijzigt de bron `paden.json`, dan volgt de zelfcheck; deze tabel is een eigen,
> gedetailleerdere snit en wordt met de hand onderhouden.

## Regie en accountability

De analyse heeft pas waarde als ze landt in eigenaarschap. Dit hoofdstuk beschrijft hoe je de regie belegt en
hoe je leveranciers stuurt op resultaat.

### Resultaatverplichting, geen inspanningsverplichting

Het uitgangspunt: een onderwerp is pas afgerond als de maatregel **aantoonbaar werkt** - niet als de
leverancier "ermee bezig is geweest". Dat verandert hoe je opdrachten formuleert en afsluit.

#### De regie-discipline (geldt voor elk onderwerp)

1. **Definition of Done vooraf.** De leverancier levert per change een meetbaar eindresultaat. De regievoerder
   accepteert die DoD voordat de change start.
2. **Resultaat controleren, niet aannemen.** "Klaar" volgens de leverancier is niet hetzelfde als aantoonbaar
   werkend. De regievoerder verifieert zelf, met bewijs (telemetrie, config-export, een test).
3. **Post-change check.** Na het doorvoeren: werkt de maatregel én is er niets gebroken? Leg het bewijs vast.
4. **Aantoonbaarheid en herijking.** Bestaan, opzet, werking en config-beschikbaarheid vastgelegd, en periodiek
   herijkt - een maatregel die ooit aanstond kan weer afvallen.

### Regie beleggen (voorbeeldindeling)

Beleg de regie intern; de uitvoering ligt steeds vaker bij beheerpartners. Intern beheer van deze componenten zorg
voor een goede 3e lijns functie!

Een werkbare indeling:

| Onderwerp | Interne regie (accountable) | Uitvoering (voorbeeld) |
|---|---|---|
| Werkplek en e-mail (MDO) | Servicemanagement + technisch applicatiebeheer (M365-beheer) | Beheerpartner werkplek |
| Identiteit en toegang | Security + M365-beheer | Beheerpartner |
| Netwerk en firewall | Security + architectuur | Beheerpartner netwerk |
| Servers en hardening | Security + architectuur | Beheerpartner datacenter |
| SOC/SIEM en detectie | Security | SOC-partner |
| Recovery en back-up | Security + architectuur | Beheerpartner datacenter |

Pas dit aan op je eigen organisatie. Markeer wat nog niet formeel belegd is expliciet als voorstel, en laat het
bevestigen door de CISO/het MT - dat maakt de accountability sluitend.

### RACI- en resultaat-sjabloon

| Onderwerp | Regie (accountable) | Uitvoering | Resultaatverplichting (concreet) |
|---|---|---|---|
| _bijv. werkplek_ | _M365-beheer_ | _beheerpartner_ | _ASR actief op alle endpoints, CLM in productie met dev-uitzondering, aantoonbaar_ |

Formuleer de resultaatverplichting altijd als een toetsbare eindtoestand, niet als een activiteit.

### Leveranciers en de naad ertussen

In veel gemeenten is security verdeeld over meerdere partijen: bijvoorbeeld een partij voor het datacenter en
de server-endpointdetectie, en een andere voor de SOC/SIEM en de netwerk-/campusdetectie (NDR). Dat is werkbaar,
maar er ontstaat een **naad** die je actief moet beheren:

- **Continuïteit bij overdracht.** Gaat de SOC/SIEM over naar een andere partij, borg dan dat bestaande
  detectieregels meegaan en getest worden - neem het niet aan.
- **Dekking over de naad.** Zorg dat geen enkel gebied tussen wal en schip valt (bijvoorbeeld oost-west-verkeer
  in het datacenter dat buiten de campus-NDR valt).
- **Concentratie versus regie.** Eén partij die meerdere rollen vervult (bijvoorbeeld firewallbeheer én SOC) is
  acceptabel **mits** je strak regie voert: functiescheiding waar mogelijk, break-glass, 4-ogen op wijzigingen,
  audit-logging naar een onafhankelijke bestemming, periodieke access-reviews, KPI's en een exit-scenario.

### Sturen op de managed-norm

Vraag van een SOC-/beheerpartner expliciet de vijf elementen van een managed dienst: bijhouden, beheren,
optimaliseren, functionaliteit aanpassen en verantwoorden (rapportage). Toets met een periodieke
aanvalssimulatie of detectie en preventie werkelijk dekken wat is afgesproken - laat het zien, neem het niet aan.

## Veilig faciliteren als langetermijnstrategie

### Twee richtingen

Er zijn grofweg twee manieren om het aanvalsoppervlak van de werkplek te verkleinen:

- **Reguleren (lockdown)** - het apparaat beperken: geen local admin, geen BYOD, een vaste
  set software.
- **Veilig faciliteren** - de bescherming in het platform leggen en toegang sturen op data en
  identiteit in plaats van op het apparaat.

Beide modellen komen in de praktijk voor en zijn verdedigbaar; de keuze hangt af van de
organisatie en de beschikbare beheercapaciteit (zie hieronder). Voor de ClickFix-casus is één
technisch punt van belang: een vergrendelde laptop beschermt op zichzelf niet tegen ClickFix,
omdat die aanval in gebruikerscontext draait en geen installatie of adminrechten nodig heeft.
De maatregelen die ClickFix wél raken (ASR, PowerShell CLM, Conditional Access, EDR,
segmentatie) passen in beide modellen. Het verschil tussen de modellen zit dus in de mate van
gebruikersvrijheid, niet in de bescherming tegen deze aanvalsvorm.

### Uitgangspunten van veilig faciliteren

1. **Afdwingen via configuratie, niet via gebruikersdiscipline.** Maatregelen zoals
   ASR-regels, PowerShell Constrained Language Mode en het uitschakelen van Win+R werken
   onafhankelijk van het gedrag van de gebruiker.
2. **Toegang op basis van data en identiteit.** Device-compliance en identiteitsrisico bepalen
   de toegang. Daarmee is BYOD mogelijk zonder het volledige apparaat te beheren.
3. **Bruikbare alternatieven bieden.** Een self-service softwarecatalogus, een beheerde
   browser en een password manager verkleinen de aanleiding om beperkingen te omzeilen en
   daarmee het risico op schaduw-IT.
4. **Uitzonderingen tijdelijk en gelogd.** Just-in-time elevatie in plaats van staande
   rechten: tijdgebonden, gelogd, automatisch vervallend en vastgelegd in een register.
5. **Elke maatregel heeft een eigenaar en aantoonbare werking.** Bestaan, opzet en werking
   zijn vastgelegd (configuratie-export, telemetrie), inclusief de afspraken met leveranciers.
6. **Detectie en herstel voor wat overblijft.** Niet alles is te blokkeren. Daarom meerdere
   chokepoints in de killchain, detectie, en geteste recovery (inclusief domain controllers).

### BYOD

BYOD is te beveiligen, maar niet met uitgefaseerde middelen. Windows Information Protection
(WIP) is door Microsoft deprecated; bouw daar geen nieuw beleid op. Bruikbare alternatieven:

- **App Protection Policies (MAM)** voor mobiel - corporate data blijft binnen een beheerde
  app-context, gescheiden van het privé-apparaat.
- **Conditional Access** met device-compliance en, voor onbeheerde Windows-apparaten,
  app-/sessiebeheer (bijvoorbeeld via een cloud-app-securityoplossing) in plaats van beheer
  van het volledige device.

### Randvoorwaarde: beheercapaciteit

Veilig faciliteren vraagt meer doorlopend beheer dan een lockdown-model. Het vervangt
eenmalige restrictie door continue configuratie, monitoring en uitzonderingsbeheer. Het model
werkt alleen als die regiecapaciteit er aantoonbaar is.

Een bruikbare toets: staan basismaatregelen die op papier "aan" staan ook werkelijk aan,
gekoppeld aan de juiste groepen (bijvoorbeeld ASR-regels)? Zo niet, dan is de regie de
bottleneck. In dat geval hoort een striktere lockdown als alternatief expliciet op tafel -
als bewuste keuze, niet als situatie die stilzwijgend ontstaat.

### Verhouding tot een lockdown-model

De modellen sluiten elkaar niet uit. Ook bij veilig faciliteren geldt een verdedigbare basis
die uit het lockdown-model bekend is: een beheerd device, geen staande local-adminrechten,
een beheerde browser en beheerde tijdelijke uitzonderingen. Dat is basishygiëne die BIO2 en
de Cyberbeveiligingswet afdwingbaar en auditbaar verwachten.

Het verschil zit in twee punten: BYOD blijft mogelijk via MAM en Conditional Access in plaats
van te worden beëindigd, en vrijheid wordt alleen weggenomen waar dat aantoonbaar risico
verkleint. Per control is de afweging: centraal afdwingen of aan het oordeel van de gebruiker
laten - en is die keuze uitlegbaar aan een auditor.

## Herbruikbare query's

De zes KQL-query's voor Advanced Hunting staan bij de handleiding waar ze bij horen:
[Werkplekanalyse op het Microsoft-platform](../werkplekanalyse-e5/). Daar staat per query waarvoor hij
dient (ClickFix-detectie, Win+R-gebruik, PowerShell-categorisatie, mshta) en hoe je de parent-processen en
uitsluitingen op je eigen omgeving aanpast.

## Werken met een LLM

Dit stuk is geschreven om mee te werken in een taalmodel. Neem de tekst en de query's mee als context, en
laat het model je helpen bij het categoriseren van je eigen meetresultaten en het invullen van de IST/SOLL-
en RACI-sjablonen.

Weeg wel af wat je waar doet. Kun je het zelf, prima. Heb je een lokaal model op geschikte hardware, doe
het daarin. Anders is het een risicoafweging: wat is het risico van het niet gebruiken van een model tegen
het risico dat je meetgegevens bij een aanbieder terechtkomen? Zet je meetresultaten liever geanonimiseerd
in, en houd de uitkomsten onder versiebeheer zodat de verbetering aantoonbaar en herhaalbaar blijft.

## Hoe dit samenhangt met de andere stukken

| Wil je | Ga naar |
|---|---|
| Weten welke aanvalspaden bij jou openstaan, in een uur | [Zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/) |
| Die uitkomst omzetten in een risicolijst met eigenaar | [Risicoanalyse langs aanvalspaden](../risicoanalyse-aanvalspaden/) |
| De rode cellen structureel dichten met mandaat | [Een blue team opzetten](../blue-team-opzetten/) |
| AI-gebruik in je organisatie feitelijk meten | [AI-gebruik in beeld](https://security-commons-nl.github.io/ai-gebruik-in-beeld/) |

## Herkomst

Gegeneraliseerd uit een concrete casus bij een gemeentelijke organisatie, ingebracht in de commons. De
voorbeelden en aantallen komen uit die casus; de aanpak is bedoeld om over te nemen, niet om na te doen.

## Licentie

EUPL-1.2, zie de [licentie van de kennisbank](../../LICENSE).
