---
domein: back-up
titel: Beleid back-up en recovery
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor het maken, bewaren, beschermen en
terugzetten van back-ups. Het geldt voor alle informatie waarvan de organisatie eigenaar is, waar die ook
staat: in een eigen omgeving, bij een hostingpartij of in een SaaS-dienst. Het gaat om gegevens en om wat
nodig is om systemen te herstellen: configuraties, instellingen van netwerk en applicaties, en de inrichting
van clouddiensten. Het gaat over ISO-beheersmaatregel 8.13.

Een back-up is geen archief. De bewaarplicht van overheidsinformatie valt onder het archiefbeleid. Uitwijk en
de keuze welke systemen kritiek zijn, staan in het continuïteitsbeleid.

## 2. Uitgangspunten

1. De organisatie is eigenaar van haar gegevens, ook als een leverancier ze verwerkt. Ze zorgt dat er een
   back-up is die bij het belang van het proces past, of ze die nu zelf maakt of laat maken.
2. Ransomware is het scenario waarop de back-up wordt ingericht: een aanvaller met beheerrechten mag de back-up
   niet kunnen wissen of versleutelen.
3. Een back-up waarvan het terugzetten niet getest is, geldt niet als back-up.

## 3. Beleidsregels

### 3.1 Back-upbeleid en scenario's

- Dit beleid en de back-upplannen per omgeving leggen samen vast wat wordt bewaard, hoe lang, waar en hoe het
  beschermd is. De back-upplannen volgen dit beleid en worden opgesteld door
  [[eigenaar back-upplannen: de functie die de back-upplannen opstelt, bijvoorbeeld de informatiemanager]].
  [8.13.01]
- De back-up is ten minste ingericht op deze scenario's: een aanval met ransomware of wiperware op de eigen
  omgeving, een grote verstoring van een datacenter, gegevensverlies in een SaaS-dienst en het per ongeluk of
  bewust verwijderen van veel gegevens door een gebruiker. [8.13.01]

### 3.2 Hersteleisen

- Per systeem of gegevensverzameling stelt de proceseigenaar het maximale gegevensverlies (RPO) en de
  maximale hersteltijd (RTO) vast, met een expliciete risicoafweging. Hij legt ook het detailniveau van herstel
  vast (bijvoorbeeld één bericht, een mailbox of een hele omgeving) en de bewaartermijn van de back-ups.
  [8.13.02]
- Zolang er voor een systeem geen afweging is, geldt een standaardregime: ten hoogste 24 uur gegevensverlies
  en een hersteltijd van ten hoogste
  [[standaard hersteltijd: bijvoorbeeld 16 werkuren]].
  [8.13.02]
- De hersteltijd van een kritiek systeem is korter dan de maximale uitvalsduur van het proces, want na het
  terugzetten volgen nog controle, koppelingen en communicatie. [8.13.02]

::: als bcm=bcm
- De hersteleisen voor kritieke systemen komen uit de BIA en het overzicht van kritieke systemen uit het
  continuïteitsbeleid. Wijkt een back-upplan daarvan af, dan beslist de proceseigenaar. [8.13.02]
:::

::: als bcm=geen,crisisteam
- Er is geen BIA. De proceseigenaar stelt de hersteleisen vast met de CISO en de systeemeigenaar, op basis van
  de classificatie van de gegevens en het overzicht van kritieke systemen. [8.13.02]
:::

### 3.3 Bescherming van de back-up

- Ten minste één kopie van de back-up kan niet worden gewijzigd of gewist binnen de bewaartermijn (immutable of
  offline), ook niet met de beheerrechten van de productieomgeving. [8.13.01]
- Back-ups zijn versleuteld. De sleutels staan gescheiden van de back-up, in een beheerde sleutelkluis, en zijn
  ook beschikbaar als de productieomgeving niet werkt. [8.13.01]
- Beheer van de back-upomgeving gaat met aparte, persoonsgebonden accounts met meerfactorauthenticatie, die
  niet in het gewone domein of de gewone tenant zitten. Verwijderen of verkorten van bewaartermijnen vraagt
  goedkeuring van een tweede persoon. [8.13.01]
- Elke back-uptaak wordt gecontroleerd op succes. Een mislukte taak wordt dezelfde of de volgende werkdag
  hersteld of gemeld. [8.13.01]
- Bewaartermijnen passen bij het doel en bij de wet. Gegevens die volgens de archief- of privacyregels
  vernietigd moeten zijn, verdwijnen uit de back-up aan het eind van de bewaartermijn. [8.13.01]

### 3.4 Gescheiden opslag

