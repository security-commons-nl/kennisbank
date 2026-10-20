# Procedure cyberdreigingen en kwetsbaarheden

### Opdrachtgever/eigenaar

CISO

### Opdrachtnemer

[naam] (informatiebeveiliger), [naam] (TISO) [naam] (BISO) en [naam] (BCM projectmanager)

### Aanleiding

Digitale dreigingen nemen toe in frequentie en impact. Een dreiging is een waargenomen risico waarvan nog onduidelijk is of het onze organisatie raakt; het is mogelijk dat er gebruik (of eigenlijk: misbruik) wordt gemaakt van kwetsbaarheden in de gemeentelijke, met als resultaat een daadwerkelijke verstoring. Die behandelen we dan als incident, hiervoor hebben we een duidelijk proces om het op te lossen, voor dreigingen is zo’n proces er nog niet.

Recente voorbeelden, zoals de dreiging als gevolg van het lek in log4j en de cyberaanval op TU Eindhoven, laten zien hoe groot de gevolgen kunnen zijn als de dreigingen werkelijkheid worden en kwetsbaarhedne worden misbruikt. Deze procedure helpt ons om adequaat te reageren op dreigingen en schade te beperken.

### Doel en belang

Met deze procedure streven we ernaar om dreigingen en kwetsbaarheden gestructureerd te beoordelen en te behandelen, op basis van urgentie, impact en risico. Dit gaat over omgaan met onzekerheden, er voor zorgen dat zaken vlot worden uitgezocht en er daarmee voldoende duidelijkheid komt. Hierdoor kan risico gestuurd, proportioneel en met duidelijk eigenaarschap worden opgetreden.

### Centrale vragen

- Hoe richten we een gestructureerde werkwijze in voor het inschatten, prioriteren en mitigeren van digitale dreigingen en kwetsbaarheden, met duidelijk eigenaarschap en verantwoordelijkheden?

- Hoe organiseren we effectieve samenwerking tussen de betrokken stakeholders van de organisatie binnen deze werkwijze?

- Hoe gaan we om met bestaande kwetsbaarheden en geaccepteerde risico's rondom bekende kwetsbaarheden?

- Hoe houden we deze werkwijze actueel en werkbaar in de praktijk?

### Werkwijze

We willen vlot maar proportioneel handelen. Dat betekent dat we in moeten schatten wat de mogelijke impact is van de kwetsbaarheid, welke mogelijke oplossingen er zijn en wat de impact is van het implementeren van de oplossing. Op basis van die informatie kan een keuze worden gemaakt.

