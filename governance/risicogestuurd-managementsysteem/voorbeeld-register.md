# Voorbeeld: het register van gemeente Duinstad (verzonnen)

<!-- Gegenereerd door tools/bouw_risicoregister.py uit voorbeeld-register.json; niet met de hand bewerken. -->

Bijlage bij [GRC voor security, privacy en continuïteit](README.md). Gemeente Duinstad bestaat niet; alle risico's, bevindingen en getallen zijn verzonnen. De sleutels van de maatregelen zijn echt. Peildatum 01-10-2026. De gegevens staan in [`voorbeeld-register.json`](voorbeeld-register.json), de regels in [het model](model.md), en dezelfde uitkomst is door te klikken in [de verkenner](voorbeeld-register-verkenner.html).

**Stand.** 3 strategische risico's, 7 operationele risico's, 16 maatregelen, 3 controls en 6 bevindingen, waarvan 5 meetellen. 5 van de 7 operationele risico's hebben een aangetoond gat; de andere zijn niet beoordeeld.

## Prioriteit: wat eerst

De lijst die je aan de directie laat zien. Eerst de maatregelen onder een risico met een aangetoond gat, dan de rest op het gewicht van het strategische risico. Bij gelijke stand het laagste niveau eerst.

| # | Maatregel | Wat | Risico | Niveau | Bevinding | Waarom hier |
|---|---|---|---|---|---|---|
| 1 | BIO2:8.08.01 | Technische kwetsbaarheden tijdig signaleren | OR-01 | 0 · niet in orde | B-02 | OR-01 heeft een aangetoond gat (score 20) |
| 2 | BIO2:8.08.02 | Patches binnen de afgesproken termijn installeren | OR-01 | 2 · bestaan | B-02 | OR-01 heeft een aangetoond gat (score 20) |
| 3 | BCM:8.5 | Plannen oefenen en herstel testen | OR-02 | 0 · niet in orde | B-03 | OR-02 heeft een aangetoond gat (score 15) |
| 4 | BCM:8.4.4 | Continuïteitsplan per kritiek proces | OR-02 | 1 · opzet | B-03 | OR-02 heeft een aangetoond gat (score 15) |
| 5 | BCM:8.2.2 | Bedrijfsimpactanalyse van de kritieke processen | OR-02 | 2 · bestaan |  | OR-02 heeft een aangetoond gat (score 15) |
| 6 | BIO2:8.02.01 | Beheerrechten apart toekennen en beperken | OR-05 | 0 · niet in orde | B-05 | OR-05 heeft een aangetoond gat (score 12) |
| 7 | BIO2:8.16.01 | Afwijkend gedrag opsporen en opvolgen | OR-06 | 0 · niet in orde | B-05 | OR-06 heeft een aangetoond gat (score 12) |
| 8 | BIO2:5.15.01 | Toegangsbeleid vastgesteld en toegepast | OR-05 | 2 · bestaan |  | OR-05 heeft een aangetoond gat (score 12) |
| 9 | BIO2:5.18.01 | Toegangsrechten toekennen, herzien en intrekken | OR-05 | 2 · bestaan | B-01 | OR-05 heeft een aangetoond gat (score 12) |
| 10 | BIO2:8.15.01 | Gebeurtenissen vastleggen in logbestanden | OR-06 | 2 · bestaan |  | OR-06 heeft een aangetoond gat (score 12) |
| 11 | BIO2:8.05.01 | Sterke authenticatie voor toegang | OR-05 | 3 · werking |  | OR-05 heeft een aangetoond gat (score 12) |
| 12 | AVG:A12 | Betrokkenen tijdig en begrijpelijk informeren over hun verzoek | OR-03 | 1 · opzet | B-04 | OR-03 heeft een aangetoond gat (score 8) |
| 13 | AVG:A15 | Inzageverzoeken binnen de wettelijke termijn afhandelen | OR-03 | 2 · bestaan | B-04 | OR-03 heeft een aangetoond gat (score 8) |
| 14 | AVG:A29 | Verwerkers werken alleen in opdracht | OR-04 | 1 · opzet |  | OR-04 niet beoordeeld; gewicht van SR-02 (score 12) |
| 15 | AVG:A28 | Verwerkersovereenkomst met elke verwerker | OR-04 | 2 · bestaan |  | OR-04 niet beoordeeld; gewicht van SR-02 (score 12) |
| 16 | BIO2:7.02.01 | Fysieke toegang tot ruimtes met apparatuur | OR-07 | 2 · bestaan |  | OR-07 niet beoordeeld en buiten de SRA; laagste gewicht |

