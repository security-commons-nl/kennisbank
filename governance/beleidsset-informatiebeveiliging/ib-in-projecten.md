# Beleid informatiebeveiliging in projecten

Beleid informatiebeveiliging, BIO 2.0-domein *Informatiebeveiliging binnen projecten*. Status: concept, vast te stellen door de organisatie zelf.

Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor projecten en wijzigingen waarin
informatiesystemen worden aangeschaft, gebouwd, gekoppeld of ingrijpend aangepast. Het zorgt dat de
beveiligingseisen worden bepaald voordat er een keuze valt, en dat de risico's bekend en behandeld zijn
voordat een systeem in gebruik gaat. Het gaat over ISO-beheersmaatregel 5.08.

Het beleid geldt voor alle projecten en programma's, ook als een leverancier het project uitvoert, en voor
wijzigingen buiten projectverband die als significant gelden (zie 3.1). Het is bedoeld voor opdrachtgevers,
projectleiders, proceseigenaren, de architectuurfunctie en inkoop.

Buiten dit beleid vallen de technische eisen aan software-ontwikkeling (beleid secure software development),
de afhandeling van gewone wijzigingen (beleid wijzigingsbeheer) en de eisen aan leveranciers in het
inkooptraject (beleid leveranciersbeheer, inkoop).

## 2. Uitgangspunten

1. Beveiliging en privacy horen bij de start van een project. Eisen die pas bij de oplevering worden
   gesteld, kosten meer en worden vaker uitgezonderd.
2. De opdrachtgever van een project is eigenaar van de projectrisico's tot de overdracht; daarna is de
   proceseigenaar eigenaar.
3. De risicoafweging gebruikt de risicomanagementmethodiek die de organisatie heeft vastgesteld; een project
   gebruikt geen eigen methode.

## 3. Beleidsregels

### 3.1 Wanneer een risicoafweging nodig is

- Een risicoafweging is verplicht bij elk nieuw informatiesysteem en bij elke significante wijziging op een
  bestaand systeem. [5.08.01]
- Een wijziging is significant als ze ten minste een van deze dingen doet: een nieuwe categorie gegevens
  verwerken, een nieuwe koppeling met een externe partij maken, de hostinglocatie of leverancier wijzigen,
  de toegang voor een nieuwe groep gebruikers openzetten of de classificatie van het systeem verhogen.
  Bij twijfel beslist de CISO. [5.08.01]
- De projectleider meldt het project bij de start (projectopdracht of startdocument) bij de CISO en de
  privacy officer. Een project zonder melding krijgt geen budget voor de realisatiefase.

### 3.2 Uitvoering van de risicoafweging

- De opdrachtgever laat de risicoafweging uitvoeren met de vastgestelde methodiek. Het resultaat is een
  verslag met de classificatie van het systeem, de dreigingen, de risico's, de gekozen maatregelen en de
  restrisico's. [5.08.01]
- De classificatie volgt het beleid informatieclassificatie en bepaalt welke maatregelen uit de BIO 2.0
  basisset en welke aanvullende maatregelen gelden. [5.08.01]
- Uit de risicoafweging volgen de beveiligingseisen. Die worden opgenomen in het programma van eisen, de
  aanbesteding of de opdracht aan de leverancier, en in de acceptatiecriteria voor oplevering. [5.08.01]
- Verwerkt het systeem persoonsgegevens, dan beoordeelt de privacy officer of een DPIA nodig is. DPIA en
  risicoafweging gebruiken dezelfde beschrijving van het systeem en worden samen opgeleverd.
- De ISO of CISO adviseert over de risicoafweging. Bij een restrisico boven de risicobereidheid van de
  organisatie is het advies schriftelijk.

> **Alleen als: In welke gevoelige domeinen verwerk je persoonsgegevens? «Sociaal domein» of «Jeugd» of «Gezondheid (WvGGZ, NTA 7516)»**
>
> - Verwerkt het systeem gegevens uit het sociaal domein, over jeugd of over gezondheid, dan is een DPIA altijd
>   verplicht en geldt voor vertrouwelijkheid ten minste het hoogste niveau uit het beleid
>   informatieclassificatie, tenzij de risicoafweging met redenen een lager niveau onderbouwt. [5.08.01]
> - De risicoafweging behandelt in dat geval ook toegang door ketenpartners en zorgaanbieders, de logging van
>   inzage en de vraag of gegevens buiten de Europese Economische Ruimte terechtkomen. De FG wordt om advies
>   gevraagd voordat het project de realisatiefase ingaat. [5.08.01]

