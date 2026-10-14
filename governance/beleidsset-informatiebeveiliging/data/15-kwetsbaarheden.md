---
domein: kwetsbaarheden
titel: Beleid kwetsbaarheden en patchmanagement
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor het vinden, beoordelen en verhelpen
van technische kwetsbaarheden, voor het hardenen van systemen en voor de bescherming tegen malware. Het
gaat over de ISO-beheersmaatregelen 8.07, 8.08 en 8.09.

Het beleid geldt voor alle ICT-middelen waarmee de organisatie informatie verwerkt: werkplekken, mobiele
apparaten, servers, netwerkcomponenten, databases, applicaties en clouddiensten, ook als een leverancier
ze beheert. Het geldt voor eigen beheerders, leveranciers en iedereen die software installeert of
configureert.

Buiten dit beleid vallen het melden en afhandelen van incidenten (beleid beveiligingsincidenten), meldingen
van buiten via de CVD-procedure (idem) en de inrichting van het netwerk (beleid netwerkbeveiliging).

## 2. Uitgangspunten

1. Wat de organisatie niet kent, kan zij niet patchen. Het overzicht van ICT-middelen uit het beleid
   bedrijfsmiddelenbeheer is de basis voor scannen en patchen.
2. De termijn voor het verhelpen van een kwetsbaarheid volgt uit kans op misbruik en verwachte schade.
3. Een systeem draait alleen wat het nodig heeft. Wat overbodig is, gaat uit of eraf.
4. Kan een kwetsbaarheid niet op tijd worden verholpen, dan is er een vastgelegde risicoafweging met
   tijdelijke maatregelen en een eigenaar.

## 3. Beleidsregels

### 3.1 Bescherming tegen malware

- Op alle werkplekken, servers en mailvoorzieningen draait antimalware-software. De software en de
  bijbehorende herstelsoftware worden automatisch bijgewerkt; een apparaat dat langer dan zeven dagen geen
  update heeft ontvangen, verschijnt als afwijking in het beheeroverzicht en wordt binnen een week
  hersteld of van het netwerk gehaald. [8.07.03]
- Gescand wordt: alle omgevingen (werkplekken, servers, mailverkeer en apparaten die verbinding maken met
  het netwerk), alle downloads vóór ze worden geopend of opgeslagen, en alle bestanden die via mail, een
  koppeling of een opslagmedium binnenkomen, vóór gebruik. [8.07.04]
- Downloaden is beperkt op basis van risico en noodzaak. Uitvoerbare bestanden en scripts van internet
  worden standaard tegengehouden; een uitzondering vraagt de gebruiker aan bij de servicedesk. Alle
  downloads gaan langs de antimalware-controle. [8.07.01]
- Medewerkers krijgen bij indiensttreding en daarna elk jaar voorlichting over veilig surfen, phishing en
  het klikken op onbekende links. Een phishing-simulatie maakt deel uit van het jaarprogramma
  bewustwording. [8.07.02]

### 3.2 Hardening en configuratie

- Voor elk type systeem (werkplek, server, netwerkcomponent, clouddienst) is een vastgestelde
  basisconfiguratie, gebaseerd op een erkende baseline zoals de CIS Benchmarks. Overbodige diensten,
  poorten, software en accounts staan uit of zijn verwijderd. Standaardwachtwoorden worden vóór
  ingebruikname vervangen.
- Alleen beheerders mogen software installeren of functies activeren. Gebruikers hebben op hun werkplek
  geen beheerrechten.
- Afwijkingen van de basisconfiguratie worden elk kwartaal automatisch gemeten. Een afwijking wordt
  hersteld of als uitzondering vastgelegd met een risicoafweging.

### 3.3 Kwetsbaarheden vinden

- Alle ICT-middelen worden ten minste maandelijks gescand op kwetsbaarheden en misconfiguraties, en
  opnieuw na een grote wijziging. Waar mogelijk gebruikt de organisatie agents op de eindpunten zodat ook
  apparaten buiten kantoor worden meegenomen.
