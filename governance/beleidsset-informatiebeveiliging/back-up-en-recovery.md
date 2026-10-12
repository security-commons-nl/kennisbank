# Beleid back-up en recovery

> **Concept, niet vastgesteld.** Dit stuk staat hier als voorbeeld van een uitgewerkt concept. Neem het niet over als vastgesteld beleid.

### Afkortingen en begrippen

| Afkorting | Omschrijving |
|---|---|
| BIO | Baseline Informatiebeveiliging Overheid. Een Baseline is een basis(beveiligings)- niveau. De BIO is het daarmee het minimale niveau waaraan overheden dienen te voldoen op het gebied van informatieveiligheid; de ondergrens. |
| SaaS | Software as a Service: ook weleens software-on-demand genoemd, is software die als een online dienst wordt aangeboden. |
| IaaS | Infrastructuur as a Service, dienstverlening die gericht is op het aanbieden van de basis IT infrastructuur, zodat klanten/gebruikers zich kunnen richten op de dienstverlening aan hun klanten omdat een groot deel van de kennisintensieve beheertaken als service wordt uitgevoerd door anderen. De applicaties en data en een deel van de technische beheertaken zijn hierbij niet uitbesteed. |
| BIO opmaat | Opmaat naar versie 2.0 van de BIO. Met de opmaat wordt geanticipeerd op de veranderingen aan de BIO als gevolg van (o.a.) de NIS 2 richtlijn. |
| IB | Informatiebeveiliging, zowel een vakgebied, aandachtspunt binnen de IV als een teamonderdeel binnen de IV organisatie |
| Back-up | Reservekopie. Bedoeld om bij verstoring in de beschikbaarheid van het originele bestand toch nog over de gegevens te kunnen beschikken en het bedrijfsproces te herstellen. |
| Recovery | Het herstellen van de gegevens vanuit de back-up als stap om het bedrijfsproces te herstellen. |
| RTO | Recovery Time Objective |
| RPO | Recovery Point Objective |
| RGO | Recovery Granitory Objective |
| Retentie | Bewaarperiode (van back-up bestanden) |
| BBN toets | Basis Beveiligings Niveau toets, waarmee op basis van de aard van de informatie bepaald wordt wat de minimale maatregelen voor de beveiliging ervan zijn. |
| Cyber & IT crisisplan | Een plan ter voorbereiding op digitale noodscenario’s. Werkwijze, bemensing en procedures voor respons en communicatie zijn hierin vastgelegd. |
| Back-up window | De periode buiten kantooruren waarbinnen een back-up wordt gemaakt, op het moment dat er weinig activiteit is, zodat de kans dat de back-up mislukt kleiner is. |

### Relevante beleidsdocumenten (en inspiratiebronnen)

- Baseline Informatiebeveiliging Overheid (BIO) en BIO 2.0 Opmaat

- Strategisch IB-beleid

- Kennisproducten IBD (informatiebeveiligingsdienst van VNG) waaronder Back-up strategie, handreiking back-up & recovery, praktische aanpak 3-2-1 regel

- NEN-EN-ISO / IEC 27001/27002 : 2022 (nl) De Nederlandse norm voor Informatiebeveiliging, cybersecurity en bescherming van de privacy

- NIST Special Publication 800-34 Rev. 1 Contingency Planning Guide (als inspiratiebron)

## Inleiding

Back-up en recovery zijn belangrijke beschikbaarheidsmaatregelen die ervoor zorgen dat corrupte, verloren of vernietigde bedrijfsinformatie hersteld kan worden. Een goed back-up en recovery proces zorgt ervoor dat er na een incident snel weer de juiste informatie teruggeplaatst kan worden en er zo min mogelijk informatie verloren gaat. Met deze back-up kan een bedrijfsproces of bedrijfsfunctie die afhankelijk is van deze informatie zo snel mogelijk hersteld worden. Een goede back-up strategie helpt om de bedrijfscontinuïteitsvereisten in te vullen. Door bij het maken van de back-up al rekening te houden met het bedrijfsbelang, kan dit inzicht worden gebruikt bij de recovery, om zo de meest bedrijfskritische processen het eerst weer beschikbaar te maken.

Back-ups gaan niet alleen over documenten, maar over alle soorten gegevens. Het gaat zowel om een bestandskopie als om een systeemkopie, met o.a. inrichtingsparameters van netwerken, applicaties, virtuele machines en databases. Alle digitaal opgeslagen informatie die een rol speelt in de werking van bedrijfssystemen of eruit voortkomt kan dus onderdeel zijn van de back-up.

