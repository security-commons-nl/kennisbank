---
domein: leveranciers-contract
titel: Beleid informatiebeveiliging in contractbeheer
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor de looptijd van contracten met
leveranciers die informatie voor de organisatie verwerken of toegang hebben tot haar systemen. Het regelt hoe
de organisatie zicht houdt op haar leveranciers en hun toeleveranciers, hoe ze jaarlijks beoordeelt of de
afspraken worden nagekomen, hoe ze clouddiensten inventariseert en beheert, en hoe ze een contract beëindigt.
Het gaat over de ISO-beheersmaatregelen 5.21 (voor zover tijdens de looptijd), 5.22 en 5.23.

**Voor wie.** Het beleid is primair bedoeld voor de contracteigenaren, de proceseigenaren die de risico's van
een dienst dragen en de afdeling die het contractmanagement uitvoert. Het geldt voor iedereen die namens de
organisatie een contract met een informatiecomponent beheert, een leverancier aanstuurt of een clouddienst
afneemt, ook een afdeling die zelf een dienst heeft aangeschaft.

**Waarop.** Alle lopende contracten met een informatiecomponent: software, clouddiensten, hosting,
beheerdiensten, koppelingen, hardware met onderhoud op afstand en adviesdiensten met toegang tot informatie,
inclusief gratis diensten en diensten die buiten de inkoopfunctie om zijn afgenomen. Is het contractmanagement
zelf uitbesteed, bijvoorbeeld aan een samenwerkingsverband of een regiepartij, dan gelden de eisen uit dit
beleid als minimumeis voor die partij. De organisatie legt dat vast in het contract en toetst de naleving met
een onafhankelijke verklaring, zoals een ISO 27001-certificaat of een ISAE 3402- of ISAE 3000-rapport; het
vastleggen loopt via het beleid informatiebeveiliging bij inkoop, het toetsen via dit beleid.

Buiten dit beleid vallen de eisen vóór het contract (uitvraag, voorwaarden, eerste bewijs, exitregeling), die
staan in het beleid informatiebeveiliging bij inkoop, de inhoud van de verwerkersovereenkomst (privacybeleid)
en de afhandeling van incidenten die een leverancier meldt (beleid beveiligingsincidenten).

::: als samenwerking=centrum
De organisatie sluit contracten ook namens de deelnemers. Het register en de jaarlijkse beoordeling vermelden
per contract voor welke deelnemers het geldt, en de deelnemers krijgen de uitkomst van de beoordeling.
:::

## 2. Uitgangspunten

1. Elk contract met een informatiecomponent heeft een contracteigenaar en een proceseigenaar. De
   proceseigenaar is verantwoordelijk voor de beveiligingsrisico's van de dienst.
2. De beoordeling van een leverancier steunt op bewijs: rapporten van onafhankelijke derden, rapportages uit
   het contract en eigen onderzoek. Een gesprek alleen is geen bewijs.
3. De risico's in de keten van toeleveranciers horen bij de risico's van de organisatie zelf.
4. De zwaarte van de beoordeling volgt uit het impactniveau en het vertrouwelijkheidslabel van de informatie
   die de leverancier verwerkt (beleid informatieclassificatie).

## 3. Beleidsregels

### 3.1 Register van leveranciers en contracten

- [[contracteigenaar: de functie die het contract beheert]] houdt per contract het register van leveranciers
  en contracten met een informatiecomponent bij. Per contract staat erin: de dienst, de contracteigenaar, de
  proceseigenaar, het impactniveau en het vertrouwelijkheidslabel van de informatie, of er een
  verwerkersovereenkomst is, de belangrijkste toeleveranciers, de datum van de laatste beoordeling en de
  einddatum. [5.22.02]
- De contracteigenaar zet een nieuw contract binnen een maand na ondertekening in het register, op basis van
  het inkoopdossier dat de inkoopadviseur overdraagt. Een beëindigd contract blijft erin staan tot de exit is
  afgerond en de leverancier de verwijdering van gegevens schriftelijk heeft bevestigd. [5.22.02]
