---
domein: back-up
titel: Beleid back-up en recovery
samenvatting: Over het maken, beschermen en terugzetten van back-ups, met ransomware als leidend scenario. Behandelt back-upplannen en het back-upregister, hersteleisen per systeem, een onveranderbare kopie, gescheiden opslag op meerdere plekken en het jaarlijks testen van herstel.
invoeren:
  - Stel per omgeving een back-upplan op dat per scenario het herstel beschrijft, ook ransomware (hoofdstuk 3).
  - Zet een back-upregister op met per systeem de hersteleisen, locaties en laatste hersteltest (hoofdstuk 3).
  - Laat de proceseigenaar per systeem het maximale gegevensverlies en de hersteltijd vaststellen (hoofdstuk 4).
  - Richt ten minste één onveranderbare of offline kopie van de back-up in (hoofdstuk 5).
  - Versleutel de back-ups en bewaar de sleutels gescheiden in een beheerde sleutelkluis (hoofdstuk 5).
  - Richt voor de back-upomgeving aparte beheeraccounts met MFA buiten het gewone domein in (hoofdstuk 5).
  - Plaats back-ups van kritieke systemen op twee plekken die elkaar bij een incident niet raken (hoofdstuk 6).
  - Voer een eerste hersteltest uit volgens het ransomwarescenario, in een schone omgeving (hoofdstuk 7).
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor het maken, bewaren, beschermen en
terugzetten van back-ups. Het legt vast welke hersteleisen gelden, hoe de back-up beschermd is tegen een
aanvaller met beheerrechten, waar de kopieën staan en hoe het terugzetten wordt getest, zodat de organisatie
na verlies, vernietiging of versleuteling van gegevens haar processen binnen de afgesproken tijd hervat. Het
gaat over ISO-beheersmaatregel 8.13.

**Voor wie.** Het beleid is primair bedoeld voor de beheerorganisatie die de back-up uitvoert of bij
leveranciers regisseert, voor functioneel beheer van clouddiensten en voor de proces- en systeemeigenaren
die de hersteleisen vaststellen. Het geldt ook voor leveranciers die back-up en herstel voor de organisatie
verzorgen.

**Waarop.** Alle informatie waarvan de organisatie eigenaar is, waar die ook staat: in een eigen omgeving,
bij een hostingpartij of in een SaaS-dienst. Het gaat om gegevens en om wat nodig is om systemen te
herstellen: configuraties, instellingen van netwerk en applicaties, en de inrichting van clouddiensten. Is
back-up of herstel uitbesteed, dan gelden de eisen uit dit beleid als minimumeis voor die partij. De
organisatie legt dat vast in het contract en toetst de naleving met een onafhankelijke verklaring, zoals een
ISO 27001-certificaat of een ISAE 3402- of ISAE 3000-rapport; het vastleggen loopt via het beleid
informatiebeveiliging bij inkoop, het toetsen via het beleid contractbeheer.

Buiten dit beleid vallen de archivering van overheidsinformatie (een back-up is geen archief; de bewaarplicht
staat in het archiefbeleid), de uitwijk en de keuze welke systemen kritiek zijn (continuïteitsbeleid), het
sleutelbeheer voor de versleuteling (beleid cryptografie) en de fysieke beveiliging van opslaglocaties (beleid
fysieke toegang en beveiliging).

## 2. Uitgangspunten

1. De organisatie is eigenaar van haar gegevens, ook als een leverancier ze verwerkt. Zij zorgt dat er een
   back-up is die bij het impactniveau van het proces past, of zij die nu zelf maakt of laat maken.
2. Ransomware is het scenario waarop de back-up is ingericht: een aanvaller met beheerrechten op de
   productieomgeving kan de back-up niet wissen of versleutelen.
3. Een back-up waarvan het terugzetten niet is getest, geldt niet als back-up.
4. Hoe hoger het impactniveau van een systeem, hoe korter de hersteltijd en hoe strikter de scheiding van
   de kopieën.
5. Termijnen en frequenties in dit beleid die niet uit een wet of uit de BIO 2.0 komen, zijn standaardwaarden.
   De organisatie past ze aan op haar eigen risicoafweging en legt de keuze vast bij de vaststelling van dit beleid.

## 3. Back-upplannen en scenario's

