---
titel: Een blue team opzetten
vakgebied: security
type: aanpak
normen: [BIO2]
versie: 2026-08
herkomst: ontstaan uit een echt tijdelijk interventieteam in een regionale samenwerking van gemeenten; voorbeelden en cijfers in de bijlagen zijn verzonnen
status: in gebruik
samenvatting: Handleiding in acht stappen voor de CISO of ISO die een tijdelijk, defensief interventieteam wil neerzetten naast de reguliere IV-lijn. Trigger en nulmeting, team op kunnen, mandaat op één A4, de organisatie meenemen, één dreiging van begin tot eind, ritme, opschalen en afbouwen. Met mandaatprotocol, memo's per gremium en een uitgewerkte voorbeeldcasus als bijlagen.
---

# Een blue team opzetten

Een blue team is hier een **tijdelijk interventieteam** dat in een afgebakend venster de meest urgente
gaten in je cyberweerbaarheid dicht, detectie inricht en de reactie oefent. Het staat náást je reguliere
IV-lijn, werkt in fix-modus en heeft een vooraf belegd mandaat om snel te handelen. Het is defensief:
eigen zwakke plekken zichtbaar maken en dichten. Geen red teaming, geen tegenaanvallen.

Deze handleiding is geschreven voor de CISO of ISO die het moet gaan doen. Acht stappen, in de volgorde
waarin je ze in de praktijk tegenkomt. De sjablonen en een uitgewerkt voorbeeld staan in de bijlagen:

| Bestand | Wat het is |
|---|---|
| [`mandaatprotocol-model.md`](mandaatprotocol-model.md) | Modelprotocol met voorbeeldclausules; door je eigen bestuur of CIO vast te stellen |
| [`memos-per-gremium.md`](memos-per-gremium.md) | Per gremium een voorbeeldmemo en een invulbaar sjabloon, voor gemeente en waterschap |
| [`voorbeeldcasus.md`](voorbeeldcasus.md) | Een verzonnen nulmeting en coverage-heatmap, om te zien hoe het eruitziet als je het invult |
| [`index.html`](index.html) | Deze handleiding als leesversie, plakbaar in Word |

## Wanneer wel, wanneer niet

Een blue team is geen nieuwe afdeling en geen vervanging van je IV-operatie of verbeterprogramma. Het is
wel:

- **tijdelijk**, met een einddatum en een evaluatiemoment;
- **aanvullend**: het leent mensen uit de lijn, de lijnverantwoordelijkheid blijft waar die is;
- **defensief**: eigen kwetsbaarheden vinden en dichten;
- **gericht op tempo en eigenaarschap** binnen het venster.

Het is niet: een audit, een compliance-exercitie, een beleidsherschrijving, of een permanente structuur.
Herken je jezelf in "we weten wat de gaten zijn, maar het komt er in de lijn niet van", dan is dit het
instrument. Is het probleem dat je de gaten niet kent, begin dan bij stap 1 en stop mogelijk daar: een
goede nulmeting kan al genoeg zijn om de lijn in beweging te krijgen.

## Stap 1. Een trigger en een eerlijke foto

Een interventieteam verdien je niet met "het zou kunnen". Je hebt twee dingen nodig: een aantoonbare
externe trigger en een nuchter beeld van je eigen stand.

**De trigger.** Een dreiging die groot genoeg is om buiten de gewone route te rechtvaardigen en concreet
genoeg om een venster aan te hangen. Denk aan een waarschuwing van het nationale CSIRT of je sector-CERT,
een bevestigde exploited-in-the-wild-melding op iets wat jij in huis hebt, of een verschuiving in het
dreigingslandschap die meerdere autoriteiten onafhankelijk benoemen. Leg de bron vast; je gaat hem in elke
memo citeren.

**De nulmeting.** Dit is "praten met je data": stel per bron een paar concrete vragen en schrijf de
antwoorden op.

| Bron | Vragen |
|---|---|
| Identiteit (AD, Entra) | Wie heeft admin, direct én via geneste groepen? Welke accounts hebben geen MFA? Welke accounts zijn stale (> 90 dagen geen login)? Welke service-accounts met hoge rechten is iedereen vergeten? |
| Netwerk (firewall, config) | Welke paden bestaan er écht? Is DNS-filtering actief? Zijn beheerpaden gescheiden van de werkplek? Staan er end-of-life-componenten in de keten? |
| Kwetsbaarheden (scanner, CMDB) | Hoeveel zijn direct exploiteerbaar en internet-facing? Hoeveel CRITICAL staan langer dan 60 dagen open? Welke systemen zijn end-of-life? |
| Back-up en continuïteit | Voldoe je aan 3-2-1-1-0? Is er immutable opslag? Wanneer is een restore voor het laatst écht getest? |
| Pentest | Wat was de laatste uitkomst? Hoe snel was Domain Admin bereikt, hoeveel hashes gekraakt? |

