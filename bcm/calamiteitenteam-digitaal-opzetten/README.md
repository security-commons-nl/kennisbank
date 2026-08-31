---
titel: Een digitaal calamiteitenteam opzetten
vakgebied: bcm
type: handleiding
normen: [NIS2, BIO2, ISO 22301]
peildatum: 2026-08-31
herkomst: in gebruik bij de crisisorganisatie van een gemeente
status: sjabloon
samenvatting: Een startpakket voor de organisatie die nog geen team heeft dat een digitale calamiteit
  bestrijdt. Rolverdeling, logboek, sleutelbesluiten en evaluatie, met de invulformulieren erbij.
  Bewust binnen de eigen bedrijfsvoering te beleggen, zodat je volgende week kunt beginnen zonder eerst
  de crisisorganisatie te hoeven veranderen.
barrieres: [crisis]
rol: alternatief
---

# Een digitaal calamiteitenteam opzetten

Als er morgen ransomware in je netwerk zit, wie zit er dan om tafel? Bij veel publieke organisaties is
het antwoord: dat zoeken we op dat moment uit. Er is een crisisorganisatie voor een brand of een
overstroming, en er is een IT-afdeling die de storing oplost, maar tussen die twee in zit niets dat een
digitale calamiteit bestuurt.

Dit is het gereedschap om dat gat te vullen met wat je zelf al in huis hebt. Geen structuurwijziging,
geen bestuurlijk traject: je zet de mensen uit je eigen bedrijfsvoering bij elkaar, geeft ze een
rolverdeling, een logboek en een besluitprocedure, en dan kun je oefenen.

## Twee vragen, en dit stuk beantwoordt er één

Er zijn twee manieren om digitale crisisrespons te beleggen, en ze lossen iets anders op.

1. **Zet de juiste mensen uit de bedrijfsvoering bij elkaar.** Snel, binnen je eigen span of control,
   geen besluit van het bestuur nodig. Je krijgt een team dat de calamiteit *bestrijdt*. Dat is dit stuk.
2. **Hang het onder de crisisorganisatie.** Trager, vraagt de eigenaar van de crisisorganisatie en de
   gemeentesecretaris. Je krijgt *mandaat*, bestuurlijke aansluiting en een geoefende vastleggingslijn.

De eerlijke volgorde is meestal eerst 1, dan 2. En er is één ding dat route 1 principieel niet kan: een
oordeel geven dat de organisatie bindt. Onder NIS2 en de Nederlandse Cyberbeveiligingswet moet je een
significant incident melden, en een van de drempels is de vraag of de financiële gevolgen binnen de
begroting op te vangen zijn. Dat is geen IT-oordeel maar een begrotingsoordeel, en aan de tafel van
route 1 zit niemand die dat namens de organisatie mag geven. Het team kan het voorbereiden, niet
vaststellen.

Weet dat dus vooraf. Zet het team op, en beleg apart wie dat oordeel geeft en hoe die persoon binnen de
termijn bereikbaar is.

## Wie er aan tafel zit

Zes rollen zijn genoeg om te beginnen. Ze staan uitgewerkt in [taakkaarten.md](taakkaarten.md), met per
rol de kerntaken en een checklist voor de startfase, de uitvoering en de afbouw.

| Rol | Waarvoor |
|---|---|
| Voorzitter | Leidt het overleg, neemt of escaleert het sleutelbesluit |
| CIO of directeur bedrijfsvoering | Verbinding met de directie en de bestuurlijke lijn |
| Secretaris of loghouder | Houdt het logboek bij; zonder deze rol valt het team stil |
| CISO of informatiebeveiliger | Duidt de dreiging en de technische impact |
| Manager IT-beheer | Voert containment en herstel uit |
| Communicatieadviseur | Interne en externe boodschap |

De verdeling van verantwoordelijkheden over de hele incidentketen staat in
[rolverdeling-raci.xlsx](rolverdeling-raci.xlsx), van detectie tot nazorg, inclusief de rollen buiten het
team zelf: functionaris gegevensbescherming, juridische zaken, afdelingshoofden, gemeentesecretaris en
bestuur.

**Let op de dubbelfunctie.** Wie in dit team zit, kan niet tegelijk een rol in de bredere
crisisorganisatie vervullen. Loop dat vooraf na, niet tijdens.

## Het logboek is het halve werk

Eén persoon houdt bij wat er gebeurt, met exacte tijdstippen. Dat klinkt als administratie en het is het
verschil tussen een evaluatie die klopt en een reconstructie achteraf uit herinneringen. Het logboek is
ook je bewijs richting toezichthouder, verzekeraar en, als het misgaat, de rechter.

De opzet staat in [logboekformat.md](logboekformat.md). Het lege invulblad is
[logboek-invulblad.xlsx](logboek-invulblad.xlsx), met vijf tabbladen: instructie, het doorlopende
logboek, de meldketen met de wettelijke termijnen, de sleutelbesluiten en de opkomstregistratie.

Twee regels die in de praktijk het meeste schelen: overschrijf nooit een eerdere regel maar voeg een
correctie toe als nieuwe regel, en nummer je sleutelbesluiten door zodat je er vanuit het logboek naar
kunt verwijzen.

