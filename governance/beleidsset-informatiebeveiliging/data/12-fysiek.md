---
domein: fysiek
titel: Beleid fysieke toegang en beveiliging
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor de fysieke beveiliging van locaties,
ruimten en voorzieningen waar informatie wordt verwerkt of bewaard. Het geldt voor iedereen die een locatie
van de organisatie betreedt: medewerkers, inhuur, stagiairs, bezoekers en leveranciers. Het gaat over de
ISO-beheersmaatregelen 7.01 tot en met 7.05 en 7.12.

Buiten dit beleid vallen het werken in beveiligde zones en het plaatsen en onderhouden van apparatuur
(beleid bedrijfsmiddelenbeheer), clear desk en clear screen (beleid IT-compliance) en opslagmedia (beleid
afvoer en hergebruik van gegevensdragers).

::: als hosting=saas
De organisatie heeft geen eigen datacenter en geen serverruimte bij een hostingpartij. De fysieke
beveiliging van de systemen ligt bij de SaaS-leveranciers; dit beleid regelt de kantoorlocaties, de
netwerk- en stroomvoorzieningen op die locaties en de eisen die de organisatie aan leveranciers stelt.
:::

## 2. Uitgangspunten

1. Fysieke beveiliging is risicogestuurd: hoe groter de gevolgen van onbevoegde toegang voor beschikbaarheid,
   integriteit en vertrouwelijkheid, hoe zwaarder de maatregelen.
2. Elke ruimte valt in een beveiligingszone. De zone bepaalt de eisen; de eisen van een hogere zone komen
   bovenop die van de lagere.
3. Kritieke informatie en kritieke systemen liggen achter minstens twee opeenvolgende zones.

## 3. Beleidsregels

### 3.1 Beveiligingszones

- De organisatie deelt elke locatie in vier zones in en legt dat vast in een zoneringsplan per locatie:
  niveau 0 openbaar (buitenruimte, ontvangsthal), niveau 1 kantoor, niveau 2 beperkt (netwerk- en
  stroomknooppunten, archief, opslag van kritieke apparatuur) en niveau 3 kritiek (serverruimte, opslag van
  waardedocumenten).
- Het zoneringsplan noemt per zone de eigenaar. De eigenaar controleert ten minste elk halfjaar wie toegang
  heeft en beoordeelt jaarlijks of het niveau nog klopt.
- Een ruimte met kritieke informatie of kritieke systemen is alleen bereikbaar via ten minste twee zones met
  elk een eigen toegangscontrole; één deur of één pas is nooit genoeg. [7.01.02]

::: als hosting=eigen-dc
- De eigen serverruimte is een zone van niveau 3 binnen een zone van niveau 2. Toegang loopt via een
  tweede, persoonsgebonden controle (pas met pincode of biometrie) die per binnenkomst wordt gelogd. [7.01.02]
:::

::: als hosting=hostingpartij,saas
- Waar systemen bij een hostingpartij of SaaS-leverancier staan, eist de organisatie in het contract een
  zonering met ten minste twee opeenvolgende beveiligde zones voor de ruimte met de systemen, en een
  verklaring (ISO 27001-certificaat of ISAE 3402-rapport) die dat aantoont. [7.01.02]
- Ook op de eigen locaties liggen netwerk- en stroomknooppunten achter ten minste twee zones. [7.01.02]
:::

### 3.2 Fysieke toegang

- Toegang tot zones van niveau 1 en hoger gaat met een persoonsgebonden toegangsmiddel. Rechten volgen de
  functie en worden ingetrokken op de laatste werkdag.
- Bezoekers melden zich bij de receptie, dragen zichtbaar een bezoekerspas en worden in zones van niveau 2 en
  hoger begeleid.
