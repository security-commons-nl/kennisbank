---
domein: bcm
titel: Beleid ICT-continuïteit en uitwijk
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor de continuïteit van informatie en
ICT. Het regelt welke processen en systemen kritiek zijn, welke hersteleisen daarbij horen, welke redundantie
en uitwijk de organisatie inricht, hoe de beveiliging overeind blijft tijdens een verstoring en hoe de
plannen worden getest. Het gaat over de ISO-beheersmaatregelen 5.29, 5.30 en 8.14.

**Voor wie.** Het beleid is primair bedoeld voor de directie, de proceseigenaren, de systeemeigenaren en de
afdeling die de ICT-voorzieningen voor continuïteit uitvoert. Het geldt voor iedereen die een rol heeft in
een continuïteitsplan of een calamiteitenteam, ook inhuur en leveranciers.

**Waarop.** Alle informatie, systemen, netwerken, koppelingen en gedeelde voorzieningen waarvan de kritieke
processen van de organisatie afhangen, ongeacht of ze in eigen beheer zijn, bij een hostingpartij draaien of
als clouddienst worden afgenomen. Is een systeem of voorziening uitbesteed, dan gelden de eisen uit dit
beleid als minimumeis voor de leverancier. De organisatie legt dat vast in het contract en toetst de
naleving met een onafhankelijke verklaring, zoals een ISO 27001-certificaat of een ISAE 3402- of ISAE
3000-rapport; het vastleggen loopt via het beleid informatiebeveiliging bij inkoop, het toetsen via het
beleid contractbeheer.

Buiten dit beleid vallen de bedrijfscontinuïteit van processen die niets met ICT te maken hebben, de
crisisorganisatie zelf (crisisprocedure), het maken en terugzetten van back-ups (beleid back-up en recovery),
de noodstroom en de fysieke bescherming van ruimten (beleid fysieke toegang en beveiliging) en de afhandeling
van het incident dat de verstoring veroorzaakt (beleid beveiligingsincidenten). Dit beleid sluit daarop aan.

::: als bcm=bcm
De organisatie heeft een BCM-functie met een business impact analyse (BIA) en continuïteitsplannen. Dit
beleid volgt de BIA: de hersteleisen voor systemen komen uit de hersteleisen voor processen.
:::

::: als bcm=geen,crisisteam
De organisatie heeft geen BCM-functie met een BIA. Dit beleid legt daarom zelf de minimale stappen vast om
kritieke processen en systemen te bepalen. Komt er een BIA, dan vervangt die de stappen in paragraaf 3.1.
:::

## 2. Uitgangspunten

1. De lijn bepaalt welke processen kritiek zijn en in welke volgorde ze terugkomen. ICT vertaalt dat naar
   systemen, hersteleisen en voorzieningen.
2. De maximale hersteltijd en het toelaatbare gegevensverlies van een proces volgen uit zijn impactniveau
   volgens het beleid informatieclassificatie (verwaarloosbaar, gering, gemiddeld, kritiek of zeer ernstig,
   catastrofaal). Dat beleid zegt per niveau welke hersteltijd en welk gegevensverlies hoogstens toelaatbaar
   zijn.
3. Een continuïteitsplan dat niet getest is, telt niet als maatregel.
4. Tijdens een verstoring gelden dezelfde beveiligingseisen als daarbuiten, tenzij een vooraf vastgestelde
   noodprocedure iets anders zegt.

## 3. Beleidsregels

### 3.1 Kritieke processen en systemen

- De proceseigenaren stellen vast welke processen niet mogen uitvallen, omdat inwoners of bedrijven er direct
  last van hebben of omdat er een wettelijke termijn op zit. Per proces leggen ze vast: het impactniveau, de
  maximale hersteltijd en het toelaatbare gegevensverlies die daaruit volgen, en het minimumniveau waarop de
  dienstverlening tijdens de verstoring doorgaat. [5.30.02]
- Op basis daarvan stelt elke proceseigenaar, met de systeemeigenaren, vast welke systemen kritiek zijn. Het
  gebeurt binnen de inventaris van bedrijfsmiddelen, met de risicomanagementmethodiek van de organisatie, en
  de afweging wordt vastgelegd. Een systeem is kritiek als een kritiek proces er binnen zijn maximale
  hersteltijd niet zonder kan. [5.30.02]