- Startpunt: Signaal van dreiging. Directe actie (binnen 1 uur na binnenkomst starten risico-analyse bij CVSS score > 9, of melding vanuit IBD of leverancier dat het een acuut issue is. Bij lagere dreiging: binnen een week behandelen. Als maatregelen nodig zijn of overwogen moeten worden, maak dan altijd een melding aan in het servicedesksysteem.

- Bepaal de kans de kwetsbaarheid zich ook bij ons voordoet: Verzamel dreigingsinformatie (o.a. CVSS-score, NCSC/NLCS-duidingen). Bepaal in hoeverre dit in VOORBEELDGEMEENTE van toepassing is, en of kan en impact overeenkomen of juist afwijken van de dreigingsinformatie. Identificeer de kwetsbaarheid voor onze systemen en mogelijke aanvalspaden. Is het niet van toepassing voor onze systemen?

- Bekijk impact eigen organisatie en toets tegen kritische processen (BIA, kroonjuwelen). Kijk naar dimensies: beschikbaarheid, integriteit, vertrouwelijkheid, privacy, bestuurlijke gevolgen. Eigenaar: Proceseigenaar. Actiehouder: ISO, die zorgt dat de proceseigenaar het advies krijgt. Is het niet bekend wie de proceseigenaar is? Dan willen we toch voortvarend handelen in deze onzekere situatie Is het risico proces overstijgend (bijvoorbeeld omdat het de IT infrastructuur raakt), dan ook de CIO als eigenaar behandelen. Volg ook het calamiteitenplan digitaal in dat geval.

- Risico-inschatting

Bepaal kans × impact (kwalitatief of kwantitatief) op een 5 puntsschaal. 1 is zeer laag, 5 is zeer hoog. Omdat de risk-appetite van de organisatie nog niet bepaald is, werken we hiermee als vuistregel. Vermenigvuldig de kans (zie punt 1 in deze werkwijze) met de impact (zie punt 2 in deze werkwijze) en neem dat getal als de risico-inschatting. Let wel: Als je een “niet-pluis-gevoel" hebt, dan mag je altijd escaleren. Professionaliteit gaat boven de procedure.

Handelingskader:

Laag Risico: score lager dan 5

Voorbeeldaanpak: -ISO/informatiebeveiliger maakt inschatting aanpak. Neemt contact op met functioneel beheer, TAB en eventueel MSP; afstemming via het servicedesksysteem. Reactie in het servicedesksysteem binnen een werkdag, oplossen via reguliere planning. Doorlooptijd: maximaal 10 werkdagen. Gemiddeld Risico van 5 tot en met 14 Voorbeeldaanpak: - ISO stemt af met incidentcoördinator. - Binnen 1 uur gezamenlijke verkenning en bepaling vervolgstappen. - Rollen kunnen deels onduidelijk zijn → zo nodig herijken. - Registratie in het servicedesksysteem. Escalatie: indien nodig naar CISO en teammanager regie en processen. Doorlooptijd: maximaal 5 werkdagen, afhankelijk van de dreiging.

Acuut Risico groter dan 15

Voorbeeldaanpak: - ISO en incidentcoördinator stemmen af en informeren hun coördinator. - Indien aanpak onduidelijk of geen oplossing binnen 1 uur: escalatie naar CISO. - CISO kan adviseren aan CIO om het CTD te activeren. - Registratie in het servicedesksysteem.

Bij acuut risico kan het nodig zijn dat preventief een (deel van een) systeem worden uitgeschakeld. Ook als dat impact heeft op de (kritische) dienstverlening. In dat geval is het goed om het CTD in te schakelen en daarbij de proceseigenaar uit te nodigen. Als de dreiging écht acuut is, dan is het belangrijk eerst de maatregel te nemen en daarna te informeren.

Geen oplossing vandaag → CISO adviseert CTD te activeren. Doorlooptijd: zo kort mogelijk, bij voorkeur binnen één werkdag.

- Beoordeel opties ISO 27005 noemt: risico vermijden, verminderen, overdragen, accepteren. Toets ook aan wettelijke eisen (Cbw, BIO2). Soms zijn er verschillende maatregelen mogelijk om een risico te mitigeren, met verschillende kostenplaatjes en restrisico’s. Koppel terug aan de proceseigenaar en de systeemeigenaar als het de (IT-)infrastructuur raakt. Is de proces- of systeemeigenaar onbekend, dan binnen de IT-organisatie escaleren.

- Kies maatregelen en leg deze vast. Is de gekozen maatregel omvangrijk of vergt het doorlooptijd, leg dat dan vast in het servicedesksysteem.

- Uitvoeren binnen acceptabele termijn Monitor voortgang (het servicedesksysteem of ISMS, P&C-cyclus). Escaleren bij vertraging of onvoldoende effect. Eigenaar: Projectleider / verantwoordelijke uitvoerder.

- Besluit risico-acceptatie Als maatregelen niet (tijdig) uitvoerbaar zijn → voorleggen aan bevoegde beslisser (bv. gemeentesecretaris of directie, afhankelijk van impactniveau). Documenteer expliciet (waiver/risico-acceptatieformulier). Eigenaar: Bestuurder/Directeur, na advies CISO.

### Samenwerking

Algemene uitgangspunten in de samenwerking:

- Werk met vaste rollen en back-ups,

- Zorg altijd voor een warme opstart, dus direct contact (via telefoon, teamschat, videocall oid) bij deze aanpak. Tijdens het werken aan de oplossing kan de communicatie deels ook via het servicedesksysteem, het servicedesksysteem is niet de tool om de samenwerking mee op te starten omdat de interactie te beperkt is.

- Gebruik het servicedesksysteem als centrale plek voor registratie én monitoring.

- Zorg voor beslisbevoegdheden die vooraf zijn afgestemd, of vraag deze expliciet aan het management (mandaten, stekkermandaat).

- Zorg regelmatig voor afstemming tussen ISO en incidentcoördinatoren. Bijvoorbeeld eens per kwartaal

### Voortvarend omgaan met onzekerheid

Dreigingen zijn niet altijd meteen helder in te schatten. Zowel het inschatten van de kans als van de impact is ingewikkeld. Hulpmiddelen zoals een actuele en volledige architectuurplaat en CMDB zijn een randvoorwaarde om de impact te kunnen inschatten. Als er een dreiging speelt op een bepaalde component, dan kan je op basis van de beschikbare informatie soms zekerheid krijgen dat de dreiging voor de organisatie relevant is.

Lijkt het niet relevant op basis van de beschikbare informatie, dan het belangrijk goed na te gaan wat de zekerheid is waarmee je kan zeggen dat de dreiging dus niet speelt in VOORBEELDGEMEENTE. Is de twijfel groot of klein? Bij grote twijfel en een grote kans op misbruik, en (mogelijk) een grote impact op de business moet er tóch nader geanalyseerd worden, meer zekerheid komen. Het advies van IBD en andere bronnen is dan ook belangrijke input om wel of niet te escaleren.

Sinds een paar jaar is de “Assume breach” aanpak in opkomst binnen de cybersecurity. We weten immers dan hetgeen we zien, niet alles is wat bestaat, dus dat er meer zekerheid en voorzichtigheid moet worden ingebouwd in processen. Dit betekent nogal wat voor de ISO’s: als er een dreiging is van niveau Midden of Acuut, dan wordt in onderling overleg meteen bepaald hoe er een risico-assessment gedaan wordt dat binnen een uur een eerste resultaat moet hebben. Dat passen we toe in deze procedure, die we uiteraard aanpassen als vanuit evaluaties blijkt dat het strakker of losser moet.

### Vuistregels

Deze procedure geeft wat richting aan de manier waarop we omgaan met concrete cyberdreigingen, zodat we proportioneel kunnen handelen. Onderstaande vuistregels gelden daarbij ook, en mogen we van onszelf en onze collega’s verwachten:

- Zien = Doen! De persoon die het signaal ontvangt, is verantwoordelijk voor het initiëren van de actie. Neem de regie, je hoeft niet alles op te lossen, maar zorgen dat het signaal tot actie leidt is je werk. Je toont eigenaarschap: zorgt dat het voor elkaar komt.

- We zijn er bijna? Toch escaleren! Ervaring leert dat het lastig in te schatten is hoeveel tijd het oplossen van een dreiging of incident nog kost. Escaleer dus als het tijd is, ben je (vaak) te snel met aan de bel trekken? Dan passen we na verloop van tijd de procedure aan.

### Wie moet geïnformeerd worden, waarover en door wie?

| Dreigingsniveau | Te informeren personen | Door wie | Onderwerpen van communicatie |
|---|---|---|---|
| Laag Risico | Functioneel beheerder | ISO/informatiebeveiliger | Technische aard van dreiging, mogelijk aanpak, overleg over realistische oplossingstermijn |
|  | Gebruikersgroepen | Functioneel beheerder | Eventuele tijdelijke beperkingen of alternatieven |
| Gemiddeld Risico | Incidentcoördinator | ISO/informatiebeveiliger | Risico-inschatting, onzekerheden, beoogde oplossing en tijdspad |
|  | CISO, teammanager regie en processen (bij escalatie) | Incidentcoördinator / ISO | Dreigingsbeeld, knelpunten in aanpak, noodzaak prioriteit of escalatie, bedrijfsimpact beoogde oplossing |
|  | Gebruikersorganisatie | Incidentcoördinator / ISO (evt. met communicatie of functioneel beheer) | Verwachte impact op dienstverlening en alternatieven |
| Acuut Risico | Incidentcoördinator | ISO | Risico-inschatting, onzekerheden, beoogde oplossing en tijdspad, escalatie-aanpak |
|  | CISO en teammanager regie en processen | Incidentcoördinator / ISO | Onmogelijkheid tot snelle mitigatie, besluitvorming over inzet CTD, beoogde oplossing inclusief bedrijfsimpact |
|  | CIO (bij activering CTD) | CISO | Advies voor instellen CTD voor centrale aansturing oplossing |
|  | CTD-leden (na besluit tot inzet) | CISO/secretaris CTD | Dreigingsbeeld, besluitvorming en rollen CTD |
|  | Communicatieadviseur als deelnemer aan CTD | CISO/CTD-secretaris | Of en hoe (intranet, persoonlijk) er intern/extern gecommuniceerd moet worden (denk aan IBD, Gemeentelijke clusters, de organisatie) |
|  | Direct betrokken afdelingen | Communicatie (CTD) of incidentcoördinator | Aard van verstoring, bedrijfsimpact, planning herstel, eventuele maatregelen en alternatieve werkwijze |

### Actualiseren werkwijze

Beheerder van deze procedure is ISO. Jaarlijks of als onderdeel van een evaluatie bij dreigingen wordt de procedure aanpast, in samenspraak met de incident coördinator.

Bij dreigingen die acuut zijn, moet deze binnen een week na afhandeling worden geëvalueerd. Deze procedure geeft mee invulling aan het informatiebeveiligingsbeleid.
