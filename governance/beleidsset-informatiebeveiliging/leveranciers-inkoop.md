# Beleid informatiebeveiliging bij inkoop

Beleid informatiebeveiliging, BIO 2.0-domein *Leveranciersbeheer - Inkoop*. Status: concept, vast te stellen door de organisatie zelf.

Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor de inkoop van producten en diensten
waarbij informatie wordt verwerkt, opgeslagen of ontsloten. Het regelt wat de organisatie vastlegt vóórdat een
contract wordt getekend: de eisen in de uitvraag, de voorwaarden in het contract, het bewijs dat de
leverancier levert en de exit. Het geldt voor elke inkoop met een informatiecomponent, ook onderhands en ook
bij verlenging of uitbreiding van een bestaand contract. Het gaat over de ISO-beheersmaatregelen 5.19, 5.20
en 5.21 voor zover die vóór het contract spelen.

Het beheer van de leverancier tijdens de looptijd (jaarlijkse beoordeling, ketenwijzigingen, register van
contracten, beleid voor clouddiensten) staat in het beleid contractbeheer. De verwerkersovereenkomst volgt
uit het privacybeleid; dit beleid verwijst ernaar.

> **Alleen als: Wie beheert je IT? «Regie: eigen organisatie stuurt, beheer is uitbesteed» of «Volledig uitbesteed»**
>
> De organisatie heeft het beheer van haar IT uitbesteed. De contracten met beheer- en hostingpartijen zijn
> daarmee de zwaarste inkopen onder dit beleid: wat daar niet in staat, kan de organisatie later niet afdwingen.

## 2. Uitgangspunten

1. De organisatie blijft verantwoordelijk voor de informatie die een leverancier voor haar verwerkt. Een
   certificaat of verklaring van de leverancier verandert daar niets aan.
2. Beveiligingseisen staan in de uitvraag. Wat pas na de gunning wordt bedacht, is in de onderhandeling niet
   meer te krijgen.
3. De zwaarte van de eisen volgt uit een risicoafweging per inkoop, op basis van de classificatie van de
   informatie en het belang van het proces.
4. Bij IT-inkoop gebruikt de organisatie een standaardset inkoopvoorwaarden voor IT, bijvoorbeeld de GIBIT
   voor gemeenten of de ARBIT voor het Rijk, en vult die per inkoop aan.

## 3. Beleidsregels

### 3.1 Risicoafweging en eisen in de uitvraag

- Bij elke inkoop met een informatiecomponent stelt de proceseigenaar met de inkoopadviseur en de CISO vast
  welke informatie de leverancier verwerkt, welk classificatieniveau die heeft en welke eisen aan
  beschikbaarheid, integriteit en vertrouwelijkheid daaruit volgen. De afweging wordt vastgelegd in het
  inkoopdossier. [5.19.01]
- De eisen uit die afweging staan in de offerteaanvraag of uitvraag, naast de functionele eisen, en wegen mee
  in de beoordeling van de inschrijvingen. Een inschrijver die niet aan een eis kan voldoen, zegt dat in de
  inschrijving. [5.19.01]
- Bij een inkoop onder de drempel voor een risicoafweging (bijvoorbeeld een dienst zonder persoonsgegevens en
  zonder koppeling met eigen systemen) volstaat de standaardset eisen. De drempel staat in
  **[drempel risicoafweging inkoop]**.
  [5.19.01]

> **Alleen als: Wat is je status onder de Cyberbeveiligingswet? «Essentiële entiteit» of «Belangrijke entiteit»**
>
> - De organisatie valt onder de Cyberbeveiligingswet. De zorgplicht omvat de beveiliging van de
>   toeleveringsketen. Bij inkoop van een dienst die een rol speelt in de dienstverlening onder die wet, legt de
>   risicoafweging ook vast hoe de leverancier bijdraagt aan het voldoen aan de meldplicht en welke eisen de
>   bestuurder daarvoor heeft goedgekeurd. [5.19.01]

### 3.2 Voorwaarden in het contract

