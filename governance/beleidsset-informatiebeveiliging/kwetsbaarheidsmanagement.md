# Beleid kwetsbaarheidsmanagement

### Afkortingen

| Afkorting | Omschrijving |
|---|---|
| BIO | Baseline Informatiebeveiliging Overheid |
| IBD | Informatiebeveiligingsdienst |
| DNB | De Nederlandsche Bank |
| ATP | Advanced Persistent Threat |
| CISO | Chief Information Security Officer |
| IV | Informatievoorziening |
| RACI | Responsible Accountable Consulted Informed |

### Relevante beleidsdocumenten

## Inleiding

Het Beleid Kwetsbaarheidsmanagement van de organisatie is opgesteld met als doel de principes en richtlijnen vast te stellen die nodig zijn om technische kwetsbaarheden op een effectieve en efficiënte manier te beheren binnen alle functionerende systemen van de organisatie.

Dit beleid is gebaseerd en vormgegeven op basis van de eisen en principes van de volgende raamwerken: de Baseline Informatiebeveiliging Overheid (BIO), de Informatiebeveiligingsdienst (IBD) en de Good Practices van De Nederlandsche Bank (DNB).

### 1.1 Doel

Het doel van dit beleid is om de vereisten voor het management van kwetsbaarheden van de organisatie te bepalen. Het management van kwetsbaarheden is noodzakelijk om te zorgen dat kwetsbaarheden in netwerken en systemen van de organisatie worden gedetecteerd en dat er passende acties worden ondernomen om een veilige infrastructuur te waarborgen.

### 1.2 Doelstellingen

Het beleid heeft als doelstellingen dat de volgende fases van kwetsbaarheidsmanagement duidelijk zijn gedefinieerd en dat bijbehorende acties duidelijk zijn voor de bijbehorende uitvoerders en verantwoordelijken:

- Identificatie van kwetsbaarheden

- Classificatie van kwetsbaarheden

- Documentatie van kwetsbaarheden

- Implementatie van tegenmaatregelen

- Verificatie van tegenmaatregelen

### 1.3 Toepassingsgebied van het document

Dit beleid is van toepassing op alle medewerkers, dienstenleveranciers en externe partijen die betrokken zijn bij het beheer en het gebruik van IT diensten onder de organisatie. IT-diensten omvatten zowel die diensten die eigendom zijn van, worden bediend, onderhouden en gecontroleerd door de organisatie, als door een derde partij waarbij de geleverde dienst van invloed is op de vertrouwelijkheid, integriteit en/of beschikbaarheid en algemene beveiliging van de organisatie-gegevens en/of -systemen.

Dit omvat:

- Netwerkapparaten (firewalls, routers, switches, load balancers, andere netwerkapparaten),

- Servers (zowel fysiek als virtueel, met besturingssystemen, applicaties, databases en gegevens die erop staan)

- Cloud-aanbieders

- Applicaties en

- Alle andere IT-processen of apparatuur die kunnen worden aangevallen.

## Beleidsvereisten

### 2.1 Identificatie van kwetsbaarheden

Het proces van identificatie van kwetsbaarheden vormt de eerste stap in het algehele proces voor het management van kwetsbaarheden. Gedurende deze fase, dient de organisatie te streven naar het tijdig ontdekken van mogelijke zwakke punten in de systemen en netwerken die mogelijk kunnen worden geëxploiteerd door aanvallers.

#### 2.1.1 Uitvoeren van kwetsbaarheidscans

- De organisatie zal scans van kwetsbaarheden uitvoeren op alle ICT-assets om potentiële zwakke punten die misbruikt kunnen worden, op te sporen.

- Wanneer de scans van de kwetsbaarheden van de systemen en infrastructuur van de organisatie worden uitgevoerd door een derde partij, zullen de vereisten voor deze scans duidelijk worden vastgelegd in een Service Level Agreement (SLA) met deze externe leverancier.

- Deze scans zullen volgens een vastgesteld schema worden uitgevoerd, of onmiddellijk nadat er aanzienlijke wijzigingen zijn aangebracht in de netwerken of systemen.

- De scans moeten met de volgende frequentie worden uitgevoerd:

- Interne systemen en netwerken: Maandelijks

- De organisatie gebruikt software-agenten/-collectoren om kwetsbaarheden op te sporen op (fysieke en virtuele) eindpunten.

- Ontdekking van kwetsbaarheden en misconfiguraties in besturingssystemen, apparaten en applicaties, on-premises of in de cloud, kan automatisch worden bereikt door de kwetsbaarheidsscans van de organisatie.

