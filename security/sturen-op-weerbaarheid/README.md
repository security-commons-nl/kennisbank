---
titel: Sturen op weerbaarheid in plaats van op maatregelen
vakgebied: security
type: aanpak
normen: [BIO2]
versie: 2026-09
herkomst: gegeneraliseerd uit een casus bij een gemeentelijke organisatie
status: in gebruik
samenvatting: Voor bestuur, directie en CISO: waarom digitale weerbaarheid nu op tafel ligt, wie waarvoor verantwoordelijk is, en de keuze tussen alles dichtzetten of veilig faciliteren. Met het lagenmodel, een RACI-sjabloon, de naad tussen eigen organisatie en leveranciers, en waarom een resultaatverplichting iets anders is dan een inspanningsverplichting.
pijler: meten-voordat-je-ingrijpt
---

# Sturen op weerbaarheid in plaats van op maatregelen

> **Lees dit stuk online:** [security-commons-nl.github.io/kennisbank/security/sturen-op-weerbaarheid](https://security-commons-nl.github.io/kennisbank/security/sturen-op-weerbaarheid/)

Dit stuk is voor bestuur, directie en de CISO die hen adviseert. Het beantwoordt drie vragen: waarom dit
onderwerp nu op tafel ligt, wie waarvoor verantwoordelijk is als het misgaat, en of je kiest voor
dichtzetten of voor veilig faciliteren.

Het hangt aan geen enkele barriere uit de zelfcheck, en dat is geen omissie. "Kies tussen lockdown en
veilig faciliteren" is een bestuurlijk gesprek, geen maatregel die je inricht en waarvan je bewijs
overlegt. De maatregelen zelf staan in de handleidingen; hier staat waarop je stuurt.

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

## Hoe dit samenhangt

Dit stuk hoort bij [Meten voordat je ingrijpt](../meten-voordat-je-ingrijpt/): daar staat de methode,
hier staat waarop je stuurt terwijl je hem uitvoert. De maatregelen zelf staan als handleidingen in de
[kennisbank](../), elk gekoppeld aan een barriere uit de
[zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/).

Voert u het gesprek met college of directie, dan is de
[weerbaarheidsgame](https://security-commons-nl.github.io/weerbaarheid-game/) een werkvorm die dezelfde
vragen op tafel legt zonder dat er techniek aan te pas komt.

## Herkomst

Gegeneraliseerd uit een casus bij een gemeentelijke organisatie. Alle herleidbare gegevens zijn
verwijderd; wat overblijft is de werkwijze.

## Licentie

[EUPL-1.2](../../LICENSE).
