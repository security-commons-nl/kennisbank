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
>
> **Met je eigen API-sleutel:** de [AI-hulp](beleidsset-ai.html) leest je eigen documenten en stelt de antwoorden
> op de contextvragen of de waarden voor de invulvelden voor, elk met een citaat. Jij kiest in de generator wat je
> overneemt.

Onder de BIO 2.0 en de Cyberbeveiligingswet heeft elke overheidsorganisatie een strategisch beleid nodig, en
daaronder beleid per onderwerp dat de 117 overheidsmaatregelen invult, en de 40 ISO-beheersmaatregelen waarvoor de
BIO 2.0 geen overheidsmaatregel kent. Dit is zo'n set, geordend naar de 21
domeinen van het BIO 2.0-controleraamwerk en geschreven op BIO 2.0 versie 1.3.

Een kleine gemeente die alles heeft uitbesteed, heeft een ander back-upbeleid nodig dan een grote organisatie
met een eigen datacenter. Daarom is elk stuk opgebouwd uit vaste regels en regels die afhangen van het
antwoord op een contextvraag. Wie de vragen beantwoordt, krijgt alleen de regels die passen. Wie een vraag
overslaat, krijgt beide varianten, elk in een kader met de vraag erboven.

## De stukken

Elk stuk hieronder is de leesversie zonder profiel: alle varianten staan erin. Bovenaan elk stuk staat in het
kort waar het over gaat en welke onderwerpen het regelt; onderaan staat welke maatregelen het invult, waar, met
welke controle, en wat de organisatie zelf nog moet invullen. Elk stuk is ook te downloaden als Word-bestand.

- **Hele set in Word:** [beleidsset-informatiebeveiliging.docx](beleidsset-informatiebeveiliging.docx), alle 21
  stukken achter elkaar, elk op een nieuwe pagina.
- **[Maatregelenoverzicht](maatregelenoverzicht.md)** ([Word](maatregelenoverzicht.docx)): per BIO 2.0-maatregel
  het stuk, het hoofdstuk en de controle.
- **[Invoeren: wat er nog moet gebeuren](invoeren.md)** ([Word](invoeren.docx)): per stuk wat de organisatie
  inricht, welke controles zij gaat uitvoeren en wat zij nog moet invullen.

Maak je een set op maat in de [generator](beleidsset-generator.html), dan krijg je dezelfde overzichten voor jouw
antwoorden, en ook alles als Word.

