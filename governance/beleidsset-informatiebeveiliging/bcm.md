# Beleid ICT-continuïteit en uitwijk

Beleid informatiebeveiliging, BIO 2.0-domein *Business Continuity & Disaster Recovery*. Status: concept, vast te stellen door de organisatie zelf.

Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor de continuïteit van informatie en
ICT. Het regelt welke systemen kritiek zijn, welke hersteleisen daarbij horen, hoe de organisatie uitwijkt
als een systeem of locatie uitvalt, hoe de beveiliging overeind blijft tijdens een verstoring en hoe de
plannen worden getest. Het gaat over de ISO-beheersmaatregelen 5.29, 5.30 en 8.14.

Buiten dit beleid vallen de bedrijfscontinuïteit van processen die niets met ICT te maken hebben, de
crisisorganisatie zelf en het maken en terugzetten van back-ups (beleid back-up en recovery). Dit beleid sluit
daarop aan.

> **Alleen als: Hoe is je crisis- en continuïteitsorganisatie geregeld? «Een BCM-functie met continuïteitsplannen en een BIA»**
>
> De organisatie heeft een BCM-functie met een business impact analyse (BIA) en continuïteitsplannen. Dit
> beleid volgt de BIA: de hersteleisen voor systemen komen uit de hersteleisen voor processen.

> **Alleen als: Hoe is je crisis- en continuïteitsorganisatie geregeld? «Geen» of «Een crisisteam, zonder BCM-functie»**
>
> De organisatie heeft geen BCM-functie met een BIA. Dit beleid legt daarom zelf de minimale stappen vast om
> kritieke processen en systemen te bepalen. Komt er een BIA, dan vervangt die de stappen in 3.1.

## 2. Uitgangspunten

1. De lijn bepaalt welke processen kritiek zijn en in welke volgorde ze terugkomen. ICT vertaalt dat naar
   systemen, hersteleisen en voorzieningen.
2. Een continuïteitsplan dat niet getest is, telt niet als maatregel.
3. Tijdens een verstoring gelden dezelfde beveiligingseisen als daarbuiten, tenzij een vooraf vastgestelde
   noodprocedure iets anders zegt.

## 3. Beleidsregels

### 3.1 Kritieke processen en systemen

- De proceseigenaren stellen vast welke processen niet mogen uitvallen, omdat inwoners of bedrijven er direct
  last van hebben of omdat er een wettelijke termijn op zit. Per proces leggen ze vast: de maximale
  uitvalsduur, het maximale gegevensverlies en het minimumniveau waarop de dienstverlening tijdens de
  verstoring doorgaat.
- Op basis daarvan stelt elke proceseigenaar, met de systeemeigenaren, vast welke systemen kritiek zijn. Het
  gebeurt binnen de inventaris van bedrijfsmiddelen, met de risicomanagementmethodiek van de organisatie, en
  de afweging wordt vastgelegd. Een systeem is kritiek als een kritiek proces er binnen zijn maximale
  uitvalsduur niet zonder kan. [5.30.02]
- Het overzicht van kritieke systemen noemt per systeem de hersteltijd, het maximale gegevensverlies, de
  afhankelijkheden (netwerk, identiteitsvoorziening, koppelingen, leveranciers) en de herstelvolgorde. De
  herstelvolgorde is een besluit van de directie. [5.30.02]
- De proceseigenaar actualiseert het overzicht ten minste eens per drie jaar, en eerder bij een
  reorganisatie, een nieuwe aanbesteding, een uitbesteding of een migratie van een kritiek systeem. [5.30.02]

> **Alleen als: Hoe is je crisis- en continuïteitsorganisatie geregeld? «Een BCM-functie met continuïteitsplannen en een BIA»**
>
> - De kritieke processen en hun hersteleisen komen uit de BIA. De BCM-functie levert het overzicht aan;
>   **[eigenaar overzicht kritieke systemen]**
>   koppelt de systemen eraan. [5.30.02]

