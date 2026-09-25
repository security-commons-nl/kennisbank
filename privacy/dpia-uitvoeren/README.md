---
titel: Een DPIA uitvoeren: wat er al ligt
vakgebied: privacy
type: referentie
normen: [AVG]
peildatum: 2026-09-25
herkomst: wegwijzer samengesteld door de commons; de stukken zelf zijn van het Rijk en de Informatiebeveiligingsdienst
status: concept
samenvatting: Voor een DPIA hoef je niets zelf te bouwen. Het Rijk heeft een invulhulp die de plichttoets uitrekent en het Rijksmodel invult, de Informatiebeveiligingsdienst heeft een handreiking met sjablonen en een bibliotheek met 27 uitgevoerde gemeentelijke DPIA's om van te lenen. Deze wegwijzer zet ze in de volgorde waarin je ze gebruikt.
bronnen: [bzk-invulhulpen, bzk-par-dpia-form, ibd-dpia-handreiking, ibd-collectieve-dpias, ibd-ai-toelichting-dpia, ibd-notitie-dpia-copilot, ibd-privacy-risicomanagement]
---

# Een DPIA uitvoeren: wat er al ligt

> **Lees de wegwijzer online:** [security-commons-nl.github.io/kennisbank/privacy/dpia-uitvoeren](https://security-commons-nl.github.io/kennisbank/privacy/dpia-uitvoeren/)

Een gegevensbeschermingseffectbeoordeling (DPIA, artikel 35 AVG) is voor de meeste gemeentelijke
verwerkingen geen nieuw terrein: het Rijk en de Informatiebeveiligingsdienst (IBD) hebben er allebei
werk voor liggen dat vrij te gebruiken is. Dit stuk voegt daar geen eigen model aan toe. Het zegt
welk stuk je op welk moment pakt, en wat je er wel en niet van mag verwachten. De adressen staan
onderaan, bij *Wat anderen al hebben*.

## 1. Moet het? De pre-scan

Begin met de **pre-scan in de Invulhulpen van het Rijk**. Die stelt 57 vragen in acht blokken en
rekent zelf uit of een DPIA verplicht is (de lijst van de Autoriteit Persoonsgegevens, de criteria
van de EDPB, nieuwe wetgeving, een risicoscore) of aanbevolen. Hij signaleert ook of een DTIA, KIA of
IAMA in beeld komt. De invulhulp draait in de browser; het formulier zonder account, het samenwerken
met een account. De IBD heeft een eigen **sjabloon pre-DPIA** in de handreiking (stap 2), als je
liever in Word werkt.

## 2. Hoe pak je het aan? Twee modellen naast elkaar

Er zijn twee modellen die allebei voldoen, en gemeenten gebruiken ze allebei:

- **Het Rijksmodel DPIA (versie 3.0), via de Invulhulpen.** 210 vragen in 21 hoofdstukken, van
  beschrijving en rechtsgrond tot de acht rechten van betrokkenen, risico's en maatregelen met
  restrisico. De invulhulp exporteert een pdf en een JSON-dossier dat je later weer kunt inladen. De
  vragenlijsten staan als YAML in de repo `MinBZK/par-dpia-form`, onder EUPL-1.2, zodat je ze ook in
  je eigen tooling kunt gebruiken.
- **De DPIA-handreiking van de IBD, *Samen naar een kwalitatief goede DPIA*,** met een sjabloon DPIA,
  een sjabloon pre-DPIA, een sjabloon werkproces, checklists, een stappenplan op een A4 en drie
  webinars. De stukken zijn van september 2024; de lijst *Must have DPIA's* van maart 2025.

Kies het Rijksmodel als je wilt dat het dossier machineleesbaar is en aansluit bij wat het Rijk
bijhoudt. Kies de IBD-handreiking als je organisatie al met IBD-sjablonen werkt of het werkproces
eromheen nog moet inrichten. Wat je ook kiest: bij *Maatregelen* staat in beide een leeg vak. Daar zit
het werk.

## 3. Hoe zag het er elders uit? De collectieve DPIA's

De IBD houdt een **bibliotheek van uitgevoerde gemeentelijke DPIA's** bij: op 25-09-2026 27 stuks,
geanonimiseerd en ontdaan van gevoelige informatie, over onder meer jeugdhulp, schuldhulpverlening,
handhaving Participatiewet, personeelsdossiers, bodycams, scanauto's, e-mailarchivering en de Wpg. De
IBD zegt zelf wat je ermee mag: gemeenten kunnen de inhoud overnemen en bij bepaalde delen aanpassen en
aanvullen, maar het is geen knip-en-plakwerk; de verwerkingsverantwoordelijke moet zorgen dat de DPIA
klopt met het proces zoals het bij haar loopt. Gebruik ze dus als startpunt voor de risico's en
maatregelen, niet als eindproduct.

## 4. Zit er AI of een algoritme in?

Dan komen er twee stukken bij. De **AI-specifieke toelichting voor DPIA's** van de IBD (versie 1.0,
augustus 2026) zegt per onderdeel van het standaardformat wat je extra nagaat als de verwerking een
AI-component heeft. En de **IAMA** (Impact Assessment Mensenrechten en Algoritmes) zit als derde
invulhulp in dezelfde omgeving van het Rijk als de pre-scan en de DPIA. Voor een concreet geval is de
**IBD-notitie DPIA Microsoft Copilot** een voorbeeld van hoe die beoordeling uitpakt.

## 5. En daarna: de risico's opvolgen

Een DPIA levert maatregelen op; de meeste organisaties merken dat de opvolging daarvan het moeilijkste
deel is. De **handreiking privacy-risicomanagement** van de IBD gaat precies daarover: een stappenplan
voor het opvolgen van risico's, de verdeling van verantwoordelijkheden, en formats die aansluiten op de
DPIA-handreiking, met een risicoregister erbij.

## Wat hier bewust niet staat

Geen eigen model, geen eigen sjabloon en geen ingevulde DPIA's van een aanwijsbare organisatie. Wat de
commons wel wil toevoegen is wat in geen van deze stukken staat: bij elke soort verwerking de risico's
en maatregelen die in uitgevoerde DPIA's telkens terugkeren, als voorstel dat de gebruiker per regel
bevestigt. Dat is het plan `dpiacheck`; zodra het er is, verwijst deze wegwijzer ernaar.
