---
domein: ib-in-projecten
titel: Beleid informatiebeveiliging in projecten
samenvatting: Regelt hoe beveiliging en privacy vanaf de start meegaan in projecten en significante wijzigingen aan informatiesystemen. Behandelt wanneer een risicoafweging nodig is, hoe die wordt uitgevoerd, de beslismomenten van start tot overdracht naar beheer, en de inbedding in de projectmethodiek.
invoeren:
  - Richt een meldpunt in waar projectleiders hun project bij de start aanmelden (hoofdstuk 3).
  - Regel dat een project zonder melding geen budget krijgt voor de realisatiefase (hoofdstuk 3).
  - Houd een overzicht bij van lopende projecten met de status van hun risicoafweging (hoofdstuk 3).
  - Wijs een risico-acceptant aan voor restrisico's boven de risicobereidheid (hoofdstuk 5).
  - Neem de beslismomenten uit dit beleid als vaste stappen op in de projectmethodiek (hoofdstuk 6).
  - Maak sjablonen voor de risicoafweging en voor de risicoacceptatie (hoofdstuk 6).
  - Geef nieuwe projectleiders binnen een maand een instructie en registreer de deelname (hoofdstuk 6).
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor projecten en wijzigingen waarin
informatiesystemen worden aangeschaft, gebouwd, gekoppeld of ingrijpend aangepast. Het zorgt dat de
beveiligingseisen worden bepaald voordat er een keuze valt, en dat de risico's bekend en behandeld zijn
voordat een systeem in gebruik gaat. Het gaat over ISO-beheersmaatregel 5.8.

**Voor wie.** Het beleid is primair bedoeld voor opdrachtgevers, projectleiders en proceseigenaren, en
daarnaast voor de architectuurfunctie, inkoop, de CISO en de privacy officer die in een project adviseren.
De regels gelden ook voor projectleiders en projectmedewerkers die zijn ingehuurd.

**Waarop.** Alle projecten en programma's van de organisatie waarin informatie of informatiesystemen een
rol spelen, ook als een leverancier het project uitvoert of als het project vooral een organisatie- of
procesverandering is, en alle wijzigingen buiten projectverband die als significant gelden (hoofdstuk 3).
Is de uitvoering van een project uitbesteed, dan gelden de eisen uit dit beleid als minimumeis voor die
partij. De organisatie legt dat vast in het contract en toetst de naleving met een onafhankelijke verklaring,
zoals een ISO 27001-certificaat of een ISAE 3402- of ISAE 3000-rapport; het vastleggen loopt via het beleid
informatiebeveiliging bij inkoop, het toetsen via het beleid contractbeheer.

Buiten dit beleid vallen de technische eisen aan software-ontwikkeling (beleid secure software development),
de afhandeling van gewone wijzigingen (beleid wijzigingsbeheer), de eisen aan leveranciers in het
inkooptraject (beleid informatiebeveiliging bij inkoop) en de classificatie van informatie zelf (beleid
informatieclassificatie).

## 2. Uitgangspunten

1. Beveiliging en privacy horen bij de start van een project. Eisen die pas bij de oplevering worden
   gesteld, kosten meer en worden vaker uitgezonderd.
2. De opdrachtgever van een project is eigenaar van de projectrisico's tot de overdracht; daarna is de
   proceseigenaar eigenaar.
3. De risicoafweging gebruikt de risicomanagementmethodiek die de organisatie heeft vastgesteld; een project
   gebruikt geen eigen methode.
4. Een project gaat pas live als de restrisico's bekend zijn en zijn geaccepteerd door wie dat mag.
5. Termijnen en frequenties in dit beleid die niet uit een wet of uit de BIO 2.0 komen, zijn standaardwaarden.
   De organisatie past ze aan op haar eigen risicoafweging en legt de keuze vast bij de vaststelling van dit beleid.

## 3. Wanneer een risicoafweging nodig is

- De opdrachtgever laat een risicoafweging uitvoeren bij elk nieuw informatiesysteem en bij elke
  significante wijziging op een bestaand systeem, voordat de keuze voor een oplossing of leverancier valt.
  Het verslag van de risicoafweging is het bewijs. [5.08.01]
- Een wijziging is significant als ze ten minste een van deze dingen doet: een nieuwe categorie gegevens
  verwerken, een nieuwe koppeling met een externe partij maken, de hostinglocatie of leverancier wijzigen,
  de toegang voor een nieuwe groep gebruikers openzetten of de classificatie van het systeem verhogen. Bij
  twijfel beslist de CISO; die beslissing wordt vastgelegd bij de melding van het project. [5.08.01]
- De projectleider meldt het project bij de start, met de projectopdracht of het startdocument, bij de CISO
  en de privacy officer via
  [[meldpunt projecten: waar projecten worden aangemeld, bijvoorbeeld het projectbureau of een intakeformulier]].
  Een project zonder melding krijgt geen budget voor de realisatiefase. [5.08.01]