## Van strategisch risico naar maatregel

### SR-01 · Uitval van kritieke dienstverlening door een cyberaanval

Kans 4 × impact 5 = 20 (Kritiek).

- **OR-01** Bekende kwetsbaarheden in systemen worden te laat verholpen · BIO 2.0, ISO 27002 8.8 · score 20 (Kritiek)
  - BIO2:8.08.01 Technische kwetsbaarheden tijdig signaleren · 0 · niet in orde · B-02
  - BIO2:8.08.02 Patches binnen de afgesproken termijn installeren · 2 · bestaan · B-02
- **OR-02** Herstel van kritieke processen is niet voorbereid of niet beproefd · BCM (ISO 22301), ISO 22301 8.4 en 8.5 · score 15 (Hoog)
  - BCM:8.2.2 Bedrijfsimpactanalyse van de kritieke processen · 2 · bestaan
  - BCM:8.4.4 Continuïteitsplan per kritiek proces · 1 · opzet · B-03
  - BCM:8.5 Plannen oefenen en herstel testen · 0 · niet in orde · B-03

### SR-02 · Onrechtmatige verwerking of verlies van persoonsgegevens van inwoners

Kans 3 × impact 4 = 12 (Hoog).

- **OR-03** Verzoeken van betrokkenen worden niet tijdig of niet volledig afgehandeld · Privacy (AVG), thema rechten van betrokkenen · score 8 (Gemiddeld)
  - AVG:A12 Betrokkenen tijdig en begrijpelijk informeren over hun verzoek · 1 · opzet · B-04
  - AVG:A15 Inzageverzoeken binnen de wettelijke termijn afhandelen · 2 · bestaan · B-04
- **OR-04** Verwerkers werken met persoonsgegevens zonder passende afspraken · Privacy (AVG), thema verwerkers en ketenpartners · niet beoordeeld
  - AVG:A28 Verwerkersovereenkomst met elke verwerker · 2 · bestaan
  - AVG:A29 Verwerkers werken alleen in opdracht · 1 · opzet

### SR-03 · Misbruik van bevoegdheden via een gekaapt of intern account

Kans 3 × impact 5 = 15 (Hoog).

- **OR-05** Toegangsrechten passen niet bij de functie of worden niet ingetrokken · BIO 2.0, ISO 27002 5.15, 5.18, 8.2 en 8.5 · score 12 (Hoog)
  - BIO2:5.15.01 Toegangsbeleid vastgesteld en toegepast · 2 · bestaan
  - BIO2:5.18.01 Toegangsrechten toekennen, herzien en intrekken · 2 · bestaan · B-01
  - BIO2:8.02.01 Beheerrechten apart toekennen en beperken · 0 · niet in orde · B-05
  - BIO2:8.05.01 Sterke authenticatie voor toegang · 3 · werking
- **OR-06** Misbruik van accounts wordt niet of te laat gezien · BIO 2.0, ISO 27002 8.15 en 8.16 · score 12 (Hoog)
  - BIO2:8.15.01 Gebeurtenissen vastleggen in logbestanden · 2 · bestaan
  - BIO2:8.16.01 Afwijkend gedrag opsporen en opvolgen · 0 · niet in orde · B-05

### Buiten de strategische risicoanalyse

Risico's uit de standaardlijst zonder passend strategisch risico. Dat is een bevinding over de risicoanalyse zelf: ontbreekt er een strategisch risico, of hoort dit erbij?

- **OR-07** Onbevoegden komen fysiek bij apparatuur · BIO 2.0, ISO 27002 7.2 · niet beoordeeld
  - BIO2:7.02.01 Fysieke toegang tot ruimtes met apparatuur · 2 · bestaan

## Bevindingen

Een bevinding is een aangetoond feit over een maatregel die niet werkt. Het risico volgt uit de maatregel: de eerste maatregel bepaalt het primaire risico. Alleen open en in behandeling tellen mee.

### B-01 · Toegangsrechten worden bij een functiewissel niet aangepast

- **Aangetoond:** Kwartaalcontrole Q2 door de tweede lijn (15-07-2026): bij 2 van de 6 afdelingen samen 14 accounts met rechten uit een vorige functie. De controle zelf liep bij die afdelingen niet.
- **Bronsoort en bron:** toets, toetsrapport C-01, Q2 2026 (peildatum 15-07-2026)
- **Maatregel BIO2:5.18.01:** rechten worden bij functiewissel niet herzien
- **Afgeleid:** OR-05, SR-03
- **Score:** kans 3 × impact 4 = 12 (Hoog)
- **Status:** open sinds 20-07-2026

