# Het model: van strategisch risico naar de maatregel die eerst moet

Bijlage bij [GRC voor security, privacy en continuïteit](README.md). Hier staan de regels van het register:
de lagen, de relaties, het schema van een bevinding, het niveau van een maatregel en de prioriteit. Het
[voorbeeld van Duinstad](voorbeeld-register.md) is met deze regels doorgerekend; het script
`tools/bouw_risicoregister.py` in de kennisbank voert ze uit.

## 1. Doel

Het register beantwoordt één vraag: welke maatregel en welke control pakken we eerst, en waarom.
Verantwoording aan de directie en de auditor volgt daaruit. Voor sturen is een rangorde genoeg; het
register rekent daarom geen restrisico uit.

## 2. Vijf lagen

| Laag | Wat het is | Waar het vandaan komt |
|---|---|---|
| **SR** · strategisch risico | Risico op het niveau van de directie, met kans en impact | De strategische risicoanalyse |
| **OR** · operationeel risico | Risico uit een standaardlijst per kader | Zie de tabel hieronder |
| **Bevinding** | Aangetoond feit over een maatregel die niet werkt, met bron, datum en score | Toetsen, incidenten, metingen, tests, analyses (§4) |
| **Maatregel** | Eenheid uit de maatregelenlijst van een kader | Verklaring van toepasselijkheid, BCM-set, privacykader |
| **Control** | Toetsbare beheersactiviteit met eigenaar, frequentie en bewijs | Het controleraamwerk bij het beleid |

| Kader | Standaardlijst voor de OR's | Maatregelen | Stand per maatregel in de bron |
|---|---|---|---|
| **BIO 2.0** | Per ISO 27002-control een risicoformulering; verwante controls mogen samen één OR vormen | De toepasselijke overheidsmaatregelen uit de verklaring van toepasselijkheid | Geïmplementeerd of niet |
| **BCM** (ISO 22301) | Per thema van de eigen BCM-maatregelenset | De BCM-maatregelen | Voltooid, deels of niets |
| **Privacy** (AVG) | Per thema van het privacykader, bijvoorbeeld het AVG-borgingsproduct van de IBD | De normen van dat kader | Opzet, bestaan en werking als groen, oranje of rood |

Neem bronnen die er al zijn. Een register dat een nieuwe maatregelenlijst vraagt, haalt niemand bij.

## 3. Relaties

1. **SR naar OR: één op veel.** Elk OR heeft precies één primair SR. Dat SR geeft het gewicht.
   a. Een SR zonder OR is niet onderbouwd. Dat is een melding, geen fout.
   b. Een OR zonder passend SR hangt onder *buiten de risicoanalyse*. Dat zegt iets over de
      risicoanalyse: ontbreekt er een strategisch risico?
2. **OR naar maatregel: één OR per maatregel.** Het OR volgt uit de standaardlijst van het eigen kader:
   een BIO 2.0-maatregel via zijn ISO-control, een BCM- of privacymaatregel via zijn thema. Een maatregel
   hangt nooit onder een OR van een ander kader.
3. **Bevinding naar maatregel: veel op veel.** Een bevinding noemt per maatregel wat aantoonbaar niet
   werkt, met een reden. Het OR en het SR volgen daaruit (§4.2).
4. **Maatregel naar control: veel op veel.** Eén control kan meer maatregelen toetsen, en één maatregel
   kan door meer controls worden getoetst.

## 4. Bevindingen

### 4.1 Wat een bevinding is

Een aangetoond feit dat laat zien dat een maatregel niet werkt, of niet bestaat terwijl de organisatie
denkt dat hij er is. Twee dingen zijn geen bevinding:

1. **Een kaderstand.** "Niet geïmplementeerd", rood in het privacykader of "niet voltooid" in de BCM-set
   is een gat dat al meetelt via het niveau (§5). Wie er een bevinding van maakt, telt het dubbel.
2. **Een zorg of verwachting.** Zonder vastgesteld feit, datum en bron is het een risico-inschatting.
   Die hoort in een risicosessie over het OR.

### 4.2 Afleiding: de maatregel is het anker

1. De bevinding noemt één of meer maatregelen met hun sleutel (`BIO2:8.08.02`, `BCM:8.5`, `AVG:A15`),
   elk met een reden.
2. Het primaire OR is het OR van de eerste maatregel. De overige maatregelen geven de secundaire OR's.
   Het SR is het SR van het primaire OR. Niemand typt een OR of SR bij een bevinding.
3. Het menselijke oordeel zit in twee dingen: welke maatregel faalt, en de score (kans maal impact).
4. **Uitzondering.** Past geen enkele maatregel, dan mag een bevinding direct onder een OR hangen, met
   een motivering. Elke uitzondering wordt gemeld, want ze wijst op een gat in de standaardlijst of de
   maatregelenset.

### 4.3 Schema

| Veld | Verplicht | Inhoud |
|---|---|---|
| code | ja | B-nn, doorlopend, nooit hergebruikt |
| titel | ja | Het gat als patroon, één niveau smaller dan het OR |
| aangetoond | ja | Wat is vastgesteld, door wie (rol) en wanneer |
| bronsoort | ja | toets, incident, meting, test of analyse |
| bron | ja | Document en vindplaats |
| peildatum | ja | Datum van het feit. Ouder dan twaalf maanden zonder herbevestiging wordt gemeld |
| maatregelen | ja | Sleutels met reden per maatregel; de eerste bepaalt het primaire OR |
| uitzondering | nee | OR plus motivering, alleen als geen maatregel past |
| kans, impact | ja | Elk 1 tot en met 5; score is kans maal impact |
| status | ja | kandidaat, open, in behandeling, geaccepteerd of gesloten, met datum |
| acceptatie | bij geaccepteerd | Het besluit van de risico-eigenaar, met termijn |
| detail | nee | Verwijzing naar een gerubriceerd blad; exploiteerbare details staan nooit in het register |

