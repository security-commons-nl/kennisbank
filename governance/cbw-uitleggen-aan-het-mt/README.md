---
titel: De Cyberbeveiligingswet uitgelegd aan het MT
vakgebied: governance
type: lesmateriaal
normen: [Cbw, NIS2, BIO2]
peildatum: 2026-10-29
herkomst: opgesteld door de CISO van een regionale samenwerking van vier gemeenten, voor de managementteams van die gemeenten, naast de verplichte training van de colleges
status: concept
route: geen
samenvatting: Een sessie van twee uur voor het managementteam of directieteam van een gemeente over de Cyberbeveiligingswet, naast de certificaattraining van het college. Eerst de wet en de plichten op een rij, dan de tien vereisten van de zorgplicht, elk op een plek in de gemeente die iedereen herkent, van het gemaal tot de keukentafel. Bij elk vereiste dezelfde drie vragen: welk risico, wie koos, waar staat het. Een sjabloon met invulvelden en een eigen deel Waar staan we nu.
bronnen: [ncsc-cbw-valt-mijn-organisatie-eronder, rdi-cbw-wat-betekent-het-voor-u, do-cbw-welke-overheidsorganisaties, ibd-bio2-factsheet-informatiebeveiliging-en-de-lijnmanager, ibd-bio-handreiking-risicomanagement-voor-gemeenten]
---

# De Cyberbeveiligingswet uitgelegd aan het MT