> **Alleen als: Hoe is je crisis- en continuïteitsorganisatie geregeld? «Geen» of «Een crisisteam, zonder BCM-functie»**
>
> - Zolang er geen BIA is, organiseert de CISO elke drie jaar een sessie met de proceseigenaren om de kritieke
>   processen te bepalen, met een startomvang van ongeveer twintig processen. De uitkomst wordt door de
>   directie vastgesteld. [5.30.02]

> **Alleen als: Wat is je status onder de Cyberbeveiligingswet? «Essentiële entiteit» of «Belangrijke entiteit»**
>
> - De organisatie valt onder de Cyberbeveiligingswet. De diensten waarvoor zij is aangewezen staan als
>   kritieke processen op de lijst, en de bestuurder keurt de hersteleisen en de herstelvolgorde goed. [5.30.02]

> **Alleen als: Heb je operationele technologie (OT)? «Beperkt: gebouwbeheer, toegang, camera's» of «Substantieel: bruggen, gemalen, verkeer, zuivering»**
>
> - Operationele technologie staat in hetzelfde overzicht. Per installatie staat erbij of hij bij uitval van
>   de ICT lokaal of met de hand te bedienen is en wie dat kan. [5.30.02]

### 3.2 Uitwijk en redundantie

- Voor elk kritiek systeem is een voorziening ingericht waarmee de hersteltijd haalbaar is: dubbele
  uitvoering, een uitwijklocatie of een herstel uit back-up dat aantoonbaar binnen de tijd past.
- Gedeelde voorzieningen waar meer kritieke systemen van afhangen (netwerk, internetverbinding,
  identiteitsvoorziening, stroom) zijn dubbel uitgevoerd of hebben een gedocumenteerde noodroute.
- Een uitwijkvoorziening is tegen dezelfde dreigingen beschermd als de primaire omgeving en is daar zo ver
  van gescheiden dat een cyberaanval of fysiek incident ze niet allebei raakt. Waar dat niet kan, staat het
  restrisico in het risicoregister.
- Ligt een kritiek systeem bij een leverancier, dan staan de hersteltijd, het maximale gegevensverlies en de
  uitwijkvoorziening in het contract, en levert de leverancier het bewijs van zijn eigen tests.

> **Alleen als: Heb je operationele technologie (OT)? «Substantieel: bruggen, gemalen, verkeer, zuivering»**
>
> - Bij installaties zoals gemalen, bruggen, sluizen en zuivering heeft de organisatie per installatie een
>   terugvalscenario zonder centrale besturing, met de bemensing die daarvoor nodig is en de tijd die het kan
>   volhouden. De OT-omgeving kan bij een aanval op de kantoor-ICT worden losgekoppeld zonder dat de installatie
>   stopt.

### 3.3 Beveiliging tijdens een verstoring

- Elk continuïteitsplan beschrijft welke beveiligingsmaatregelen tijdens uitwijk of noodbedrijf gelden. Een
  noodaccount, een handmatige werkwijze of een tijdelijke verbinding staat vooraf in het plan, met wie
  hem mag inzetten.
- Noodaccounts en tijdelijke uitzonderingen worden na de verstoring binnen
  **[termijn intrekken noodvoorzieningen]**
  ingetrokken, en de CISO controleert dat.
- Na een cyberincident gaat een systeem pas terug in productie als vaststaat dat de oorzaak is weggenomen en de
  herstelde omgeving schoon is.

### 3.4 Continuïteitsplannen en testen

- Voor elk kritiek proces is er een continuïteitsplan dat beschrijft hoe het proces doorgaat en wordt
  hersteld bij uitval van de ICT, met contactgegevens, beslissers en de herstelvolgorde. Het plan is ook
  beschikbaar als de eigen systemen niet werken.
- De proceseigenaar test het continuïteitsplan elk jaar op werking, volledigheid en actualiteit. De test kan
  een tafeloefening, een technische uitwijktest of een combinatie zijn; ten minste eens per drie jaar is er
  een technische test van de uitwijk van de kritieke systemen. [5.30.01]