- De CISO volgt de waarschuwingen van het NCSC en de sectorale CERT. Een waarschuwing die een gebruikt
  product raakt, wordt binnen één werkdag aan de systeemeigenaar doorgezet.
- Informatiesystemen worden jaarlijks gecontroleerd op technische naleving van de beveiligingseisen, met
  een kwetsbaarheidsanalyse, een penetratietest of een red-teamingtest. Welke vorm per systeem, bepaalt
  de CISO op basis van de classificatie. [8.08.04]
- Systemen die vanaf internet bereikbaar zijn, worden continu op kwetsbaarheden gescand, bijvoorbeeld met
  een geautomatiseerde externe scan, en ten minste jaarlijks getest. [8.08.04, 8.08.05]
- Bij elke nieuwe release of grote update van een internetbereikbaar systeem volgt een penetratietest,
  waar mogelijk geautomatiseerd. Een bevinding met hoog risico die niet op een andere manier kan worden
  gemitigeerd, houdt de release tegen: het systeem gaat dan niet in productie. [8.08.05]
- Penetratietesten worden uitgevoerd door een partij die onafhankelijk is van de bouwer en de beheerder
  van het systeem, met een vooraf afgesproken methode en reikwijdte.

::: als ontwikkeling=ja
- Voor software die de organisatie zelf bouwt, worden de broncode en de gebruikte bibliotheken bij elke
  build automatisch gescand op bekende kwetsbaarheden. Een kritieke bevinding in een bibliotheek stopt de
  build. Elke applicatie heeft een actuele lijst van gebruikte componenten (SBOM). [8.08.05]
- De pentest bij een release van een zelfgebouwde internetbereikbare applicatie staat in de
  releaseprocedure als poort; de ontwikkelaar levert het testrapport aan bij de wijzigingsaanvraag. [8.08.05]
:::

::: als ontwikkeling=nee
- De organisatie bouwt zelf geen software. Bij inkoop en contractverlenging eist zij van de leverancier
  een pentest bij elke grote release van een internetbereikbaar systeem, inzage in het rapport en het
  verhelpen van hoge bevindingen vóór de release in productie gaat. [8.08.05]
:::

### 3.4 Beoordelen en verhelpen

- Elke gevonden kwetsbaarheid krijgt een risico-inschatting op basis van kans op misbruik en verwachte
  schade, waarbij de classificatie van het systeem en de bereikbaarheid vanaf internet meewegen. Op basis
  van die expliciete afweging kiest de systeemeigenaar de maatregel: patchen, de configuratie aanpassen,
  de functie uitzetten of het systeem afschermen. [8.08.02]
- Termijnen voor het verhelpen:

| Risico | Termijn |
|---|---|
| Kans op misbruik hoog en schade hoog | zo snel mogelijk, uiterlijk binnen een week |
| Overig hoog | binnen een maand |
| Gemiddeld | binnen drie maanden |
| Laag | bij de eerstvolgende reguliere update |

- Bij hoge kans en hoge schade zijn de mitigerende maatregelen uiterlijk binnen een week getroffen. Bij
  actief misbruik werkt de organisatie dezelfde dag. [8.08.01]
- Kan de patch niet binnen een week, of is er nog geen patch, dan treft de systeemeigenaar direct
  tijdelijke maatregelen op basis van een vastgelegde risicoafweging, bijvoorbeeld de functie uitzetten,
  de toegang beperken of extra bewaking. De afweging noemt het restrisico, de einddatum en wie het
  restrisico accepteert. [8.08.03]
- Software waarvoor de leverancier geen beveiligingsupdates meer levert, wordt vervangen. Zolang dat niet
  is gebeurd, staat het systeem afgeschermd en als risico in het risicoregister.
- Na het verhelpen controleert een herhaalscan dat de kwetsbaarheid weg is. Pas dan wordt de melding
  gesloten.

