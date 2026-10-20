# Procedure security classificatie (BIV)

### Afkortingen

| Afkorting | Omschrijving |
|---|---|
| ISO | Information Security Officer |
| B/I/V | Beschikbaarheid, Integriteit, Vertrouwelijkheid |

### Relevante beleidsdocumenten

- Beleid Strategisch IB-beleid

- Procedure risicoanalyse

#### Doelstelling

Deze procedure is opgesteld op de stappen vast te leggen voor het bepalen van de B/I/V-classificatie van informatiesystemen en applicaties. Deze classificatie vormt de basis en de eerste stap in risicomanagement, om risico’s rond beschikbaarheid, integriteit en vertrouwelijkheid van systemen te mitigeren.

#### Scope

Deze procedure is van toepassing op alle gemeenten binnen de organisatie, waaronder de deelnemende gemeenten en het samenwerkingsverband. De scope omvat zowel nieuwe als bestaande applicaties.

Het uitvoeren van een aanvullende risicoanalyse en de selectie van extra beveiligingsmaatregelen vallen buiten de scope van deze procedure. De risicoanalyse wordt behandeld in ‘Procedure Risicoanalyse’.

## Risicomanagement

### Het belang van security classificatie

In de organisatie, waar veel met vertrouwelijke informatie wordt gewerkt, is het beheersen van risico's van groot belang. Het Strategisch IB-beleid vereist dat risicomanagement wordt toegepast in de deelnemende gemeenten en het samenwerkingsverband. Hierbij moeten applicaties worden voorzien van een beveiligingsclassificatie. Voor elke nieuwe en bestaande applicaties is een beveiligingsclassificatie vereist op B/I/V-niveau.

Deze classificatie bepaalt of de huidige beheersmaatregelen voor een systeem voldoende zijn, of dat er een aanvullende risicoanalyse vereist is, waarbij mogelijk extra maatregelen moeten worden getroffen.

Onderstaande flowchart visualiseert het risicomanagementproces:

### Waarom een security classificatie

Een beveiligingsclassificatie is essentieel om de gevoeligheid van informatie in applicaties te beoordelen. Deze classificatie bepaalt welke set beheersmaatregelen nodig is om de risico's die de beschikbaarheid, integriteit en vertrouwelijkheid beïnvloeden, effectief te beheersen.

### Beveiligingsclassificatieproces

Het classificatieproces wordt uitgevoerd samen met de proceseigenaar en een ISO, met gebruik van de B/I/V-vragenlijst welke in de architectuurtool zit. Het resultaat van de classificatie moet worden goedgekeurd door zowel de proceseigenaar als de ISO. De ISO moet ervoor zorgen dat de resultaten correct en volledig worden opgenomen in de architectuurtool.

| # | Processtap | Activiteit | Verantwoordelijkheden |  |
|---|---|---|---|---|
| 1 | Uitvoeren security classificatie | De ISO leidt de uitvoering van de security classificatie en begeleidt de proceseigenaar bij het beantwoorden van de vragen. De ISO helpt en daagt de proceseigenaar uit om in samenwerking tot de best mogelijke invulling te komen | R | ISO |
|  |  |  | A | Proceseigenaar |
|  |  |  | C | - |
|  |  |  | I | CISO |
| 2 | Aftekenen security classificatie | De ISO en de proceseigenaar tekenen de resultaten af. | R | ISO |
|  |  |  | A | Proceseigenaar |
|  |  |  | C | - |
|  |  |  | I | - |
| 3 | Steekproef maatregelen testen | De ISO test door middel van een steekproef of maatregelen correct zijn/worden geïmplementeerd. | R | ISO |
|  |  |  | A | - |
|  |  |  | C | Proceseigenaar |
|  |  |  | I | - |
| 4 | Aanvullende risicoanalyse | Indien de security classificatie aangeeft dat één van de B/I/V-niveaus op ‘hoog’ staat wordt een aanvullende risicoanalyse uitgevoerd. Dit proces wordt verder toegelicht in ‘Procedure risicoanalyse’. | R | ISO |
|  |  |  | A | - |
|  |  |  | C | CISO |
|  |  |  | I | Team IB&P |
| 5 | Herziening security classificatie | De classificatie wordt bij significante wijzigingen herzien. | R | Proceseigenaar |
|  |  |  | A | ISO |
|  |  |  | C | CISO |
|  |  |  | I | Afdelingsmanager |