- [[eigenaar overzicht kritieke systemen: de functie die het overzicht van kritieke systemen bijhoudt, bijvoorbeeld de informatiemanager]]
  houdt het overzicht van kritieke systemen bij. Het noemt per systeem de hersteltijd, het toelaatbare
  gegevensverlies, de afhankelijkheden (netwerk, identiteitsvoorziening, koppelingen, leveranciers) en de
  herstelvolgorde. De directie stelt de herstelvolgorde vast. [5.30.02]
- De proceseigenaar actualiseert zijn deel van het overzicht ten minste eens per drie jaar, en eerder bij een
  reorganisatie, een nieuwe aanbesteding, een uitbesteding of een migratie van een kritiek systeem. De datum
  van de laatste actualisatie staat in het overzicht. [5.30.02]

::: als bcm=bcm
- De kritieke processen en hun hersteleisen komen uit de BIA. De BCM-functie levert het overzicht aan en de
  eigenaar van het overzicht kritieke systemen koppelt de systemen eraan. [5.30.02]
:::

::: als bcm=geen,crisisteam
- Zolang er geen BIA is, organiseert de CISO elke drie jaar een sessie met de proceseigenaren om de kritieke
  processen te bepalen, met een startomvang van ongeveer twintig processen. De directie stelt de uitkomst
  vast. [5.30.02]
:::

::: als cbw=essentieel,belangrijk
- De organisatie valt onder de Cyberbeveiligingswet. De diensten waarvoor zij is aangewezen staan als
  kritieke processen op de lijst, en de bestuurder keurt de hersteleisen en de herstelvolgorde goed. [5.30.02]
:::

::: als ot=beperkt,substantieel
- Operationele technologie staat in hetzelfde overzicht. Per installatie staat erbij of hij bij uitval van
  de ICT lokaal of met de hand te bedienen is en wie dat kan. [5.30.02]
:::

### 3.2 Uitwijk en redundantie

- Voor elk kritiek systeem richt de systeemeigenaar een voorziening in waarmee de hersteltijd en het
  toelaatbare gegevensverlies haalbaar zijn: dubbele uitvoering, een uitwijklocatie of een herstel uit
  back-up dat aantoonbaar binnen de tijd past. De keuze en de onderbouwing staan in het overzicht van
  kritieke systemen. [5.30.01, 8.14.01]
- Gedeelde voorzieningen waar meer kritieke systemen van afhangen (netwerk, internetverbinding,
  identiteitsvoorziening, stroom, koeling) voert [[lijneigenaar ICT-continuïteit: de manager die de ICT-voorzieningen voor continuïteit uitvoert]]
  dubbel uit, zonder gemeenschappelijk punt van uitval, of hij legt een noodroute vast die binnen de kortste
  hersteltijd van de afhankelijke systemen past. De lijneigenaar ICT-continuïteit test de omschakeling van
  elke dubbele voorziening jaarlijks. [8.14.01]
- De lijneigenaar ICT-continuïteit beschermt een uitwijkvoorziening tegen dezelfde dreigingen als de primaire
  omgeving en scheidt haar daar zo ver van dat een cyberaanval of fysiek incident ze niet allebei raakt:
  eigen stroom en netwerk, eigen beheeraccounts en een andere locatie. Waar dat niet kan, zet de
  systeemeigenaar het restrisico in het risicoregister. [8.14.01]
- Ligt een kritiek systeem bij een leverancier, dan staan de hersteltijd, het toelaatbare gegevensverlies en
  de uitwijkvoorziening in het contract, en levert de leverancier jaarlijks het bewijs van zijn eigen
  uitwijktests. De proceseigenaar beoordeelt dat bewijs bij de jaarlijkse leveranciersbeoordeling (beleid
  contractbeheer). [5.30.01, 8.14.01]
- Een redundante voorziening voldoet aan dezelfde beveiligingseisen als de primaire, en de systeemeigenaar
  neemt haar mee in patchen, logging en toegangsbeheer. [8.14.01]

::: als ot=substantieel
- Bij installaties zoals gemalen, bruggen, sluizen en zuivering legt de proceseigenaar per installatie een
  terugvalscenario zonder centrale besturing vast, met de bemensing die daarvoor nodig is en de tijd die het
  kan volhouden. De OT-omgeving kan bij een aanval op de kantoor-ICT worden losgekoppeld zonder dat de
  installatie stopt; de systeemeigenaar test dat jaarlijks. [5.30.01, 8.14.01]
