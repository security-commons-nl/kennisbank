---
domein: cryptografie
titel: Beleid cryptografie
samenvatting: Regelt wanneer en hoe de organisatie versleutelt en wie sleutels en certificaten beheert. Behandelt de minimale versleuteling per vertrouwelijkheidslabel, verplichte standaarden en adviezen van NCSC en NBV, de inventaris van certificaten en sleutels, en de procedure sleutelbeheer met intrekking en reservecertificaten.
invoeren:
  - Leg per systeem het versleutelingsniveau volgens de minimumtabel vast in het systeemdossier (hoofdstuk 3).
  - Breng websites en maildomeinen op de verplichte standaarden van het Forum Standaardisatie (hoofdstuk 4).
  - Wijs een eigenaar cryptografie en een sleutelbeheerder aan (hoofdstuk 5).
  - Neem elk certificaat, elke sleutel en elke versleutelingsvoorziening op in de inventaris (hoofdstuk 5).
  - Stel in de inventaris een automatisch signaal in voor certificaten die bijna verlopen (hoofdstuk 5).
  - Stel een procedure sleutelbeheer op voor alle fasen, van aanvragen tot vernietigen (hoofdstuk 6).
  - Zet sleutels in een sleutelkluis of beveiligde hardware, niet in code of gedeelde mappen (hoofdstuk 6).
  - Bepaal per kritiek certificaat of reservecertificaten nodig zijn en oefen de vervanging (hoofdstuk 6).
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor het gebruik van cryptografie:
versleuteling van gegevens bij transport en opslag, digitale handtekeningen, certificaten en het beheer van
cryptografische sleutels. Het legt vast wanneer de organisatie versleutelt, met welke middelen en wie de
sleutels beheert, zodat vertrouwelijkheid en integriteit van informatie ook buiten de eigen muren overeind
blijven. Het gaat over de ISO-beheersmaatregel 8.24.

**Voor wie.** Het beleid is primair bedoeld voor de functie die cryptografie implementeert, de
sleutelbeheerder en de systeemeigenaren. De gedragsregels over tokens, sleutels en het verzenden van
vertrouwelijke informatie gelden voor alle medewerkers en inhuur.

**Waarop.** Alle systemen, applicaties, verbindingen, back-ups, gegevensdragers en gegevens waarvoor de
organisatie verantwoordelijk is, en alle sleutels en certificaten die daarbij horen. Is een systeem gehost
of beheerd door een leverancier, dan gelden de eisen uit dit beleid als minimumeis voor die partij. De
organisatie legt dat vast in het contract en toetst de naleving met een onafhankelijke verklaring, zoals een
ISO 27001-certificaat of een ISAE 3402- of ISAE 3000-rapport; het vastleggen loopt via het beleid
informatiebeveiliging bij inkoop, het toetsen via het beleid contractbeheer.

Buiten dit beleid vallen de classificatie zelf (beleid informatieclassificatie), de inrichting van de
netwerkverbindingen die versleuteld worden (beleid netwerkbeveiliging), de versleuteling van mobiele
apparaten (beleid mobile device management) en het wissen van gegevensdragers (beleid afvoer en hergebruik
van gegevensdragers).

## 2. Uitgangspunten

1. Cryptografie volgt de classificatie: hoe hoger het vertrouwelijkheidslabel van de informatie, hoe
   zwaarder de versleuteling.
2. De organisatie gebruikt alleen erkende, openbare algoritmen en protocollen in een actuele versie, geen
   eigen of geheime constructies.
3. Elk cryptografisch middel (certificaat, sleutel, versleutelingsvoorziening) heeft een eigenaar en staat
   in de inventaris.
4. Sleutels zijn net zo goed beschermd als de informatie die ze beschermen.
5. Termijnen en frequenties in dit beleid die niet uit een wet of uit de BIO 2.0 komen, zijn standaardwaarden.
   De organisatie past ze aan op haar eigen risicoafweging en legt de keuze vast bij de vaststelling van dit beleid.

## 3. Wanneer de organisatie cryptografie inzet