<!-- stukken:begin -->
| BIO 2.0-domein | Stuk | Waar het over gaat | Overheidsmaatregelen | ISO-maatregelen |
|---|---|---|---|---|
| IV-beleid | [Strategisch informatiebeveiligingsbeleid](iv-beleid.md) ([Word](iv-beleid.docx), [bouwsteen](data/01-iv-beleid.md)) | Het bovenliggende kader voor informatiebeveiliging: wat de organisatie wil bereiken, wie verantwoordelijk is en hoe zij aantoont dat het werkt. Behandelt de vaststelling en inbedding van het beleid, de samenhang met privacy, OT en continuïteit, de organisatie van de beveiligingsfunctie, bewustzijn, contacten en dreigingsinformatie, audit en verantwoording, en de evaluatie. | 7 | 3 |
| Informatiebeveiliging binnen projecten | [Beleid informatiebeveiliging in projecten](ib-in-projecten.md) ([Word](ib-in-projecten.docx), [bouwsteen](data/02-ib-in-projecten.md)) | Regelt hoe beveiliging en privacy vanaf de start meegaan in projecten en significante wijzigingen aan informatiesystemen. Behandelt wanneer een risicoafweging nodig is, hoe die wordt uitgevoerd, de beslismomenten van start tot overdracht naar beheer, en de inbedding in de projectmethodiek. | 1 | 0 |
| Screening, bewustzijn & opleiding | [Beleid screening, bewustzijn en opleiding](screening-bewustzijn.md) ([Word](screening-bewustzijn.docx), [bouwsteen](data/03-screening-bewustzijn.md)) | Over de mens als onderdeel van de beveiliging, van werving tot vertrek. Behandelt screening, aanstelling en geheimhouding, training en bewustzijn, scholing van het bestuur, functiewijziging en vertrek, en de disciplinaire procedure bij niet naleven. | 7 | 3 |
| Bedrijfsmiddelenbeheer | [Beleid bedrijfsmiddelenbeheer](bedrijfsmiddelen.md) ([Word](bedrijfsmiddelen.docx), [bouwsteen](data/04-bedrijfsmiddelen.md)) | Regelt welke bedrijfsmiddelen de organisatie heeft, wie er eigenaar van is en hoe ze gebruikt, beschermd en ingeleverd worden. Behandelt de inventaris, eigendom, aanvaardbaar gebruik, teruggeven bij vertrek, werken in beveiligde zones, plaatsing en nutsvoorzieningen, apparatuur buiten de locaties en onderhoud. | 3 | 7 |
| Informatie classificatie | [Beleid informatieclassificatie](classificatie.md) ([Word](classificatie.docx), [bouwsteen](data/05-classificatie.md)) | Over het classificeren, labelen en veilig overdragen van informatie op beschikbaarheid, integriteit en vertrouwelijkheid. Behandelt de classificatiemethode met vijf impactniveaus, de minimumeisen per label, het labelen van documenten en hardware, en de eisen aan websites, e-mail, certificaten en andere overdracht. | 6 | 1 |
| Logische toegangsbeveiliging | [Beleid logische toegangsbeveiliging](logische-toegang.md) ([Word](logische-toegang.docx), [bouwsteen](data/06-logische-toegang.md)) | Regelt de toegang tot informatiesystemen, netwerken en gegevens: hoe accounts ontstaan en vervallen, hoe gebruikers zich aanmelden en wie welke rechten krijgt. Behandelt accounts, MFA, wachtwoorden, werken op afstand, periodieke beoordeling van rechten, beheeraccounts, toegang voor leveranciers, hoog gelabelde informatie en broncode. | 14 | 2 |
| Leveranciersbeheer - Inkoop | [Beleid informatiebeveiliging bij inkoop](leveranciers-inkoop.md) ([Word](leveranciers-inkoop.docx), [bouwsteen](data/07-leveranciers-inkoop.md)) | Over wat de organisatie regelt voordat zij een contract tekent met een leverancier die haar informatie verwerkt of bij haar systemen kan. Behandelt de risicoafweging en eisen in de uitvraag, contractvoorwaarden, bewijs van de leverancier, meldplicht bij incidenten, afhankelijkheid en exit, de keten van toeleveranciers en het inkoopdossier. | 8 | 0 |
| Leveranciersbeheer - contractbeheer | [Beleid informatiebeveiliging in contractbeheer](leveranciers-contract.md) ([Word](leveranciers-contract.docx), [bouwsteen](data/08-leveranciers-contract.md)) | Regelt hoe de organisatie zicht houdt op leveranciers met een informatiecomponent zolang een contract loopt. Gaat over het register van leveranciers en contracten, de jaarlijkse beoordeling van de leverancier, de keten van toeleveranciers, clouddiensten en het beëindigen van een contract. | 6 | 0 |
| Security Incident Management | [Beleid beveiligingsincidenten](incidenten.md) ([Word](incidenten.docx), [bouwsteen](data/09-incidenten.md)) | Over het melden, beoordelen, afhandelen en leren van beveiligingsincidenten en datalekken. Behandelt het meldloket, de classificatie, detectie en escalatie, de afhandeling, meldingen aan externe partijen, coordinated vulnerability disclosure, het veiligstellen van bewijs en de evaluatie achteraf. | 12 | 1 |
| Business Continuity & Disaster Recovery | [Beleid ICT-continuïteit en uitwijk](bcm.md) ([Word](bcm.docx), [bouwsteen](data/10-bcm.md)) | Regelt de continuïteit van informatie en ICT als systemen uitvallen. Gaat over het bepalen van kritieke processen en systemen met hun hersteleisen, uitwijk en redundantie, de beveiliging tijdens een verstoring en het opstellen en testen van continuïteitsplannen. | 2 | 2 |
| IT-Compliance | [Beleid IT-compliance](it-compliance.md) ([Word](it-compliance.docx), [bouwsteen](data/11-it-compliance.md)) | Over de naleving van wet- en regelgeving en contractuele eisen voor informatie en systemen. Behandelt het register van eisen, licenties, bewaartermijnen, privacy en testgegevens, clear desk en clear screen, capaciteit en kloksynchronisatie, en audits op productiesystemen. | 2 | 8 |
| Fysieke toegang & beveiliging | [Beleid fysieke toegang en beveiliging](fysiek.md) ([Word](fysiek.docx), [bouwsteen](data/12-fysiek.md)) | Regelt de fysieke beveiliging van locaties en ruimten waar informatie wordt verwerkt of bewaard. Gaat over de indeling in vier beveiligingszones, de eisen per zone, de omgang met incidenten, monitoring en waarschuwingen, en het dragen van toegangspassen. | 2 | 4 |
| Afvoer en hergebruik gegevensdragers | [Beleid afvoer en hergebruik van gegevensdragers](gegevensdragers.md) ([Word](gegevensdragers.docx), [bouwsteen](data/13-gegevensdragers.md)) | Over gegevensdragers, van USB-stick en harde schijf tot papier, en over informatie in systemen die niet meer nodig is. Behandelt het gebruik van verwijderbare media, wissen en vernietigen, afvoer en hergebruik van apparatuur, wissen in systemen en transport. | 3 | 2 |
| Mobile Device Management | [Beleid mobile device management](mdm.md) ([Word](mdm.docx), [bouwsteen](data/14-mdm.md)) | Regelt de inrichting, het beheer en het gebruik van laptops, smartphones en tablets met toegang tot bedrijfsinformatie. Gaat over zero footprint en bescherming op het apparaat, beheer via MDM en MAM, en de gebruikersovereenkomst mobiel werken. | 2 | 0 |
| Vulnerability & patchmanagement | [Beleid kwetsbaarheden en patchmanagement](kwetsbaarheden.md) ([Word](kwetsbaarheden.docx), [bouwsteen](data/15-kwetsbaarheden.md)) | Regelt hoe de organisatie technische kwetsbaarheden vindt, beoordeelt en binnen vaste termijnen verhelpt. Behandelt bescherming tegen malware, basisconfiguraties en hardening, scannen en penetratietesten, patchtermijnen per risico en het kwetsbaarhedenregister met een maandrapportage aan de directie. | 9 | 1 |
| Back-up & Recovery | [Beleid back-up en recovery](back-up.md) ([Word](back-up.docx), [bouwsteen](data/16-back-up.md)) | Over het maken, beschermen en terugzetten van back-ups, met ransomware als leidend scenario. Behandelt back-upplannen en het back-upregister, hersteleisen per systeem, een onveranderbare kopie, gescheiden opslag op meerdere plekken en het jaarlijks testen van herstel. | 4 | 0 |
| Logging & monitoring | [Beleid logging en monitoring](logging.md) ([Word](logging.docx), [bouwsteen](data/17-logging.md)) | Regelt wat systemen moeten loggen, hoe logbestanden veilig worden bewaard en hoe de omgeving wordt bewaakt op aanvallen. Behandelt minimale loggebeurtenissen, het overzicht van logbronnen, bewaartermijnen, centrale opslag buiten bereik van beheerders, detectie met escalatieregels en het delen van dreigingen met de CERT. | 10 | 0 |
| Netwerkbeveiliging | [Beleid netwerkbeveiliging](netwerk.md) ([Word](netwerk.docx), [bouwsteen](data/18-netwerk.md)) | Over het ontwerp, de inrichting en de bewaking van de netwerken, zodat een aanvaller die binnenkomt niet vrij verder kan. Behandelt segmentatie, beheer van netwerkcomponenten, firewalls en detectie op koppelpunten, het webfilter, versleuteling onderweg en wifi. | 7 | 1 |
| Cryptografie | [Beleid cryptografie](cryptografie.md) ([Word](cryptografie.docx), [bouwsteen](data/19-cryptografie.md)) | Regelt wanneer en hoe de organisatie versleutelt en wie sleutels en certificaten beheert. Behandelt de minimale versleuteling per vertrouwelijkheidslabel, verplichte standaarden en adviezen van NCSC en NBV, de inventaris van certificaten en sleutels, en de procedure sleutelbeheer met intrekking en reservecertificaten. | 4 | 0 |
| Secure Software Development | [Beleid veilige softwareontwikkeling](ssd.md) ([Word](ssd.docx), [bouwsteen](data/20-ssd.md)) | Over beveiliging in software die de organisatie bouwt, laat bouwen of afneemt, voordat die in gebruik gaat. Behandelt architectuurprincipes, beveiligingseisen per toepassing, veilig ontwikkelen of de eisen daarvoor aan leveranciers, afspraken bij uitbestede ontwikkeling en testen met fictieve gegevens. | 2 | 3 |
| Wijzigingsbeheer | [Beleid wijzigingsbeheer](wijzigingsbeheer.md) ([Word](wijzigingsbeheer.docx), [bouwsteen](data/21-wijzigingsbeheer.md)) | Regelt hoe een wijziging in productie wordt aangevraagd, beoordeeld, getest, goedgekeurd en doorgevoerd. Behandelt het wijzigingsproces met standaard-, normale en spoedwijzigingen, werkinstructies voor beheertaken, het installeren van software, de scheiding van omgevingen en acceptatietesten. | 6 | 2 |
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
  generator nummert de regels per hoofdstuk, zodat een controle of een reviewer naar "eis 5.4" kan wijzen;
