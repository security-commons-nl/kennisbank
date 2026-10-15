---
domein: logging
titel: Beleid logging en monitoring
samenvatting: Regelt wat systemen moeten loggen, hoe logbestanden veilig worden bewaard en hoe de omgeving wordt bewaakt op aanvallen. Behandelt minimale loggebeurtenissen, het overzicht van logbronnen, bewaartermijnen, centrale opslag buiten bereik van beheerders, detectie met escalatieregels en het delen van dreigingen met de CERT.
invoeren:
  - Richt op elk systeem de minimale loggebeurtenissen en verplichte velden in, met één tijdbron (hoofdstuk 3).
  - Stel een overzicht van logbronnen op met gebeurtenissen, opslag, bewaartermijn en beoordelaar per systeem (hoofdstuk 3).
  - Leg per logbron de bewaartermijn vast op basis van een risicoafweging (hoofdstuk 4).
  - Neem logging met persoonsgegevens op in het verwerkingsregister (hoofdstuk 4).
  - Kopieer logbestanden naar centrale opslag waar beheerders van het bronsysteem niets kunnen wijzigen (hoofdstuk 4).
  - Stel een automatische melding in bij het wijzigen, verwijderen of stoppen van logging (hoofdstuk 4).
  - Richt een detectievoorziening in die de logging van alle bronnen samenbrengt, bijvoorbeeld een SIEM (hoofdstuk 5).
  - Leg escalatieregels vast met per ernstniveau de termijn en de ontvanger (hoofdstuk 5).
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor het vastleggen, bewaren en
beschermen van logbestanden en voor het bewaken van de omgeving op aanvallen en afwijkingen. Logging is
nodig om aanvallen te ontdekken, om incidenten achteraf te reconstrueren en om aan te tonen wie wat heeft
gedaan met welke gegevens. Het gaat over de ISO-beheersmaatregelen 8.15 en 8.16.

**Voor wie.** Het beleid is primair bedoeld voor de afdeling die de centrale logvoorziening beheert, voor
systeemeigenaren en voor wie de meldingen beoordeelt: het eigen SOC, een SOC-dienstverlener of de
beheerder. De regels over het gebruik van logging gelden voor iedereen die logbestanden inricht, beheert
of raadpleegt.

**Waarop.** Alle systemen, applicaties, netwerkcomponenten, werkplekken, identiteitsvoorzieningen en
clouddiensten waarmee de organisatie informatie verwerkt, en de logbestanden die daaruit voortkomen. Is de
logvoorziening, de bewaking of een systeem uitbesteed, dan gelden de eisen uit dit beleid als minimumeis
voor die partij. De organisatie legt dat vast in het contract en toetst de naleving met een onafhankelijke
verklaring, zoals een ISO 27001-certificaat of een ISAE 3402- of ISAE 3000-rapport; het vastleggen loopt
via het beleid informatiebeveiliging bij inkoop, het toetsen via het beleid contractbeheer.

Buiten dit beleid vallen de afhandeling van incidenten die uit monitoring voortkomen (beleid
beveiligingsincidenten), de tijdsynchronisatie en de netwerkinrichting (beleid netwerkbeveiliging) en de
toekenning van rechten die de logging vastlegt (beleid logische toegangsbeveiliging).

## 2. Uitgangspunten

1. Wat gelogd wordt, volgt uit risico: hoe hoger het impactniveau van een systeem, hoe meer er wordt
   vastgelegd en hoe langer het wordt bewaard.
2. Logbestanden zijn zelf informatie met ten minste het label vertrouwelijk. Ze worden beschermd tegen
   inzage, wijziging en verwijdering.
3. Logging zonder beoordeling heeft weinig waarde. Voor elke logbron staat vast wie hem bekijkt en wat er
   gebeurt bij een afwijking.
4. Logging met persoonsgegevens dient alleen beveiliging, beheer en verantwoording, niet het volgen van
   medewerkers.
5. Termijnen en frequenties in dit beleid die niet uit een wet of uit de BIO 2.0 komen, zijn standaardwaarden.
   De organisatie past ze aan op haar eigen risicoafweging en legt de keuze vast bij de vaststelling van dit beleid.

## 3. Wat er gelogd wordt

