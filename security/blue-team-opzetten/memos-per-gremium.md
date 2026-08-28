---
titel: Memo's per gremium bij een blue team
vakgebied: security
type: sjabloon
normen: []
versie: 2026-08
herkomst: bijlage bij "Een blue team opzetten"; namen, regio en cijfers verzonnen
status: sjabloon
samenvatting: Per gremium een voorbeeldmemo en een invulbaar sjabloon om de organisatie vooraf mee te nemen bij een tijdelijk interventieteam. Twee sets, voor gemeente en waterschap.
---

# Memo's per gremium

Bijlage bij [Een blue team opzetten](README.md), stap 5. Per gremium een **voorbeeldmemo** (verzonnen
organisatie, verzonnen cijfers) en een **sjabloon** om in te vullen. Elke memo heeft dezelfde bouw:
aanleiding, wat we doen, waarom het u raakt, wat dit concreet kan betekenen, waarborgen, wat wij u vragen,
wat u van ons krijgt. Vul de scenario's met je eigen diensten.

Placeholders staan tussen `[ ]`. `[einddatum venster]` is de datum waarop het mandaat afloopt.

## Gemeente

### College & burgemeester

**Kernboodschap.** Er werkt tijdelijk een team met mandaat om buiten de reguliere route te handelen; het college kent het risico, de burgemeester (openbare orde/veiligheid) is aangesloten, en er is één vast aanspreekpunt.

#### Voorbeeldmemo (verzonnen)

> *Aan: college van B&W, t.a.v. burgemeester · Van: CISO [regio] · Betreft: tijdelijk interventieteam, ter informering · Classificatie: intern*

> **Aanleiding.** Drie partijen waarschuwden recent onafhankelijk voor hetzelfde: AI-gedreven aanvalscapaciteit maakt het vinden én misbruiken van kwetsbaarheden sneller en goedkoper, de tijd tussen "kwetsbaarheid bekend" en "actief misbruikt" krimpt van dagen naar uren. We hebben een handelingsvenster tot [einddatum venster] om onze meest urgente gaten te dichten; daarna moeten we ervan uitgaan dat zulke capaciteit breed beschikbaar is.

> **Wat we doen.** We richten tijdelijk een klein interventieteam in dat náást de reguliere IT-lijn de grootste gaten dicht, detectie inricht en onze reactie oefent. Het team is uitdrukkelijk tijdelijk en heeft een vooraf belegd mandaat; het vervangt niets en herschrijft geen beleid.

> **Waarom dit het college raakt.** Om in dat tempo te handelen mag het team, onder voorwaarden, buiten de reguliere change-procedure ingrijpen: een kritieke update uitrollen, een dienst tijdelijk afschakelen, of een externe partij inschakelen. Dat kan de dienstverlening kortstondig raken en, bij een incident, doorwerken in de openbare orde en de communicatie naar inwoners. Het gezag van de burgemeester en uw bestuurlijk eigenaarschap blijven volledig bij u; het team handelt binnen een mandaat dat u kent en hebt goedgekeurd.

> **Wat dit concreet kan betekenen.** (A) we rollen 's avonds een spoedpatch uit op een internet-gerichte dienst, burgers merken hooguit een onderbreking van enkele minuten; (B) we vermoeden misbruik van een account en zetten een dienst een dag stil voor onderzoek, met balie en telefoon als terugval; (C) bij een bevestigd incident schakelen we een gespecialiseerde partij in, die mogelijk fysiek op locatie meewerkt. In alle gevallen hoort u het op het moment zelf, niet achteraf.

> **Waarborgen.** Elke ingreep met merkbare impact is een besluit van minstens twee teamleden (vier-ogen), wordt binnen 24 uur vastgelegd in een besluitenregister, en valt onder onafhankelijk toezicht. Zo blijft achteraf navolgbaar wát is gebeurd en waaróm.

> **Wat wij u vragen.** (1) Neem kennis van het mandaat en de drie situaties hierboven; (2) bevestig de lijn naar de burgemeester voor de openbare-orde- en gezagsaspecten; (3) laten we vooraf afspreken wie woordvoering doet als een ingreep zichtbaar wordt.

> **Wat u van ons krijgt.** Een melding bij elke ingreep met bestuurlijke lading (niet achteraf), een korte periodieke voortgangsrapportage, en kant-en-klare feitelijke bouwstenen voor uw woordvoering of een raadsbriefing, inclusief een eindbeeld vóór het venster sluit.

#### Sjabloon

```
Memo college & burgemeester, ter informering
Aanleiding. [trigger + venster-datum]
Waarom het college dit moet weten. [mandaat + bestuurlijke/OOV-lading]
Wat dit kan betekenen. [1-3 scenario's]
Wat ik u vraag. [kennisname; OOV-lijn burgemeester; woordvoering]
Wat u van mij krijgt. [melding bij ingreep + rapportageritme + woordvoeringsbouwstenen]
```

### Gemeentesecretaris (GS)

**Kernboodschap.** Als hoogste ambtenaar bent u het scharnier naar het bestuur; u hoort het vóóraf en wijst één vast aanspreekpunt aan.