De categorieën zijn generiek, de waarden blijven intern. Een ingevuld voorbeeld met verzonnen cijfers staat
in [`voorbeeldcasus.md`](voorbeeldcasus.md); daar zie je ook hoe hard zo'n foto binnenkomt bij een
directie.

## Stap 2. Eén opdracht en een einddatum

Formuleer de opdracht in één zin: *de meest urgente gaten dicht, detectie ingericht en reactie geoefend
vóór het venster sluit.* Meer hoeft niet. Alles wat je erbij zet, wordt een reden om het niet te doen.

Maak de tijdelijkheid expliciet: een einddatum, en een verlengings-, afbouw- of overgangsbesluit dat ruim
vóór die datum op de agenda staat. Zonder einddatum wordt het een afdeling; zonder gepland besluit wordt
het een stille dood.

Drie dingen die het team doet, en niets anders:

1. **Gaten dichten.** Bekende, aantoonbare gaten: MFA, patching, segmentatie van beheerpaden, DNS- en
   webfiltering, back-uphygiëne.
2. **Detectie inrichten.** Zichtbaar maken wat nu niet gezien wordt (netwerkflows, egress, detectieregels)
   en dat netjes overdragen aan de SOC- of MDR-partner.
3. **Reactie oefenen.** Reactieroutes activeren en beproeven, zodat "kunnen ingrijpen" geen papier is.

## Stap 3. Een team op kunnen, niet op positie

Selecteer op kennis, lef en netwerk, niet op functieprofiel. Een klein team dat mag, doet meer dan een
groot team dat moet afstemmen.

| Laag | Omvang | Wie |
|---|---|---|
| Kern | ongeveer 6 | Multidisciplinair, in fix-modus: overzicht en techniek, incidentervaring, operationele security, crisis en continuïteit, omgevingskennis, en iemand die de brug slaat tussen risico en uitvoering |
| Schil | ongeveer 4 | Service manager (spil naar leveranciers en SOC), manager IV-operatie, hoofd IV-projecten (voor de latente bevindingen), bedrijfsvoering (voor de impactweging) |
| Governance | 5 rollen | Opdrachtgever · beslisser en budgethouder · facilitator · tweede lijn (risico-advies, geen veto) · derde lijn (onafhankelijke toets) |

Het team leent mensen. Spreek per persoon af hoeveel tijd, voor hoe lang, en wie in de lijn dat weet.
Dedicated capaciteit plus een WIP-limiet is wat het team beschermt tegen "kun je dit er even bij doen".

## Stap 4. Het mandaat op één A4

Dit is de stap die het verschil maakt tussen een werkgroep en een interventieteam. Het mandaat regelt
vooraf wat het team mag zonder akkoord per geval. Drie handelingen:

1. kritieke patches uitrollen buiten de change-vensters, ook bij tijdelijke dienstimpact;
2. een dienst of systeem tijdelijk afschakelen bij een actieve dreiging (bij OT: altijd met de
   proceseigenaar en een veilige terugval);
3. externe partijen raadplegen zonder aparte opdracht.

Met vier voorwaarden die altijd gelden:

- **Trigger:** alleen bij een Rood-score (zie stap 6), dus relevant, direct bereikbaar en zonder dekking.
- **Vier ogen:** minstens twee kernteamleden zijn het eens dat het Rood is.
- **Melding:** de beslisser hoort het zo snel mogelijk, niet achteraf.
- **Register:** binnen 24 uur in het besluitenregister: datum, besluit, onderbouwing, hersteltijd,
  betrokkenen, bewijslink. Ook de mandaat-bypass gaat gewoon door de reguliere change- of
  incidentregistratie.

Voeg een financieel mandaat toe met drie drempels (team beslist · beslisser vooraf akkoord · formeel
akkoord), en drie escalatieniveaus (kernteam · beslisser/CIO · calamiteitenteam). De uitwerking met
voorbeeldclausules staat in [`mandaatprotocol-model.md`](mandaatprotocol-model.md). Laat het vaststellen
door je bestuur of CIO vóór de eerste ingreep; een mandaat dat achteraf wordt betwist, is geen mandaat.

