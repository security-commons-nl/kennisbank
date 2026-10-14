---
titel: Beleidsset informatiebeveiliging op BIO 2.0, op maat gemaakt met contextvragen
vakgebied: governance
type: beleid
normen: [BIO2, ISO 27001, ISO 27002, Cbw]
peildatum: 2026-10-14
herkomst: herschreven op BIO 2.0 versie 1.3 vanuit de thema-beleidsstukken (2020-2026) van het team informatiebeveiliging en privacy van een regionale samenwerking van gemeenten, aangevuld met de handreikingen van de IBD
status: concept
samenvatting: Een beleidsset informatiebeveiliging voor de 21 BIO 2.0-domeinen die je op maat maakt. Beantwoord een paar contextvragen, zoals wie je IT beheert, waar je systemen draaien en of je onder de Cbw valt, en de generator stelt per domein een conceptbeleid samen met de regels die bij jouw organisatie passen. Elke regel noemt de maatregel die hij invult, elk stuk heeft een controleraamwerk, en een test bewijst dat elke set alle 117 overheidsmaatregelen en 40 ISO-beheersmaatregelen dekt, bij elk antwoord. Zonder antwoorden lees je alle varianten naast elkaar.
bronnen: [ibd-bio2-template-strategisch-informatiebeveiligings-en-privacybeleid, ibd-bio2-handreiking-strategisch-informatiebeveiligings-en-privacybeleid, ibd-bio2-rasci-tabel-controls-informatieveiligheid-en-privacy, ibd-bio2-gap-analyse, ibd-beleid-logische-toegangsbeveiliging-v1-0, ibd-dataclassificatie-bio2, ibd-encryptiebeleid-pki-gemeente-v1-0, ibd-hardening-beleid-voor-gemeenten, ibd-back-up-en-recovery-gemeente, ibd-personeelsbeleid, ibd-voorbeeld-incidentmanagement-en-response-beleid-2, ibd-wachtwoordbeleid-2]
---

# Beleidsset informatiebeveiliging op BIO 2.0, op maat gemaakt met contextvragen

