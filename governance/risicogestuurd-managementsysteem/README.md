---
titel: "GRC voor security, privacy en continuïteit: één risicogestuurde PDCA-ronde"
vakgebied: governance
type: aanpak
normen: [BIO2, ISO 27001, AVG, ISO 22301, Cbw]
versie: 2026-10
herkomst: ontwikkeld door de CISO van een regionale samenwerking van gemeenten, waar het register de werknaam risicoboom had; de methode en een verzonnen voorbeeld, zonder gegevens van die organisatie
status: concept
barrieres: [owner, treatment]
rol: verdieping
samenvatting: Wat governance, risk en compliance is, waarom security, privacy en continuïteit er één stelsel voor nodig hebben, en twee manieren om dat te doen. Een GRC-tool kopen, of een risicoregister bijhouden waarin elk risico uit een aangetoonde fout in een maatregel volgt en de prioriteit wordt uitgerekend, met een AI-assistent als lezer binnen vaste regels. Met het model, een doorgerekend voorbeeld van een verzonnen gemeente, plakbare prompts en een leeg register.
bronnen: [ibd-bio2-handreiking-isms, ibd-bio2-infographic-wat-is-een-isms, ibd-bio2-handreiking-isms-proces-implementatie, ibd-bio-handreiking-risicomanagement-voor-gemeenten, ibd-risicoregister-inclusief-risicobehandelplan-en-dashboards, ibd-handreiking-risicoregister-en-risico-acceptatie-overeenkomst-rao, ibd-bio2-kans-en-impact-tabellen-gemeenten, ibd-avg-borgingsproduct-3-1-toetsingskader, ibd-avg-borgingsproduct-3-1-handreiking, cip-bio-tekst, ncsc-cbw-valt-mijn-organisatie-eronder]
---

# GRC voor security, privacy en continuïteit: één risicogestuurde PDCA-ronde

