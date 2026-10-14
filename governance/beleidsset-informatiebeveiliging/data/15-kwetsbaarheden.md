---
domein: kwetsbaarheden
titel: Beleid kwetsbaarheden en patchmanagement
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor het vinden, beoordelen en verhelpen
van technische kwetsbaarheden, voor het beheren van de configuratie van systemen en voor de bescherming
tegen malware. Het legt vast wie scant, wie beoordeelt, binnen welke termijn een kwetsbaarheid verholpen is
en waaruit dat blijkt, zodat bekende zwakke plekken niet de ingang worden voor een aanval. Het gaat over de
ISO-beheersmaatregelen 8.7, 8.8 en 8.9.

**Voor wie.** Het beleid is primair bedoeld voor de beheerorganisatie, de systeemeigenaren en de CISO. De
gedragsregels over downloaden en installeren gelden voor iedereen die met een apparaat of account van de
organisatie werkt: medewerkers, inhuur, stagiairs en leveranciers.

**Waarop.** Alle ICT-middelen waarmee de organisatie informatie verwerkt: werkplekken, mobiele apparaten,
servers, netwerkcomponenten, databases, applicaties, koppelingen en clouddiensten. Is het beheer van die
middelen of een dienst uitbesteed, dan gelden de eisen uit dit beleid als minimumeis voor de leverancier.
De organisatie legt dat vast in het contract en toetst de naleving met een onafhankelijke verklaring, zoals
een ISO 27001-certificaat of een ISAE 3402- of ISAE 3000-rapport; het vastleggen loopt via het beleid
informatiebeveiliging bij inkoop, het toetsen via het beleid contractbeheer.

Buiten dit beleid vallen het melden en afhandelen van incidenten en de procedure voor meldingen van
buiten (CVD), beide in het beleid beveiligingsincidenten, het doorvoeren van een patch als wijziging (beleid
wijzigingsbeheer), het veilig bouwen van eigen software (beleid veilige softwareontwikkeling) en de
inrichting van het netwerk (beleid netwerkbeveiliging).

## 2. Uitgangspunten

1. Wat de organisatie niet kent, kan zij niet patchen. Het overzicht van ICT-middelen uit het beleid
   bedrijfsmiddelenbeheer is de basis voor scannen, patchen en configuratiebeheer.
2. De termijn voor het verhelpen van een kwetsbaarheid volgt uit de kans op misbruik en de verwachte
   schade, met het impactniveau van het systeem als maat voor die schade.
3. Een systeem draait alleen wat het nodig heeft. Wat overbodig is, gaat uit of eraf, en de gewenste
   configuratie is vastgelegd, zodat een afwijking meetbaar is.
4. Kan een kwetsbaarheid niet op tijd worden verholpen, dan is er een vastgelegde risicoafweging met
   tijdelijke maatregelen, een einddatum en een eigenaar.
5. Termijnen en frequenties in dit beleid die niet uit een wet of uit de BIO 2.0 komen, zijn standaardwaarden.
   De organisatie past ze aan op haar eigen risicoafweging en legt de keuze vast bij de vaststelling van dit beleid.

## 3. Beleidsregels

### 3.1 Bescherming tegen malware

- [[beheerorganisatie: de eigen afdeling of de leverancier die de systemen beheert]] zorgt dat op alle
  werkplekken, servers en mailvoorzieningen antimalware-software draait die zichzelf en de bijbehorende
  herstelsoftware automatisch bijwerkt. Een apparaat dat langer dan zeven dagen geen update heeft ontvangen,
  verschijnt als afwijking in het beheeroverzicht en is binnen een week hersteld of van het netwerk
  gehaald. [8.07.03]
- De antimalware-software scant alle omgevingen (werkplekken, servers, mailverkeer en apparaten die
  verbinding maken met het netwerk), alle downloads vóór ze worden geopend of opgeslagen en alle bestanden
  die via mail, een koppeling of een opslagmedium binnenkomen, vóór gebruik. De scanlogging is voor de
  beheerorganisatie en de CISO in te zien. [8.07.04]