- Back-ups van kritieke systemen staan op ten minste twee plekken, waarvan één zo gescheiden van de
  productieomgeving dat een incident op de ene plek (brand, stroomuitval, een aanval op het netwerk of de
  beheeromgeving) de andere niet raakt. Een vuistregel is 3-2-1: drie kopieën, op twee soorten opslag, één
  daarvan op een andere locatie. [8.13.03]

::: als hosting=eigen-dc
- Bij een eigen datacenter staat de gescheiden kopie op een andere fysieke locatie of bij een externe
  opslagdienst, met een eigen beheeromgeving. Media die worden vervoerd, zijn versleuteld en er is een logboek
  van waar ze zijn. [8.13.03]
:::

::: als hosting=hostingpartij
- Bij een hostingpartij is een gespiegeld tweede datacenter niet genoeg: dat deelt meestal de kwetsbaarheden
  van het eerste. Het contract regelt daarnaast een kopie bij een andere partij of in een gescheiden omgeving,
  waar de organisatie zelf bij kan. [8.13.03]
:::

::: als hosting=saas
- Voor elke SaaS-dienst die een kritiek proces ondersteunt, weet de organisatie hoe de leverancier back-ups
  maakt, waar ze staan en hoe lang ze bewaard worden. Biedt de leverancier geen gescheiden kopie, of kan de
  organisatie er niet zelf bij, dan exporteert de organisatie de gegevens periodiek naar eigen opslag of neemt
  ze een back-updienst van een andere partij af. [8.13.03]
:::

::: als werkplek=cloud,hybride
- De cloudwerkplek (mail, bestanden, samenwerkruimtes) heeft een eigen back-up buiten de tenant. De
  ingebouwde prullenbak en versiebeheer van de aanbieder gelden niet als back-up. De back-up omvat ook de
  inrichting die nodig is voor herstel, zoals groepen, rechten en beleidsinstellingen, voor zover de aanbieder
  dat mogelijk maakt. [8.13.03]
:::

### 3.5 Herstel en testen

- Herstel uit een back-up gebeurt na toestemming van de systeemeigenaar. Bij een groot incident of ransomware
  beslist de proceseigenaar over de opties, op advies van ICT en de CISO. Elke hersteloperatie wordt gelogd.
  [8.13.04]
- De herstelprocedure wordt elk jaar getest en na elke grote wijziging, zoals een migratie of een nieuwe
  back-upvoorziening. De test zet echte gegevens terug, controleert of ze volledig en bruikbaar zijn en meet de
  benodigde tijd tegen de hersteltijd. [8.13.04]
- Ten minste één test per jaar gaat uit van het ransomwarescenario: herstel uit de onveranderbare kopie, in een
  schone omgeving. [8.13.04]

::: als beheer=eigen
- De eigen beheerorganisatie voert de tests uit en legt ze vast in een testverslag met tijden en bevindingen.
  [8.13.04]
:::

::: als beheer=regie,uitbesteed
- Back-up en herstel liggen bij de beheerpartij. Het contract verplicht die partij om de tests uit te voeren
  met de organisatie erbij, de verslagen te leveren en ook kopieën te maken en te testen van onderdelen die bij
  andere leveranciers liggen, of dat expliciet uit te sluiten. De regieorganisatie houdt het overzicht welke
  leverancier welk deel van de back-up doet. [8.13.04]
:::

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| Proceseigenaar | Hersteleisen en bewaartermijnen, besluit over herstel bij grote incidenten |
| Systeemeigenaar | Back-upplan van zijn systeem, toestemming voor herstel |
| [[lijneigenaar back-up: de manager die back-up en herstel uitvoert of bij leveranciers regisseert]] | Uitvoering, dagelijkse controle, tests en het back-upregister |
| Functioneel beheer | Back-up en herstel van SaaS-diensten en de cloudwerkplek, samen met de leverancier |
| CISO | Advies, toetsing van dit beleid en van de bescherming tegen ransomware |

## 5. Naleving en bewaking

- Dagelijks: controle op mislukte back-uptaken; bewijs is het logboek met de afhandeling.
- Jaarlijks: overzicht van de hersteltests per kritiek systeem, met gemeten hersteltijd tegen de eis; bewijs
  zijn de testverslagen.
- Jaarlijks: controle dat het back-upregister volledig is: elk kritiek systeem en elke SaaS-dienst met een
  kritiek proces heeft een back-upplan, een gescheiden kopie en een onveranderbare kopie.
- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het hangt samen met het continuïteitsbeleid
(kritieke systemen en uitwijk), het beleid informatiebeveiliging bij inkoop en contractbeheer (afspraken met
leveranciers), het beleid cryptografie (sleutelbeheer), het beleid logische toegang (beheeraccounts) en het
archiefbeleid (bewaartermijnen).
