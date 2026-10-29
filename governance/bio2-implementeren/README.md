---
titel: BIO 2.0 invoeren, een plan van aanpak met urenraming
vakgebied: governance
type: aanpak
normen: [BIO2, ISO 27001, Cbw]
peildatum: 2026-10-14
herkomst: plan van aanpak voor de invoering van BIO 2.0, deel 1 en deel 2 (2026), van het team informatiebeveiliging en privacy van een regionale samenwerking van gemeenten; nog niet vastgesteld
status: concept
route: [eerste-honderd-dagen]
samenvatting: Hoe een samenwerking van gemeenten de invoering van BIO 2.0 aanpakt, met de cijfers die in handreikingen ontbreken. Deel 1 (het managementsysteem) in zeven onderdelen met producten, eigenaar en uren per rol, samen 768 uur. Deel 2 (de maatregelen) via beleid per thema, maatregelen in de bestaande beheerprocessen met het bewijs in het ticket, een vaststellingsroute en een volgorde van 21 thema's met de afdeling die eigenaar is. Met de randvoorwaarden en de zes projectrisico's die het plan zelf noemt, en een sjabloon om je eigen plan in te vullen.
bronnen: [ibd-bio2-handreiking-realistische-implementatie-aanpak-bria, ibd-bio2-handreiking-isms-proces-implementatie, ibd-bio2-handreiking-isms, ibd-bio2-beschrijving-isms-verantwoordelijkheden-binnen-de-gemeente, ibd-bio2-rasci-tabel-controls-informatieveiligheid-en-privacy, ibd-handreiking-bio-voor-kleine-gemeenten, cip-bio-tekst]
---

# BIO 2.0 invoeren, een plan van aanpak met urenraming