#### Voorbeeldmemo (verzonnen)

> *Aan: gemeentesecretaris [gemeente] (mede namens de regiogemeenten) · Van: CISO [regio] · Betreft: interventieteam, ter informering · Classificatie: intern*

> **Aanleiding.** De vier gemeenten in onze regio delen één digitale infrastructuur; een kwetsbaarheid bij één raakt potentieel allemaal. Meerdere autoriteiten waarschuwen onafhankelijk voor AI-gedreven aanvalscapaciteit, met een handelingsvenster tot [einddatum venster]. Wachten betekent dat de aanvalskant ons inhaalt vóór we de basis op orde hebben.

> **Wat het interventieteam is.** Een tijdelijk team in "fix-modus" dat náást de reguliere IV-lijn de meest urgente gaten dicht, detectie inricht en de reactie oefent. Het mandaat is belegd bij de directeur Bedrijfsvoering (opdrachtgever) en de CIO (beslisser en budgethouder); u gaf als gemeentesecretaris het groen licht. Het team leent mensen uit de lijn, de lijnverantwoordelijkheid blijft ongewijzigd.

> **Uw rol.** Als hoogste ambtenaar bent u het scharnier naar het bestuur én naar de collega-secretarissen in de regio. Daarom hoort u het vooraf, en bent u degene die de bestuurlijke lijn en de woordvoering afstemt.

> **Wat dit concreet kan betekenen.** (A) een patch buiten het reguliere change-venster, meestal 5-30 minuten onderbreking; (B) een dienst die we bij verdenking van misbruik uren tot dagen stilzetten, met een alternatieve route; (C) het inschakelen van een externe partij, soms fysiek op locatie. Omdat de infrastructuur gedeeld is, kan zo'n ingreep alle vier de gemeenten tegelijk raken.

> **Waarborgen.** Vier-ogen-besluit bij elke ingreep met impact, vastlegging in een besluitenregister binnen 24 uur, en onafhankelijk toezicht (tweede en derde lijn).

> **Wat wij u vragen.** (1) Informeer uw bestuurlijke lijn en de collega-secretarissen; (2) wijs één vast aanspreekpunt aan, naam, rol, 06-nummer, ook buiten kantooruren; (3) laten we de woordvoeringslijn vooraf afstemmen (wie levert feiten, wie communiceert).

> **Wat u van ons krijgt.** Een korte bila vooraf, een melding op het moment van een ingreep, een periodieke voortgangsrapportage, en ondersteuning bij de briefing van burgemeester of raad.

#### Sjabloon

```
Memo GS, ter informering
Aanleiding. [trigger + gedeelde-infrastructuur-zin]
Wat speelt. Tijdelijk team [naam] tot [einddatum]; mandaat bij [opdrachtgever] / [CIO].
Wat kan dit betekenen. [1-3 scenario's + max. onderbreking]
Wat ik u vraag. Aanspreekpunt: [naam, rol, 06-nr]; woordvoering: [wie].
Wat u van mij krijgt. [ritme] + melding bij ingreep.
```

### Directieteam (DT)

**Kernboodschap.** Het dreigingslandschap verschuift; handelen kan nu, in een venster; dat vraagt wendbaarheid, sneller schakelen en de gevolgen accepteren.

#### Voorbeeldmemo (verzonnen)

> *Aan: directieteam · Van: CISO · Betreft: wendbaarheid bij acute cyberdreiging, ter informering*

> **Duiding.** Drie onafhankelijke signalen, een AI-modelleverancier, het nationale CSIRT en een sectorberaad, wijzen dezelfde kant op: de drempel om aan te vallen daalt snel. Wat eerst weken specialistisch werk kostte, kan straks in uren en grotendeels geautomatiseerd. We hebben een venster tot [einddatum venster].

> **Wat dit voor de regio betekent.** Aanvallen versnellen en schalen; onze publieke dienstverlening is kwetsbaar op punten die we al kennen (toegang, patching, segmentatie); en we zijn afhankelijk van ketenpartners die hetzelfde venster voelen.

> **Waarom nú.** De reguliere verbetercyclus, met change-vensters, planning en afstemming, is te traag voor dit venster. Niet omdat de lijn iets fout doet, maar omdat het tempo nu eenmaal hoger moet.

> **Twee sporen.** Het structurele spoor (het verbeterprogramma) loopt ongewijzigd door. Daarnaast een acuut spoor dat gericht de grootste gaten dicht en detectie inricht. Eén bijwerking is bewust: méér detectie betekent dat we vaker en sneller iets zullen afschakelen.

> **Wat we van het DT vragen.** Wendbaarheid. Concreet: (1) aanvaard een hoger tempo en meer, meestal korte, verstoringen; (2) zorg per kritiek proces voor een Plan B, zodat afschakelen geen ramp is; (3) spreek je managers aan op actiebereidheid, niet alleen op het geven van akkoord.

> **Waarborgen & vervolg.** Elke mandaat-inzet is een vier-ogen-besluit met vastlegging en onafhankelijk toezicht. We starten met een eerste werksessie [datum], rapporteren periodiek, en monitoren zowel het resultaat als de cultuurverandering die dit vraagt.

