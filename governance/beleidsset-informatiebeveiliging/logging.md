# Beleid logging en monitoring

| | |
|---|---|
| Documenttype | Beleid informatiebeveiliging onder het strategisch informatiebeveiligingsbeleid; BIO 2.0-domein *Logging & monitoring* |
| Status | Concept, vast te stellen door de organisatie |
| Eigenaar | **[eigenaar van dit beleid]** |
| Vaststeller | **[vaststeller]** |
| Evaluatie | Jaarlijks, in de plan-do-check-act-cyclus van het managementsysteem voor informatiebeveiliging |

Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.

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

## 3. Beleidsregels

### 3.1 Wat er gelogd wordt

1. De systeemeigenaar zorgt dat elk systeem ten minste logt: aanmeldingen en mislukte aanmeldpogingen, het
   gebruik van beheerrechten, wijzigingen in accounts en rechten, wijzigingen in de beveiligingsinstellingen,
   het starten en stoppen van de logging zelf, en de toegang tot gegevens met het label vertrouwelijk of
   hoger. [8.15.01]
2. Elke logregel bevat: de handeling, het object waarop de handeling betrekking had, het resultaat, het
   apparaat of netwerkadres van herkomst, de persoon of het proces dat de handeling startte, en datum en
   tijd. Alle systemen gebruiken dezelfde tijdbron. [8.15.01]
3. Logregels bevatten geen wachtwoorden, sessietokens, sleutels of andere gegevens waarmee de beveiliging
   kan worden doorbroken. Bij de ingebruikname van een nieuwe logbron controleert
   **[beheerder logvoorziening]** een steekproef
   van de logregels hierop en legt de uitkomst vast. [8.15.02]
4. **[beheerder logvoorziening]** houdt een overzicht bij van alle logbronnen: per systeem welke gebeurtenissen
   worden gelogd, waar de logbestanden staan, de bewaartermijn, wie ze beheert en wie ze beoordeelt. Een
   nieuw systeem gaat pas in productie als het in dit overzicht staat; wijzigingsbeheer controleert dat bij
   elke ingebruikname. [8.15.03]

> **Alleen als: Waar draaien je systemen? «Vooral SaaS en publieke cloud»**
>
> 5. Voor SaaS- en clouddiensten legt de organisatie bij inkoop in het contract vast welke auditlogs de
>    leverancier beschikbaar stelt, hoe lang die bewaard blijven en hoe de organisatie ze kan exporteren naar
>    de eigen centrale logvoorziening. Waar de leverancier de logs korter bewaart dan de eigen termijn, haalt
>    **[beheerder logvoorziening]** ze zelf op. [8.15.03, 8.15.04]

> **Alleen als: Waar draaien je systemen? «Hostingpartij (IaaS, gedeeld datacenter)»**
>
> 6. Bij een hostingpartij logt de organisatie zelf op het niveau van besturingssysteem en applicatie. De
>    logging van de platformlaag (hypervisor, beheerportaal, netwerk van de hostingpartij) levert de
>    hostingpartij op verzoek binnen de termijn uit het contract. [8.15.03]

> **Alleen als: Waar draaien je systemen? «Eigen datacenter of serverruimte»**
>
> 7. In het eigen datacenter verzamelt een centrale logvoorziening de logging van servers, opslag,
>    virtualisatie en netwerkcomponenten. De logvoorziening staat in een eigen beheersegment. [8.15.03]

