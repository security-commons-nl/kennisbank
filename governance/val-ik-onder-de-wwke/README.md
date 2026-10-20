---
titel: Valt een gemeente onder de Wwke?
vakgebied: governance
type: referentie
normen: [Wwke, CER, Cbw]
peildatum: 2026-10-20
herkomst: analyse van de CISO-organisatie van een regionale samenwerking van gemeenten op de wettekst (Stb. 2026, 188), juli 2026, voor de commons bijgewerkt op de inwerkingtreding
status: concept
samenvatting: De Wet weerbaarheid kritieke entiteiten (Wwke, de Nederlandse uitwerking van de CER-richtlijn) geldt sinds 15 augustus 2026. Een gemeente staat niet in de bijlage, want de sector overheid noemt alleen de centrale overheid, en zonder aanwijzing door een minister gelden er geen verplichtingen. Twee routes verdienen wel een expliciete toets (wegbeheer en afvalwater), en één spoor verdient monitoring: een minister kan een extra sector aanwijzen. Met de knip naar de Cyberbeveiligingswet.
---

# Valt een gemeente onder de Wwke?

> **Lees de analyse online:** [security-commons-nl.github.io/kennisbank/governance/val-ik-onder-de-wwke](https://security-commons-nl.github.io/kennisbank/governance/val-ik-onder-de-wwke/)

De Wet weerbaarheid kritieke entiteiten (Wwke, Stb. 2026, 188, kamerstuk 36 765) zet de Europese CER-richtlijn
(EU) 2022/2557 om. Waar de Cyberbeveiligingswet over digitale weerbaarheid gaat, gaat de Wwke over de fysieke
en organisatorische weerbaarheid van kritieke entiteiten. De wet en het Besluit weerbaarheid kritieke
entiteiten traden in werking op **15 augustus 2026** (Stb. 2026, 190, artikel 19), zonder fasering per artikel.

De vraag die bij gemeenten opkomt: komt hier extra werk op ons af? Het korte antwoord is nee, en het lange
antwoord zegt waar je toch moet kijken.

## 1. De kern: niet in de bijlage, dus geen aanwijzing

De Wwke werkt via **aanwijzing door een minister**, en aangewezen kan alleen wie in een sector uit de bijlage
valt (artikel 6, eerste lid). Bij de sector overheid staat precies één categorie: "overheidsinstanties die
behoren tot de **centrale overheid**". Een gemeente is decentrale overheid. De richtlijn liet lidstaten vrij om
lokaal bestuur mee te nemen; Nederland heeft dat niet gedaan.

De brede definitie van overheidsinstantie in artikel 1 verandert daar niets aan: die definieert het begrip,
de bijlage bepaalt de reikwijdte.

Gevolg: geen aanwijzing, dus geen zorgplicht, geen risicobeoordeling, geen meldplicht en geen
verbindingsfunctionaris. Er is geen gap om te assessen.

## 2. Twee routes die je toch expliciet toetst

"Gemeenten vallen er niet onder" is iets te kort door de bocht. Er zijn twee categorieën waar een gemeente op
het eerste gezicht wél in past. Beide keren komt de gemeente er langs dezelfde deur uit: een uitzondering voor
wie de activiteit als bijzaak doet. Dat is een oordeel, geen automatisme, en dat oordeel leg je vast.

**Vervoer, wegen.** Wegenautoriteiten die verantwoordelijk zijn voor verkeersbeheer, *met uitzondering van
overheidsinstanties voor wie verkeersbeheer of de exploitatie van intelligente vervoerssystemen een
niet-essentieel onderdeel van hun algemene activiteiten is*. Een gemeente is wegenautoriteit met
verkeersbeheer (verkeerslichten, ITS, beweegbare bruggen), maar verkeersbeheer is een fractie van wat zij doet.
De uitzondering vangt haar vrijwel zeker op.

**Afvalwater.** Ondernemingen die stedelijk afvalwater opvangen, lozen of behandelen, *met uitzondering van
ondernemingen waarvoor dat een niet-essentieel onderdeel van hun algemene activiteit is*. Een gemeente heeft de
rioleringszorgplicht, maar twee uitgangen wijzen dezelfde kant op: een gemeente is geen onderneming, en
riolering is een niet-essentieel onderdeel van haar activiteit.

**Wat niet speelt.** Openbaar vervoer (de categorie noemt exploitanten), gezondheidszorg (zorgaanbieders in de
zin van de Wkkgz; een gemeente contracteert Wmo-zorg maar is zelf geen zorgaanbieder), drinkwater (de
drinkwaterbedrijven).

## 3. Aanwijzing is een besluit, geen zelfevaluatie

Aanwijzing gebeurt bij regeling of besluit van de betrokken minister (artikel 6), op basis van criteria als het
aantal afhankelijke gebruikers, afhankelijkheid van andere sectoren, ernst en duur van gevolgen en beschikbare
alternatieven. Voor de sector overheid is **BZK** de bevoegde autoriteit (artikel 8).

Je bepaalt dus niet zelf of je eronder valt. Word je aangewezen, dan krijg je een besluit met de verplichtingen
en de ingangsdatum. Er valt niets te missen door niets te doen. En er is geen haast:

| Verplichting na aanwijzing | Ingang |
|---|---|
| Eigen risicobeoordeling (artikel 14) | binnen 9 maanden |
| Zorgplicht (artikel 15) | vanaf 10 maanden |
| Meldplicht (artikel 17) | vanaf 10 maanden |

## 4. De knip met de Cyberbeveiligingswet

Artikel 4: "Deze wet is niet van toepassing op aangelegenheden waarop de Cyberbeveiligingswet van toepassing
is." De regimes kunnen samenvallen op de **entiteit** (je kunt kritieke entiteit én essentiële entiteit zijn),
maar niet op dezelfde **aangelegenheid**: de Wwke gaat over het fysieke en organisatorische, de Cbw over het
digitale. De coördinatie tussen beide toezichthouders is in de wet geregeld (artikel 13 en 27), niet aan de
entiteit overgelaten.

## 5. Het spoor om te volgen: artikel 7

Een minister kan bij regeling een extra sector of categorie aanwijzen waarvoor hij beleidsverantwoordelijk is
(artikel 7, eerste lid). Dat is de enige route waarlangs gemeenten alsnog in beeld komen: als BZK ooit
"decentrale overheid" als categorie aanwijst. Iets om te volgen, niet om nu op te assessen. Beleg bij iemand
dat hij dit spoor in de gaten houdt.

## 6. Wat wel relevant is voor een gemeente

- **Verbonden partijen.** Een gemeente zit in gemeenschappelijke regelingen en aandeelhoudersrelaties met
  partijen die wél kritieke entiteit kunnen worden: de GGD, het drinkwaterbedrijf, het waterschap, de
  netbeheerder. Dat is een vraag over ketenafhankelijkheid, geen eigen verplichting. Zie
  [Ketenafhankelijkheden in beeld](../../security/ketenafhankelijkheden/).
- **Veiligheidsregio's zijn uitgezonderd** (artikel 5, onderdeel e), net als defensie, de inlichtingendiensten,
  het OM en de politie. Een veiligheidsregio wordt dus nooit kritieke entiteit; oefen wel mét de kritieke
  entiteiten in de regio.
- **Weren van leveranciers (artikel 15a).** Een minister kan een kritieke entiteit verplichten producten van een
  leverancier met banden met een vijandige statelijke actor niet te gebruiken. Niet voor de gemeente zelf, wel
  iets dat via leveranciers langs kan komen.
- **Gezamenlijk uitvoeren (artikel 14, vijfde lid, en 15, vierde lid).** Risicobeoordeling en maatregelen mogen
  gezamenlijk binnen een gemeenschappelijke regeling of andere vastgelegde samenwerking, mits per entiteit
  zichtbaar blijft wat voor haar geldt.
- **Boetes (artikel 40)** zijn entiteitsboetes; de Wwke kent geen persoonlijke bestuurdersaansprakelijkheid
  zoals de Cbw.

## 7. Let op bij samenvattingen

Er circuleren samenvattingen van de Wwke die door AI zijn gemaakt en aantoonbaar onnauwkeurig zijn: een
verkeerd aantal sectoren (de bijlage kent er elf), of de RDI als toezichthouder voor de sector overheid
(artikel 8 wijst per sector een minister aan). Ga bij twijfel naar de wettekst.

## Bronnen

- Wet weerbaarheid kritieke entiteiten, Stb. 2026, 188: [zoek.officielebekendmakingen.nl/stb-2026-188.html](https://zoek.officielebekendmakingen.nl/stb-2026-188.html)
- Besluit weerbaarheid kritieke entiteiten en inwerkingtreding, Stb. 2026, 190: [zoek.officielebekendmakingen.nl/stb-2026-190.html](https://zoek.officielebekendmakingen.nl/stb-2026-190.html)
- Richtlijn (EU) 2022/2557 (CER): [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:32022L2557)
- Wetsvoorstel 36 765 bij de Eerste Kamer: [eerstekamer.nl](https://www.eerstekamer.nl/wetsvoorstel/36765_wet_weerbaarheid_kritieke)