#### Sjabloon

```
DT-memo, ter informering
Duiding. [signalen + venster-datum]
Wat wachten kost. [reguliere doorlooptijd vs. venster]
Twee sporen. Regulier: [programma]. Acuut: [team].
Wat ik van het DT vraag. [tempo/verstoringen aanvaarden]; Plan B: [eigenaar per proces].
Vervolg. [startdatum + ritme]
```

### IB&P (Informatiebeveiliging & Privacy)

**Kernboodschap.** De brede technische toegang raakt persoonsgegevens; jullie blik op grondslag, proportionaliteit en waarborgen hoort er vooraf bij.

#### Voorbeeldmemo (verzonnen)

> *Aan: IB&P-overleg · Van: CISO · Betreft: het interventieteam, mandaat, technische toegang en waarborgen*

> **Aanleiding & beeld.** Onze nulmeting (fictief) laat zien waaróm tempo nodig is: ± 640 accounts zonder MFA (waarvan 61 beheerders), 152 direct exploiteerbare kwetsbaarheden, en een Identity Secure Score van 29%. Stuk voor stuk bekende, dichtbare gaten, maar te veel om in de reguliere cyclus op tijd weg te werken.

> **Wat het interventieteam wél en niet doet.** Het dicht gaten en richt detectie in. Het herschrijft geen beleid, voert geen gedragsmonitoring op medewerkers uit, en neemt de informatiebeveiligingsfunctie niet over, het werkt binnen jullie kaders, alleen sneller.

> **Mandaat & technische toegang.** Drie handelingen mogen zonder akkoord-per-geval (patch buiten change-venster, dienst tijdelijk afschakelen, externen raadplegen), getriggerd door een "Rood"-score en met vier-ogen. De toegang loopt over zes categorieën, identity, monitoring/logging, netwerk, kwetsbaarheden, endpoints en back-up, read-only waar het kan, schrijfrechten alleen waar nodig.

> **Raakvlak met IB&P.** Die toegang raakt persoonsgegevens, dus jullie blik hoort er vooraf bij, niet erachter. Concreet op vier punten: de privacy-toets op het mandaat; accountability (alles in een besluitenregister); de impact-afweging bij afschakelen; en de meldplicht-inschatting bij een vermoed datalek.

> **Wat we van jullie vragen.** (1) Capaciteit van de IB&P-kernleden die in of naast het team werken; (2) meedenken over de kaders, wat mag, wat loggen we, wat vraagt overleg; (3) consulteerbaar zijn bij twijfel; en (4) het tempo meedragen, zodat jullie blik vóór de actie komt en niet als rem erna.

#### Sjabloon

```
IB&P-briefing
Toegang die we voorzien. [systemen per categorie]
Wat we daar wél/niet mee doen. [configuratie/metadata, géén inhoud]
Waarborgen. read-only · geaggregeerd · logging in register · 4-ogen.
Wat we vragen. [capaciteit + consultatie bij twijfel]
```

### Bedrijfsvoering (BVO)

**Kernboodschap.** Drie verwachtingen kalibreren, de dienstverlening kán geraakt worden, het kán binnen uren zonder reguliere change, en je hoort het vooraf via een vast contactpunt.

#### Voorbeeldmemo (verzonnen)

> *Aan: bedrijfsvoeringsoverleg · Van: CISO · Betreft: wat het interventieteam voor jouw cluster kan betekenen*

> **Wat het interventieteam is (kort).** Een tijdelijk team dat de meest urgente beveiligingsgaten dicht, náást de reguliere lijn, tot [einddatum venster]. Het is geen nieuw loket en geen verbeterprogramma, het werkt op tempo binnen een vooraf belegd mandaat.

> **Waarom het bedrijfsvoering raakt, drie verwachtingen.** (1) De dienstverlening kán geraakt worden; (2) het kán binnen uren, zonder de reguliere change-ronde; (3) je hoort het vooraf via één vast contactpunt. Het doel van deze memo is verwachtingen kalibreren, zodat de eerste ingreep geen verrassing is, maar de uitvoering van een bekend scenario.

> **Wat merkt mijn cluster, twee voorbeelden.** (A) We moeten een kritieke patch uitrollen op het gedeelde inlogplatform: ~15 minuten geen toegang, in alle gemeenten tegelijk, vooraf aangekondigd. (B) Bij verdenking van misbruik zetten we een online aanvraagformulier een dag stil voor onderzoek; burgers worden naar balie en telefoon geleid, en je cluster krijgt een dagelijkse statusupdate.

> **Waarom we het je vooraf vertellen.** Jij ziet operationele context die wij niet zien, een piekperiode, een evenement, een lopend traject, een afspraak met een ketenpartner. Die context helpt ons een ingreep beter te timen.

> **Wat we vragen.** (1) Neem kennis van de scenario's; (2) deel ze met je teammanagers, vooral in de dienstverlening; (3) meld knelpunten vooraf, zodat we ze kunnen meewegen.

