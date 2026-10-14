# Beleid cryptografie

Beleid informatiebeveiliging, BIO 2.0-domein *Cryptografie*. Status: concept, vast te stellen door de organisatie zelf.

Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor het gebruik van cryptografie:
versleuteling van gegevens bij transport en opslag, digitale handtekeningen, certificaten en het beheer van
cryptografische sleutels. Het geldt voor alle systemen, applicaties en gegevens waarvoor de organisatie
verantwoordelijk is, ook als een leverancier ze host of beheert. Het gaat over de ISO-beheersmaatregel 8.24.

Buiten dit beleid vallen de classificatie zelf (beleid informatieclassificatie), de verplichte
internetstandaarden voor websites en mail voor zover ze over de inrichting van diensten gaan (beleid
informatieclassificatie en beleid netwerkbeveiliging) en de versleuteling van mobiele apparaten (beleid
mobile device management).

## 2. Uitgangspunten

1. Cryptografie volgt de classificatie: hoe hoger het betrouwbaarheidsniveau van de informatie, hoe
   zwaarder de versleuteling.
2. De organisatie gebruikt alleen erkende, openbare algoritmen en protocollen in een actuele versie, geen
   eigen of geheime constructies.
3. Elk cryptografisch middel (certificaat, sleutel, versleutelingsvoorziening) heeft een eigenaar en staat
   in de inventaris.
4. Sleutels zijn net zo goed beschermd als de informatie die ze beschermen.

## 3. Beleidsregels

### 3.1 Wanneer de organisatie cryptografie inzet

- De organisatie zet cryptografie in volgens deze minimumtabel, die per classificatieniveau aansluit op het
  classificatiebeleid: [8.24.01]
  - laag: versleuteld transport over elk netwerk buiten het eigen interne netwerk;
  - midden: versleuteld transport over elk netwerk, ook intern, en versleutelde opslag op draagbare
    apparaten en gegevensdragers;
  - hoog: daarbovenop versleutelde opslag in databases en bestandsopslag en, bij uitwisseling, versleuteling
    van het bericht zelf.
- Back-ups worden versleuteld opgeslagen. De sleutels staan gescheiden van de back-up, en een herstel met die
  sleutels wordt jaarlijks getest. [8.24.01]
- Voor integriteit en onweerlegbaarheid gebruikt de organisatie digitale handtekeningen of gekwalificeerde
  elektronische zegels waar een wet of de risicoanalyse dat vraagt, bijvoorbeeld bij besluiten die digitaal
  worden verzonden. [8.24.01]
- Vertrouwelijke informatie gaat niet via persoonlijke webmail, privé-opslagdiensten of sociale media. [8.24.01]

### 3.2 Normen en sterkte

- De organisatie past de verplichte standaarden van het Forum Standaardisatie toe volgens pas toe of leg uit.
  Voor websites en mail zijn dat in elk geval HTTPS met HSTS, TLS, DNSSEC, DKIM, DMARC, SPF en STARTTLS met
  DANE. Afwijkingen worden gemotiveerd en jaarlijks gerapporteerd. [8.24.01]
- De keuze van algoritmen, sleutellengten en protocolversies volgt de actuele adviezen van het NCSC (onder
  meer de ICT-beveiligingsrichtlijnen voor TLS) en van het Nationaal Bureau voor Verbindingsbeveiliging van de
  AIVD. Instellingen die als onvoldoende of uit te faseren gelden, worden binnen
  **[termijn uitfaseren]**
  uitgezet. [8.24.04]
- De beheerder van de cryptografische inventaris controleert elk halfjaar of er nieuwe adviezen zijn en of
  de inzet nog voldoet. Dit omvat de voorbereiding op quantumveilige cryptografie: de inventaris laat zien
  welke toepassingen eerst over moeten. [8.24.04]
- Het beschermingsniveau van een toepassing volgt uit de classificatie van de informatie en de
  risicoanalyse van het systeem. De systeemeigenaar legt het vast in het systeemdossier. [8.24.01]