- Het register staat in [[register leveranciers: de plaats of het systeem waar het register wordt bijgehouden]].
  [[lijneigenaar leveranciersmanagement: de manager die het contractmanagement uitvoert]] is eigenaar van het
  register en stelt elk kwartaal vast dat het register overeenkomt met de contractadministratie van inkoop.
  [5.22.02]

### 3.2 Jaarlijkse beoordeling van de leverancier

- De proceseigenaar beoordeelt elk jaar of de leverancier aan de afgesproken beveiligingseisen voldoet. Hij
  gebruikt daarvoor het bewijs dat de leverancier volgens het contract aanlevert (beleid informatiebeveiliging
  bij inkoop), de rapportages uit de looptijd en de gemelde incidenten en kwetsbaarheden. De beoordeling staat
  met datum in het register. [5.22.01]
- De beoordeling stelt de beveiligingsrisico's vast, bijvoorbeeld een voorbehoud in het rapport, een verlopen
  certificaat, een reikwijdte die de dienst niet meer dekt of een incident dat niet op tijd is gemeld. De
  proceseigenaar laat maatregelen nemen, door de leverancier of door de organisatie zelf, of accepteert een
  restrisico en zet dat in het risicoregister. [5.22.01]
- De CISO adviseert over de beoordeling. Bij een contract voor een kritiek proces of met informatie met het
  label vertrouwelijk of hoger is dat advies verplicht en staat het in het register. [5.22.01]
- De beoordeling volgt een vast format:
  [[format leveranciersbeoordeling: het sjabloon met de vragen en het bewijs per vraag]].
  De lijneigenaar leveranciersmanagement plant de beoordelingen en bewaakt dat ze op tijd zijn. [5.22.01]
- Levert de leverancier het jaarlijkse bewijs niet binnen de termijn uit het contract, dan maant de
  contracteigenaar hem schriftelijk aan en meldt dat aan de proceseigenaar en de CISO. Ontbreekt het bewijs
  drie maanden na de termijn, dan behandelt de proceseigenaar dat als risico in het risicoregister. [5.22.01]

::: als beheer=regie,uitbesteed
- Bij beheer- en hostingpartijen bespreekt de regieorganisatie de beveiligingsrapportage ten minste elk
  kwartaal in het reguliere leveranciersoverleg: incidenten, kwetsbaarheden, patchstand, wijzigingen en
  back-uptests. De verslagen zijn bewijs bij de jaarlijkse beoordeling. [5.22.01]
:::

::: als beheer=eigen
- Bij eigen beheer zijn de meeste contracten licentie- en ondersteuningscontracten. Daarvoor volstaat een
  lichtere jaarlijkse beoordeling door de proceseigenaar: geldigheid van het bewijs, ondersteuningstermijn
  van de software en de meldingen van de leverancier over kwetsbaarheden. [5.22.01]
:::

### 3.3 Keten van toeleveranciers

- Het contract verplicht de leverancier om de beveiligingseisen ook op zijn toeleveranciers toe te passen.
  Laat hij een eis voor een toeleverancier vallen omdat die eis voor diens rol niet van toepassing is, dan
  meldt hij dat met een onderbouwing. De proceseigenaar beoordeelt die onderbouwing bij de jaarlijkse
  beoordeling en legt het oordeel vast. [5.21.03]
- Het contract verplicht de leverancier om tijdens de looptijd elke wijziging in de keten van toeleveranciers
  die de dienst raakt te melden bij de contracteigenaar, met de risico's die hij erin ziet. Ook kwetsbaarheden
  en incidenten bij een toeleverancier die de dienst kunnen raken, meldt hij. [5.21.04]
- Bij een melding over de keten beoordeelt de CISO binnen
  [[beoordelingstermijn ketenwijziging: bijvoorbeeld tien werkdagen]]
  of de risico's aanvaardbaar zijn. De proceseigenaar besluit, en de contracteigenaar legt het besluit vast in
  het register. [5.21.04]
- De CISO neemt de toeleveringsketen mee in de jaarlijkse risicoanalyse van de organisatie. Per directe
  leverancier van een kritieke dienst gaat het over de bekende kwetsbaarheden van de leverancier en zijn
  producten, de kwaliteit van zijn producten en de beveiligingspraktijk van zijn eigen leveranciers, inclusief
  hun manier van veilig ontwikkelen. De uitkomst staat in het risicoregister. [5.21.05]

