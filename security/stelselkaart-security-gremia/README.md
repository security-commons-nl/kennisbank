# Stelselkaart security-gremia

Wie organiseert de digitale weerbaarheid van de Nederlandse overheid, en hoe verhouden die partijen
zich tot elkaar? Deze map bevat een **open dataset** van 83 partijen en 19 concrete diensten:
van designated clubs als de IBD tot publiek-private platforms, plus de Europese laag als context.

> **Bekijk de stelselkaart online:** [security-commons-nl.github.io/kennisbank/security/stelselkaart-security-gremia](https://security-commons-nl.github.io/kennisbank/security/stelselkaart-security-gremia/)

> **Peildatum 11 augustus 2026.** Dit is een momentopname van een stelsel dat op dat moment hard in
> beweging was. De Cyberbeveiligingswet trad op 15 augustus 2026 in werking, meerdere CSIRT-aanwijzingen
> waren nog niet rond, en de OKTT-status stond op het punt te vervallen. **Kloppen er dingen niet meer?
> Open een [issue](https://github.com/security-commons-nl/kennisbank/issues/new/choose).** Dat is precies
> waarvoor deze dataset open is.

> **Bijgewerkt 13 augustus 2026, na de eerste externe review uit de sector.** Drie aanscherpingen:
> de vier gaten in de dienstentabel maken nu onderscheid tussen *niets belegd* en *wel aan gewerkt, en
> door wie* (een nul betekende hier ten onrechte dat er niets gebeurde) · bij de RDI staat nu in de
> omschrijving zelf dat BZK de bevoegde autoriteit is en de RDI het toezicht uitvoert · **regionale
> samenwerkingsverbanden** zijn als categorie opgenomen, met RSIV Den Haag als uitgewerkt voorbeeld,
> omdat er landelijk meer van zulke verbanden bestaan dan dat ene. Wat nog ontbreekt is het landelijke
> beeld: welke verbanden er zijn en welke gemeenten erbuiten vallen.
>
> **Tweede ronde, dezelfde dag, na doorvragen op de plaat zelf.** De relatiegraaf miste een lijn van **BZK
> naar de RDI**, terwijl de tekst al zei dat BZK bevoegd gezag is en de RDI het toezicht uitvoert; die staat
> er nu in. **Gemeenschappelijke regelingen** ontbraken volledig als entiteitstype en staan nu als eigen blok
> naast gemeente en regio, met hun Cbw-status als open vraag: een GR met eigen rechtspersoonlijkheid kan zelf
> entiteit zijn, maar dat is nergens uitgewerkt terwijl een groot deel van de gemeentelijke uitvoering er zit.
> **Privacy is bewust buiten scope gehouden**, ook al doen meerdere partijen hier beide; dat staat nu expliciet
> in de verantwoording in plaats van dat het onbenoemd ontbreekt.

## Waarom dit bestaat

Er zijn heel veel gremia die de samenwerking op security binnen de overheid proberen te verbeteren:
CISO-kringen, de IBD, VNG, CIP, de NDS-versnellers, ISAC's, cyberweerbaarheidscentra, en zo verder.
Voor een gemeentelijke CISO is nergens te vinden welke er zijn, wie waarvoor gaat, waar je zelf terecht
kunt, en waar het aanbod elkaar overlapt. Dit is een poging dat één keer goed uit te zoeken en het
resultaat te delen in plaats van in een la te leggen.

## Wat je hier vindt

| Bestand | Inhoud |
|---|---|
| **`index.html`** | **De leesbare weergave.** Open het bestand in je browser, of lees hem [online](https://security-commons-nl.github.io/kennisbank/security/stelselkaart-security-gremia/). Vijf visualisaties, een filterbaar overzicht van alle partijen, en de bronverantwoording. Offline te openen, geen externe afhankelijkheden |
| `data/partijen.json` | 83 partijen met laag, mandaatsoort, functies, toegankelijkheid voor een gemeente, omschrijving en toelichting |
| `data/diensten.json` | 19 concrete diensten met wie ze levert, inclusief **4 gaten**. Per gat staat in `gat_soort` of er niets is belegd of dat er wel aan gewerkt wordt, en in dat laatste geval staat in `werk_in_uitvoering` door wie |

Beide JSON-bestanden bevatten een `meta`-blok met het vocabulaire, zodat de codes zelfverklarend zijn.

### De vijf weergaven in `index.html`

| | Wat het laat zien |
|---|---|
| **Functie bij bestuurslaag** | Matrix van functies tegen bestuurslagen. Meerdere partijen in een cel is overlap, een lege cel is een gat |
| **Lagenmodel** | Het stelsel als bevelslijn van Brussel naar de gemeente. Laat zien hoeveel schakels er tussen een Europese richtlijn en een gemeentelijke maatregel zitten |
| **Relatiegraaf** | Wie stuurt wie aan, wie betaalt wie, wie informeert wie |
| **Waar zit welke overlap** | Per concrete dienst wie hem levert, gesorteerd van druk naar leeg, met de gaten onderaan. De kleuren tonen de mandaatsoort, en dat is het halve verhaal |
| **Wie is wiens dubbelganger** | Dezelfde data omgedraaid: hoeveel concrete diensten twee partijen allebei leveren |

### Waarom twee bestanden

`partijen.json` ordent op **functie** (normstelling, toezicht, CERT, kennisdeling, inkoop, crisis,
detectie, opleiden). Dat is bruikbaar voor oriëntatie, maar functie is een containerbegrip:
NCSC-advisories en een vakblad van een beroepsvereniging vallen er allebei onder "kennisdeling" terwijl
ze niets met elkaar te maken hebben. Dat levert schijn-overlap op, en het verbergt echte overlap
(de EASM-dienst van de IBD en ThreatMatcher van Connect2Trust zijn in de praktijk hetzelfde product,
maar zitten in verschillende functiecategorieën).

`diensten.json` lost dat op door te ordenen op **wat een partij feitelijk levert**. Pas op dat niveau
wordt overlap hard aanwijsbaar, en worden de gaten zichtbaar.

## Wat eruit komt

**De vier drukste diensten:**

| Aantal partijen | Dienst | Waarvan met wettelijk mandaat |
|---|---|---|
| 8 | Kennisbijeenkomsten en community | 1 |
| 6 | Crisisoefening aanbieden | 2 |
| 6 | Collectieve security-inkoop | **0** |
| 6 | Handreikingen en templates | 2 |

**De vier gaten, in twee soorten.** Waar helemaal niets is belegd: een landelijke weerbaarheidsmeting van
gemeenten (de Algemene Rekenkamer heeft geen mandaat over gemeenten, lokale rekenkamers leveren geen
landelijk beeld, ENSIA levert data maar geen analyse) en de opvolging van de OKTT-status (vervalt met de
Cbw, opvolging niet uitgewerkt). Waar geen kader is vastgesteld maar wel aan gewerkt wordt: **OT-normering**
(een expertgroep OT voor gemeenten vanuit de IBD heeft een opzet voor objectbaselines voor de 23 meest
voorkomende OT-objecten in review; duidelijkheid verwacht rond eind september 2026) en **ketenregie tussen
organisaties** (NDS-versneller 5.4 levert een begrippenkader, een centraal register staat expliciet niet in
scope).

Dat onderscheid is er sinds 13 augustus 2026 en het is geen detail: een nul in een tabel leest als "niemand
doet iets", en dat deed het werk van anderen tekort.

**Drie observaties die uit de data volgen:**

1. **Wettelijk mandaat en feitelijke dienstverlening lopen niet parallel.** De partijen met een wettelijk
   mandaat leveren weinig van wat een gemeentelijke CISO dagelijks gebruikt. De partijen die dat wel doen
   (IBD, VNG-voorzieningen, CIP, Connect2Trust) hebben geen wettelijke basis. Vrijwel elke spanning in het
   stelsel is een uitdrukking van die scheve verhouding.
2. **Het aantal partijen zegt weinig, de mandaatsoort zegt alles.** Bij collectieve inkoop staan zes
   partijen en heeft er géén enkele wettelijke bevoegdheid: niemand kon het afdwingen, dus begon iedereen
   zelf. Bij normstelling staan er vijf, waarvan vier met een wettelijk mandaat en een eigen domein, en
   dan is meervoud geen versnippering maar arbeidsdeling.
3. **De IBD levert 11 van de 19 diensten** en komt voor in 7 van de 10 partijparen die twee of meer
   diensten delen. Dat verklaart waarom elk nieuw initiatief in dit veld al snel als concurrentie van de
   IBD wordt gelezen: je kunt er feitelijk nauwelijks omheen bouwen. De zwaarste dubbeling is IBD en NCSC
   met vijf gedeelde diensten (handreikingen, situationeel beeld, dreigingsinfo op eigen assets,
   CSIRT-bijstand en kwetsbaarheidsmelding). Op de peildatum was die verdeling nog niet gemaakt.

Tegenbewijs dat de functie-indeling schijn-overlap opleverde: CIP en NCSC delen nul concrete diensten,
CIP en Connect2Trust ook, terwijl ze in de functie-indeling in dezelfde categorieën vallen.

## Toegankelijkheid voor een gemeente

Het veld `toegang_gemeente` geeft aan of je er als gemeente zelf bij kunt:

- **`direct`** (38 partijen) — zelf terecht, lid worden of een dienst afnemen
- **`indirect`** (17 partijen) — alleen via een koepel of schakelorganisatie, meestal de IBD
- **`gesloten`** (28 partijen) — niet toegankelijk voor een gemeente

Dat laatste getal is op zichzelf een bevinding: ruim een derde van het stelsel is voor een gemeente
geen deur maar een muur.

## Bronverantwoording

Samengesteld op basis van openbare bronnen: wetgeving en Staatscourant-publicaties, Kamerstukken,
websites en jaarplannen van de betrokken partijen, en adviezen van onder meer de Cyber Security Raad,
de Raad van State, de Algemene Rekenkamer en de WRR. Waar officiële bronnen elkaar op de peildatum
tegenspraken, is dat in de toelichting benoemd in plaats van gladgestreken.

Twee voorbeelden daarvan, beide relevant genoeg om te noemen:

- **Wie het CSIRT voor gemeenten is.** VNG en RDI noemden de IBD, terwijl Digitale Overheid op
  6 augustus 2026 meldde dat de besluitvorming nog liep en het NCSC de dienstverlening voorlopig
  leverde, in ieder geval tot eind 2026. De dataset volgt de laatste, recentere bron.
- **Wanneer 3000D verplicht wordt voor DigiD-verantwoording.** De ENSIA-documentatie en Logius drukken
  dit verschillend uit (verantwoordingsjaar 2026 versus indieningsperiode 2027 over boekjaar 2026).
  Waarschijnlijk hetzelfde besluit, anders geformuleerd. Niet opgelost, wél gemarkeerd.

## Status en wat er nog komt

Dit is bewust **eerst de dataset**, niet het afgeronde verhaal. De feiten zijn van iedereen en kunnen
door iedereen gecorrigeerd worden. De duiding, met de volledige analyse van overlap, onnodige
concurrentie en gaten, volgt zodra er een tweede maintainer meetekent. Dat is geen slag om de arm maar
een principe: een oordeel over het stelsel is sterker als het van meer dan één gemeente komt.

**Meedoen?** Open een [issue](https://github.com/security-commons-nl/kennisbank/issues/new/choose) of een
discussion, of wijzig direct
[een regel in de dataset](https://github.com/security-commons-nl/kennisbank/edit/main/security/stelselkaart-security-gremia/data/partijen.json).
Dat laatste werkt ook zonder schrijfrechten: GitHub maakt er automatisch een voorstel van. Eén regel
corrigeren is genoeg om bij te dragen, je hoeft geen visualisatie te bouwen.

## Hergebruik

De dataset is bewust machineleesbaar zodat je er je eigen weergave op kunt bouwen: een tabel voor je
eigen bestuur, een filter op alleen de partijen waar je zelf bij kunt, of een koppeling aan je eigen
stakeholderregister. Alle codes staan in het `meta`-blok van beide bestanden.

## Licentie

[EUPL-1.2](https://github.com/security-commons-nl/kennisbank/blob/main/LICENSE), vrij te hergebruiken en
aan te passen. Feedback en verbeteringen welkom via de
[kennisbank](https://github.com/security-commons-nl/kennisbank).