- De systemen voor kwetsbaarheidsscans worden ook gebruikt door de organisatie om de effectiviteit van de geïmplementeerde tegemaatregelen te evalueren (zie voor meer informatie 2.5 Verificatie van tegenmaatregelen).

#### 2.1.2 Uitvoeren van penetratie testen

- Naast reguliere kwetsbaarheidsscans zal de organisatie penetratie testen uitvoeren om zwakke punten in de systemen en netwerken op te sporen.

- Deze tests zullen simuleren hoe een aanvaller kan proberen in te breken op de systemen en de organisatie helpen bij het identificeren van gebieden waar de beveiliging eventueel versterkt moet worden.

- Een onafhankelijke derde leverancier voert deze penetratie testen uit.

- Het is belangrijk dat het proces van penetratietesten wordt afgestemd op de specifieke behoeften en risico's van de organisatie, waarbij rekening wordt gehouden met zowel de potentiële voordelen van de update als de mogelijke risico's van nieuwe kwetsbaarheden die door de update kunnen worden geïntroduceerd. Het doel is om een evenwicht te vinden tussen het bevorderen van veiligheid en het minimaliseren van verstoringen in de bedrijfsvoering.

- Informatiesystemen worden bij voorkeur jaarlijks gecontroleerd op technische naleving van beveiligingsnormen en risico’s ten aanzien van de feitelijke veiligheid. Dit kan bijvoorbeeld door (geautomatiseerde) kwetsbaarheidsanalyses, penetratietesten of red-teamingstesten.

- Internetfacing-systemen hebben een verplichte (bij voorkeur geautomatiseerde) penetratietest bij iedere nieuwe release of major update. Als daar bevindingen met een hoog risico uitkomen, mag het systeem niet in productie.

#### 2.1.3 Penetratie test methodes

De organisatie zal op voorhand een methode vaststellen voor het uitvoeren penetratietesten.

- Om consistentie te garanderen, dient er een standaardprotocol te worden gemaakt voor de penetratietesten in samenwerking met de onafhankelijke uitvoerder van de penetratietesten.

#### 2.1.4 Gebruik van threat intelligence sharing mechanismen

- De organisatie zal gebruik maken van Threat Intelligence sharing mechanismen om op de hoogte te blijven van de nieuwste bedreigingen en actoren en om tijdig te reageren op deze bedreigingen.

- Deze mechanismen bieden actuele informatie over nieuwe en opkomende bedreigingen en helpen de organisatie om proactief kwetsbaarheden te identificeren en te corrigeren voordat deze kunnen worden uitgebuit.

- De organisatie voert continu inventarisaties uit van kwetsbaarheden op basis van dreigingsinformatie.

- De IBD deelt eveneens kwetsbaarheden met de organisatie.

- De IBD beschikt over een actueel beeld van de systemen en netwerken van de organisatie en kan advies op maat geven in het geval van een potentiële dreiging.

- Bij ontdekte nieuwe dreigingen worden deze, rekening houdend met de geldende juridische kaders, verplicht gedeeld binnen de overheid, waaronder met het NCSC (alleen voor rijksoverheidsorganisaties) of de sectorale CERT, bij voorkeur door geautomatiseerde mechanismen (threat intelligence sharing).

### 2.2 Classificatie van kwetsbaarheden

Na het identificeren van kwetsbaarheden wordt elke kwetsbaarheid geclassificeerd. Het classificatieproces geeft de organisatie inzicht in de risico’s die de kwetsbaarheid met zich mee brengt en is daardoor van cruciaal belang voor het bepalen van de acties die ondernomen moeten worden om deze risico's naar een acceptabel niveau te brengen.

#### 2.2.1 Classificatie van categorieën technische kwetsbaarheid

Technische kwetsbaarheden worden in zes categorieën ingedeeld van de organisatie:

- Besturingssysteem Kwetsbaarheden

- Applicatie Kwetsbaarheden

- Netwerk Kwetsbaarheden

- Fysieke kwetsbaarheden

- Database kwetsbaarheden

- Systeem/Service kwetsbaarheden

Deze classificatie van technische kwetsbaarheden stelt de organisatie in staat om een holistische aanpak te hanteren voor het beheren van kwetsbaarheden en zorgt ervoor dat alle mogelijke gebieden van kwetsbaarheid worden aangepakt.

#### 2.2.2 Identificatie van false positives

- Gedurende het proces van het scannen van kwetsbaarheden, kunnen er false-positives resultaten worden geïdentificeerd - dit zijn meldingen van kwetsbaarheden die in werkelijkheid geen bedreiging vormen voor het systeem of netwerk.

