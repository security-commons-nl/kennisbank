---
titel: Uitwijk regelen voor kritieke diensten
vakgebied: bcm
type: handleiding
normen: [BIO2, Cbw, NIS2, ISO 22301]
peildatum: 2026-10-15
herkomst: opgesteld door de CISO van een gemeente voor een interbestuurlijke werkgroep bedrijfscontinuïteit
status: concept
route: geen
samenvatting: Hoe je per kritieke dienst kiest wat er gebeurt als de normale voorziening wegvalt, met de
  nadruk op clouddiensten, data en leveranciers. Vijf stappen van de hersteleis uit de BIA naar een geteste
  uitwijkkeuze, met de uitwijkkaart als invulformat: een rij per dienst die laat zien of de gekozen vorm de
  hersteltijd haalt, wat contractueel geregeld is en wanneer er voor het laatst echt is uitgeweken.
barrieres: [restore, dependencies]
rol: verdieping
bronnen: [ibd-model-continuiteitsstrategie, ibd-handreiking-bedrijfscontinuiteitsbeheer, ibd-scenariokaart-3-uitval-ict, ibd-aandachtspunten-back-up-en-recovery-inclusief-saas-leveranciers, ibd-praktische-aanpak-3-2-1-back-up-regel, cip-clouddiensten, bzk-herziening-rijksbreed-cloudbeleid-2026, ciorijk-implementatiekader-risicoafweging-cloudgebruik, bzk-abdtopconsult-van-kwetsbaar-naar-weerbaar, ncsc-herstel-van-een-cyberincident]
---

# Uitwijk regelen voor kritieke diensten