:::

### 3.3 Beveiliging tijdens een verstoring

- Elk continuïteitsplan beschrijft welke beveiligingsmaatregelen tijdens uitwijk of noodbedrijf gelden en
  welke tijdelijk vervallen. Een noodaccount, een handmatige werkwijze of een tijdelijke verbinding staat
  vooraf in het plan, met wie hem mag inzetten en wie daarover beslist. De CISO keurt dat deel van het plan
  goed. [5.29.01]
- Tijdens een verstoring houdt de proceseigenaar een logboek bij van de ingezette noodvoorzieningen, de
  tijdelijk vervallen maatregelen en de informatie die daardoor minder beschermd was, zodat de organisatie
  achteraf kan beoordelen of er een incident of datalek is ontstaan. [5.29.01]
- De proceseigenaar trekt noodaccounts en tijdelijke uitzonderingen na de verstoring binnen
  [[termijn intrekken noodvoorzieningen: bijvoorbeeld vijf werkdagen]]
  in, en de CISO controleert dat aan de hand van het logboek. [5.29.01]
- Na een cyberincident brengt de systeemeigenaar een systeem pas terug in productie als vaststaat dat de
  oorzaak is weggenomen en de herstelde omgeving schoon is. De CISO geeft daarvoor vrijgave en legt die vast.
  [5.29.01]
- Informatie met het label vertrouwelijk of hoger blijft ook tijdens een verstoring versleuteld en alleen
  toegankelijk voor bevoegden; een handmatige werkwijze voor die informatie staat alleen in het plan als de
  CISO heeft vastgesteld dat de bescherming gelijkwaardig is. [5.29.01]

### 3.4 Continuïteitsplannen en testen

- Voor elk kritiek proces stelt de proceseigenaar een continuïteitsplan op dat beschrijft hoe het proces
  doorgaat en wordt hersteld bij uitval van de ICT, met contactgegevens, beslissers, de herstelvolgorde en
  de beveiliging tijdens de verstoring. Het plan is ook beschikbaar als de eigen systemen niet werken, op
  papier of op een losstaande voorziening. [5.30.01]
- De proceseigenaar test het continuïteitsplan elk jaar op werking, volledigheid en actualiteit. De test kan
  een tafeloefening, een technische uitwijktest of een combinatie zijn; ten minste eens per drie jaar is er
  een technische test waarin de uitwijk van de kritieke systemen binnen de hersteltijd en met ten hoogste het
  toelaatbare gegevensverlies wordt aangetoond. [5.30.01]
- Elke test heeft een verslag met de bevindingen en de verbeteringen. De proceseigenaar past het plan binnen
  drie maanden aan en meldt open verbeteringen in het risicoregister. [5.30.01]
- De lijneigenaar ICT-continuïteit houdt de uitwijkvoorzieningen en de herstelprocedures actueel bij elke
  wijziging van een kritiek systeem, via het wijzigingsproces (beleid wijzigingsbeheer). [5.30.01]

::: als bcm=geen
- Er is geen crisisteam. Voor een digitale calamiteit stelt de CISO met de ICT-organisatie een
  calamiteitenteam samen uit de eigen bedrijfsvoering, met een rolverdeling, een logboek en een
  besluitprocedure. Dat team oefent elk jaar een scenario met uitval van ICT. [5.30.01]
:::

::: als bcm=crisisteam,bcm
- De jaarlijkse test van de continuïteitsplannen sluit aan op een oefening van het crisisteam met een
  digitaal scenario, bijvoorbeeld ransomware, zodat ook de besluitvorming en de communicatie worden getest.
  [5.30.01]
:::

::: als cbw=essentieel,belangrijk
- De tests dekken ook de meldplicht onder de Cyberbeveiligingswet: wie stelt vast of een incident
  significant is, en lukt de vroege waarschuwing binnen 24 uur. [5.30.01]