- Alle beveiligingseisen uit de uitvraag komen letterlijk of als verwijzing in het contract, met de
  afspraken die in de onderhandeling zijn gemaakt. Een eis die in de uitvraag stond en niet in het contract,
  geldt als vervallen en vraagt een besluit van de proceseigenaar. [5.20.01]
- De organisatie verklaart haar eigen inkoopvoorwaarden van toepassing en wijst de algemene voorwaarden van
  de leverancier uitdrukkelijk van de hand. [5.20.02]
- Lukt dat niet, bijvoorbeeld bij een standaarddienst van een grote aanbieder, dan beoordeelt de CISO de
  voorwaarden van de leverancier. De beoordeling noemt welke gevolgen de organisatie accepteert, welke ze met
  eigen maatregelen afdekt en welke voorwaarden ze nooit accepteert. De proceseigenaar tekent voor de
  geaccepteerde risico's. [5.20.02]
- Voorwaarden die de organisatie nooit accepteert, staan in
  **[lijst onaanvaardbare voorwaarden]**.
  [5.20.02]
- Verwerkt de leverancier persoonsgegevens, of kan hij erbij, dan sluit de organisatie een
  verwerkersovereenkomst volgens het privacybeleid, voordat de verwerking begint.

### 3.3 Bewijs van de leverancier en eigen onderzoek

- Het contract verplicht de leverancier om aan te tonen dat hij aan de eisen voldoet, in opzet, bestaan en
  werking, met een rapport van een onafhankelijke derde. Voorbeelden zijn een ISAE 3000- of ISAE
  3402-rapport type II of een ISO 27001-certificaat met een verklaring van toepasselijkheid. [5.20.03]
- De reikwijdte van dat rapport dekt de gecontracteerde dienst, inclusief de manier waarop de leverancier zijn
  eigen toeleveranciers beheert. Valt een deel van de dienst buiten de reikwijdte, dan levert de leverancier
  voor dat deel ander bewijs. [5.20.03]
- De leverancier levert het bewijs bij het sluiten van het contract en daarna elk jaar opnieuw. [5.20.03]
- Het contract geeft de organisatie het recht om zelf een audit of een technisch onderzoek te laten doen,
  bijvoorbeeld een penetratietest, ook om de rapporten van de leverancier te controleren. De verdeling van de
  kosten staat in het contract. [5.20.04]
- Restrisico's uit het bewijs of het eigen onderzoek gaan naar het risicoregister en worden behandeld volgens
  de risicomanagementmethodiek van de organisatie. [5.20.04]

### 3.4 Transparantie over kwetsbaarheden en incidenten

- Het contract verplicht de leverancier om beveiligingsincidenten, datalekken en kwetsbaarheden die de dienst
  aan de organisatie kunnen raken, te melden bij het meldpunt van de organisatie. De termijn staat in het
  contract en is kort genoeg om de wettelijke meldtermijnen van de organisatie te halen. [5.20.05]
- De leverancier geeft bij een melding wat de organisatie nodig heeft om te reageren: wat er is gebeurd,
  welke gegevens en welke gebruikers geraakt zijn, en welke maatregelen hij neemt. [5.20.05]

> **Alleen als: Wat is je status onder de Cyberbeveiligingswet? «Essentiële entiteit» of «Belangrijke entiteit»**
>
> - Voor diensten die onder de Cyberbeveiligingswet vallen, is de meldtermijn van de leverancier ten hoogste
>   **[meldtermijn leverancier]**
>   na ontdekking. Het contract regelt ook dat de leverancier meewerkt aan de vervolgmeldingen. [5.20.05]

### 3.5 Afhankelijkheid en exit

- Vóór het contract beoordeelt de proceseigenaar of de afhankelijkheid van de leverancier beheersbaar is: zijn
  er alternatieven, hoe lang duurt een overstap, en kan de organisatie haar gegevens in een bruikbaar formaat
  terugkrijgen. [5.20.06]