- Hoewel deze false-positives geen actie vereisen, is het nodig dat ze worden herkend en gecategoriseerd om te voorkomen dat toekomstige middelen en tijd worden besteed aan het oplossen van niet-bestaande problemen.

- De tool voor het scannen van kwetsbaarheden van de organisatie zal false-positives detecteren, analyseren en verwijderen. In gevallen van onzekerheid worden deze doorgestuurd naar de organisatie. Alle false-positives worden bijgehouden voor toekomstige referentie. Dit zal in het contract worden vastgelegd met de derde partij die de kwetsbaarheidsscans uitvoert.

#### 2.2.3 Categorisatie op basis van impact en ernst

- Alle geïdentificeerde kwetsbaarheden worden gecategoriseerd op basis van hun potentiële impact en ernst van de bedreiging voor de organisatie.

- Aspecten zoals het type gegevens dat in gevaar zou kunnen komen en de potentiële schade aan de systemen en operaties van de organisatie, worden in overweging genomen bij het bepalen van de ernst van elke kwetsbaarheid.

#### 2.2.4 Classificatie op basis van kritiek, hoog, gemiddeld of laag risico

Kwetsbaarheden worden geclassificeerd als kritiek, hoog, gemiddeld of laag risico op basis van hun potentiële impact en de ernst van de dreiging die zij vormen. Kritieke risico's zijn die welke onmiddellijke actie vereisen vanwege hun potentieel om aanzienlijke schade te veroorzaken, terwijl kwetsbaarheden met een lager risico minder snel een actie vereisen.

De organisatie classificeert kwetsbaarheden volgens de volgende categorieën:

- Kritiek: Een kritieke kwetsbaarheid is een ernstige beveiligingszwakte in een systeem, applicatie of netwerk die het risico met zich meebrengt van aanzienlijke schade, inbreuk op de vertrouwelijkheid, integriteit of beschikbaarheid van gegevens, of zelfs het volledige compromis van het getroffen systeem. Deze klasse van kwetsbaarheden vormt het hoogste risico voor een systeem brede compromittering van het netwerk van de organisatie.

- Hoog: Dit betekent dat een kwetsbaarheid een indringer toegang zou kunnen geven tot de host op het beheerdersniveau of mogelijk toegang zou kunnen geven tot gevoelige informatie die op de host is opgeslagen. Hoewel deze klasse van kwetsbaarheden uiterst ernstig is, is het risico op een inbreuk of compromittering niet zo urgent als bij een kritieke kwetsbaarheid.

- Middelmatig: Dit betekent dat een kwetsbaarheid een indringer toegang kan geven tot specifieke informatie die op de host is opgeslagen, inclusief beveiligingsinstellingen. Hoewel deze kwetsbaarheden niet direct geassocieerd zijn met een compromittering van een getroffen host, stellen deze kwetsbaarheden indringers in staat om toegang te krijgen tot informatie die in de toekomst kan worden gebruikt om de host te compromitteren.

- Laag: Dit zijn kwetsbaarheden die geen directe bedreiging vormen voor de host of het netwerk van de organisatie. Deze kwetsbaarheden verwijzen voornamelijk naar zwakke punten in een apparaat die een indringer toegang geven tot informatie die in de toekomst kan worden gebruikt om de host te compromitteren.

Het classificeren van kwetsbaarheden volgens deze categorieën helpt de organisatie bij het identificeren van de ernst van elke gekenmerkte kwetsbaarheid en richt de inspanningen en middelen op een manier die de bescherming van de meest kritieke aspecten van haar systemen en netwerken vooropstelt.

### 2.3 Documentatie van kwetsbaarheden

De organisatie dient ervoor te zorgen dat ontdekte kwetsbaarheden en de bijbehorende classificatie wordt gedocumenteerd en gerapporteerd aan de CISO. Het documenteren en rapporteren van kwetsbaarheden dient de volgende doelen:

- Het afleggen van verantwoording

- Creëren van bewustwording

- Basis voor analyse en verbetering

- Basis voor toekomstige besluitvorming

- Bijhouden van voortgang van implementatie van tegenmaatregelen

#### 2.3.1 Rapporteren

Na de identificatie en classificatie van kwetsbaarheden zullen de specifieke details van elke kwetsbaarheid worden samengevat in gedocumenteerde rapporten.

- De rapporten worden maandelijks aangeleverd door de derde leverancier die de kwetsbaarheidsscans uitvoert.

- Deze rapporten zullen de aard van de kwetsbaarheid, de systemen die risico lopen, de voorgestelde tegenmaatregelen en andere relevante informatie bevatten.

