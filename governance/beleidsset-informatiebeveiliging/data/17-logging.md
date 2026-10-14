---
domein: logging
titel: Beleid logging en monitoring
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor het vastleggen, bewaren en
beschermen van logbestanden en voor het bewaken van de omgeving op aanvallen en afwijkingen. Logging is
nodig om aanvallen te ontdekken, om incidenten achteraf te kunnen reconstrueren en om te kunnen aantonen
wie wat heeft gedaan met welke gegevens. Het gaat over de ISO-beheersmaatregelen 8.15 en 8.16.

Het beleid geldt voor alle systemen, applicaties, netwerkcomponenten en clouddiensten waarmee de
organisatie informatie verwerkt, en voor iedereen die logging inricht, beheert of beoordeelt, ook als een
leverancier of SOC-dienstverlener dat doet.

Buiten dit beleid vallen de afhandeling van incidenten die uit monitoring voortkomen (beleid
beveiligingsincidenten) en de tijdsynchronisatie en netwerkinrichting (beleid netwerkbeveiliging).

## 2. Uitgangspunten

1. Wat gelogd wordt, volgt uit risico: hoe hoger de classificatie van een systeem, hoe meer er wordt
   vastgelegd en hoe langer het wordt bewaard.
2. Logbestanden zijn zelf vertrouwelijke informatie. Ze worden beschermd tegen inzage, wijziging en
   verwijdering.
3. Logging zonder beoordeling heeft weinig waarde. Voor elke logbron staat vast wie hem bekijkt en wat er
   gebeurt bij een afwijking.

## 3. Beleidsregels

### 3.1 Wat er gelogd wordt

- Elk systeem logt ten minste: aanmeldingen en mislukte aanmeldpogingen, het gebruik van beheerrechten,
  wijzigingen in accounts en rechten, wijzigingen in de beveiligingsinstellingen, het starten en stoppen
  van de logging zelf, en de toegang tot gegevens met classificatie hoog.
- Elke logregel bevat: de handeling, het object waarop de handeling betrekking had, het resultaat, het
  apparaat of netwerkadres van herkomst, de persoon of het proces dat de handeling startte, en datum en
  tijd. Alle systemen gebruiken dezelfde tijdbron. [8.15.01]
- Logregels bevatten geen wachtwoorden, sessietokens, sleutels of andere gegevens waarmee de beveiliging
  kan worden doorbroken. Bij de ingebruikname van een nieuwe logbron controleert de beheerder een
  steekproef van de logregels hierop. [8.15.02]
- De organisatie houdt een overzicht bij van alle logbronnen: per systeem welke gebeurtenissen worden
  gelogd, waar de logbestanden staan, de bewaartermijn, wie ze beheert en wie ze beoordeelt. Een nieuw
  systeem gaat pas in productie als het in dit overzicht staat. [8.15.03]

::: als hosting=saas
- Voor SaaS- en clouddiensten legt de organisatie in het contract vast welke auditlogs de leverancier
  beschikbaar stelt, hoe lang die bewaard blijven en hoe de organisatie ze kan exporteren naar de eigen
  centrale logvoorziening. Waar de leverancier de logs korter bewaart dan de eigen termijn, haalt de
  organisatie ze zelf op. [8.15.03, 8.15.04]
:::

::: als hosting=hostingpartij
- Bij een hostingpartij logt de organisatie zelf op het niveau van besturingssysteem en applicatie. De
  logging van de platformlaag (hypervisor, beheerportaal, netwerk van de hostingpartij) levert de
  hostingpartij op verzoek binnen een afgesproken termijn, vastgelegd in het contract. [8.15.03]
:::

::: als hosting=eigen-dc
- In het eigen datacenter verzamelt een centrale logvoorziening de logging van servers, opslag,
  virtualisatie en netwerkcomponenten. De logvoorziening staat in een eigen beheersegment. [8.15.03]
:::