> **Lees deze handleiding online:** [security-commons-nl.github.io/kennisbank/bcm/uitwijk-regelen](https://security-commons-nl.github.io/kennisbank/bcm/uitwijk-regelen/)

> **Barrieres:** test herstel tegen de afgesproken RTO en RPO, en breng kritieke systemen en leveranciers
> in samenhang in beeld. Deze handleiding legt de schakel ertussen: welke uitwijk je per dienst kiest, en
> hoe je laat zien dat die werkt.

Uitwijk is het vooraf geregelde alternatief waarmee een kritieke dienst doorloopt, of binnen de afgesproken
hersteltijd terugkomt, als de normale voorziening wegvalt. Het is een van de keuzes in een
continuïteitsstrategie, naast redundantie, een alternatieve (vaak analoge) werkwijze en bewust uitstel.

De bouwstenen liggen er al, verspreid. De IBD beschrijft uitwijk als strategiekeuze en als scenariokaart
voor het crisisteam. Het Rijk eist sinds 2026 per materiële clouddienst een exitplan met een scenario voor
onverwachte uitval. De internationale standaarden leveren de begrippen. Wat meestal ontbreekt is het stuk
ertussen: een route die een organisatie van haar kritieke diensten naar een geteste uitwijkkeuze brengt, en
een plek waar die keuze per dienst staat. Dat is deze handleiding, met de [uitwijkkaart](uitwijkkaart.md) als
invulformat.

## Wanneer wel, wanneer niet

Gebruik deze handleiding als je een lijst kritieke diensten hebt met per dienst een hersteltijd. Heb je die
nog niet, begin dan bij [kritieke processen en herstelprioriteiten vaststellen](../kritieke-processen-vaststellen/)
en het [BIA- en risicoanalysesjabloon](../bia-en-risicoanalyse-sjabloon/). Zonder hersteleis valt er niets te
kiezen: elke uitwijkvorm is dan goed of te duur, en je weet niet welke.

De kern gaat over drie lagen: ICT-platform en data, clouddienst en leverancier, en de mensen die het herstel
doen. Gebouw, stroom en werkplekken staan in het [bedrijfscontinuïteitsplan](../bedrijfscontinuiteitsplan-sjabloon/);
hier komen ze alleen langs voor zover een ICT-uitwijk ervan afhangt.

## Vier lagen, vier uitwijkvragen

| Laag | Wat valt uit | Uitwijkvormen |
|---|---|---|
| Werkplek en locatie | Gebouw, stroom, netwerk, telefonie | Tweede locatie, buurorganisatie, thuiswerken, noodstroom, noodcommunicatie |
| ICT-platform en data | Eigen datacenter, hostingpartij, servers, opslag | Tweede datacenter (gespiegeld of warm), herstel uit back-up op een schone omgeving, onderlinge uitwijk met een andere overheidsorganisatie |
| Clouddienst en leverancier | SaaS of PaaS valt uit, leverancier failliet of gestopt, toegang geblokkeerd | Back-up buiten de clouddienst, tweede leverancier of eigen landingsplaats, escrow, step-in-rechten, geplande en acute exit |
| Mensen en proces | Beheerders, sleutelkennis, ketenpartner | Minimale noodorganisatie, handmatige terugvalprocedure, afspraken met ketenpartners |

De cloudlaag verschilt op twee punten van de andere drie. Er is geen eigen hardware om naar uit te wijken,
dus je enige ruimte is wat je vooraf buiten de dienst zet (data, configuratie, documentatie, kennis) en wat
je contractueel afdwingt. En het scenario is niet alleen een storing maar ook stoppen: faillissement,
opzegging, een geopolitieke blokkade. Een uitwijkkeuze voor een clouddienst moet beide dekken.

## Zo richt je het in

### Stap 1. Weten wat er moet doorlopen

Neem per kritieke dienst de rij uit je BIA over: eigenaar, maximaal toelaatbare uitvalduur (MTPD),
hersteltijd (RTO), toelaatbaar dataverlies (RPO) en het noodniveau, dus wat minimaal door moet. Vraag die
gegevens niet opnieuw uit; de uitwijkkaart pakt ze over.

Leg daarbij vast wat de kleinste organisatie is die de dienst op noodniveau draait: welke mensen, welke
systemen, welke werkplekken. Dat is de maat voor de uitwijk. Wie de volledige dienst wil uitwijken, betaalt
voor capaciteit die op de dag zelf niemand nodig heeft.

### Stap 2. Weten waar het van afhangt

Zet per dienst de bouwstenen en leveranciers op een rij. [Ketenafhankelijkheden in beeld](../../security/ketenafhankelijkheden/)
is daar de handleiding voor. Voor uitwijk tellen twee vragen extra:

1. **Wat van de dienst staat buiten de dienst?** De data, de configuratie, de documentatie om opnieuw op te
   bouwen, de kennis van wie het kan. Bij een SaaS-dienst is dit vaak niets, en dat is de bevinding.
2. **Waar zit concentratie?** Vijf diensten bij dezelfde leverancier, of op hetzelfde platform, vallen
   samen uit. Uitwijk per dienst helpt dan niet als de uitwijk van alle vijf ook daar zit.

### Stap 3. De uitwijkkeuze maken

Uitwijk is een schaal van kosten tegen hersteltijd. Voor een eigen platform is de klassieke indeling uit
[NIST SP 800-34](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf) nog steeds
de helderste:

| Vorm | Wat er klaarstaat | Hersteltijd |
|---|---|---|
| Cold site | Ruimte, stroom, koeling; geen apparatuur | Weken |
| Warm site | Apparatuur, geen actuele data | Dagen |
| Hot site | Apparatuur en actuele data | Uren |
| Mirrored site | Gespiegelde omgeving die meedraait | Vrijwel geen |
| Mobile site | Verplaatsbare voorziening op afroep | Afhankelijk van levering |

Daarnaast zijn er vormen die in de publieke sector vaak goedkoper uitkomen:

- **Herstel uit back-up op een schone omgeving.** Werkt alleen als de back-up buiten het bereik van de
  aanvaller staat; zie [onveranderbare back-ups](../../security/onveranderbare-backups/).
- **Onderlinge uitwijk.** Twee overheden zijn elkaars uitwijk. Een bekend Nederlands voorbeeld zijn twee
  Gelderse gemeenten die dat in 2008 deden over een bestaande glasvezelverbinding, betaald uit bestaande
  vervangings- en uitwijkbudgetten (Computable, juli 2008). Randvoorwaarden: een verbinding, gelijke
  platformkeuzes en een gezamenlijke beheerafspraak.
- **Tweede leverancier of eigen landingsplaats** voor een clouddienst, met de data er al in of in een
  formaat dat je daar binnen de RTO kunt inlezen.
- **Analoge terugval.** Papier, telefoon, handmatig. Goedkoop, en houdt het vaak een paar dagen vol.
- **Bewust uitstel.** Voor een dienst die een week kan wachten is dat de juiste keuze, mits je het
  opschrijft.

De keuzeregel is eenvoudig: **de goedkoopste vorm die de RTO en het noodniveau haalt.** Haalt geen enkele
betaalbare vorm de RTO, dan klopt de RTO niet of het budget niet. Dat is een besluit voor de eigenaar van de
dienst, niet voor ICT.

### Stap 4. Vastleggen en afdwingen

Voor een clouddienst of uitbestede dienst zit de helft van de uitwijk in het contract. Het rijksbrede
cloudbeleid van 2026 vraagt bij materieel cloudgebruik een exitplan met twee scenario's, en die indeling werkt
voor elke publieke organisatie:

1. **Geplande exit.** Hoe je naar een andere leverancier of eigen beheer gaat zonder verstoring: hoe data,
   metadata en applicaties worden overgedragen, met de minimale termijn die dat kost.
2. **Disruptieve onderbreking.** Wat je doet als de dienst onverwacht wegvalt, welke maatregelen je daarvoor
   vooraf hebt genomen (zoals een back-up buiten de clouddienst) en hoe je de meest kritieke processen
   herstelt.

Wat in het contract hoort: beide scenario's, data- en serviceportabiliteit, step-in-rechten, escrow waar het
zin heeft, inzicht in de onderaannemers, en een opzeggingsrecht bij dreigend faillissement. En in de eigen
begroting: geld voor een acute exit. Het implementatiekader cloudgebruik van CIO Rijk noemt budget twee keer
als onderdeel van een exitstrategie, en dat is geen toeval: een exit die niet begroot is, gebeurt niet.

Leg ook vast wie de uitwijk activeert en wie dat besluit neemt. Dat staat in het
[bedrijfscontinuïteitsplan](../bedrijfscontinuiteitsplan-sjabloon/), hoofdstuk 3.

### Stap 5. Testen en bijhouden

Een uitwijk die nooit is uitgevoerd, is een aanname. Drie dingen:

1. **Echt uitwijken, niet alleen een tafeloefening.** Een volwassen vorm is periodiek wisselen tussen de
   primaire en de uitwijkomgeving, zodat de uitwijk de gewone gang van zaken wordt.
2. **De isolatietoets op back-ups.** Staat de back-up buiten bereik van wie de primaire omgeving
   overneemt? Het Britse NCSC heeft daar
   [principes voor ransomware-bestendige back-ups](https://www.ncsc.gov.uk/collection/ransomware-resistant-backups)
   voor, een set voor eigen opslag en een voor cloud, bruikbaar als toetslijst richting leveranciers.
3. **Jaarlijks herzien.** De BIO2 vraagt jaarlijks testen van continuïteitsplannen en herstelprocedures.
   Neem het exitplan per clouddienst in dezelfde ronde mee.

De uitvoering van de test zelf staat in [hersteltest tegen RTO en RPO](../../security/hersteltest/).

## Wat het kost en wat het oplevert

De analyse kost per dienst een tot twee uur met de eigenaar en een beheerder, als de BIA er al ligt. De
uitwijk zelf kost wat de keuze kost, en dat is precies het punt: per dienst wordt zichtbaar wat een uur
kortere hersteltijd kost, en de eigenaar beslist.

Wat het oplevert: een overzicht dat in een oogopslag laat zien welke kritieke diensten hun hersteltijd niet
halen, welke clouddienst geen exitplan heeft en welke uitwijk nooit is getest. Dat overzichtsblad is wat naar
de directie gaat.

Waar je op moet letten:

- Een uitwijk die op dezelfde leverancier of hetzelfde platform leunt als de dienst zelf, wijkt nergens heen.
- Exitplannen gaan vaak uit van voldoende tijd. Toets of het plan ook werkt als de leverancier morgen stopt.
- De uitwijkkaart veroudert bij elke contractwijziging. Koppel de herziening aan het contractbeheer.

## Bewijs

Wat je aan het eind kunt laten zien, aan je directie, je accountant of je toezichthouder:

- De **uitwijkkaart** per kritieke dienst, met de gekozen vorm en of die de RTO haalt.
- Per clouddienst of uitbestede dienst een **exitplan met beide scenario's**, en de contractbepalingen die
  het afdwingen.
- Het **verslag van de laatste uitwijktest**: welke dienst, welke datum, welke soort test (tafeloefening,
  deeltest, echte uitwijk), de gemeten hersteltijd en de restpunten.
- Het **overzichtsblad** over alle diensten, met de datum waarop de directie het zag.

Wat je hiermee niet aantoont: dat de back-up zelf onaantastbaar is. Dat bewijs hoort bij
[onveranderbare back-ups](../../security/onveranderbare-backups/).

## Zo leg je het uit

**Aan de directie.** "Voor elke kritieke dienst hebben we nu op een rij wat er gebeurt als de leverancier of
het platform wegvalt, en of dat snel genoeg gaat. Bij drie diensten haalt de uitwijk de hersteltijd niet. U
kunt kiezen: meer uitgeven aan uitwijk, of de hersteltijd verruimen. Niet kiezen is ook een keuze, alleen
merkt u die pas tijdens de storing."

**Aan de informatiemanager.** "Elke clouddienst krijgt een exitplan met twee scenario's, en de
contractbepalingen die daarbij horen. Bij nieuwe aanbestedingen nemen we die op in het programma van eisen;
bij bestaande contracten bij de eerstvolgende verlenging."

**Aan het MT.** "Per dienst een uur of twee met de eigenaar, daarna een test per jaar. Het levert een lijst op
van wat we zouden doen als het misgaat, en welke gaten we vooraf kennen."

## Hoe dit samenhangt

Deze handleiding hoort bij de barrieres `restore` en `dependencies` uit de
[zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/), als verdieping naast
[hersteltest tegen RTO en RPO](../../security/hersteltest/) en
[ketenafhankelijkheden in beeld](../../security/ketenafhankelijkheden/). Wat dit aantoont in de BIO2 staat op
[van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

De hersteleisen komen uit het [BIA- en risicoanalysesjabloon](../bia-en-risicoanalyse-sjabloon/), het besluit
om uit te wijken staat in het [bedrijfscontinuïteitsplan](../bedrijfscontinuiteitsplan-sjabloon/), en het
beleid erboven in [beleid ICT-continuïteit en uitwijk](../../governance/beleidsset-informatiebeveiliging/bcm.html)
uit de beleidsset.

Normatief kader, voor wie het wil nalopen:

- **BIO2**, maatregelen 5.30 (ICT-gereedheid voor bedrijfscontinuïteit) en 8.13 (back-up): continuïteitsplannen
  en herstelprocedures minimaal jaarlijks testen, back-up op een locatie die niet door hetzelfde incident
  wordt geraakt.
- **Cbw en NIS2** artikel 21: bedrijfscontinuïteit, back-upbeheer en crisisbeheer horen bij de zorgplicht.
- **Rijksbreed cloudbeleid 2026**, paragraaf 3.2: exitplan met twee scenario's bij materieel cloudgebruik.
- **ISO 22301** hoofdstuk 8.3 (strategieën en oplossingen) en
  [ISO/IEC 27031](https://www.iso.org/standard/80975.html) (ICT-gereedheid voor bedrijfscontinuïteit), voor
  de begrippen.

## Wat er in deze map staat

- [uitwijkkaart.md](uitwijkkaart.md): het invulformat, een kaart per kritieke dienst plus het overzichtsblad,
  met twee ingevulde voorbeelden (verzonnen)

## Licentie

[EUPL-1.2](../../LICENSE).