### B-02 · Kritieke kwetsbaarheden in extern bereikbare systemen blijven langer open dan de patchtermijn

- **Aangetoond:** Incident maart 2026: misbruik van een kwetsbaarheid in de VPN-voorziening, negen dagen nadat de patch beschikbaar was. Kwetsbaarheidsscan juni 2026: 3 van de 11 extern bereikbare systemen boven de termijn.
- **Bronsoort en bron:** incident, incidentverslag maart 2026; scanrapport juni 2026 (peildatum 30-06-2026)
- **Maatregel BIO2:8.08.02:** patchtermijn voor kritieke kwetsbaarheden niet gehaald
- **Maatregel BIO2:8.08.01:** publicatie van de kwetsbaarheid niet tijdig opgemerkt
- **Afgeleid:** OR-01, SR-01
- **Score:** kans 4 × impact 5 = 20 (Kritiek)
- **Status:** in behandeling sinds 01-08-2026

### B-03 · Herstel van kritieke applicaties is niet binnen de hersteltijd beproefd

- **Aangetoond:** Hersteltest mei 2026: herstel van het zaaksysteem uit back-up duurde 31 uur bij een afgesproken hersteltijd van 8 uur. Voor de andere vier kritieke applicaties is nooit een hersteltest gedaan.
- **Bronsoort en bron:** test, verslag hersteltest mei 2026 (peildatum 20-05-2026)
- **Maatregel BCM:8.5:** herstel niet beproefd voor vier van vijf kritieke applicaties
- **Maatregel BCM:8.4.4:** continuïteitsplan noemt een hersteltijd die niet haalbaar is
- **Afgeleid:** OR-02, SR-01
- **Score:** kans 3 × impact 5 = 15 (Hoog)
- **Status:** open sinds 01-06-2026

### B-04 · Inzageverzoeken worden structureel buiten de wettelijke termijn afgehandeld

- **Aangetoond:** Toets door de functionaris gegevensbescherming (september 2026): 7 van de 19 inzageverzoeken in 2026 na meer dan een maand afgehandeld, zonder dat de betrokkene over verlenging is geïnformeerd.
- **Bronsoort en bron:** toets, rapportage FG, september 2026 (peildatum 10-09-2026)
- **Maatregel AVG:A15:** termijn van een maand niet gehaald
- **Maatregel AVG:A12:** betrokkene niet geïnformeerd over verlenging
- **Afgeleid:** OR-03, SR-02
- **Score:** kans 4 × impact 2 = 8 (Gemiddeld)
- **Status:** open sinds 15-09-2026

### B-05 · Activiteit van beheeraccounts wordt niet bewaakt

- **Aangetoond:** Meting augustus 2026: aanmeldingen van beheeraccounts worden gelogd, maar er staat geen melding op. In 90 dagen nul meldingen, terwijl de logs drie aanmeldingen buiten kantoortijd vanaf een onbekend apparaat tonen.
- **Bronsoort en bron:** meting, meetrapport logging, augustus 2026 (peildatum 28-08-2026)
- **Maatregel BIO2:8.16.01:** geen detectie op afwijkend gebruik van beheeraccounts
- **Maatregel BIO2:8.02.01:** beheeraccounts worden ook gebruikt buiten beheertaken
- **Afgeleid:** OR-06; secundair OR-05, SR-03
- **Score:** kans 3 × impact 4 = 12 (Hoog)
- **Status:** open sinds 01-09-2026

### B-06 · Verwerkersovereenkomsten ontbreken bij kleine leveranciers

- **Aangetoond:** Inventarisatie van het verwerkingsregister (april 2026): 2 van de 41 verwerkers zonder overeenkomst, beide kleine leveranciers met een contract dat eind 2026 afloopt.
- **Bronsoort en bron:** analyse, inventarisatie verwerkingsregister, april 2026 (peildatum 30-04-2026)
- **Maatregel AVG:A28:** geen overeenkomst bij twee verwerkers
- **Afgeleid:** OR-04, SR-02
- **Score:** kans 2 × impact 3 = 6 (Gemiddeld)
- **Status:** geaccepteerd sinds 12-05-2026, telt niet mee
- **Besluit risico-eigenaar:** Risico-eigenaar accepteert tot het einde van beide contracten op 31-12-2026; daarna niet verlengen zonder overeenkomst.

## Maatregelen