::: als politiegegevens=ja
- Voor systemen met politiegegevens logt de organisatie elke raadpleging en elke verstrekking, met de
  persoon die raadpleegt en, waar het systeem dat toelaat, het doel van de raadpleging. Deze logging is
  nodig voor de verantwoording onder de Wet politiegegevens. [8.15.01, 8.15.03]
:::

::: als ketens=digid,suwinet,brp,bag,anders
- Voor de aansluiting op landelijke voorzieningen volgt de organisatie bovendien de logeisen uit het
  normenkader van die voorziening en neemt zij de betreffende systemen apart op in het overzicht van
  logbronnen. [8.15.03]
:::

### 3.2 Bewaren en beschermen

- De bewaartermijn per logbron staat in het overzicht en is gebaseerd op een risicoafweging. Omdat
  aanvallers vaak maanden onopgemerkt in een omgeving zitten, is de termijn voor beveiligingsrelevante
  logging en voor de gegevens in het SIEM ten minste
  [[bewaartermijn beveiligingslogging: de minimale termijn, bijvoorbeeld twaalf maanden]]. Logging die bij
  een incident hoort, valt onder de termijn van het incidentdossier (drie jaar). [8.15.04]
- Logging die persoonsgegevens bevat, wordt niet langer bewaard dan de vastgestelde termijn en alleen
  gebruikt voor beveiliging, beheer en verantwoording. De verwerking staat in het verwerkingsregister.
- Logbestanden worden zo snel mogelijk na het ontstaan naar een centrale opslag gekopieerd waar de
  beheerders van het bronsysteem geen schrijf- of verwijderrechten hebben.
- Een poging om loggegevens oneigenlijk te wijzigen of te verwijderen, of het onverwacht stoppen van de
  logging, wordt direct als beveiligingsincident gemeld via de incidentprocedure. De centrale
  logvoorziening geeft hierop een automatische melding. [8.15.05]
- Op basis van een risicoafweging stelt de CISO vast hoe vaak wordt getoetst dat de logbestanden
  gedurende de bewaartermijn ongewijzigd en volledig aanwezig zijn, met ten minste een jaarlijkse toets.
  De toets wordt uitgevoerd door iemand die geen beheertaken heeft op de logvoorziening of de
  bronsystemen. [8.15.06]

::: als capaciteit=geen,parttime
- De organisatie heeft geen eigen team dat onafhankelijk is van het beheer. De toets op ongewijzigde
  logbestanden laat zij uitvoeren door een externe auditor of door de interne controle. [8.15.06]
:::

::: als capaciteit=team
- De toets op ongewijzigde logbestanden voert een ISO uit die geen beheerrechten heeft op de logging. [8.15.06]
:::

::: als politiegegevens=ja
- De logging van systemen met politiegegevens wordt bewaard volgens de termijn uit de Wet politiegegevens
  en is onderwerp van de periodieke Wpg-audit. Alleen de privacy officer, de CISO en de functionaris die
  de Wpg-controle uitvoert, mogen deze logging raadplegen.
:::

### 3.3 Monitoren en detecteren

- De omgeving wordt bewaakt met een detectie- en responsvoorziening die de logging van werkplekken,
  servers, identiteiten, clouddiensten en netwerkcomponenten bij elkaar brengt, bijvoorbeeld een SIEM met
  endpoint detection and response. Afwijkingen worden binnen een vastgestelde tijd beoordeeld en
  opgevolgd. [8.16.03]
- Actieve netwerkcomponenten (firewalls, routers, switches, toegangspunten voor wifi en VPN) sturen hun
  logging naar deze voorziening. Er zijn detectieregels voor afwijkend gedrag zoals ongebruikelijk verkeer,
  wijzigingen in de configuratie en aanmeldingen buiten de beheerroute. [8.16.04]
- Voor de monitoring liggen vaste regels vast over wanneer een melding als incident aan het management
  gaat: per ernstniveau de termijn en de ontvanger. Een melding met ernst hoog of kritiek gaat altijd direct
  naar de CISO, die bepaalt of de directie wordt ingelicht. [8.16.02]