- [[lijneigenaar projectportfolio: de functie die het overzicht van projecten bijhoudt, bijvoorbeeld het projectbureau]]
  houdt een overzicht bij van alle lopende projecten en significante wijzigingen met per project de datum
  van de melding, de classificatie en de status van de risicoafweging. [5.08.01]

## 4. Uitvoering van de risicoafweging

- De opdrachtgever laat de risicoafweging uitvoeren met de vastgestelde methodiek. Het resultaat is een
  verslag met de classificatie van het systeem, de dreigingen, de risico's, de gekozen maatregelen en de
  restrisico's, vastgelegd in het sjabloon van de projectmethodiek. [5.08.01]
- De proceseigenaar bepaalt de classificatie volgens het beleid informatieclassificatie, op de impactniveaus
  verwaarloosbaar tot en met catastrofaal en de vertrouwelijkheidslabels openbaar tot en met geheim. De
  classificatie bepaalt welke maatregelen uit de BIO 2.0 basisset en welke aanvullende maatregelen gelden.
  [5.08.01]
- Uit de risicoafweging volgen de beveiligingseisen. De opdrachtgever neemt ze op in het programma van
  eisen, de aanbesteding of de opdracht aan de leverancier, en in de acceptatiecriteria voor oplevering.
  [5.08.01]
- Verwerkt het systeem persoonsgegevens, dan beoordeelt de privacy officer bij de melding of een DPIA nodig
  is. DPIA en risicoafweging gebruiken dezelfde beschrijving van het systeem en worden samen opgeleverd.
  [5.08.01]
- De CISO of ISO adviseert schriftelijk over elke risicoafweging voordat de keuze voor een oplossing valt.
  Bij een restrisico boven de risicobereidheid van de organisatie noemt het advies de maatregelen die het
  risico terugbrengen en de rol die het resterende risico moet accepteren. [5.08.01]
- Maakt het project een koppeling met een systeem van een andere partij, dan beschrijft de risicoafweging
  ook de beveiliging van de koppeling: welke gegevens erover gaan, hoe de partijen elkaar herkennen en wie
  bij een incident wie waarschuwt. De afspraken daarover komen in de overeenkomst met die partij. [5.08.01]

::: als gevoelig=sociaal,jeugd,gezondheid
- Verwerkt het systeem gegevens uit het sociaal domein, over jeugd of over gezondheid, dan is een DPIA altijd
  verplicht en geldt voor vertrouwelijkheid ten minste het label strikt vertrouwelijk, tenzij de risicoafweging met
  redenen een lager label onderbouwt. [5.08.01]
- De risicoafweging behandelt in dat geval ook toegang door ketenpartners en zorgaanbieders, de logging van
  inzage en de vraag of gegevens buiten de Europese Economische Ruimte terechtkomen. De FG wordt om advies
  gevraagd voordat het project de realisatiefase ingaat; het advies zit bij het verslag. [5.08.01]
:::

::: als gevoelig=gezondheid
- Bij gezondheidsgegevens toetst de risicoafweging het systeem en de berichtenstroom (mail, chat,
  berichtenbox) aan NEN 7510 en NTA 7516 waar die van toepassing zijn, en legt vast welke eisen daaruit
  in het programma van eisen zijn opgenomen. [5.08.01]
:::

## 5. Projectfasen en beslismomenten

- Bij de start meldt de projectleider het project, bepaalt de proceseigenaar een eerste classificatie en
  stelt de CISO vast of het project of de wijziging significant is. De uitkomst staat in het startdocument.
  [5.08.01]
- Voor de keuze van oplossing of leverancier is de risicoafweging af en staan de beveiligingseisen in het
  programma van eisen. De opdrachtgever legt dat vast in het besluit over de keuze. [5.08.01]
- Voor de livegang toont de opdrachtgever aan dat de eisen zijn gerealiseerd, met testresultaten, een
  pentest bij systemen die vanaf internet bereikbaar zijn en een overzicht van de ingerichte toegang. Open
  punten staan met eigenaar en termijn in het risicoregister. [5.08.01]