- Elke test heeft een verslag met de bevindingen en de verbeteringen. De proceseigenaar past het plan binnen
  drie maanden aan en meldt open verbeteringen in het risicoregister. [5.30.01]

> **Alleen als: Hoe is je crisis- en continuïteitsorganisatie geregeld? «Geen»**
>
> - Er is geen crisisteam. Voor een digitale calamiteit stelt de CISO met de ICT-organisatie een
>   calamiteitenteam samen uit de eigen bedrijfsvoering, met een rolverdeling, een logboek en een
>   besluitprocedure. Dat team oefent elk jaar een scenario met uitval van ICT. [5.30.01]

> **Alleen als: Hoe is je crisis- en continuïteitsorganisatie geregeld? «Een crisisteam, zonder BCM-functie» of «Een BCM-functie met continuïteitsplannen en een BIA»**
>
> - De jaarlijkse test van de continuïteitsplannen sluit aan op een oefening van het crisisteam met een
>   digitaal scenario, bijvoorbeeld ransomware, zodat ook de besluitvorming en de communicatie worden getest.
>   [5.30.01]

> **Alleen als: Wat is je status onder de Cyberbeveiligingswet? «Essentiële entiteit» of «Belangrijke entiteit»**
>
> - De tests dekken ook de meldplicht onder de Cyberbeveiligingswet: wie stelt vast of een incident
>   significant is, en lukt de vroege waarschuwing binnen 24 uur. [5.30.01]

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| Directie | Vaststellen van de kritieke processen en de herstelvolgorde |
| Proceseigenaar | Hersteleisen per proces, kritieke systemen, continuïteitsplan en de jaarlijkse test |
| Systeemeigenaar | Uitwijk- en redundantievoorzieningen en de technische uitwijktest |
| **[lijneigenaar ICT-continuïteit]** | Uitvoering van uitwijk en herstel, ook bij leveranciers |
| CISO | Advies, toetsing van dit beleid, beveiliging tijdens verstoringen |

## 5. Naleving en bewaking

- Jaarlijks: overzicht van de continuïteitstests van dat jaar per kritiek proces, met de processen waarvoor de
  test ontbreekt; bewijs zijn de testverslagen.
- Jaarlijks: controle of de verbeteringen uit de tests van het jaar ervoor zijn doorgevoerd.
- Eens per drie jaar, of na een trigger uit 3.1: actualisatie van het overzicht van kritieke systemen;
  bewijs is het vastgestelde overzicht met datum.
- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het hangt nauw samen met het beleid back-up
en recovery (hersteltijden en gegevensverlies), het incidentbeleid (overgang van incident naar calamiteit),
het beleid bedrijfsmiddelenbeheer (inventaris), het beleid fysieke beveiliging (noodstroom, uitwijklocatie) en
het beleid contractbeheer (afspraken met leveranciers over uitwijk en exit).

## Bijlage: BIO 2.0-maatregelen

De overheidsmaatregelen van dit domein (2) en waar dit stuk ze invult. Nummers volgens BIO2 v1.3 definitief - 9 januari 2026; de tekst van de maatregel staat bij het CIP.

| Maatregel | Titel | In dit stuk |
|---|---|---|
| 5.30.01 | ICT-gereedheid voor bedrijfscontinuïteit | 3.4 Continuïteitsplannen en testen |
| 5.30.02 | ICT-gereedheid voor bedrijfscontinuïteit | 3.1 Kritieke processen en systemen |

## Nog in te vullen

- **eigenaar overzicht kritieke systemen**: de functie die het overzicht van kritieke systemen bijhoudt, bijvoorbeeld de informatiemanager
- **termijn intrekken noodvoorzieningen**: bijvoorbeeld vijf werkdagen
- **lijneigenaar ICT-continuïteit**: de manager die de ICT-voorzieningen voor continuïteit uitvoert