- Toegang tot zones van niveau 3 wordt per binnenkomst gelogd; de logging wordt ten minste een jaar bewaard.
- Bij een concreet beveiligingsrisico voor een locatie, zoals een dreiging, een inbraak of een verdachte
  situatie, waarschuwt
  [[meldpunt fysieke beveiliging: de functie die de waarschuwing doet, zoals de coördinator facilitaire beveiliging]]
  volgens de gemaakte afspraken de relevante collega's in het
  beveiligingsdomein van de overheid: de CISO, de beveiligingscoördinatoren van samenwerkingspartners op
  dezelfde locatie en, bij een strafbaar feit, de politie. [7.02.01]
- De afspraken over wie wie waarschuwt, met welk kanaal en binnen welke tijd, staan in
  [[afsprakenlijst waarschuwingen: document met de contactpersonen en kanalen per partner]]
  en worden jaarlijks
  gecontroleerd. [7.02.01]

### 3.3 Kantoren, ruimten en faciliteiten

- Ruimten van niveau 2 en hoger zijn niet herkenbaar als zodanig aangeduid en staan niet op openbare
  plattegronden.
- Buiten openingstijden zijn locaties afgesloten en bewaakt. Een ingehuurde bewakingsdienst heeft een
  vergunning volgens de Wet particuliere beveiligingsorganisaties en recherchebureaus.

### 3.4 Monitoren

- Toegangsdeuren van niveau 2 en hoger hebben een alarm bij openbreken of te lang openstaan; het alarm komt
  binnen kantoortijd bij de receptie en daarbuiten bij de meldkamer van de bewakingsdienst.
- Camerabeelden worden alleen gemaakt waar dat nodig is voor de beveiliging, met een registratie in het
  verwerkingsregister en een bewaartermijn van ten hoogste vier weken, tenzij een incident langer bewaren
  rechtvaardigt.

### 3.5 Omgevingsdreigingen

- Ruimten van niveau 3 hebben brandmelding, automatische blussing of een gelijkwaardige maatregel,
  temperatuurbewaking en een noodstroomvoorziening die is afgestemd op de hersteltijden uit het
  continuïteitsbeleid.

::: als ot=beperkt,substantieel
- Ruimten met operationele technologie (gemalen, sluizen, installaties, gebouwbeheer) zijn opgenomen in het
  zoneringsplan. Besturingskasten en lokale bedieningspanelen zitten achter slot en worden bij elke
  inspectie gecontroleerd op sporen van openbreken. [7.01.02]
:::

### 3.6 Bekabeling

- Netwerk- en stroombekabeling naar ruimten van niveau 2 en hoger loopt niet door openbare ruimten of is daar
  afgeschermd. Patchkasten zijn afgesloten.

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| [[lijneigenaar fysieke beveiliging: de manager die dit beleid uitvoert, bijvoorbeeld facilitaire zaken]] | Uitvoering van dit beleid, het zoneringsplan en de toegangsmiddelen |
| Eigenaar van een zone | Controle van de toegangsrechten (halfjaarlijks) en van het niveau van de zone (jaarlijks) |
| CISO | Advies, toetsing van dit beleid en ontvangst van waarschuwingen bij concrete dreigingen |
| Medewerkers | Hun toegangsmiddel persoonlijk gebruiken, bezoekers begeleiden en verdachte situaties melden |

## 5. Naleving en bewaking

- Jaarlijks: steekproef op de toegangsrechten per zone van niveau 2 en 3 tegen de personeelsadministratie;
  bewijs is de vergelijking met de afwijkingen en hun afhandeling.
- Jaarlijks: controle dat het zoneringsplan actueel is en dat elke kritieke ruimte achter twee zones ligt.
- Jaarlijks: controle dat de afsprakenlijst voor waarschuwingen actueel is, en na elke waarschuwing een korte
  evaluatie of de juiste partners op tijd zijn bereikt.
- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid
bedrijfsmiddelenbeheer (apparatuur in beveiligde zones), het beleid afvoer en hergebruik van gegevensdragers,
het beleid back-up en recovery (uitwijk- en opslaglocaties) en het continuïteitsbeleid (noodstroom en
uitwijk).