- Wisselt de organisatie versleutelde informatie uit met een andere organisatie, dan leggen beide partijen
  vooraf vast welke versleuteling, welke certificaten en welk sleutelbeheer ze gebruiken, bijvoorbeeld in een
  aansluitovereenkomst of verwerkersovereenkomst. [8.24.01]

### 3.3 Verantwoordelijkheden en registratie

- **[eigenaar cryptografie]**
  is verantwoordelijk voor de implementatie van cryptografie. [8.24.01]
- **[sleutelbeheerder]**
  is verantwoordelijk voor het beheer van sleutels en certificaten gedurende de hele levenscyclus. [8.24.01]
- Elk certificaat, elke sleutel met een functie in productie en elke versleutelingsvoorziening staat in de
  inventaris van bedrijfsmiddelen, met waar het wordt gebruikt, wie de eigenaar is, het algoritme en de
  sleutellengte, de vervaldatum en hoe het actueel wordt gehouden. [8.24.02]
- De inventaris geeft
  **[waarschuwingstermijn verlopen]**
  voor het verlopen van een certificaat automatisch een signaal aan de eigenaar. [8.24.02]

### 3.4 Sleutel- en certificaatbeheer

- Voor PKIoverheid-certificaten volgt de organisatie de eisen van PKIoverheid aan het sleutelbeheer. Voor
  overige sleutels volgt ze een erkende norm voor sleutelbeheer, zoals ISO/IEC 11770. [8.24.01]
- Voor elke fase is vastgelegd wie wat doet: aanvragen (na vaststelling van de identiteit van de aanvrager),
  genereren, distribueren, opslaan, vervangen, herstellen, intrekken, archiveren en vernietigen. [8.24.01]
- Een privésleutel is alleen toegankelijk voor de houder of de voorziening die hem gebruikt. Sleutels staan
  in een sleutelkluis of beveiligde hardware; nooit in broncode, scripts of gedeelde mappen. [8.24.01]
- Verlies, diefstal of een vermoeden van misbruik van een sleutel of token meldt de medewerker direct, en
  uiterlijk binnen vier uur, bij de servicedesk. De sleutelbeheerder trekt het certificaat in en publiceert
  de intrekking via de gebruikelijke kanalen (CRL of OCSP). [8.24.01]
- Voor certificaten waarvan de dienstverlening afhangt (bijvoorbeeld voor websites, koppelingen en
  ketenaansluitingen) bepaalt de risicoafweging of de organisatie reservecertificaten van een andere
  leverancier nodig heeft. Is dat zo, dan liggen er afspraken met die leverancier en is de vervanging
  beschreven in het continuïteitsplan. [8.24.05]

> **Alleen als: Waar draaien je systemen? «Eigen datacenter of serverruimte»**
>
> - Sleutels voor de eigen systemen worden in de eigen omgeving gegenereerd en beheerd. Sleutels voor
>   informatie met classificatie hoog staan in een hardware security module of een gelijkwaardige
>   voorziening. [8.24.01]

> **Alleen als: Waar draaien je systemen? «Hostingpartij (IaaS, gedeeld datacenter)»**
>
> - Waar de hostingpartij versleuteling of certificaten levert, staat in het contract wie de sleutels beheert,
>   dat de hostingpartij de normen uit dit beleid volgt en dat de organisatie inzage krijgt in het
>   sleutelbeheer. Interne certificaten van de hostingpartij staan ook in de inventaris van de organisatie. [8.24.01, 8.24.02]

> **Alleen als: Waar draaien je systemen? «Vooral SaaS en publieke cloud»**
>
> - Bij SaaS en publieke cloud toetst de organisatie bij inkoop of de leverancier versleutelt bij transport en
>   opslag volgens dit beleid. Voor informatie met classificatie hoog kiest de organisatie waar het kan voor
>   sleutels die zij zelf beheert (customer-managed keys) of die buiten de leverancier liggen. [8.24.01]
> - De versleutelingsinstellingen van elke clouddienst staan in de inventaris, ook als de leverancier de
>   sleutels beheert. [8.24.02]

