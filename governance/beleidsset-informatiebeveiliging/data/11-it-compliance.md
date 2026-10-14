---
domein: it-compliance
titel: Beleid IT-compliance
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor de naleving van wet- en
regelgeving en contractuele eisen die op informatie en informatiesystemen van de organisatie rusten. Het
regelt hoe de organisatie weet welke eisen gelden, hoe registraties en bewaartermijnen zijn ingericht,
hoe werkplekken en schermen worden afgeschermd en hoe systemen tijdens audits beschermd blijven. Het gaat
over de ISO-beheersmaatregelen 5.31 tot en met 5.34, 7.07, 8.06, 8.11, 8.12, 8.17 en 8.34.

Het beleid geldt voor alle informatiesystemen in de scope van het managementsysteem en voor iedereen die
ermee werkt. Het is bedoeld voor proceseigenaren, de archieffunctie, de privacy officer, de IT-organisatie en
de CISO.

## 2. Uitgangspunten

1. De proceseigenaar weet welke wettelijke en contractuele eisen op zijn proces rusten en is verantwoordelijk
   voor de naleving.
2. Informatie wordt niet langer bewaard dan nodig, en niet korter dan de wet voorschrijft.
3. Naleving is aantoonbaar met registraties die de organisatie zelf bijhoudt.

## 3. Beleidsregels

### 3.1 Wettelijke en contractuele eisen

- De CISO houdt samen met de privacy officer en de juridische functie een register bij van de wet- en
  regelgeving en de contractuele eisen die gelden voor informatiebeveiliging, met per eis de eigenaar en het
  beleidsstuk waarin hij is uitgewerkt. Het register wordt jaarlijks en bij elke relevante wetswijziging
  bijgewerkt.
- Het register bevat ten minste de AVG, de Archiefwet, de Cyberbeveiligingswet waar die geldt en de
  sectorale wetgeving van de eigen taken.
- De organisatie gebruikt alleen software waarvoor een geldige licentie is. De IT-organisatie houdt de
  licenties bij en vergelijkt ze jaarlijks met de geïnstalleerde software.

::: als politiegegevens=ja
- De organisatie verwerkt politiegegevens, bijvoorbeeld door boa's of bij handhaving en opsporing. Voor die
  verwerkingen geldt de Wet politiegegevens naast de AVG. Het register noemt per verwerking het doel uit de
  Wpg, de geautoriseerde functies en de bewaartermijn.
- Autorisaties voor politiegegevens worden per persoon verleend en ten minste halfjaarlijks door de
  proceseigenaar gecontroleerd. Elke raadpleging en wijziging wordt gelogd; de logging wordt bewaard
  zolang de Wpg voorschrijft.
- Over de verwerking van politiegegevens laat de organisatie de periodieke privacy-audit uitvoeren die de
  Wpg voorschrijft en stuurt het rapport naar de Autoriteit Persoonsgegevens.
:::

::: als ketens=digid,suwinet,brp,bag,anders
- De organisatie is aangesloten op landelijke voorzieningen met een eigen beveiligings- en auditregime. Het
  register noemt per aansluiting het normenkader, de eigenaar en de termijn van de verantwoording.
:::

::: als ketens=digid
- Voor de DigiD-aansluiting laat de organisatie jaarlijks een ICT-beveiligingsassessment door een
  onafhankelijke auditor uitvoeren en levert het rapport op tijd aan bij de beheerder van DigiD.
:::

::: als ketens=suwinet
- Voor Suwinet legt de organisatie jaarlijks verantwoording af over de normen voor gebruik en beveiliging.
  De proceseigenaar controleert per kwartaal de autorisaties en steekproefsgewijs de raadplegingen op
  doelbinding.
:::

::: als ketens=brp
- Voor de BRP voert de organisatie de jaarlijkse zelfevaluatie of audit uit die de beheerder van de BRP
  voorschrijft, en controleert de proceseigenaar de autorisaties ten minste jaarlijks.
:::

::: als ketens=bag
- Voor de BAG en andere basisregistraties waarvoor de organisatie bronhouder is, voert de organisatie de
  verplichte kwaliteitscontroles en audits uit en volgt de bevindingen op.
:::

::: als ketens=anders
- Voor andere ketens met eigen beveiligingseisen staat het normenkader en de wijze van verantwoording in
  [[overzicht overige ketens: per keten het normenkader, de eigenaar en de auditcyclus]].
:::

### 3.2 Registraties en bewaartermijnen

- De proceseigenaar legt voor elk informatiesysteem en elke categorie informatie de bewaartermijn vast, op
  basis van de geldende selectielijst, de Archiefwet, de privacywetgeving en de eigen bedrijfsdoelen. De
  termijnen staan in het verwerkingsregister of in een overzicht dat de archieffunctie bijhoudt. [5.33.01]
- De proceseigenaar zorgt dat het systeem de termijnen ook uitvoert: vernietiging, overbrenging of
  anonimisering na afloop, automatisch waar het systeem dat kan en volgens een vast schema waar dat niet kan.
  [5.33.01]
- De proceseigenaar toetst ten minste jaarlijks met een steekproef of informatie na afloop van de termijn
  daadwerkelijk is vernietigd of overgebracht, en legt de uitkomst vast. [5.33.01]
- Bij aanschaf of vervanging van een systeem is de mogelijkheid om bewaartermijnen uit te voeren een eis in
  het programma van eisen. [5.33.01]