:::

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| Directie | Vaststellen van de kritieke processen en de herstelvolgorde |
| Proceseigenaar | Hersteleisen per proces, kritieke systemen, continuïteitsplan, de jaarlijkse test, het logboek tijdens een verstoring en het intrekken van noodvoorzieningen |
| Systeemeigenaar | Uitwijk- en redundantievoorzieningen per kritiek systeem, de technische uitwijktest, restrisico's en de terugkeer in productie |
| [[eigenaar overzicht kritieke systemen]] | Het overzicht van kritieke systemen met hersteleisen, afhankelijkheden en herstelvolgorde |
| [[lijneigenaar ICT-continuïteit]] | Eigenaar van dit beleid; gedeelde voorzieningen, uitwijkvoorzieningen en herstelprocedures, ook bij leveranciers; jaarlijkse omschakeltest |
| CISO | Advies, goedkeuring van de beveiliging tijdens een verstoring, vrijgave na een cyberincident, jaarlijkse toetsing van opzet en werking |

## 5. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in [[registratie van controles: het systeem waarin controles worden vastgelegd, bijvoorbeeld het ticketsysteem of het managementsysteem]];
afwijkingen gaan als bevinding naar het risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| BCDR-01 | Het overzicht van kritieke systemen is volledig en actueel: elk kritiek proces heeft een impactniveau, hersteltijd en toelaatbaar gegevensverlies, elk kritiek systeem heeft afhankelijkheden en een plaats in de vastgestelde herstelvolgorde, en de actualisatie is niet ouder dan drie jaar | [[eigenaar overzicht kritieke systemen]] | Jaarlijks | Overzicht met datum, besluit van de directie over de herstelvolgorde | 5.30.02 |
| BCDR-02 | Elk kritiek proces heeft een continuïteitsplan dat in het afgelopen jaar is getest, en eens per drie jaar een technische uitwijktest binnen de hersteleisen | [[lijneigenaar ICT-continuïteit]] | Jaarlijks | Overzicht van de tests per kritiek proces met de processen waarvoor de test ontbreekt, testverslagen | 5.30.01 |
| BCDR-03 | De verbeteringen uit de tests van het jaar ervoor zijn binnen drie maanden in de plannen doorgevoerd of staan in het risicoregister | CISO | Jaarlijks | Vergelijking van de testverslagen met de aangepaste plannen en het risicoregister | 5.30.01 |
| BCDR-04 | Elke gedeelde voorziening en elk kritiek systeem heeft een redundantie- of uitwijkvoorziening die past bij de hersteleisen, de omschakeling is getest, en restrisico's staan in het risicoregister | [[lijneigenaar ICT-continuïteit]] | Jaarlijks | Overzicht van de voorzieningen per systeem, verslagen van de omschakeltests, risicoregister | 8.14.01 |
| BCDR-05 | Leveranciers van kritieke systemen hebben de hersteleisen en de uitwijk in het contract en hebben het bewijs van hun uitwijktests geleverd | Proceseigenaar | Jaarlijks, bij de leveranciersbeoordeling | Contract, testbewijs van de leverancier, beoordeling in het register van leveranciers | 5.30.01, 8.14.01 |
| BCDR-06 | Elk continuïteitsplan bevat een door de CISO goedgekeurd deel over de beveiliging tijdens een verstoring, en na elke verstoring is het logboek aanwezig, zijn de noodvoorzieningen binnen de termijn ingetrokken en is de vrijgave na een cyberincident vastgelegd | CISO | Jaarlijks, en na elke verstoring | Goedkeuring per plan, logboeken, intrekkingsregistratie, vrijgavebesluiten | 5.29.01 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De
proceseigenaar dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de looptijd. De
afwijking geldt pas na acceptatie van het risico door [[risico-eigenaar: de manager die restrisico's accepteert]]
en staat in het risicoregister; afwijkingen worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. De hersteleisen volgen het beleid
informatieclassificatie. Het beleid hangt nauw samen met het beleid back-up en recovery (hersteltijden en
gegevensverlies), het beleid beveiligingsincidenten (overgang van incident naar calamiteit), het beleid
bedrijfsmiddelenbeheer (inventaris), het beleid fysieke toegang en beveiliging (noodstroom, uitwijklocatie),
het beleid wijzigingsbeheer (actueel houden van uitwijk en herstel) en het beleid informatiebeveiliging bij
inkoop en contractbeheer (afspraken met leveranciers over uitwijk en exit).