Back-up en recovery zijn beschikbaarheidsmaatregelen, bedoeld om de bedrijfsfuncties beschikbaar te houden. Deze maatregelen voor back-up en recovery staan dan ook niet op zich, maar moeten in samenhang met andere beschikbaarheidsmaatregelen bekeken worden. Als er redundantie is in functionaliteiten, dan is de afhankelijkheid van een ondersteunend middel kleiner; er is immers nog een alternatief. Dus is de afhankelijkheid van de back-up dan kleiner. Wel kan zoiets per scenario verschillen; sommige calamiteiten hebben invloed op alle redundante middelen tegelijk. Back-ups zijn vaak nodig als eerdere maatregelen om beschikbaarheid te verhogen onvoldoende werken, een laatste redmiddel om informatie of bedrijfsfuncties te herstellen.

### Doelstelling van back-up en recovery

Doelstelling van back-up en recovery is het bewaren en beschermen van de gegevens en functionaliteit van de programmatuur. Bij verlies of beschadiging is herstel mogelijk, na bijvoorbeeld:

- Een security incident veroorzaakt door een ransomware aanval;

- Een niet correct uitgevoerde wijziging/change;

- Fouten in de software of corruptie van data of programmatuur;

- Menselijke fouten, zoals bedienfouten (bewust en onbewust);

- Corruptie van data of programmatuur

Niet alleen bedrijfsinformatie (zoals een bestand of database) dient meegenomen te worden in een back-up, maar ook de systeeminstellingen, zodat programma’s, diensten en verbindingen.

Een goede back-up die regelmatig vernieuwd wordt om steeds actueel te blijven, zorgt ervoor dat een recovery ook daadwerkelijk succesvol kan zijn. De recovery moet gericht zijn op het bedrijfsbelang (de belangrijkste processen het eerst weer herstellen) en bewezen betrouwbaar zijn. Soms valt het niet meteen op dat gegevens niet meer beschikbaar zijn en terug gehaald moeten worden vanuit een back-up. Verschillende versies van bestanden (op verschillende momenten gemaakt) kunnen dan uitkomst bieden.

### Verschil tussen Back-up en Archief

Back-ups zijn bedoeld om gegevens bij calamiteiten te kunnen herstellen. Een archief is een goed geordende en toegankelijke bewaarplaats van gegevens om te zorgen dat belangrijke overheidsinformatie behouden blijft en toegankelijk wordt op het juiste moment voor de juiste mensen. Er geldt voor archieven ook een plicht om gegevens conform het archiefbeleid openbaar te maken of te vernietigen. Het publieke belang van de informatie staat bij het archief voorop, terwijl bij de back-up het bedrijfsvoeringsbelang voorop staat. Een back-up is dus geen archief. En een archief is dus geen back-up.

### Begrippen

Bij back-up en recovery zijn RTO en RPO de meest belangrijke begrippen. Recovery Time Objective (binnen hoeveel tijd moet het proces hersteld zijn) en Recovery Point Objective (Vanaf welk punt in de tijd moet het zeker zijn dat je de gegevens nog hebt. En dus: hoeveel gegevens en mutaties mag je maximaal verliezen?). Deze vragen zijn voor verschillende soorten informatie anders. Het vraagt per soort informatie om een risico-afweging.

Naast RPO en RTO is ook de RGO van belang: de Recovery Granularity Objective. Hiermee wordt aangegeven wat het detailniveau is waarop gegevens hersteld moeten kunnen worden. Als voorbeeld voor e-mail: moet dit per bericht, per mailbox, of per mailserver te herstellen zijn?

En hoe lang wil je bepaalde back-ups bewaren, de zogenaamde retentieperiode? Als de retentieperiode te kort is, dan is herstel van bestanden alsnog niet mogelijk. De retentieperiode moet voor alle scenario’s waar een back-up uitkomst voor moet beiden passend zijn.

Al met al moet de back-up zorgen voor een betrouwbare kopie van belangrijke gegevens, waarbij nooit te veel informatie verloren kan raken. De tijd die nodig is om gegevens en bedrijfsfuncties te herstellen is voorspelbaar en passend bij het maatschappelijk belang. Het proces van back-up en recovery, inclusief de benodigde middelen (tools, processen, kosten) is zo een bewust ingezette beheersmaatregel voor de risico’s op verlies van gegevens en bedrijfsondersteunende systemen.

### Risico-afweging

Het risico dat we als gemeente(n) onze maatschappelijk taak niet meer kunnen vervullen, doordat de dienstverlening (aan kwetsbare groepen) stil komt te liggen willen we niet lopen. 100% zekerheid bestaat niet en hoe korter de RTO en RPO, hoe hoger de kosten zullen zijn. Op basis van het bedrijfsbelang en de (al dan niet acceptabele) risico’s moeten de kosten en de baten worden afgewogen.

Vanuit Bedrijfscontinuïteitsmanagement zijn maatschappelijke risico’s van verstoring van processen al afgewogen en is er een prioritering vastgesteld. Voor de meest kritische processen (zoals het betalen van uitkeringen en leefgeld) is de maximaal acceptabele hersteltijd bepaald op 1 dag.