### 4.4 De titel is het gat, aangetoond is het bewijs

Een bevinding benoemt een patroon, geen gebeurtenis. "Kritieke kwetsbaarheden in extern bereikbare
systemen blijven langer open dan de patchtermijn" is een bevinding. "Het VPN-incident van maart" is
bewijs, en staat onder *aangetoond*. Breder is sterker, binnen drie grenzen:

1. **Smaller dan het OR.** Is de titel gelijk aan het OR, dan zegt de bevinding niets meer dan het risico.
2. **Gedragen door het bewijs.** Minstens twee onafhankelijke bewijsstukken, of één meting over de hele
   populatie. Eén incident plus het woord "structureel" is een mening.
3. **Sluitbaar.** Er is één eigenaar denkbaar die het kan oplossen, en het is te zeggen hoe "opgelost"
   eruitziet.

### 4.5 Status

Alleen *open* en *in behandeling* tellen mee in het niveau en de prioriteit.

- *Kandidaat* telt niet. Pas als de CISO hem aanneemt, wordt hij open.
- *Geaccepteerd* telt niet: de risico-eigenaar heeft besloten niet te behandelen. De bevinding blijft
  zichtbaar, met het besluit en de termijn.
- *Gesloten* vraagt bewijs dat de maatregel nu werkt.

### 4.6 Waar bevindingen vandaan komen

| Bronsoort | Voorbeelden | Hoe het een bevinding wordt |
|---|---|---|
| Toets | Toets van een control door de tweede of derde lijn, toets van de FG, audit, managementletter | Werking of bestaan negatief getoetst, met bewijs |
| Incident | Incidentregister, datalekken, meldingen onder de Cbw | Het incident laat zien welke maatregel faalde |
| Meting | Configuratie-exports, kwetsbaarheidsscans, logs | Een meetwaarde met datum die de maatregel weerspreekt |
| Test | Pentest, hersteltest, oefening | Een geslaagde aanval of een mislukte hersteltest |
| Analyse | Risicoanalyse langs aanvalspaden, DPIA, bedrijfsimpactanalyse | Een vastgestelde tekortkoming in het rapport |

## 5. Niveau: opzet, bestaan, werking

Het niveau van een maatregel is cumulatief: 0 niet in orde of onbekend, 1 opzet, 2 bestaan, 3 werking.

1. **Uit de bron, per kader.** Privacy: werking groen (met opzet en bestaan groen) is 3, anders bestaan
   groen is 2, anders opzet groen is 1, anders 0. Oranje telt niet. BCM: voltooid is 2, deels is 1, niets
   is 0. BIO 2.0: geïmplementeerd is 2, anders 0. Een zelfbeoordeling komt nooit verder dan bestaan.
2. **Controls.** Heeft een maatregel getoetste controls, dan geldt de zwakste: het niveau is het laagste
   niveau van de controls die hem toetsen. Alleen zo komt een maatregel op werking.
3. **Geldigheid.** Werking vervalt als een control een toetsronde mist. Het niveau zakt dan naar bestaan.
4. **Meetellende bevinding.** Een open bevinding op een maatregel betekent dat de werking aantoonbaar niet
   in orde is: het niveau is hooguit 2.
5. **Onbekend telt als niet in orde.** Niet getoetst is 0.

## 6. Prioriteit

Prioriteit is gewicht maal gat. De rangorde:

1. Eerst de maatregelen onder een OR met een meetellende bevinding, want daar is het gat aangetoond.
   Daarbinnen op de score van het OR, dan op de score van het SR. De score van een OR is de hoogste score
   van de meetellende bevindingen waarvan het het primaire OR is. Een secundaire relatie telt niet mee,
   anders weegt één bevinding meer keren.
2. Daarna de maatregelen onder een OR zonder bevinding, op de score van het SR. *Buiten de
   risicoanalyse* telt als laagste gewicht.
3. Bij gelijke stand het laagste niveau eerst. Een maatregel op werking zakt naar achteren.

Wat de lijst niet doet: een restrisico berekenen. Of een restrisico aanvaardbaar is, besluit de
risico-eigenaar met de acceptatieladder van de eigen risicoanalyse. Een gebruikelijke ladder: kritiek naar
de directie, hoog naar het tactisch overleg met een termijn, gemiddeld bij het tactisch overleg, laag bij
de eigenaar.

## 7. Twee soorten eigenaar

1. **Beheerseigenaar** van maatregel en control: richt in, voert uit en levert het bewijs. Staat in de
   bron van het kader.
2. **Risico-eigenaar** van OR en SR: kiest de behandeling en accepteert restrisico. Staat in het
   risicoregister van de organisatie.

Het voorbeeld toont alleen de beheerseigenaar, als rol. Wie welk risico draagt, hoort in het eigen register.

## 8. Wat de generator doet

Het script `tools/bouw_risicoregister.py` (of prompt 3 in [`prompts.md`](prompts.md)) doet drie dingen:

1. **Toetsen.** Het weigert een bevinding zonder maatregel of motivering, zonder bron of peildatum, met
   een onbekende maatregelsleutel, een onbekende status of bronsoort, of een dubbele code. Een maatregel
   onder een OR van een ander kader en een geaccepteerde bevinding zonder besluit worden ook geweigerd.
2. **Afleiden.** OR en SR uit de maatregel, het niveau per maatregel, de score per OR.
3. **Melden.** Uitzonderingen en feiten ouder dan twaalf maanden.

Het bedenkt geen bevindingen. Wat erin staat, heeft een mens aangenomen.