> **Alleen als: Mogen medewerkers eigen apparaten gebruiken (BYOD)? «Ja, onder voorwaarden»**
>
> - Op privéapparaten (BYOD) staan werkgegevens alleen in een beheerde, versleutelde app-omgeving met een
>   eigen sleutel van de organisatie, die de organisatie op afstand kan wissen zonder de privégegevens te
>   raken. [8.24.01]

> **Alleen als: In welke gevoelige domeinen verwerk je persoonsgegevens? «Sociaal domein» of «Jeugd» of «Gezondheid (WvGGZ, NTA 7516)»**
>
> - Mail met bijzondere persoonsgegevens (sociaal domein, jeugd of gezondheid) gaat naar externe ontvangers
>   alleen over een kanaal dat versleuteling afdwingt en de ontvanger controleert, bijvoorbeeld beveiligde mail
>   volgens NTA 7516. Zonder zo'n kanaal wordt de informatie niet gemaild. [8.24.01]

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| **[lijneigenaar cryptografie]** | Uitvoering van dit beleid en de inventaris van cryptografische middelen |
| Eigenaar cryptografie | Implementatie van versleuteling en de halfjaarlijkse toets op de adviezen van NCSC en NBV |
| Sleutelbeheerder | Levenscyclus van sleutels en certificaten, intrekking bij misbruik |
| Systeemeigenaar | Beschermingsniveau per systeem en afspraken met leveranciers |
| CISO | Advies, toetsing van dit beleid en van afwijkingen op de standaarden |
| Medewerkers | Zorgvuldig gebruik van tokens en sleutels, direct melden van verlies |

## 5. Naleving en bewaking

- Doorlopend: meting van websites en maildomeinen tegen de verplichte standaarden, bijvoorbeeld met
  internet.nl; bewijs is de maandelijkse uitslag en de afhandeling van afwijkingen.
- Halfjaarlijks: controle van de inventaris op volledigheid, vervaldata en zwakke instellingen; bewijs is
  het bijgewerkte overzicht met acties.
- Jaarlijks: test van herstel van een versleutelde back-up en, waar reservecertificaten zijn afgesproken,
  een oefening met de vervanging.
- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid
informatieclassificatie (niveaus), het beleid bedrijfsmiddelenbeheer (inventaris), het beleid back-up en
recovery, het beleid mobile device management, het beleid leveranciersbeheer (afspraken over versleuteling)
en het continuïteitsbeleid (reservecertificaten).

## Bijlage: BIO 2.0-maatregelen

De overheidsmaatregelen van dit domein (4) en waar dit stuk ze invult. Nummers volgens BIO2 v1.3 definitief - 9 januari 2026; de tekst van de maatregel staat bij het CIP.

| Maatregel | Titel | In dit stuk |
|---|---|---|
| 8.24.01 | Gebruik van cryptografie | 3.1 Wanneer de organisatie cryptografie inzet |
| 8.24.02 | Gebruik van cryptografie | 3.3 Verantwoordelijkheden en registratie |
| 8.24.04 | Gebruik van cryptografie | 3.2 Normen en sterkte |
| 8.24.05 | Gebruik van cryptografie | 3.4 Sleutel- en certificaatbeheer |

## Nog in te vullen

- **termijn uitfaseren**: bijvoorbeeld zes maanden na publicatie van het advies
- **eigenaar cryptografie**: de functie die verantwoordelijk is voor de implementatie, bijvoorbeeld de IT-architect of het hoofd IT
- **sleutelbeheerder**: de functie die verantwoordelijk is voor het sleutel- en certificaatbeheer
- **waarschuwingstermijn verlopen**: bijvoorbeeld 60 dagen
- **lijneigenaar cryptografie**: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd IT
