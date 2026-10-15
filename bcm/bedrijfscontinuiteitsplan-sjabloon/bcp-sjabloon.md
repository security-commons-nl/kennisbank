# Bedrijfscontinuïteitsplan (BCP)

**[Naam organisatie of organisatieonderdeel]** · sjabloon · de toelichting staat in de [README](README.md)

| | |
|---|---|
| **Organisatieonderdeel** | [naam] |
| **Plan-eigenaar** | [functie] |
| **Versie en datum** | [versie] · [datum] |
| **Rubricering** | [volgens het eigen classificatiebeleid; een BCP met bereikbaarheidsgegevens is in de regel vertrouwelijk] |
| **Volgende toets** | [datum, uiterlijk twaalf maanden na vaststelling] |
| **Vastgesteld door** | [ambtelijk eindverantwoordelijke: gemeentesecretaris, provinciesecretaris, secretaris-directeur, secretaris-generaal of directeur] op [datum] |

## Hoe dit plan werkt

Dit plan is een werkdocument voor het moment dat een kritieke dienst uitvalt of dreigt uit te vallen. Het is
geschreven om uitgeprint te gebruiken: op de dag zelf is de ICT misschien precies wat niet werkt.

Het plan heeft drie delen:

1. **Weten** (hoofdstuk 1 en 2): wie het crisisteam vormt en welke diensten voorrang hebben.
2. **Doen** (hoofdstuk 3 tot en met 6): opschaling, de drie fasen van een verstoring, de scenario's en de
   noodcommunicatie.
3. **Onderhouden** (hoofdstuk 7 en 8): oefenen, beheer en de verplichtingen waar het plan aan voldoet.

De bijlagen zijn de formulieren voor de dag zelf: de bereikbaarheidslijst, het logboek, de crisiskoffer en de
actiekaarten.

Houd een actueel exemplaar op drie plaatsen: in de crisiskoffer, bij elk lid van het crisisteam buiten de
eigen ICT, en op de uitwijklocatie. Het plan hoort bij het calamiteitenplan van het gebouw en bij de
crisisorganisatie van de organisatie; wat daar geregeld is, herhaalt dit plan niet.

## 1. Crisisteam

### 1.1 Samenstelling

| Rol | Naam | Plaatsvervanger | Bereikbaar via (buiten de eigen ICT) |
|---|---|---|---|
| Voorzitter crisisteam | | | |
| Secretaris en logboek | | | |
| Bedrijfsvoering en huisvesting | | | |
| ICT (eigen ICT en dienstverlener) | | | |
| Informatiebeveiliging (CISO) | | | |
| Communicatie en woordvoering | | | |
| HR (medewerkers) | | | |
| Juridische zaken en inkoop (contracten) | | | |
| Eigenaar van de getroffen dienst | | | |
| Verbinding met de crisisorganisatie | | | |

Wie hier zit, kan niet tegelijk een rol in de bredere crisisorganisatie vervullen. Loop dat vooraf na.

### 1.2 Taken van het crisisteam

1. Vaststellen wat er aan de hand is, welke diensten geraakt zijn en of het plan wordt geactiveerd.
2. De volgorde van herstel bepalen aan de hand van tabel 1 (kritieke diensten).
3. Besluiten over uitwijk, noodstroom, terugvalprocedures en de inzet van medewerkers.
4. De wettelijke meldingen laten doen (hoofdstuk 6.2).
5. Informeren: medewerkers, ketenpartners, het bestuur via de lijn, en bij opschaling de crisisorganisatie.
6. Het logboek bijhouden (bijlage 2): elk besluit, elke actie, elk contact, met tijd en naam.
7. Afschalen zodra het noodniveau stabiel is, en de evaluatie organiseren.

### 1.3 Vergaderplaats

| | Locatie | Adres en toegang | Voorzieningen |
|---|---|---|---|
| Eerste keus | | | |
| Uitwijk (ander kantoor, buurorganisatie, of online buiten de eigen ICT) | | | |

## 2. Kritieke diensten