- De systeemeigenaar zet cryptografie in volgens deze minimumtabel, die per vertrouwelijkheidslabel
  aansluit op het beleid informatieclassificatie, en legt het gekozen niveau vast in het systeemdossier:
  [8.24.01]
  - intern: versleuteld transport over elk netwerk buiten het eigen interne netwerk;
  - vertrouwelijk: versleuteld transport over elk netwerk, ook intern, en versleutelde opslag op draagbare
    apparaten en gegevensdragers;
  - strikt vertrouwelijk en geheim: daarbovenop versleutelde opslag in databases en bestandsopslag en, bij
    uitwisseling, versleuteling van het bericht zelf.
- Back-ups worden versleuteld opgeslagen. De sleutels staan gescheiden van de back-up, en de
  [[sleutelbeheerder: de functie die verantwoordelijk is voor het sleutel- en certificaatbeheer]] test
  jaarlijks met de eigenaar van de back-up een herstel met die sleutels. [8.24.01]
- Voor integriteit en onweerlegbaarheid gebruikt de organisatie digitale handtekeningen of gekwalificeerde
  elektronische zegels waar een wet of de risicoanalyse dat vraagt, bijvoorbeeld bij besluiten die digitaal
  worden verzonden; de systeemeigenaar legt vast welke documenten dat zijn. [8.24.01]
- Medewerkers sturen informatie met het label vertrouwelijk of hoger niet via persoonlijke webmail,
  privé-opslagdiensten of sociale media. [8.24.01]

## 4. Normen en sterkte

- De organisatie past de verplichte standaarden van het Forum Standaardisatie toe volgens pas toe of leg uit.
  Voor websites en mail zijn dat in elk geval HTTPS met HSTS, TLS, DNSSEC, DKIM, DMARC, SPF en STARTTLS met
  DANE. [[eigenaar cryptografie: de functie die verantwoordelijk is voor de implementatie, bijvoorbeeld de IT-architect of het hoofd IT]]
  motiveert afwijkingen en rapporteert ze jaarlijks aan de CISO. [8.24.01]
- De keuze van algoritmen, sleutellengten en protocolversies volgt de actuele adviezen van het NCSC (onder
  meer de ICT-beveiligingsrichtlijnen voor TLS) en van het NBV. Instellingen die als onvoldoende of uit te
  faseren gelden, zet [[eigenaar cryptografie]] binnen
  [[termijn uitfaseren: bijvoorbeeld zes maanden na publicatie van het advies]] uit. [8.24.04]
- [[eigenaar cryptografie]] controleert elk halfjaar of er nieuwe adviezen zijn en of de inzet nog voldoet,
  en legt de uitkomst vast. Dit omvat de voorbereiding op quantumveilige cryptografie: de inventaris laat
  zien welke toepassingen eerst over moeten. [8.24.04]
- Wisselt de organisatie versleutelde informatie uit met een andere organisatie, dan leggen beide partijen
  vooraf vast welke versleuteling, welke certificaten en welk sleutelbeheer ze gebruiken, bijvoorbeeld in een
  aansluitovereenkomst of verwerkersovereenkomst. De systeemeigenaar bewaart die afspraak in het
  systeemdossier. [8.24.01]

## 5. Verantwoordelijkheden en registratie

- [[eigenaar cryptografie]] is verantwoordelijk voor de implementatie van cryptografie en legt per
  toepassing vast welk middel is gekozen en waarom. [8.24.01]
- [[sleutelbeheerder]] is verantwoordelijk voor het beheer van sleutels en certificaten gedurende de hele
  levenscyclus en houdt daarvan een register bij. [8.24.01]
- Elk certificaat, elke sleutel met een functie in productie en elke versleutelingsvoorziening staat in de
  inventaris van bedrijfsmiddelen, met waar het wordt gebruikt, wie de eigenaar is, het algoritme en de
  sleutellengte, de vervaldatum en hoe het actueel wordt gehouden. [[sleutelbeheerder]] controleert de
  inventaris elk halfjaar op volledigheid. [8.24.02]