> **Alleen als: Verwerk je politiegegevens (boa's, opsporing, handhaving)? «Ja»**
>
> 8. Voor systemen met politiegegevens logt de organisatie elke raadpleging en elke verstrekking, met de
>    persoon die raadpleegt en, waar het systeem dat toelaat, het doel van de raadpleging. Deze logging is
>    nodig voor de verantwoording onder de Wpg. [8.15.01, 8.15.03]

> **Alleen als: Op welke landelijke voorzieningen ben je aangesloten? «DigiD» of «Suwinet» of «BRP (als bronhouder of afnemer)» of «BAG of andere basisregistraties» of «Andere ketens met eigen beveiligingseisen»**
>
> 9. Voor de aansluiting op landelijke voorzieningen volgt de systeemeigenaar bovendien de logeisen uit het
>    normenkader van die voorziening en staan de betreffende systemen apart in het overzicht van logbronnen,
>    met het normenkader erbij. [8.15.03]

### 3.2 Bewaren en beschermen

1. De bewaartermijn per logbron staat in het overzicht en volgt uit een risicoafweging door de
   systeemeigenaar. Omdat aanvallers vaak maanden onopgemerkt in een omgeving zitten, is de termijn voor
   beveiligingsrelevante logging en voor de gegevens in het SIEM ten minste
   **[bewaartermijn beveiligingslogging]**.
   Logging die bij een incident hoort, valt onder de termijn van het incidentdossier (drie jaar). [8.15.04]
2. Logging die persoonsgegevens bevat, wordt niet langer bewaard dan de vastgestelde termijn en alleen
   gebruikt voor beveiliging, beheer en verantwoording. De verwerking staat in het verwerkingsregister; de
   privacy officer toetst dat jaarlijks. [8.15.04]
3. **[beheerder logvoorziening]** kopieert logbestanden zo snel mogelijk na het ontstaan naar een centrale
   opslag waar de beheerders van het bronsysteem geen schrijf- of verwijderrechten hebben. [8.15.05]
4. Een poging om loggegevens oneigenlijk te wijzigen of te verwijderen, of het onverwacht stoppen van de
   logging, wordt direct als beveiligingsincident gemeld via de incidentprocedure. De centrale
   logvoorziening geeft hierop een automatische melding aan **[bewaking]**. [8.15.05]
5. Op basis van een risicoafweging stelt de CISO vast hoe vaak wordt getoetst dat de logbestanden
   gedurende de bewaartermijn ongewijzigd en volledig aanwezig zijn, met ten minste een jaarlijkse toets.
   De toets wordt uitgevoerd door iemand die geen beheertaken heeft op de logvoorziening of de
   bronsystemen. [8.15.06]

> **Alleen als: Welke eigen security-capaciteit heb je? «Geen eigen ISO; informatiebeveiliging is een neventaak» of «Een ISO of CISO in deeltijd»**
>
> 6. De organisatie heeft geen eigen team dat onafhankelijk is van het beheer. De toets op ongewijzigde
>    logbestanden laat zij uitvoeren door een externe auditor of door de interne controle. [8.15.06]

> **Alleen als: Welke eigen security-capaciteit heb je? «Een eigen team (CISO met ISO's)»**
>
> 7. De toets op ongewijzigde logbestanden voert een ISO uit die geen beheerrechten heeft op de logging. [8.15.06]

> **Alleen als: Verwerk je politiegegevens (boa's, opsporing, handhaving)? «Ja»**
>
> 8. De logging van systemen met politiegegevens wordt bewaard volgens de termijn uit de Wpg en is onderwerp
>    van de periodieke Wpg-audit. Alleen de privacy officer, de CISO en de functionaris die de Wpg-controle
>    uitvoert, mogen deze logging raadplegen; elke raadpleging wordt zelf ook gelogd. [8.15.04, 8.15.05]

### 3.3 Monitoren en detecteren

1. De organisatie bewaakt de omgeving met een detectie- en responsvoorziening die de logging van
   werkplekken, servers, identiteiten, clouddiensten en netwerkcomponenten bij elkaar brengt, bijvoorbeeld
   een SIEM met EDR. **[bewaking]** beoordeelt afwijkingen binnen de termijn per ernstniveau en legt de
   beoordeling vast. [8.16.03]
2. Actieve netwerkcomponenten (firewalls, routers, switches, toegangspunten voor wifi en VPN) sturen hun
   logging naar deze voorziening. **[bewaking]** onderhoudt detectieregels voor afwijkend gedrag zoals
   ongebruikelijk verkeer, wijzigingen in de configuratie en aanmeldingen buiten de beheerroute. [8.16.04]
3. De CISO legt vaste regels vast over wanneer een melding als incident aan het management gaat: per
   ernstniveau de termijn en de ontvanger. Een melding met ernst hoog of kritiek gaat altijd direct naar de
   CISO, die bepaalt of de directie wordt ingelicht. [8.16.02]
4. Nieuwe dreigingen of aanvalstechnieken die bij de monitoring worden ontdekt, deelt **[bewaking]** binnen
   de juridische kaders met de aangewezen CERT, zo nodig zonder persoonsgegevens, en legt vast wat is
   gedeeld. [8.16.01]
5. **[bewaking]** rapporteert maandelijks aan de CISO over meldingen, escalaties en gedeelde dreigingen.
   [8.16.02, 8.16.03]

> **Alleen als: Wie bewaakt je omgeving op aanvallen? «Eigen SOC»**
>
> 6. Het eigen SOC beoordeelt de meldingen uit de detectievoorziening, ook buiten kantoortijd via een
>    bereikbaarheidsdienst. Het SOC beheert de detectieregels en past ze aan na elk incident en na elke
>    relevante dreigingsmelding. [8.16.03, 8.16.04]
> 7. Het SOC heeft een vastgelegde procedure voor het delen van nieuwe dreigingen met de CERT. [8.16.01]

> **Alleen als: Wie bewaakt je omgeving op aanvallen? «Uitbesteed SOC of MDR-dienst»**
>
> 8. Een SOC- of MDR-dienstverlener bewaakt de omgeving. Het contract regelt: welke logbronnen zijn
>    aangesloten, de reactietijd per ernstniveau, de escalatie naar de organisatie, de bevoegdheid om in te
>    grijpen, het delen van nieuwe dreigingen met de CERT en een maandelijkse rapportage. [8.16.01, 8.16.02, 8.16.03]
> 9. **[beheerder logvoorziening]** controleert elk kwartaal of alle logbronnen uit het overzicht ook bij de
>    dienstverlener binnenkomen en legt de uitkomst vast. [8.16.03, 8.16.04]

> **Alleen als: Wie bewaakt je omgeving op aanvallen? «Geen structurele detectie»**
>
> 10. Er is nog geen structurele detectie. Als minimum zijn op werkplekken en servers detectie- en
>    responsfuncties actief met automatische meldingen aan de beheerder, die ze elke werkdag bekijkt. De CISO
>    neemt het ontbreken van een SOC op als risico in het risicoregister en legt in het jaarplan vast wanneer de
>    organisatie structurele detectie heeft ingericht, zelf of uitbesteed. [8.16.03, 8.16.04]

> **Alleen als: Waar draaien je systemen? «Vooral SaaS en publieke cloud» of «Hostingpartij (IaaS, gedeeld datacenter)»**
>
> 11. De logging van clouddiensten en van de hostingpartij is aangesloten op de detectievoorziening. Waar dat
>    technisch niet kan, legt de systeemeigenaar vast welke meldingen de leverancier zelf geeft en hoe snel.
>    [8.16.03]

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| **[lijneigenaar logging]** | Eigenaar van dit beleid, de centrale logvoorziening en de contracten met de SOC-dienstverlener |
| Systeemeigenaar | Bepalen wat er van zijn systeem wordt gelogd en hoe lang, opname in het overzicht van logbronnen, afspraken met leveranciers over logs |
| **[beheerder logvoorziening]** | Inrichting en beschikbaarheid van de logging en de centrale opslag, het overzicht van logbronnen, steekproef op gevoelige gegevens |
| **[bewaking]** | Beoordelen van meldingen, detectieregels, escaleren volgens de regels, delen van nieuwe dreigingen, maandrapportage |
| CISO | Vaststellen van escalatieregels en toetsfrequentie, ontvangst van escalaties, opdracht tot de onafhankelijke toets, beoordeling van afwijkingen |
| Privacy officer en FG | Toetsing van het gebruik van logging met persoonsgegevens (de FG houdt toezicht) |
| Inkoop en contractbeheer | Vastleggen van de logeisen bij leveranciers en toetsen van hun verklaringen |

## 5. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in **[registratie van controles]**;
afwijkingen gaan als bevinding naar het risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| LOG-01 | Elke logbron uit het overzicht logt daadwerkelijk en komt in de centrale opslag binnen; elk productiesysteem staat in het overzicht | **[beheerder logvoorziening]** | Per kwartaal | Vergelijking van het overzicht met de centrale logvoorziening en de configuratiedatabase, met de afwijkingen | 8.15.03, 8.15.05 |
| LOG-02 | Een steekproef van logregels uit vijf systemen bevat de verplichte velden, dezelfde tijdbron en geen wachtwoorden of sleutels | **[beheerder logvoorziening]** | Jaarlijks | Steekproefverslag met de beoordeelde logregels | 8.15.01, 8.15.02 |
| LOG-03 | De bewaartermijn per logbron is vastgesteld, wordt gehaald en logging met persoonsgegevens staat in het verwerkingsregister | Privacy officer | Jaarlijks | Overzicht van logbronnen met termijnen, rapport uit de logvoorziening over de oudste beschikbare regel, verwerkingsregister | 8.15.04 |
| LOG-04 | De logbestanden zijn over de bewaartermijn ongewijzigd en volledig aanwezig, getoetst door iemand zonder beheerrechten op de logging | Onafhankelijke toetser aangewezen door de CISO | Jaarlijks | Toetsverslag | 8.15.05, 8.15.06 |
| LOG-05 | Meldingen uit de detectievoorziening zijn binnen de termijn per ernstniveau beoordeeld en de detectieregels zijn na incidenten bijgewerkt | CISO | Per kwartaal | Maandrapportages, steekproef van meldingen met beoordelingstijd, wijzigingslog van detectieregels | 8.16.03, 8.16.04 |
| LOG-06 | De escalatie werkt: een gesimuleerde melding met ernst hoog bereikt de CISO binnen de afgesproken termijn | CISO | Jaarlijks | Tijdlijn van melding tot management | 8.16.02 |
| LOG-07 | Nieuwe dreigingen die bij de monitoring zijn ontdekt, zijn volgens de procedure met de CERT gedeeld | CISO | Jaarlijks | Registratie van gedeelde dreigingen, procedure | 8.16.01 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De
systeemeigenaar dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de looptijd.
De afwijking geldt pas na acceptatie van het risico door **[risico-eigenaar]**
en staat in het risicoregister; afwijkingen worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid
beveiligingsincidenten (melden van incidenten en bewaren van bewijs), het beleid netwerkbeveiliging
(bewaking van dataverkeer en tijdsynchronisatie), het beleid logische toegangsbeveiliging (logging van
beheerrechten en systeemhulpmiddelen), het beleid informatieclassificatie (impactniveaus en labels), het
beleid wijzigingsbeheer (ingebruikname van logbronnen), het beleid informatiebeveiliging bij inkoop en
contractbeheer (logs van leveranciers) en het privacybeleid (logging met persoonsgegevens).

## Bijlage A: BIO 2.0-maatregelen

De maatregelen van dit domein (10, waarvan 10 overheidsmaatregelen), waar dit stuk ze invult en welke controle ze aantoont. Nummers volgens BIO2 v1.3 definitief - 9 januari 2026; de tekst van de maatregel staat bij het CIP. Waar de BIO 2.0 geen overheidsmaatregel kent, geldt de ISO 27002-beheersmaatregel.

| Maatregel | Titel | Soort | In dit stuk | Controle |
|---|---|---|---|---|
| 8.15.01 | Logging | overheidsmaatregel | 3.1 Wat er gelogd wordt | LOG-02 |
| 8.15.02 | Logging | overheidsmaatregel | 3.1 Wat er gelogd wordt | LOG-02 |
| 8.15.03 | Logging | overheidsmaatregel | 3.1 Wat er gelogd wordt | LOG-01 |
| 8.15.04 | Logging | overheidsmaatregel | 3.1 Wat er gelogd wordt | LOG-03 |
| 8.15.05 | Logging | overheidsmaatregel | 3.2 Bewaren en beschermen | LOG-01, LOG-04 |
| 8.15.06 | Logging | overheidsmaatregel | 3.2 Bewaren en beschermen | LOG-04 |
| 8.16.01 | Monitoren van activiteiten | overheidsmaatregel | 3.3 Monitoren en detecteren | LOG-07 |
| 8.16.02 | Monitoren van activiteiten | overheidsmaatregel | 3.3 Monitoren en detecteren | LOG-06 |
| 8.16.03 | Monitoren van activiteiten | overheidsmaatregel | 3.3 Monitoren en detecteren | LOG-05 |
| 8.16.04 | Monitoren van activiteiten | overheidsmaatregel | 3.3 Monitoren en detecteren | LOG-05 |

## Bijlage B: Afkortingen

| Afkorting | Betekenis |
|---|---|
| BAG | Basisregistratie Adressen en Gebouwen |
| BRP | Basisregistratie Personen |
| CERT | Computer emergency response team |
| CISO | Chief Information Security Officer |
| EDR | Endpoint detection and response |
| FG | Functionaris gegevensbescherming |
| ISAE | International Standard on Assurance Engagements |
| ISO | International Organization for Standardization |
| IaaS | Infrastructure as a service |
| MDR | Managed detection and response |
| SIEM | Security information and event management |
| SOC | Security operations center |
| SaaS | Software as a service |
| VPN | Virtual private network |
| Wpg | Wet politiegegevens |

## Nog in te vullen

- **beheerder logvoorziening**: de afdeling of leverancier die de centrale logging beheert
- **bewaartermijn beveiligingslogging**: de minimale termijn, bijvoorbeeld twaalf maanden
- **bewaking**: het eigen SOC, de SOC-dienstverlener of de beheerder die de meldingen beoordeelt
- **lijneigenaar logging**: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd IT
- **registratie van controles**: het systeem waarin controles worden vastgelegd, bijvoorbeeld het ticketsysteem of het managementsysteem
- **risico-eigenaar**: de manager die restrisico's accepteert
- **eigenaar van dit beleid**: de manager die dit beleid uitvoert en laat naleven
- **vaststeller**: wie het beleid vaststelt, bijvoorbeeld de directie of het bestuur