Geen register is hetzelfde gat als bij elk incident dat "geen eenduidige oorzaak" had. Het hoeft geen
systeem te zijn; een lijst die iedereen kan vinden, volstaat.

## Stap 5. De organisatie meenemen

Een team met mandaat schrikt mensen af als ze het niet zien aankomen. Informeer daarom vooraf, per gremium,
met dezelfde kern en een eigen invalshoek. De volgorde is niet toevallig: eerst wie het groen licht geeft,
dan wie het gaat merken.

| Gremium | Wat ze moeten weten |
|---|---|
| Gemeentesecretaris of secretaris-directeur | Scharnier naar het bestuur; hoort het vooraf en wijst één vast aanspreekpunt aan |
| College en burgemeester, of dagelijks bestuur en dijkgraaf | Er handelt tijdelijk een team buiten de reguliere route; het bestuur kent het risico, de openbare-orde-lijn is aangesloten, woordvoering is vooraf afgesproken |
| Directieteam of MT | Wie de mensen uitleent, wat de WIP-limiet is, wat er na het venster gebeurt |
| IB&P | Op onderwerp overlap, op rol niet: IB&P zet het kader, het team dicht acuut en draagt structurele bevindingen over |
| Bedrijfsvoering | Impactweging bij ingrepen, terugvalroutes (balie, telefoon) |
| Privacy en FG | Geen gedragsmonitoring, read-only en geaggregeerd waar het kan, geen inhoud van mailboxen; alles via de FG en het register |
| Leveranciers en infrastructuurpartners | Wat het mandaat voor hen betekent, wie ze bellen, wat ze mogen verwachten bij een afschakeling |
| OT en procesautomatisering (waterschap) | Veiligheid vóór snelheid; alleen handelen met de proceseigenaar |