Zo’n maximaal acceptabele hersteltijd betekent concreet dat áls (de informatiesystemen die gebruikt worden bij) bedrijfskritische processen uitvallen, de organisatie in staat moet zijn dat vlot te onderkennen, correctieve maatregelen te nemen, actief te communiceren én de dienstverlening te herstellen binnen die periode. Er zal dus veel minder dan een dag tijd zijn om het back-up en recovery-proces voor bedrijfskritische systemen uit te voeren, er moet immers meer gebeuren dan back-up en recovery van de gegevens voordat de dienstverlening hersteld is.

Risico’s in bedrijfscontinuïteit zijn niet de enige risico’s die beschouwd meten worden om de back-upstrategie te bepalen. Bijvoorbeeld voor (ruimtelijke)projecten, de opgebouwde waarde van informatie en uit financiële overwegingen is het ook van belang dat gegevens beschikbaar blijven. Als er geen volledige risico-analyse is uitgevoerd, maar uit de BBN toets blijkt dat het beschermingsniveau BBN2 of hoger is, dan mag het dataverlies niet hoger zijn dan 24 uur en de hersteltijd maximaal 16 werkuren zijn. Het is goed dit als minimumniveau aan te houden tenzij er expliciet voor gekozen wordt de gegevens niet op te nemen. Zoiets is bijvoorbeeld voor luchtfoto’s (of andere omvangrijke statische datasets die van derden worden afgenomen) voorstelbaar.

Daarnaast zijn er ook back-ups nodig van de machine (server) instellingen, de zogenaamde system state back-up. Deze zorgt ervoor dat bij een volledige vervanging van een server de basis instellingen weer snel hersteld kunnen worden. Op werkdagen moeten hier back-ups van worden gemaakt, zodat er geen dataverlies kan optreden. Als er werkzaamheden aan servers worden gedaan, is het een goede gewoonte (en een bewezen effectieve werkwijze) om snapshots te maken van een server. Dit gaat dan buiten de geautomatiseerde back-up om en werkt sneller en prettiger. Zo is er altijd een laatste “werkende” versie van iedere server beschikbaar.

### Scenario’s

Het beleid voor back-up & recovery zou moeten volstaan in alle gevallen. Het is niet mogelijk voor alle gevallen een risico-analyse te maken, voor een aantal scenario’s willen we in ieder geval voorbereid zijn met de back-up oplossing:

- Een aanval met ransomware of wiperware, waarbij de gemeentelijke infrastructuur wordt aangevallen en versleuteld of verwijderd.

- Een grote verstoring in het belangrijkste datacenter

- Dataverlies bij een SaaS applicatie voor een kritische bedrijfsfunctie

- Dataverlies bij (een onderdeel van) Microsoft 365 wat de bedrijfsfunctie van de organisatie raakt

- Een boze gebruiker / een klunzige gebruik verwijdert een grote hoeveelheid bestanden

