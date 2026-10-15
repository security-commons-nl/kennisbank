---
titel: BIA en risicoanalyse per kritieke dienst, een basissjabloon
vakgebied: bcm
type: sjabloon
normen: [ISO 22301, BIO2, Cbw]
peildatum: 2026-10-15
herkomst: opgesteld door de CISO van een gemeente voor een interbestuurlijke werkgroep bedrijfscontinuïteit
status: concept
samenvatting: Een basissjabloon voor een business impact analyse en een risicoanalyse dat elke
  overheidslaag kan gebruiken: een blad per dienst met identificatie, impact per tijdvenster, hersteleisen,
  afhankelijkheden en terugval, en een risicotabel met dezelfde impactschaal. Met een vergelijking van tien
  bestaande formats, wat elk ervan mist, en de vier keuzes die je maakt voordat je het sjabloon invult.
barrieres: [critical]
rol: verdieping
bronnen: [ibd-bedrijfsimpactanalyse-bia, ibd-bio2-kans-en-impact-tabellen-gemeenten, ibd-bio2-kritieke-processen-gemeenten, ibd-bepalen-bedrijfscontinuiteitsvereisten, ibd-bio-2-template-risicoanalyse-tabel, ibd-bio-handreiking-risicomanagement-voor-gemeenten, ibd-diepgaande-risicoanalyse-methode-excel, ibd-handreiking-diepgaande-risicoanalyse-methode-gemeenten]
---

# BIA en risicoanalyse per kritieke dienst, een basissjabloon