### Tabel 1: diensten in volgorde van herstel

Vul deze tabel vanuit de business impact analyse (BIA); het [BIA-sjabloon](../bia-en-risicoanalyse-sjabloon/)
levert precies deze kolommen.

| Nr | Dienst of proces | Eigenaar | Kriticiteit | MTPD | RTO | RPO | Noodniveau (wat minimaal door moet) |
|---|---|---|---|---|---|---|---|
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |
| 6 | | | | | | | |

MTPD: maximaal toelaatbare uitvalduur. RTO: binnen hoeveel tijd de dienst op noodniveau terug moet zijn. RPO:
hoeveel gegevensverlies aanvaardbaar is; dat stuurt de back-upfrequentie (BIO2 8.13).

### Tabel 2: wat elke dienst nodig heeft

| Nr | Dienst | Medewerkers (aantal, rollen) | Systemen en gegevens | Huisvesting en werkplekken | Leveranciers en ketenpartners | Enkelvoudige afhankelijkheid? |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |

De laatste kolom is de belangrijkste. Een dienst die op een persoon, een systeem of een leverancier drijft, is
de dienst waar het plan het eerst over gaat.

## 3. Opschaling en activering

### 3.1 Wie meldt, wie besluit

1. Iedere medewerker die een verstoring ziet die een kritieke dienst raakt, meldt dit bij [servicedesk of
   piketnummer]. Bij levensgevaar eerst 112, dan de BHV.
2. De piketfunctionaris beoordeelt binnen [30 minuten] met de eigenaar van de dienst of de verstoring de MTPD
   van een dienst in tabel 1 kan raken.
3. Is dat zo, dan belt de piketfunctionaris de voorzitter van het crisisteam. Die besluit of het plan wordt
   geactiveerd en roept het crisisteam bijeen, in persoon of via het noodcommunicatiekanaal.
4. De voorzitter informeert de ambtelijk eindverantwoordelijke (als die niet zelf voorzit) en de
   crisisorganisatie.

### 3.2 Drempels

| Niveau | Wanneer | Wie stuurt |
|---|---|---|
| Verstoring | Een dienst hapert, herstel binnen de RTO is waarschijnlijk | Eigenaar van de dienst met ICT |
| Activering BCP | De RTO van een dienst in tabel 1 komt in gevaar, of meerdere diensten zijn geraakt | Crisisteam |
| Opschaling | De uitval raakt de samenleving, andere overheden of de media | Crisisteam met de crisisorganisatie: [gemeente en provincie: de eigen crisisorganisatie, zo nodig de veiligheidsregio · Rijk: het departementaal coördinatiecentrum crisisbeheersing] |

De meldplicht loopt los van deze drempels; zie hoofdstuk 6.2.

## 4. De drie fasen

### Fase 1: acute fase (eerste 24 uur)

| Nr | Actie | Toelichting | Gedaan | Door |
|---|---|---|---|---|
| 1 | Eerste beeld: wat is uitgevallen, sinds wanneer, wie is geraakt | | | |
| 2 | Veiligheid van medewerkers en bezoekers | Via BHV en calamiteitenplan | | |
| 3 | Logboek openen | Bijlage 2, vanaf het eerste telefoontje | | |
| 4 | Crisisteam bijeen, rollen bevestigen | Tabel 1.1 | | |
| 5 | Diensten in tabel 1 langslopen: wat loopt, wat niet, wat dreigt | | | |
| 6 | Besluit over uitwijk, noodstroom en terugvalprocedures | Hoofdstuk 5 | | |
| 7 | Vroegtijdige melding significant incident (24 uur) | Hoofdstuk 6.2 | | |
| 8 | Eerste bericht aan medewerkers en ketenpartners | Hoofdstuk 6, via noodcommunicatie | | |
| 9 | Informatiebeveiliging tijdens de verstoring: wie heeft nu toegang tot wat | BIO2 5.29 | | |
| 10 | Volgend overleg plannen, vast ritme (bijvoorbeeld elke drie uur) | | | |

