# Beleid informatieclassificatie

Beleid informatiebeveiliging, BIO 2.0-domein *Informatie classificatie*. Status: concept, vast te stellen door de organisatie zelf.

Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor het classificeren, labelen en veilig
overdragen van informatie. Classificeren is het vaststellen hoe zwaar informatie beschermd moet worden op
beschikbaarheid, integriteit en vertrouwelijkheid (BIV). De classificatie bepaalt welke maatregelen uit de
andere beleidsstukken van toepassing zijn. Het beleid geldt voor alle informatie van de organisatie, in alle
systemen en op alle dragers, en voor iedereen die die informatie verwerkt. Het gaat over de
ISO-beheersmaatregelen 5.12 tot en met 5.14.

Buiten dit beleid vallen de versleutelingseisen zelf (beleid cryptografie) en de toegangsrechten per
classificatie (beleid logische toegangsbeveiliging).

## 2. Uitgangspunten

1. De eigenaar van de informatie (meestal de proceseigenaar) bepaalt de classificatie en accepteert het
   restrisico. De CISO en de privacy officer adviseren.
2. Zo laag als verantwoord: te hoog classificeren kost geld en belemmert openbaarheid. Wettelijke eisen gaan
   altijd voor.
3. Het meest gevoelige deel bepaalt de classificatie van het geheel. Een systeem krijgt de classificatie van
   de zwaarste informatie die het verwerkt, tenzij het systeem die informatie apart afschermt.

## 3. Beleidsregels

### 3.1 Classificatiemethode

- De organisatie classificeert met een vastgestelde impactmethode die deel uitmaakt van de
  risicomanagementmethode van de organisatie, bijvoorbeeld de baselinetoets of een BIA. De methode staat in
  **[classificatiemethode]**. [5.12.01]
- De impact op het proces wordt per BIV-aspect gescoord op een schaal van 0 tot en met 3 en vertaald naar een
  niveau:

  | Impact | Beschikbaarheid | Integriteit | Vertrouwelijkheid |
  |---|---|---|---|
  | 0 verwaarloosbaar | niet nodig | niet zeker | openbaar |
  | 1 beperkt | belangrijk (BBN1) | beschermd (BBN1) | intern (BBN1) |
  | 2 ernstig | noodzakelijk (BBN2) | hoog (BBN2) | vertrouwelijk (BBN2) |
  | 3 zeer ernstig | essentieel (BBN2 met aanvullende risicoanalyse) | absoluut (BBN2 met aanvullende risicoanalyse) | geheim (BBN3) |

- BBN3 voor vertrouwelijkheid geldt als de informatie weerstand vraagt tegen statelijke actoren of tegen
  georganiseerde criminaliteit en ondermijning.
- De informatie in elk informatiesysteem is geclassificeerd op basis van een expliciete risicoafweging, vóór
  ingebruikname en daarna bij elke ingrijpende wijziging en ten minste elke drie jaar. De eigenaar legt de
  uitkomst vast in een classificatierapport met de ingevulde vragenlijsten, ondertekend als besluit. [5.12.01]
- De classificatie per systeem staat in de inventaris van bedrijfsmiddelen.

### 3.2 Eisen per niveau

- Elk niveau heeft een vaste set minimumeisen; de basis is de BIO 2.0 bij het bijbehorende BBN. Aanvullend
  geldt ten minste:

  | Niveau vertrouwelijkheid | Authenticatie | Autorisatie | Opslag en transport |
  |---|---|---|---|
  | intern (BBN1) | persoonsgebonden account; meerfactor bij toegang van buiten | toegang voor medewerkers van de organisatie | versleuteld transport buiten het eigen netwerk |
  | vertrouwelijk (BBN2) | meerfactor | toegang per rol, door de eigenaar toegekend | versleuteld transport en versleutelde opslag; zo min mogelijk kopieën |
  | geheim (BBN3) | meerfactor met een sterk middel, geen single sign-on | toegang per persoon, vierogenprincipe | aanvullende maatregelen op basis van een eigen risicoanalyse |

- Voor integriteit van BBN2 en hoger geldt het vierogenprincipe bij wijzigingen van gegevens die
  rechtsgevolgen hebben, en worden wijzigingen gelogd. Voor beschikbaarheid legt de eigenaar per systeem de
  hersteltijd en het toelaatbaar gegevensverlies vast in het continuïteitsbeleid.

> **Alleen als: In welke gevoelige domeinen verwerk je persoonsgegevens? «Sociaal domein» of «Jeugd»**
>
> - Informatie over cliënten in het sociaal domein of de jeugdhulp krijgt ten minste vertrouwelijk (BBN2) voor
>   vertrouwelijkheid en hoog (BBN2) voor integriteit. Een lagere classificatie kan alleen met een
>   gedocumenteerd besluit van de eigenaar na advies van de privacy officer. [5.12.01]

> **Alleen als: In welke gevoelige domeinen verwerk je persoonsgegevens? «Gezondheid (WvGGZ, NTA 7516)»**
>
> - Gezondheidsinformatie is een bijzonder persoonsgegeven en krijgt ten minste vertrouwelijk (BBN2). Ad-hoc
>   uitwisseling per e-mail of chat voldoet aan de NTA 7516: gezondheidsinformatie hoort in het
>   vakinhoudelijke systeem, gaat per e-mail alleen als dat niet kan en dan alleen versleuteld via beveiligde
>   mail, met een vastgestelde grond om te verzenden en een gecontroleerde ontvanger. Automatisch doorsturen,
>   leesbevestigingen en het delen van inloggegevens zijn niet toegestaan; wie namens een ander mailt, doet dat
>   via een zichtbare mandaatfunctie. [5.12.01]
> - De organisatie biedt burgers een beveiligde mailvoorziening aan en vermeldt die op de website.