- De inventaris geeft [[waarschuwingstermijn verlopen: bijvoorbeeld 60 dagen]] voor het verlopen van een
  certificaat automatisch een signaal aan de eigenaar; de eigenaar vervangt het certificaat voor de
  vervaldatum. [8.24.02]

## 6. Sleutel- en certificaatbeheer

- Voor PKIoverheid-certificaten volgt de organisatie de eisen van PKIoverheid aan het sleutelbeheer. Voor
  overige sleutels volgt ze een erkende norm voor sleutelbeheer, zoals ISO/IEC 11770. [8.24.01]
- [[sleutelbeheerder]] legt in de procedure sleutelbeheer voor elke fase vast wie wat doet: aanvragen (na
  vaststelling van de identiteit van de aanvrager), genereren, distribueren, opslaan, vervangen, herstellen,
  intrekken, archiveren en vernietigen. [8.24.01]
- Een privésleutel is alleen toegankelijk voor de houder of de voorziening die hem gebruikt. Sleutels staan
  in een sleutelkluis of beveiligde hardware; nooit in broncode, scripts of gedeelde mappen. [8.24.01]
- Verlies, diefstal of een vermoeden van misbruik van een sleutel of token meldt de medewerker direct, en
  uiterlijk binnen vier uur, bij de servicedesk. [[sleutelbeheerder]] trekt het certificaat in en publiceert
  de intrekking via de gebruikelijke kanalen (CRL of OCSP). [8.24.01]
- Voor certificaten waarvan de dienstverlening afhangt (bijvoorbeeld voor websites, koppelingen en
  ketenaansluitingen) bepaalt de systeemeigenaar in de risicoafweging of de organisatie reservecertificaten
  van een andere leverancier nodig heeft. Is dat zo, dan liggen er afspraken met die leverancier, is de
  vervanging beschreven in het continuïteitsplan en oefent [[sleutelbeheerder]] de vervanging jaarlijks.
  [8.24.05]

::: als hosting=eigen-dc
- Sleutels voor de eigen systemen worden in de eigen omgeving gegenereerd en beheerd. Sleutels voor
  informatie met het label strikt vertrouwelijk of geheim staan in een HSM of een gelijkwaardige voorziening.
  [8.24.01]
:::

::: als hosting=hostingpartij
- Waar de hostingpartij versleuteling of certificaten levert, staat in het contract wie de sleutels beheert,
  dat de hostingpartij de normen uit dit beleid volgt en dat de organisatie inzage krijgt in het
  sleutelbeheer. Interne certificaten van de hostingpartij staan ook in de inventaris van de organisatie. [8.24.01, 8.24.02]
:::

::: als hosting=saas
- Bij SaaS en publieke cloud toetst de organisatie bij inkoop of de leverancier versleutelt bij transport en
  opslag volgens dit beleid. Voor informatie met het label strikt vertrouwelijk of geheim kiest de organisatie waar
  het kan voor sleutels die zij zelf beheert of die buiten de leverancier liggen. [8.24.01]
- De versleutelingsinstellingen van elke clouddienst staan in de inventaris, ook als de leverancier de
  sleutels beheert. [8.24.02]
:::

::: als byod=ja
- Op privéapparaten (BYOD) staan werkgegevens alleen in een beheerde, versleutelde app-omgeving met een
  eigen sleutel van de organisatie, die de organisatie op afstand kan wissen zonder de privégegevens te
  raken. [8.24.01]
:::

::: als gevoelig=sociaal,jeugd,gezondheid
- Mail met bijzondere persoonsgegevens (sociaal domein, jeugd of gezondheid) gaat naar externe ontvangers
  alleen over een kanaal dat versleuteling afdwingt en de ontvanger controleert, bijvoorbeeld beveiligde mail
  volgens NTA 7516. Zonder zo'n kanaal wordt de informatie niet gemaild. [8.24.01]
:::

