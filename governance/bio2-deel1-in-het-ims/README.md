---
titel: BIO 2.0 deel 1 in één managementsysteem, met negen artefacten en vijf sjablonen
vakgebied: governance
type: aanpak
normen: [BIO2, ISO 27001, Cbw, ISO 22301, AVG]
peildatum: 2026-10-20
herkomst: voorstel van de CISO en vijf conceptproducten voor het managementsysteem van een regionale samenwerking van vier gemeenten (september en oktober 2026), nog niet vastgesteld
status: concept
route: geen
samenvatting: BIO 2.0 deel 1 vraagt een managementsysteem volgens ISO 27001, en de BIO zegt zelf dat je security, privacy en continuïteit in één systeem mag onderbrengen met aparte maatregelensets. Deze aanpak laat zien hoe dat werkt, beantwoordt het bezwaar dat de drie disciplines niet te verenigen zijn, brengt de vijftien producten uit een gangbaar plan van aanpak terug tot negen artefacten, geeft een dekkingsmatrix per eis van deel 1 en de zeven beslispunten die je moet doorhakken. Met sjablonen voor contextanalyse, risicomanagementbeleid, doelstellingen en KPI's, intern auditprogramma en de procedure voor afwijkingen en correctieve maatregelen.
pijler: bio2-implementeren
---

# BIO 2.0 deel 1 in één managementsysteem, met negen artefacten en vijf sjablonen