> **Lees dit lesmateriaal online:** [security-commons-nl.github.io/kennisbank/governance/cbw-uitleggen-aan-het-mt](https://security-commons-nl.github.io/kennisbank/governance/cbw-uitleggen-aan-het-mt/)

Het college van een gemeente keurt de maatregelen van de Cyberbeveiligingswet goed en volgt een verplichte
training met certificaat. Het managementteam hoeft dat niet. Toch is het MT de plek waar de wet werkt of niet
werkt: daar liggen de processen, de leveranciers, de mensen en de keuzes. Dit lesmateriaal is voor die sessie.
Het is geen certificaattraining en het gaat niet over boetes. Het gaat over één vraag die bij elk vereiste
terugkomt, tot vervelens toe:

**Welk risico? Wie koos? Waar staat het?**

De wet zegt bij de zorgplicht steeds *passend en evenredig*, en bij een van de vereisten letterlijk *waar
gepast*. Niet alles hoeft. Maar wat je niet doet, moet een keuze zijn die iemand heeft gemaakt en die ergens
staat.

## Wat er in deze map staat

- [De platen](platen.html): 26 platen voor een sessie van twee uur. Bladeren met de pijltjestoetsen; op een
  plaat met een knop onthult de pijl eerst de rest. Op de tien zorgplicht-platen staat alleen de keuzevraag; de
  uitleg staat achter de knop Meer uitleg, als reserve voor de spreker, en daar bladert de pijl gewoon door. Print op
  A4 liggend.
- [Het draaiboek](draaiboek.md): per plaat de tijd en wat je doet, met antwoordlijnen voor de vragen die
  altijd komen.
- [De tekst van de platen](data/platen.json): wie een plaat wil aanpassen, doet dat hier.
- [Het invulblok](data/invulblok.json): de velden voor de eigen organisatie, zie *Een eigen versie maken*.
- De beelden los, om in een eigen presentatie te gebruiken (in PowerPoint: invoegen als afbeelding, daarna
  converteren naar vorm): [wetketen](img/wetketen.svg) · [tijdlijn](img/tijdlijn.svg) ·
  [het NCSC-portaal](img/mijnncsc.svg) · [meldklok](img/meldklok.svg) · [refrein](img/refrein.svg) ·
  [luchtfoto](img/luchtfoto.svg) · [klantcontact](img/kcc.svg) · [gemaal](img/gemaal.svg) ·
  [leverancier](img/leverancier.svg) · [formulier](img/formulier.svg) · [verkiezing](img/verkiezing.svg) ·
  [keukentafel](img/keukentafel.svg) · [envelop](img/envelop.svg) · [balie](img/balie.svg) ·
  [crisisruimte](img/crisisruimte.svg).

## Opbouw

1. **De wet.** Het college tekent, het MT laat het werken. Van NIS2 naar de BIO2, drie woorden om te
   onthouden, wie er meekijkt en hoe de klok loopt.
2. **De plichten.** Registreren, melden, besturen en zorgen op één plaat. Het NCSC-portaal als het ene loket,
   de meldklok van 24 uur, 72 uur en een maand, en de sleutelplaat met het refrein.
3. **De zorgplicht.** De tien vereisten uit artikel 21, derde lid, eerst als overzicht en dan een voor een.
   Elk vereiste staat op een plek in de gemeente, met wat er mis kan gaan voor beschikbaarheid, integriteit en
   vertrouwelijkheid, de keuze die daar gemaakt moet worden, en een voorbeeld van wat passend is.
4. **Waar staan we nu?** Drie platen die de eigen organisatie invult: registreren en melden, de tien
   vereisten als stoplicht, en de kritieke processen.
5. **Wat we vragen.** Per kritiek proces een eigenaar, een gekozen hersteltijd en geaccepteerde risico's met
   een naam en een datum.

## De tien vereisten, elk op een plek in de gemeente

| | Vereiste | Plek | Wat er misgaat |
|---|---|---|---|
| a | Risico's kennen | Luchtfoto van de gemeente | beschikbaarheid, integriteit, vertrouwelijkheid |
| b | Incidenten afhandelen | Klantcontact en webdiensten | beschikbaarheid, integriteit |
| c | Doordraaien en herstellen | Het gemaal | beschikbaarheid |
| d | Leveranciers | Uitkeringen op de eerste van de maand | beschikbaarheid, vertrouwelijkheid |
| e | Veilig kopen en onderhouden | Online aanvragen | vertrouwelijkheid, integriteit |
| f | Werkt het ook? | Verkiezingen | integriteit |
| g | Hygiëne en opleiding | Het sociaal loket aan de keukentafel | vertrouwelijkheid, integriteit |
| h | Versleutelen | Jeugdzorg | vertrouwelijkheid |
| i | Mensen, toegang en spullen | De balie van burgerzaken | vertrouwelijkheid, integriteit |
| j | Inloggen en elkaar bereiken | De crisisorganisatie | beschikbaarheid, vertrouwelijkheid |

De koppeling tussen vereiste en plek is een keuze om het tastbaar te maken, geen indeling uit de wet. Elk
vereiste geldt voor elk proces. Wie andere plekken herkenbaarder vindt, past de beelden en de tekst aan.

## Een eigen versie maken

1. Kopieer [het invulblok](data/invulblok.json) en vul in: de naam van de gemeente, de datum, een contact, en
   de stand per onderdeel (groen, oranje, rood of onbekend, met een korte toelichting). Een foto van het eigen
   gemeentehuis of van een eigen proces kan erbij; die gaat in de pagina zelf.
   Eigen regels bij een plaat, zoals hoe de collegetraining bij jullie loopt, zet je onder `aanvullingen`; ze
   staan in groen op de plaat, zodat zichtbaar is wat lokaal is.
2. Draai vanuit de kennisbank:
   `python tools/bouw_cbw_mt.py --invul jouw-invulblok.json --uit jouw-platen.html`
3. Wat leeg blijft, staat op de platen als oranje invulveld. Zo zie je meteen wat nog ontbreekt.

De eigen versie bevat de stand van de eigen organisatie. Deel die niet verder dan nodig.

## Waarom een aparte sessie voor het MT

De trainingsplicht met certificaat (artikel 24, vijfde lid) geldt de leden van het bestuur, voor een gemeente
het college. Het eerste lid van hetzelfde artikel zegt dat het bestuur de maatregelen goedkeurt. Wie die
maatregelen uitvoert, staat niet in de wet: dat is de lijn. Deze sessie maakt die verdeling zichtbaar en legt
de keuzes waar ze horen. De syllabus van de VNG voor de bestuurderstraining beschrijft de andere kant: wat het
college van het MT mag verwachten.

## Elders in de kennisbank

- [Val ik onder de Cbw](../val-ik-onder-de-cbw/): voor wie eerst wil weten of de wet geldt.
- [Cbw-meldplicht inrichten](../cbw-meldplicht-inrichten/): de meldprocedure en het invullen van de registratie.
- [BCM uitleggen aan de bestuurder](../../bcm/bcm-voor-de-bestuurder/): dezelfde aanpak voor
  bedrijfscontinuïteit.
- [Quantumveilig per laag](../quantumveilig-per-laag/): de verdieping bij vereiste h, versleutelen.
- Voor de kritieke processen uit deel 4: [Kritieke processen en herstelprioriteiten
  vaststellen](../../bcm/kritieke-processen-vaststellen/), [de risicosessie per
  proces](../../bcm/risicosessie-per-proces/) en [Procescheck](https://security-commons-nl.github.io/procescheck/),
  een impactanalyse per proces die in de browser rekent.