## 7. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| [[lijneigenaar cryptografie: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd IT]] | Eigenaar van dit beleid en van de inventaris van cryptografische middelen |
| [[eigenaar cryptografie]] | Implementatie van versleuteling, de halfjaarlijkse toets op de adviezen van NCSC en NBV, rapportage over afwijkingen van de standaarden |
| [[sleutelbeheerder]] | Levenscyclus van sleutels en certificaten, de procedure sleutelbeheer, intrekking bij misbruik, hersteltest en oefening met reservecertificaten |
| Systeemeigenaar | Beschermingsniveau per systeem, afspraken met leveranciers en ketenpartners, risicoafweging voor reservecertificaten |
| CISO | Advies, toetsing van dit beleid, beoordeling van afwijkingen op de standaarden en van afwijkingen van dit beleid |
| Inkoop en contractbeheer | Vastleggen van de eisen uit dit beleid bij leveranciers en toetsen van hun verklaringen |
| Medewerkers | Zorgvuldig gebruik van tokens en sleutels, direct melden van verlies, geen vertrouwelijke informatie via privékanalen |

## 8. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in [[registratie van controles: het systeem waarin controles worden vastgelegd, bijvoorbeeld het ticketsysteem of het managementsysteem]];
afwijkingen gaan als bevinding naar het risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| CRY-01 | Websites en maildomeinen voldoen aan de verplichte standaarden van het Forum Standaardisatie en elke afwijking is gemotiveerd | [[eigenaar cryptografie]] | Maandelijks, rapportage jaarlijks | Meetuitslag per domein, bijvoorbeeld van internet.nl, en de afhandeling van afwijkingen | 8.24.01 |
| CRY-02 | De inventaris van certificaten, sleutels en versleutelingsvoorzieningen is volledig, elk middel heeft een eigenaar en een vervaldatum, en verlopen certificaten zijn op tijd vervangen | [[sleutelbeheerder]] | Halfjaarlijks | Bijgewerkte inventaris met acties, overzicht van signalen en vervangingen | 8.24.02 |
| CRY-03 | De gebruikte algoritmen, sleutellengten en protocolversies voldoen aan de actuele adviezen van NCSC en NBV en afgekeurde instellingen zijn binnen de termijn uitgezet | [[eigenaar cryptografie]] | Halfjaarlijks | Toetsverslag tegen de adviezen, scanrapport van de instellingen, lijst van uitgefaseerde instellingen | 8.24.04 |
| CRY-04 | Elk systeem met het label vertrouwelijk of hoger versleutelt bij transport en opslag volgens de minimumtabel, en back-ups zijn versleuteld met gescheiden sleutels | CISO | Jaarlijks | Steekproef van systeemdossiers, configuratierapport van de back-upvoorziening, verslag van de hersteltest | 8.24.01 |
| CRY-05 | Sleutels staan in een sleutelkluis of beveiligde hardware en niet in broncode, scripts of gedeelde mappen; de procedure sleutelbeheer is gevolgd | [[sleutelbeheerder]] | Jaarlijks | Scanrapport op sleutels in repositories en gedeelde mappen, steekproef van aanvragen en intrekkingen | 8.24.01 |
| CRY-06 | Voor certificaten waarvan de dienstverlening afhangt is de risicoafweging over reservecertificaten gemaakt en, waar afgesproken, de vervanging geoefend | [[sleutelbeheerder]] | Jaarlijks | Risicoafwegingen per certificaat, afspraken met de reserveleverancier, oefenverslag | 8.24.05 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De
systeemeigenaar dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de looptijd.
De afwijking geldt pas na acceptatie van het risico door [[risico-eigenaar: de manager die restrisico's accepteert]]
en staat in het risicoregister; afwijkingen worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 9. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid
informatieclassificatie (vertrouwelijkheidslabels), het beleid bedrijfsmiddelenbeheer (inventaris), het
beleid back-up en recovery (versleutelde back-ups), het beleid netwerkbeveiliging (versleuteling onderweg),
het beleid mobile device management (versleuteling van apparaten), het beleid veilige softwareontwikkeling
(geen sleutels in broncode), het beleid informatiebeveiliging bij inkoop en contractbeheer (afspraken over
versleuteling) en het beleid ICT-continuïteit en uitwijk (reservecertificaten).