::: als ketens=digid,suwinet,brp,anders
- Bij leveranciers van diensten voor een landelijke voorziening (zoals DigiD, Suwinet of de BRP) regelt het
  contract dat de leverancier meewerkt aan de audits van dat stelsel en de rapporten op tijd levert. De
  proceseigenaar toetst bij de jaarlijkse beoordeling ook of de leverancier aan de eisen van het stelsel
  voldoet. [5.22.01]
- De contracteigenaar houdt de keten van toeleveranciers voor die diensten apart bij in het register, omdat
  het stelsel eigen voorwaarden stelt aan locatie en uitbesteding. [5.22.02]
:::

### 3.4 Clouddiensten

- De organisatie past een vaste werkwijze toe voor clouddiensten. Die beschrijft hoe de organisatie
  clouddiensten inventariseert, classificeert op de informatie die ze verwerken, selecteert, beoordeelt en
  beheert, en hoe ze de dienst beëindigt. Deze paragraaf en het beleid informatiebeveiliging bij inkoop zijn
  samen die werkwijze; de CISO is er eigenaar van en herziet haar ten minste eens per drie jaar. [5.23.01]
- Inventariseren: de contracteigenaar zet elke clouddienst in het register, ook gratis diensten en diensten
  die een afdeling zelf afneemt. Wie een clouddienst gebruikt die niet in het register staat, meldt dat bij de
  CISO; de CISO laat de dienst binnen een maand opnemen of beëindigen. [5.23.01]
- Selecteren en beoordelen: welke informatie in welke soort clouddienst mag, volgt uit het beleid
  informatieclassificatie. De proceseigenaar neemt clouddiensten mee in de jaarlijkse beoordeling. [5.23.01]
- Beëindigen: elk cloudcontract noemt de situaties waarin de organisatie het contract kan ontbinden,
  bijvoorbeeld een ernstig of herhaald beveiligingsincident, verplaatsing van gegevens naar een land buiten de
  afspraken, overname van de leverancier of het niet leveren van het bewijs. De contracteigenaar controleert
  dat bij opname in het register. [5.23.01]
- Bij een belangrijke wijziging bij de leverancier, zoals een overname, een nieuwe verwerkingslocatie of een
  ingrijpende wijziging van de dienst, beoordeelt de proceseigenaar met de CISO binnen een maand de risico's
  en neemt passende maatregelen, tot en met het uitvoeren van de exitregeling. Het besluit staat in het
  register. [5.23.01]

::: als soevereiniteit=ja
- De contracteigenaar controleert bij de jaarlijkse beoordeling dat de verklaring van de leverancier over de
  locatie van gegevens, back-ups en beheer binnen de Europese Economische Ruimte nog klopt, en meldt elke
  wijziging aan de proceseigenaar en de CISO. [5.23.01]
:::

### 3.5 Beëindigen van een contract

- Bij het einde van een contract voert de contracteigenaar de exitregeling uit: gegevens terug in het
  afgesproken formaat, overdracht aan de opvolger, intrekken van alle toegang van de leverancier op de
  einddatum en een schriftelijke bevestiging van de verwijdering van gegevens. De contracteigenaar legt de
  afronding vast in het register. [5.22.01, 5.23.01]
- Ontbreekt een exitregeling in een lopend contract voor een kritiek proces of voor informatie met het label
  vertrouwelijk of hoger, dan spreekt de contracteigenaar die alsnog af bij de eerstvolgende verlenging, en
  staat het ontbreken tot die tijd in het risicoregister. [5.22.01]

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| Proceseigenaar | Jaarlijkse beoordeling, besluit over restrisico's en wijzigingen in de keten, besluit bij wijzigingen van clouddiensten |
| [[contracteigenaar]] | Register, ontvangst en bewaking van bewijs en rapportages van de leverancier, meldingen over de keten, uitvoering van de exit |
| [[lijneigenaar leveranciersmanagement]] | Eigenaar van dit beleid en van het register; werkwijze, format en planning van de beoordelingen; kwartaalcontrole van het register |
| CISO | Advies bij beoordelingen en ketenwijzigingen, risicoanalyse van de keten, eigenaar en herziening van de werkwijze voor clouddiensten, jaarlijkse toetsing van opzet en werking |
| Privacy officer of FG | Toezicht op verwerkersovereenkomsten en meldingen van datalekken door leveranciers |
| Medewerkers | Melden van clouddiensten die niet in het register staan |

