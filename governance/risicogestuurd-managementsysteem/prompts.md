# Prompts: een AI-assistent als lezer, binnen vaste regels

Bijlage bij [GRC voor security, privacy en continuïteit](README.md). Drie prompts om in een AI-assistent te
plakken. Elke prompt is zelfstandig: hij bevat het schema en de regels, zodat de uitkomst altijd dezelfde
vorm heeft, welke assistent je ook gebruikt. Vul tussen de vierkante haken je eigen materiaal in.

Plak geen materiaal in een assistent die daar niet voor is goedgekeurd. Incidentverslagen en auditrapporten
zijn vaak vertrouwelijk. Gebruik de assistent die je organisatie voor vertrouwelijke informatie heeft
ingericht, of haal namen en technische details eruit voordat je plakt.

## De regels die in elke prompt staan

De assistent:

1. bedenkt geen bevinding. Zonder vastgesteld feit, datum en bron is het een zorg; die krijgt een reden
   waarom het geen bevinding is;
2. maakt van een kaderstand nooit een bevinding. "Niet geïmplementeerd", rood of "niet voltooid" telt al
   mee via het niveau;
3. kiest geen risico. Het operationele en het strategische risico volgen uit de maatregel;
4. schrijft rollen in plaats van namen, en neemt geen exploiteerbare details over: geen hostnamen,
   IP-adressen, accountnamen, configuratie of kwetsbaarheid per systeem;
5. laat stukken over personen liggen: functioneren, inhuur, dienstverband, gezondheid;
6. laat een bron liggen die hij niet helemaal heeft kunnen lezen, en zegt dat;
7. levert kandidaten. De mens besluit welke erin komen.

## Prompt 1: van context naar kandidaat-bevindingen

```text
Je helpt een CISO bij het bijhouden van een risicoregister voor informatiebeveiliging, privacy en
bedrijfscontinuïteit. Lees de context hieronder volledig en maak kandidaat-bevindingen in het schema.

Een bevinding is een aangetoond feit dat laat zien dat een maatregel niet werkt, of niet bestaat terwijl
de organisatie denkt dat hij er is. Een bevinding heeft een feit, een datum en een bron.

Regels:
1. Bedenk niets. Staat er geen vastgesteld feit met datum en bron, dan is het geen bevinding. Zet het
   onder "geen bevinding" met de reden.
2. Een kaderstand ("niet geïmplementeerd", rood, "niet voltooid") is nooit een bevinding.
3. De titel is het gat als patroon, niet de gebeurtenis. De gebeurtenis is bewijs en staat onder
   "aangetoond". Maak de titel breder dan het incident als het bewijs dat draagt: minstens twee
   onafhankelijke bewijsstukken, of één meting over de hele populatie. Anders blijft de titel smal.
4. Noem per bevinding de maatregel(en) die aantoonbaar niet werken, met sleutel en reden. Kies uit de
   maatregelenlijst hieronder. De eerste maatregel is de belangrijkste. Kies geen operationeel of
   strategisch risico; dat wordt afgeleid.
5. Past geen enkele maatregel, zet dan "uitzondering" met het operationele risico en een motivering.
6. Geef een voorstel voor kans en impact, elk 1 tot en met 5, met één zin onderbouwing. Het blijft een
   voorstel.
7. Rollen in plaats van namen. Geen hostnamen, IP-adressen, accountnamen, configuratie of kwetsbaarheid
   per systeem. Geen stukken over personen.
8. Heb je de context niet helemaal kunnen lezen, zeg dat en stop.

Lever JSON in deze vorm, en niets anders:
{
  "kandidaten": [
    {
      "titel": "...",
      "aangetoond": "wat is vastgesteld, door welke rol, wanneer",
      "bronsoort": "toets | incident | meting | test | analyse",
      "bron": "document en vindplaats",
      "peildatum": "JJJJ-MM-DD",
      "maatregelen": [{"sleutel": "...", "reden": "..."}],
      "kans": 1, "impact": 1,
      "onderbouwing_score": "...",
      "status": "kandidaat"
    }
  ],
  "geen_bevinding": [
    {"wat": "...", "reden": "kaderstand | zorg zonder feit | over een persoon | ..."}
  ],
  "weggelaten_details": ["soort detail dat is weggelaten, zonder het detail zelf"]
}

Maatregelenlijst (sleutel, omschrijving):
[plak hier de maatregelen uit je register, één per regel]

Context:
[plak hier het verslag, rapport, de meting of de mail]
```