### Fase 2: continuïteitsfase (noodbedrijf)

| Nr | Actie | Toelichting | Gedaan | Door |
|---|---|---|---|---|
| 1 | Diensten op noodniveau brengen, in de volgorde van tabel 1 | | | |
| 2 | Terugvalmaatregelen per scenario uitvoeren | Hoofdstuk 5 | | |
| 3 | Inzet van medewerkers regelen: wie werkt waar, roosters, rust | | | |
| 4 | Leveranciers en ketenpartners aansturen op hun herstel | Escalatiecontacten in bijlage 1 | | |
| 5 | Incidentmelding (72 uur) | Hoofdstuk 6.2 | | |
| 6 | Dagelijks bericht aan medewerkers, ketenpartners en zo nodig het publiek | | | |
| 7 | Kosten en besluiten vastleggen voor de verantwoording achteraf | Logboek | | |

### Fase 3: herstel en terugkeer naar normaal bedrijf

| Nr | Actie | Toelichting | Gedaan | Door |
|---|---|---|---|---|
| 1 | Volgorde van terugkeer bepalen (niet per se dezelfde als de herstelvolgorde) | | | |
| 2 | Gegevens inhalen en controleren die tijdens het noodbedrijf buiten de systemen zijn vastgelegd | | | |
| 3 | Terugkeer naar de eigen locatie en systemen, met controle vooraf | | | |
| 4 | Afschaling: besluit van de voorzitter, melding aan crisisorganisatie en ketenpartners | | | |
| 5 | Eindverslag van het incident | Hoofdstuk 6.2 | | |
| 6 | Evaluatie binnen [vier weken]: wat werkte, wat niet, welke wijziging in dit plan | Hoofdstuk 7 | | |
| 7 | Nazorg voor medewerkers | HR | | |

## 5. Scenario's en terugvalmaatregelen

Per scenario: wat er dan in gang gaat en wie dat doet. Vul alleen in wat voor de eigen organisatie geldt en
schrap de rest.

### 5.1 Uitval van medewerkers

| Terugvalmaatregel | Ingeregeld? | Toelichting |
|---|---|---|
| Vervangers per kritieke rol (minimaal twee diep) | | |
| Thuiswerken | | |
| Tijdelijke inhuur en herverdeling van taken | | |
| Werkinstructies voor kritieke taken op papier beschikbaar | | |

### 5.2 Uitval van de huisvesting

| Terugvalmaatregel | Ingeregeld? | Toelichting |
|---|---|---|
| Uitwijklocatie voor het crisisteam (adres, toegang, afspraak) | | |
| Uitwijklocatie voor de kritieke diensten (aantal werkplekken, binnen hoeveel uur) | | |
| Thuiswerken als uitwijk | | |
| Post, archief en fysieke middelen | | |

### 5.3 Uitval van nutsvoorzieningen (stroom, water, klimaat)

| Terugvalmaatregel | Ingeregeld? | Toelichting |
|---|---|---|
| Noodstroom: welke systemen hangen eraan, hoeveel uur, wie test het | | |
| Afspraak met de gebouwbeheerder over brandstof en onderhoud | | |
| Wat er gebeurt als de noodstroom op is (gecontroleerd afschakelen) | | |

### 5.4 ICT-uitval (systemen, netwerk, telefonie, cyberaanval)

| Terugvalmaatregel | Ingeregeld? | Toelichting |
|---|---|---|
| Uitwijkvoorziening ICT per kritieke dienst (zie de [uitwijkkaart](../uitwijk-regelen/uitwijkkaart.md)) | | |
| Back-up en herstel getest tegen de RPO en RTO uit tabel 1 (BIO2 8.13) | | |
| Terugvalprocedures op papier voor de kritieke diensten | | |
| Isolatie en herstel bij een cyberaanval, met het CSIRT en de dienstverlener | | |
| Werkende communicatie buiten de eigen ICT (hoofdstuk 6) | | |

### 5.5 Uitval van een leverancier of ketenpartner

