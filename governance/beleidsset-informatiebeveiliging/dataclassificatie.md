# Beleid dataclassificatie

### Afkortingen

| Afkorting | Omschrijving |
|---|---|
| AVG | Algemene Verordening Gegevensbescherming |
| BBN | Basis Beveiligings Niveau |
| BIO | Baseline Informatieveiligheid Overheid |
| BIV | Beschikbaarheid, Integriteit, Vertrouwelijkheid |
| GAP analyse | Nulmeting waarbij inzichtelijk wordt welke beveiligingsmaatregelen er nog niet of onvoldoende zijn genomen |
| IBD | Informatie Beveiligings Dienst |
| ISO | Information Security Officer - Informatiebeveiliger |
| CISO | Chief Information Security Officer |

### Relevante beleidsdocumenten:

- Strategisch IB-beleid

- Baselinetoets

- GAP analyse

- Beleid testdata

## Inleiding

Dit document maakt deel uit van de operationalisering van het strategisch informatiebeveiligingsbeleid. Het regionale informatiebeveiligingsbeleid is gebaseerd op de BIO die per 1 januari 2020 in werking is getreden als normenkader voor informatieveiligheid binnen de overheid. Dit document is gebaseerd op de handreiking van de IBD voor dataclassificatie versie 2.1 ontwikkeld ter ondersteuning van de gemeenten.

### Doelstelling

Classificatie is het toekennen van een beveiligingsniveau aan data met als doel passende maatregelen te kunnen treffen. Classificatie van data maakt inzichtelijk welke betrouwbaarheidseisen van toepassing zijn en aansluitend welke maatregelen genomen moeten worden om die data adequaat te beschermen.

Dit document biedt een methodiek om snel een indicatie te krijgen van het belang van data die verwerkt wordt in informatiesystemen en is daarmee een basis voor een risicoanalyse. Na de classificatie kunnen de juiste maatregelen getroffen worden waardoor enerzijds inbreuken op de betrouwbaarheid worden geminimaliseerd en anderzijds daarvoor niet nodeloos veel inspanning benodigd is. Data betekent in dit verband alle gegevens, ongeacht het medium waarop deze opgeslagen worden en ongeacht de presentatie daarvan. Voor het classificeren van processen en systemen wordt de ‘Baselinetoets’ gebruik, een ander operationeel product van de IBD.

### Relatie met de BIO

De BIO ondersteunt de dataclassificatie met een set van maatregelen waarmee data passend beschermd kan worden. Met de BIO wordt op basis van een risicoanalyse een niveau van beveiliging bepaald. Het uitgangspunt is echter een wezenlijk andere. De dataclassificatie richt zich op informatie in informatiesystemen (“bottom-up”) terwijl de BIO zich richt op bedrijfsprocessen en systemen (“top-down”). Desalniettemin is het mogelijk dat enige overlap ontstaat waarbij de uitkomsten van zowel de dataclassificatie als de bepaling van de basisbeveiligingsniveau’s (BBN’s) over het algemeen zullen overeenkomen.

## Classificatie van data

Het informatiebeveiligingsbeleid van de gemeente beschrijft globaal de normen voor het waarborgen van de beschikbaarheid, integriteit en vertrouwelijkheid van informatie. Hier wordt tevens de relatie gelegd naar het BBN niveau van de BIO.

De te onderscheiden niveaus van beschikbaarheid zijn:

- Niet nodig (0): De gegevens kunnen zonder gevolgen langere tijd niet beschikbaar zijn. Schending van beschikbaarheid heeft geen gevolgschade.

- Belangrijk (BBN1): De informatie of service mag incidenteel uitvallen, het bedrijfsproces staat incidentele uitval toe. De continuïteit zal op redelijke termijn moeten worden hervat. Schending van beschikbaarheid kan enige (in)directe schade toebrengen

- Noodzakelijk (BBN2): De informatie of service mag bijna nooit uitvallen, het bedrijfsproces staat nauwelijks uitval toe. De continuïteit zal snel moeten worden hervat. Schending van beschikbaarheid kan serieuze (in)directe schade toebrengen.