> **Contact & escalatie.** Vragen lopen vooraf via de CISO; leg per cluster één operationeel contactpunt vast vóór [datum]; escalatie verloopt via de CIO.

#### Sjabloon

```
BVO-memo
Drie verwachtingen. (1) kan geraakt worden; (2) kan binnen uren; (3) je hoort het vooraf.
Scenario voor mijn cluster. [1 voorbeeld + max. onderbreking]
Operationeel contactpunt. [naam per cluster, vóór datum]
Knelpunten die ik nu al zie. [piek/evenement/lopend traject]
```

### Privacy / Functionaris Gegevensbescherming (FG)

**Kernboodschap.** Het interventieteam introduceert geen fundamenteel nieuwe verwerkingen; voorstel: een risicoanalyse-licht, geen volledige DPIA.

#### Voorbeeldmemo (verzonnen)

> *Aan: FG · Van: CISO · Betreft: werkwijze & waarborgen het interventieteam, voorstel risicoanalyse-licht*

> **Aanleiding.** Je vroeg om onderbouwing van grondslag, noodzaak, proportionaliteit en waarborgen bij de inzet van het interventieteam. Deze notitie levert dat materiaal en doet een voorstel voor de vorm van je advies.

> **Wat we doen.** Een tijdelijk team dicht de meest urgente beveiligingsgaten. Het raakvlak met persoonsgegevens is een bijproduct van bestaand IV- en CISO-werk; er ontstaat geen nieuwe verwerking en geen nieuw doel.

> **Technische toegang per categorie.** Identity (account- en MFA-status, geen wachtwoorden), monitoring/logging (gebeurtenissen, geen mailinhoud), netwerk (configuratie en metadata), kwetsbaarheden (asset-gegevens), endpoints (compliance, geen bestanden) en back-up (configuratie). Uitdrukkelijk níet: de inhoud van mailboxen of documenten, en geen profilering of beoordeling van medewerkers.

> **Grondslag & proportionaliteit.** Grondslag: de uitvoering van een taak van algemeen belang (art. 6(1)e AVG), aangevuld met sectorale wetgeving. Proportioneel: read-only en geaggregeerd waar het kan, gegevens blijven binnen het team en de kwaliteitsfunctie, en de inzet is tijdelijk met vastgelegde bewaartermijnen (register langer, scan-output kort, exports retour of vernietigd na afloop).

> **Waarborgen.** Bestaande screening van teamleden, afspraken bij overdracht aan derden, logging van elke mandaat-inzet in het besluitenregister (binnen 24 uur), een afwegingskader vóór elke ingreep, en de reguliere route via het ICT-reglement.

> **Voorstel.** Een risicoanalyse-licht in plaats van een volledige DPIA, er is geen profilering, geen geautomatiseerd besluit met rechtsgevolg en geen grootschalige bijzondere persoonsgegevens, met een periodieke FG-peilstok (steekproef uit het register) als vinger aan de pols.

#### Sjabloon

```
FG-notitie, werkwijze & waarborgen
Grondslag. [art. 6(1)e + sectorale basis]
Proportionaliteit. read-only: [ja/deels]; geen inhoud.
Bewaartermijnen. register: […]; exports: [retour na N dagen]
Vorm advies. risicoanalyse-licht; peilstok elke [N weken].
```

### Leveranciers / infrastructuurpartners

**Kernboodschap.** Een voorstel voor samenwerking in heldere scenario's, gedeeld kanaal, transparant register, directe schakeling waar het kan. "Door het proces, niet eromheen."

#### Voorbeeldmemo (verzonnen)

> *Aan: infrastructuurpartners · Van: CISO / het interventieteam · Betreft: spelregels samenwerking (voorstel)*

> **Context.** Dit is een voorstel en een levend document, reageer waar je iets anders wilt. Het doel: soepel samenwerken op tempo, mét regie, zonder langs ieders processen heen te werken.

> **Vier scenario's.** (1.1) Een signaal of vermoeden, meld het via je vaste liaison; wij triëren twee keer per week in Fix-Now / Latent / Info-only. (1.2) Je ziet iets in het domein van een andere partij, schakel rechtstreeks met die partij, met ons op cc. (1.3) Een het interventieteam-bevinding vraagt een change, die loopt via júllie versnelde change-route; wij leveren de impact-onderbouwing (geraakte processen, risico van wel/niet doen, terugrolplan). (1.4) Wrijving of een meningsverschil, eerst op werkniveau, dan via ons kernteam (vier-ogen, niet de persoonlijke lijn), dan naar opdrachtgever en CIO.

> **Werkomgeving.** Eén gedeeld (cross-tenant) kanaal en een transparant samenwerkings-register waarin per partij staat: de vaste liaison plus back-up, het spoedkanaal, de versnelde change-route, een vertrouwelijk kanaal voor exports en credentials (nooit via gewone mail), en het escalatiepad.

> **Wat er bewust niet in zit.** Echte incidenten in volle gang, daarvoor blijft jullie eigen incident-procedure en de gemeentelijke crisisroute leidend; het interventieteam is geen meldpunt en neemt de regie bij een calamiteit niet over.

