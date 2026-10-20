# Procedure datalekken en beveiligingsincidenten

> **Herkomst:** procedure van het team informatiebeveiliging en privacy (IB&P) van een regionale samenwerking van gemeenten, versie 1.1.3 (november 2024), in gebruik sinds 2016. Voor de commons herschreven in een vaste opbouw; de meldplicht onder de Cyberbeveiligingswet en de bewijsregel zijn aanvullingen van de commons (2026) en staan als zodanig gemarkeerd.

## Doel

Elk datalek en elk beveiligingsincident wordt gemeld, beoordeeld, beperkt, opgelost en geëvalueerd, langs
vaste rollen en binnen de wettelijke termijnen. Een datalek is een inbreuk op de beveiliging met een kans
op nadelige gevolgen voor de bescherming van persoonsgegevens (AVG artikel 4). Een beveiligingsincident is
een gebeurtenis die de vertrouwelijkheid, integriteit of beschikbaarheid van informatie of systemen
daadwerkelijk heeft geraakt. Ze overlappen vaak, en daarom is dit één procedure.

## Wanneer wel, wanneer niet

Altijd als iemand iets ziet dat een incident kan zijn. Melden mag iedereen: medewerker, inhuur, leverancier,
inwoner. Niet melden is het risico, niet te veel melden. Een melding die achteraf geen incident blijkt,
wordt afgesloten als gebeurtenis en kost een kwartier.

Deze procedure gaat over de afhandeling binnen de organisatie. Groeit een incident uit tot een calamiteit,
dan neemt het [calamiteitenteam](../../bcm/calamiteitenteam-digitaal-opzetten/) de coördinatie over; deze
procedure loopt dan door voor de registratie en de meldplichten.

## Rollen

| Rol | Doet |
|---|---|
| Melder | Meldt direct, beperkt waar mogelijk de blootstelling, noteert wat er is gezien |
| Servicedesk | Registreert, bepaalt of het een beveiligingsincident is, belt bij twijfel de (C)ISO |
| (C)ISO | Neemt de melding in ontvangst, stelt bewijs veilig, bepaalt prioriteit en of een responsteam nodig is; informeert CIO en FG |
| Privacy officer en FG | Beoordelen of er persoonsgegevens zijn geraakt, of er aan de Autoriteit Persoonsgegevens en aan betrokkenen gemeld moet worden; de FG beslist |
| CIO | Proceseigenaar; wordt altijd geïnformeerd, ook als er geen melding aan de AP nodig is |
| Verantwoordelijk directeur of manager | Eigenaar van het incident in de lijn; besluit over aangifte en responsteam, informeert betrokkenen |
| Probleemeigenaar | Voert de toegewezen maatregel uit |
| Incidentcoördinator IT | Verhelpt technisch; de (C)ISO is zelden de primaire behandelaar |

Betrek op afroep: communicatieadviseur, juridisch adviseur, functioneel beheer, de leverancier van het
systeem, de IBD, de SOC-dienstverlener.

## Stappen

### 1. Melden en blootstelling beperken

- De melder meldt bij de servicedesk, via het formulier, per mail of telefonisch. Vertrouwelijke zaken of
  personen: ook rechtstreeks bij de CISO.
- Bij een mogelijk besmet apparaat: niet meer gebruiken, niet uitzetten, netwerk eraf maar de stroom erop.
  Noteer hoe het is ontdekt, wanneer, op welk apparaat, in welke applicatie.
- De melder informeert de eigen leidinggevende.

### 2. Ontvangen en classificeren

- De servicedesk stelt vast of het een beveiligingsincident is (kennisitem) en belt in dat geval direct
  een beschikbare ISO of de CISO.
- De (C)ISO stelt bewijsmateriaal veilig en opent het meldingsdossier.
- Acute situaties zijn een **P1**: direct risico op schade aan de bedrijfsvoering, inbreuk op een systeem
  met gevoelige data, incidenten rond accounts van bestuurders of de gemeentesecretaris, spoedpatches, of het
  loskoppelen van een systeem. Alle andere beveiligingsmeldingen lopen als tweedelijnsmelding bij IB&P.
- CIO en FG worden direct geïnformeerd.

### 3. Beoordelen: datalek of niet

Privacy officer en FG beoordelen samen:

1. Zijn er persoonsgegevens geraakt? Zo nee, dan verder als beveiligingsincident (stap 5).
2. Wat zijn ernst en aard?
3. Moet het aan de Autoriteit Persoonsgegevens worden gemeld? De FG beslist, aan de hand van de richtsnoeren
   van de AP. Niet elk datalek is meldplichtig; nodeloze meldingen worden voorkomen.
4. Moeten betrokkenen worden geïnformeerd?

### 4. Datalek direct afhandelen

- De FG informeert, afhankelijk van ernst: gemeentesecretaris of directeur, portefeuillehouder, CIO, manager
  IT, persvoorlichter, de verantwoordelijk manager, de CISO.
- Bij criminele activiteit beslist de verantwoordelijk directeur over aangifte; de politie kan het onderzoek
  overnemen.
- De verantwoordelijk directeur vormt zo nodig een crisisteam datalek, dat de repressieve en correctieve
  maatregelen bepaalt. Per maatregel een probleemeigenaar.
- FG of privacy officer registreren het datalek, meldingsplichtig of niet: feiten, de tekst van de
  kennisgeving aan betrokkenen, de maatregelen.
- Melding aan de AP via het meldloket, binnen **72 uur** na eerste constatering.
- De verantwoordelijk manager informeert betrokkenen als de inbreuk waarschijnlijk nadelige gevolgen heeft
  voor hun persoonlijke levenssfeer. In de kennisgeving: aard van de inbreuk, waar meer informatie te
  krijgen is, aanbevolen maatregelen. Persoonlijk bij een beperkt aantal betrokkenen; bij grote aantallen
  via website en pers, in afstemming met communicatie en juridische zaken. Wees open over wat er is
  gebeurd, bied excuses aan, zeg wat de betrokkene zelf kan doen.
- Na uitvoering wordt het crisisteam opgeheven.

### 5. Beveiligingsincident direct afhandelen

- De CISO informeert, afhankelijk van ernst: gemeentesecretaris, portefeuillehouder, CIO, IBD, manager IT,
  functioneel beheer, persvoorlichter, de verantwoordelijk manager. Vaste opbouw van het bericht: korte
  inleiding, actuele status, wat er nu gebeurt, wat er nog komt, wat er van de ontvanger wordt verwacht.
- De verantwoordelijk directeur vormt zo nodig een incident-responsteam; de IBD kan erbij. Spelregels:
  niemand praat buiten het team zonder toestemming van management of CISO; alles wat het team schrijft is
  feitelijk, want het kan in een strafrechtelijk onderzoek belanden; dagelijks overleg; tijd wordt
  bijgehouden.
- Bewijs verzamelen en veiligstellen: images van schijven, netwerkverkeer, applicatie- en toegangslogs,
  foto's van de omgeving. Inventarislijst met wie, wanneer, wat.
- Forensisch onderzoek: analyseer, reconstrueer, documenteer. Werk op een kopie, bewaar het origineel,
  houd de resultaten herleidbaar.
- Maatregelen bepalen en uitvoeren, per maatregel een probleemeigenaar.
- Na uitvoering wordt het responsteam opgeheven; CIO en CISO worden geraadpleegd, de gemeentesecretaris
  geïnformeerd.

### 6. Structureel oplossen

- De probleemeigenaar stelt een onderzoeksteam samen dat de oorzaak vaststelt en rapporteert.
- Op basis van het rapport komt een verbeterplan, afgestemd met leveranciers, functioneel beheer, FG, CISO en
  juridisch adviseur. De verbeteracties komen in het meldingsregister.
- Na uitvoering worden FG en CISO geïnformeerd en wordt de status in het register bijgewerkt.
- Het register wordt periodiek met de CIO besproken.

### 7. Vragen tijdens en na het incident

Wat is er precies gebeurd, om welk type incident ging het, wanneer en hoe ontdekt. Wat zijn de gevolgen
voor organisatie en betrokkenen, en zijn die te kwantificeren. Wat was de oorzaak: techniek, mens of
proces. Welke stappen zijn gezet, hoe snel, en is er nog actie nodig van iemand binnen of buiten de
organisatie. Wat hebben we geleerd en welke maatregelen volgen. Wat zijn de conclusies en aanbevelingen.

## Aanvulling van de commons: de meldplicht onder de Cyberbeveiligingswet

> De oorspronkelijke procedure kent alleen de AVG-meldplicht. Onder de Cyberbeveiligingswet (de Nederlandse
> uitwerking van NIS2) geldt voor gemeenten een tweede meldplicht, met kortere termijnen.