> **Lees het online:** [security-commons-nl.github.io/kennisbank/governance/bio2-implementeren](https://security-commons-nl.github.io/kennisbank/governance/bio2-implementeren/)

De vraag die elke CISO krijgt zodra de Cyberbeveiligingswet geldt: wat moeten we doen, in welke volgorde,
en wat kost het aan mensen? De handreikingen van de IBD beschrijven het managementsysteem en de maatregelen
goed. Wat ze niet geven, is een raming in uren en een volgorde die je aan een directie kunt voorleggen.

Dit is het plan van aanpak van een samenwerking van vier gemeenten met één gezamenlijke bedrijfsvoering. Het
splitst de invoering in de twee delen van BIO 2.0 en zet bij elk onderdeel wie het doet en hoeveel tijd het
kost. Het is een concept: de directie had het op de peildatum nog niet vastgesteld, en de uren zijn een
raming, geen nacalculatie.

**Het sjabloon:** [plan-van-aanpak-sjabloon.md](plan-van-aanpak-sjabloon.md), met de structuur van dit plan
en blokhaken waar jouw gegevens komen.

## Twee delen, twee soorten werk

BIO 2.0 vraagt drie dingen: een managementsysteem voor informatiebeveiliging (ISMS) met een vastgestelde
scope, de verplichte maatregelen voor wat binnen die scope valt, en kunnen aantonen dat die maatregelen
bestaan en werken. Het plan maakt daar twee trajecten van:

- **Deel 1, het managementsysteem.** Vooral werk van de CISO, met de ISO voor de risicoanalyse en een
  IT-auditor voor de evaluatie. Klein in uren, groot in besluiten.
- **Deel 2, de maatregelen.** Werk van de lijn: HR, facilitair, inkoop, IV-ontwikkeling en IV-beheer. De
  CISO en de ISO regisseren; de afdelingen voeren uit.

Wie dat onderscheid niet maakt, legt deel 2 bij het team informatiebeveiliging neer, en daar past het niet.

## Deel 1: het managementsysteem in zeven onderdelen

Het plan volgt de hoofdstukken van ISO 27001, waar deel 1 van BIO 2.0 op gebaseerd is. Per onderdeel de
producten, wie eigenaar is en de geraamde uren.

| Onderdeel | Producten | Eigenaar | CISO | ISO | IT-auditor |
|---|---|---|---|---|---|
| Context en scope | scope en reikwijdte van het ISMS, contextanalyse, overzicht van belanghebbenden | concerncontrol | 40 | 8 | |
| Leiderschap | informatiebeveiligingsbeleid | concerncontrol | 120 | 8 | |
| Planning | risicomanagementbeleid, kritische prestatie-indicatoren | concerncontrol | 40 | 8 | |
| Risicoanalyse | risicoanalyse, verklaring van toepasselijkheid | team informatiebeveiliging | 24 | 200 | |
| Ondersteuning | competentie- en opleidingseisen, beheer van ISMS-documenten | team informatiebeveiliging | 40 | 16 | |
| Evaluatie | intern auditprogramma, auditrapportage, directiebeoordeling | concerncontrol | 40 | | 160 |
| Verbetering | registratie van afwijkingen, correctieve maatregelen en opvolging | concerncontrol | 40 | 24 | |
| **Totaal** | | | **344** | **264** | **160** |

Drie dingen vallen op:

- **De CISO zit bij concerncontrol, niet in IV.** Daarom is concerncontrol eigenaar van vijf van de zeven
  onderdelen. Zit jouw CISO in de IV-organisatie, dan verschuift het eigenaarschap, niet het werk.
- **Het beleid kost de meeste CISO-uren.** 120 van de 344, omdat het strategisch beleid de rollen, de
  scope en de verantwoordelijkheid van het bestuur vastlegt. De rest volgt daaruit.
- **De risicoanalyse is ISO-werk, en veel.** 200 uur, omdat de verklaring van toepasselijkheid per
  maatregel een onderbouwing vraagt. De auditscope van de IT-auditor is beperkt tot het ISMS; de werking
  van de maatregelen zelf valt erbuiten.

Bij een volle werkweek van 36 uur is dat ruim negen weken CISO, ruim zeven weken ISO en ruim vier weken
IT-audit, verspreid over een jaar. Voor een samenwerking van vier gemeenten. Een enkele gemeente heeft
minder afstemming, maar niet minder producten.

**Eerst de kritieke processen.** Het plan zet niet alle onderdelen in het eerste jaar. Het eerste jaar
staat in het teken van de kritieke processen, de kritieke IT-middelen en de eisen die daaruit volgen,
omdat deel 2 daarop leunt: zonder die lijst weet je niet op welke systemen de maatregelen moeten. De
volledige cyclus van plan, uitvoering, controle en verbetering draait pas het jaar daarna, met in het
eerste kwartaal de contextanalyse, de risicoanalyse, de verklaring van toepasselijkheid en een
verbeterkalender, in het derde kwartaal de audit en in het vierde de directiebeoordeling.

## Deel 2: de maatregelen

BIO 2.0 versie 1.3 heeft 117 overheidsmaatregelen, en 40 ISO-beheersmaatregelen zonder eigen
overheidsmaatregel ([nummers en titels in de normwijzer](https://security-commons-nl.github.io/normen/normwijzer.html)). Het
plan pakt ze niet maatregel voor maatregel aan, maar per thema.

### Per thema: beleid, ontwerp, inrichting, bewaking

Elk thema krijgt een eigen beleidsstuk; het plan rekent op ongeveer twintig, naast het strategisch beleid.
De stukken volgen de domeinindeling van het BIO 2.0-controleraamwerk; een set om mee te beginnen is de
[beleidsset informatiebeveiliging](../beleidsset-informatiebeveiliging/). Per thema doorloopt het plan drie
stappen:

1. **Richten.** Het beleid schrijven, samen met de afdeling die het moet uitvoeren. Het huidige proces
   langs de risico's leggen. De maatregelen ontwerpen die er nog bij moeten.
2. **Inrichten.** De maatregelen in het ITSM-systeem zetten, als stap in een bestaand proces of als
   terugkerende taak. Werkinstructies schrijven (checklists, systeemrapportages, formulieren). Een workshop
   met de uitvoerders voor acceptatie en uitleg.
3. **Verrichten.** De uitvoerders begeleiden, knelpunten oplossen en de bewaking door de tweede lijn
   inrichten. Het projectteam volgt elk thema de eerste zes maanden na de invoering en rapporteert per
   kwartaal aan de stuurgroep.

**Het bewijs zit in het ticket.** De kern van de aanpak: een maatregel wordt waar het kan een taak in een
proces dat al bestaat. Een rechtenaanvraag, een wijzigingsverzoek of een kalendertaak start hem, en de
uitvoering wordt vastgelegd in het ticket. Dan heb je het bewijs voor de audit zonder apart
compliancesysteem, en wordt de maatregel uitgevoerd door wie het proces al draait.

Per thema gaan drie documenten ter goedkeuring naar de regiegroep: een risicoanalyse bij de maatregelen,
het beleid en een risico- en controlematrix met de maatregelen uit BIO 2.0.

### Zet het naast wat al loopt

In het voorbeeld liep al een verbeterprogramma voor de IV-operatie, met een eigen set maatregelen voor de
korte termijn. Ongeveer een kwart van de maatregelen viel daaronder. Het plan neemt die niet opnieuw op,
maar regisseert ze: het programma voert uit, het plan bewaakt dat het resultaat aan BIO 2.0 voldoet. Kijk
voordat je begint welke maatregelen al ergens belegd zijn. Dat scheelt dubbel werk en ruzie over
eigenaarschap.

### De vaststellingsroute voor beleid

| Stap | Wie | Wat |
|---|---|---|
| 1 | team informatiebeveiliging | stelt het beleid op, samen met de afdeling die het uitvoert |
| 2 | teammanager | review |
| 3 | afdelingsmanager | review |
| 4 | MT van de directie | review |
| 5 | CIO | biedt het beleid ter goedkeuring aan |
| 6 | directeur | stelt het beleid vast |

Zes stappen per stuk, twintig stukken: reken op doorlooptijd. Het plan vangt dat op door eerst het beleid
van een thema vast te stellen en dan pas de maatregelen in te richten.

### Volgorde en eigenaar per thema

Het plan zet de thema's in deze volgorde, verspreid over ruim drie jaar. Per thema wordt eerst het beleid
vastgesteld; de invoering van de maatregelen duurt daarna ongeveer twee keer zo lang.

| # | Thema | Eigenaar (afdeling) |
|---|---|---|
| 1 | Fysieke toegang en beveiliging | facilitaire zaken |
| 2 | Bedrijfsmiddelenbeheer | IV-beheer |
| 3 | Logische toegangsbeveiliging | IV-beheer |
| 4 | Mobile device management en mobile application management | IV-beheer |
| 5 | Inkoop en aanbesteding | inkoop en financiën |
| 6 | Contractbeheer | IV-beheer |
| 7 | Screening, bewustzijn en opleiding | HR |
| 8 | Security incident management | IV-beheer |
| 9 | Wijzigingsbeheer | IV-beheer |
| 10 | Kwetsbaarheden en patchmanagement | IV-beheer |
| 11 | Informatieclassificatie | IV-beheer |
| 12 | Gebruik van cloudtechnologie | IV-ontwikkeling |
| 13 | Netwerkbeveiliging | IV-beheer |
| 14 | Informatiebeveiliging binnen projecten | IV-ontwikkeling |
| 15 | Logging en monitoring | IV-beheer |
| 16 | Back-up en recovery | IV-beheer |
| 17 | Cryptografie | IV-beheer |
| 18 | Business continuity en disaster recovery | IV-beheer |
| 19 | Secure software development | IV-beheer |
| 20 | Afvoer en hergebruik van gegevensdragers | IV-beheer |
| 21 | IT-compliance | IV-ontwikkeling |

Fysieke toegang staat vooraan omdat het buiten IV ligt en snel resultaat geeft. Vijftien van de 21 thema's
liggen bij IV-beheer. Daar zit de capaciteit die de invoering bepaalt, en daar hoort de volgorde besproken
te worden.

### Randvoorwaarden

Deel 2 leunt op wat er in de beheerorganisatie al is. Ontbreekt het, dan wordt het onderdeel van de
invoering en schuift de planning. Het plan noemt:

- **Een juiste en volledige CMDB.** Een harde randvoorwaarde: zonder registratie van de IT-middelen maken
  de workflows geen onderscheid tussen kritieke en niet-kritieke systemen.
- Een IT-governancedocument met taken, rollen en verantwoordelijkheden.
- Een screeningsproces.
- Dataclassificatie.
- Een incidentbeheerproces en een wijzigingsproces.
- Autorisatiebeheer, bij voorkeur op basis van rollen (RBAC).
- Netwerksegmentatie.

## De projectrisico's die het plan zelf noemt

| Risico | Maatregel |
|---|---|
| Te weinig prioriteit, waardoor managers en specialisten buiten het kernteam geen tijd hebben | het belang en de aanpak bij de start in een workshop toelichten; contactmomenten tijdig plannen; tijdig escaleren naar de stuurgroep |
| Te weinig capaciteit om de processen in het ITSM-systeem in te richten | de planning afstemmen met de beheerder van het ITSM-systeem; vroeg escaleren voor extra capaciteit |
| Weerstand tegen de timing en de omvang van de capaciteitsvraag | gefaseerd invoeren, de volgorde in overleg met het MT |
| Weerstand in de beheerorganisatie tegen meer vastleggen | de organisatie regelmatig vertellen wat er verandert; de last spreiden in de planning |
| Weerstand van systeem- en functioneel beheerders tegen minder verhoogde rechten | de beperking onderbouwen met het beleid en de risico's; nieuwe eisen tijdig en persoonlijk uitleggen |
| Te weinig bewustzijn bij de betrokken medewerkers | periodiek aandacht voor informatieveiligheid tijdens het project; onderscheid maken tussen gewone gebruikers, systeemeigenaren en kritieke functies in de beheerorganisatie |

## Hoe je het gebruikt

- **Voor de directie.** Neem de tabel van deel 1 over en pas de uren aan op je eigen omvang. De vraag "wat
  kost dit" heeft dan een antwoord met een onderbouwing.
- **Voor de planning van deel 2.** Begin met de lijst van thema's en eigenaren. Zet er de maatregelen naast
  die al belegd zijn, en vraag per afdeling wat er past.
- **Voor het eerste thema.** Kies een thema buiten IV, zoals fysieke toegang, en loop richten, inrichten
  en verrichten één keer helemaal door. Dan weet je wat een thema werkelijk kost voordat je er twintig
  plant.
- **Het sjabloon:** [plan-van-aanpak-sjabloon.md](plan-van-aanpak-sjabloon.md).

## Wat dit niet is

Geen vastgesteld plan en geen nacalculatie: de uren zijn een raming vooraf. De planning per kwartaal uit het
origineel staat er niet in, alleen de volgorde, omdat de jaartallen bij één organisatie horen. De
beschrijving van deel 1 en deel 2 van BIO 2.0 is een samenvatting; de norm zelf staat bij het CIP.

## Licentie

EUPL-1.2.