## Vier besluiten die je vooraf wilt hebben doordacht

Er zijn vier ingrepen die zo zwaar zijn dat je ze niet wilt improviseren: VPN loskoppelen, infrastructuur
isoleren, een forensische partij inschakelen, en de internetverbinding er helemaal uit gooien.

Voor elk daarvan staat een invulformat klaar in
[sleutelbesluiten-format.md](sleutelbesluiten-format.md): wie besloot, waarom, welke impact op de
dienstverlening, hoeveel medewerkers en inwoners geraakt, wie vooraf geconsulteerd, wie erna
geïnformeerd, en welke herstelacties eraan hangen.

Het punt van dat format is niet de vastlegging maar de **impactvraag**. Dezelfde ingreep is op een
dinsdagochtend iets heel anders dan tijdens een uitkeringsrun, een paspoortpiek of een verkiezing. Het
format dwingt je dat moment expliciet te benoemen voordat je besluit.

## Vooruitkijken, maar niet te vroeg

Scenariodenken werkt averechts als het team nog in de hectiek zit. In
[scenariodenken-bob.md](scenariodenken-bob.md) staat een besliskader met twee assen, herkenbaarheid van
de situatie en de noodzaak tot handelen, dat zegt wanneer je wel en niet vooruit moet denken. Bij hoge
herkenbaarheid en hoge handelingsdruk: gewoon besluiten. Pas als het beeld stabiliseert heeft
scenariodenken zin.

Het kader is afgeleid van het NIPV-rapport *Scenario denken in crisisbeheersing* (2025).

## Na afloop

Plan de evaluatie voordat je hem nodig hebt. [evaluatiesessie-sjabloon.pptx](evaluatiesessie-sjabloon.pptx)
is een sessie van maximaal zestig minuten in vijf stappen: uitgangspunten, de gebeurtenis beschrijven,
wat ging goed en wat kan beter per fase (preventie, detectie, respons, herstel, communicatie), en
maximaal vijf verbeteracties met eigenaar en datum. Dat laatste is de enige stap die telt.

Werkt ook na een oefening, en dat is meteen de goedkoopste manier om het team te laten wennen aan de
werkwijze zonder dat er iets echt misgaat.

## Wat er in deze map staat

- [logboekformat.md](logboekformat.md) — de opzet van het logboek en de procedure voor sleutelbesluiten
- [sleutelbesluiten-format.md](sleutelbesluiten-format.md) — invulformats voor de vier zware ingrepen
- [taakkaarten.md](taakkaarten.md) — generieke taakkaart plus zes rolspecifieke kaarten
- [scenariodenken-bob.md](scenariodenken-bob.md) — wanneer wel en niet vooruitdenken
- [logboek-invulblad.xlsx](logboek-invulblad.xlsx) — leeg logboek met vijf tabbladen
- [rolverdeling-raci.xlsx](rolverdeling-raci.xlsx) — verantwoordelijkheden over de hele incidentketen
- [evaluatiesessie-sjabloon.pptx](evaluatiesessie-sjabloon.pptx) — evaluatiesessie in vijf stappen

## Bewijs

Wat je aan het eind kunt laten zien, aan je directie, je accountant of je toezichthouder:

- Een **aanwijsbaar team** met zes ingevulde rollen en een plaatsvervanger per rol.
- Een **gevuld logboek** van een oefening of een echt incident, met tijdstippen en genummerde besluiten.
- Minstens één **vastgelegd sleutelbesluit** in het format, inclusief de impactinschatting en wie er
  vooraf is geconsulteerd.
- Een **evaluatieverslag** met verbeteracties die een eigenaar en een datum hebben.
- Een **nagelopen dubbelfunctielijst**: niemand zit tegelijk in dit team en in de bredere
  crisisorganisatie.

Wat je hiermee **niet** aantoont: dat je meldplicht is geborgd. Daarvoor moet je apart beleggen wie het
begrotingsoordeel geeft en wie meldt als de eerste persoon niet bereikbaar is.

## Zo leg je het uit

Tegen een directie die vraagt waarom dit nodig is, terwijl er al een crisisorganisatie is:

> "De crisisorganisatie is gebouwd voor een brand of een overstroming. Die komt bij elkaar als er iets
> zichtbaars gebeurt in de stad. Een digitale calamiteit ziet er anders uit: er brandt niets, maar onze
> dienstverlening ligt eruit en de wettelijke meldtermijn loopt al. We hebben een team nodig dat begint
> zonder dat er eerst opgeschaald hoeft te worden."

Tegen iemand die het te zwaar vindt voor de eigen organisatie:

> "Het kost geen formatie en geen structuurwijziging. Het zijn zes mensen die dit werk feitelijk al doen,
> met een rolverdeling op papier en een logboek. De investering is een oefening van een dagdeel."

De kortste versie, en die werkt het best: **je hebt dit team één keer nodig, en dan wil je niet die dag
pas uitzoeken wie mag besluiten om het internet eruit te trekken.**
