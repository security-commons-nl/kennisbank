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

Voor een DPIA (artikel 35 AVG) ligt bij het Rijk en de Informatiebeveiligingsdienst (IBD) alles wat je
nodig hebt, vrij te gebruiken. Dit stuk voegt geen eigen model toe; het zegt welk stuk je wanneer pakt.
De adressen staan onderaan, bij *Wat anderen al hebben*.

## 1. Moet het? De pre-scan

De **pre-scan in de Invulhulpen van het Rijk** rekent zelf uit of een DPIA verplicht of aanbevolen is,
en signaleert of een DTIA, KIA of IAMA in beeld komt. Draait in de browser, zonder account. De IBD heeft
een **sjabloon pre-DPIA** in Word, in de handreiking van stap 2.

## 2. Hoe pak je het aan? Twee modellen

Beide voldoen, gemeenten gebruiken ze allebei. **Het Rijksmodel DPIA 3.0 via de Invulhulpen**: 210
vragen, exporteert pdf en een JSON-dossier dat je later weer inlaadt; de vragenlijsten staan als YAML in
`MinBZK/par-dpia-form` (EUPL-1.2). **De DPIA-handreiking van de IBD** *Samen naar een kwalitatief goede
DPIA*: sjablonen voor DPIA, pre-DPIA en werkproces, checklists, een stappenplan op een A4 en drie
webinars (september 2024). Kies het Rijksmodel voor een machineleesbaar dossier, de IBD-handreiking als
je al met IBD-sjablonen werkt. In beide is *Maatregelen* een leeg vak: daar zit het werk.

## 3. Hoe zag het er elders uit?

De **collectieve DPIA's van de IBD**: 27 uitgevoerde gemeentelijke DPIA's (peildatum 25-09-2026),
geanonimiseerd, over onder meer jeugdhulp, schuldhulpverlening, handhaving, personeelsdossiers, bodycams
en scanauto's. De IBD zegt zelf: overnemen en bij bepaalde delen aanpassen mag, maar het is geen
knip-en-plakwerk; de DPIA moet kloppen met het proces zoals het bij jou loopt.

## 4. Zit er AI of een algoritme in?

Dan komen erbij: de **AI-specifieke toelichting voor DPIA's** van de IBD (versie 1.0, augustus 2026), per
onderdeel van het format wat je extra nagaat, en de **IAMA** als derde invulhulp van het Rijk. De
**IBD-notitie DPIA Microsoft Copilot** laat zien hoe zo'n beoordeling uitpakt.

## 5. En daarna

De opvolging van maatregelen is voor de meeste organisaties het moeilijkste deel. De **handreiking
privacy-risicomanagement** van de IBD geeft daar een stappenplan, een rolverdeling en een risicoregister
voor.

## Wat hier bewust niet staat

Geen eigen model en geen DPIA's van een aanwijsbare organisatie. Wat de commons wil toevoegen is wat in
geen van deze stukken staat: per soort verwerking de risico's en maatregelen die telkens terugkeren, als
voorstel dat je per regel bevestigt. Dat is het plan `dpiacheck`; zodra het er is, verwijst deze
wegwijzer ernaar.