Per gremium staat in [`memos-per-gremium.md`](memos-per-gremium.md) een voorbeeldmemo en een sjabloon,
voor gemeente en waterschap. Elke memo heeft dezelfde bouw: aanleiding, wat we doen, waarom het u raakt, wat
dit concreet kan betekenen (drie scenario's), waarborgen, wat wij u vragen, wat u van ons krijgt. Vul de
scenario's in met jouw diensten; abstracte memo's overtuigen niemand.

## Stap 6. Eén dreiging van begin tot eind

De werkwijze is een herhaalbaar recept: één concrete dreiging als drager, langs zeven stappen. Draai hem de
eerste keer helemaal uit voordat je opschaalt; daar leer je het meest van.

1. **Scenario kiezen.** Neem één concreet dreigingsrapport (nationaal CSIRT, MDR-partner, publieke threat
   intelligence) mét TTP's en indicatoren. Leg rapport en bron vast.
2. **TTP's op de kill chain mappen.** Vertaal naar aanvalstechnieken (MITRE ATT&CK) en bepaal welke
   chokepoints in welke zones geraakt worden. Filter op je kroonjuwelen.
3. **D/R/P beoordelen.** Per geraakte cel: kunnen we het **D**etecteren, weten we hoe te **R**eageren,
   houden we het **P**reventief tegen? Volgorde D > R > P: eerst zien, dan handelen, dan voorkomen.
4. **R/E/C scoren, bewijs, opdrachten.** Scoor elk gat op urgentie, leg bewijs vast bij wat groen heet,
   maak per gat een kaart met de kleur als prioriteit. Rood vereist vier ogen.
5. **"Set en forget" voorkomen.** Laat groen automatisch degraderen als het bewijs te oud is; detecteer
   drift. Een status "actief" zonder bewijs is een leugen op je dashboard.
6. **Variant-run.** Dezelfde techniek, andere ingang of zone. Zo test je de robuustheid.
7. **Herhalen.** Geen project met einddatum maar een ritme: een lopende reeks runs, gekoppeld aan de
   sprintcyclus.

**R/E/C** is de urgentiescore per bevinding:

- **R**elevance: maakt deze zwakte minstens één kill-chain-stap aantoonbaar makkelijker? (ja / deels / nee)
- **E**xposure: bereikbaar vanaf een plausibel startpunt? (direct / indirect / niet)
- **C**ontrol gap: wat blijft over als je maatregelen hun werk doen? (niets / deels / stopt)

R is de poort: geen relevance, dan niet urgent.

| Uitslag | Betekenis | Actie |
|---|---|---|
| Rood | relevant, direct, geen dekking | mandaat-actie; vier ogen; binnen 24 uur in het register; beslisser binnen een uur gemeld |
| Oranje | serieus risico op minstens één as | deze of eerstvolgende sprint, normale change-procedure |
| Geel | latent of structureel | naar de lijn of projecten, of parkeren |
| Groen | laag risico | loggen en sluiten |

De uitkomst van stap 3 zet je in een **coverage-heatmap**: zones (werkplek, identiteit, datacenter, cloud,
OT, keten) tegen D/R/P, met een percentage per cel. Eén oogopslag laat zien waar de aandacht heen moet, en
dat is de zwakste cel, niet de sterkste. Een verzonnen voorbeeld staat in
[`voorbeeldcasus.md`](voorbeeldcasus.md).

**De gouden regel: bewijs stuurt status.** Een groen vinkje is een gekoppelde, actieve detectieregel én een
beproevingsverslag. Twee vormen van bewijs: bestaan (export, contract, playbook) én beproeving (oefenverslag,
test). Geen bewijs, dan geen groen.

## Stap 7. Ritme en bord

Kies een werkvorm die je al kent. Een eenvoudig bord en een vast ritme zijn genoeg; gebruik wat er al is.

| Stapel | Bedoeling |
|---|---|
| Nieuw | nog te bekijken |
| Nu mee bezig | het urgente werk van deze week, met WIP-limiet |
| Wacht of later | wacht op iets, of gaat naar de lijn of projecten |
| Controle | hertest of verificatie loopt |

Eén tip die zich terugbetaalt: leg besluiten en bewijs vast op de kaart zelf, niet in een chatkanaal.

Vóór je een kaart "klaar" noemt, loop je vier vragen langs: is de actie echt gedaan en heb ik er bewijs
van? Heeft een tweede persoon meegekeken? Weet ik hoe ik het terugdraai? Wie moest het weten, en is die
ingelicht? Geen verplichte afvinklijst, wel de vragen die voorkomen dat "klaar" niet echt klaar is.

Voor een ingreep buiten de normale route helpt een geheugensteun van zes regels: wat is er aan de hand en
waar weet je dat vandaan · wat raakt het (systemen, processen, mensen) · hoe urgent is het echt (laag,
serieus, acuut) · wie beslist mee · hoe draai je het terug · wie moet het weten en wie schrijft het op.

## Stap 8. Opschalen en afbouwen

Hoe groter de impact, hoe hoger je het optilt. Koppel de drie niveaus aan wat je al hebt; niet elke
organisatie heeft een apart digitaal calamiteitenteam, en dat hoeft ook niet.

| Zwaarte | Ongeveer wanneer | Waar leg je het neer |
|---|---|---|
| Licht | bekend probleem, beperkte impact, binnen je mandaat | het team beslist zelf (met een tweede paar ogen) en legt het vast |
| Zwaarder | langere of bredere impact, ketenpartner merkbaar geraakt, of buiten het mandaat | naar je leidinggevende of CIO; opdrachtgever op de hoogte |
| Zwaar | bevestigde aanval, datalek met meldplicht, onduidelijke scope | naar je bestaande crisis- of calamiteitenroute, plus toezichthouder of CSIRT waar verplicht |

Heb je geen formele crisisstructuur? Spreek dan vooraf één ding af: wie je belt als het echt groot is, en
wie dan de leiding neemt. Dat is het minimum.

**Afbouwen** is een besluit, geen gebeurtenis. Ruim vóór de einddatum kies je: afbouwen, overdragen aan de
lijn, of verlengen als de context erom vraagt. Wat je overdraagt: het register, de openstaande gele
kaarten met eigenaar, de detectieregels bij de SOC-partner, en een eindbeeld van de heatmap naast de
nulmeting. Dat laatste is je verantwoording naar het bestuur.

## De weerstand die je krijgt, en je antwoord

| Bezwaar | Antwoord |
|---|---|
| Waarom een nieuw team? We hebben de lijn toch al? | Het vervangt niets en is tijdelijk. De lijn en het verbeterprogramma lopen door; het team leent mensen en voegt tempo en eigenaarschap toe. |
| Overlapt dit niet met IB&P, de IV-operatie, het programma? | Op onderwerp wel, op rol niet. IB&P zet het kader, de operatie beheert, het programma verbetert structureel. Het team dicht acuut en draagt structurele bevindingen over. |
| Is dit red teaming? | Nee. Defensief: eigen zwakke plekken zichtbaar maken en dichten. Pentesten blijven bij externe partijen. |
| Mogen jullie echt buiten de change-vensters patchen? | Ja, alleen bij Rood, met vier ogen, met melding aan de beslisser en binnen 24 uur in het register. Het mandaat is vooraf belegd, niet per geval. |
| En als een afschakeling schade doet? | Vóór elke ingreep een rollback-pad, een impactafweging en het juiste beslisniveau. Bij OT gaat veiligheid vóór snelheid. Bij twijfel niet doen, eerst opschalen. |
| Wie houdt toezicht? | Opdrachtgever (periodiek), tweede lijn (risico-advies), onafhankelijke derde lijn (steekproef). Plus het register: elke mandaat-inzet is achteraf navolgbaar. |
| Gaat dit niet ten koste van het reguliere werk? | Dedicated capaciteit en een WIP-limiet. Latente bevindingen gaan naar de lijn of projecten, niet op het bord van het team. |
| Wat gebeurt er na het venster? | Ruim vóór de einddatum een besluit: afbouwen, overdragen of verlengen. Geen open einde. |
| Wat betekent dit voor privacy? | Geen gedragsmonitoring, read-only en geaggregeerd waar het kan, geen inhoud van mailboxen of bestanden. Alles via de FG en het register. |

## Uit de praktijk

**Het mandaat was de helft van het werk.** De technische gaten waren in een week bekend; het duurde
langer om vast te leggen wie mocht besluiten om buiten het change-venster te patchen. Begin met stap 4
zodra de trigger er is, niet pas als de eerste Rood-kaart op het bord staat.

**De keten was de zwakste cel, en de minst zichtbare.** In de coverage-heatmap scoorde de zone
leveranciers en keten op alle drie de assen het laagst. Dat verraste niemand in het team en iedereen
daarbuiten. Zet die zone bewust in de eerste run.

**Groen zonder bewijs kwam meer voor dan rood.** Bij de eerste run bleek een deel van wat "actief" heette
niet beproefd. De regel "bewijs stuurt status" is geen formaliteit; hij haalt de vinkjes van het dashboard
die je een vals gevoel van veiligheid gaven.

**De memo aan het bestuur ging niet over techniek.** Wat het college wilde weten: wie beslist, wat merken
inwoners, wie doet woordvoering. De drie scenario's (spoedpatch 's avonds, een dienst een dag stil, een
externe partij op locatie) deden meer dan elke tabel.