> **Alleen als: Verwerk je politiegegevens (boa's, opsporing, handhaving)? «Ja»**
>
> - Politiegegevens die de organisatie verwerkt (bijvoorbeeld door boa's of in de handhaving) worden apart
>   geclassificeerd en krijgen ten minste vertrouwelijk (BBN2). Ze worden gescheiden gehouden van de overige
>   informatie in een systeem of omgeving waarvoor de autorisatie-, logging- en bewaareisen van de Wet
>   politiegegevens gelden, en gaan niet via gewone e-mail of chat naar ontvangers buiten de kring die de wet
>   toestaat. [5.12.01]

### 3.3 Labelen

- Informatie van vertrouwelijk (BBN2) en hoger is herkenbaar gelabeld: digitaal met een classificatielabel
  in de metagegevens, en op papier met het niveau op elke pagina. Systemen die labels ondersteunen, passen
  de bijbehorende beveiliging (versleuteling, deelbeperkingen) automatisch toe.
- Hardware krijgt een sticker met het kenmerk uit de inventaris.

### 3.4 Overdragen van informatie

- Websites, webapplicaties, API's en het e-mailverkeer van de organisatie die vanaf internet bereikbaar zijn,
  voldoen aan de verplichte standaarden van de lijst van het Forum Standaardisatie en aan de eisen uit het
  Cyberbeveiligingsbesluit. De organisatie stelt die zo in dat de beveiliging maximaal is zonder dat de dienst
  ervan uitvalt. [5.14.01]
- **[beheerder internetfacing systemen]**
  meet elke maand alle domeinen met internet.nl, rapporteert de scores aan de CISO en zet tekortkomingen
  binnen drie maanden om in een wijziging of een geaccepteerd risico. [5.14.01]
- Voor openbaar webverkeer met gevoelige gegevens gebruikt de organisatie ten minste publiek vertrouwde
  OV-certificaten; voor intern webverkeer met gevoelige gegevens ten minste publiek vertrouwde OV-certificaten
  of PKIoverheid-certificaten uit een private stam. Zwaardere certificaten volgen uit een risicoanalyse,
  aansluitvoorwaarden of wetgeving. [5.14.02]
- Gebruikt de organisatie geavanceerde of gekwalificeerde elektronische handtekeningen, dan voldoen die aan
  de AdES Baseline Profiles van de lijst open standaarden. Bij aanschaf van een ondertekendienst is dat een
  eis in de uitvraag. [5.14.03]
- De organisatie heeft één actuele registratie van alle internetfacing systemen, webapplicaties, IP-adressen
  en API's, als onderdeel van de inventaris van bedrijfsmiddelen. Een nieuw systeem komt pas online na
  registratie. [5.14.04]
- Alle publiek toegankelijke websites zijn aangemeld in het Register Internetdomeinen Overheid. De
  registratie wordt ten minste elk halfjaar bijgewerkt. [5.14.05]

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| Proceseigenaar (eigenaar van de informatie) | Classificatie, classificatierapport en acceptatie van het restrisico |
| Systeemeigenaar | Toepassen van de maatregelen die bij de classificatie horen; registratie in de inventaris |
| **[beheerder internetfacing systemen]** | Metingen met internet.nl, certificaten, registratie van internetfacing systemen en RIO |
| CISO | Methode, advies bij classificatie, toetsing van de uitkomsten en van dit beleid |
| Privacy officer of FG | Advies bij classificatie van persoonsgegevens |
| Medewerkers | Informatie labelen en volgens het niveau behandelen |

## 5. Naleving en bewaking

- Jaarlijks: controle dat elk systeem in de inventaris een classificatie heeft die niet ouder is dan drie
  jaar; bewijs is de lijst met ontbrekende of verlopen classificaties en de afhandeling.
- Maandelijks: internet.nl-scores per domein, met een kwartaaloverzicht aan de CISO.
- Halfjaarlijks: vergelijking van de registratie van internetfacing systemen en van het RIO met een externe
  scan van de domeinen en IP-reeksen van de organisatie.
- Jaarlijks: steekproef op de certificaten van internetfacing systemen met gevoelige gegevens.
- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. De classificatie stuurt het beleid
logische toegangsbeveiliging, het beleid cryptografie, het beleid logging en monitoring, het beleid afvoer
en hergebruik van gegevensdragers en het continuïteitsbeleid. De inventaris uit het beleid
bedrijfsmiddelenbeheer bevat de classificaties en de registratie van internetfacing systemen.

## Bijlage: BIO 2.0-maatregelen

De overheidsmaatregelen van dit domein (6) en waar dit stuk ze invult. Nummers volgens BIO2 v1.3 definitief - 9 januari 2026; de tekst van de maatregel staat bij het CIP.

| Maatregel | Titel | In dit stuk |
|---|---|---|
| 5.12.01 | Classificeren van informatie | 3.1 Classificatiemethode |
| 5.14.01 | Overdragen van informatie | 3.4 Overdragen van informatie |
| 5.14.02 | Overdragen van informatie | 3.4 Overdragen van informatie |
| 5.14.03 | Overdragen van informatie | 3.4 Overdragen van informatie |
| 5.14.04 | Overdragen van informatie | 3.4 Overdragen van informatie |
| 5.14.05 | Overdragen van informatie | 3.4 Overdragen van informatie |

## Nog in te vullen

- **classificatiemethode**: het vastgestelde document met vragenlijsten en impactschaal
- **beheerder internetfacing systemen**: de functie die de metingen uitvoert, bijvoorbeeld de netwerkbeheerder