- Dit beleid en de back-upplannen per omgeving leggen samen vast wat wordt bewaard, hoe vaak, hoe lang, waar
  en hoe het is beschermd. [[eigenaar back-upplannen: de functie die de back-upplannen opstelt, bijvoorbeeld de informatiemanager]]
  stelt de plannen op, de systeemeigenaar keurt ze goed en zij worden jaarlijks en na elke grote wijziging
  herzien. [8.13.01]
- De back-up is ten minste ingericht op deze scenario's: een aanval met ransomware of wiperware op de eigen
  omgeving, een grote verstoring van een datacenter, gegevensverlies in een SaaS-dienst en het per ongeluk of
  bewust verwijderen van veel gegevens door een gebruiker. Het back-upplan beschrijft per scenario hoe het
  herstel verloopt. [8.13.01]
- [[lijneigenaar back-up: de manager die back-up en herstel uitvoert of bij leveranciers regisseert]] houdt
  een back-upregister bij met per systeem en per SaaS-dienst: het back-upplan, de hersteleisen, de locaties
  van de kopieën, de onveranderbare kopie en de datum van de laatste hersteltest. [8.13.01]

## 4. Hersteleisen

- Per systeem of gegevensverzameling stelt de proceseigenaar het maximale gegevensverlies (RPO) en de
  maximale hersteltijd (RTO) vast, met een vastgelegde risicoafweging. De proceseigenaar legt ook het
  detailniveau van herstel vast (bijvoorbeeld één bericht, een mailbox of een hele omgeving) en de
  bewaartermijn van de back-ups. [8.13.02]
- Zolang er voor een systeem geen afweging is, geldt een standaardregime: ten hoogste 24 uur
  gegevensverlies en een hersteltijd van ten hoogste [[standaard hersteltijd: bijvoorbeeld 16 werkuren]].
  De eigenaar van de back-upplannen rapporteert jaarlijks welke systemen nog op het standaardregime
  draaien. [8.13.02]
- De hersteltijd van een systeem met impactniveau kritiek of hoger is korter dan de maximale uitvalsduur
  van het proces, want na het terugzetten volgen nog controle, koppelingen en communicatie. De
  proceseigenaar legt de marge vast in het back-upplan. [8.13.02]

::: als bcm=bcm
- De hersteleisen voor kritieke systemen komen uit de BIA en het overzicht van kritieke systemen uit het
  continuïteitsbeleid. Wijkt een back-upplan daarvan af, dan beslist de proceseigenaar en legt die het
  besluit vast. [8.13.02]
:::

::: als bcm=geen,crisisteam
- Er is geen BIA. De proceseigenaar stelt de hersteleisen vast met de CISO en de systeemeigenaar, op basis
  van het impactniveau van de gegevens en het overzicht van kritieke systemen, en legt ze vast in het
  back-upplan. [8.13.02]
:::

## 5. Bescherming van de back-up

- Ten minste één kopie van de back-up is binnen de bewaartermijn niet te wijzigen of te wissen
  (onveranderbaar of offline), ook niet met de beheerrechten van de productieomgeving. De beheerorganisatie
  toont dat bij elke hersteltest aan. [8.13.01]
- Back-ups zijn versleuteld volgens het beleid cryptografie. De sleutels staan gescheiden van de back-up,
  in een beheerde sleutelkluis, en zijn ook beschikbaar als de productieomgeving niet werkt. [8.13.01]
- Beheer van de back-upomgeving gaat met aparte, persoonsgebonden accounts met MFA, die niet in het gewone
  domein of de gewone tenant zitten. Verwijderen of verkorten van bewaartermijnen vraagt goedkeuring van een
  tweede persoon en wordt gelogd. [8.13.01]
- De beheerorganisatie controleert elke werkdag of alle back-uptaken zijn geslaagd. Een mislukte taak is
  dezelfde of de volgende werkdag hersteld, of gemeld aan de systeemeigenaar met de reden. De controle en
  de afhandeling staan in het logboek. [8.13.01]
- Bewaartermijnen passen bij het doel en bij de wet. Gegevens die volgens de archief- of privacyregels
  vernietigd moeten zijn, verwijdert de beheerorganisatie uit de back-up aan het eind van de bewaartermijn
  en legt dat vast. [8.13.01]

## 6. Gescheiden opslag