> **Lees de aanpak online:** [security-commons-nl.github.io/kennisbank/governance/bio2-deel1-in-het-ims](https://security-commons-nl.github.io/kennisbank/governance/bio2-deel1-in-het-ims/)

Een plan van aanpak voor BIO 2.0 deel 1 telt al snel vijftien producten, elk met een eigenaar en een
urenraming (zie [BIO 2.0 invoeren](../bio2-implementeren/)). Tegelijk heeft een gemeente vaak al een handboek
voor een geïntegreerd managementsysteem (IMS) voor security, privacy en continuïteit. Dan rijst de vraag:
bouwen we naast het IMS een tweede systeem voor de BIO, of past deel 1 erin?

Het antwoord van dit stuk: **één managementsysteem, drie implementatieplannen.** Het handboek beschrijft het
systeem (context, governance, risicoproces, audit, directiebeoordeling, verbetering) voor de drie disciplines
samen. Daaronder gaat elk implementatieplan zo diep als zijn norm vraagt: BIO deel 1 en 2 voor het ISMS, een
werkmap voor privacy, een werkmap voor continuïteit.

## Wat er in deze map staat

- [contextanalyse-sjabloon.md](contextanalyse-sjabloon.md): context en belanghebbenden (ISO 27001, 4.1 en 4.2),
  met het wettelijk kader en de eisen die uit de context volgen.
- [risicomanagementbeleid-sjabloon.md](risicomanagementbeleid-sjabloon.md): de risicoprocedure (6.1, 8.2,
  8.3), met rollen, zes stappen, klassen, acceptatieladder en registervelden.
- [doelstellingen-en-kpi-sjabloon.md](doelstellingen-en-kpi-sjabloon.md): doelstellingen en indicatoren (6.2,
  9.1) op twee niveaus, met meetplan en rekenregels.
- [auditprogramma-sjabloon.md](auditprogramma-sjabloon.md): intern auditprogramma over drie jaar (9.2), met
  onafhankelijkheid, diepgang, prioritering en spelregels.
- [afwijkingenprocedure-sjabloon.md](afwijkingenprocedure-sjabloon.md): afwijkingen en correctieve maatregelen
  (10.1, 10.2), met ernst en termijnen en een verbeterregister.

## Wat BIO 2.0 deel 1 eist

Deel 1 (Staatscourant 2026, 7416) is een kader van achttien hoofdstukken, geen productenlijst. De harde eisen:

1. Het managementsysteem voldoet aan ISO 27001, clausules 4 tot en met 10.
2. De reikwijdte omvat minimaal de bedrijfsprocessen en informatiesystemen die kritiek zijn voor de dienstverlening.
3. De risicomethodiek heeft vier onderdelen: een quickscan met classificatie van proces en systeem, een methode
   voor de volledige risicoanalyse, een risicoregister met de tijdelijk geaccepteerde risico's, en een opvolgproces.
4. Een verklaring van toepasselijkheid, met de overheidsmaatregelen erin en een bijlage met uitzonderingen.
5. Interne audits, managementbeoordelingen en actuele documentatie.
6. Verantwoording in het jaarverslag en inzicht aan ketenpartners via de verklaring van toepasselijkheid.
7. Vier rollen: bestuurder, lijnmanagement als eigenaar, CISO als coördinator en adviseur, interne toezichthouder.
8. Opzet, bestaan en werking van maatregelen aantonen.

De Cyberbeveiligingsregeling sector overheid maakt dat sinds 15 augustus 2026 wettelijk: artikel 3 schrijft
ISO 27001 voor, inclusief het vaststellen van het toepassingsgebied; artikel 5 schrijft de maatregelen van ISO
27002 en de overheidsmaatregelen van BIO 2.0 voor, en eist dat opzet, bestaan en werking aantoonbaar zijn.

## Het bezwaar en het antwoord

Het bezwaar dat je in elke organisatie hoort: security, privacy en continuïteit verschillen in scope en diepgang,
dus ze passen niet in één systeem. **Over de inhoud klopt dat.** Security gaat over alles, privacy over
verwerkingen, continuïteit over kritieke processen. De maatregelensets verschillen, het bewijs verschilt, de
toezichthouder verschilt.

Maar dat verschil zit in de maatregelen, en de BIO wil het juist zo. Paragraaf 5.2 van deel 1: de BIO sluit aan
op de Harmonized Structure voor managementsystemen, "waardoor de integratie van verschillende (ISO-)normen voor
managementsystemen wordt vereenvoudigd. Hierdoor wordt dubbel werk voorkomen." En hoofdstuk 11 en 18: ISO 22301
en NEN 7510 kunnen worden geïntegreerd in een managementsysteem op basis van ISO 27001; privacy en continuïteit
zijn aanpalend en worden daarom niet in de BIO uitgewerkt.

**Integreer de systemen, houd de maatregelensets apart.** Eén context, één governance, één risicoproces met één
schaal, één audit, één directiebeoordeling, één verbeterloop. Het alternatief is drie handboeken, drie
rapportages en drie directiebeoordelingen bij hetzelfde directieteam.

## Van vijftien producten naar negen artefacten

| Product uit een gangbaar plan van aanpak | Blijft een artefact? | Anders |
|---|---|---|
| 1 Toepassingsgebied | ja | |
| 2 Contextanalyse | ja | |
| 3 Belanghebbenden | nee | onderdeel van de contextanalyse |
| 4 Informatiebeveiligingsbeleid | ja | |
| 5 Risicomanagementbeleid | ja | |
| 6 Doelstellingen en KPI's | ja | |
| 7 Risicoanalyse | ja | |
| 8 Verklaring van toepasselijkheid | ja | |
| 9 Competentie- en opleidingseisen | nee | hoofdstuk van het handboek, uitgewerkt in het opleidingsplan |
| 10 Beheer van ISMS-documenten | nee | bijlage van het handboek |
| 11 Intern auditprogramma | ja | |
| 12 Auditrapportage | nee | uitkomst van het programma |
| 13 Directiebeoordeling | nee | het moment in de IMS-cyclus, met de halfjaarrapportage als input |
| 14 Registratie van afwijkingen | ja | |
| 15 Correctieve maatregelen | nee | zit in 14 |

Rekenen de producten mee in een capaciteitsvraag, reken die dan opnieuw: zes van de vijftien vallen samen of
vervallen, en een deel ligt vaak al als concept. (De bron sprak van acht artefacten; in de eigen tabel stonden er
negen.)

## De dekkingsmatrix

Het eerste wat een auditor pakt, is een tabel per eis: welk deel van het handboek dekt hem, welk artefact is het
bewijs, hoe staat het, wie is eigenaar. Houd hem bij als bijlage bij het handboek.

| Eis deel 1 | Handboek | Artefact | Stand (datum) | Eigenaar |
|---|---|---|---|---|
| Managementsysteem volgens ISO 27001 | hele handboek | handboek | | |
| Reikwijdte: minimaal kritieke processen en systemen | | toepassingsgebied, lijst kritieke processen | | |
| Context en belanghebbenden | | contextanalyse | | |
| Beleid | | strategisch informatiebeveiligingsbeleid | | |
| Methodiek: methode | | risicomanagementbeleid | | |
| Methodiek: quickscan en classificatie | | [classificatieschema](../../bcm/kritieke-processen-vaststellen/classificatieschema-biv.md) | | |
| Methodiek: register | | risicoregister | | |
| Methodiek: opvolgproces | | procedure afwijkingen | | |
| Risicoanalyse | | strategische analyse en [risicosessies](../../bcm/risicosessie-per-proces/) | | |
| Verklaring van toepasselijkheid met bijlage uitzonderingen | | VvT per gemeente | | |
| Interne audit | | auditprogramma en rapportage | | |
| Managementbeoordeling | | directiebeoordeling, met de [halfjaarrapportage](../ims-rapportage/) als input | | |
| Doelstellingen en meting | | KPI-set | | |
| Competenties | | opleidingseisen | | |
| Verantwoording jaarverslag en ketenpartners | | paragraaf jaarverslag, VvT delen | | |
| Vier rollen | | handboek, functieprofiel CISO | | |
| Leveranciers | | leveranciers- en ketenbeleid | | |
| Opzet, bestaan en werking aantonen | | controleraamwerk en bewijsdossier (deel 2) | | |

Wat de regio ermee zag: van negentien regels was er één vastgesteld, ontbraken er drie, en stond bij bijna de
helft "CISO, daarna open" als eigenaar. Eigenaarschap is de rode draad.

## De zeven beslispunten

Hak deze knopen door voordat je de producten gaat schrijven. Elk is in één sessie te doen.

1. **Toepassingsgebied.** Het systeem is organisatiebreed (handboek); de implementatie is gefaseerd en begint bij
   de kritieke processen (deel 1, 5.1). Beide in één scopedocument, vastgesteld door het directieteam. Bij een
   samenwerking: per gemeente een eigen verklaring van toepasselijkheid.
2. **Wie stelt wat vast.** Eén vaststellingsmatrix, die van het handboek. Beleid per gemeente door het college;
   strategische stukken (scope, risicobeleid, risicoanalyse, VvT, auditprogramma, directiebeoordeling) door het
   directieteam; tactische stukken (KPI's, afwijkingen) door het tactische IMS-overleg; operationele door de
   discipline-eigenaar. Leg niet de KPI's of de auditrapportage bij het college; daar hoort alleen beleid.
3. **Materiespecifiek beleid.** De lijneigenaar schrijft, het tactische overleg reviewt en stelt vast. Een aparte
   regiegroep voor beleid is een extra laag die niets toevoegt.
4. **Cadans.** Een BIO-project met een eigen kwartaalrapportage is tijdelijk. Benoem het overdrachtsmoment; daarna
   is de BIO-voortgang een vast blok in de halfjaarrapportage van het IMS.
5. **Directiebeoordeling.** Eén beoordeling voor de drie disciplines. Onderscheid twee dingen: de halfjaarrapportage
   is de input; de directiebeoordeling is het moment waarop het directieteam die input weegt volgens ISO 27001
   9.3 (status van eerdere besluiten, wijzigingen in context, auditresultaten, risicobeeld, verbeterkansen) en
   besluit over middelen en verbeteringen. Kies één cadans (minimaal jaarlijks), één datum, en leg vast wie de
   in-controlverklaring tekent.
6. **Ontbrekende artefacten in de documentatieboom.** De VvT, de lijst kritieke processen, het
   classificatieschema, de bewijslast, de KPI-set en het auditprogramma ontbreken vaak in het overzicht van
   documenten. Zet alle negen artefacten erin; het implementatieplan verwijst ernaar en voert geen eigen nummering.
7. **Eigenaarschap per onderdeel.** Eén naam per onderdeel: handboek, discipline-eigenaar informatiebeveiliging in
   het tactische overleg, implementatieplan deel 2 en VvT, risicoregister, consolidatie van de rapportage,
   ondertekening van de in-controlverklaring, en de artefacten van deel 1.

Over een GRC-applicatie: die verandert niets aan de vraag wie eigenaar is. Deel 1 zegt het zelf: een
managementsysteem is geen applicatie.

## Bewijs

- De **dekkingsmatrix** per eis van deel 1, met stand en eigenaar, als bijlage bij het handboek.
- De **negen artefacten**, elk met versie, opsteller, vaststeller en norm op de titelpagina, en het besluit van de
  vaststeller.
- Het **besluit over de zeven beslispunten**, vastgelegd in het besluitenlog van het IMS.
- De **directiebeoordeling** met de inputs en outputs van ISO 27001 9.3.

## BIO 2.0

| Maatregel of clausule | Wat deze aanpak daarvoor levert |
|---|---|
| ISO 27001, clausules 4 tot en met 10 (via deel 1 en artikel 3 van de regeling) | Het systeem en de artefacten per clausule |
| 5.1 Informatiebeveiligingsbeleid | Beleid in de vaststellingsmatrix |
| 5.2 Rollen en verantwoordelijkheden bij informatiebeveiliging | De vier rollen en het eigenaarschap per onderdeel |
| 5.4 Managementverantwoordelijkheden | De directiebeoordeling |
| 5.35 Onafhankelijke beoordeling van informatiebeveiliging | Het interne auditprogramma |
| 5.36 Naleving van beleid, regels en normen voor informatiebeveiliging | De procedure voor afwijkingen |

## Zo leg je het uit

**Aan de directie.** "De BIO vraagt een managementsysteem, en we hebben er al een. We bouwen er geen tweede naast.
Wat ontbreekt zijn negen documenten en een paar handtekeningen, en voor elk daarvan een naam."

**Aan de collega's van privacy en continuïteit.** "Jullie maatregelen blijven van jullie, met jullie eigen
normen. Wat we samen doen, is één risicoschaal, één audit en één beoordeling door de directie. Dat scheelt jullie
werk, het kost jullie geen diepgang."

**Aan de auditor.** "Hier is de dekkingsmatrix. Per eis ziet u welk deel van het handboek hem dekt, welk document
het bewijs is en wie de eigenaar is."