- De opdrachtgever accepteert de restrisico's schriftelijk voor de livegang. Restrisico's boven de
  risicobereidheid worden geaccepteerd door
  [[risico-acceptant: de functie die hoge restrisico's mag accepteren, bijvoorbeeld de directie]].
  Zonder acceptatie gaat het systeem niet live. [5.08.01]
- Bij de overdracht naar beheer geeft de projectleider de proceseigenaar het verslag van de risicoafweging,
  de lijst van open risico's en de beheerafspraken, en registreert het systeem in het register van
  bedrijfsmiddelen volgens het beleid bedrijfsmiddelenbeheer. De proceseigenaar bevestigt de ontvangst.
  [5.08.01]
- Verandert de scope van een lopend project zodanig dat een van de criteria uit hoofdstuk 3 alsnog
  geldt, dan actualiseert de opdrachtgever de risicoafweging voordat het project verder gaat. [5.08.01]

## 6. Projectmethodiek

- De projectmethodiek van de organisatie bevat de beslismomenten uit hoofdstuk 5 als vaste stappen, met
  een sjabloon voor de risicoafweging en een sjabloon voor de risicoacceptatie. De eigenaar van de
  methodiek toetst elk jaar met de CISO of de stappen en sjablonen nog aansluiten op dit beleid en op het
  beleid informatieclassificatie. [5.08.01]
- Dezelfde stappen gelden voor projecten die met een agile of iteratieve aanpak werken: de risicoafweging
  loopt mee met de eerste oplevering en wordt bij elke oplevering die een criterium uit hoofdstuk 3 raakt
  bijgewerkt. [5.08.01]
- Projectleiders kennen de methodiek. Nieuwe projectleiders, ook inhuur, krijgen binnen een maand na de
  start een instructie van de ISO of CISO; de deelname wordt vastgelegd. [5.08.01]

## 7. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| Opdrachtgever | Laten uitvoeren van de risicoafweging, opnemen van de eisen in de opdracht, aantonen van de realisatie, accepteren van restrisico's |
| Projectleider | Melding bij de start, planning van de beslismomenten, bewijs bij oplevering, overdracht naar beheer |
| Proceseigenaar | Classificatie, inbreng van de eisen vanuit het proces, eigenaar van de risico's na overdracht |
| CISO of ISO | Advies over de risicoafweging, beslissing of een wijziging significant is, instructie van projectleiders |
| Privacy officer en FG | Beoordeling van de DPIA-plicht, advies bij persoonsgegevens; de FG adviseert bij gevoelige domeinen |
| [[lijneigenaar projectportfolio]] | Overzicht van lopende projecten met de status van hun risicoafweging |
| [[risico-acceptant]] | Acceptatie van restrisico's boven de risicobereidheid |

## 8. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in [[registratie van controles: het systeem waarin controles worden vastgelegd, bijvoorbeeld het ticketsysteem of het managementsysteem]];
afwijkingen gaan als bevinding naar het risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| PRJ-01 | Elk project en elke significante wijziging in het projectportfolio is gemeld bij de CISO en de privacy officer | CISO | Per kwartaal | Vergelijking van het projectportfolio met de ontvangen meldingen, lijst van projecten zonder melding en de afhandeling | 5.08.01 |
| PRJ-02 | Voor elk project dat de keuzefase heeft doorlopen, is de risicoafweging af en staan de beveiligingseisen in het programma van eisen of de opdracht | CISO of ISO | Per kwartaal | Verslag van de risicoafweging, programma van eisen of opdracht, schriftelijk advies | 5.08.01 |
| PRJ-03 | Voor elk systeem dat live is gegaan, is de realisatie van de eisen aangetoond en zijn de restrisico's schriftelijk geaccepteerd door de bevoegde rol | Interne audit of accountant | Jaarlijks | Steekproef van ten minste vijf opgeleverde projecten of significante wijzigingen: testresultaten, pentestrapport, risicoacceptatie | 5.08.01 |
| PRJ-04 | Bij elk overgedragen systeem heeft de proceseigenaar het verslag, de open risico's en de beheerafspraken ontvangen en staat het systeem in het register van bedrijfsmiddelen | [[lijneigenaar projectportfolio]] | Per kwartaal | Ontvangstbevestiging per project, register van bedrijfsmiddelen | 5.08.01 |
| PRJ-05 | De projectmethodiek bevat de beslismomenten en sjablonen uit dit beleid en nieuwe projectleiders hebben de instructie gevolgd | CISO | Jaarlijks | Vastgestelde methodiek met datum, registratie van de instructies | 5.08.01 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De
opdrachtgever dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de looptijd. De
afwijking geldt pas na acceptatie van het risico door [[risico-eigenaar: de manager die restrisico's accepteert]]
en staat in het risicoregister; afwijkingen worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 9. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het gebruikt de classificatie uit het
beleid informatieclassificatie en de methodiek uit het risicomanagementbeleid. Het raakt het privacybeleid
(DPIA), het beleid informatiebeveiliging bij inkoop en het beleid contractbeheer (eisen in de aanbesteding
en verklaringen van leveranciers), het beleid wijzigingsbeheer (wijzigingen die geen project zijn), het
beleid bedrijfsmiddelenbeheer (registratie bij overdracht), het beleid kwetsbaarhedenbeheer (pentest voor
livegang) en het beleid secure software development (eigen ontwikkeling).