- Essentieel (BBN2 met aanvullende risicoanalyse): De informatie of service mag alleen in zeer uitzonderlijke situaties uitvallen, bijvoorbeeld als gevolg van een calamiteit, het bedrijfskritische bedrijfsproces staat eigenlijk geen uitval toe. De continuïteit zal zeer snel moeten worden hervat. Schending van beschikbaarheid kan (zeer) grote schade toebrengen.

De onderscheiden niveaus van integriteit zijn:

- Niet zeker (0): Deze informatie mag worden veranderd. Geen extra bescherming van integriteit noodzakelijk. Schending van integriteit heeft geen gevolgschade.

- Beschermd (BBN1): Het bedrijfsproces dat gebruik maakt van deze informatie staat enkele (integriteits-) fouten toe. Een basisniveau van beveiliging is noodzakelijk. Schending van integriteit kan enige (in-)directe schade toebrengen

- Hoog (BBN2): Het bedrijfsproces dat gebruik maakt van deze informatie staat zeer weinig (integriteits-)fouten toe. Bescherming van integriteit is absoluut noodzakelijk. Schending van integriteit kan serieuze (in)directe schade toebrengen.

- Absoluut (BBN2 met aanvullende risicoanalyse): Het bedrijfsproces dat gebruik maakt van deze informatie staat geen (integriteits-)fouten toe. Schending van integriteit kan (zeer) grote schade toebrengen

De onderscheiden niveaus van vertrouwelijkheid zijn:

- Openbaar (0): Alle informatie die algemeen toegankelijk is voor iedereen. Er is geen schending van vertrouwelijkheid mogelijk.

- Bedrijfsvertrouwelijk (BBN1): Informatie die toegankelijk mag of moet zijn voor alle medewerkers van de eigen organisatie(s). Vertrouwelijkheid is gering. Schending van vertrouwelijkheid kan enige (in)directe schade toebrengen.

- Geheim (BBN2): Informatie die alleen toegankelijk mag zijn voor een beperkte groep gebruikers. De informatie wordt ter beschikking gesteld op basis van vertrouwen. Schending van vertrouwelijkheid kan serieuze (in)directe schade toebrengen.

- Geheim (BBN3): Dit betreft gevoelige informatie die alleen toegankelijk mag zijn voor de direct geadresseerde. Schending van vertrouwelijkheid kan zeer grote schade toebrengen. Weerstand tegen statelijke actoren noodzakelijk. Let wel: statelijke actoren kan binnen de gemeentelijke context vertaald worden naar georganiseerde misdaad en ondermijning

## Principes voor classificatie

De volgende principes zijn het uitgangspunt voor (data)classificatie:

- De classificatietabel heeft betrekking op alle in beheer zijnde gegevensverzamelingen, gegevensdragers, informatiesystemen, servers en netwerkcomponenten.

- Data kan meer of minder gevoelig of kritisch zijn. Voor bepaalde data kan een extra niveau van bescherming of een speciale verwerking nodig zijn. Als een informatiesysteem daarvoor maatregelen (applicatie controles) genomen heeft om delen van de systeeminformatie die hoger geclassificeerd is adequaat te beschermen op record of schermniveau, dan kan een systeem als geheel lager ingeschaald worden binnen de tabel.

- Bedenk bij classificeren ook wie belang zou kunnen hebben bij de data, dit bepaalt ook welke middelen ingezet kunnen worden om de bescherming te doorbreken.

- De data-eigenaar (veelal ook de proceseigenaar) bepaalt het vereiste beschermingsniveau (classificatie). Indien sprake is van wettelijke eisen wordt dit expliciet aangegeven. De data-eigenaar bepaalt tevens wie toegang krijgt tot welke gegevens.

- Er wordt gestreefd naar een zo ‘laag’ mogelijk classificatieniveau; te hoge classificatie leidt namelijk tot onnodige kosten. Bovendien dient data in beginsel voor zoveel mogelijk mensen beschikbaar zijn in het kader van een transparante overheid.

- Het object van classificatie is data. De classificatie die door het soort data bepaald wordt geldt ook voor het hogere niveau van informatiesystemen (of informatieservices), dat wil zeggen dat als een systeem geheime informatie verwerkt het hele systeem als geheim wordt aangemerkt tenzij voor dat hogere niveau maatregelen genomen zijn binnen het informatiesysteem. Alle classificaties van alle bedrijfskritische systemen zijn centraal vastgelegd door de eigenaren en dienen jaarlijks gecontroleerd te worden door de CISO.