> **Wat we vragen.** Vóór [datum]: een vaste liaison (met back-up), je ingevulde rij in het register, en akkoord op deze werkwijze, of een tegenvoorstel waar je iets anders wilt.

#### Sjabloon

```
Rij in het samenwerkings-register
Partij: […]
Vaste liaison + back-up: […]
Spoedkanaal: [telefoon/ticket/IM]
Versnelde change-route: [trigger + doorlooptijd]
Vertrouwelijk kanaal exports: [tool]
Escalatiepad: [accountmgr → senior mgmt → partner-CISO]
```

## Waterschap

### Dagelijks Bestuur & dijkgraaf

**Kernboodschap.** Als vitale aanbieder (NIS2) raakt digitale uitval de waterveiligheid; er werkt tijdelijk een team met mandaat, en de dijkgraaf (crisisbeheersing) is aangesloten.

#### Voorbeeldmemo (verzonnen)

> *Aan: dagelijks bestuur, t.a.v. dijkgraaf · Van: CISO [waterschap] · Betreft: tijdelijk interventieteam, ter informering*

> **Aanleiding.** Drie partijen waarschuwden recent onafhankelijk voor hetzelfde: AI-gedreven aanvalscapaciteit maakt het vinden én misbruiken van kwetsbaarheden sneller en goedkoper, met een handelingsvenster tot [einddatum venster]. Als vitale aanbieder (NIS2) kan digitale uitval ons primaire proces direct raken, waterpeilbeheer, zuivering, dijkbewaking.

> **Wat we doen.** We richten tijdelijk een klein interventieteam in dat náást de reguliere lijn de meest urgente gaten dicht, detectie inricht en de reactie oefent. Het mandaat is belegd bij de secretaris-directeur (opdrachtgever) en de CIO (beslisser en budgethouder); u gaf als dagelijks bestuur het groen licht. Uitdrukkelijk tijdelijk; het vervangt niets.

> **Waarom dit het bestuur raakt.** Om op tempo te kunnen handelen mag het team, onder voorwaarden, buiten de reguliere change-procedure ingrijpen. Bij IT betekent dat hooguit een korte onderbreking; bij OT kan een ingreep fysieke gevolgen hebben, en daar gaat veiligheid altijd vóór snelheid. De gezagsrol van de dijkgraaf bij crisisbeheersing en uw bestuurlijk eigenaarschap blijven volledig bij u.

> **Wat dit concreet kan betekenen.** (A) een spoedpatch op een internet-gericht IT-systeem, vooraf aangekondigd; (B) bij verdenking van misbruik een OT-component tijdelijk afschakelen of overzetten naar handbediening, altijd samen met de proces-eigenaar en met een veilige terugval; (C) het inschakelen van het sector-CERT of een gespecialiseerde leverancier.

> **Waarborgen.** Elke ingreep met merkbare impact is een vier-ogen-besluit, wordt binnen 24 uur vastgelegd, en valt onder onafhankelijk toezicht. Bij OT geldt bovendien: bij twijfel niet handelen, eerst opschalen.

> **Wat wij u vragen.** (1) Neem kennis van het mandaat; (2) bevestig de koppeling met de crisis- en calamiteitenorganisatie voor waterveiligheid; (3) stem de woordvoering vooraf af.

> **Wat u van ons krijgt.** Een melding bij elke ingreep met bestuurlijke of veiligheids-lading, een periodieke voortgangsrapportage, en feitelijke bouwstenen voor uw woordvoering.

#### Sjabloon

```
Memo DB & dijkgraaf, ter informering
Aanleiding. [trigger + venster + NIS2/vitaal]
Waarom het bestuur dit moet weten. [mandaat + OT/waterveiligheid-lading]
Wat dit kan betekenen. [IT-patch; OT-afschakeling met proces-eigenaar; extern]
Wat ik u vraag. [kennisname; koppeling crisisorganisatie; woordvoering]
Wat u van mij krijgt. [melding bij ingreep + rapportageritme]
```

### Secretaris-directeur

**Kernboodschap.** Als ambtelijk eindverantwoordelijke bent u opdrachtgever/scharnier naar het bestuur; u hoort het vóóraf en wijst één vast aanspreekpunt aan.

#### Voorbeeldmemo (verzonnen)

> *Aan: secretaris-directeur [waterschap] · Van: CISO · Betreft: interventieteam, opdracht & informering*

> **Aanleiding.** AI-gedreven aanvalscapaciteit verlaagt de drempel om aan te vallen, met een venster tot [einddatum venster]. Als vitale aanbieder willen we onze meest urgente gaten dichten vóór dat venster sluit.

> **Wat het interventieteam is.** Een tijdelijk team in "fix-modus" dat náást de reguliere lijn werkt. U bent opdrachtgever; de CIO beslist en budgetteert; het team leent mensen uit de lijn, waarvan de verantwoordelijkheid ongewijzigd blijft.

> **Uw rol.** Als ambtelijk eindverantwoordelijke bent u het scharnier naar het dagelijks en algemeen bestuur. U hoort het vooraf, en u verbindt het team met de bestaande crisis- en continuïteitsstructuur.

