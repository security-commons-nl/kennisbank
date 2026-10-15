# Sjabloon: BIA en risicoanalyse per kritieke dienst

Twee bladen. Blad 1 vul je per dienst in, blad 2 is een tabel voor alle risico's samen. De keuzes die je
vooraf maakt en de vergelijking met bestaande formats staan in de [toelichting](README.md).

Werk je in een spreadsheet: een tabblad per dienst voor blad 1, een tabblad voor blad 2, en een tabblad met
de impactschaal die je gebruikt.

## Instellingen

Leg deze drie vooraf vast, voor de hele organisatie. Ze bepalen hoe de uitkomst in blok H wordt afgeleid.

| Instelling | Voorstel | Waarom |
|---|---|---|
| Impactschaal | Vijf niveaus (1 zeer laag tot 5 zeer hoog), met een beschrijving per categorie en niveau. Gemeenten: de BIO2 kans- en impacttabellen van de IBD | Een schaal voor BIA en risicoanalyse; een tweede schaal geeft twee uitkomsten voor dezelfde dienst |
| Drempel kritiek | Een dienst is kritiek als binnen **2 dagen** op een categorie score **4** of hoger wordt bereikt | Twee dagen is een gangbare grens voor gouden processen; 4 is het niveau van ernstige schade |
| Venster voor beschikbaarheid | De beschikbaarheidsklasse volgt uit de hoogste score bij **1 dag** uitval | Zo levert de BIA de BIV-classificatie zonder tweede beoordeling |

## Blad 1: BIA per dienst

### A. Identificatie

| Veld | Vulling |
|---|---|
| Organisatie | |
| Bestuurslaag | Rijk · provincie · gemeente · waterschap · uitvoeringsorganisatie · gemeenschappelijke regeling |
| Naam van de dienst | |
| Eigenaar (functie) | |
| Kenmerk in eigen register | bijvoorbeeld GEMMA-proces, dienstencatalogus |
| Datum en versie | |
| Opgesteld met | functies van wie er aan tafel zat |

### B. Wat de dienst levert en aan wie

| Veld | Vulling |
|---|---|
| Omschrijving van de dienst | |
| Voor wie | inwoners · bedrijven · andere overheden · keten |
| Wettelijke grondslag | |
| Processen die de dienst leveren | |
| Keten: wie levert aan deze dienst | |
| Keten: aan wie levert deze dienst | |

### C. Impact bij uitval, per tijdvenster

Score 1 tot 5 volgens de impactschaal; leeg als de categorie niet speelt. De hoogste score per venster telt.

| Categorie | 4 uur | 1 dag | 2 dagen | 1 week | 1 maand | Waarom deze score |
|---|---|---|---|---|---|---|
| Maatschappelijke impact | | | | | | |
| Schade aan vitale processen | | | | | | |
| Belang voor de organisatie | | | | | | |
| Financiële impact | | | | | | |
| Politieke en bestuurlijke schade | | | | | | |
| Imagoschade en verlies van vertrouwen | | | | | | |
| Letsel | | | | | | |
| Inbreuk op de persoonlijke levenssfeer | | | | | | |
| Medewerkers (motivatie, belasting) | | | | | | |
| Verlies van sturing | | | | | | |
| Diplomatieke schade (alleen waar het speelt, bijvoorbeeld bij het Rijk) | | | | | | |
| **Hoogste score per venster** | | | | | | |

**C2. Integriteit en vertrouwelijkheid.** Twee scores op dezelfde schaal, nodig voor blok H:

| Vraag | Score | Waarom |
|---|---|---|
| Zwaarste gevolg als gegevens van deze dienst onjuist of onvolledig zijn | | |
| Zwaarste gevolg als gegevens van deze dienst bij onbevoegden terechtkomen | | |

### D. Hersteleisen

Elke eis met een onderbouwing: wet, werklast, contract of bestuurlijke afspraak. Een hersteltijd zonder
onderbouwing wordt bij de eerste budgetdiscussie onderhandelbaar.

| Eis | Waarde | Onderbouwing |
|---|---|---|
| MTPD-indicatie uit blok C | het eerste venster waarin de drempel wordt bereikt | afgeleid, geen besluit |
| MTPD, vastgesteld: hoe lang mag de dienst uitvallen voordat de schade onaanvaardbaar is | | |
| RTO: binnen welke tijd draait de dienst weer op noodniveau (korter dan de MTPD) | | |
| RPO: tot welk moment terug mogen gegevens verloren gaan | | |
| Noodniveau: wat moet er minimaal door tijdens de verstoring | | |

### E. Middelen en afhankelijkheden

| Middel | Enkelvoudig punt van uitval? | Hersteltijd van het middel | Wat precies, en welke afspraken (leverancier, SLA, uitwijk) |
|---|---|---|---|
| Mensen | | | |
| Apparatuur | | | |
| Programmatuur | | | |
| Gegevens | | | |
| Organisatie | | | |
| Omgeving (gebouwen, nutsvoorzieningen) | | | |
| Diensten van derden (leveranciers, cloud) | | | |
| Ketenpartners en andere overheden | | | |
| Andere diensten van de eigen organisatie | | | |