- Back-ups van systemen met impactniveau kritiek of hoger staan op ten minste twee plekken, waarvan één zo
  gescheiden van de productieomgeving dat een incident op de ene plek (brand, stroomuitval, een aanval op
  het netwerk of de beheeromgeving) de andere niet raakt. Een vuistregel is 3-2-1: drie kopieën, op twee
  soorten opslag, één daarvan op een andere locatie. Het back-upregister noemt de locaties. [8.13.03]

::: als hosting=eigen-dc
- Bij een eigen datacenter staat de gescheiden kopie op een andere fysieke locatie of bij een externe
  opslagdienst, met een eigen beheeromgeving. Media die worden vervoerd, zijn versleuteld en de
  beheerorganisatie houdt een logboek bij van waar ze zijn. [8.13.03]
:::

::: als hosting=hostingpartij
- Bij een hostingpartij is een gespiegeld tweede datacenter niet genoeg, omdat dat de kwetsbaarheden van het
  eerste deelt. Het contract regelt daarnaast een kopie bij een andere partij of in een gescheiden
  omgeving, waar de organisatie zelf bij kan. De contracteigenaar controleert dat jaarlijks. [8.13.03]
:::

::: als hosting=saas
- Voor elke SaaS-dienst die een kritiek proces ondersteunt, legt functioneel beheer in het back-upregister
  vast hoe de leverancier back-ups maakt, waar ze staan en hoe lang ze bewaard worden. Biedt de leverancier
  geen gescheiden kopie, of kan de organisatie er niet zelf bij, dan exporteert de organisatie de gegevens
  periodiek naar eigen opslag of neemt zij een back-updienst van een andere partij af. [8.13.03]
:::

::: als werkplek=cloud,hybride
- De cloudwerkplek (mail, bestanden, samenwerkruimtes) heeft een eigen back-up buiten de tenant. De
  ingebouwde prullenbak en het versiebeheer van de aanbieder gelden niet als back-up. De back-up omvat ook de
  inrichting die nodig is voor herstel, zoals groepen, rechten en beleidsinstellingen, voor zover de
  aanbieder dat mogelijk maakt. Functioneel beheer controleert elk kwartaal dat de back-up alle actieve
  onderdelen dekt. [8.13.03]
:::

## 7. Herstel en testen

- Herstel uit een back-up gebeurt na toestemming van de systeemeigenaar. Bij een groot incident of
  ransomware beslist de proceseigenaar over de opties, op advies van de beheerorganisatie en de CISO. De
  beheerorganisatie logt elke hersteloperatie met aanvrager, tijdstip en resultaat. [8.13.04]
- De beheerorganisatie test de herstelprocedure van elk systeem met impactniveau kritiek of hoger elk
  jaar en na elke grote wijziging, zoals een migratie of een nieuwe back-upvoorziening. De test zet echte
  gegevens terug, controleert of ze volledig en bruikbaar zijn en meet de benodigde tijd tegen de
  hersteltijd. De uitkomst staat in een testverslag. [8.13.04]
- Ten minste één test per jaar gaat uit van het ransomwarescenario: herstel uit de onveranderbare kopie,
  in een schone omgeving, zonder gebruik van de beheeraccounts van productie. [8.13.04]
- Haalt een test de hersteltijd niet, dan past de systeemeigenaar binnen drie maanden het back-upplan of de
  voorziening aan, of accepteert de proceseigenaar het risico vastgelegd. [8.13.04, 8.13.02]

::: als beheer=eigen
- De eigen beheerorganisatie voert de tests uit en legt ze vast in een testverslag met tijden, bevindingen
  en opvolging. [8.13.04]
:::

::: als beheer=regie,uitbesteed
- Back-up en herstel liggen bij de beheerpartij. Het contract verplicht die partij om de tests uit te voeren
  met de organisatie erbij, de verslagen te leveren en ook kopieën te maken en te testen van onderdelen die
  bij andere leveranciers liggen, of dat expliciet uit te sluiten. De regieorganisatie houdt in het
  back-upregister bij welke leverancier welk deel van de back-up doet. [8.13.04]
:::