## 5. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in [[registratie van controles: het systeem waarin controles worden vastgelegd, bijvoorbeeld het ticketsysteem of het managementsysteem]];
afwijkingen gaan als bevinding naar het risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| LEV-01 | Nieuwe en beëindigde contracten staan in het register, met alle verplichte velden, en het register komt overeen met de contractadministratie van inkoop | [[lijneigenaar leveranciersmanagement]] | Elk kwartaal | Vergelijking van het register met de contractadministratie, met de afhandeling van de verschillen | 5.22.02 |
| LEV-02 | Elke leverancier in het register heeft een beoordeling van ten hoogste een jaar oud, met het verplichte advies van de CISO waar dat geldt, en het jaarlijkse bewijs is ontvangen | [[lijneigenaar leveranciersmanagement]] | Jaarlijks | Overzicht uit het register met de leveranciers waarvoor de beoordeling of het bewijs ontbreekt of te laat is, met de afhandeling | 5.22.01 |
| LEV-03 | Steekproef op de kwaliteit van ten minste [[aantal steekproef beoordelingen: bijvoorbeeld drie beoordelingen van kritieke diensten]]: gebruikt bewijs, vastgestelde risico's, opvolging, oordeel over de onderbouwing van de leverancier over zijn toeleveranciers | CISO | Jaarlijks | Verslag van de steekproef met de bevindingen | 5.21.03, 5.22.01 |
| LEV-04 | Meldingen over wijzigingen, kwetsbaarheden en incidenten in de keten zijn binnen de beoordelingstermijn beoordeeld en het besluit staat in het register | CISO | Jaarlijks | Overzicht van de ketenmeldingen van het jaar met datum van melding, beoordeling en besluit | 5.21.04 |
| LEV-05 | De risicoanalyse van de organisatie bevat de toeleveringsketen van elke kritieke dienst en is in het afgelopen jaar bijgewerkt | CISO | Jaarlijks | Risicoanalyse met datum en de opgenomen leveranciers | 5.21.05 |
| LEV-06 | Alle clouddiensten in gebruik staan in het register, elk cloudcontract bevat de ontbindingsgronden, en wijzigingen bij cloudleveranciers zijn binnen een maand beoordeeld | [[lijneigenaar leveranciersmanagement]] | Jaarlijks | Vergelijking van het register met een inventarisatie van clouddiensten in gebruik (bijvoorbeeld uit de identiteitsvoorziening of de netwerklogging), contracten, besluiten | 5.23.01 |
| LEV-07 | De werkwijze voor clouddiensten is in de afgelopen drie jaar herzien en vastgesteld | CISO | Eens per drie jaar | Vastgestelde versie met datum | 5.23.01 |
| LEV-08 | Beëindigde contracten hebben een afgeronde exit: gegevens terug, toegang ingetrokken op de einddatum, bevestiging van verwijdering ontvangen | [[lijneigenaar leveranciersmanagement]] | Jaarlijks | Overzicht van de beëindigde contracten van het jaar met de exitstukken per contract | 5.22.01, 5.23.01 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De
proceseigenaar dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de looptijd. De
afwijking geldt pas na acceptatie van het risico door [[risico-eigenaar: de manager die restrisico's accepteert]]
en staat in het risicoregister; afwijkingen worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid en volgt op het beleid informatiebeveiliging
bij inkoop (eisen, eerste bewijs, exitregeling). Het raakt het beleid informatieclassificatie (welke informatie
waar mag en hoe zwaar de beoordeling is), het beleid beveiligingsincidenten (meldingen van leveranciers), het
beleid kwetsbaarheden en patchmanagement (meldingen over kwetsbaarheden in de keten), het continuïteitsbeleid
(exit en afhankelijkheid), het beleid logische toegang (intrekken van toegang bij het einde van een contract)
en het privacybeleid (verwerkersovereenkomsten).