### Voorbeeld: een verzonnen incidentverslag

Context, geplakt in prompt 1 met de maatregelen uit het [voorbeeld van Duinstad](voorbeeld-register.md):

```text
Evaluatie incident 2026-031, gemeente Duinstad, 18 september 2026.
Op zaterdag 6 september om 02:14 meldde de leverancier van de beveiligingsmonitoring een verdachte
aanmelding op beheeraccount adm-[naam] op server DS-APP-07. De melding kwam binnen in de gedeelde
mailbox van het team. Niemand las die mailbox in het weekend; de melding is maandag om 08:40 gezien.
Toen bleek dat de aanvaller zondag een tweede beheeraccount had aangemaakt. Beide accounts zijn maandag
om 09:30 geblokkeerd. Er is geen data buitgemaakt, voor zover bekend.
In juni ging een vergelijkbare melding over een werkplek pas na 61 uur naar iemand die kon handelen.
In de verklaring van toepasselijkheid staat 8.16.01 op niet geïmplementeerd.
Het team maakt zich zorgen dat de leverancier bij een volgend incident ook niet belt.
Collega [naam] had die zaterdag dienst maar was ziek.
```

Wat de assistent hoort terug te geven:

```json
{
  "kandidaten": [
    {
      "titel": "Beveiligingsmeldingen buiten kantoortijd worden niet opgevolgd",
      "aangetoond": "Evaluatie incident 2026-031 (18-09-2026): melding van verdachte aanmelding op een beheeraccount op zaterdag 02:14 kwam in een gedeelde mailbox en werd maandag 08:40 gezien; de aanvaller maakte intussen een tweede beheeraccount aan. Ook in juni ging een vergelijkbare melding pas na 61 uur naar iemand die kon handelen.",
      "bronsoort": "incident",
      "bron": "evaluatie incident 2026-031, 18-09-2026",
      "peildatum": "2026-09-06",
      "maatregelen": [
        {"sleutel": "BIO2:8.16.01", "reden": "meldingen worden buiten kantoortijd niet opgevolgd"},
        {"sleutel": "BIO2:8.02.01", "reden": "een aanvaller kon met een beheeraccount een nieuw beheeraccount aanmaken"}
      ],
      "kans": 4, "impact": 4,
      "onderbouwing_score": "twee keer in vier maanden; een beheeraccount geeft toegang tot de hele omgeving",
      "status": "kandidaat"
    }
  ],
  "geen_bevinding": [
    {"wat": "8.16.01 staat op niet geïmplementeerd", "reden": "kaderstand; telt al mee via het niveau"},
    {"wat": "zorg dat de leverancier bij een volgend incident niet belt", "reden": "zorg zonder feit; de leverancier meldde dit keer wel"},
    {"wat": "bezetting van de dienst die zaterdag", "reden": "over een persoon"}
  ],
  "weggelaten_details": ["naam van een beheeraccount", "servernaam", "naam van een medewerker"]
}
```

De CISO beslist daarna: nieuwe bevinding, feit onder een bestaande, of afwijzen. In Duinstad staat al B-05
"Activiteit van beheeraccounts wordt niet bewaakt" op dezelfde maatregel. Dan is de vraag of dit incident
bewijs onder B-05 is, of een eigen gat (de opvolging, los van de detectie). Dat oordeel maakt de mens.

## Prompt 2: een bevinding toetsen

Voor een kandidaat die er al staat, of een bevinding die je wilt herzien.