De eerste zeven zijn de MAPGOOD-indeling. Een middel met een hersteltijd die langer is dan de RTO van de
dienst, is de eerste vraag voor de [uitwijkkaart](../uitwijk-regelen/uitwijkkaart.md).

### F. Terugval

| Vraag | Antwoord |
|---|---|
| Alternatieve werkwijze (handmatig, papier, uitwijk, beperkte dienst) | |
| Hoe lang is die vol te houden | |
| Is dit vooraf afgesproken en geoefend | |

### G. Dreigingen en bestaande maatregelen

| Vraag | Antwoord |
|---|---|
| Reële scenario's (uitval leverancier, ransomware, stroomuitval, uitval personeel) | |
| Bestaande maatregelen voor continuïteit | |

Werk elk scenario uit op blad 2.

### H. Uitkomst

Afgeleid uit blok C en C2 met de instellingen bovenaan. Het oordeel blijft bij de eigenaar.

| Uitkomst | Regel |
|---|---|
| Hoogste impact over alle vensters | de hoogste score in blok C |
| Kritieke dienst | ja als de drempel binnen het ingestelde venster wordt bereikt |
| Beschikbaarheid | de hoogste score in het venster voor beschikbaarheid |
| Integriteit | de score uit C2 |
| Vertrouwelijkheid | de score uit C2 |
| Oordeel en besluit eigenaar, met datum | |

## Blad 2: Risicotabel

Een regel per risico. Kans 1 tot 5, impact 1 tot 5 op dezelfde schaal als blok C. Risico is kans maal impact.

| Nr | Dienst | Scenario of dreiging | Middel (MAPGOOD) | BIV-aspect | Kans | Impact | Risico | Behandeling | Maatregel | BIO2-maatregel | Kans na | Impact na | Restrisico | Eigenaar | Datum |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | | | | | | | |
| 2 | | | | | | | | | | | | | | | |
| 3 | | | | | | | | | | | | | | | |

Behandeling is een van vier: verminderen, accepteren, overdragen, vermijden. Accepteren is een besluit van de
eigenaar met een datum; zie [risicogestuurd managementsysteem](../../governance/risicogestuurd-managementsysteem/)
voor hoe je dat vastlegt.

Een indeling van het risico in niveaus, als je die wilt, afgeleid van de risicotabel van de IBD: 1 zeer laag, 2 tot 3 laag, 4 tot 6 gemiddeld, 8 tot
16 hoog, 20 tot 25 extreem. Waar de grenzen liggen hangt af van de risicobereidheid van de organisatie; leg
dat vast bij de instellingen.

## Voorbeeld (verzonnen)

Een gemeente vult blad 1 in voor het verstrekken van een uitkering levensonderhoud.

| Blok | Vulling |
|---|---|
| B | Inwoners zonder voldoende inkomen krijgen maandelijks een uitkering. De betaalrun is maandelijks, aanvragen en mutaties lopen doorlopend. Keten: inkomensgegevens van het Rijk, de basisregistratie personen, de bank, de leverancier van de uitkeringssoftware. |
| C | Maatschappelijke impact 1 bij 4 uur, 2 bij 1 dag, 4 bij 2 dagen, 5 bij een week. Buiten de betaalrun weinig merkbaar; rond de betaalrun raken duizenden huishoudens binnen dagen in de problemen. Financiële impact 3 bij 1 dag en 4 bij 2 dagen. Politieke schade 3 bij 1 dag en 4 bij 2 dagen. |
| C2 | Integriteit 4: onjuiste bedragen raken direct het inkomen en leiden tot terugvordering. Vertrouwelijkheid 4: financiële en bijzondere gegevens van kwetsbare inwoners. |
| D | MTPD-indicatie 2 dagen. MTPD vastgesteld 2 dagen (daarna betalingsachterstanden bij huur en energie). RTO 1 dag. RPO 1 dag. Noodniveau: voorschot aan bestaande klanten op basis van het vorige betaalbestand. |
| E | Programmatuur: SaaS-uitkeringsadministratie, enkelvoudig, uitwijk contractueel geregeld en niet getest. Diensten van derden: de bank voor de betaalbestanden. |
| F | Voorschot via het bankbestand van de vorige maand; houdt een betaalrun vol; afgesproken, niet geoefend. |
| H | Kritiek: score 4 binnen 2 dagen. Beschikbaarheid 3 (hoogste score bij 1 dag), integriteit 4, vertrouwelijkheid 4. |

En de eerste regel op blad 2: de leverancier van de uitkeringssoftware valt langer dan twee dagen uit rond de
betaalrun. Kans 2, impact 5, risico 10. Behandeling: verminderen, met een geteste voorschotprocedure en een
exitplan voor onverwachte uitval in het contract.