In alle gevallen kan de eigenaar van de gegevens zich voor het classificeren laten ondersteunen door beveiligingsspecialisten, zoals de ISO of de CISO.

## Beveiligingseisen per classificatieniveau

Classificeren is geen exacte wetenschap. Bepaling van het classificatieniveau volgt uit een risicobeoordeling waarin de 'waarde' van informatie wordt bepaald. Aangezien 'waarde' lang niet altijd meetbaar is, is toekenning van een classificatieniveau soms arbitrair. In die gevallen kan een afweging gemaakt worden tussen de waarde en het risico van verlies van data. Het classificatieniveau en de daarbij behorende beveiligingseisen en maatregelen moet altijd 'passen' bij het te beschermen gegeven. De vraag is natuurlijk: wat is een 'passende' maatregel?

Artikel 32 AVG noemt criteria die bij de keuze van de te nemen technische en organisatorische maatregelen gebruikt moeten worden:

- De stand der techniek: Hierbij wordt allereerst vastgesteld welke technische maatregelen op dat moment beschikbaar zijn; Ten aanzien van de aanwezige voorzieningen geldt dat achterhaalde technieken niet langer als passend geclassificeerd kunnen worden;

Dit betekent dat een verantwoordelijke bij het bepalen van de te nemen technische maatregelen een afstemming moet vinden tussen de technische faciliteiten die in gebruik zijn bij de verwerking en die in gebruik zijn bij de beveiliging van persoonsgegevens;

De verantwoordelijke moet deze analyse periodiek herhalen.

- Uitvoeringskosten Hier moet de verantwoordelijke een keuze maken tussen de mogelijke technische en organisatorische maatregelen: in alle redelijkheid moet worden afgewogen of er een evenredigheid bestaat tussen de kosten van de beveiliging en het effect daarvan voor de beveiliging van persoonsgegevens; De risico's die de verwerking met zich meebrengen (rekening houdend met aard, omvang, context van verwerking) Hier wordt vastgesteld welk risico de betrokkene c.q. De verantwoordelijke lopen bij verlies of onrechtmatige verwerking van persoonsgegevens: naarmate het risico toeneemt zullen de maatregelen evenredig verzwaard worden.

Daarnaast bevat de BIO drie basisbeveiligingsniveau ’s die door het bepalen van het classificatieniveau aangeven welke controls en verplichte maatregelen van toepassing zijn. Aanvullend kan met de ISO 27002 bepaald worden op welke wijze de geselecteerde controls geïmplementeerd kunnen worden.

### Beschikbaarheid

Beschikbaarheid stelt in tegenstelling tot integriteit en vertrouwelijkheid geen eisen aan de inhoud van de data. Er gelden daarom geen bijzondere maatregelen voor authenticatie, autorisatie, monitoring en beveiliging, zoals voor integriteit en vertrouwelijkheid (zie volgende paragrafen). Aangezien de normen voor beschikbaarheid verschillen per service moet het classificatieniveau voor beschikbaarheid altijd worden gespecificeerd. De BIO geeft voor beschikbaarheid maatregelen aan tot het niveau ‘noodzakelijk’.

#### 4.1.1. Definitie

Beschikbaarheid is gedefinieerd de mate waarin informatie beschikbaar en toegankelijk is voor geautoriseerde gebruikers. Beschikbaarheid wordt gemeten aan de hand van de Mean Time Between Failures (MTBF). Dit is de gemiddelde tijd tussen het herstel van het ene incident en het optreden van het volgende incident.

| Klasse Belangrijk (Laag) (BBN1 beschikbaarheidsmaatregelen) |  |  |
|---|---|---|
| Werktijden | Van 08:00 tot 17:00 uur op maandag t/m vrijdag behoudens algemeen erkende feestdagen. |  |
| Beschikbaarheid tijdens werktijd | 99,6% | (min.) |
| Beschikbaarheid buiten werktijd | 96,1% | (min.) |
| MTBF | 100 dagen | (min.) |
| MTTR (voor storingen langer dan 3 minuten) | 4 uur | (max.) |

