---
titel: Bedrijfscontinuïteitsplan, een compact sjabloon
vakgebied: bcm
type: sjabloon
normen: [Cbw, NIS2, BIO2, ISO 22301]
peildatum: 2026-10-15
herkomst: opgesteld door de CISO van een gemeente voor een interbestuurlijke werkgroep bedrijfscontinuïteit
status: sjabloon
route: geen
samenvatting: Een bedrijfscontinuïteitsplan dat uitgeprint werkt op de dag dat de ICT eruit ligt:
  crisisteam, herstelvolgorde, opschaling, drie fasen, scenario's, noodcommunicatie en meldingen, met
  bereikbaarheidslijst, logboek, crisiskoffer en actiekaarten. Voor elke bestuurslaag, met een termenlijst.
  Met een vragenlijst per kritiek proces langs zeven bronnen van verstoring, een ingevuld voorbeeld voor het klantcontactcentrum en een proceskaart voor het gemeentelijke calamiteitenteam.
barrieres: [crisis]
rol: verdieping
bronnen: [ibd-model-continuiteitsplan, ibd-model-continuiteitsstrategie, ibd-handreiking-bedrijfscontinuiteitsbeheer, ibd-scenariokaart-1-uitval-gebouw, ibd-scenariokaart-2-uitval-door-stroomstoring, ibd-scenariokaart-3-uitval-ict, ibd-scenariokaart-7-uitval-personeel, cip-ketencommunicatiebijcrises]
---