## Begrippen

| Term | Uitleg |
|---|---|
| Kill chain | De stappen die een aanvaller doorloopt; nuttig om te zien waar je hem kunt stoppen |
| Chokepoint | Een plek in je omgeving waar je een aanvalsstap kunt zien of tegenhouden |
| TTP | Tactics, Techniques and Procedures: hoe een aanvaller te werk gaat (MITRE ATT&CK) |
| D/R/P | Detect, Respond, Prevent: kunnen we het zien, weten we wat te doen, houden we het tegen |
| R/E/C | Relevance, Exposure, Control gap: de urgentiescore per bevinding |
| Vier ogen | Een besluit dat minstens twee mensen samen nemen |
| SOC, MDR | (Externe) bewaking van je systemen die op signalen reageert |
| OT, SCADA | Operationele techniek: de systemen die fysieke processen aansturen (gemalen, sluizen, zuivering) |
| WIP-limiet | Maximum aantal kaarten dat tegelijk "in bewerking" mag zijn |

## Bronnen en tooling

- **MITRE ATT&CK** (attack.mitre.org): het referentiekader voor TTP's in stap 6.
- **Atomic Red Team** (github.com/redcanaryco/atomic-red-team): open-source aanvalstests gekoppeld aan
  ATT&CK, om je eigen detectie te beproeven. Van dezelfde MDR-leverancier komt een jaarlijks Threat
  Detection Report dat als scenario-bron kan dienen.
- **security-commons-nl** (github.com/security-commons-nl): de tooling rond "praten met je data" die
  bij deze aanpak hoort, waaronder `kill-chain-analysis` (stap 2 en 3), `security-posture-tool` (de
  heatmap) en `dreigingsanalyse` (scenario's). In ontwikkeling; richting en voorbeeld, nog geen afgeronde
  producten.

## Licentie

[EUPL-1.2](../../LICENSE), vrij te hergebruiken en aan te passen. Feedback en verbeteringen welkom via een
[issue](https://github.com/security-commons-nl/kennisbank/issues/new/choose).