- Downloaden is beperkt op basis van risico en noodzaak. Uitvoerbare bestanden en scripts van internet
  houdt de werkplekbeveiliging standaard tegen; een uitzondering vraagt de gebruiker aan bij de servicedesk
  en de beheerorganisatie legt de toekenning vast. [8.07.01]
- Medewerkers krijgen bij indiensttreding en daarna elk jaar voorlichting over veilig surfen, phishing en
  het klikken op onbekende links. Een phishing-simulatie maakt deel uit van het jaarprogramma
  bewustwording; de deelname en de uitkomst staan in het verslag van dat programma. [8.07.02]

### 3.2 Configuratiebeheer en hardening

- Voor elk type systeem (werkplek, server, netwerkcomponent, database, clouddienst) stelt de
  beheerorganisatie een basisconfiguratie vast, gebaseerd op een erkende baseline zoals de CIS Benchmarks of
  de richtlijnen van de leverancier. Overbodige diensten, poorten, software en accounts staan uit of zijn
  verwijderd en standaardwachtwoorden zijn vóór ingebruikname vervangen. De basisconfiguraties zijn
  vastgelegd en worden jaarlijks herzien. [8.09.01]
- De beheerorganisatie legt van elk systeem de werkelijke configuratie vast in
  [[configuratieregister: het systeem waarin de configuraties staan, bijvoorbeeld de configuratiedatabase van het beheertool]],
  met de verwijzing naar de basisconfiguratie en de goedgekeurde afwijkingen. Een wijziging van de
  configuratie loopt via het beleid wijzigingsbeheer. [8.09.01]
- De beheerorganisatie meet elk kwartaal geautomatiseerd de afwijkingen van de basisconfiguratie. Een
  afwijking is binnen een maand hersteld of staat als uitzondering vastgelegd met een risicoafweging en een
  einddatum. [8.09.01]
- Alleen beheerders installeren software of activeren functies. Gebruikers hebben op hun werkplek geen
  beheerrechten; de technische handhaving daarvan staat in het beleid wijzigingsbeheer. [8.09.01, 8.07.01]

### 3.3 Kwetsbaarheden vinden

- De beheerorganisatie scant alle ICT-middelen ten minste maandelijks op kwetsbaarheden en
  misconfiguraties, en opnieuw na een grote wijziging. Waar mogelijk gebruikt zij agents op de eindpunten,
  zodat ook apparaten buiten kantoor meetellen. De scanresultaten staan in het kwetsbaarhedenregister
  (paragraaf 3.5). [8.08.01, 8.08.02]
- De CISO volgt de waarschuwingen van het NCSC en de sectorale CERT. Een waarschuwing die een gebruikt
  product raakt, zet de CISO binnen één werkdag door aan de systeemeigenaar en de beheerorganisatie, met
  een registratie van de doorzetting en de reactie. [8.08.01]
- De CISO stelt jaarlijks een testprogramma vast waarin elk informatiesysteem wordt gecontroleerd op
  technische naleving van de beveiligingseisen, met een kwetsbaarheidsanalyse, een penetratietest of een
  red-teamtest. Welke vorm per systeem, bepaalt de CISO op basis van het impactniveau. [8.08.04]
- Systemen die vanaf internet bereikbaar zijn, worden continu op kwetsbaarheden gescand, bijvoorbeeld met
  een geautomatiseerde externe scan, en ten minste jaarlijks met een penetratietest getest. [8.08.04, 8.08.05]
- Bij elke nieuwe release of grote update van een internetbereikbaar systeem volgt een penetratietest,
  waar mogelijk geautomatiseerd. Een bevinding met hoog risico die niet op een andere manier kan worden
  beperkt, houdt de release tegen: het systeem gaat dan niet in productie. Het testrapport hoort bij de
  wijziging in het wijzigingsregister. [8.08.05]
- Penetratietesten voert een partij uit die onafhankelijk is van de bouwer en de beheerder van het
  systeem, met een vooraf afgesproken methode en reikwijdte. De CISO bewaart de rapporten en de opvolging
  in [[register testrapporten: de plek waar pentestrapporten en opvolging staan, bijvoorbeeld het managementsysteem]].
  [8.08.04, 8.08.05]