Verklaring van verantwoordelijkheden:

- R (Responsible): Verantwoordelijk voor de uitvoering van de taak.

- A (Accountable): Eindverantwoordelijk voor de taak en goedkeuring.

- C (Consulted): Moet worden geraadpleegd alvorens een besluit of actie wordt genomen.

- I (Informed): Moet worden geïnformeerd na het nemen van een besluit of actie.

## Security classificatie vragenlijst

De onderstaande vragen dienen als hulpmiddel om het juiste B/I/V-classificatieniveau te bepalen.

### Beschikbaarheid

- Wat is de maximale tijd dat de applicatie of dienst onbeschikbaar mag zijn zonder ernstige gevolgen voor de gemeente of burgers?

- 4 uur

- 1 dag

- 2 dagen

- 1 week

- 2 weken

- Hoeveel gegevensverlies is acceptabel zonder de continuïteit van de dienstverlening te verstoren?

- 4 uur

- 1 dag

- 2 dagen

- 1 week

- 2 weken

- Hoeveel gebruikers of burgers worden direct beïnvloed door de onbeschikbaarheid van de applicatie of dienst?

- Weinig of geen gebruikers (<5% van de gebruikers)

- Een minimaal aantal gebruikers (<20% van de gebruikers)

- Een significant aantal gebruikers (+/- 50% van de gebruikers)

- Een groot aantal gebruikers (<75% van de gebruikers)

- Een zeer groot aantal gebruikers (>75% van de gebruikers)

- Hoe snel moet de data hersteld kunnen worden om de bedrijfscontinuïteit te waarborgen?

- Niet. Het proces draait ook zonder de data

- Minstens gedeeltelijk

- Volledig tot een zekere datum

- Volledig tot een datum op korte termijn

- Volledig tot het moment van onbeschikbaarheid

- Welk percentage prestatieverlies is toelaatbaar zonder grote impact op de gemeente of burgers?

- Tot 100%

- Maximaal 75%

- Maximaal 50%

- Maximaal 25%

- Tot 0%

#### Integriteit

- Wat zijn de gevolgen voor het bedrijfsproces als informatie onjuist of gemanipuleerd is?

- Het bedrijfsproces staat enkele integriteitsfouten toe zonder grote schade

- Schending van integriteit kan enige (in)directe financiële/imago schade toebrengen

- Schending leidt tot grote financiële/imago schade

- Schending van integriteit kan zeer grote financiële/imago schade aanrichten

- Niet van toepassing op deze applicatie

- Welke risico's ontstaan er voor het primaire proces door niet-integere informatie?

- Gebrekkige integriteit heeft geen impact op de primaire dienstverlening

- Veroorzaakt een onderbreking van het primaire proces van max een dag

- Veroorzaakt een onderbreking van het primaire proces van max een week

- Veroorzaakt een onderbreking van het primaire proces van max 1 tot 2 maanden

- Veroorzaakt een onderbreking van het primaire proces die niet te overzien is

- Niet van toepassing op deze applicatie

- Hoe kan gebrekkige informatie-integriteit de reputatie van de gemeente schaden?

- Verlies van publiek respect; klachten van burgers

- Nationale negatieve publiciteit en motivatieverlies onder medewerkers

- Meerdere weken negatieve berichtgeving. Grote financiële schade

- Niet van toepassing op deze applicatie

- Welke juridische gevolgen kunnen voortvloeien uit een gebrek aan informatie-integriteit?

- Geen impact

- Financiële schade voor individuen

- Grote impact. De financiële gevolgen niet meer op te vangen binnen de begroting

- Wat zijn de mogelijke operationele en financiële gevolgen van niet-integere gegevens?

- Irritatie bij medewerkers en/of burgers geventileerd in media/interne negatieve publiciteit

- Juridische of strafrechtelijke vervolging

- Niet van toepassing op deze applicatie

#### Vertrouwelijkheid

- In hoeverre mag de informatie gedeeld worden met derden of binnen de organisatie?

- De informatie is openbaar en mag zonder restricties worden gedeeld

- De informatie kan/mag op verzoek publiek gedeeld worden

- Mag zonder restricties intern worden gedeeld

- Informatie is beperkt tot een kleine groep interne/externe gebruikers