- tekst die van een vraag afhangt, staat tussen `::: als hosting=saas` en `:::`;
- wat de organisatie zelf invult, staat als `[[eigenaar back-up: de rol die de back-up bewaakt]]`;
- het controleraamwerk is een tabel met per rij een controle (`FYS-01`) en de maatregelen die hij aantoont.

**De lat: waar elk stuk aan voldoet.** De opbouw is afgekeken van een gemeentelijk beleidsstuk dat op
BIO 2.0 is geschreven, en de build bewaakt hem:

1. Vaste hoofdstukken voor en achter: 1 doel en reikwijdte (voor wie, waarop, wat erbuiten valt, en wat
   geldt als een voorziening is uitbesteed), 2 uitgangspunten, dan elk onderwerp van het domein als eigen
   hoofdstuk met de beleidsregels (bij back-up bijvoorbeeld 3 back-upplannen en scenario's, 4 hersteleisen),
   en daarna rollen en verantwoordelijkheden, naleving en controle, en samenhang. De nummers lopen door.
2. Elke regel in een onderwerphoofdstuk zegt wie wat doet, hoe vaak en waaruit dat blijkt, en noemt de
   maatregel die hij invult. Dat geldt voor alle maatregelen van het domein: de overheidsmaatregelen én de
   ISO-beheersmaatregelen waarvoor de BIO 2.0 geen overheidsmaatregel kent; daarvoor geldt de tekst van
   ISO 27002.
3. Het hoofdstuk naleving en controle bevat een controleraamwerk: per controle wat, wie, hoe vaak, welk bewijs en welke
   maatregelen. Elke maatregel van het domein heeft ten minste één controle. Daarna een vaste
   afwijkingsprocedure (gedocumenteerde risicoafweging, acceptatie door een risico-eigenaar, in het
   risicoregister, jaarlijks herbeoordeeld) en wat er gebeurt bij niet naleven.
4. Organisatie-inrichting (rollen, systemen, termijnen die de organisatie zelf kiest) is een invulveld;
   termijnen die uit een norm of wet komen, staan als getal.
5. In de frontmatter van de bouwsteen staan een `samenvatting` (twee of drie zinnen over waar het stuk over
   gaat) en onder `invoeren` wat de organisatie moet inrichten om het beleid in te voeren, elk met het
   hoofdstuk waar het vandaan komt.
6. De generator zet er een titelblad voor (documenttype, status, eigenaar, vaststeller, evaluatie), dan de
   samenvatting en de onderwerpen, en twee bijlagen achter: A de maatregeltabel met per maatregel soort,
   hoofdstuk en controle, B de gebruikte afkortingen uit [`afkortingen.json`](data/afkortingen.json).

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

## AI-hulp met je eigen sleutel

De [AI-hulp](beleidsset-ai.html) volgt het patroon van de andere instrumenten van de commons: een aparte pagina,
je eigen sleutel (alleen in de tab, weg als je hem sluit), een leverancier naar keuze (standaard Mistral, ook een
lokale Ollama), en toestemming per sessie. Twee opdrachten:

- **Contextvragen beantwoorden** uit een beschrijving van je organisatie, zoals een jaarverslag of een eerdere
  ENSIA-verantwoording.
- **Invulvelden invullen** uit je eigen documenten, zoals een organisatiebesluit, een mandaatregeling of een lijst
  met systemen.

Het model schrijft geen beleid: de regels staan in de bouwstenen. Het levert een voorstel als bestand. Elke regel
draagt een letterlijk citaat, en een regel waarvan het citaat niet in je document staat, staat in de generator
standaard uit. Pas na *Overnemen* verandert er iets, en onder elk stuk staat dan welke velden uit een AI-voorstel
komen. De prompts en schema's staan als data in
[`tools/beleidsset-ai/opdrachten.json`](https://github.com/security-commons-nl/kennisbank/blob/main/tools/beleidsset-ai/opdrachten.json);
de controles (schema, citaat) delen een kern met de andere instrumenten. Uitleg over wat er waarheen gaat:
[AI-hulp met je eigen sleutel](https://security-commons-nl.github.io/ai-hulp/).

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