- De systeemeigenaar zorgt dat elk systeem ten minste logt: aanmeldingen en mislukte aanmeldpogingen, het
  gebruik van beheerrechten, wijzigingen in accounts en rechten, wijzigingen in de beveiligingsinstellingen,
  het starten en stoppen van de logging zelf, en de toegang tot gegevens met het label vertrouwelijk of
  hoger. [8.15.01]
- Elke logregel bevat: de handeling, het object waarop de handeling betrekking had, het resultaat, het
  apparaat of netwerkadres van herkomst, de persoon of het proces dat de handeling startte, en datum en
  tijd. Alle systemen gebruiken dezelfde tijdbron. [8.15.01]
- Logregels bevatten geen wachtwoorden, sessietokens, sleutels of andere gegevens waarmee de beveiliging
  kan worden doorbroken. Bij de ingebruikname van een nieuwe logbron controleert
  [[beheerder logvoorziening: de afdeling of leverancier die de centrale logging beheert]] een steekproef
  van de logregels hierop en legt de uitkomst vast. [8.15.02]
- [[beheerder logvoorziening]] houdt een overzicht bij van alle logbronnen: per systeem welke gebeurtenissen
  worden gelogd, waar de logbestanden staan, de bewaartermijn, wie ze beheert en wie ze beoordeelt. Een
  nieuw systeem gaat pas in productie als het in dit overzicht staat; wijzigingsbeheer controleert dat bij
  elke ingebruikname. [8.15.03]

::: als hosting=saas
- Voor SaaS- en clouddiensten legt de organisatie bij inkoop in het contract vast welke auditlogs de
  leverancier beschikbaar stelt, hoe lang die bewaard blijven en hoe de organisatie ze kan exporteren naar
  de eigen centrale logvoorziening. Waar de leverancier de logs korter bewaart dan de eigen termijn, haalt
  [[beheerder logvoorziening]] ze zelf op. [8.15.03, 8.15.04]
:::

::: als hosting=hostingpartij
- Bij een hostingpartij logt de organisatie zelf op het niveau van besturingssysteem en applicatie. De
  logging van de platformlaag (hypervisor, beheerportaal, netwerk van de hostingpartij) levert de
  hostingpartij op verzoek binnen de termijn uit het contract. [8.15.03]
:::

::: als hosting=eigen-dc
- In het eigen datacenter verzamelt een centrale logvoorziening de logging van servers, opslag,
  virtualisatie en netwerkcomponenten. De logvoorziening staat in een eigen beheersegment. [8.15.03]
:::

::: als politiegegevens=ja
- Voor systemen met politiegegevens logt de organisatie elke raadpleging en elke verstrekking, met de
  persoon die raadpleegt en, waar het systeem dat toelaat, het doel van de raadpleging. Deze logging is
  nodig voor de verantwoording onder de Wpg. [8.15.01, 8.15.03]
:::

::: als ketens=digid,suwinet,brp,bag,anders
- Voor de aansluiting op landelijke voorzieningen volgt de systeemeigenaar bovendien de logeisen uit het
  normenkader van die voorziening en staan de betreffende systemen apart in het overzicht van logbronnen,
  met het normenkader erbij. [8.15.03]
:::

## 4. Bewaren en beschermen

- De bewaartermijn per logbron staat in het overzicht en volgt uit een risicoafweging door de
  systeemeigenaar. Omdat aanvallers vaak maanden onopgemerkt in een omgeving zitten, is de termijn voor
  beveiligingsrelevante logging en voor de gegevens in het SIEM ten minste
  [[bewaartermijn beveiligingslogging: de minimale termijn, bijvoorbeeld twaalf maanden]].
  Logging die bij een incident hoort, valt onder de termijn van het incidentdossier (drie jaar). [8.15.04]
- Logging die persoonsgegevens bevat, wordt niet langer bewaard dan de vastgestelde termijn en alleen
  gebruikt voor beveiliging, beheer en verantwoording. De verwerking staat in het verwerkingsregister; de
  privacy officer toetst dat jaarlijks. [8.15.04]
- [[beheerder logvoorziening]] kopieert logbestanden zo snel mogelijk na het ontstaan naar een centrale
  opslag waar de beheerders van het bronsysteem geen schrijf- of verwijderrechten hebben. [8.15.05]