- Verlies of lekken van de informatie heeft een zeer grote impact op de gemeente

- De informatie is als geheim geclassificeerd

- Wat zijn de gevolgen voor de gemeente als vertrouwelijke informatie onrechtmatig wordt vrijgegeven?

- Geen impact

- De potentiële schade is beperkt (beperkte imago schade)

- De potentiële schade is aanzienlijk (imago schade)

- Financiële gevolgen zijn groot

- Is de informatie van vertrouwelijke aard en vereist deze extra bescherming?

- Ja

- Nee

- Is de informatie geheim?

- Ja

- Nee

- Leidt het openbaar maken van de informatie tot politieke schade?

- Ja

- Nee

- Betekent openbaarmaking, verlies van publiek respect; imago schade, klachten van burgeres of significant verlies van motivatie van medewerkers?

- Ja

- Nee

## Classificatiebeoordeling

De resultaten van de security classificatie vragenlijst worden gebruikt om een algehele B/IV/-score te bepalen. De onderstaande niveaus zijn van toepassing:

Score Beschikbaarheid

De mate waarin informatie en systemen toegankelijk zijn voor bevoegde gebruikers wanneer dat nodig is.

- Niet zeker: De gegevens kunnen zonder gevolgen langere tijd niet beschikbaar zijn. Schending van beschikbaarheid heeft geen gevolgschade.

- Belangrijk: De informatie of het systeem is belangrijk, en onbeschikbaarheid kan leiden tot enige verstoring van de bedrijfsprocessen, maar de organisatie kan nog-steeds functioneren. De informatie of service mag incidenteel uitvallen, het bedrijfsproces staat incidentele uitval toe. De continuïteit zal op redelijke termijn moeten worden hervat. Schending van beschikbaarheid kan enige (in)directe schade toebrengen.

- Noodzakelijk: De informatie of service mag bijna nooit uitvallen, het bedrijfsproces staat nauwelijks uitval toe. De continuïteit zal snel moeten worden hervat. Schending van beschikbaarheid kan serieuze (in)directe schade toebrengen.

- Essentieel: De informatie of dienst mag alleen in zeer uitzonderlijke situaties uitvallen, bijvoorbeeld als gevolg van een calamiteit, het bedrijfskritische bedrijfsproces staat eigenlijk geen uitval toe. De continuïteit zal zeer snel moeten worden hervat.

Score Integriteit

De zekerheid dat informatie accuraat, compleet en ongewijzigd is, en dat systemen op de juiste manier functioneren.

- Verwaarloosbaar: Deze informatie mag worden veranderd. Geen extra bescherming van integriteit noodzakelijk. Schending van integriteit heeft geen gevolgschade.

- Gering: Het bedrijfsproces dat gebruik maakt van deze informatie staat enkele (integriteits-) fouten toe. Een basisniveau van beveiliging is noodzakelijk. Schending van integriteit kan enige (in-)directe schade toebrengen.

- Ernstig: Het bedrijfsproces dat gebruik maakt van deze informatie staat zeer weinig (integriteits-)fouten toe. Bescherming van integriteit is absoluut noodzakelijk. Schending van integriteit kan serieuze (in)directe schade toebrengen.

- Desastreus: Het Bedrijfsproces dat gebruik maakt van deze informatie staat geen (integriteits-) fouten toe. Schending van integriteit kan (zeer) grote schade toebrengen.

Score Vertrouwelijkheid

De bescherming van informatie tegen ongeautoriseerde toegang of openbaarmaking.

- Openbaar: Alle informatie die algemeen toegankelijk is voor iedereen. Er is geen schending van vertrouwelijkheid mogelijk.

- Intern: Informatie die toegankelijk mag of moet zijn voor alle medewerkers van de eigen organisatie(s). Vertrouwelijkheid is gering. Schending van vertrouwelijkheid kan enige (in)directe schade toebrengen.

- Vertrouwelijk: Informatie die alleen toegankelijk mag zijn voor een beperkte groep gebruikers. De informatie wordt ter beschikking gesteld op basis van vertrouwen. Schending van vertrouwelijkheid kan serieuze (in)directe schade toebrengen.

- Geheim: Dit betreft gevoelige informatie die alleen toegankelijk mag zijn voor de direct geadresseerde. Schending van vertrouwelijkheid kan zeer grote schade toebrengen.