::: als ontwikkeling=ja
- Voor software die de organisatie zelf bouwt, scant de bouwstraat de broncode en de gebruikte
  bibliotheken bij elke build automatisch op bekende kwetsbaarheden. Een kritieke bevinding in een
  bibliotheek stopt de build. Elke applicatie heeft een actuele lijst van gebruikte componenten (SBOM),
  zodat een nieuwe kwetsbaarheid in een bibliotheek direct te vinden is. [8.08.05, 8.08.01]
- De penetratietest bij een release van een zelfgebouwde internetbereikbare applicatie staat in de
  releaseprocedure als poort; de ontwikkelaar levert het testrapport aan bij de wijzigingsaanvraag. [8.08.05]
:::

::: als ontwikkeling=nee
- De organisatie bouwt zelf geen software. Bij inkoop en contractverlenging eist zij van de leverancier
  een penetratietest bij elke grote release van een internetbereikbaar systeem, inzage in het rapport en het
  verhelpen van hoge bevindingen vóór de release in productie gaat. De contracteigenaar controleert dat bij
  elke release. [8.08.05]
:::

### 3.4 Beoordelen en verhelpen

- Elke gevonden kwetsbaarheid krijgt van de systeemeigenaar, op advies van de beheerorganisatie, een
  risico-inschatting op basis van kans op misbruik en verwachte schade. Daarin wegen de ernstscore van de
  leverancier of het CVE-register, het impactniveau van het systeem en de bereikbaarheid vanaf internet mee.
  Op basis van die vastgelegde afweging kiest de systeemeigenaar de maatregel: patchen, de configuratie
  aanpassen, de functie uitzetten of het systeem afschermen. [8.08.02]
- De beheerorganisatie verhelpt een kwetsbaarheid binnen de termijn die bij het risico hoort, gerekend
  vanaf het moment dat de kwetsbaarheid bekend is: [8.08.01, 8.08.02]

  | Risico | Termijn |
  |---|---|
  | Kans op misbruik hoog en schade hoog | zo snel mogelijk, uiterlijk binnen [[patchtermijn hoog en hoog: standaard een week, de BIO 2.0 noemt een week als grens voor tijdelijke maatregelen]] |
  | Overig hoog | binnen [[patchtermijn hoog: standaard een maand]] |
  | Gemiddeld | binnen [[patchtermijn gemiddeld: standaard drie maanden]] |
  | Laag | bij de eerstvolgende reguliere update |

- Bij hoge kans en hoge schade zijn de beperkende maatregelen uiterlijk binnen een week getroffen. Bij
  actief misbruik in het wild handelt de beheerorganisatie dezelfde dag en meldt zij de stand aan de CISO.
  [8.08.01]
- Kan de patch niet binnen de termijn, of is er nog geen patch, dan treft de systeemeigenaar direct
  tijdelijke maatregelen op basis van een vastgelegde risicoafweging, bijvoorbeeld de functie uitzetten,
  de toegang beperken of extra bewaking. De afweging noemt het restrisico, de einddatum en wie het
  restrisico accepteert, en staat in het kwetsbaarhedenregister. [8.08.03]
- Software waarvoor de leverancier geen beveiligingsupdates meer levert, vervangt de systeemeigenaar
  binnen [[termijn uitfaseren]]. Zolang dat niet is gebeurd, staat het systeem afgeschermd en als risico
  in het risicoregister, met een risico-eigenaar. [8.08.03]
- Na het verhelpen stelt de beheerorganisatie met een herhaalscan vast dat de kwetsbaarheid weg is. Pas
  dan sluit zij de melding in het kwetsbaarhedenregister. [8.08.01]

::: als beheer=eigen
- De eigen beheerorganisatie installeert beveiligingsupdates voor werkplekken, servers en
  netwerkcomponenten volgens een vast maandelijks venster, met een spoedprocedure voor de weektermijn.
  Patchen loopt als standaardwijziging via het beleid wijzigingsbeheer; een spoedpatch mag achteraf worden
  geregistreerd. [8.08.01]