| Maatregel | Wat | Risico | Stand in de bron | Niveau | Waar het niveau vandaan komt | Beheerseigenaar |
|---|---|---|---|---|---|---|
| BIO2:8.08.01 | Technische kwetsbaarheden tijdig signaleren | OR-01 | niet geïmplementeerd | 0 · niet in orde | stand in de bron | teamleider technisch beheer |
| BIO2:8.08.02 | Patches binnen de afgesproken termijn installeren | OR-01 | geïmplementeerd | 2 · bestaan | stand in de bron | teamleider technisch beheer |
| BCM:8.2.2 | Bedrijfsimpactanalyse van de kritieke processen | OR-02 | voltooid | 2 · bestaan | stand in de bron | BCM-coördinator |
| BCM:8.4.4 | Continuïteitsplan per kritiek proces | OR-02 | deels | 1 · opzet | stand in de bron | BCM-coördinator |
| BCM:8.5 | Plannen oefenen en herstel testen | OR-02 | niets | 0 · niet in orde | stand in de bron | BCM-coördinator |
| AVG:A12 | Betrokkenen tijdig en begrijpelijk informeren over hun verzoek | OR-03 | opzet groen, bestaan oranje, werking rood | 1 · opzet | stand in de bron | privacy officer |
| AVG:A15 | Inzageverzoeken binnen de wettelijke termijn afhandelen | OR-03 | opzet groen, bestaan groen, werking rood | 2 · bestaan | stand in de bron | privacy officer |
| AVG:A28 | Verwerkersovereenkomst met elke verwerker | OR-04 | opzet groen, bestaan groen, werking oranje | 2 · bestaan | stand in de bron | contractmanager |
| AVG:A29 | Verwerkers werken alleen in opdracht | OR-04 | opzet groen, bestaan rood, werking rood | 1 · opzet | stand in de bron | contractmanager |
| BIO2:5.15.01 | Toegangsbeleid vastgesteld en toegepast | OR-05 | geïmplementeerd | 2 · bestaan | control C-03 (toets 01-06-2026, werking verlopen (cyclus gemist)) | informatiemanager |
| BIO2:5.18.01 | Toegangsrechten toekennen, herzien en intrekken | OR-05 | geïmplementeerd | 2 · bestaan | zwakste control C-01 (toets 15-07-2026) | teamleider functioneel beheer |
| BIO2:8.02.01 | Beheerrechten apart toekennen en beperken | OR-05 | niet geïmplementeerd | 0 · niet in orde | stand in de bron | teamleider technisch beheer |
| BIO2:8.05.01 | Sterke authenticatie voor toegang | OR-05 | geïmplementeerd | 3 · werking | control C-02 (toets 01-09-2026) | teamleider technisch beheer |
| BIO2:8.15.01 | Gebeurtenissen vastleggen in logbestanden | OR-06 | geïmplementeerd | 2 · bestaan | stand in de bron | teamleider technisch beheer |
| BIO2:8.16.01 | Afwijkend gedrag opsporen en opvolgen | OR-06 | niet geïmplementeerd | 0 · niet in orde | stand in de bron | teamleider technisch beheer |
| BIO2:7.02.01 | Fysieke toegang tot ruimtes met apparatuur | OR-07 | geïmplementeerd | 2 · bestaan | stand in de bron | facilitair manager |

## Controls

Een control is de toetsbare activiteit die laat zien dat een maatregel werkt. De zwakste getoetste control bepaalt het niveau van de maatregel. Werking vervalt als de volgende toets niet op tijd komt.

| Control | Wat | Toetst | Frequentie | Laatste toets | Niveau | Bewijs |
|---|---|---|---|---|---|---|
| C-01 | Kwartaalcontrole van toegangsrechten per afdeling | BIO2:5.18.01 | elke 92 dagen | 15-07-2026, tweede lijn | 2 · bestaan (toets 15-07-2026) | steekproef Q2: 2 van 6 afdelingen niet gecontroleerd |
| C-02 | Aanmelden alleen met phishingbestendige MFA | BIO2:8.05.01 | elke 183 dagen | 01-09-2026, tweede lijn | 3 · werking (toets 01-09-2026) | export aanmeldbeleid en aanmeldlog over 30 dagen |
| C-03 | Uitdienstmelding leidt binnen een werkdag tot blokkade | BIO2:5.18.01, BIO2:5.15.01 | elke 31 dagen | 01-06-2026, tweede lijn | 2 · bestaan (toets 01-06-2026, werking verlopen (cyclus gemist)) | vergelijking HR-uitstroom met blokkades, mei |

## Meldingen van de generator

Geen.