- Een poging om loggegevens oneigenlijk te wijzigen of te verwijderen, of het onverwacht stoppen van de
  logging, wordt direct als beveiligingsincident gemeld via de incidentprocedure. De centrale
  logvoorziening geeft hierop een automatische melding aan [[bewaking: het eigen SOC, de SOC-dienstverlener of de beheerder die de meldingen beoordeelt]]. [8.15.05]
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
- De logging van systemen met politiegegevens wordt bewaard volgens de termijn uit de Wpg en is onderwerp
  van de periodieke Wpg-audit. Alleen de privacy officer, de CISO en de functionaris die de Wpg-controle
  uitvoert, mogen deze logging raadplegen; elke raadpleging wordt zelf ook gelogd. [8.15.04, 8.15.05]
:::

## 5. Monitoren en detecteren

- De organisatie bewaakt de omgeving met een detectie- en responsvoorziening die de logging van
  werkplekken, servers, identiteiten, clouddiensten en netwerkcomponenten bij elkaar brengt, bijvoorbeeld
  een SIEM met EDR. [[bewaking]] beoordeelt afwijkingen binnen de termijn per ernstniveau en legt de
  beoordeling vast. [8.16.03]
- Actieve netwerkcomponenten (firewalls, routers, switches, toegangspunten voor wifi en VPN) sturen hun
  logging naar deze voorziening. [[bewaking]] onderhoudt detectieregels voor afwijkend gedrag zoals
  ongebruikelijk verkeer, wijzigingen in de configuratie en aanmeldingen buiten de beheerroute. [8.16.04]
- De CISO legt vaste regels vast over wanneer een melding als incident aan het management gaat: per
  ernstniveau de termijn en de ontvanger. Een melding met ernst hoog of kritiek gaat altijd direct naar de
  CISO, die bepaalt of de directie wordt ingelicht. [8.16.02]
- Nieuwe dreigingen of aanvalstechnieken die bij de monitoring worden ontdekt, deelt [[bewaking]] binnen
  de juridische kaders met de aangewezen CERT, zo nodig zonder persoonsgegevens, en legt vast wat is
  gedeeld. [8.16.01]
- [[bewaking]] rapporteert maandelijks aan de CISO over meldingen, escalaties en gedeelde dreigingen.
  [8.16.02, 8.16.03]

::: als detectie=eigen-soc
- Het eigen SOC beoordeelt de meldingen uit de detectievoorziening, ook buiten kantoortijd via een
  bereikbaarheidsdienst. Het SOC beheert de detectieregels en past ze aan na elk incident en na elke
  relevante dreigingsmelding. [8.16.03, 8.16.04]
- Het SOC heeft een vastgelegde procedure voor het delen van nieuwe dreigingen met de CERT. [8.16.01]
:::

::: als detectie=uitbesteed
- Een SOC- of MDR-dienstverlener bewaakt de omgeving. Het contract regelt: welke logbronnen zijn
  aangesloten, de reactietijd per ernstniveau, de escalatie naar de organisatie, de bevoegdheid om in te
  grijpen, het delen van nieuwe dreigingen met de CERT en een maandelijkse rapportage. [8.16.01, 8.16.02, 8.16.03]
- [[beheerder logvoorziening]] controleert elk kwartaal of alle logbronnen uit het overzicht ook bij de
  dienstverlener binnenkomen en legt de uitkomst vast. [8.16.03, 8.16.04]
:::

::: als detectie=geen
- Er is nog geen structurele detectie. Als minimum zijn op werkplekken en servers detectie- en
  responsfuncties actief met automatische meldingen aan de beheerder, die ze elke werkdag bekijkt. De CISO
  neemt het ontbreken van een SOC op als risico in het risicoregister en legt in het jaarplan vast wanneer de
  organisatie structurele detectie heeft ingericht, zelf of uitbesteed. [8.16.03, 8.16.04]
:::

::: als hosting=saas,hostingpartij
- De logging van clouddiensten en van de hostingpartij is aangesloten op de detectievoorziening. Waar dat
  technisch niet kan, legt de systeemeigenaar vast welke meldingen de leverancier zelf geeft en hoe snel.
  [8.16.03]