:::

::: als beheer=regie,uitbesteed
- Het beheer is uitbesteed. Het contract met de beheerpartij bevat de termijnen uit de tabel hierboven,
  de plicht om binnen één werkdag te melden welke systemen een kritieke waarschuwing raakt, en een
  maandelijkse rapportage over openstaande kwetsbaarheden en de patchstand. [8.08.01]
- De organisatie ontvangt de scanresultaten zelf of laat de scan doen door een andere partij dan de
  beheerder, zodat zij de rapportage van de beheerpartij kan controleren. De contracteigenaar legt de
  vergelijking elk kwartaal vast. [8.08.02, 8.08.04]
:::

::: als beheer=uitbesteed
- Omdat er geen eigen beheerorganisatie is, wijst de organisatie een contractmanager aan die de
  patchrapportage elke maand bespreekt met de leverancier, het verslag vastlegt en afwijkingen aan de CISO
  meldt. [8.08.01]
:::

### 3.5 Registreren en rapporteren

- Alle open kwetsbaarheden met risico gemiddeld of hoger staan in
  [[kwetsbaarhedenregister: het systeem waarin open kwetsbaarheden staan, bijvoorbeeld de scantool of het ticketsysteem]],
  met systeem, risico, eigenaar, termijn en status. Termijnoverschrijdingen zijn zichtbaar en de
  beheerorganisatie houdt het register dagelijks bij. [8.08.01, 8.08.02]
- De CISO rapporteert maandelijks aan de directie het aantal open kwetsbaarheden per risiconiveau, de
  termijnoverschrijdingen, de geaccepteerde restrisico's en de patchstand. [8.08.01, 8.08.03]

::: als capaciteit=geen
- Er is geen eigen informatiebeveiligingsfunctionaris met voldoende tijd. De scans en de risico-inschatting
  voert een externe partij uit; [[functionaris informatiebeveiliging]] bespreekt de maandrapportage met die
  partij, legt de besluiten vast en zet open punten uit bij de systeemeigenaren. [8.08.02]
:::

::: als capaciteit=parttime,team
- De informatiebeveiligingsfunctionaris beoordeelt elke maand de scanresultaten, filtert valse meldingen,
  legt dat vast en zet open punten uit bij de systeemeigenaren. [8.08.02]
:::

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| [[lijneigenaar kwetsbaarhedenbeheer: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd ICT]] | Eigenaar van dit beleid; de middelen voor scannen, patchen en configuratiebeheer; opvolging van de maandrapportage |
| Systeemeigenaar | Risico-inschatting en keuze van de maatregel, risicoafweging bij uitstel, vervanging van software zonder updates, acceptatie van restrisico binnen de eigen bevoegdheid |
| [[beheerorganisatie]] | Antimalware, basisconfiguraties en het configuratieregister, scannen, patchen binnen de termijn, herhaalscans en het bijhouden van het kwetsbaarhedenregister |
| CISO | Testprogramma, doorzetten van waarschuwingen van NCSC en CERT, bewaren van testrapporten, maandrapportage aan de directie, toetsing van risicoafwegingen en jaarlijkse toetsing van dit beleid |
| Contracteigenaar | Vastleggen van de termijnen en rapportageplichten bij de beheerpartij en leveranciers, controle van pentestbewijs bij releases van leveranciers |
| Medewerkers en inhuur | Geen software installeren buiten de regels om, uitzonderingen aanvragen bij de servicedesk, verdachte bestanden of links melden |