| Terugvalmaatregel | Ingeregeld? | Toelichting |
|---|---|---|
| Per kritieke leverancier: continuïteitseisen in het contract, escalatiecontact, exitplan | | |
| Alternatieve leverancier of handmatige werkwijze | | |
| Afspraken met ketenpartners over elkaars uitval (ketenoefening) | | |

### 5.6 Fysieke dreiging, ontruiming, verdachte post

Staat in het calamiteitenplan en het BHV-plan van het gebouw: [verwijzing]. Dit BCP regelt alleen wat daarna
nodig is om de dienst door te laten lopen.

## 6. Noodcommunicatie en meldingen

### 6.1 Kanalen

| Doel | Kanaal | Werkt zonder de eigen ICT? | Beheerder |
|---|---|---|---|
| Alarmeren crisisteam | | | |
| Berichten aan alle medewerkers | | | |
| Contact met de crisisorganisatie | | | |
| Contact met ketenpartners en leveranciers | | | |
| Contact met het CSIRT en de bevoegde autoriteit | | | |
| Publiek en media | Woordvoering | | |

Minstens een kanaal moet werken als de eigen mail, telefonie en het netwerk uitvallen. Test dat kanaal bij
elke oefening.

### 6.2 Meldingen die de wet voorschrijft

| Melding | Termijn | Aan wie | Wie doet het |
|---|---|---|---|
| Vroegtijdige waarschuwing significant incident (Cbw) | 24 uur na kennisname | CSIRT en de bevoegde autoriteit van de sector [invullen] | |
| Incidentmelding (Cbw) | 72 uur na kennisname | CSIRT en bevoegde autoriteit | |
| Eindverslag (Cbw) | Een maand na de incidentmelding | CSIRT en bevoegde autoriteit | |
| Melding verstoring (Wwke, alleen na aanwijzing als kritieke entiteit) | [termijn uit de aanwijzing] | [bevoegde autoriteit] | |
| Datalek (AVG) | 72 uur | Autoriteit Persoonsgegevens, via de FG | |
| Interne lijn | Direct | Ambtelijk eindverantwoordelijke, bestuur, crisisorganisatie | |

Welke organisaties onder de Cbw vallen en wie hun bevoegde autoriteit is, staat in
[val ik onder de Cbw](../../governance/val-ik-onder-de-cbw/).

### 6.3 Kernboodschappen

Zet hier drie standaardberichten klaar die alleen nog ingevuld hoeven te worden: aan medewerkers, aan
ketenpartners en aan het publiek. Wat is er aan de hand, wat doen we, wat vragen we van u, wanneer volgt het
volgende bericht.

## 7. Opleiden, trainen en oefenen (OTO) en beheer

| Activiteit | Frequentie | Verantwoordelijk | Laatst gedaan |
|---|---|---|---|
| Briefing nieuwe leden crisisteam | Bij aantreden | Plan-eigenaar | |
| Tafeloefening crisisteam op een scenario uit hoofdstuk 5 | Jaarlijks | Plan-eigenaar | |
| Hersteltest ICT tegen RTO en RPO | Jaarlijks, per kritiek systeem | ICT | |
| Test van het noodcommunicatiekanaal | Halfjaarlijks | Beheerder kanaal | |
| Ketenoefening met een of meer ketenpartners | Tweejaarlijks | Eigenaar dienst | |
| Toets van dit plan en de bijlagen | Jaarlijks en na elke activering | Plan-eigenaar | |
| Training van het bestuur (Cbw) | [volgens de regels die daarvoor gelden] | [CISO of bestuursondersteuning] | |

De plan-eigenaar houdt het plan actueel en legt elke wijziging vast in de versietabel voorin. De
bereikbaarheidslijst (bijlage 1) wordt elk kwartaal gecontroleerd.

## 8. Waar dit plan aan voldoet