Er zijn ook scenario’s waarbij de beschikbaarheid van gegevens in het datacenter geraakt wordt, maar waar een back-up geen oplossing kan bieden. Denk bijvoorbeeld aan uitval van internetlijnen of netwerkverbindingen. De gegevens worden hierbij niet geraakt (zijn nog steeds beschikbaar in het datacenter, maar de beschikbaarheid van de gegevens voor de dienstverlening is toch verstoord. Dat valt dan niet onder de scope van dit beleid, maar past wel binnen het Cyber&IT crisisplan.

## Back-up strategie

Prioritering van de back-up van gegevens vind plaats aan de hand van het bedrijfsbelang. Met de BBN-toets kan het basisbeveiligingsniveau van informatie worden bepaald, dat bepaalt hoe de back-up minimaal ingericht zou moeten zijn. Ook zijn vanuit bedrijfscontinuïteitsmanagement de processen vastgesteld waarvan verstoring de grootste negatieve maatschappelijke impact heeft. En zijn de bijbehorende maximaal acceptabele hersteltijen bepaald. Dit geeft ook een prioritering aan bij herstel, hoe hoger het BBN niveau en hoe korter de maximaal acceptabele hersteltijd, hoe hoger de prioriteit waarmee aan herstel van dit proces gewerkt dient te worden.

Eerst de meest kritische processen herstellen om zo maatschappelijke ontwrichting te voorkomen, daarna zorgen dat de bedrijfsvoering zo snel mogelijk hersteld kan worden. Indien er nog geen analyse of classificatie heeft plaatsgevonden, kan het standaard regime voor back-ups worden toegepast. Het krijgt dan geen bijzondere prioriteit bij herstel.

Een reservekopie moet steeds actueel zijn, zodat er niet te veel informatie kwijt kan raken. Afhankelijk van het soort informatie wil je ook kiezen hoe je de back-up wil bewaren. Het moet niet te lang duren om gegevens te kunnen herstellen en wil je kunnen het detailniveau waarop je gegevens herstelt goed kunnen kiezen. Bijvoorbeeld voor e-mail: wil je een mail, een mailbox of mailserver kunnen herstellen? Of alle 3, afhankelijk van de situatie?

Per onderdeel van de back-up worden de RTO, RPO, RGO, back-up frequentie en retentietijd bepaald. De relatie tussen de back-up en het bijbehorende proces moet bekend zijn, zodat het belang van het proces kan worden gebruikt om in de juiste volgorde te herstellen vanuit de back-up.

Alle gegevens waarvan we eigenaar zijn moet geback-upt worden. Ook als de data in de cloud staat. Als data-eigenaar hoort dat bij onze verantwoordelijkheid om daar op toe te zien. In een samenwerking met cloudpartners die vooral hosting beschikbaar stellen zal de taak van ons als opdrachtgever groter zijn dan bij cloudpartners die een bedrijfsfunctie ondersteunen, maar in beide gevallen is het in het primaire belang van ons als opdrachtgever dat dit goed geregeld is en past bij het bedrijfsbelang dat met de cloud-partner wordt ingevuld..

### Algemene uitgangspunten en good practices back-up:

Voor alle back-ups, binnen het eigen datacenter én bij SaaS leveranciers, zijn er een aantal uitgangspunten en good practices beschikbaar. Deze hanteren we als uitgangspunten om de beschikbaarheid, integriteit en vertrouwelijkheid van de back-ups te borgen:

- 3-2-1- vuistregel: Minstens drie versies van een back-up moeten worden bewaard, op tenminste twee verschillende opslagmedium, waarvan er 1 op een andere fysieke plek bewaard moet worden. Een off-site back-up is in ieder geval voor gegevens in bedrijfskritische processen vereist.

- Minimale en maximale bewaartijden van back-ups moet bepaald zijn en passen bij gebruiksdoelen en (privacy-)wetgeving; gegevens mogen niet kwijt raken maar ook niet te lang bewaard worden; als gegevens verwijderd moeten worden obv (bijvoorbeeld) de archiefwet, dan dienen de gegevens ook uit de back-up verwijderd te worden.

- Authenticiteit van back-ups moet geborgd zijn. Dat kan door technische en/of organisatorische maatregelen. (zijn deze te wijzigen of versleutelen of niet)

- Integriteit van de back-ups moeten gewaarborgd zijn. Bijvoorbeeld met het WORM-principe: write once, read many. Dit zorgt ervoor dat gegevens niet kunnen worden gewijzigd als ze eenmaal zijn geschreven en opgeslagen.

- Er moet een proces zijn ingericht om dagelijks te controleren of de back-up is geslaagd. Indien dit niet het geval is, dan dient er indien mogelijk alsnog een correcte back-up gemaakt te worden. Off-site back-ups moeten altijd gecontroleerd worden door te checken of ze ontsleuteld kunnen worden en “valide” zijn.

- Back-ups worden regelmatig getest om te verifiëren dat het proces betrouwbaar is. Compleetheid en integriteit van de te herstellen bestanden moet buiten kijf staan.

- Er moet een nauwkeurig en volledig register van back-up bestanden, herstelprocedures en bewaarplaatsen worden bijgehouden.

- Vertrouwelijke gegevens die onderdeel zijn van de back-up dienen altijd versleuteld (en voorzien van toegangsmaatregelen) opgeslagen te worden. Anders wordt een back-up bestand meer een risico dan deel van de oplossing. Het beheren van toegang tot de sleutels (om een back-up ook weer te kunnen ontsleutelen) en het monitoren van het gebruik ervan is een belangrijke randvoorwaarde. Hiervoor kan de bestaande wachtwoordkluis gebruikt worden.

### Back-up en wetgeving

Het is noodzakelijk om een back-up te maken van belangrijke systemen om te kunnen voldoen aan wetgeving. Nederlandse gemeenten zijn verplicht om na een calamiteit de Basisregistratie personen (BRP) en andere systemen binnen 48 uur weer volledig operationeel te hebben op een alternatieve locatie. Zonder een goede back-ups, procedures en uitwijktesten is dit niet mogelijk en kan de dienstverlening niet aan de wet voldoen. Binnen de organisatie zijn de procedures hiervoor opgesteld in het beveiligingsplan Burgerzaken.

#### AVG

Back-ups bevatten ook persoonsgegevens, en vallen daarmee onder de AVG-wetgeving. Persoonsgegevens moet ook op het back-up medium versleuteld zijn. De organisatie is in bepaalde gevallen verplicht om iemands gegevens te verwijderen als diegene hierom vraagt. Bijvoorbeeld als de gegevens niet meer nodig zijn, iemand zijn toestemming intrekt of er geen wettelijke basis meer is om deze gegevens te bewaren. Deze gegevens dienen dan in principe ook uit de back-up verwijderd te worden. Om bedrijfsvoeringsrisico’s te vermijden, is het onvermijdelijk dat de verwijderde persoonsgegevens tijdens de retentieperiode nog wel in de back-up aanwezig zijn. Omdat persoonsgegevens in de back-up versleuteld zijn opgeslagen, is dit geen onacceptabele inbreuk op de privacy. Na de retentieperiode zijn de verwijderde persoonsgegevens ook uit de back-up verdwenen.

#### NIS2

Vanuit de NIS2 richtlijn is de gemeente als een essentiële dienstverlener benoemd. Dat geeft een extra verantwoordelijkheid voor het borgen van de continuïteit.

- De zorgplicht van de gemeente,

- De meldplicht bij verstoring van de dienstverlening aan de IBD en

- Het toezicht hierop door de Rijksdienst voor de Digitale Infrastructuur (RDI), met verantwoording via de ENSIA methodiek.

NIS2 is nog niet in Nederlandse wetgeving vertaald. Toch geeft de Opmaat naar de BIO 2.0 al wel richting aan de manier waarop vanuit NIS2 de eisen rondom back-up worden geformuleerd:

- Er moet een back-up beleid zijn, met speciale aandacht voor ransomware

- Op basis van een expliciete risicoafweging is bepaald wat het maximaal toegestane dataverlies is en wat de maximale hersteltijd is na een incident.

In het back-upbeleid staan minimaal de volgende eisen:

- (a) Dataverlies bedraagt maximaal 28 uur.

- (b) Hersteltijd in geval van incidenten is maximaal 16 werkuren (2 dagen van 8 uur) in 85% van de gevallen.

- Het back-upproces voorziet in opslag van de back-up op een locatie, waarbij een incident op de ene locatie niet kan leiden tot schade op de andere.

- Zorg dat ten minste één back-up niet online benaderbaar is en beschermd wordt tegen veranderingen.

- De herstelprocedure wordt minimaal jaarlijks getest of na een grote wijziging, om de goede werking te waarborgen als deze in noodgevallen uitgevoerd moet worden.

Met dit beleid wordt invulling gegeven aan deze eisen.

### Back-up en Recovery binnen een regieorganisatie

De organisatie wil strategisch de regie voeren op de IT diensten. De infrastructuur wordt als service (IaaS) afgenomen, voornamelijk bij een hostingpartij. Er zijn ook andere leveranciers die een deel van het IT-landschap in beheer hebben. Door middel van regie wordt de samenhang bewaakt en de bedrijfsdoelstelling zo goed mogelijk gesteund. Voor de systeemback-up zijn er mogelijk dus meerdere leveranciers betrokken.

Voor de back-up op bestandsniveau zijn er ook twee smaken: of de data staat in het datacenter van de organisatie, dat gehost wordt door de hostingpartij. Of het is onderdeel van de Software as a Service (SaaS) dienstverlening. Bij het maken en testen van een back-up is het dus van belang regie te houden en van alle onderdelen in de keten of er een reservekopie is die past bij de bedrijfsbelangen en de back-up strategie die de organisatie gekozen heeft.

De benodigde architectuur (bedrijfsarchitectuur, informatiearchitectuur en technische architectuur) moet inzichtelijk zijn om prioriteiten te kunnen stellen bij recovery. Is het inzicht in de relatie tussen architectuurcomponenten en bedrijfsfuncties er niet, dan moet “alles” hersteld worden of zal er tijdens de recovery iteratief blijken welke kritische processen al dan niet functioneren. Bij grote calamiteiten gaat er dan veel tijd verloren terwijl de maatschappelijke behoeften niet kunnen worden ingevuld.

#### Infrastructure as a Service

Gegevens mogen niet verloren raken, omdat daarmee de betrouwbaarheid van de gemeente als organisatie in het geding komt. Om er voor te zorgen dat de kans op een dergelijke calamiteit zeer klein is, is gekozen voor een hoog beschikbaar datacenter met een gespiegelde omgeving. Door gedurende de dag, maar in ieder geval steeds tussen twee werkdagen een reservekopie van gegevens te maken kunnen er nooit meer gegevens verloren raken dan tijdens de werkdag zijn gegenereerd of bijgewerkt. Het maximale dataverlies is daarmee theoretisch 24 uur, maar in de praktijk binnen het datacenter van de hostingpartij beperkt tot een kwartier.

In het (helaas niet ondenkbare) geval dat het datacenter gehackt zou worden, biedt een gespiegeld datacenter niet altijd uitkomst. Dit secundaire datacenter kent in principe dezelfde kwetsbaarheden als het primaire, maar staat op een andere locatie. Secundaire datacentra kunnen met een volledig gespiegelde omgeving of met een “overboekte” opzet worden aangeboden. Een overboekt secundair datacenter bevat wel alle bestanden, maar heeft minder rekenkracht beschikbaar. Er zullen dan ook keuzes moeten worden gemaakt als het primaire datacenter om welke reden dan ook niet beschikbaar is. Deze keuzes kunnen en dienen te worden voorbereid. Door vooraf in een Disaster recovery plan helder te maken welke prioriteiten er gesteld worden, kan het belangrijkste deel van de infrastructuur zsm weer beschikbaar komen.

Indien zowel het primaire als secundaire datacenter gehackt zouden zijn, dan is een off site back-up die niet te wijzigen is (immutable) is in dat geval de enige wijze om in control te blijven en op termijn aan de maatschappelijke en wettelijke plicht te voldoen. Het terugzetten van gegevens uit de back-up zal dan voor een heel datacenter (waarvan de hardware niet beschikbaar is / niet voorbereid is) moeten gebeuren, wat een onvoorspelbare RTO geeft.

#### Disaster Recovery diensten van de hostingpartij (ook wel uitwijk genoemd)

Soms is een goede back-up niet voldoende. Bijvoorbeeld als de infrastructuur of het datacenter waar we gebruik van maken niet beschikbaar is. In dat geval kan een Disaster Recovery omgeving in een gespiegeld datacenter zorgen dat de RPO en RTO veel gunstiger zijn in het secundaire datacenter dan in de situatie waarin alles vanuit de back-up hersteld zou worden. Wel moeten alle netwerkverbindingen worden hersteld en moeten de apparaten van de gebruikers van de organisatie op de juiste plaats uitkomen. Met deze DR omgeving verandert de meerwaarde van de back-up; deze is vooral van belang voor gegevens die beschadigd raken en voor de langere termijn.

Niet in alle scenario’s is een disaster recovery omgeving een oplossing; bijvoorbeeld bij ransomware is een gespiegeld datacenter ook kwetsbaar, omdat het gebouwd is om hetzelfde te doen als het primaire datacenter en dus nagenoeg dezelfde kwetsbaarheden kent. De RTO is beperkt tot enkele uren, maximaal een dag. De RPO is zeer kort, er gaat amper verloren. Maximaal een kwartier aan gegevens.

Met het inrichten van deze oplossing zijn nog keuzes te maken: moet de gespiegelde omgeving meteen beschikbaar zijn, voor alle functionaliteit? Of is het voldoende een voorbereide omgeving te hebben, waarbij de data wel aanwezig is, maar de keuzes voor de (op dat moment) belangrijkste functionaliteiten nog gemaakt moet worden? In dat laatste geval kan een zogenaamde overboekte omgeving een kostentechnisch interessant alternatief zijn. De hersteltijd ligt dan lager dan bij het teruglezen vanuit back-up (de hardware is gegarandeerd beschikbaar (maar slechts voor een beperkt deel van de reguliere capaciteit).

Of er voldoende capaciteit beschikbaar is bij de IaaS dienstverlener om het secundaire datacenter aan de slag te krijgen is de vraag. Er is op dat moment immers een grote calamiteit in het primaire datacenter die bestreden moet worden, én meerdere klanten kunnen daar last van hebben en dus om ondersteuning verlegen zitten.

Een nadeel bij het overcommitted datacenter is dat opschalen van de geleverde rekenkracht lastig zal zijn, omdat de hostingpartner klaarblijkelijk een groot probleem heeft in het primaire datacenter. De impact zal dan groter zijn dan alleen voor de organisatie als klant, waardoor er op korte termijn weinig mogelijkheden zijn om de beschikbare rekenkracht te vergroten.

### Back-up en SaaS/Cloud leverancier

Omdat in het geval van SaaS en Cloud-oplossingen de informatie verwerkt wordt binnen de systemen van de betreffende leverancier moeten er duidelijke afspraken over back-up en recovery gemaakt worden, waarop ook periodiek kan worden getoetst. Dit kunnen afspraken zijn omtrent aantoonbaarheid van:

- Garanties en beschikbaarheid vastgelegd in een SLA (inclusief rapportage);

- Wijze van back-up, omvang en gebruikt medium;

Daarnaast kan wat worden vastgelegd m.b.t.:

- Afspraken over het importeren van back-up informatie in testsystemen;

- Vastgelegde back-up afspraken in de verwerkersovereenkomst;

- Afspraken over recovery;

- Afspraken over het periodiek testen van de effectiviteit van de recovery.

- Afspraken over de beschikbaarheid van back-up bestanden van (off-site) back-up bestanden voor de organisatie als eigenaar van de informatie (alleen de bestandsback-up, niet de systeem back-up)

De SaaS leverancier is niet de eigenaar van de verwerkte gegevens. Dat blijft de organisatie. Daarin willen we niet afhankelijk zijn van de SaaS leverancier, maar regie voeren. Dat vraagt een actieve houding en gelijkwaardigheid in relatie met leverancier. Dit is lastig te realiseren op het moment dat de gegevens niet eigenstandig terug te halen zijn, dan ontstaat er toch een afhankelijkheid.

Heldere afspraken over een back-up waar de organisatie ook toegang toe heeft helpen om deze afhankelijkheid te verkleinen. Deze gegevens zijn niet altijd 1-op-1 toepasbaar in een andere applicaties, het datamodel of de gegevensstructuur kan per applicatie anders zijn waardoor een conversie moet worden gedaan. Als een SaaS leverancier niet (langer) de meerwaarde biedt die de organisatie zoekt, dan is een exit-strategie nodig, in ieder geval voor de applicaties die kritische processen ondersteunen of waar vertrouwelijke gegevens worden verwerkt. Binnen de standaard GIBIT voorwaarden is een leverancier verplicht om mee te werken aan het opstellen en uitvoeren van een exitplan. Deze voorwaarden zijn niet met alle leveranciers zo overeengekomen.

#### SaaS Generiek werkplek (Microsoft)

Voor de generieke werkplek waar alle gebruikers binnen de organisatie gebruik van maken, is Microsoft 365 een belangrijke component. Microsoft garandeert een hoge beschikbaarheid van de software, maar is niet verantwoordelijk voor de inrichting en de data, die is van de klantorganisatie. Microsoft 365 bevat veel functionaliteit en verschillende apps. Per app is het nodig te bepalen wat de bedrijfsfunctie is en wat er onderdeel zou moeten zijn van de back-up. Bedenk daarbij dat de bestandsback-up en de systeem back-up niet hetzelfde zijn; als bestanden in Teams onder water in OneDrive staan en via een synchronisatie op het netwerk (gehost door de hostingpartij) komen te staan, dan worden de bestanden onderdeel van een off-site back-up. De chats, autorisaties en de inrichting van de Teams Site zijn dan geen onderdeel van de back-up.

#### SaaS specifieke bedrijfsfuncties (vakapplicaties)

Voor applicaties voor specifieke bedrijfsfuncties zoals het raadsinformatiesysteem en het zaaksysteem sociaal domein, kan aan de hand van een risico-inventarisatie bekeken worden welke maatregelen er nodig zijn rondom back-up. Het is primair de verantwoordelijkheid van de leverancier, maar omdat de organisatie eigenaar blijft van de gegevens én zekerheid wil hebben over de continuïteit is het nodig hier inzicht in te hebben.

## Recovery

Recovery is het herstel van gegevens, een applicatie of omgeving naar de staat van vóór het incident. Recovery is noodzakelijk na het verloren gaan van een applicatie of gegevens. Voor het herstellen is altijd toestemming nodig van de eigenaar van het systeem of de gegevens.

Bij grotere incidenten, bijvoorbeeld als een database corrupt is geraakt of een ransomware aanval, is altijd overleg nodig met de proces / data eigenaar over de opties én hoe verder herstel kan worden uitgevoerd. De proces eigenaar bepaalt en de ICT-afdeling heeft een adviserende/uitvoerende rol.

Alle recovery operaties dienen te worden gelogd. Deze logging kan gebruikt worden binnen andere beheerprocessen om te bepalen of er bijvoorbeeld andere storingen op komst zijn.

## PDCA

Ook voor een back-up wil je weten of dit blijvend aansluit bij de bedrijfsdoelstellingen. Het gebruik en het belang van (delen van) de IT infrastructuur verandert, en de IT infrastructuur zelf ook. Wat vandaag een prima oplossing is, kan op onderdelen niet meer voldoen naar verloop van tijd. Ook wil je zekerheid hebben dat voor de totale omgeving de back-ups voldoen én betrouwbaar en voorspelbaar (bijvoorbeeld qua doorlooptijd) kunnen worden ingezet voor recovery. Dat betekent dat vraagt een beheersproces, dat bewezen werkt en op basis van actuele inzichten actueel gehouden wordt.

- Afspraken met leveranciers over back-up en recovery worden vastgelegd in contractuele afspraken/SLA-documentatie; wederzijdse en wederkerige afspraken over het testen van het gezamenlijke continuïteitsplan.

- De back-ups van alle gemeentelijke informatie, software en besturingssystemen (en instellingen) moeten worden bewaard, zodat de computer besturingssystemen, applicaties en informatie volledig hersteld kunnen worden in geval van een calamiteit.

- Alle gemeentelijke informatie welke staat op werkstations, laptops of andere draagbare apparaten moeten worden opgeslagen op een netwerk file server om back-up mogelijk te maken;

- Dagelijks worden controles uitgevoerd op basis van de logfiles van de back-up. Mislukte back-ups worden indien mogelijk binnen het back-up window hersteld.

- Vereiste back-up documentatie omvat de identificatie van alle belangrijke gegevens, programma's, documentatie en support items die nodig zijn om essentiële taken tijdens een herstelperiode te voeren. Documentatie van het recoveryproces moet procedures omvatten voor het herstel van single-systeem of applicatiestoringen, alsmede voor een totale datacenter ramp scenario (in geval van uitwijk), indien van toepassing;

- Er zijn geteste ICT-procedures voor back-up en recovery;

- De back-up en recovery procedures moet worden getest conform de documentatie en deze moet regelmatig worden bijgewerkt om rekening te houden met nieuwe technologie, veranderingen in het bedrijf, en de migratie van toepassingen naar alternatieve platforms;

- Recovery procedures moeten minimaal op jaarbasis worden getest;

- Van back-up en recovery activiteiten en de verblijfplaats van de media wordt een logboek bijgehouden;

- De back-ups worden vernietigd meteen na de retentieperiode.

### Back-up plan

Voor de verschillende onderdelen van de IT infrastructuur moet door de beheerder een plan worden opgesteld dat past bij dit beleid. Toetsen en bijstellen aan de hand van de inzichten die uit de beheersactiviteiten naar voren komen hoort daar bij. Voor de IaaS dienstverlening komt het backupplan terug in de Producten en Diensten Catalogus qua keuzemogelijkheden, in de ServiceLevel Agreement voor de gemaakte keuzes en bijbehorende servicenormen en in het Dossier Afspraken en Processen voor de te volgen werkwijze, taakverdeling en verantwoording tussen opdrachtgever en leverancier.

### Controleren en testen back-ups en restore

Back-ups moeten worden gecontroleerd. Binnen het back-up window moeten foutmeldingen worden geanalyseerd en waar mogelijk hersteld. Back-ups dienen regelmatig te worden getest. De restore procedure wordt minimaal jaarlijks getest of na een grote wijziging. Hierbij moet de data-formaat juist zijn en is het van belang te meten dat de tijd die het kost om de data terug te zetten acceptabel is, en dus niet enkele weken duurt voor bijv. kritische systemen.

Het recovery proces moet getest worden. Dat betekent dat de werking van het back-up en recovery proces minimaal jaarlijks aangetoond moet worden door middel van een representatieve en succesvolle hersteltest. De verschillende onderdelen van de IV infrastructuur die geback-upt worden, dienen hier onderdeel van uit te maken. Ook qua omvang moet het dusdanig zijn dat een test wat zegt over de duur van recovery als de totale omgeving zou uitvallen.

### Wijzigingenbeheer

Als onderdeel van wijzigingsbeheer, dient bij projecten met impact op de infrastructuur of veranderingen in de bedrijfsfuncties die worden ondersteund met bepaalde software steeds ook gekeken worden of de risico-inventarisatie hierdoor nog actueel blijft.

Los van bovenstaande triggers om zaken bij te stellen, dient het periodiek actualiseren van het back-up beleid onderdeel uit e maken van de reguliere beleidscyclus van het team IB&P.

## Eigenaarschap

Eigenaarschap is een belangrijke randvoorwaarde om van beleid ook naar een goede invulling te komen. Op het moment dat de IT omgeving gebruik moet maken van de back-up, dan is de hele organisatie én de lokale samenleving daarvan afhankelijk.

Dit RACI-diagram biedt een overzicht van de verdeling van verantwoordelijkheden binnen de

implementatie en handhaving van het netwerkbeveiligingsbeleid van de organisatie. De matrix

identificeert de rollen van verschillende belanghebbenden bij specifieke taken en activiteiten die

essentieel zijn voor een effectieve beveiliging van het netwerk. Hieronder wordt de betekenis van de

gebruikte afkortingen toegelicht:

- R (Responsible): De persoon of groep die verantwoordelijk is voor de uitvoering van een specifieke taak of activiteit.

- A (Accountable): De individuele persoon die uiteindelijk verantwoordelijk is en beslissingsbevoegdheid heeft voor het betreffende onderdeel.

- C (Consulted): Personen of afdelingen die geraadpleegd moeten worden voor input en feedback bij de uitvoering van taken.

- I (Informed): Personen of afdelingen die op de hoogte moeten worden gehouden van de voortgang en resultaten van specifieke taken.

| Activiteit | R | A | C | I |
|---|---|---|---|---|
| Opstellen van Back-up Beleid | IB | CIO |  |  |
| Risicoafweging | Strategisch informatiemanager | CIO |  |  |
| Vaststellen Back-up beleid | MT bedrijfsvoering | Gemeentesecretaris | CIO, IB |  |
| Periodiek toetsen Back-up beleid aan bedrijfsdoelstellingen | Architectuur | CIO |  |  |
| Opstellen Back-up plan centrale infrastructuur | Strategisch informatiemanager | CIO | Team ICT Regie & Processen |  |
| Uitvoeren Back-up plan centrale infrastructuur | Team ICT Regie & Processen | CIO |  |  |
| Opstellen Back-up plan SaaS generieke werkplek | Strategisch informatiemanager | CIO | Functioneel beheer |  |
| Uitvoeren Back-up plan SaaS generieke werkplek | Functioneel beheer | CIO |  |  |
| Opstellen Back-up plan SaaS specifieke bedrijfsapplicatie | Strategisch informatiemanager | Proceseigenaar, CIO | Functioneel beheer |  |
| Uitvoeren Back-up plan SaaS specifieke bedrijfsapplicatie | Functioneel beheer | CIO |  |  |
| Opstellen en bijhouden back-upregister | IB | CIO | Team ICT Regie & Processen, Functioneel beheer |  |
| Besluiten om Recovery toe te passen obv een backup | Systeemeigenaar (CIO of SaaS-leverancier) | Proceseigenaar | Team ICT Regie & Processen, Functioneel beheer | CISO, CIO |