## 5. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in [[registratie van controles]]; afwijkingen gaan als bevinding naar het
risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| VPM-01 | Elk apparaat in het overzicht van ICT-middelen heeft actieve antimalware met een update van ten hoogste zeven dagen oud, en apparaten die daarbuiten vallen zijn hersteld of van het netwerk gehaald | [[beheerorganisatie]] | Maandelijks | Rapport uit de antimalware-console vergeleken met het overzicht van ICT-middelen, met de afhandeling per afwijking | 8.07.03, 8.07.04 |
| VPM-02 | Uitvoerbare bestanden en scripts van internet worden tegengehouden en elke toegestane uitzondering heeft een vastgelegde aanvraag; de jaarlijkse voorlichting en de phishing-simulatie zijn uitgevoerd | CISO | Jaarlijks | Testdownload met het resultaat, lijst van uitzonderingen met aanvragen, verslag van het programma bewustwording | 8.07.01, 8.07.02 |
| VPM-03 | Elk type systeem heeft een vastgestelde basisconfiguratie van ten hoogste een jaar oud, de gemeten afwijkingen zijn binnen een maand hersteld of als uitzondering vastgelegd, en het configuratieregister is volledig | [[lijneigenaar kwetsbaarhedenbeheer]] | Per kwartaal | Meetrapport van de afwijkingen met afhandeling, lijst van basisconfiguraties met vaststellingsdatum, steekproef van vijf systemen in het configuratieregister | 8.09.01 |
| VPM-04 | Alle ICT-middelen uit het overzicht zijn in de afgelopen maand gescand en elke kwetsbaarheid met risico gemiddeld of hoger staat in het kwetsbaarhedenregister met eigenaar en termijn | CISO | Maandelijks | Scanrapport vergeleken met het overzicht van ICT-middelen, uittreksel uit het kwetsbaarhedenregister | 8.08.01, 8.08.02 |
| VPM-05 | Kwetsbaarheden zijn binnen de termijn van de tabel verholpen en de herhaalscan bevestigt dat; overschrijdingen zijn aan de directie gerapporteerd | CISO | Maandelijks | Maandrapportage met de termijnoverschrijdingen per risiconiveau, herhaalscans bij een steekproef van vijf gesloten meldingen | 8.08.01, 8.08.02 |
| VPM-06 | Elke uitgestelde kwetsbaarheid en elk systeem zonder beveiligingsupdates heeft een volledige risicoafweging met tijdelijke maatregelen, einddatum en risico-eigenaar, en de einddatum is nagekomen | CISO | Per kwartaal | Steekproef van vijf uitgestelde kwetsbaarheden met de afweging en de stand op de einddatum, uittreksel uit het risicoregister | 8.08.03 |
| VPM-07 | Elke waarschuwing van NCSC of CERT die een gebruikt product raakte, is binnen één werkdag doorgezet en opgevolgd | [[lijneigenaar kwetsbaarhedenbeheer]] | Per kwartaal | Registratie van de ontvangen waarschuwingen met datum van doorzetting en reactie | 8.08.01 |
| VPM-08 | Elk informatiesysteem en elk internetbereikbaar systeem is volgens het testprogramma getest, de bevindingen met hoog risico zijn opgevolgd en elke release van een internetbereikbaar systeem heeft een penetratietestrapport bij de wijziging | CISO | Jaarlijks | Testprogramma met de testrapporten, opvolging per bevinding, steekproef van vijf releases in het wijzigingsregister | 8.08.04, 8.08.05 |
| VPM-09 | De beheerpartij en de leveranciers van internetbereikbare systemen leveren de afgesproken rapportages en penetratietestbewijzen en halen de termijnen uit het contract | Contracteigenaar | Jaarlijks | Contracten met de termijnen, ontvangen rapportages en pentestbewijzen, beoordeling van de uitzonderingen | 8.08.01, 8.08.05 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De
systeemeigenaar dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de looptijd.
De afwijking geldt pas na acceptatie van het risico door [[risico-eigenaar: de manager die restrisico's accepteert]]
en staat in het risicoregister; afwijkingen worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid
bedrijfsmiddelenbeheer (het overzicht van ICT-middelen), het beleid wijzigingsbeheer (patches en
configuratiewijzigingen als wijziging, lijst van toegestane software), het beleid veilige
softwareontwikkeling (scannen van eigen code en bibliotheken), het beleid beveiligingsincidenten (CVD en
misbruik van een kwetsbaarheid), het beleid informatieclassificatie (impactniveau als maat voor de schade),
het beleid informatiebeveiliging bij inkoop en contractbeheer (termijnen en rapportages in contracten) en
het beleid screening, bewustzijn en opleiding (voorlichting en phishing-simulatie).