```text
Toets de bevinding hieronder aan de regels van een risicoregister. Geef per regel "voldoet" of "voldoet
niet", met één zin waarom, en een voorstel als iets niet voldoet. Verander zelf niets.

Regels:
1. Het is een aangetoond feit met datum en bron, geen zorg of verwachting.
2. Het is geen kaderstand ("niet geïmplementeerd", rood, "niet voltooid").
3. De titel is het gat als patroon, en is smaller dan het operationele risico waar hij onder valt.
4. De titel wordt gedragen door het bewijs: minstens twee onafhankelijke bewijsstukken, of één meting over
   de hele populatie.
5. De bevinding is sluitbaar: er is één eigenaar denkbaar, en te zeggen hoe "opgelost" eruitziet.
6. Elke genoemde maatregel heeft een reden, en de eerste maatregel is de belangrijkste.
7. Er staan geen namen, hostnamen, accountnamen, configuratie of kwetsbaarheid per systeem in.
8. De peildatum is niet ouder dan twaalf maanden, of het feit is herbevestigd.

Leid daarna af, uit de koppeltabel hieronder:
- het primaire operationele risico: het risico van de eerste maatregel;
- de secundaire operationele risico's: die van de overige maatregelen, zonder het primaire;
- het strategische risico: dat van het primaire operationele risico.

Koppeltabel (maatregel, operationeel risico, strategisch risico):
[plak hier de koppeling uit je register]

Bevinding:
[plak hier de bevinding]
```

## Prompt 3: de prioriteit opnieuw opbouwen

Voor wie het script niet draait. De prompt rekent met dezelfde regels als `tools/bouw_risicoregister.py`;
controleer de eerste keer de uitkomst tegen het [voorbeeld van Duinstad](voorbeeld-register.md) door dat
register te plakken en de volgorde te vergelijken.

```text
Bouw uit het register hieronder de prioriteitslijst van de maatregelen. Volg de regels precies en reken
niets anders uit dan wat er staat. Laat bij elke stap zien wat je hebt berekend.

Stap 1, meetellende bevindingen: alleen status "open" of "in behandeling".
Stap 2, per bevinding: score = kans × impact. Primair operationeel risico = het risico van de eerste
maatregel. Strategisch risico = dat van het primaire operationele risico.
Stap 3, per operationeel risico: score = hoogste score van de meetellende bevindingen waarvan het het
primaire risico is. Geen zulke bevinding: "niet beoordeeld".
Stap 4, per maatregel het niveau (0 niet in orde, 1 opzet, 2 bestaan, 3 werking):
  a. BIO 2.0: geïmplementeerd = 2, anders 0. BCM: voltooid = 2, deels = 1, niets = 0. Privacy: werking,
     bestaan en opzet groen = 3; bestaan en opzet groen = 2; opzet groen = 1; anders 0. Oranje telt niet.
  b. Heeft de maatregel getoetste controls: neem het laagste niveau van die controls (opzet, bestaan,
     werking cumulatief). Werking vervalt naar 2 als de toets langer geleden is dan de frequentie, gerekend
     vanaf de peildatum van het register.
  c. Heeft de maatregel een meetellende bevinding: niveau hooguit 2.
Stap 5, sorteer de maatregelen:
  a. eerst de maatregelen waarvan het operationele risico een score heeft, op die score van hoog naar laag;
  b. dan de rest;
  c. binnen a en b op de score van het strategische risico, van hoog naar laag; buiten de risicoanalyse
     telt als 0;
  d. bij gelijke stand het laagste niveau eerst, dan op sleutel.

Lever een tabel: plek, sleutel, omschrijving, operationeel risico, niveau, bevindingen, waarom op deze plek.
Zet daaronder elke regel die je niet kon toepassen, met de reden.

Register:
[plak hier het register]
```

## Waarom deze verdeling

Lezen en structureren is werk waar een assistent goed in is: een verslag van drie pagina's teruggebracht
tot één feit in een vast schema. Oordelen is dat niet. Of een incident een eigen gat is of bewijs onder een
bestaande bevinding, en hoe zwaar het weegt, hangt af van wat de CISO weet over de organisatie. Daarom levert
prompt 1 kandidaten en geen bevindingen, en daarom zet prompt 2 niets zelf recht. Rekenen kan een assistent
ook, maar een script doet het elke keer hetzelfde. Gebruik prompt 3 om te beginnen en het script zodra het
register groeit.