> **Wat dit concreet kan betekenen.** Patches buiten het change-venster op IT; bij verdenking een tijdelijke afschakeling, bij OT (gemalen, zuivering, peilbeheer) altijd met de proces-eigenaar en een veilige terugval; of het inschakelen van externen. Bij OT gaat veiligheid vóór snelheid.

> **Waarborgen.** Vier-ogen-besluit, vastlegging in een besluitenregister binnen 24 uur, en onafhankelijk toezicht (tweede en derde lijn).

> **Wat wij u vragen.** (1) Informeer het dagelijks bestuur; (2) wijs één vast aanspreekpunt aan, ook buiten kantooruren; (3) bevestig de lijn naar de crisisorganisatie.

> **Wat u van ons krijgt.** Een periodieke rapportage, een melding bij elke ingreep, en, ruim vóór de einddatum, een eindbeeld met advies: verlengen, afbouwen of overdragen aan de lijn.

#### Sjabloon

```
Memo secretaris-directeur
Aanleiding. [trigger + venster + vitaal]
Opdracht & mandaat. [opdrachtgever = u; CIO beslist/budget]
Wat kan dit betekenen. [IT/OT-scenario's]
Wat ik u vraag. Aanspreekpunt: [naam, rol, 06-nr]; lijn crisisorganisatie.
Wat u van mij krijgt. [ritme + eindbeeld vóór einddatum]
```

### Directie / MT

**Kernboodschap.** Handelen kan nu, in een venster; dat vraagt wendbaarheid, en bij een waterschap weegt elke afschakeling zwaar omdat het primaire proces fysiek is.

#### Voorbeeldmemo (verzonnen)

> *Aan: directie / MT · Van: CISO · Betreft: wendbaarheid bij acute cyberdreiging*

> **Duiding.** Onafhankelijke signalen wijzen dezelfde kant op: de aanvalsdrempel daalt snel, en wat eerst weken specialistisch werk kostte kan straks in uren. We hebben een venster tot [einddatum venster].

> **Wat dit voor ons betekent.** Niet alleen onze kantoor-IT is doelwit, maar juist ook onze OT, gemalen, zuivering, peilbeheer, dijkbewaking. Een aanvaller die binnenkomt via IT zoekt het pad naar die processen; uitval raakt de waterveiligheid en de omgeving.

> **Waarom nú.** De reguliere verbetercyclus is te traag voor dit venster. Daarom een tweede, sneller spoor, niet in plaats van, maar náást het verbeterprogramma.

> **Twee sporen.** Het verbeterprogramma loopt ongewijzigd door; het interventieteam is het acute spoor dat gericht gaten dicht en detectie inricht. Méér detectie betekent ook: vaker en sneller ingrijpen.

> **Wat we van het MT vragen.** Wendbaarheid, met een waterschaps-nuance: (1) aanvaard een hoger tempo; (2) zorg per kritiek (OT-)proces voor een Plan B inclusief veilige handbediening, zodat afschakelen beheerst kan; (3) spreek teammanagers aan op actiebereidheid.

> **Waarborgen & vervolg.** Elke mandaat-inzet is een vier-ogen-besluit met vastlegging en onafhankelijk toezicht; bij OT geldt veiligheid vóór snelheid. We starten met een eerste werksessie [datum], rapporteren periodiek, en monitoren resultaat én cultuur.

#### Sjabloon

```
MT-memo
Duiding. [signalen + venster]
Wat het ons raakt. [IT + OT/waterveiligheid]
Twee sporen. Regulier: [programma]. Acuut: het interventieteam.
Wat ik vraag. Plan B per kritiek OT-proces: [eigenaar + handbediening].
Vervolg. [startdatum + ritme]
```

### IB&P (Informatiebeveiliging & Privacy)

**Kernboodschap.** De brede technische toegang raakt persoonsgegevens én OT; jullie blik op grondslag, proportionaliteit en veiligheid hoort er vooraf bij.

#### Voorbeeldmemo (verzonnen)

> *Aan: IB&P-overleg · Van: CISO · Betreft: het interventieteam, mandaat, toegang en waarborgen*

> **Aanleiding & beeld.** Onze nulmeting (fictief) laat zien waaróm tempo nodig is: ± 640 accounts zonder MFA, 152 direct exploiteerbare kwetsbaarheden, en OT-segmenten die onvoldoende gescheiden zijn van de kantoor-IT. Bekende, dichtbare gaten, maar te veel voor de reguliere cyclus binnen het venster.

> **Wat het interventieteam wél en niet doet.** Het dicht gaten en richt detectie in, in IT én OT. Het herschrijft geen beleid en voert geen gedragsmonitoring op medewerkers uit; het werkt binnen jullie kaders, alleen sneller.

> **Mandaat & technische toegang.** Drie handelingen mogen zonder akkoord-per-geval (patch buiten change-venster, dienst/component tijdelijk afschakelen, externen raadplegen), getriggerd door een "Rood"-score en met vier-ogen. Toegang over identity, monitoring/logging, netwerk, kwetsbaarheden, endpoints, back-up én OT-/SCADA-omgevingen, read-only waar het kan, en in OT altijd met de proces-eigenaar.