| Klasse Noodzakelijk (Midden) (BBN2 beschikbaarheidsmaatregelen) |  |  |
|---|---|---|
| Werktijden | Van 07:00 tot 21:00 uur op maandag t/m vrijdag behoudens algemeen erkende feestdagen. |  |
| Beschikbaarheid tijdens werktijd | 99,6% | (min.) |
| Beschikbaarheid buiten werktijd | 96,1% | (min.) |
| MTBF | 100 dagen | (min.) |
| MTTR (voor storingen langer dan 3 minuten) | 4 uur | (max.) |

| Klasse Essentieel (Hoog) (BBN2 beschikbaarheidsmaatregelen en risicoanalyse noodzakelijk voor specifieke maatregelen) |  |  |
|---|---|---|
| Werktijden | 24 uur per dag, 7 dagen per week, behoudens gepland onderhoud. |  |
| Beschikbaarheid | 99,9% | (min.) |
| MTBF | 200 dagen | (min.) |
| MTTR (voor storingen langer dan 3 minuten) | 4 uur | (max.) |

Tabel 1 Uitwerking beschikbaarheidsniveaus

### Integriteit

Het onderwerp integriteit valt normaliter in twee delen uiteen: de integriteit van datacommunicatie en opslag enerzijds (d.w.z. niet gerelateerd aan het gemeentelijke proces zelf), en de integriteit van de informatie in de applicaties of fysiek (d.w.z. gerelateerd aan het gemeentelijke proces zelf). Integriteit gekoppeld aan de applicatie is altijd afhankelijk van de situatie en de eisen van een specifiek proces. Voor de functionele integriteit van de informatievoorziening wordt een minimale set van normen opgesteld waarbij er per dienst en/of applicatie nadere afspraken gemaakt kunnen worden.

#### 4.2.1. Definitie

Integriteit geeft de mate aan waarin de informatie actueel en correct is. Kenmerken zijn juistheid, volledigheid en tijdigheid van de transacties.

#### 4.2.2. Beveiligingsmaatregelen

Tabel 2 beschrijft de beveiligingseisen (en -maatregelen) per classificatieniveau, onderverdeeld in eisen voor authenticatie, autorisatie, monitoring en beveiliging. In tabel 2 zijn een aantal voorbeeldmaatregelen weergegeven. De GAP-analyse BIO bevat eveneens kolommen voor de cotrols op beschikbaarheid, integriteit en vertrouwelijkheid, deze kunnen ook gebruikt worden om vast te stellen welke beveiligingsmaatregelen noodzakelijk zijn bij een bepaalde integriteit dataclassificatie.

| Niveau | Authenticatie | Autorisatie | Monitoring | Beveiliging |
|---|---|---|---|---|
| Niet zeker (0) | Geen | Geen | Geen | Geen |
| Laag (BBN1) | Authenticatie ‘basis’ vereist. | Autorisatie vereist. | Vastleggen authenticatie (correct en foutief) en tijdstip. Vastleggen relevante input en output van een ICT-systeem of service. Monitoringsgegevens bewaren voor periode van minimaal 1/2 jaar. | Invoervalidatie. Controleren op mutatie tijdens transport. Transportbeveiliging of berichtbeveiliging. Versie van gebruikte gegevens is bekend. Na uitvoering van een service blijven gewijzigde gegevens consistent. |
| Midden (BBN2) | Authenticatie ‘midden’ vereist. | Autorisatie vereist. 4-ogen principe vereist. | Vastleggen authenticatie (correct en foutief) en tijdstip. Vastleggen relevante input en output van een ICT-systeem of service. Monitoringsgegevens bewaren voor periode van minimaal 2 jaar of langer bij een vermoed beveiligingsincident. | Invoervalidatie. Controleren op mutatie tijdens transport. Berichtbeveiliging. Versie van gebruikte gegevens is bekend. Wijzigingen alleen op bron. Na uitvoering van een service blijven gewijzigde gegevens consistent. |
| Hoog (BBN3 met aanvullende risicoanalyse) | Authenticatie ‘hoog’ vereist. Geen SSO toegestaan. | Autorisatie vereist. 4-ogen principe vereist. | Vastleggen authenticatie (correct en foutief) en tijdstip. Vastleggen relevante input en output van een ICT-systeem of service. Monitoringsgegevens bewaren voor periode van minimaal 3jaar bij een vermoed beveiligingsincident. Vastleggen oude staat van te wijzigen gegevens. | Invoervalidatie. Controleren op mutatie tijdens transport. Berichtbeveiliging. Gegevens worden niet buiten hun bron opgeslagen (behalve voor beschikbaarheid) en niet buiten hun bron gewijzigd. Na uitvoering van een service blijven gewijzigde gegevens consistent. |