- Elk contract voor een dienst die een kritiek proces ondersteunt of vertrouwelijke informatie verwerkt, bevat
  een uitgewerkte exitregeling: het teruggeven van gegevens in een open of gedocumenteerd formaat, de
  medewerking bij overdracht aan een opvolger, de termijn waarin de leverancier gegevens verwijdert en het
  bewijs daarvan. [5.20.06]
- Bij software die de organisatie in eigen beheer draait en die niet makkelijk te vervangen is, regelt het
  contract een escrow of een gelijkwaardige continuïteitsregeling. [5.20.06]

### 3.6 Keten van toeleveranciers

- Vóór het contract geeft de leverancier een overzicht van de toeleveranciers die bij de dienst betrokken
  zijn, met hun rol, de locatie van de verwerking en de risico's die hij daarin ziet. [5.21.02]
- De CISO beoordeelt of die risico's acceptabel zijn. De proceseigenaar besluit, en legt het besluit vast in
  het inkoopdossier. [5.21.02]
- Het contract verbiedt de leverancier om zonder schriftelijke toestemming werk aan een nieuwe toeleverancier
  over te dragen.

### 3.7 Eisen per soort dienst

> **Alleen als: Waar draaien je systemen? «Eigen datacenter of serverruimte»**
>
> - Bij inkoop van hardware en software voor het eigen datacenter regelt het contract hoe de leverancier op
>   afstand toegang krijgt voor onderhoud (alleen na aanvraag, met persoonsgebonden accounts en logging) en
>   hoelang hij beveiligingsupdates levert. [5.20.01]

> **Alleen als: Waar draaien je systemen? «Hostingpartij (IaaS, gedeeld datacenter)»**
>
> - Bij een hostingpartij legt het contract de locatie van de datacenters vast, de fysieke beveiliging, de
>   scheiding tussen klanten, de uitwijkvoorziening en de back-updiensten die de organisatie afneemt. [5.20.01]

> **Alleen als: Waar draaien je systemen? «Vooral SaaS en publieke cloud»**
>
> - Bij SaaS en publieke cloud gelden aanvullend: inloggen via de eigen identiteitsvoorziening met
>   meerfactorauthenticatie, een jaarlijkse penetratietest door een externe partij met de reikwijdte van de
>   geleverde dienst, het delen van de bevindingen en de hersteltermijnen, afspraken over de locatie van de
>   gegevens, en de mogelijkheid om gegevens zelf te exporteren. [5.20.01, 5.20.03]

> **Alleen als: Stel je eisen aan Europese of soevereine cloud? «Ja: alleen EU of soevereine dienstverlening»**
>
> - Bij clouddiensten eist de uitvraag dat gegevens, back-ups en beheer binnen de Europese Economische Ruimte
>   blijven, en dat de leverancier niet onder een buitenlandse wet valt die hem kan dwingen gegevens af te
>   staan zonder tussenkomst van een Europese rechter. De leverancier geeft daarover een verklaring, en het
>   contract regelt wat er gebeurt als dat verandert. [5.20.01]
> - Waar de markt geen dienst levert die hieraan voldoet, legt de proceseigenaar de afwijking met het restrisico
>   vast en beoordeelt de CISO die. **[besluitvormer afwijking soevereiniteit]**

> **Alleen als: Wie beheert je IT? «Eigen beheer»**
>
> - Bij inkoop van beheertools en ondersteuning blijft het beheer bij eigen medewerkers. Het contract regelt
>   dat de leverancier geen standaardtoegang tot de omgeving heeft. [5.20.01]