- Nieuwe dreigingen of aanvalstechnieken die bij de monitoring worden ontdekt, deelt de organisatie
  binnen de juridische kaders met de aangewezen CERT, zo nodig zonder persoonsgegevens. [8.16.01]

::: als detectie=eigen-soc
- Het eigen SOC beoordeelt de meldingen uit de detectievoorziening, ook buiten kantoortijd via een
  bereikbaarheidsdienst. Het SOC beheert de detectieregels en past ze aan na elk incident en na elke
  relevante dreigingsmelding. [8.16.03]
- Het SOC heeft een vastgelegde procedure voor het delen van nieuwe dreigingen met de CERT. [8.16.01]
:::

::: als detectie=uitbesteed
- Een SOC- of MDR-dienstverlener bewaakt de omgeving. Het contract regelt: welke logbronnen zijn
  aangesloten, de reactietijd per ernstniveau, de escalatie naar de organisatie, de bevoegdheid om in te
  grijpen, het delen van nieuwe dreigingen met de CERT en een maandelijkse rapportage. [8.16.01, 8.16.02, 8.16.03]
- De organisatie controleert elk kwartaal of alle logbronnen uit het overzicht ook bij de dienstverlener
  binnenkomen.
:::

::: als detectie=geen
- Er is nog geen structurele detectie. Als minimum zijn op werkplekken en servers detectie- en
  responsfuncties actief met automatische meldingen aan de beheerder, en worden de meldingen elke
  werkdag bekeken. De organisatie neemt het ontbreken van een SOC op als risico en legt in het jaarplan
  vast wanneer zij structurele detectie heeft ingericht, zelf of uitbesteed. [8.16.03]
:::

::: als hosting=saas,hostingpartij
- De logging van clouddiensten en van de hostingpartij is aangesloten op de detectievoorziening. Waar dat
  technisch niet kan, legt de organisatie vast welke meldingen de leverancier zelf geeft en hoe snel. [8.16.03]
:::

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| Systeemeigenaar | Bepalen wat er van zijn systeem wordt gelogd en hoe lang, opname in het overzicht van logbronnen |
| [[beheerder logvoorziening: de afdeling of leverancier die de centrale logging beheert]] | Inrichting en beschikbaarheid van de logging en de centrale opslag, steekproef op gevoelige gegevens |
| [[bewaking: het eigen SOC, de SOC-dienstverlener of de beheerder die de meldingen beoordeelt]] | Beoordelen van meldingen, escaleren volgens de regels, delen van nieuwe dreigingen |
| CISO | Vaststellen van bewaartermijnen en toetsfrequentie, ontvangst van escalaties, opdracht tot de onafhankelijke toets |
| Privacy officer en FG | Toetsing van het gebruik van logging met persoonsgegevens (FG houdt toezicht) |

## 5. Naleving en bewaking

- Per kwartaal: controle dat elke logbron uit het overzicht daadwerkelijk logt en in de centrale opslag
  binnenkomt; bewijs is de vergelijking met de afwijkingen.
- Jaarlijks: onafhankelijke toets op ongewijzigde en volledige logbestanden over de bewaartermijn; bewijs
  is het toetsverslag.
- Jaarlijks: steekproef van logregels uit vijf systemen op de verplichte velden en op het ontbreken van
  wachtwoorden of sleutels.
- Jaarlijks: test van de escalatie met een gesimuleerde melding met ernst hoog; bewijs is de tijdlijn van
  melding tot management.
- Maandelijks: rapportage over meldingen, escalaties en gedeelde dreigingen aan de CISO.
- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid
beveiligingsincidenten (melden van incidenten en bewaren van bewijs), het beleid netwerkbeveiliging
(bewaking van dataverkeer), het beleid logische toegangsbeveiliging (logging van beheerrechten), het
beleid informatieclassificatie (bewaartermijnen) en het privacybeleid (logging met persoonsgegevens).