Tabel 2 Classificatieniveau integriteit in relatie tot authenticatie, autorisatie, monitoring en beveiliging

De authenticatieniveaus verwijzen naar het vereiste beveiligingsmechanisme:

- Basis (1 factor): authenticatie gebaseerd op iets wat men weet (naam/wachtwoord).

- Midden (2 factor): authenticatie gebaseerd op iets wat men weet en iets wat men heeft (bijv. een token, smartcard of certificaat).

- Hoog (3 factor): authenticatie gebaseerd op eigenschap, bijvoorbeeld irisscan of vingerafdruk, iets wat men heeft en iets wat men weet, dus een combinatie van 3 eigenschappen.

De autorisatieniveaus verwijzen naar de wijze waarop de controle wordt uitgevoerd. Vanaf ‘beschermd’ is altijd autorisatie verplicht en vanaf ‘hoog’ komt daar het 4-ogen principe bij. Het 4-ogen principe bestaat uit één persoon die vastlegt en één persoon die fiatteert.

Bij monitoring van de niveaus ‘beschermd’ en ‘hoog’ wordt de term ‘relevant’ gebruikt. Welke gegevens ‘relevant’ zijn, is ter beoordeling van de eigenaar. Voorbeelden en richtlijnen voor relevante gegevens zijn stamgegevens (gegevens waarop andere gegevens gebaseerd zijn), gegevens in basis- en kernregistraties, privacygevoelige informatie en gegevens beschermd door wet- en regelgeving.

Bij datatransport is berichtbeveiliging te prefereren boven transportbeveiliging. Echter, transportbeveiliging kan in bepaalde gevallen eenvoudiger en/of goedkoper te implementeren zijn. Daarom is bij classificatieniveau ‘beschermd’ de keuze voor transportbeveiliging en berichtbeveiliging open gelaten. Bij ‘hoog’ en ‘absoluut’ is de classificatie zodanig dat berichtbeveiliging toegepast moet worden.

### Vertrouwelijkheid

#### 4.3.1. Definitie

Vertrouwelijkheid is het kwaliteitsbegrip waaronder privacybescherming, maar ook de exclusiviteit van informatie, gevangen kan worden. Het waarborgt dat alleen geautoriseerde gebruikers toegang krijgen.

Vertrouwelijke gegevens zijn bijvoorbeeld:

- Persoonsgegevens

- Gemeentelijke- en bedrijfsgeheimen

- Concurrentiegevoelige gegevens zoals voorbereidingen voor bestemmingsplannen

- Medische gegevens

#### 4.3.2. Beveiligingsmaatregelen

Tabel 3 beschrijft voorbeelden van beveiligingseisen (en maatregelen) per classificatieniveau, onderverdeeld in eisen voor authenticatie, autorisatie, monitoring en beveiliging. De GAP-analyse BIO bevat eveneens kolommen voor de controls op beschikbaarheid, integriteit en vertrouwelijkheid, deze kunnen ook gebruikt worden om vast te stellen welke beveiligingsmaatregelen noodzakelijk zijn bij een bepaalde vertrouwelijkheid dataclassificatie. In de BIO is de vertrouwelijkheid en het bij BBN3 het belang voor externe statelijke actoren leidend om te komen tot BBN3. Voor gemeenten heeft dit meestal tot gevolg dat de niveaus uit de onderstaande tabel als volgt vertaald kunnen worden naar een BBN niveau:

- Bedrijfsvertrouwelijk -> BBN1

- Geheim -> BBN2

- Geheim en aanvullende beveiliging noodzakelijk tegen statelijke actoren -> BBN3

