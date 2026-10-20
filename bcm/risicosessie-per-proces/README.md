---
titel: Een risicosessie per kritiek proces, met de proceseigenaar aan tafel
vakgebied: bcm
type: aanpak
normen: [BIO2, ISO 22301, Cbw]
peildatum: 2026-10-20
herkomst: sessieformat van het team informatiebeveiliging, privacy en bedrijfscontinuïteit van een regionale samenwerking van gemeenten, 2025 tot 2026, gebruikt voor twintig kritieke processen
status: in gebruik
samenvatting: Een vast format voor een sessie van anderhalf uur met de proceseigenaar per kritiek proces. In drie stappen classificeer je het proces op beschikbaarheid, integriteit en vertrouwelijkheid, breng je de applicaties in kaart die het proces draaien, en leg je de procescontext vast met een canvas: ketenpartners, piekperiodes, wetgeving, persoonsgegevens. Zo voer je de bedrijfsimpactanalyse uit met de lijn in plaats van voor de lijn. De uitkomst is de basis voor herstelafspraken met IT-beheer, het bedrijfscontinuïteitsplan en de risicoanalyse onder BIO 2.0 en de Cyberbeveiligingswet.
barrieres: [critical, dependencies]
rol: verdieping
pijler: kritieke-processen-vaststellen
---

# Een risicosessie per kritiek proces, met de proceseigenaar aan tafel