| Verplichting | Bron | Waar in dit plan |
|---|---|---|
| Zorgplicht met passende maatregelen, inclusief de keten | Cbw artikel 21; BIO2 5.19 tot en met 5.23 | Hoofdstuk 2 en 5.5 |
| Goedkeuring van de maatregelen en training door het bestuur | Cbw artikel 24 | Voorblad en hoofdstuk 7 |
| Melding van significante incidenten | Cbw | Hoofdstuk 6.2 |
| Crisismanagementplan en bedrijfscontinuïteitsplan, inclusief oefenen | Wwke en het besluit daaronder (na aanwijzing) | Dit plan en hoofdstuk 7 |
| Informatiebeveiliging tijdens een verstoring | BIO2 5.29 | Fase 1, actie 9 |
| ICT-gereedheid voor bedrijfscontinuïteit | BIO2 5.30 | Hoofdstuk 5.4 en 7 |
| Back-up | BIO2 8.13 | Tabel 1 (RPO) en 5.4 |
| Redundantie van ICT-voorzieningen | BIO2 8.14 | Hoofdstuk 5.3 en 5.4 |

## Bijlage 1: Bereikbaarheidslijst

Alleen op papier in de crisiskoffer en bij de leden van het crisisteam. Privénummers alleen met toestemming.

| Naam | Rol | Mobiel (werk) | Mobiel (privé, met toestemming) | Ander kanaal buiten de eigen ICT |
|---|---|---|---|---|
| | | | | |
| | | | | |
| | | | | |

| Externe partij | Contactpersoon | Nummer | Escalatie | Contract of afspraak |
|---|---|---|---|---|
| Crisisorganisatie | | | | |
| CSIRT | | | | |
| Bevoegde autoriteit en toezichthouder | | | | |
| ICT-dienstverlener | | | | |
| Gebouwbeheer en beveiliging | | | | |
| [leverancier 1] | | | | |
| [ketenpartner 1] | | | | |

## Bijlage 2: Logboek crisisteam

Begin bij het eerste telefoontje, een regel per gebeurtenis. Dit logboek is ook het bewijs voor de
verantwoording achteraf. Een uitgebreider logboekformat staat bij
[een digitaal calamiteitenteam opzetten](../calamiteitenteam-digitaal-opzetten/logboekformat.md).

| Datum en tijd | Gebeurtenis, besluit of actie | Wie | Vervolg of afgerond |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

## Bijlage 3: Crisiskoffer

Een fysiek exemplaar buiten het gebouw en een digitaal exemplaar buiten de eigen ICT. Controle elk kwartaal,
verantwoordelijk: [functie].

| Inhoud | Aanwezig | Laatst gecontroleerd |
|---|---|---|
| Dit plan, uitgeprint, met bijlagen | | |
| Bereikbaarheidslijst (bijlage 1) | | |
| Calamiteitenplan en plattegronden van het gebouw | | |
| Contracten en escalatiecontacten van kritieke leveranciers | | |
| Werkinstructies op papier voor de kritieke diensten | | |
| Logboekformulieren, pennen, hesjes voor het crisisteam | | |
| Toegangspassen en sleutels van de uitwijklocatie | | |
| Noodcommunicatiemiddelen (opgeladen, getest) | | |
| Laptop met offline toegang tot de terugvalprocedures | | |
| Betaalmiddel voor noodaankopen | | |

## Bijlage 4: Actiekaarten

Een kaart per rol in het crisisteam, een A4, bij de rol zelf en in de koffer. Uitgewerkte kaarten per rol
staan bij [een digitaal calamiteitenteam opzetten](../calamiteitenteam-digitaal-opzetten/taakkaarten.md).

| Actiekaart: [rol] | |
|---|---|
| Eerste uur | 1. [ ] 2. [ ] 3. [ ] |
| Eerste dag | 1. [ ] 2. [ ] 3. [ ] |
| Dagelijks tijdens het noodbedrijf | 1. [ ] 2. [ ] |
| Bij afschaling | 1. [ ] 2. [ ] |
| Wie ik bel | [namen uit bijlage 1] |
| Wat ik niet zelf besluit | [wat bij de voorzitter of de ambtelijk eindverantwoordelijke ligt] |
