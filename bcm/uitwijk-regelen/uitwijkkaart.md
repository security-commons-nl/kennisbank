# Uitwijkkaart per kritieke dienst

Een kaart per kritieke dienst, en een overzichtsblad over alle diensten. Wat al in de BIA staat, neem je over;
de kaart vraagt alleen wat nieuw is. De toelichting staat in de [handleiding](README.md).

Werk je in een spreadsheet: een tabblad per dienst plus het overzichtsblad. De kolommen hieronder zijn de
velden.

## De kaart

| Veld | Vulling | Komt uit |
|---|---|---|
| Dienst en eigenaar | | BIA |
| Kriticiteitsklasse | | BIA |
| MTPD, RTO, RPO | | BIA |
| Noodniveau: wat minimaal door moet | | BIA |
| Minimale noodorganisatie: mensen, systemen, werkplekken | | nieuw |
| Laag die uitvalt | eigen platform · hosting · SaaS of PaaS · leverancier · locatie · mensen | nieuw |
| Leverancier(s), contractvorm, einddatum | | contractbeheer |
| Concentratie: welke andere kritieke diensten zitten bij dezelfde leverancier of op hetzelfde platform | | ketenoverzicht |
| Wat staat buiten de dienst | back-up buiten de dienst (ja of nee, waar, hoe oud) · configuratie · documentatie om op te bouwen · exportformaat | nieuw |
| Gekozen uitwijkvorm | geen · bewust uitstel · analoge terugval · herstel uit back-up op schone omgeving · cold, warm, hot of gespiegeld · onderlinge uitwijk met ... · tweede leverancier · eigen landingsplaats | nieuw |
| Haalt deze vorm de RTO en het noodniveau | ja of nee, met de verwachte hersteltijd | nieuw |
| Exitplan, geplande exit | aanwezig ja of nee, laatst beoordeeld | contract |
| Exitplan, disruptieve onderbreking | aanwezig ja of nee, laatst beoordeeld | contract |
| Contractueel geregeld | dataportabiliteit · step-in · escrow · inzicht in onderaannemers · opzegging bij dreigend faillissement | contract |
| Budget voor een acute exit | gereserveerd ja of nee, bedrag | begroting |
| Wie activeert, wie besluit | | BCP |
| Laatste test | datum · soort (tafeloefening, deeltest, echte uitwijk) · gemeten hersteltijd · restpunten | testverslag |
| Volgende test en herziening | | planning |

## Het overzichtsblad

Een regel per dienst, alleen de kolommen waar de directie op stuurt. Rood is wat aandacht vraagt.

| Dienst | RTO | Gekozen vorm | Haalt RTO | Exitplan (beide scenario's) | Laatste echte test | Restpunten open |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |
| | | | | | | |

Drie vragen die dit blad moet beantwoorden:

1. Welke diensten halen hun hersteltijd niet met de uitwijk die er nu is?
2. Welke clouddienst heeft geen exitplan voor onverwachte uitval?
3. Welke uitwijk is nooit echt uitgevoerd?

## Voorbeeld 1: een SaaS-dienst (verzonnen)

Een gemeente gebruikt een SaaS-zaaksysteem voor vergunningen.

| Veld | Vulling |
|---|---|
| Dienst en eigenaar | Omgevingsvergunningen verlenen; teamleider vergunningen |
| MTPD, RTO, RPO | MTPD 5 werkdagen (wettelijke termijnen lopen door); RTO 2 werkdagen; RPO 1 werkdag |
| Noodniveau | Spoedaanvragen en lopende termijnen bewaken; nieuwe reguliere aanvragen mogen wachten |
| Laag die uitvalt | SaaS |
| Concentratie | Dezelfde leverancier levert ook het zaaksysteem voor sociaal domein |
| Wat staat buiten de dienst | Dagelijkse export van zaakgegevens en documenten naar eigen opslag, formaat CSV plus pdf; configuratie niet |
| Gekozen uitwijkvorm | Analoge terugval op de export (termijnbewaking in een spreadsheet), herstel bij de leverancier |
| Haalt RTO | Ja voor het noodniveau; nee voor volledige dienstverlening als de leverancier stopt |
| Exitplan | Geplande exit: ja, in het contract. Disruptief: nee |
| Contractueel | Dataportabiliteit ja; step-in nee; opzegging bij dreigend faillissement nee |
| Budget acute exit | Niet gereserveerd |
| Laatste test | Tafeloefening, vorig jaar; de export bleek drie dagen oud |
| Restpunten | Disruptief exitplan opstellen; exportcontrole dagelijks automatiseren; opzeggingsrecht meenemen bij de verlenging |

## Voorbeeld 2: een eigen platform (verzonnen)

Een waterschap draait de financiële administratie op een eigen virtueel platform in een datacenter van een
hostingpartij.

| Veld | Vulling |
|---|---|
| Dienst en eigenaar | Betalingen aan leveranciers en uitkeringen; hoofd financiën |
| MTPD, RTO, RPO | MTPD 3 werkdagen; RTO 1 werkdag; RPO 4 uur |
| Noodniveau | Betaalbatch van vaste lasten en uitkeringen moet draaien |
| Laag die uitvalt | ICT-platform en data |
| Wat staat buiten de dienst | Onveranderbare back-up in een tweede datacenter van een andere partij; configuratie als code in een eigen repository |
| Gekozen uitwijkvorm | Warm site bij de tweede partij, herstel uit back-up |
| Haalt RTO | Ja, gemeten 14 uur bij de laatste test |
| Laatste test | Echte uitwijk van de betaalbatch, vorig najaar; terugkeer naar de primaire omgeving duurde twee dagen langer dan gepland |
| Restpunten | Terugkeerprocedure herschrijven; certificaten op de uitwijkomgeving liepen af zonder melding |