| Wat | Termijn | Aan wie |
|---|---|---|
| Vroegtijdige waarschuwing van een significant incident | onverwijld, uiterlijk **24 uur** na kennisname | het NCSC (voorlopig CSIRT voor gemeenten, in elk geval tot eind 2026), via het meld- en registratieportaal, dat doorgeleidt naar de RDI (bevoegde autoriteit) |
| Melding met initiële beoordeling | uiterlijk **72 uur** na kennisname | idem |
| Eindverslag | uiterlijk **een maand** na de melding van 72 uur | idem |
| Kennisgeving aan ontvangers van diensten (informatieplicht) | onverwijld | inwoners, bedrijven en ketenpartners |
| Datalek met persoonsgegevens | binnen **72 uur** | Autoriteit Persoonsgegevens, los van de Cbw-melding |

Een incident is significant als het ten minste één van drie drempelwaarden voor decentrale overheden haalt of
kan halen: **uitval van de dienstverlening voor ten minste vier uur**, **financiële gevolgen die niet binnen de
begroting kunnen worden opgevangen**, of **ernstige verwonding of de dood van een persoon**. Het gaat om wat het
incident kan veroorzaken, niet alleen om wat het al deed. Een datalek dat alleen de vertrouwelijkheid raakt, is
op zichzelf geen Cbw-incident.

De drempel over de begroting is geen IT-oordeel. Leg daarom vooraf vast wie toetst en wie meldt, en hoe die
binnen 24 uur bereikbaar zijn, ook in het weekend. De volledige uitwerking, met sjablonen en melden namens
meerdere gemeenten, staat in [De Cbw-meldplicht inrichten](../../governance/cbw-meldplicht-inrichten/).

Voeg aan stap 2 toe: bij elke P1 legt de (C)ISO het tijdstip van kennisname vast (T0) en toetst binnen een uur
of het incident een drempelwaarde kan halen.

## Bewijs

Wat je aan het eind kunt laten zien:

- Het **meldingsregister** met alle incidenten en datalekken van het jaar, ook de niet-meldplichtige, met
  per incident de classificatie, de maatregelen en de status van de verbeteracties.
- Per meldplichtig datalek: de **melding aan de AP** met tijdstempel, en de kennisgeving aan betrokkenen.
- Per significant incident: de **vroegtijdige waarschuwing**, de melding en het eindverslag, met tijdstempels.
- De **inventarislijst van bewijsmateriaal** van een incident waar forensisch onderzoek is gedaan.
- Het **verslag van de periodieke bespreking** van het register met de CIO.

## BIO 2.0

| Maatregel | Wat deze procedure daarvoor levert |
|---|---|
| 5.24 Plannen en voorbereiden van het beheer van informatiebeveiligingsincidenten | De rollen, stappen en meldkanalen zijn vastgelegd en bekend |
| 5.25 Beoordelen van en besluiten over informatiebeveiligingsgebeurtenissen | Stap 2 en 3: classificatie door servicedesk, (C)ISO, privacy officer en FG |
| 5.26 Reageren op informatiebeveiligingsincidenten | Stap 4 en 5: maatregelen met probleemeigenaar, responsteam, communicatie |
| 5.27 Leren van informatiebeveiligingsincidenten | Stap 6: onderzoek, verbeterplan, register, periodieke bespreking |
| 5.28 Verzamelen van bewijsmateriaal | Stap 5: veiligstellen, inventarislijst, werken op een kopie |
| 6.8 Melden van informatiebeveiligingsgebeurtenissen | Stap 1: iedereen meldt, via vaste kanalen |
| 5.34 Privacy en bescherming van persoonsgegevens | Stap 3 en 4, met AVG artikel 33 en 34 |

## Zo leg je het uit

**Aan de directie.** "Een incident kost ons altijd iets. Zonder procedure kost het ons daarnaast de
meldtermijn, en die is niet in te halen. Deze procedure zorgt dat de juiste mensen binnen een uur weten wat
er speelt en dat de klok voor de AP en de toezichthouder op tijd gaat lopen."

**Aan de servicedesk.** "Jullie zijn de eerste schakel. Twijfel je of iets een beveiligingsincident is, bel
dan. Een telefoontje te veel is geen probleem, een melding die blijft liggen wel."

**Aan een manager.** "Als het in jouw afdeling gebeurt, ben jij de eigenaar. Niet omdat het jouw schuld is,
maar omdat jij weet wat het voor jouw proces en jouw inwoners betekent. Wij ondersteunen."