- Deze rapporten worden regelmatig besproken met relevante belanghebbenden binnen de organisatie en gebruikt om te helpen bij het maken van geïnformeerde beslissingen over hoe de kwetsbaarheden het beste kunnen worden aangepakt.

#### 2.3.2 Documentatie in IT-risicoregister

Alle geïdentificeerde kwetsbaarheden worden gedocumenteerd in het IT-risicoregister van de organisatie. Dit register dient als een centrale opslagplaats voor informatie over alle bekende kwetsbaarheden en hun status. Het bijhouden van dit register stelt de organisatie in staat om de status van elke kwetsbaarheid snel te bekijken en de voortgang van de gekozen tegenmaatregelen te volgen.

#### 2.3.3 Delen van documentatie en rapporten

- Security teams en proces- en systeemeigenaren dienen maandelijks te rapporteren aan de CISO over kwetsbaarheden die openstaande risico’s vormen.

- Bij kwetsbaarheden die als kritiek en hoog risicovol gezien worden geldt dat deze maandelijks gepresenteerd en besproken moeten worden.

- De organisatie bespreekt ook met derde leveranciers rapportages en dashboards omtrent de resultaten van kwetsbaarheid scans.

### 2.4 Implementatie van tegenmaatregelen

Zodra kwetsbaarheden zijn geïdentificeerd, geclassificeerd en gedocumenteerd, dient de organisatie passende tegenmaatregelen te implementeren om deze kwetsbaarheden te verhelpen of te mitigeren.

#### 2.4.1 Patches, updates en andere methodes voor tegenmaatregelen

- De tegenmaatregelen kunnen variëren afhankelijk van de aard van de kwetsbaarheid en het risico dat deze vormt. De maatregelen kunnen onder andere bestaan uit het toepassen van patches, het uitvoeren van systeemupdates, het aanbrengen van wijzigingen in de configuraties van systemen of het implementeren van extra beveiligingscontroles.

- Bij het kiezen van de meest geschikte tegenmaatregel, zal de organisatie de mogelijke impact van elk van deze acties op de systemen en operaties in overweging nemen.

De volgende tegenmaatregelen van de organisatie zijn onderworpen aan specifieke vereisten vanuit de BIO:

2.4.1.2 Patches:

- Als de kans op misbruik en de verwachte schade beiden hoog worden ingeschat (zie NCSC-classificatie kwetsbaarheid waarschuwingen), dienen patches zo snel mogelijk maar uiterlijk binnen een week geïnstalleerd.

2.4.1.2 Updates:

- De organisatie inventariseert periodiek voor welke software geen of niet tijdig security updates beschikbaar worden gesteld.

- Leveranciers zijn verplicht binnen de afgesproken termijn een oplossing te bieden.

- Software ondergaat regelmatig security updates binnen de afgesproken termijn.

#### 2.4.2 Verantwoordelijkheden voor implementeren tegenmaatregelen

- De verantwoordelijkheid voor het implementeren van tegenmaatregelen wordt over het algemeen toegewezen aan de IV-teams, in samenwerking met de relevante systeem en proceseigenaren. De IV-teams zorgen voor de correcte implementatie van de tegenmaatregelen en zijn verantwoordelijk om alle veranderingen correct te documenteren in het IT-risicoregister.

### 2.5 Verificatie van tegenmaatregelen

- Na de implementatie van tegenmaatregelen, worden er verificatiecontroles uitgevoerd door het securityteam van de organisatie. Het doel van deze controles is om te bevestigen dat de genomen maatregelen naar behoren werken en de geïdentificeerde kwetsbaarheden effectief worden verholpen.

- De verificatie omvat herhaaldelijk uitgevoerde kwetsbaarheid scans, functionele testen van betrokken systemen en/of netwerken, en het doorlopen van event-specificaties of logs voor bewijs van effectieve mitigatie. Deze verificatiecontroles worden ook zorgvuldig gedocumenteerd als onderdeel van het IT-risicoregister, waardoor een volledig overzicht van de verantwoording van elke kwetsbaarheid wordt bijgehouden.

- Mocht een tegenmaatregel niet succesvol blijken te zijn in het aanpakken van de specifieke kwetsbaarheid, dan wordt dit probleem onmiddellijk geëscaleerd naar het relevante IV-team voor verdere analyse en actie.

- De verificatie van tegenmaatregelen speelt een belangrijke rol in het waarborgen van de effectiviteit van het beleid voor kwetsbaarheidsmanagement van de organisatie en dient als een laatste controle om ervoor te zorgen dat alle kwetsbaarheden op een adequate en volledige manier worden aangepakt.