| Niveau | Authenticatie | Autorisatie | Monitoring | Beveiliging |
|---|---|---|---|---|
| Openbaar (0) | Geen | Geen | Geen | Geen |
| Bedrijfs- vertrouwelijk (laag) (BBN1) | Authenticatie ‘basis’ vereist. Sessie time-out na 15 min inactiviteit. Voor klant absolute sessie time-out na 120 min. Identiteit blokkeren na 10 achtereenvolgende foutieve authenticatiepogingen. Authenticatie ‘basis’ nodig voor deblokkeren. | Autorisatie vereist (lid van organisatie). | Vastleggen herhaaldelijk foutieve authenticatie en tijdstip. Monitoringsgegevens bewaren voor periode van minimaal 1/2 jaar. | Uitvoervalidatie. Versleuteling tijdens transport buiten netwerk van de gemeente via transportbeveiliging of berichtbeveiliging. Kopieën van gegevens moeten net zo goed beveiligd worden. Gegevens uit productieomgeving worden niet gebruikt in OTA-omgevingen tenzij deze zijn geanonimiseerd en de gegevenseigenaar toestemming heeft gegeven. |
| Geheim (Midden) (BBN2) | Authenticatie ‘midden’ vereist. Sessie time-out na 15 min inactiviteit. Voor klant absolute sessie time-out na 120 min. Identiteit blokkeren na 10 achtereenvolgende foutieve authenticatiepogingen. Authenticatie ‘midden’ nodig voor deblokkeren. | Autorisatie vereist (specifieke rol). | Vastleggen herhaaldelijk foutieve authenticatie en tijdstip. Monitoringsgegevens bewaren voor periode van minimaal 2 jaar. | Uitvoervalidatie. Versleuteling tijdens transport en op tussenstations binnen en buiten netwerk van de gemeente via berichtbeveiliging. Kopieën van gegevens moeten minimaal net zo goed beveiligd worden. Aantal kopieën minimaliseren. Berichtbeveiliging. Gegevens uit productieomgeving worden niet gebruikt in OTA-omgevingen tenzij deze zijn geanonimiseerd en de gegevenseigenaar toestemming heeft gegeven. |
| Geheim, statelijke actoren (Hoog) (BBN3) | Deze maatregelen komen in een aanvulling op de BIO later beschikbaar |  |  |  |

Tabel 3 Classificatieniveau vertrouwelijkheid in relatie tot authenticatie, autorisatie, monitoring en beveiliging

De authenticatie niveaus verwijzen naar het vereiste beveiligingsmechanisme (zie voorgaande paragraaf). Bedrijfsvertrouwelijk verwijst naar de ‘organisatie’, waarmee wordt bedoeld: de Gemeente, een deelgemeente of een dienst. Zie voor bewaartermijnen ook de ontwerpselectielijst voor archiefbescheiden van VNG.

## Bepalen van classificatieniveaus

In de voorgaande hoofdstukken is de context beschreven die van belang is bij het toekennen van classificatieniveaus: wet- en regelgeving, beleidsuitgangspunten, architectuurprincipes, BIV-classificatieniveau, dreigingsprofiel en het basisbeveiligingsniveau. Met deze kennis kan data geclassificeerd gaan worden. In dit hoofdstuk zijn de te doorlopen stappen uitgewerkt.

### Stap 1: Wettelijke eisen

De eerste stap bij dataclassificatie is nagaan welke wet- en regelgeving mogelijk eisen stelt aan gebruik, distributie en opslag van data.

In veel gevallen zijn er eisen t.a.v. beschikbaarheid, integriteit en vertrouwelijkheid in de wetten opgenomen. Hier dient men rekening te houden met de classificatie van data. Voorbeelden zijn de BAG en de BRP die totaal verschillende eisen stellen aan vertrouwelijkheid van gegevens.

Een ander voorbeeld is de AVG , die zal moeten worden opgevolgd als er sprake is van persoonsgegevens.

### Stap 2: Verantwoordelijkheden t.a.v. data

De eigenaar van de gegevens is verantwoordelijk voor de classificatie. Bij het classificeren kan de eigenaar van de gegevens de hulp inroepen van de verantwoordelijk functioneel beheerder en de persoon die belast is met de rol van ISO of CISO.

### Stap 3: Analyse kritische bedrijfsprocessen

Classificatieniveaus zijn afgeleid van de waarde van data en het belang van het bedrijfsproces waarin deze data een rol speelt. Stel daarom vast wat het belang is van de processen voor de organisatie en hoe deze processen worden ondersteund door de ICT-voorzieningen.