> **Lees dit online:** [security-commons-nl.github.io/kennisbank/governance/risicogestuurd-managementsysteem](https://security-commons-nl.github.io/kennisbank/governance/risicogestuurd-managementsysteem/)

Elke gemeente heeft een lijst met maatregelen die af moeten, en die lijst is te lang. BIO 2.0 alleen telt al
ruim honderd overheidsmaatregelen; privacy en bedrijfscontinuïteit komen daar bovenop. De vraag die de
directie stelt is altijd dezelfde: wat doen we eerst, en waarom? Dit stuk geeft een manier om die vraag elk
jaar opnieuw te beantwoorden, voor de drie disciplines tegelijk, met een antwoord dat je kunt narekenen.

Wie BIO 2.0 nog moet invoeren, begint bij
[BIO 2.0 invoeren, een plan van aanpak met urenraming](../bio2-implementeren/). Dit stuk is de ronde die
daarna elk jaar draait.

| Bestand | Wat het is |
|---|---|
| [`model.md`](model.md) | De regels: vijf lagen, hoe een risico uit een bevinding volgt, hoe het niveau en de prioriteit worden berekend |
| [`voorbeeld-register.md`](voorbeeld-register.md) | Een doorgerekend register van de verzonnen gemeente Duinstad: drie strategische risico's, zeven operationele risico's, zestien maatregelen, drie controls, zes bevindingen |
| [`voorbeeld-register-verkenner.html`](voorbeeld-register-verkenner.html) | Hetzelfde voorbeeld om door te klikken, met tabbladen en een filter per kader |
| [`voorbeeld-register.json`](voorbeeld-register.json) | De gegevens van het voorbeeld, als invoer voor het rekenscript |
| [`prompts.md`](prompts.md) | Drie prompts om in een AI-assistent te plakken, met de regels die de assistent niet mag overtreden |
| [`sjabloon-register.md`](sjabloon-register.md) | Een leeg register om zelf in te vullen |
| [`index.html`](index.html) | Dit stuk als leesversie, plakbaar in Word |

## Wat GRC is

GRC staat voor governance, risk en compliance. Het zijn drie vragen die bij elkaar horen:

1. **Sturen.** Wie besluit wat er eerst gebeurt, en op grond waarvan?
2. **Beheersen.** Welke risico's lopen we, en welke maatregelen staan daartegenover?
3. **Aantonen.** Werken die maatregelen, en kunnen we dat laten zien aan de directie, de auditor en de
   toezichthouder?

In de normen heet het geheel een managementsysteem: het ISMS voor informatiebeveiliging, het PIMS voor
privacy, het BCMS voor continuïteit. Alle drie draaien op dezelfde ronde van plannen, doen, controleren en
bijsturen (PDCA). De IBD heeft voor gemeenten een handreiking ISMS en een handreiking risicomanagement; die
beschrijven wat er in zo'n systeem moet zitten. Dit stuk gaat over hoe je het risicodeel ervan zo opzet
dat er een prioriteit uitkomt.

## Waarom één stelsel voor drie disciplines

Security, privacy en continuïteit hebben elk een eigen kader (BIO 2.0, de AVG, ISO 22301), een eigen
functionaris en vaak een eigen toezichthouder. Ze gaan wel over dezelfde processen, dezelfde systemen en
dezelfde directie. Drie losse risicolijsten geven drie prioriteiten die elkaar tegenspreken aan dezelfde
tafel. Een back-up die niet terug te zetten is, is tegelijk een continuïteitsrisico, een
beschikbaarheidsrisico onder BIO 2.0 en een privacyrisico als het om persoonsgegevens gaat.

De Cyberbeveiligingswet maakt dit dringender. De zorgplicht vraagt passende maatregelen op basis van een
risicobenadering, en de bestuurder is aanspreekbaar. Een directie die op drie lijsten moet sturen, kan
moeilijk uitleggen waarom ze koos wat ze koos.

Eén stelsel betekent hier: één register, één manier van scoren, één prioriteitslijst. Elk kader houdt zijn
eigen maatregelen en zijn eigen eigenaar. De functionaris gegevensbescherming toetst privacy, de
BCM-coördinator continuïteit. Alleen de vraag "wat eerst" krijgt één antwoord.

## Twee routes

### Route A: een GRC-tool

Een GRC-tool is software waarin je risico's, maatregelen, controls en bewijs bijhoudt. Wat je ervoor
krijgt:

- workflow: taken, herinneringen, goedkeuringen, wie wat wanneer moet aanleveren;
- bewijsbeheer: per control het bewijsstuk met een vervaldatum;
- koppelingen tussen normen, zodat één maatregel voor BIO 2.0, ISO 27001 en de AVG tegelijk telt;
- een audit trail per record: wie heeft wat wanneer veranderd;
- meerdere gebruikers met rechten, zodat de lijn zelf invult.

Wat het kost: een licentie van een paar honderd tot een paar duizend euro per jaar, afhankelijk van
omvang en hosting. Er zijn ook open en gratis varianten.
[CISO Assistant](https://github.com/intuitem/ciso-assistant-community) heeft een community-editie onder
AGPLv3 met honderden normenkaders, en [Eramba](https://www.eramba.org/) een gratis community-editie voor
eigen hosting. Dan betaal je met beheer in plaats van met een licentie.

De grootste kostenpost is in alle gevallen de tijd. Het normenstelsel moet worden ingericht, de bestaande
lijsten moeten erin, en daarna moet iemand de tool blijven voeden. Een tool die niet gevoed wordt, geeft
een dashboard dat niemand gelooft. Een tool is sterk in het proces: wie, wanneer, met welk bewijs. Welk
risico het zwaarst weegt, moet je hem nog steeds vertellen.

### Route B: een register met afleiding en prioriteit

Route B is een register in platte bestanden (markdown, een spreadsheet of JSON) met vaste regels. Vier
dingen maken het meer dan een spreadsheet:

1. **Een risico volgt uit een bevinding.** Een bevinding is een aangetoond feit over een maatregel die
   niet werkt, met bron en datum. Het risico waar de bevinding onder hangt, wordt afgeleid uit de
   maatregel. Niemand kiest het met de hand, dus het kan niet per persoon verschillen.
2. **Een kaderstand is geen bevinding.** "Niet geïmplementeerd" in de verklaring van toepasselijkheid is
   een zelfbeoordeling. Die telt mee als niveau van de maatregel. Pas een toets, incident, meting, test of
   analyse maakt er een bevinding van.
3. **De prioriteit wordt uitgerekend.** Eerst de maatregelen onder een risico met een aangetoond gat, dan
   de rest op het gewicht van het strategische risico, bij gelijke stand het grootste gat eerst. Wie de
   lijst niet gelooft, kan hem narekenen.
4. **Een AI-assistent leest, de mens beslist.** Een assistent leest nieuwe context (een incidentverslag,
   een auditrapport, een meting) en zet kandidaat-bevindingen klaar in het vaste schema. De CISO beslist
   wat erin komt. De regels voor de assistent staan in [`prompts.md`](prompts.md): hij bedenkt geen
   bevinding, maakt van een kaderstand geen bevinding, kiest geen risico en neemt geen namen of
   exploiteerbare details over.

Wat route B geeft: scherpte, een herleidbare prioriteit en geen licentie. Wat het niet geeft: workflow,
herinneringen en meerdere schrijvers tegelijk. Route B heeft één schrijver nodig die de ronde draait. Valt
die weg, dan is het register een momentopname.

In de herkomstorganisatie liep dit als bestanden in de documentbibliotheek van het managementsysteem, met
een klein script dat het register toetst en de prioriteit uitrekent. Een versie van dat script staat in de
kennisbank (`tools/bouw_risicoregister.py`) en rekent het voorbeeld van Duinstad door. Zonder script kan
het ook: prompt 3 in [`prompts.md`](prompts.md) bouwt de lijst met dezelfde regels.

## Welke route past

| Situatie | Route |
|---|---|
| Je weet nog niet welke risico's het zwaarst wegen, of de bestaande lijst is een opsomming van rode vakjes | Begin met B. Je leert wat je stelsel moet doen |
| Meerdere afdelingen moeten zelf bewijs aanleveren, met herinneringen en termijnen | A, of B voor de prioriteit en A voor het bewijs |
| Er is één informatiebeveiliger en weinig tijd voor beheer | A als SaaS, mits iemand de tool voedt |
| Er komt een externe audit op ISO 27001 of een certificering | A, met de regels van B als eis aan de inrichting |

Het advies: begin met B en koop A pas als je weet wat het stelsel moet doen. Het register is dan de
specificatie waaraan een tool moet voldoen. Een tool die geen onderscheid kan maken tussen een kaderstand
en een aangetoond gat, of die de prioriteit niet kan uitleggen, voldoet niet.

## De ronde, stap voor stap

Het register past op de PDCA-ronde van het managementsysteem. De regels staan uitgewerkt in
[`model.md`](model.md); het voorbeeld in [`voorbeeld-register.md`](voorbeeld-register.md) laat zien wat
eruit komt.

1. **Plan: het register opzetten.**
   a. Strategische risico's (SR) uit de strategische risicoanalyse, met kans en impact. De kans- en
      impacttabellen van de IBD zijn een goede start.
   b. Operationele risico's (OR) uit een standaardlijst per kader: voor BIO 2.0 een risicoformulering per
      ISO 27002-control, voor BCM en privacy per thema van de eigen maatregelenset. Elk OR hangt onder
      precies één SR, of onder "buiten de risicoanalyse" als er geen past.
   c. Maatregelen uit de bronnen die er al zijn: de verklaring van toepasselijkheid, de BCM-set en het
      privacykader. Elke maatregel hangt onder het OR van zijn eigen kader.
2. **Do: de maatregelen inrichten.** Dit is gewoon werk van de beheerseigenaren. Het register volgt de
   stand in de bronnen en schrijft die niet voor.
3. **Check: bevindingen en controls.**
   a. Bevindingen komen uit toetsen, incidenten, metingen, tests en analyses. De
      [risicoanalyse langs aanvalspaden](../../security/risicoanalyse-aanvalspaden/) is een goede eerste
      bron: haar rode cellen zijn aangetoonde gaten.
   b. Controls toetsen of een maatregel werkt (opzet, bestaan, werking). Alleen een toets door de tweede of
      derde lijn telt als werking. Een gemiste toetsronde laat de werking vervallen.
4. **Act: de prioriteit.** De lijst komt uit het register. De risico-eigenaar besluit per risico:
   behandelen, accepteren of overdragen. Een geaccepteerde bevinding blijft zichtbaar en telt niet meer
   mee in de prioriteit.

Daarna begint de ronde opnieuw. Elke nieuwe context loopt door dezelfde vier stappen: lezen, kandidaat,
besluit, opnieuw rekenen.

## Zo begin je

1. Neem de strategische risicoanalyse en zet de risico's in [`sjabloon-register.md`](sjabloon-register.md).
   Geen analyse? Begin met drie: uitval van dienstverlening, verlies van persoonsgegevens, misbruik van
   bevoegdheden.
2. Kies per kader een standaardlijst voor de OR's en koppel elk OR aan een SR.
3. Zet de maatregelen erin met hun stand uit de bron. Dat is overtypen, geen beoordeling.
4. Plak het laatste auditrapport, het incidentregister van dit jaar en de laatste managementletter in
   prompt 1. Beoordeel de kandidaten één voor één.
5. Laat de prioriteit uitrekenen, met het script of met prompt 3, en leg de lijst voor aan de directie.

Reken voor de eerste vulling op een paar dagen werk van de CISO, waarvan het meeste in stap 4 zit.

## Wat dit niet is

- Geen restrisicoberekening. De prioriteit is een rangorde. Of een restrisico aanvaardbaar is, besluit
  de risico-eigenaar, met de acceptatieladder van de eigen risicoanalyse.
- Geen vervanging van de toets door de functionaris gegevensbescherming of de BCM-coördinator. Het
  register neemt hun oordeel over als bevinding of als stand.
- Geen eigenarenoverzicht. Het register noemt per maatregel de beheerseigenaar uit de bron; wie welk
  risico draagt, staat in het risicoregister van de organisatie zelf.

## Licentie

EUPL-1.2, zoals alles in de kennisbank.