> **Raakvlak met IB&P.** Jullie blik hoort er vooraf bij, op vier punten: de privacy-toets op het mandaat; accountability (alles in een besluitenregister); de impact-afweging bij afschakelen, met een uitdrukkelijke veiligheidsweging voor OT; en de meldplicht-inschatting.

> **Wat we van jullie vragen.** (1) Capaciteit van de kernleden; (2) meedenken over de kaders, wat mag, wat loggen we, wat vraagt overleg; (3) consulteerbaar zijn bij twijfel; (4) het tempo meedragen, zodat jullie blik vóór de actie komt.

#### Sjabloon

```
IB&P-briefing
Toegang die we voorzien. [IT-systemen + OT/SCADA]
Wat we daar wél/niet mee doen. [config/metadata, géén inhoud]
Waarborgen. read-only · OT met proces-eigenaar · logging · 4-ogen.
Wat we vragen. [capaciteit + consultatie]
```

### Bedrijfsvoering

**Kernboodschap.** Drie verwachtingen kalibreren, bedrijfsvoeringssystemen kunnen geraakt worden, het kan binnen uren, en je hoort het vooraf.

#### Voorbeeldmemo (verzonnen)

> *Aan: bedrijfsvoering · Van: CISO · Betreft: wat het interventieteam voor jouw werkveld kan betekenen*

> **Wat het interventieteam is (kort).** Een tijdelijk team dat de meest urgente beveiligingsgaten dicht, náást de reguliere lijn, tot [einddatum venster].

> **Waarom het bedrijfsvoering raakt, drie verwachtingen.** (1) Bedrijfsvoeringssystemen (financieel, HR, vergunningverlening, heffingen) kunnen geraakt worden; (2) het kán binnen uren, zonder de reguliere change-ronde; (3) je hoort het vooraf via één vast contactpunt. Doel: verwachtingen kalibreren, zodat de eerste ingreep geen verrassing is.

> **Wat merkt mijn werkveld, een voorbeeld.** We rollen een kritieke patch uit op het heffings-/belastingsamenwerkingssysteem: een korte, vooraf aangekondigde onderbreking. Bij verdenking van misbruik zetten we het tijdelijk stil voor onderzoek, met een alternatieve route.

> **Waarom we het je vooraf vertellen.** Jij ziet operationele context die wij niet zien, een piek bij de aanslagoplegging, een lopend traject, een afspraak met een ketenpartner. Die context helpt ons de timing te kiezen.

> **Wat we vragen.** (1) Neem kennis van de scenario's; (2) deel ze met je teammanagers; (3) meld knelpunten vooraf.

> **Contact & escalatie.** Vragen lopen vooraf via de CISO; leg één contactpunt vast vóór [datum]; escalatie via de CIO.

#### Sjabloon

```
Bedrijfsvoering-memo
Drie verwachtingen. (1) kan geraakt worden; (2) kan binnen uren; (3) je hoort het vooraf.
Scenario voor mijn werkveld. [1 voorbeeld + max. onderbreking]
Operationeel contactpunt. [naam, vóór datum]
Knelpunten die ik nu al zie. [piek/lopend traject]
```

### OT / procesautomatisering

**Kernboodschap.** Hier raakt cybersecurity de fysieke wereld; het interventieteam komt nooit zonder de proces-eigenaar aan een OT-component, en veiligheid gaat vóór snelheid.

#### Voorbeeldmemo (verzonnen)

> *Aan: team procesautomatisering / OT-beheer · Van: CISO · Betreft: samenwerking het interventieteam rond OT*

> **Waarom dit jullie raakt.** Een aanvaller die binnenkomt via de kantoor-IT zoekt het pad naar de OT: gemalen, sluizen, zuivering, peilregeling. het interventieteam wil dat pad zichtbaar maken en afsnijden, zonder ooit het proces zelf in gevaar te brengen.

> **De grondregel.** Veiligheid en continuïteit gaan vóór snelheid. het interventieteam komt nooit zonder de proces-eigenaar aan een OT-component, en bij twijfel doen we het niet, dan schalen we eerst op.

> **Werkafspraken.** (1) Read-only en passief waar het kan, we kijken liever dan dat we draaien; (2) elke handeling aan een OT-component gebeurt sámen met de proces-eigenaar en met een veilige terugval (handbediening); (3) we plannen rond kritieke momenten (hoogwater, droogte, gepland onderhoud); (4) elke ingreep heeft een vooraf bekend terugrolpad.

> **Wat we zoeken.** Inzicht in de segmentatie tussen IT en OT, in de remote-toegang van OT-leveranciers, en in de monitoring van de OT-netwerken, zodat we weten of we een aanval in dat domein überhaupt zouden zien.

> **Wat we vragen.** Een vaste OT-contactpersoon in of naast het kernteam, en meedenken over een veilige manier om te oefenen (bijvoorbeeld op een testopstelling in plaats van op een live gemaal).

#### Sjabloon