De analyse wordt uitgevoerd met de modelvragenlijsten uit baselinetoets. Deze vragenlijsten geven direct het gewenste classificatieniveau voor beschikbaarheid, integriteit en/of vertrouwelijkheid van data.

In het kader van reproduceerbaarheid en voor bijvoorbeeld auditpartijen die achtergrondgegevens vragen, maar ook om vergelijkingen mogelijk te maken bij toekomstige her classificatie, wordt sterk aanbevolen om de ingevulde vragenlijsten te archiveren als systeem documentatie.

In het kader van de BIO heeft de IBD Gemma referentie componenten en een aantal bedrijfsfuncties geclassificeerd op basis van de BIO. Deze hele lijst is ingelezen in de architectuurtool en kan gebruikt worden als leidraad bij een eerste classificatie.

### Stap 4: Het resultaat

Het resultaat van de analyse vertaalt zich in een classificatierapport (bijlage 2) met daarbij de ingevulde vragenlijsten als bijlagen.

Bijlage 1: Classificatie leidraad

Het classificatieproces wordt ondersteund door een drietal vragenlijsten, waarmee de impact op het bedrijfsproces wordt bepaald:

• Vragen over beschikbaarheid

• Vragen over integriteit

• Vragen over vertrouwelijkheid

De impact op het bedrijfsproces wordt beoordeeld op basis van de volgende 4-puntsschaal:

0. Verwaarloosbare schade

1. Belangrijke schade

2. Ernstige schade

3. Bedreigt het voortbestaan van de gemeente

Vanuit de impact op de bedrijfsproces beoordelingen (4-puntsschaal) kan een vertaling gemaakt worden naar de 4-puntsschaal die gebruikt wordt voor de BIV-classificatie.

Voor de classificatie naar de inzichten integriteit en vertrouwelijkheid is de vertaling in tabel 4 weergegeven.

Voor de beschikbaarheid is deze verdeling niet zo direct te leggen, maar de impact beoordeling die daaruit komt geeft over het algemeen voldoende aanknopingspunt om een classificatie naar belangrijk, noodzakelijk en essentieel te maken.

| Bedrijfsproces impact | B-classificatie | I-classificatie | V-classificatie |
|---|---|---|---|
| 0 | 0 – Niet zeker | 0 – Niet zeker | 0 - Openbaar |
| 1 | 1 – Laag (BBN1) | 1 – Laag (BBN1) | 1 – Bedrijfsvertrouwelijk (BBN1) |
| 2 | 2 – Midden (BBN2) | 2 – Midden (BBN2) | 2 – Geheim (BBN2) |
| 3 | 3 – Hoog (BBN2 + aanvullend) | 3 – Hoog (BBN2 + aanvullend) | 3 – Geheim (BBN3) |

Tabel 4 vier-puntsschaal voor impact op bedrijfsproces vertaald naar integriteit en vertrouwelijkheid

Bijlage 2: Classificatierapport

Deze bijlage kan als apart document gebruikt worden en als basis dienen om de classificaties vast te stellen. Vul onderstaande gegevens in.

| Document eigenaar |  |
|---|---|
| Functie |  |
| Organisatieonderdeel |  |
| Telefoonnummer |  |
| Laatste datum invullen |  |

Het resultaat van het onderzoek voor wat betreft de BIV- aspecten voor het proces <procesnaam> van de gemeente <naam gemeente> geeft een inschaling op de volgende niveaus:

Beschikbaarheid :

Integriteit :

Vertrouwelijkheid :

<Gebruik voor een verklaring van de resultaten, de waardes van de BIV waardering, de verklarende toelichting uit hoofdstuk 3 ‘Beleidskaders voor classificatie’ uit dit document. Dat maakt het advies leesbaarder en begrijpelijker voor niet informatiebeveiligers.>

Conclusie: Het proces <procesnaam> kent het basisbeveiligingsniveau:

Is er een motivatie om af te wijken van de conclusie (door de data-eigenaar)?

Indien er een afwijking is, verklaart de data-eigenaar dat hij het rest risico accepteert.

Aldus opgemaakt d.d.

Naam Eigenaar