> **Alleen als: Wie beheert je IT? «Regie: eigen organisatie stuurt, beheer is uitbesteed» of «Volledig uitbesteed»**
>
> - Bij inkoop van beheerdiensten regelt het contract ook: screening van het beheerpersoneel van de
>   leverancier, beheertoegang alleen via persoonsgebonden accounts met meerfactorauthenticatie, logging van
>   beheerhandelingen die de organisatie kan inzien, en rapportage over de afgesproken beveiligingsprocessen
>   (patchen, kwetsbaarheden, wijzigingen, back-up). [5.20.01]

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| Proceseigenaar | Risicoafweging per inkoop, besluit over restrisico's, afhankelijkheid en exit |
| **[inkoopadviseur]** | Opnemen van de eisen in uitvraag en contract, het inkoopdossier |
| CISO | Advies over de eisen, beoordeling van voorwaarden, bewijs en keten van toeleveranciers |
| Privacy officer of FG | Advies over de verwerkersovereenkomst en de verwerking van persoonsgegevens |
| **[contracteigenaar]** | Overdracht van het inkoopdossier naar contractbeheer |

## 5. Naleving en bewaking

- Per inkoop: het inkoopdossier bevat de risicoafweging, de eisen, de beoordeling van de keten van
  toeleveranciers en het eerste bewijs van de leverancier. Zonder die stukken geeft de CISO geen positief
  advies.
- Jaarlijks: steekproef van ten minste
  **[aantal steekproef inkoop]**
  op de aanwezigheid en kwaliteit van die stukken en op het van de hand wijzen van algemene voorwaarden;
  bewijs is het verslag van de steekproef.
- Jaarlijks: controle of de standaardset eisen en de lijst onaanvaardbare voorwaarden nog actueel zijn.
- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid en het inkoopbeleid van de organisatie. Het
loopt door in het beleid contractbeheer. Het raakt het classificatiebeleid (niveau van de eisen), het
beleid back-up en recovery (afspraken met leveranciers over back-up), het continuïteitsbeleid (exit en
uitwijk), het beleid secure software development (eisen aan ontwikkeling door leveranciers) en het
privacybeleid (verwerkersovereenkomst).

## Bijlage: BIO 2.0-maatregelen

De overheidsmaatregelen van dit domein (8) en waar dit stuk ze invult. Nummers volgens BIO2 v1.3 definitief - 9 januari 2026; de tekst van de maatregel staat bij het CIP.

| Maatregel | Titel | In dit stuk |
|---|---|---|
| 5.19.01 | Informatiebeveiliging in leveranciersrelaties | 3.1 Risicoafweging en eisen in de uitvraag |
| 5.20.01 | Adresseren van informatiebeveiliging in leveranciersovereenkomsten | 3.2 Voorwaarden in het contract |
| 5.20.02 | Adresseren van informatiebeveiliging in leveranciersovereenkomsten | 3.2 Voorwaarden in het contract |
| 5.20.03 | Adresseren van informatiebeveiliging in leveranciersovereenkomsten | 3.3 Bewijs van de leverancier en eigen onderzoek |
| 5.20.04 | Adresseren van informatiebeveiliging in leveranciersovereenkomsten | 3.3 Bewijs van de leverancier en eigen onderzoek |
| 5.20.05 | Adresseren van informatiebeveiliging in leveranciersovereenkomsten | 3.4 Transparantie over kwetsbaarheden en incidenten |
| 5.20.06 | Adresseren van informatiebeveiliging in leveranciersovereenkomsten | 3.5 Afhankelijkheid en exit |
| 5.21.02 | Beheren van informatiebeveiliging in de ICT-toeleveringsketen | 3.6 Keten van toeleveranciers |

## Nog in te vullen

- **drempel risicoafweging inkoop**: de criteria waaronder een inkoop met de standaardset eisen kan
- **lijst onaanvaardbare voorwaarden**: bijvoorbeeld eenzijdig wijzigen van de beveiligingsafspraken of gebruik van gegevens voor eigen doelen van de leverancier
- **meldtermijn leverancier**: bijvoorbeeld 12 uur, zodat de vroege waarschuwing binnen 24 uur kan
- **besluitvormer afwijking soevereiniteit**: wie de afwijking goedkeurt
- **inkoopadviseur**: de functie die het inkoopproces begeleidt
- **contracteigenaar**: de functie die het contract na ondertekening beheert
- **aantal steekproef inkoop**: bijvoorbeeld vijf inkopen met een informatiecomponent