> **Lees dit sjabloon online:** [security-commons-nl.github.io/kennisbank/bcm/bedrijfscontinuiteitsplan-sjabloon](https://security-commons-nl.github.io/kennisbank/bcm/bedrijfscontinuiteitsplan-sjabloon/)

# Bedrijfscontinuïteitsplan, een compact sjabloon

> **Barriere:** oefen het ransomware- en crisisherstelplan. Dit is het plan zelf, in een vorm die je kunt
> oefenen: wie besluit, in welke volgorde je herstelt, en wat je op papier nodig hebt als de systemen weg zijn.

Een bedrijfscontinuïteitsplan wordt gelezen op de slechtste dag van het jaar, door mensen onder druk, vaak
zonder de systemen waar het plan op staat. Dat bepaalt de vorm: kort, met tabellen in plaats van proza, een
actielijst per fase, en alles wat je op de dag zelf moet opzoeken als bijlage op papier.

Het sjabloon staat in [bcp-sjabloon.md](bcp-sjabloon.md). Het is generiek voor de publieke sector; waar de
bestuurslaag verschil maakt, staat het als invulveld.

## Wanneer gebruik je het

Als er een lijst kritieke diensten met hersteltijden ligt, of die in dezelfde ronde ontstaat. Tabel 1 van het
plan wordt gevuld vanuit de BIA; het [BIA-sjabloon](../bia-en-risicoanalyse-sjabloon/) levert precies die
kolommen.

Heb je nog geen team dat een digitale calamiteit bestuurt, begin dan bij
[een digitaal calamiteitenteam opzetten](../calamiteitenteam-digitaal-opzetten/). Dat stuk gaat over het
team en de werkwijze; dit sjabloon is het plan dat dat team gebruikt.

## Hoe het plan is opgebouwd

| Deel | Hoofdstuk | Wat erin staat |
|---|---|---|
| Weten | 1. Crisisteam | Samenstelling met plaatsvervangers, taken, vergaderplaats en uitwijk |
| | 2. Kritieke diensten | Tabel 1: herstelvolgorde met MTPD, RTO, RPO en noodniveau. Tabel 2: wat elke dienst nodig heeft, met de enkelvoudige afhankelijkheden |
| Doen | 3. Opschaling en activering | Wie meldt, wie besluit, en de drempels |
| | 4. De drie fasen | Actielijst voor de acute fase, het noodbedrijf en de terugkeer |
| | 5. Scenario's | Terugvalmaatregelen bij uitval van mensen, huisvesting, nutsvoorzieningen, ICT en leveranciers |
| | 6. Noodcommunicatie en meldingen | Kanalen buiten de eigen ICT, de wettelijke meldingen met termijn, kernboodschappen |
| Onderhouden | 7. OTO en beheer | Wat je hoe vaak oefent en test |
| | 8. Waar het plan aan voldoet | De verplichtingen uit Cbw, Wwke en BIO2, met de plek in het plan |
| Bijlagen | 1 tot en met 4 | Bereikbaarheidslijst, logboek, crisiskoffer, actiekaarten |

## Drie keuzes die het verschil maken

1. **Een exemplaar buiten de eigen ICT.** Een plan dat alleen op het netwerk staat, is weg op het moment dat
   je het nodig hebt. Drie plekken: de crisiskoffer, bij elk lid van het crisisteam, en de uitwijklocatie.
2. **De enkelvoudige afhankelijkheid als eerste kolom die je leest.** Tabel 2 eindigt met de vraag of een
   dienst op een persoon, een systeem of een leverancier drijft. Dat is de dienst waar het plan het eerst over
   gaat, en meestal de dienst waar niemand aan dacht.
3. **De meldplicht loopt los van de opschaling.** Een significant incident onder de Cbw moet je binnen 24 uur
   melden, ook als het crisisteam nog niet bijeen is. Wie dat doet en hoe die persoon bereikbaar is, staat in
   hoofdstuk 6.2 en in de bereikbaarheidslijst. Welke organisaties onder de Cbw vallen staat in
   [val ik onder de Cbw](../../governance/val-ik-onder-de-cbw/).

## Wat je per bestuurslaag invult

Het sjabloon laat open wat per laag anders is:

| Onderwerp | Gemeente, provincie, waterschap | Rijk |
|---|---|---|
| Wie het plan vaststelt | Gemeentesecretaris, provinciesecretaris, secretaris-directeur | Secretaris-generaal of directeur van het onderdeel |
| Opschaling | Eigen crisisorganisatie, zo nodig de veiligheidsregio | Departementaal coördinatiecentrum crisisbeheersing, bij nationale opschaling het nationale crisiscentrum |
| Prioritering van diensten | Uitkomst van de BIA | Uitkomst van de BIA, naast de classificatie van te beschermen belangen |
| Rubricering van het plan | Eigen classificatiebeleid | Voorschrift vertrouwelijkheid rijksdienst |

## Waar dit vandaan komt

De opbouw (crisisteam, opschaling, drie fasen, scenario's, logboek, koffer, actiekaarten) volgt een Engelstalig
BCP-sjabloon voor organisaties van Leicestershire County Council (Verenigd Koninkrijk). De tekst is nieuw geschreven voor de Nederlandse publieke sector. Weggelaten zijn de Britse delen over
bommeldingen en verdachte post, die in Nederland in het calamiteitenplan van het gebouw staan. Toegevoegd zijn
de wettelijke meldingen, de BIO2-maatregelen, het toelaatbare dataverlies (RPO) en een eigen hoofdstuk
noodcommunicatie. De vertaalkeuzes per term staan in de [termenlijst](termenlijst.md).

De IBD heeft voor gemeenten een uitgebreider model continuïteitsplan en zeven scenariokaarten voor het
crisisteam; die staan hieronder bij *Wat anderen al hebben*. Dit sjabloon is korter en niet gemeentelijk van
opzet. De scenariokaarten zijn goed te gebruiken naast hoofdstuk 5.

## Hoe dit samenhangt

Dit sjabloon hoort bij barriere `crisis` uit de
[zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/), als verdieping naast
[crisisoefening voor ransomware en uitval](../../security/crisisoefening/) en
[een digitaal calamiteitenteam opzetten](../calamiteitenteam-digitaal-opzetten/). De uitwijk per dienst
(hoofdstuk 5.4) werk je uit met de [uitwijkkaart](../uitwijk-regelen/). Voor de communicatie naar buiten:
[cyber-crisiscommunicatie](../../security/crisiscommunicatie/).

## Wat er in deze map staat

- [bcp-sjabloon.md](bcp-sjabloon.md): het plan, met vier bijlagen
- [vragenlijst-per-proces.md](vragenlijst-per-proces.md): het gesprek per kritiek proces dat het plan vult,
  langs gebouwen, mensen, nutsvoorzieningen, bedrijfsmiddelen, leveranciers, ICT en communicatiekanalen
- [voorbeeld-klantcontactcentrum.md](voorbeeld-klantcontactcentrum.md): een ingevulde vragenlijst, ingekort
  en geanonimiseerd, met wat goed werkt en wat open bleef
- [proceskaart-calamiteitenteam.md](proceskaart-calamiteitenteam.md): een kaart van één pagina voor het
  calamiteitenteam bij uitval van een kritiek proces, met agenda volgens beeld, oordeel en besluit
- [termenlijst.md](termenlijst.md): Engelse BCM-termen en de Nederlandse term in het sjabloon, met de
  vertaalkeuzes

## Licentie

[EUPL-1.2](../../LICENSE).
