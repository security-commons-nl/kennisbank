---
titel: Quantumveilig per laag, wat bestuur, directie, CISO, IT en inkoop nu doen
vakgebied: governance
type: aanpak
normen: [BIO2, Cbw, NIS2, AVG]
peildatum: 2026-10-28
herkomst: samengesteld uit de rijksbronnen over quantumveilige cryptografie (AIVD, CWI en TNO, CIO Rijk, Digitale Overheid) door de CISO-organisatie van een gemeente, voor gebruik in de hele publieke sector
status: concept
samenvatting: Wat een quantumcomputer kapotmaakt is niet de toekomst maar het heden, want wat je vandaag versleuteld verstuurt kan rond 2030 open op straat liggen. Dit stuk vertaalt de rijkshandreikingen naar één pagina per laag van de organisatie, van bestuur tot inkoop, met per laag wat je nu doet, wat daarna komt en wanneer het klaar moet zijn. Vijf vragen vooraf bepalen welke variant voor jouw organisatie geldt. Met per laag een set platen om het gesprek te openen.
bronnen: [aivd-bescherm-je-nu-tegen-quantumcomputers-2026, aivd-pqc-migratie-handboek, ciorijk-rijksbreed-beleidskader-cryptografie, ciorijk-pqc-migratie-tijdpad-quantumstrategie, do-quantumveilig-bereid-je-voor, do-quantumveilig-handige-hulpmiddelen]
---

# Quantumveilig per laag, wat bestuur, directie, CISO, IT en inkoop nu doen