> **Lees dit sjabloon online:** [security-commons-nl.github.io/kennisbank/bcm/bia-en-risicoanalyse-sjabloon](https://security-commons-nl.github.io/kennisbank/bcm/bia-en-risicoanalyse-sjabloon/)

> **Barriere:** stel kritieke processen en herstelprioriteiten vast. Dit sjabloon is de invulvorm bij die
> stap: per dienst de impact, de hersteleisen en de risico's, op een schaal die tussen organisaties
> vergelijkbaar is.

Formats voor een business impact analyse (BIA) en een risicoanalyse zijn er genoeg. De IBD heeft een publieke
set voor gemeenten, NIST een sjabloon voor de Amerikaanse federale overheid, en verschillende overheden
hebben een eigen versie. Wat ontbreekt is een sjabloon dat elke overheidslaag kan gebruiken en dat de BIA en
de risicoanalyse op dezelfde impactschaal zet. Zonder die gedeelde schaal krijgt een dienst twee
kriticiteitsbepalingen, een uit de BIA en een uit de risicoanalyse, en die spreken elkaar tegen.

Dit sjabloon volgt in de opbouw [ISO/TS 22317](https://www.iso.org/standard/79000.html), de technische
specificatie voor de BIA bij ISO 22301, en in de vulling de formats die in gemeenten al in gebruik zijn.

## Wanneer gebruik je het

Als je per kritieke dienst de hersteleisen wilt vastleggen en de lijst kritieke diensten er al ligt, of in
dezelfde ronde ontstaat. Hoe je die lijst met de lijn maakt staat in
[kritieke processen en herstelprioriteiten vaststellen](../kritieke-processen-vaststellen/).

Wil je de BIA en de BIV-classificatie per proces liever in een instrument doen dat zelf rekent, gebruik dan
[procescheck](https://security-commons-nl.github.io/procescheck/). Dit sjabloon is de papieren vorm, voor wie
de uitkomst in een eigen register of spreadsheet wil houden en wil kunnen vergelijken met andere
organisaties.

## Het sjabloon

Het sjabloon zelf staat in [sjabloon.md](sjabloon.md): blad 1 de BIA per dienst (blokken A tot en met H),
blad 2 de risicotabel. Kort wat erin zit:

| Blok | Wat je vastlegt |
|---|---|
| A. Identificatie | Organisatie, bestuurslaag, dienst, eigenaar, versie, en de koppeling aan een procesregister |
| B. Wat de dienst levert | Product, doelgroep, wettelijke grondslag, de keten waar de dienst in zit |
| C. Impact per tijdvenster | Vaste vensters (4 uur, 1 dag, 3 dagen, 1 week, 1 maand) tegen vaste impactcategorieën |
| D. Hersteleisen | MTPD, RTO, RPO en noodniveau, elk met de onderbouwing |
| E. Middelen en afhankelijkheden | De zeven MAPGOOD-middelen plus ketenpartners en leveranciers, met per middel of het een enkelvoudig punt van uitval is |
| F. Terugval | Welke alternatieve werkwijze er is, hoe lang die volhoudt |
| G. Dreigingen en bestaande maatregelen | De brug naar de risicotabel |
| H. Uitkomst | Kriticiteitsklasse, en als je dat wilt de BIV-classificatie, uit dezelfde impactscores |

De risicotabel op blad 2 gebruikt per risico dezelfde impactcategorieën als blok C. Dat is de belangrijkste
winst van een gezamenlijk sjabloon.

## Vier keuzes voordat je invult

1. **Proces of dienst als eenheid.** Een dienst is wat de inwoner en de keten zien, een proces is wat de
   organisatie stuurt. Het advies is de dienst als eenheid, met de processen als regels eronder. Dan sluit de
   BIA aan op hoe ketenpartners en toezichthouders naar je kijken, en blijft hij bruikbaar als de organisatie
   zich anders indeelt.
2. **Tijdvensters en niveaus.** Begin bij vier uur. Die grens komt terug in de regelgeving voor de sector
   overheid: de regeling onder de Wet weerbaarheid kritieke entiteiten legt de drempel voor een aanzienlijke
   verstoring onder meer bij vier uur uitval. Gebruik een schaal met een beschrijving per niveau, zodat
   "hoog" in de ene organisatie hetzelfde betekent als in de andere. Voor gemeenten ligt de schaal er al: de
   vijf niveaus uit de BIO2 kans- en impacttabellen van de IBD. Die teksten staan niet in dit sjabloon,
   want ze vallen onder een licentie die niet-commercieel gebruik voorschrijft; haal ze bij de IBD.
3. **BIV wel of niet in de BIA.** Informatiebeveiligers willen de classificatie op beschikbaarheid,
   integriteit en vertrouwelijkheid erin; ISO 22317 kent haar niet. Het advies: leid haar af in blok H uit
   dezelfde impactscores, en doe geen aparte beoordeling.
4. **Een scoringslogica in de hele organisatie.** Gebruikt de organisatie al een impactschaal voor
   informatiebeveiliging of voor de classificatie van te beschermen belangen, neem die dan over in blok C.
   Twee schalen naast elkaar is de versnippering die dit sjabloon moet voorkomen.

## Wat er al is, en wat elk format mist

| Format | Van | Vorm | Eenheid | Wat het mist |
|---|---|---|---|---|
| Bedrijfsimpactanalyse (BIA) | IBD | Excel: intake, impactanalyse, resultaat | Proces | Meet alleen beschikbaarheid, levert een beveiligingsniveau op in plaats van een continuïteitsprofiel |
| BIO2 Kritieke processen gemeenten | IBD | Excel, twaalf uitgewerkte processen met RPO en RTO | Proces | Landelijk voorbeeld, geen eigen analyse; bruikbaar om je uitkomst te kalibreren |
| Business Impact Analysis Template bij [SP 800-34](https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final) | NIST | Word, drie stappen | Informatiesysteem | Vertrekt bij het systeem in plaats van de dienst; wel de beste uitleg waarom elke hersteltijd een onderbouwing nodig heeft |
| [ISO/TS 22317](https://www.iso.org/standard/79000.html) | ISO | Specificatie, geen sjabloon; betaald | Product of dienst, activiteit | Het skelet: MTPD, RTO, RPO, minimaal dienstverleningsniveau, middelen en afhankelijkheden |
| Diepgaande Risicoanalyse Methode Gemeenten | IBD | Excel met berekeningen, plus handreiking | Proces of systeem | Sinds versie 3.1 met bedrijfscontinuïteit erin; gemeentelijk vocabulaire |
| BIO2 Handreiking risicomanagement en risicoanalysetabel | IBD | Handreiking, Excel-tabel en sjablonen | Proces | Compleet en recent; de invalshoek via een business model canvas vraagt uitleg |
| [SP 800-30](https://csrc.nist.gov/pubs/sp/800/30/r1/final) | NIST | Gids met schalen | Organisatie, missie, systeem | Referentie voor schalen, als invulformat te zwaar |
| [A basic risk assessment and management method](https://www.ncsc.gov.uk/collection/risk-management/a-basic-risk-assessment-and-management-method) | NCSC (VK) | Webmethode, elf stappen | Organisatie | Geen sjabloon, wel de eenvoudigste uitleg; geschikt voor kleine organisaties |

Elk BIA-format hierboven mist minstens een onderdeel van het ISO-skelet: de IBD-formats het minimale
dienstverleningsniveau, NIST de dienst als vertrekpunt. Het sjabloon in deze map vult die aan.

## Hoe dit samenhangt

Dit sjabloon hoort bij barriere `critical` uit de
[zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/), als verdieping naast
[kritieke processen en herstelprioriteiten vaststellen](../kritieke-processen-vaststellen/). De hersteleisen
uit blok D zijn de invoer voor de [uitwijkkaart](../uitwijk-regelen/) en voor tabel 1 van het
[bedrijfscontinuïteitsplan](../bedrijfscontinuiteitsplan-sjabloon/). De afhankelijkheden uit blok E zijn het
startpunt voor [ketenafhankelijkheden in beeld](../../security/ketenafhankelijkheden/). Een risicoanalyse die
bij de aanvaller begint in plaats van bij de dienst staat in
[risicoanalyse langs aanvalspaden](../../security/risicoanalyse-aanvalspaden/).

## Wat er in deze map staat

- [sjabloon.md](sjabloon.md): blad 1 (BIA per dienst, blokken A tot en met H) en blad 2 (risicotabel), met de
  impactschaal

## Licentie

[EUPL-1.2](../../LICENSE).