- Registraties die als bewijs dienen (zoals logging, besluiten en audit trails) zijn beschermd tegen
  wijziging en voortijdige verwijdering.

### 3.3 Privacy en persoonsgegevens

- De privacymaatregelen staan in het privacybeleid. Dit beleid regelt alleen de raakvlakken: het register
  van eisen (3.1) en de bewaartermijnen (3.2) gelden ook voor persoonsgegevens.
- In test- en ontwikkelomgevingen worden geen echte persoonsgegevens gebruikt, tenzij ze zijn gemaskeerd of
  gepseudonimiseerd en de privacy officer heeft ingestemd.
- De IT-organisatie zet maatregelen in tegen het onbedoeld weglekken van gevoelige gegevens, zoals
  waarschuwingen of blokkades bij het versturen van gegevens met een hoge classificatie naar externe
  adressen. De keuze volgt uit de risicoanalyse.

### 3.4 Clear desk en clear screen

- Medewerkers laten geen vertrouwelijke informatie onbeheerd achter op hun werkplek, printer of in
  vergaderruimten, en vergrendelen hun scherm wanneer zij de werkplek verlaten.
- Werkplekken vergrendelen automatisch na
  [[vergrendeltijd: het aantal minuten inactiviteit, bijvoorbeeld 10]]
  minuten zonder activiteit.
- Waar toegang tot systemen werkt met een chipcard, pas of andere fysieke token, vergrendelt de werkplek
  automatisch zodra het token wordt verwijderd. De IT-organisatie stelt dat centraal in, zodat gebruikers het
  niet kunnen uitzetten. [7.07.01]
- Werkt de organisatie niet met een fysieke token, dan geldt de vorige regel voor elke toekomstige invoering
  ervan en is hij een eis bij de aanschaf. [7.07.01]

### 3.5 Techniek ter ondersteuning van naleving

- De IT-organisatie bewaakt de capaciteit van kritieke systemen (opslag, rekenkracht, netwerk) en signaleert
  tekorten voordat ze de beschikbaarheid raken.
- Alle systemen synchroniseren hun klok met een betrouwbare tijdbron, zodat logging uit verschillende
  systemen vergelijkbaar is.

### 3.6 Audits op informatiesystemen

- Audits en technische tests op productiesystemen worden vooraf afgestemd met de systeemeigenaar en de
  IT-organisatie: wat wordt getest, door wie, wanneer en met welke rechten.
- Auditors krijgen bij voorkeur alleen-lezen toegang. Rechten worden na afloop direct ingetrokken.
- Tests die de beschikbaarheid kunnen raken, gebeuren buiten piektijden of op een kopie.

::: als capaciteit=geen
- Zonder eigen ISO houdt
  [[functionaris informatiebeveiliging: de medewerker met de neventaak informatiebeveiliging]]
  het register uit 3.1 bij. De jaarlijkse controle op het register en op de steekproef bewaartermijnen wordt
  belegd bij de CISO-invulling of de interne controle.
:::

::: als capaciteit=parttime,team
- De ISO of CISO houdt het register uit 3.1 bij en voert de jaarlijkse controle op de bewaartermijnen uit
  samen met de archieffunctie.
:::

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| Proceseigenaar | Naleving van de eisen op het eigen proces, bewaartermijnen vastleggen, uitvoeren en toetsen |
| [[lijneigenaar archief: de functie die de archieffunctie uitvoert, bijvoorbeeld de DIV-coördinator]] | Overzicht van bewaartermijnen, selectielijst, ondersteuning bij vernietiging en overbrenging |
| CISO of ISO | Register van eisen, advies, controle op naleving |
| Privacy officer en FG | Privacyeisen, maskeren in testomgevingen; de FG houdt toezicht |
| IT-organisatie | Automatische vergrendeling, licenties, capaciteit, kloksynchronisatie, begeleiding van audits |
| Medewerkers | Clear desk en clear screen |

## 5. Naleving en bewaking

- Jaarlijks: actualisering van het register van wettelijke en contractuele eisen; bewijs is de versie met
  datum en de lijst van wijzigingen.
- Jaarlijks: steekproef per kritiek systeem op de uitvoering van bewaartermijnen; bewijs is het
  vernietigingsverslag of de overbrengingsverklaring.
- Jaarlijks: technische controle dat automatische vergrendeling (op inactiviteit en bij verwijderen van een
  token) op alle werkplekken aanstaat; bewijs is de configuratie-export.
- Halfjaarlijks: rondgang clear desk door de ISO of de lijneigenaar, met een kort verslag.

::: als volwassenheid=startend,bio1
- De controles hierboven worden eerst ingevoerd voor de systemen met de hoogste classificatie. Binnen twee
  jaar dekken ze alle systemen in de scope.
:::

::: als volwassenheid=bio2-opbouw,bio2-werkend
- Elke controle hierboven is een control in het controleraamwerk, met eigenaar, frequentie en bewijs.
:::

::: als politiegegevens=ja
- Halfjaarlijks: controle van de autorisaties voor politiegegevens; periodiek: de Wpg-audit en de
  opvolging van de bevindingen.
:::

- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het privacybeleid
(persoonsgegevens en bewaartermijnen), het beleid logische toegangsbeveiliging (vergrendeling en
autorisaties), het beleid logging en monitoring (bewaren van logging en kloksynchronisatie), het beleid
informatieclassificatie (gegevenslekken) en het beleid secure software development (testdata).