> **Lees de aanpak online:** [security-commons-nl.github.io/kennisbank/governance/quantumveilig-per-laag](https://security-commons-nl.github.io/kennisbank/governance/quantumveilig-per-laag/)

Een quantumcomputer die de huidige versleuteling breekt bestaat nog niet. Toch is het risico er nu al, om
drie redenen die de AIVD in maart 2026 opnieuw op een rij zette:

1. **Store now, decrypt later.** Wat een aanvaller vandaag onderschept en bewaart, ontcijfert hij zodra de
   computer er is. Alles met een vertrouwelijkheidstermijn die tot na dat moment loopt is dus nu al kwetsbaar.
2. **De migratie duurt langer dan vijf jaar.** Eerdere, kleinere cryptografische overgangen leren dat. Wie
   in 2030 veilig wil zijn, moet in 2026 beginnen.
3. **Apparatuur met een lange levensduur** (OT, gemalen, tunnels, meetnetten, chipkaarten) is na
   ingebruikname vaak niet meer bij te werken. Wat je nu koopt, bepaalt of je in 2035 nog kwetsbaar bent.

De AIVD adviseert te rekenen met een quantumcomputer in **2030**. Experts schatten de kans op zo'n computer
in 2029 op 5 tot 14 procent en in 2034 op 19 tot 34 procent. Voor gevoelige informatie is een kleine kans
al genoeg om nu te handelen.

Het Rijk heeft daar een tijdpad voor vastgesteld (Rijksbrede Quantumstrategie, 5 oktober 2026). Dat
tijdpad is verplicht voor rijksorganisaties en richtinggevend voor de rest van de publieke sector. Dit stuk
vertaalt dat tijdpad en de handreikingen van AIVD, CWI, TNO en Digitale Overheid naar wat elke laag van
een organisatie concreet doet. Niet omdat het Rijk het zegt, maar omdat de redenering per laag anders is.

## Wat er in deze map staat

- Deze pagina: de vijf vragen vooraf, de acties per laag, het tijdpad en de no-regret moves.
- Vijf sets platen, een per gremium, om het gesprek te openen. Elke set begint met één beeld dat het
  probleem tastbaar maakt en eindigt met het besluit of de handeling die van dat gremium wordt gevraagd:
  [platen-bestuur.html](platen-bestuur.html) · [platen-directie.html](platen-directie.html) ·
  [platen-ciso-privacy.html](platen-ciso-privacy.html) · [platen-it.html](platen-it.html) ·
  [platen-inkoop.html](platen-inkoop.html). Openen in een browser, bladeren met de pijltjestoetsen;
  afdrukken geeft een plaat per A4 met de feiten open.
- De vijf beelden los als SVG, voor gebruik in een eigen presentatie:
  [op straat](img/op-straat.svg) · [verbouwing](img/verbouwing.svg) · [Mosca](img/mosca.svg) ·
  [inventaris](img/inventaris.svg) · [levensduur](img/levensduur.svg). In PowerPoint: invoegen als
  afbeelding en daarna converteren naar vorm; de tekst blijft tekst.
- De inhoud van de platen staat in [data/platen.json](data/platen.json). Wie een plaat wil aanpassen,
  wijzigt dat bestand en draait `python tools/bouw_quantumplaten.py`; de html en de svg's worden daaruit
  gemaakt.

## Vijf vragen vooraf

De bronnen schrijven één route voor, maar de urgentie en de rolverdeling verschillen per organisatie.
Beantwoord deze vijf vragen eerst; de blokken per laag verwijzen ernaar.

| # | Vraag | Wat het antwoord verandert |
|---|---|---|
| 1 | Ben je rijksorganisatie, decentrale overheid (gemeente, provincie, waterschap) of uitvoeringsorganisatie? | **Rijk:** het tijdpad hieronder is verplicht. **Overig:** richtinggevend; de eigen haken zijn BIO 2.0 maatregel 8.24 (cryptografie), de zorgplicht van de Cbw en de AVG voor persoonsgegevens. |
| 2 | Heb je gegevens die na 2030 nog vertrouwelijk moeten zijn? Persoonsgegevens met lange bewaartermijn, medische, justitiële of jeugdzorggegevens, gerubriceerde informatie. | **Ja:** je bent een *urgente adopter* in de termen van het handboek. Store now, decrypt later geldt nu al; bestuur besluit dit jaar. **Nee:** reguliere adopter, je volgt het tijdpad zonder versnelling. |
| 3 | Heb je systemen die na 2030 nog draaien en niet bij te werken zijn? OT, gemalen, bruggen, tunnels, verkeersinstallaties, meetnetten, toegangspassen. | **Ja:** vervanging en inkoopeisen gaan nu het meerjarenplan in, niet pas in 2028. De lagen inkoop en IT krijgen voorrang. |
| 4 | Beheer je zelf cryptografie (eigen PKI, eigen applicaties, eigen VPN of koppelvlakken) of koop je vrijwel alles in als dienst? | **Zelf:** de IT-laag voert de migratie uit. **Inkoop:** de leveranciers dragen de migratie, IT toetst en inkoop stuurt. De meeste gemeenten zitten in de tweede groep. |
| 5 | Heb je al een cryptografiebeleid en een register van sleutels en certificaten? | **Nee:** begin bij stap 1 (diagnose). **Ja:** begin bij stap 2 (planning) en toets het beleid aan het Rijksbreed Beleidskader Cryptografie. |

## De drie stappen die elke bron deelt

AIVD, CWI en TNO beschrijven de migratie in drie stappen. Alles hieronder hangt daaraan.

1. **Diagnose van quantumkwetsbaarheid.** Inventariseer de te beschermen gegevens, de cryptografische
   componenten en de afhankelijkheden (ook bij leveranciers), en beoordeel het risico. Gebruik Mosca's
   ongelijkheid: als vertrouwelijkheidstermijn plus migratietijd langer is dan de tijd tot de
   quantumcomputer, ben je nu al te laat.
2. **Plan de migratie.** Schat de migratietijd, bepaal welke apparatuur over kan en welke vervangen moet,
   benoem de knelpunten (niet bij te werken apparatuur, interoperabiliteit met ketenpartners, beperkte
   rekenkracht) en wijs een migratiemanager aan.
3. **Voer de migratie uit.** Hybride constructies (klassiek plus post-quantum), de gestandaardiseerde
   algoritmen (ML-KEM of FrodoKEM voor sleuteluitwisseling, AES-256 symmetrisch) en crypto-agility, zodat
   een volgende wissel niet opnieuw vijf jaar kost.

## Per laag: nu, daarna, klaar wanneer

### Bestuur: college, raad, dagelijks bestuur, raad van toezicht

**Waarom deze laag.** Dit is de laag waar het gat zit. De techniek kan beginnen zonder bestuur, maar het
budget, de prioriteit en de risicobereidheid niet. En het is een bestuurlijk risico: de gegevens die het
hardst raken zijn die van inwoners en cliënten.

**Nu (2026)**
- Neem het quantumrisico op in het risicoregister van de organisatie, met een eigenaar op directieniveau
  en een expliciete uitspraak over risicobereidheid. Voor het Rijk is dit verplicht uiterlijk eind 2026.
- Stel het cryptografiebeleid vast, of geef opdracht het te maken, langs het Rijksbreed Beleidskader
  Cryptografie. Ook verplicht Rijk eind 2026.
- Vraag één overzicht: welke gegevens van ons moeten na 2030 nog geheim zijn, en waar staan ze.

**Daarna (2027 en 2028)**
- Reserveer mensen en geld voor de migratie in de meerjarenbegroting (Rijk: eind 2027).
- Laat de inkoopvoorwaarden aanpassen, zodat geen nieuw systeem meer binnenkomt zonder quantumveilige
  cryptografie of een migratiepad (Rijk: eind 2028).

**Klaar wanneer.** Eind 2030 zijn de scenario's met hoog risico gemigreerd. Dat haal je alleen als het
besluit in 2026 valt.

**Verschilt als.** Vraag 2 ja: dit is geen agendapunt voor 2027 maar voor de volgende vergadering.
Vraag 1 decentraal: het tijdpad is niet afdwingbaar, de zorgplicht onder de Cbw en de AVG wel; leg het
besluit vast als eigen keuze, niet als rijksopdracht.

### Directie, MT en CIO

**Waarom deze laag.** De migratie is geen IT-project maar een verbouwing van het hele pand terwijl de
winkel open blijft. Elke afdeling heeft gegevens, elke afdeling heeft leveranciers. Zonder sturing vanuit
de directie blijft het bij de ICT-afdeling hangen.

**Nu**
- Wijs een migratiemanager aan: iemand met overzicht over de hele organisatie en toegang tot alle
  afdelingen. Het handboek noemt dit de eerste stap van de planning.
- Geef de diagnose (stap 1) opdracht en termijn, en koppel hem aan de bestaande processen:
  gegevensclassificatie, risicomanagement, assetmanagement, leveranciersmanagement.
- Zet quantum als vaste vraag in de projectportfolio: elk nieuw systeem beantwoordt "hoe migreert dit".

**Daarna**
- Conceptmigratieplanning met praktijkproeven voor de scenario's met hoog en gemiddeld risico (Rijk: eind 2027).
- Inzicht in benodigde mensen en middelen, verwerkt in de begroting (Rijk: eind 2027).
- Gebruik het groeimodel uit het handboek (acht prioriteiten: samenwerking, bewustwording, bestuur, beleid,
  beschikbaarheid van PQC, hybride aanpak, strategie, kennis) om jaarlijks te meten waar je staat.

**Klaar wanneer.** Eind 2027 ligt de planning, eind 2030 is hoog risico over.

**Verschilt als.** Vraag 4 inkoop: de migratiemanager stuurt vooral leveranciers en contracten, niet
engineers. Vraag 3 ja: de planning begint bij de vervangingskalender van de OT, niet bij de kantoor-IT.

### CISO, informatiebeveiliging, privacy en FG

**Waarom deze laag.** Hier wordt het risico uitgerekend. En hier zit de link met privacy: persoonsgegevens
met een lange bewaartermijn zijn de urgentste categorie. Het handboek noemt overheden, de zorg en
financiële instellingen met name als organisaties waarvoor de dreiging voor persoonsgegevens nu al groot
is. Een wet die dit specifiek regelt is er nog niet, maar het handboek acht het waarschijnlijk dat
beheerders van die gegevens aanspreekbaar zijn als ze later alsnog worden ontsleuteld.

**Nu**
- Bepaal de persona van de organisatie (urgente of reguliere adopter) met de vragen 2 en 3.
- Voer de diagnose uit: te beschermen belangen, cryptografische componenten, afhankelijkheden,
  risicobeoordeling. Werk met quantumrisicoscores per gebruiksscenario (impact maal kwetsbaarheid maal
  migratiemoeite) zodat de planning op feiten rust.
- Herzie het cryptografiebeleid langs het Rijksbreed Beleidskader: verplichte hoofdstukken (bijlage A),
  per technisch aspect aanbevolen, toegestaan, uit te faseren of niet toegestaan, register van sleutels
  en certificaten met quantumveiligheidsniveau, crypto-agility, geen DV-certificaten.
- Neem quantum op in de DPIA-vragen: bewaartermijn versus 2030.

**Daarna**
- Halfjaarlijkse toets of nieuwe adviezen van NCSC, NBV en AIVD de inzet veranderen (BIO 2.0 8.24.04).
- Praktijkproeven begeleiden en de risicoscores bijwerken; de inventaris is nooit af.

**Klaar wanneer.** Diagnose en beleid in 2026, planning in 2027.

**Verschilt als.** Vraag 5 ja: sla de inventarisatie niet over maar toets hem; de meeste registers kennen
wel de certificaten en niet de cryptografie in applicaties en koppelvlakken.

### Architectuur en IT-beheer

**Waarom deze laag.** Van elke laptop weet je waar hij is; van geen enkel certificaat. De cryptografische
inventaris is de CMDB voor sleutels, en zonder die inventaris is elke planning een gok.

**Nu**
- Zet cryptografisch componentbeheer op: welke algoritmen, sleutellengten, protocollen, certificaten en
  bibliotheken draaien waar, met eigenaar en levensduur. Dit is een no-regret move: het verkort ook nu
  al de responstijd bij een gelekte sleutel of een verlopen certificaat.
- Verhoog symmetrische sleutels naar 256 bits (AES-256 geldt als quantumveilig).
- Voer de voorbereidende wijzigingen door: TLS 1.2 naar TLS 1.3, verouderde protocollen uit.
- Toets apparatuur en software op crypto-agility: kan dit systeem van algoritme wisselen zonder vervanging.

**Daarna**
- Hybride constructies invoeren waar de leverancier of de eigen bouw het toelaat; ML-KEM of FrodoKEM voor
  sleuteluitwisseling, FrodoKEM waar meer zekerheid gewenst is.
- Eigen PKI: migratieplan voor root- en tussencertificaten, want die hebben een lange geldigheid.
- Crypto-agility inbouwen in change management, zodat een volgende algoritmewissel een gewone wijziging is.

**Klaar wanneer.** Volwassen cryptografisch assetmanagement eind 2027 (Rijk), hoog risico gemigreerd eind
2030, software en firmware standaard quantumveilig eind 2030.

**Verschilt als.** Vraag 4 inkoop: de inventaris bestaat dan vooral uit vragen aan leveranciers; de
Infoset Quantumveilige Cryptografie van Digitale Overheid is de gespreksleidraad. Vraag 3 ja: OT en
meetapparatuur krijgen een eigen spoor met de vervangingskalender als leidraad; vaak is tunneling door een
symmetrisch beveiligde verbinding de enige tussenoplossing.

### Inkoop en contractmanagement

**Waarom deze laag.** Je koopt nu een gemaal dat tot 2045 draait, met een slot dat in 2030 open kan. De
goedkoopste maatregel van allemaal is één zin in de aanbesteding.

**Nu**
- Neem eisen voor quantumveilige cryptografie, of een aantoonbaar migratiepad, op in elke aanbesteding
  en elk nieuw contract. Digitale Overheid noemt dit als eerste stap, nu, niet later.
- Stel de leverancier van elk bestaand systeem één vraag: wanneer is uw product quantumveilig, en wat
  is uw migratiepad. Leg het antwoord vast in het contractdossier.
- Gebruik de Infoset Quantumveilige Cryptografie (Digitale Overheid) als vragenlijst voor dat gesprek.

**Daarna**
- Contractmanagement: de toezegging van de leverancier wordt een contractuele mijlpaal met datum.
- Vervangingskalender: systemen die niet kunnen migreren krijgen een einddatum vóór 2030.

**Klaar wanneer.** Rijk: eind 2028 structureel eisen en wensen stellen, met aandacht voor
contractmanagement, beheer en uitvoering. Voor wie vraag 3 met ja beantwoordt: nu.

**Verschilt als.** Vraag 1 decentraal: gebruik de gezamenlijke inkoopvoorwaarden (GIBIT) en de
collectieve kanalen; een leverancier beweegt sneller voor tweehonderd gemeenten dan voor één.

## Het rijkstijdpad, en wat het voor de rest betekent

| Uiterlijk | Rijksorganisaties (verplicht) | Rest van de publieke sector (richtinggevend) |
|---|---|---|
| eind 2026 | Quantumrisico in het risicomanagement. Eigen cryptografiebeleid conform het Rijksbreed Beleidskader. | Zelfde twee stappen; ze vallen samen met BIO 2.0 8.24 en de zorgplicht van de Cbw. |
| eind 2027 | Conceptmigratieplanning en praktijkproeven voor hoog en gemiddeld risico. Volwassen cryptografisch assetmanagement. Mensen en middelen in de begroting. | Planning en inventaris; budget in de meerjarenbegroting. |
| eind 2028 | Bij inkoop en aanbesteding eisen stellen over quantumveilige cryptografie, inclusief contractmanagement en beheer. | Eisen in aanbestedingen nu al; eind 2028 als uiterste. |
| eind 2030 | Migratie voor hoog risico voltooid. Software en firmware standaard quantumveilig. | Zelfde doel; de datum waarop store now, decrypt later werkelijkheid kan zijn. |
| eind 2035 | Migratie voor gemiddeld risico voltooid, laag risico zo ver mogelijk. | Zelfde doel. |

Het tijdpad kan worden bijgesteld of versneld als het dreigingsbeeld verandert. Een organisatie mag
sneller gaan als haar risicobereidheid daar aanleiding toe geeft.

## No-regret moves

Het handboek noemt acht stappen die nuttig zijn ongeacht wanneer de quantumcomputer komt. Gebruik ze als
checklist bij elke laag:

- Beoordeel de afhankelijkheden in de toeleveringsketen.
- Zet cryptografisch componentbeheer op.
- Herzie het cryptografisch beleid.
- Voer een quantumrisicobeoordeling uit binnen het bestaande risicomanagement.
- Schat de kosten van de migratie, in geld en in capaciteit.
- Inventariseer de regelgeving (Cbw, AVG, sectorregels) die PQC gaat vereisen.
- Zorg voor een back-upplan voor als de dreiging eerder komt of een standaard breekt.
- Werk samen met gelijksoortige organisaties; interoperabiliteit dwingt dat af.

## Bewijs

Wat je aan het eind van elke stap kunt laten zien:

- Een regel in het risicoregister met eigenaar, risicobereidheid en datum.
- Een vastgesteld cryptografiebeleid met de hoofdstukken van bijlage A van het Beleidskader.
- Een register van sleutels, certificaten en cryptografische componenten met quantumveiligheidsniveau.
- Een migratieplanning met risicoscores per scenario en een migratiemanager.
- Aanbestedingsteksten en contractclausules met de eis en de mijlpaal.
- Antwoorden van leveranciers in het contractdossier.

## Zo leg je het uit

**Aan het bestuur.** Alles wat we nu versleuteld opslaan of versturen, kan rond 2030 open op straat liggen:
de bijstandsdossiers, de jeugdzorgverslagen, het mailverkeer van dit bestuur. Het slot op de deur werkt nog,
maar de sleutel ligt al bij de inbreker in de 3D-printer. Eén besluit nu: het risico op de lijst, een
eigenaar, en geld in de meerjarenbegroting.

**Aan de directie.** Dit is een verhuizing van het hele pand terwijl de winkel open blijft. Vijf jaar,
elke afdeling, elke leverancier. Zonder een migratiemanager en een planning blijft het bij ICT hangen en
halen we 2030 niet.

**Aan de informatiemanager en de inkoper.** De goedkoopste maatregel is één zin in de aanbesteding en één
vraag aan elke leverancier. Wat we nu kopen zonder die zin, draait in 2035 nog met een slot dat open kan.

## Hoe dit samenhangt

- De beleidsset informatiebeveiliging op BIO 2.0 bevat een hoofdstuk cryptografie; maatregel 3 daarvan
  (halfjaarlijkse toets, voorbereiding op quantumveilige cryptografie) is het haakje voor deze aanpak.
- De Cbw-zorgplicht en NIS2 artikel 21 vragen passende maatregelen; het Beleidskader mapt zijn eisen op
  BIO, ISO 27002 8.24 en NIS2 21(2)(h).
- Voor OT-objecten (gemalen, bruggen, tunnels) sluit dit aan op de CSIR-assessment-tool, waar de levensduur
  van een object de urgentie bepaalt.
- De hulpmiddelenpagina van Digitale Overheid bundelt ruim dertig bronnen in vijf rubrieken (leren,
  publiek-private samenwerking, strategie, beleid en wetgeving, tools); daar staan ook het HAPKIDO-handboek
  voor quantumveilige PKI, de PQChoiceAssistant van TNO en CWI en de marktverkenning van tooling voor
  cryptografische asset discovery.

## Licentie

[EUPL-1.2](../../LICENSE).