:::

## 6. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| [[lijneigenaar logging: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd IT]] | Eigenaar van dit beleid, de centrale logvoorziening en de contracten met de SOC-dienstverlener |
| Systeemeigenaar | Bepalen wat er van zijn systeem wordt gelogd en hoe lang, opname in het overzicht van logbronnen, afspraken met leveranciers over logs |
| [[beheerder logvoorziening]] | Inrichting en beschikbaarheid van de logging en de centrale opslag, het overzicht van logbronnen, steekproef op gevoelige gegevens |
| [[bewaking]] | Beoordelen van meldingen, detectieregels, escaleren volgens de regels, delen van nieuwe dreigingen, maandrapportage |
| CISO | Vaststellen van escalatieregels en toetsfrequentie, ontvangst van escalaties, opdracht tot de onafhankelijke toets, beoordeling van afwijkingen |
| Privacy officer en FG | Toetsing van het gebruik van logging met persoonsgegevens (de FG houdt toezicht) |
| Inkoop en contractbeheer | Vastleggen van de logeisen bij leveranciers en toetsen van hun verklaringen |

## 7. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in [[registratie van controles: het systeem waarin controles worden vastgelegd, bijvoorbeeld het ticketsysteem of het managementsysteem]];
afwijkingen gaan als bevinding naar het risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| LOG-01 | Elke logbron uit het overzicht logt daadwerkelijk en komt in de centrale opslag binnen; elk productiesysteem staat in het overzicht | [[beheerder logvoorziening]] | Per kwartaal | Vergelijking van het overzicht met de centrale logvoorziening en de configuratiedatabase, met de afwijkingen | 8.15.03, 8.15.05 |
| LOG-02 | Een steekproef van logregels uit vijf systemen bevat de verplichte velden, dezelfde tijdbron en geen wachtwoorden of sleutels | [[beheerder logvoorziening]] | Jaarlijks | Steekproefverslag met de beoordeelde logregels | 8.15.01, 8.15.02 |
| LOG-03 | De bewaartermijn per logbron is vastgesteld, wordt gehaald en logging met persoonsgegevens staat in het verwerkingsregister | Privacy officer | Jaarlijks | Overzicht van logbronnen met termijnen, rapport uit de logvoorziening over de oudste beschikbare regel, verwerkingsregister | 8.15.04 |
| LOG-04 | De logbestanden zijn over de bewaartermijn ongewijzigd en volledig aanwezig, getoetst door iemand zonder beheerrechten op de logging | Onafhankelijke toetser aangewezen door de CISO | Jaarlijks | Toetsverslag | 8.15.05, 8.15.06 |
| LOG-05 | Meldingen uit de detectievoorziening zijn binnen de termijn per ernstniveau beoordeeld en de detectieregels zijn na incidenten bijgewerkt | CISO | Per kwartaal | Maandrapportages, steekproef van meldingen met beoordelingstijd, wijzigingslog van detectieregels | 8.16.03, 8.16.04 |
| LOG-06 | De escalatie werkt: een gesimuleerde melding met ernst hoog bereikt de CISO binnen de afgesproken termijn | CISO | Jaarlijks | Tijdlijn van melding tot management | 8.16.02 |
| LOG-07 | Nieuwe dreigingen die bij de monitoring zijn ontdekt, zijn volgens de procedure met de CERT gedeeld | CISO | Jaarlijks | Registratie van gedeelde dreigingen, procedure | 8.16.01 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De
systeemeigenaar dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de looptijd.
De afwijking geldt pas na acceptatie van het risico door [[risico-eigenaar: de manager die restrisico's accepteert]]
en staat in het risicoregister; afwijkingen worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 8. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid
beveiligingsincidenten (melden van incidenten en bewaren van bewijs), het beleid netwerkbeveiliging
(bewaking van dataverkeer en tijdsynchronisatie), het beleid logische toegangsbeveiliging (logging van
beheerrechten en systeemhulpmiddelen), het beleid informatieclassificatie (impactniveaus en labels), het
beleid wijzigingsbeheer (ingebruikname van logbronnen), het beleid informatiebeveiliging bij inkoop en
contractbeheer (logs van leveranciers) en het privacybeleid (logging met persoonsgegevens).