## 3. Evaluatie en Verbetering van het Beleid

Het Beleid Kwetsbaarheid management wordt jaarlijks geëvalueerd om de doeltreffendheid ervan te waarborgen. Op basis van evaluatieresultaten worden indien nodig verbeteringen aangebracht in het beleid.

## 4. Vrijwaring

In het kader van voortdurende verbetering en naleving van beleidsdoelstellingen, wordt erkend dat bepaalde vereisten momenteel niet kunnen worden vervuld volgens het huidige beleidsstuk. Echter, met het oog op toekomstige inzet voor progressieve ontwikkeling, zijn deze niet nagekomen verplichtingen opgenomen in de veranderkalender voor 2024. Hoewel ze momenteel buiten bereik liggen, is uitgesproken om tegen de aangegeven tijdlijn aan alle gestelde eisen te voldoen, waarmee het beleid wordt versterkt in lijn met gemeentelijke doelstellingen en in lijn met de vereisten van de BIO 2.0.

## 5. Rollen en verantwoordelijkheden

Dit RACI-diagram biedt een overzicht van de verdeling van verantwoordelijkheden binnen de implementatie en handhaving van het netwerkbeveiligingsbeleid van de organisatie. De matrix identificeert de rollen van verschillende belanghebbenden bij specifieke taken en activiteiten die essentieel zijn voor een effectieve beveiliging van het netwerk. Hieronder wordt de betekenis van de gebruikte afkortingen toegelicht:

- R (Responsible): De persoon of groep die verantwoordelijk is voor de uitvoering van een specifieke taak of activiteit.

- A (Accountable): De individuele persoon die uiteindelijk verantwoordelijk is en beslissingsbevoegdheid heeft voor het betreffende onderdeel.

- C (Consulted): Personen of afdelingen die geraadpleegd moeten worden voor input en feedback bij de uitvoering van taken.

- I (Informed): Personen of afdelingen die op de hoogte moeten worden gehouden van de voortgang en resultaten van specifieke taken.

| Activiteit | R | A | C | I |
|---|---|---|---|---|
| 2.1 Identificatie van kwetsbaarheden | Externe leverancier kwetsbaarheidsscans | CISO | Securityteam |  |
| 2.1.1 Uitvoeren van kwetsbaarheidsscans | Externe leverancier kwetsbaarheidsscans | CISO |  |  |
| 2.1.2 Uitvoeren van penetration testing | Externe leverancier penetratietesten | CISO |  |  |
| 2.1.3 Verschillende penetratie testmethodes | Externe leverancier penetratietesten | CISO |  |  |
| 2.1.4 Gebruik van threat intelligence sharing mechanismen | Externe leverancier kwetsbaarheidsscans | CISO |  |  |
| 2.2 Classificatie van kwetsbaarheden | Externe leverancier kwetsbaarheidsscans | CISO | Securityteam |  |
| 2.2.1 Classificatie van categorieën technische kwetsbaarheid | Externe leverancier kwetsbaarheidsscans | CISO | Securityteam |  |
| 2.2.2 Identificatie van false positives | Externe leverancier kwetsbaarheidsscans | CISO |  |  |
| 2.2.3 Categorisatie op basis van impact en ernst | Externe leverancier kwetsbaarheidsscans | CISO | Securityteam |  |
| 2.2.4 Classificatie op basis van kritiek, hoog, gemiddeld of laag risico | Externe leverancier kwetsbaarheidsscans | CISO | Securityteam |  |
| 2.3 Documentatie van kwetsbaarheden | Externe leverancier kwetsbaarheidsscans | CISO |  |  |
| 2.3.1 Rapporteren | Securityteam | CISO |  |  |
| 2.3.2 Documentatie in IT-risicoregister | Securityteam | CISO |  |  |
| 2.3.3 Delen van documentatie en rapporten | CISO | CISO |  | CIO |
| 2.4 Implementatie van tegenmaatregelen | Systeembeheerder | Securityteam |  | CISO |
| 2.4.1 Patches, updates en andere methodes voor tegenmaatregelen | Systeembeheerder | Securityteam |  | CISO |
| 2.4.2 Verantwoordelijkheden voor implementeren tegenmaatregelen | Systeembeheerder | Securityteam |  | CISO |
| 2.5 Verificatie van tegenmaatregelen | Systeembeheerder | Securityteam |  | CISO |

## Bijlage 1: Kwetsbaarheidsmanagement stroomdiagram