> **Lees de beleidsset online:** [security-commons-nl.github.io/kennisbank/governance/beleidsset-informatiebeveiliging](https://security-commons-nl.github.io/kennisbank/governance/beleidsset-informatiebeveiliging/)
>
> **Maak je eigen set:** [beleidsset op maat](beleidsset-generator.html). Beantwoord de vragen die je kunt
> beantwoorden en je krijgt in één keer 21 conceptstukken: het strategisch informatiebeveiligingsbeleid en twintig
> tactische stukken, één per BIO 2.0-domein. Download per stuk of de hele set.
>
> **Met een AI-assistent:** geef je assistent de link naar de generatorpagina. Daarop staan instructies voor de
> assistent: welke vragen hij stelt, welke bestanden hij ophaalt en wat hij niet mag veranderen.

Onder de BIO 2.0 en de Cyberbeveiligingswet heeft elke overheidsorganisatie een strategisch beleid nodig, en
daaronder beleid per onderwerp dat de 117 overheidsmaatregelen invult, en de 40 ISO-beheersmaatregelen waarvoor de
BIO 2.0 geen overheidsmaatregel kent. Dit is zo'n set, geordend naar de 21
domeinen van het BIO 2.0-controleraamwerk en geschreven op BIO 2.0 versie 1.3.

Een kleine gemeente die alles heeft uitbesteed, heeft een ander back-upbeleid nodig dan een grote organisatie
met een eigen datacenter. Daarom is elk stuk opgebouwd uit vaste regels en regels die afhangen van het
antwoord op een contextvraag. Wie de vragen beantwoordt, krijgt alleen de regels die passen. Wie een vraag
overslaat, krijgt beide varianten, elk in een kader met de vraag erboven.

## De stukken

Elk stuk hieronder is de leesversie zonder profiel: alle varianten staan erin. Onderaan elk stuk staat welke
maatregelen het invult, waar, met welke controle, en wat de organisatie zelf nog moet invullen.

<!-- stukken:begin -->
| BIO 2.0-domein | Stuk | Bouwsteen | Overheidsmaatregelen | ISO-maatregelen |
|---|---|---|---|---|
| IV-beleid | [Strategisch informatiebeveiligingsbeleid](iv-beleid.md) | [01-iv-beleid.md](data/01-iv-beleid.md) | 7 | 3 |
| Informatiebeveiliging binnen projecten | [Beleid informatiebeveiliging in projecten](ib-in-projecten.md) | [02-ib-in-projecten.md](data/02-ib-in-projecten.md) | 1 | 0 |
| Screening, bewustzijn & opleiding | [Beleid screening, bewustzijn en opleiding](screening-bewustzijn.md) | [03-screening-bewustzijn.md](data/03-screening-bewustzijn.md) | 7 | 3 |
| Bedrijfsmiddelenbeheer | [Beleid bedrijfsmiddelenbeheer](bedrijfsmiddelen.md) | [04-bedrijfsmiddelen.md](data/04-bedrijfsmiddelen.md) | 3 | 7 |
| Informatie classificatie | [Beleid informatieclassificatie](classificatie.md) | [05-classificatie.md](data/05-classificatie.md) | 6 | 1 |
| Logische toegangsbeveiliging | [Beleid logische toegangsbeveiliging](logische-toegang.md) | [06-logische-toegang.md](data/06-logische-toegang.md) | 14 | 2 |
| Leveranciersbeheer - Inkoop | [Beleid informatiebeveiliging bij inkoop](leveranciers-inkoop.md) | [07-leveranciers-inkoop.md](data/07-leveranciers-inkoop.md) | 8 | 0 |
| Leveranciersbeheer - contractbeheer | [Beleid informatiebeveiliging in contractbeheer](leveranciers-contract.md) | [08-leveranciers-contract.md](data/08-leveranciers-contract.md) | 6 | 0 |
| Security Incident Management | [Beleid beveiligingsincidenten](incidenten.md) | [09-incidenten.md](data/09-incidenten.md) | 12 | 1 |
| Business Continuity & Disaster Recovery | [Beleid ICT-continuïteit en uitwijk](bcm.md) | [10-bcm.md](data/10-bcm.md) | 2 | 2 |
| IT-Compliance | [Beleid IT-compliance](it-compliance.md) | [11-it-compliance.md](data/11-it-compliance.md) | 2 | 8 |
| Fysieke toegang & beveiliging | [Beleid fysieke toegang en beveiliging](fysiek.md) | [12-fysiek.md](data/12-fysiek.md) | 2 | 4 |
| Afvoer en hergebruik gegevensdragers | [Beleid afvoer en hergebruik van gegevensdragers](gegevensdragers.md) | [13-gegevensdragers.md](data/13-gegevensdragers.md) | 3 | 2 |
| Mobile Device Management | [Beleid mobile device management](mdm.md) | [14-mdm.md](data/14-mdm.md) | 2 | 0 |
| Vulnerability & patchmanagement | [Beleid kwetsbaarheden en patchmanagement](kwetsbaarheden.md) | [15-kwetsbaarheden.md](data/15-kwetsbaarheden.md) | 9 | 1 |
| Back-up & Recovery | [Beleid back-up en recovery](back-up.md) | [16-back-up.md](data/16-back-up.md) | 4 | 0 |
| Logging & monitoring | [Beleid logging en monitoring](logging.md) | [17-logging.md](data/17-logging.md) | 10 | 0 |
| Netwerkbeveiliging | [Beleid netwerkbeveiliging](netwerk.md) | [18-netwerk.md](data/18-netwerk.md) | 7 | 1 |
| Cryptografie | [Beleid cryptografie](cryptografie.md) | [19-cryptografie.md](data/19-cryptografie.md) | 4 | 0 |
| Secure Software Development | [Beleid veilige softwareontwikkeling](ssd.md) | [20-ssd.md](data/20-ssd.md) | 2 | 3 |
| Wijzigingsbeheer | [Beleid wijzigingsbeheer](wijzigingsbeheer.md) | [21-wijzigingsbeheer.md](data/21-wijzigingsbeheer.md) | 6 | 2 |
| **Totaal** | | | **117** | **40** |
<!-- stukken:einde -->

## Hoe het werkt

**De contextvragen.** [`profiel.json`](profiel.json) bevat zestien vragen met vaste antwoorden: wie je IT
beheert, waar systemen draaien, hoe je werkplek eruitziet, of je onder de Cbw valt, wie je omgeving bewaakt,
of je zelf software bouwt, of je OT of politiegegevens hebt, en meer. Per vraag staat welke domeinen hij
raakt. Geen vraag is verplicht.

**De bouwstenen.** Per domein staat de tekst in een bouwsteen in de map `data/`, in gewone markdown
met vier afspraken:

- een beleidsregel eindigt op de nummers van de maatregelen die hij invult, zoals `[8.13.01]`; de
  generator nummert de regels per paragraaf, zodat een controle of een reviewer naar "eis 3.2.4" kan wijzen;
- tekst die van een vraag afhangt, staat tussen `::: als hosting=saas` en `:::`;
- wat de organisatie zelf invult, staat als `[[eigenaar back-up: de rol die de back-up bewaakt]]`;
- het controleraamwerk is een tabel met per rij een controle (`FYS-01`) en de maatregelen die hij aantoont.

**De lat: waar elk stuk aan voldoet.** De opbouw is afgekeken van een gemeentelijk beleidsstuk dat op
BIO 2.0 is geschreven, en de build bewaakt hem:

1. Zes vaste hoofdstukken: 1 doel en reikwijdte (voor wie, waarop, wat erbuiten valt, en wat geldt als
   een voorziening is uitbesteed), 2 uitgangspunten, 3 beleidsregels, 4 rollen en verantwoordelijkheden,
   5 naleving en controle, 6 samenhang.
2. Elke regel in hoofdstuk 3 zegt wie wat doet, hoe vaak en waaruit dat blijkt, en noemt de maatregel die
   hij invult. Dat geldt voor alle maatregelen van het domein: de overheidsmaatregelen én de
   ISO-beheersmaatregelen waarvoor de BIO 2.0 geen overheidsmaatregel kent; daarvoor geldt de tekst van
   ISO 27002.
3. Hoofdstuk 5 bevat een controleraamwerk: per controle wat, wie, hoe vaak, welk bewijs en welke
   maatregelen. Elke maatregel van het domein heeft ten minste één controle. Daarna een vaste
   afwijkingsprocedure (gedocumenteerde risicoafweging, acceptatie door een risico-eigenaar, in het
   risicoregister, jaarlijks herbeoordeeld) en wat er gebeurt bij niet naleven.
4. Organisatie-inrichting (rollen, systemen, termijnen die de organisatie zelf kiest) is een invulveld;
   termijnen die uit een norm of wet komen, staan als getal.
5. De generator zet er een titelblad voor (documenttype, status, eigenaar, vaststeller, evaluatie) en
   twee bijlagen achter: A de maatregeltabel met per maatregel soort, paragraaf en controle, B de gebruikte
   afkortingen uit [`afkortingen.json`](data/afkortingen.json).

Een nieuwe versie van de BIO of een beter stuk van een andere organisatie verandert de bouwstenen, niet
de generator.

**De generator.** [`tools/bouw_beleidsset.py`](https://github.com/security-commons-nl/kennisbank/blob/main/tools/bouw_beleidsset.py)
zet een profiel en de bouwstenen om in een set. De [generatorpagina](beleidsset-generator.html) doet hetzelfde
in je browser; er gaat niets naar een server en er zit geen taalmodel in, dus dezelfde antwoorden geven
dezelfde tekst. Alle gegevens van de pagina staan ook los in [`beleidsset.json`](beleidsset.json).

**De dekking is een test.** Voor elk mogelijk antwoord op de vragen die een domein raakt, moet het stuk elke
maatregel van dat domein met minstens één regel invullen en met minstens één controle aantonen: de 117
overheidsmaatregelen en de 40 ISO-beheersmaatregelen zonder overheidsmaatregel. Mist er één, dan faalt de build. Een test
houdt ook de generator in de browser woord voor woord gelijk aan die in Python. De nummers, titels en domeinen
komen uit [`bio2-maatregelen.json`](data/bio2-maatregelen.json), een kopie uit de
[normen-repository](https://github.com/security-commons-nl/normen). De tekst van de overheidsmaatregelen
staat er niet in; die is van het CIP en staat op [bio-overheid.nl](https://www.bio-overheid.nl/bio2/).

## Met je eigen AI-agent

Geef je assistent de link naar de [generatorpagina](beleidsset-generator.html). Bovenaan staat, als gewone tekst
die ook een assistent zonder JavaScript leest, een blok *Instructies voor de assistent*: eerst de contextvragen
uit [`profiel.json`](profiel.json) stellen, dan per gekozen stuk de leesversie ophalen, de kaders houden of weghalen
naar de antwoorden, de invulvelden met de gebruiker invullen, en de nummers, het controleraamwerk en bijlage A
laten staan zodat het stuk toetsbaar blijft. Wie precies dezelfde tekst wil als het formulier, rekent met
[`beleidsset.json`](beleidsset.json) of draait `python tools/bouw_beleidsset.py --profiel antwoorden.json uitmap/`.

## Bijdragen

Een regel die bij jullie anders is, een vraag die ontbreekt of een domein dat beter kan: pas de bouwsteen aan
en draai `python tools/bouw_beleidsset.py`. Die zegt welke maatregel bij welk profiel niet meer gedekt is.
Zie [CONTRIBUTING.md](../../CONTRIBUTING.md).

**Invoeren.** Hoe je van deze set naar ingerichte maatregelen komt, met volgorde, eigenaar per thema en
een urenraming: [BIO 2.0 invoeren, een plan van aanpak](../bio2-implementeren/).

## Wat dit niet is

Geen vastgesteld beleid: elk stuk is een concept dat de organisatie zelf vaststelt. De test zegt dat er voor
elke overheidsmaatregel een regel staat, niet dat de maatregel in de praktijk werkt. Geen vervanging van de
IBD-templates; die blijven een bron.

## Licentie

EUPL-1.2.