::: als beheer=eigen
- De eigen beheerorganisatie installeert beveiligingsupdates voor werkplekken en servers volgens een vast
  maandelijks venster, met een spoedprocedure voor de weekregel. Patchen loopt via wijzigingsbeheer; een
  spoedpatch mag achteraf worden geregistreerd. [8.08.01]
:::

::: als beheer=regie,uitbesteed
- Het beheer is uitbesteed. Het contract met de beheerpartij bevat de termijnen uit de tabel hierboven,
  de plicht om binnen één werkdag te melden welke systemen een kritieke waarschuwing raakt, en een
  maandelijkse rapportage over openstaande kwetsbaarheden en de patchstand. [8.08.01]
- De organisatie ontvangt de scanresultaten zelf of laat de scan door een andere partij doen dan de
  beheerder, zodat zij de rapportage kan controleren.
:::

::: als beheer=uitbesteed
- Omdat er geen eigen beheerorganisatie is, wijst de organisatie een contractmanager aan die de
  patchrapportage elke maand bespreekt met de leverancier en afwijkingen aan de CISO meldt.
:::

### 3.5 Registreren en rapporteren

- Alle open kwetsbaarheden met risico gemiddeld of hoger staan in een register met systeem, risico,
  eigenaar, termijn en status. Termijnoverschrijdingen zijn zichtbaar.
- De CISO rapporteert maandelijks aan de directie het aantal open kwetsbaarheden per risiconiveau, de
  overschrijdingen en de geaccepteerde restrisico's.

::: als capaciteit=geen
- Er is geen eigen ISO. De scans en de risico-inschatting worden uitgevoerd door een externe partij;
  [[functionaris informatiebeveiliging: de medewerker die dit als neventaak heeft]] bespreekt de
  maandrapportage met die partij en legt besluiten vast.
:::

::: als capaciteit=parttime,team
- De ISO beoordeelt de scanresultaten, filtert valse meldingen en zet open punten uit bij de
  systeemeigenaren.
:::

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| Systeemeigenaar | Risico-inschatting, keuze van de maatregel, risicoafweging bij uitstel, acceptatie restrisico binnen de eigen bevoegdheid |
| [[beheerorganisatie: de eigen afdeling of de leverancier die de systemen beheert]] | Antimalware, basisconfiguratie, patchen en herhaalscans |
| CISO | Scanprogramma, opvolging CERT-waarschuwingen, pentestplanning, maandrapportage, toetsing van risicoafwegingen |
| [[lijneigenaar kwetsbaarhedenbeheer: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd ICT]] | Uitvoering van dit beleid en de middelen ervoor |
| Medewerkers | Geen software installeren buiten de regels om en verdachte bestanden of links melden |

## 5. Naleving en bewaking

- Maandelijks: rapportage van open kwetsbaarheden, termijnoverschrijdingen en patchstand; bewijs is het
  rapport met de scanresultaten.
- Per kwartaal: meting van afwijkingen van de basisconfiguratie en van apparaten met verouderde
  antimalware; bewijs is de meting met de afhandeling.
- Jaarlijks: controle dat elk informatiesysteem en elk internetbereikbaar systeem in het testprogramma zit
  en is getest; bewijs is het overzicht met de testrapporten.
- Per release van een internetbereikbaar systeem: het pentestrapport bij de wijziging.
- Jaarlijks: steekproef van vijf uitgestelde kwetsbaarheden op een volledige risicoafweging en op het
  nakomen van de einddatum.
- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid
bedrijfsmiddelenbeheer (het overzicht van ICT-middelen), het beleid wijzigingsbeheer (patchen en releases),
het beleid secure software development (eigen code), het beleid beveiligingsincidenten (CVD en
waarschuwingen), het beleid leveranciersbeheer (patchtermijnen in contracten) en het beleid screening,
bewustzijn en opleiding (voorlichting).
