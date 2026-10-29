---
titel: De Cbw-meldplicht en registratieplicht inrichten, voor een gemeente of een regio
vakgebied: governance
type: aanpak
normen: [Cbw, NIS2, BIO2]
peildatum: 2026-10-20
herkomst: vastgestelde meldplichtprocedure (versie 1.0, september 2026) en invulblad voor de registratie van een regionale samenwerking van vier gemeenten
status: in gebruik
route: [ciso]
samenvatting: Hoe een gemeente de meldplicht en de registratieplicht onder de Cyberbeveiligingswet in de praktijk regelt. Een vastgestelde meldplichtprocedure met de drie drempelwaarden voor een significant incident (vier uur uitval, niet in de begroting op te vangen, ernstig letsel), de klok vanaf kennisname (24 uur waarschuwen, 72 uur melden, eindverslag na een maand), de informatieplicht aan inwoners, melden namens meerdere gemeenten met mandaat, en vier invulsjablonen. Daarnaast de registratie bij het NCSC veld voor veld, met de redenering per antwoord.
bronnen: [do-cbw-welke-overheidsorganisaties, ncsc-cbw-valt-mijn-organisatie-eronder, rdi-cbw-wat-betekent-het-voor-u]
---

# De Cbw-meldplicht en registratieplicht inrichten, voor een gemeente of een regio

> **Lees de aanpak online:** [security-commons-nl.github.io/kennisbank/governance/cbw-meldplicht-inrichten](https://security-commons-nl.github.io/kennisbank/governance/cbw-meldplicht-inrichten/)

Sinds 15 augustus 2026 zijn gemeenten essentiële entiteiten onder de Cyberbeveiligingswet. Van de drie
plichten die daaruit volgen, loopt de zorgplicht meestal al via BIO 2.0 en het managementsysteem. De andere
twee zijn nieuw en moeten apart worden belegd: de **registratieplicht** (eenmalig registreren bij het NCSC en
binnen 14 dagen bijhouden) en de **meldplicht** (elk significant incident melden, binnen 24 uur een eerste
waarschuwing).

Dit item geeft beide, zoals een regionale samenwerking van vier gemeenten ze heeft ingericht.

## Wat er in deze map staat

- [meldplichtprocedure.md](meldplichtprocedure.md): de vastgestelde procedure, met de toets, de
  meldingsketen, de informatieplicht en vier sjablonen (meldformulier, tussentijds verslag, eindverslag,
  bericht aan inwoners).
- [registratie-invullen.md](registratie-invullen.md): de registratie bij het NCSC, veld voor veld, met de
  redenering achter elk antwoord en een logboek per gemeente.

Of je onder de Cbw valt, toets je eerst met [Val ik onder de Cbw?](../val-ik-onder-de-cbw/). Voor gemeenten is
dat zeker; voor gemeenschappelijke regelingen en zbo's niet altijd.

## Wanneer wel, wanneer niet

Wel voor elke gemeente, en voor elke andere organisatie die als essentiële of belangrijke entiteit onder de
Cbw valt. De procedure is geschreven voor decentrale overheden; de drempelwaarden voor andere sectoren
verschillen.

Niet als vervanging van de incidentprocedure. De meldplicht is één spoor binnen de afhandeling van een
incident; de afhandeling zelf staat in de
[procedure datalekken en beveiligingsincidenten](../../security/procedures-informatiebeveiliging/incident-response.md).

## De vier dingen die het verschil maken

1. **Wie bepaalt of iets significant is, en is die 24/7 bereikbaar?** De drempel voor financiële gevolgen is
   geen IT-oordeel maar een begrotingsoordeel. Beleg vooraf wie dat geeft. Hier: het calamiteitenteam
   digitaal toetst, de CISO meldt.
2. **De klok loopt vanaf kennisname, ook in het weekend.** T0 is het tijdstip waarop het incident in het
   registratiesysteem komt, niet het eerste overleg. Interne streeftijden van 8 en 48 uur geven marge.
3. **Melden namens meerdere gemeenten kan, maar met mandaat.** Elke gemeente blijft zelf meldplichtig. Een
   collegemandaat per gemeente en een vooraf afgesproken scenario (één melding per geraakte gemeente) voorkomen
   discussie tijdens het incident.
4. **Een datalek is niet automatisch een Cbw-incident.** Alleen vertrouwelijkheid geraakt? Dan meld je bij de
   Autoriteit Persoonsgegevens, niet onder de Cbw, tenzij ook een van de drie drempels in beeld is.

## Bewijs

- De **vastgestelde procedure**, met vaststellingsdatum en herzieningstermijn.
- Per deelnemende gemeente het **collegemandaat** voor de CISO en de aanwijzing van het calamiteitenteam als
  toetsend orgaan.
- Per gemeente de **registratie** bij het NCSC, met het logboek van wat is ingevuld en de mutaties.
- Per significant incident de **meldingen met tijdstempel** (T0, waarschuwing, melding, eindverslag) en de
  kennisgeving aan inwoners.
- Een **oefening** waarin de klok is doorlopen, bijvoorbeeld een incident op vrijdagavond.

## BIO 2.0

| Maatregel | Wat dit item daarvoor levert |
|---|---|
| 5.24 Plannen en voorbereiden van het beheer van informatiebeveiligingsincidenten | Rollen, mandaat en klok liggen vooraf vast |
| 5.26 Reageren op informatiebeveiligingsincidenten | De meldingsketen en de informatieplicht als onderdeel van de respons |
| 5.5 Contact met overheidsinstanties | Melding aan NCSC en RDI, registratie en contactpersonen |
| 5.31 Wettelijke, statutaire, regelgevende en contractuele eisen | De Cbw-plichten zijn vertaald in een procedure en een registratie |

## Zo leg je het uit

**Aan het college.** "Elke gemeente moet een ernstig cyberincident binnen 24 uur melden, ook in het weekend.
Wij doen dat voor u, maar alleen als u ons daarvoor mandateert. Zonder mandaat moet uw gemeente het zelf
regelen, op het moment dat de ICT eruit ligt."

**Aan de directie.** "De moeilijkste vraag is niet hoe je meldt, maar of iets meldplichtig is. Eén van de drie
drempels is of de schade binnen de begroting past. Dat oordeel moet iemand namens de organisatie kunnen geven,
binnen een dag. Wie is dat bij ons?"

**Aan IT-beheer.** "Leg een incident direct vast als het mogelijk groot is. Dat tijdstip is het begin van de
klok, niet het moment dat het calamiteitenteam bijeenkomt."