> **Alleen als: In welke gevoelige domeinen verwerk je persoonsgegevens? «Gezondheid (WvGGZ, NTA 7516)»**
>
> - Bij gezondheidsgegevens toetst de risicoafweging het systeem en de berichtenstroom (mail, chat,
>   berichtenbox) aan NEN 7510 en NEN 7516 waar die van toepassing zijn. [5.08.01]

### 3.3 Projectfasen en beslismomenten

- Bij de start: melding, eerste classificatie en de vraag of het project significant is.
- Voor de keuze van oplossing of leverancier: risicoafweging af, beveiligingseisen in het programma van
  eisen. [5.08.01]
- Voor de livegang: de opdrachtgever toont aan dat de eisen zijn gerealiseerd, bijvoorbeeld met testresultaten,
  een pentest bij systemen die vanaf internet bereikbaar zijn en de configuratie van de toegang. Open
  punten staan met eigenaar en termijn in het risicoregister.
- De opdrachtgever accepteert de restrisico's schriftelijk. Restrisico's boven de risicobereidheid worden
  geaccepteerd door
  **[risico-acceptant]**.
  [5.08.01]
- Bij de overdracht naar beheer krijgt de proceseigenaar het verslag van de risicoafweging en de lijst van
  open risico's.

### 3.4 Projectmethodiek

- De projectmethodiek van de organisatie bevat de beslismomenten uit 3.3 als vaste stappen met een
  sjabloon voor de risicoafweging. [5.08.01]
- Projectleiders kennen de methodiek. Nieuwe projectleiders, ook inhuur, krijgen bij de start een korte
  instructie van de ISO of CISO.

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| Opdrachtgever | Laten uitvoeren van de risicoafweging, opnemen van de eisen in de opdracht, accepteren van restrisico's |
| Projectleider | Melding bij de start, planning van de beslismomenten, bewijs bij oplevering |
| Proceseigenaar | Classificatie, inbreng van de eisen vanuit het proces, eigenaar van de risico's na overdracht |
| CISO of ISO | Advies over de risicoafweging en over de vraag of een wijziging significant is |
| Privacy officer en FG | Beoordeling DPIA-plicht, advies bij persoonsgegevens |
| **[lijneigenaar projectportfolio]** | Overzicht van lopende projecten met de status van hun risicoafweging |

## 5. Naleving en bewaking

- Elk kwartaal: de CISO vergelijkt het projectportfolio met de ontvangen meldingen; bewijs is de lijst met
  projecten zonder melding en de afhandeling daarvan.
- Jaarlijks: steekproef van ten minste vijf opgeleverde projecten of significante wijzigingen op een
  volledige risicoafweging, eisen in de opdracht en schriftelijke risicoacceptatie.
- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het gebruikt de classificatie uit het
beleid informatieclassificatie en de methodiek uit het risicomanagementbeleid. Het raakt het privacybeleid
(DPIA), het beleid leveranciersbeheer (eisen in de aanbesteding), het beleid wijzigingsbeheer (wijzigingen
die geen project zijn) en het beleid secure software development (eigen ontwikkeling).

## Bijlage: BIO 2.0-maatregelen

De overheidsmaatregelen van dit domein (1) en waar dit stuk ze invult. Nummers volgens BIO2 v1.3 definitief - 9 januari 2026; de tekst van de maatregel staat bij het CIP.

| Maatregel | Titel | In dit stuk |
|---|---|---|
| 5.08.01 | Informatiebeveiliging in projectmanagement | 3.1 Wanneer een risicoafweging nodig is |

## Nog in te vullen

- **risico-acceptant**: de functie die hoge restrisico's mag accepteren, bijvoorbeeld de directie
- **lijneigenaar projectportfolio**: de functie die het overzicht van projecten bijhoudt, bijvoorbeeld het projectbureau