## 8. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| [[lijneigenaar back-up]] | Eigenaar van dit beleid; uitvoering of regie van back-up en herstel, dagelijkse controle, hersteltests en het back-upregister |
| Proceseigenaar | Hersteleisen en bewaartermijnen, besluit over herstel bij grote incidenten, acceptatie van een niet gehaalde hersteltijd |
| Systeemeigenaar | Goedkeuring van het back-upplan van zijn systeem, toestemming voor herstel, aanpassing na een mislukte test |
| [[eigenaar back-upplannen]] | Opstellen en jaarlijks herzien van de back-upplannen, rapportage over systemen op het standaardregime |
| Functioneel beheer | Back-up en herstel van SaaS-diensten en de cloudwerkplek, samen met de leverancier |
| Contracteigenaar | Vastleggen van de eisen uit dit beleid bij leveranciers en toetsen van hun verklaringen en testverslagen |
| CISO | Advies, jaarlijkse toetsing van dit beleid en van de bescherming tegen ransomware, beoordeling van afwijkingen |

## 9. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in [[registratie van controles]]; afwijkingen gaan als bevinding naar het
risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| BUR-01 | Alle back-uptaken van de afgelopen maand zijn gecontroleerd en elke mislukte taak is binnen een werkdag hersteld of gemeld | [[lijneigenaar back-up]] | Maandelijks | Logboek van de back-uptaken met de afhandeling per mislukte taak | 8.13.01 |
| BUR-02 | Het back-upregister is volledig: elk systeem met impactniveau kritiek of hoger en elke SaaS-dienst met een kritiek proces heeft een goedgekeurd back-upplan van ten hoogste een jaar oud, vastgestelde hersteleisen, een gescheiden kopie en een onveranderbare kopie | [[eigenaar back-upplannen]] | Jaarlijks | Back-upregister vergeleken met het overzicht van kritieke systemen en de inventaris van bedrijfsmiddelen | 8.13.01, 8.13.02, 8.13.03 |
| BUR-03 | Elk systeem heeft vastgestelde hersteleisen met een risicoafweging, of staat gemeld op het standaardregime; de hersteltijd van kritieke systemen ligt onder de maximale uitvalsduur | CISO | Jaarlijks | Rapportage over het standaardregime, steekproef van vijf back-upplannen tegen de BIA of het overzicht van kritieke systemen | 8.13.02 |
| BUR-04 | De onveranderbare kopie is niet te wissen met de beheerrechten van productie, de back-upaccounts staan buiten het gewone domein met MFA, en het verkorten van bewaartermijnen vereist een tweede persoon | CISO | Jaarlijks | Testpoging tot verwijderen met het resultaat, lijst van back-upaccounts, logging van de goedkeuringen | 8.13.01 |
| BUR-05 | De gescheiden kopie staat op een locatie die een incident op de productielocatie niet raakt, en bij leveranciers is dat in het contract en met een verklaring aangetoond | Contracteigenaar | Jaarlijks | Back-upregister met de locaties, contracten, verklaringen en testverslagen van leveranciers | 8.13.03 |
| BUR-06 | Elk kritiek systeem heeft in het afgelopen jaar een hersteltest gehad die de hersteltijd haalde, waaronder ten minste één test van het ransomwarescenario uit de onveranderbare kopie | [[lijneigenaar back-up]] | Jaarlijks | Testverslagen met gemeten tijd tegen de eis, opvolging van niet gehaalde tests | 8.13.04 |
| BUR-07 | Elke hersteloperatie is gelogd met toestemming van de systeemeigenaar | [[lijneigenaar back-up]] | Per kwartaal | Logboek van hersteloperaties met de toestemmingen | 8.13.04 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De
systeemeigenaar dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de looptijd.
De afwijking geldt pas na acceptatie van het risico door [[risico-eigenaar: de manager die restrisico's accepteert]]
en staat in het risicoregister; afwijkingen worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 10. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het hangt samen met het
continuïteitsbeleid (kritieke systemen, BIA en uitwijk), het beleid informatieclassificatie (impactniveau
als maat voor de hersteleisen), het beleid informatiebeveiliging bij inkoop en contractbeheer (afspraken
met en verklaringen van leveranciers), het beleid cryptografie (versleuteling en sleutelbeheer), het beleid
logische toegangsbeveiliging (beheeraccounts), het beleid fysieke toegang en beveiliging (opslaglocaties),
het beleid beveiligingsincidenten (herstel na ransomware) en het archiefbeleid (bewaartermijnen).