```
OT-werkafspraken
Scope. [welke OT-systemen/locaties]
Spelregels. read-only waar kan · altijd met proces-eigenaar · veilige terugval · veiligheid vóór snelheid.
Kritieke momenten om te mijden. [hoogwater/droogte/onderhoud]
OT-contactpersoon. [naam + back-up]
```

### Privacy / Functionaris Gegevensbescherming (FG)

**Kernboodschap.** Geen fundamenteel nieuwe verwerkingen; voorstel: een risicoanalyse-licht, geen volledige DPIA.

#### Voorbeeldmemo (verzonnen)

> *Aan: FG · Van: CISO · Betreft: werkwijze & waarborgen het interventieteam*

> **Aanleiding.** Je vroeg om onderbouwing van grondslag, noodzaak, proportionaliteit en waarborgen. Deze notitie levert dat materiaal en doet een voorstel voor de vorm van je advies.

> **Wat we doen.** Een tijdelijk team dicht de meest urgente gaten. Het raakvlak met persoonsgegevens is een bijproduct van bestaand IV- en CISO-werk, geen nieuwe verwerking. OT-gegevens zijn bovendien vooral technische meet- en stuurdata, zelden persoonsgegevens.

> **Technische toegang per categorie.** Identity (account- en MFA-status, geen wachtwoorden), monitoring/logging (gebeurtenissen, geen mailinhoud), netwerk (configuratie en metadata), kwetsbaarheden, endpoints (compliance, geen bestanden), back-up en OT (technische data). Uitdrukkelijk níet: inhoud van mailboxen of documenten, en geen profilering van medewerkers.

> **Grondslag & proportionaliteit.** Grondslag: uitvoering van een taak van algemeen belang (art. 6(1)e AVG), aangevuld met sectorale wetgeving. Proportioneel: read-only en geaggregeerd waar het kan, gegevens binnen team en kwaliteitsfunctie, tijdelijk, met vastgelegde bewaartermijnen.

> **Waarborgen.** Bestaande screening, afspraken bij overdracht aan derden, logging van elke mandaat-inzet in het besluitenregister, een afwegingskader vóór elke ingreep, en de reguliere route via het ICT-reglement.

> **Voorstel.** Een risicoanalyse-licht in plaats van een volledige DPIA, geen profilering, geen geautomatiseerd besluit met rechtsgevolg, met een periodieke FG-peilstok als vinger aan de pols.

#### Sjabloon

```
FG-notitie
Grondslag. [art. 6(1)e + sectorale basis]
Proportionaliteit. read-only: [ja/deels]; geen inhoud.
Bewaartermijnen. [register / exports]
Vorm advies. risicoanalyse-licht; peilstok elke [N weken].
```

### Leveranciers / infrastructuurpartners (incl. OT)

**Kernboodschap.** Samenwerking in heldere scenario's, met extra aandacht voor OT-/SCADA-leveranciers en hun remote-toegang.

#### Voorbeeldmemo (verzonnen)

> *Aan: infrastructuur- en OT-partners · Van: CISO / het interventieteam · Betreft: spelregels samenwerking (voorstel)*

> **Context.** Dit is een voorstel en een levend document, reageer waar je iets anders wilt. Doel: soepel samenwerken op tempo, mét regie, met extra aandacht voor de OT-/SCADA-kant.

> **Vier scenario's.** Als bij IT: (1.1) een signaal/vermoeden via je vaste liaison; (1.2) partij-naar-partij rechtstreeks, met ons op cc; (1.3) een het interventieteam-bevinding die een change vraagt loopt via júllie versnelde change-route, wij leveren de impact-onderbouwing; (1.4) wrijving via een drietraps-escalatie (werkniveau → kernteam → opdrachtgever/CIO).

> **Extra voor OT.** De remote-toegang van OT-leveranciers wordt geïnventariseerd en waar nodig ingeperkt; changes aan OT lopen altijd via de proces-eigenaar met een veilige terugval; en er zijn geen losse "even-inbellen"-routes buiten het register om. Veiligheid gaat vóór snelheid.

> **Werkomgeving.** Eén gedeeld (cross-tenant) kanaal en een transparant samenwerkings-register (vaste liaison, spoedkanaal, versnelde change-route, escalatiepad), plus een vertrouwelijk kanaal voor exports en credentials, nooit via gewone mail.

> **Wat er bewust niet in zit.** Echte incidenten in volle gang, daarvoor blijft jullie eigen incident-procedure en de crisisroute van het waterschap leidend; het interventieteam is geen meldpunt.

> **Wat we vragen.** Vóór [datum]: een vaste liaison (ook voor OT, met back-up), je ingevulde rij in het register, en akkoord op deze werkwijze, of een tegenvoorstel.

#### Sjabloon

```
Rij in het samenwerkings-register (OT)
Partij: […]
Liaison + back-up: […]
Remote-toegang OT: [hoe, wanneer, door wie]
Versnelde change-route OT: [via proces-eigenaar + terugval]
Vertrouwelijk kanaal exports/credentials: [tool]
Escalatiepad: [accountmgr → senior mgmt → partner-CISO]
```