> **Lees de aanpak online:** [security-commons-nl.github.io/kennisbank/bcm/risicosessie-per-proces](https://security-commons-nl.github.io/kennisbank/bcm/risicosessie-per-proces/)

Een lijst met kritieke processen is een begin. Maar wat een proces echt nodig heeft, weet alleen de
proceseigenaar: hoe lang het mag stilliggen, welke applicaties het draaien, wie er in de keten van afhangt.
Dat haal je niet uit een vragenlijst per mail. Je haalt het op in een gesprek, en dit is het format daarvoor.

Een regionale samenwerking van vier gemeenten liep zo twintig kritieke processen langs, van reisdocumenten
en de basisregistratie personen tot uitkeringen, jeugdzorg, verkiezingen en het klantcontactcentrum. Het
doel: informatiebeveiliging, informatievoorziening en bedrijfscontinuïteit op één manier inrichten, op basis
van eisen die de lijn zelf heeft gesteld.

## Wanneer wel, wanneer niet

Wel voor elk proces op de lijst van kritieke processen (zie
[Kritieke processen en herstelprioriteiten vaststellen](../kritieke-processen-vaststellen/)), en opnieuw bij
een grote wijziging: nieuwe applicatie, nieuwe leverancier, andere organisatie.

Niet als vervanging van het bedrijfscontinuïteitsplan. De sessie levert de eisen; het plan beschrijft wat je
doet als het misgaat. Ook niet zonder de proceseigenaar: zonder hem wordt het een IT-classificatie, en die
wordt later betwist.

## Wie er aan tafel zit

| Rol | Waarom |
|---|---|
| Proceseigenaar | Hoofdrolspeler. Weet wat het proces betekent en wat er gebeurt als het misgaat |
| Inhoudelijk expert uit het proces | Kent de dagelijkse uitvoering, de pieken en de workarounds |
| Gespreksleider (BCM of informatiebeveiliging) | Leidt de drie stappen, bewaakt de tijd, vraagt door |
| Notulist | Vult de classificatie, de applicatielijst en het canvas live in |
| Op afroep: functioneel beheer, architectuur | Bij twijfel over welke applicaties het proces gebruikt |

## De sessie in drie stappen

Reken op anderhalf uur. Begin met tien minuten waarom: één aanpak voor beveiliging, informatievoorziening en
continuïteit, op basis van eisen die de lijn zelf stelt. Zeg ook: "Jullie zijn vandaag de hoofdrolspelers."

### Stap 1. Classificatie (40 minuten)

Classificeer het proces op beschikbaarheid, integriteit en vertrouwelijkheid met het
[classificatieschema in vijf niveaus](../kritieke-processen-vaststellen/classificatieschema-biv.md). Stel de
vragen per aspect uit dat schema en kies pas daarna het niveau. Begin altijd met beschikbaarheid, want daar
hebben proceseigenaren het scherpste beeld van: "Dit proces valt morgenochtend volledig uit. Wanneer wordt
dat echt een probleem?"

Leg per aspect het niveau vast én de reden in een zin. De reden is wat je over een jaar nodig hebt als
iemand vraagt waarom dit proces op 4 staat.

### Stap 2. Ondersteunende applicaties (20 minuten)

Loop het proces door van invoer via activiteiten naar uitvoer en vraag bij elke stap: welke applicatie maakt
dit mogelijk? Denk aan vakapplicaties, registratie- en workflowsystemen, opslag en archief, e-mail,
publicatieplatforms en koppelingen met landelijke voorzieningen. De applicaties erven de classificatie van
het proces; een applicatie die in meerdere processen zit, krijgt het hoogste niveau.

### Stap 3. Procescontext (25 minuten)

Leg de context vast met een canvas van tien blokken. Je hoeft niet alles in te vullen; de vragen zijn
geheugensteun.

| Blok | Vragen |
|---|---|
| Kernpartners | Welke ketenpartners zijn betrokken (bijvoorbeeld RvIG, UWV, RDW, IND, CJIB, IBD)? Welke andere gemeenten of leveranciers? Welke afspraken, convenanten of wettelijke partnerschappen? Wie is onmisbaar? |
| Kernactiviteiten | Wat doet het proces in twee of drie zinnen, wat is de trigger en wat het eindresultaat? Hoe vaak loopt het? Zijn er piekperiodes waarin het extra kritiek is? Zijn er spoedvarianten? |
| Waardepropositie | Welke waarde levert het proces aan inwoners of samenleving? Welk probleem lost het op? |
| Klantrelaties | Zelfbediening of persoonlijk contact? Hoe is het klantcontact gedigitaliseerd (DigiD, e-formulieren)? |
| Klantsegmenten | Voor wie: inwoners, bedrijven, andere overheden? Zijn er doelgroepen die extra ondersteuning nodig hebben? |
| Kernmiddelen | Welke hardware, systemen, data, mensen, locaties, vergunningen en bevoegdheden zijn nodig? Welke gegevens worden gebruikt? |
| Kanalen | Post, app, balie, e-mail? Hoe wordt aangevraagd, beoordeeld en geleverd? |
| Kostenstructuur | Personeel, licenties, infrastructuur, uitbesteding. Wat is het duurst? |
| Kernaspecten | Welke wet- en regelgeving geldt? Welke positie heeft het proces in de keten? Welke continuïteitseisen gelden? |
| Baten | Welke financiële of maatschappelijke baten? Draagt het bij aan beleidsdoelen? |

Sluit af met één vraag over persoonsgegevens: verwerkt het proces persoonsgegevens, en zo ja, ook bijzondere?
Dat bepaalt of er een DPIA moet komen.

### Afronding (5 minuten)

Vertel wat er met de uitkomst gebeurt: de sessie wordt voor alle kritieke processen gehouden, de uitkomst
wordt afgestemd met de andere gemeenten, en daarna formeel vastgesteld. Pas dan wordt het een eis waar
IT-beheer en leveranciers op worden aangesproken.

## Tips uit de praktijk

- **Bereid het canvas voor.** Vul vooraf in wat je al weet uit procesbeschrijving en applicatielandschap. Dan
  gaat de sessie over controleren en aanvullen, niet over overtypen.
- **Eén proces per sessie.** Twee processen in anderhalf uur lukt niet; de tweede wordt dan een
  IT-classificatie.
- **Laat de proceseigenaar het niveau kiezen.** De gespreksleider stelt de vragen en mag doorvragen, maar het
  niveau is van de lijn.
- **Gebruik een vaste presentatie per proces**, met de naam en het nummer van het proces op elke dia, zodat
  het verslag direct aan het proces hangt.

## Bewijs

- Per kritiek proces een **sessieverslag** met de classificatie per aspect en de reden, de lijst met
  applicaties en het ingevulde canvas.
- Het **overzicht van alle kritieke processen** met hun classificatie, vastgesteld door het bevoegde gremium.
- De **afgeleide herstelnormen** (RTO, RPO) per proces en per applicatie, en de afspraken met IT-beheer en
  leveranciers die daarop gebaseerd zijn.

## BIO 2.0

| Maatregel | Wat de sessie daarvoor levert |
|---|---|
| 5.12 Classificeren van informatie | De classificatie per proces, door de proceseigenaar |
| 5.9 Inventarisatie van informatie en andere gerelateerde bedrijfsmiddelen | De applicaties per proces, met eigenaar |
| 5.30 ICT-gereedheid voor bedrijfscontinuïteit | De hersteleisen die IT-beheer moet waarmaken |
| 5.29 Informatiebeveiliging tijdens een verstoring | De eisen die ook tijdens uitval blijven gelden |
| 5.21 Beheren van informatiebeveiliging in de ICT-toeleveringsketen | Het blok kernpartners: wie in de keten onmisbaar is |

Onder ISO 22301 is dit de bedrijfsimpactanalyse (8.2.2). Onder de Cyberbeveiligingswet levert het de
onderbouwing van de risicoanalyse en de basis voor het oordeel welk incident significant is.

## Zo leg je het uit

**Aan de proceseigenaar.** "Jij weet als geen ander wat er gebeurt als dit proces stilvalt. Wij hebben die
kennis nodig om IT, beveiliging en continuïteit zo in te richten dat het past bij wat jouw proces vraagt,
niet bij wat wij denken dat het vraagt."

**Aan de directie.** "Twintig sessies van anderhalf uur, en daarna weten we per kritiek proces wat het nodig
heeft en wat het mag kosten als het misgaat. Dat is de basis onder alle afspraken met IT-beheer en
leveranciers, en onder onze verantwoording aan de toezichthouder."

**Aan IT-beheer.** "Dit zijn de eisen van de lijn, niet van ons. Als jullie een hersteltijd niet kunnen
halen, horen we dat liever nu dan tijdens de storing."
