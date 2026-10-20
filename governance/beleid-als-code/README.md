---
titel: Beleid als code, met een AI-agent die configuratie beheert onder menselijke goedkeuring
vakgebied: governance
type: aanpak
normen: [BIO2, Cbw, AVG, AI Act]
peildatum: 2026-10-20
herkomst: verkenning en pilotvoorstel van het team informatiebeveiliging en privacy van een regionale samenwerking van gemeenten (augustus 2026), voor de commons generiek gemaakt
status: concept
samenvatting: De klassieke keten van wet naar beleid naar configuratie faalt in de middelste laag, want beleidstekst heeft zelden het detail om een configuratie af te dwingen. Policy-as-code draait de pijl om: de configuratie in een repository is de bron van waarheid, en de leesbare beleidsteksten, beheerdocumenten en de bewijsmapping voor de auditor worden eruit gegenereerd, zodat configuratiebeheer en wijzigingsbeheer de beleidscyclus worden. Met een model van vier lagen, een indeling van de repository, zes spelregels voor agentic AI met systeemtoegang (alleen configuratie, eigen identiteit, plan en apply met menselijke goedkeuring), de volgorde privacy en medezeggenschap, en een pilot op een logplatform.
---

# Beleid als code, met een AI-agent die configuratie beheert onder menselijke goedkeuring

> **Lees de aanpak online:** [security-commons-nl.github.io/kennisbank/governance/beleid-als-code](https://security-commons-nl.github.io/kennisbank/governance/beleid-als-code/)

Een gemeente stelt informatiebeveiligingsbeleid vast, en daarna richt een beheerder de systemen in. Tussen die
twee zit een gat. Beleidstekst heeft bijna nooit het detail om een configuratie af te dwingen: welke logbron, welke
bewaartermijn, welke detectieregel, welke rol. Dus nemen beheerders die beslissingen zelf, ad hoc en
ongedocumenteerd, en het vastgestelde document drijft weg van de werkelijkheid. Bij de volgende audit klopt het
beleid niet meer met wat er draait.

Policy-as-code draait de richting om. **De configuratie is de norm**; de leesbare beleidsteksten worden eruit
gegenereerd, per doelgroep. Een document kan dan niet meer afwijken van de werkelijkheid, want het komt eruit.

De gereedschapskant krijgt een eigen plek in de repository
[policy-as-code](https://github.com/security-commons-nl/policy-as-code) van de commons. Dit stuk gaat over het
model en de governance eromheen.

## Het model in vier lagen

| Laag | Wat | Tempo | Wie stelt vast |
|---|---|---|---|
| 1 Norm | BIO 2.0, Cbw, AVG, DigiD, Suwinet; vertaald naar een machineleesbare lijst van maatregelen | extern gegeven | wetgever, normbeheerder |
| 2 Kader | informatiebeveiligingsbeleid, AI-beleid, definities van standaardwijzigingen; dun, in mensentaal | zelden | college (kader), directie en CAB (definities) |
| 3 Code | een repository per platform: configuratie, detectieregels, toegangsrollen, koppeling naar maatregelen | doorlopend, via de goedkeuring | proceseigenaar of CAB, per wijziging |
| 4 Weergaven | gegenereerde documenten per doelgroep, met versiestempel | volgt laag 3 automatisch | niemand; het is documentatie, geen besluit |

Een voorbeeld van een repository voor een logplatform:

```
logplatform/
  config/          configuratie, bewaartermijnen, verwerkingsstappen
  detections/      detectieregels, elk met een metadatakop
  access/          rollen en rechten
  mappings/        maatregel uit BIO 2.0 of Cbw <-> configuratie-onderdeel
  docs-generated/  gegenereerde weergaven; nooit met de hand bewerken
```

**Twee principes die het laten werken:**

1. **Metadata bij elke configuratie-eenheid:** doel, eigenaar, gedekte maatregel, classificatie. Dan genereer je
   geen technische opsomming maar beleid: "de gemeente detecteert verdachte inlogpogingen (maatregel 8.16); logs
   worden 90 dagen bewaard (verantwoording AVG)".
2. **De pijlrichting is heilig.** Documenten komen uit de code, nooit andersom. Beleid wijzigen is configuratie
   wijzigen via de goedkeuring, en daarna opnieuw genereren. Compliance wordt een test op de repository
   ("bewaartermijn ten minste 90 dagen") in plaats van een gesprek met de auditor.

**Drie weergaven**, elk gestempeld "gegenereerd uit versie X op datum Y": een tekst voor bestuur en medewerkers,
een beheerdersdocument, en een bewijsmapping voor de auditor (maatregel, configuratieregel, laatste wijziging, wie
keurde goed).

## Hoe een wijziging loopt

1. **De agent stelt voor (plan):** een configuratie, detectieregel of bewaartermijn, met een samenvatting van de impact.
2. **De mens beslist:** de proceseigenaar of het CAB keurt goed. Standaardwijzigingen zijn vooraf gedefinieerd.
3. **Apply:** de wijziging landt in de repository; versie en historie zijn de audittrail.
4. **Genereren:** de drie weergaven ontstaan opnieuw.

## Waar het al past in bestaand beleid

Je hebt meestal geen nieuw governancebouwwerk nodig. Zoek in het vastgestelde informatiebeveiligingsbeleid en het
AI-beleid naar deze haakjes:

- **Proceseigenaren keuren systeemwijzigingen goed die de beveiliging raken.** Dat is de formele basis voor de
  goedkeuringsstap.
- **Een uitzonderingsproces naar risico:** laag bij het IB-team, middel bij CISO en CIO, hoog bij de directie. Dat
  patroon is herbruikbaar voor de categorieën standaardwijziging.
- **Een mandaat voor monitoring en logbeheer** bij de manager IT-beheer. Daar hoort het platform formeel thuis.
- **In het AI-beleid:** een intake, een quickscan op risico, een AI-register en autorisatie van tools; een gelaagd
  model met een stabiel kader en flexibele uitwerkingen. Policy-as-code is daar de technische verlenging van.

Wat in AI-beleid vaak ontbreekt, is **de handelingskant**. Het regelt welke data een AI-systeem in mag en dat er een
mens tussen zit bij besluiten over mensen, maar niets over AI die zelf acties op systemen uitvoert. Voeg een
paragraaf "agentic AI met systeemtoegang" toe aan het uitvoeringsplan, met de spelregels hieronder.

## Zes spelregels voor een agent met systeemtoegang

1. **Nooit meer rechten dan de opdrachtgever.** Geen route naar privilege-escalatie.
2. **Een eigen identiteit**, geen persoonlijk account; elke actie wordt gelogd.
3. **Plan en apply gescheiden.** De agent stelt voor, een mens keurt goed, daarna pas uitvoeren. Dat is ook de
   beheersmaatregel tegen prompt injection.
4. **Alleen configuratiedata.** Geen log-inhoud, geen persoonsgegevens. Leg dat vast als classificatie in het
   AI-register.
5. **Geen gevoelige data naar externe modellen.** De tool doorloopt de autorisatie uit het AI-beleid.
6. **De omgeving van de agent is een beheerwerkplek:** gehard, gescheiden, gelogd. De logs van de agent erven de
   classificatie van het gevoeligste systeem dat hij raakt.

Zie voor de bevoegdheid van een agent ook [Wiens bevoegdheid gebruikt een AI-agent?](../../security/agent-bevoegdheid/)
en voor de werkplek [Beheerwerkplek voor administratieve taken](../../security/beheerwerkplek/).

## De volgorde: privacy en medezeggenschap eerst

Analyse op logs van medewerkers kan een personeelsvolgsysteem zijn (instemming van de ondernemingsraad onder de
WOR, artikel 27; bij een samenwerking meerdere OR's) en staat op de lijst van verwerkingen waarvoor de Autoriteit
Persoonsgegevens een DPIA verplicht stelt. Ook als een externe SOC dezelfde data al verwerkt: een eigen kopie heeft
een eigen doel, bewaartermijn en toegangsregeling nodig. Bouwen op synthetische data mag dus meteen; echte bronnen
pas na DPIA en OR.

## Een pilot op een logplatform

Een eigen logplatform dat nog niet in productie is, is een bijna ideaal proefterrein: geen proces dat kan omvallen,
geen leverancier in de weg, geen gat in de detectie.

| Keuze | Waarom |
|---|---|
| Doel: eigen analyse en hunting naast het SOC; policy-as-code als bewezen bijvangst | het platform moet ook zonder het experiment iets opleveren |
| De agent beheert alleen configuratie, nooit log-inhoud | geen gevoelige data naar modellen, minimaal oppervlak voor prompt injection, lokale AI wordt fase 2 in plaats van voorwaarde |
| IB&P trekt de pilot tijdelijk; bij de eerste productiebron gaat het eigenaarschap naar IT-beheer | de CISO blijft zuiver in de toetsende rol (drie lijnen) |
| Bronnen in volgorde: infrastructuur en synthetische data eerst; identiteitslogs na DPIA en OR; telemetrie van de werkplekbeveiliging na afstemming met het SOC; Wpg-bronnen buiten scope | wat het minst gevoelig is, eerst |
| Demo en wijzigingsvoorstel tegelijk: bouwen op synthetische data terwijl de kaderwijziging bij het CAB ligt | laten zien en regelen lopen parallel |

**Fasering:** (1) demo op synthetische data en kaderwijziging bij het CAB; (2) autorisatie van de tool; (3) echte
bronnen, infrastructuur eerst, na DPIA en OR; (4) lokale AI voor analyse, en het patroon verbreden naar
apparaatbeheer, cloudbeleid en firewalls.

## Bewijs

- De **repository** met configuratie, metadata per eenheid en de koppeling naar maatregelen.
- De **wijzigingshistorie** met per wijziging het voorstel, de goedkeuring en wie goedkeurde.
- De **gegenereerde weergaven** met versiestempel, waaronder de bewijsmapping voor de auditor.
- **Tests op de repository** die de naleving van normregels bewaken.
- De **registratie van de agent** in het AI-register, met classificatie, en de DPIA en het OR-besluit vóór echte bronnen.

## BIO 2.0

| Maatregel | Wat deze aanpak daarvoor levert |
|---|---|
| 8.9 Configuratiebeheer | De configuratie staat versiebeheerd in een repository, met eigenaar en metadata |
| 8.32 Wijzigingsbeheer | Plan, goedkeuring en apply; de historie is de audittrail |
| 5.36 Naleving van beleid, regels en normen voor informatiebeveiliging | Naleving als test op de repository, en de bewijsmapping |
| 8.15 Logging | Het logplatform zelf, en de logging van elke actie van de agent |
| 8.2 Speciale toegangsrechten | Een eigen identiteit voor de agent, nooit meer rechten dan de opdrachtgever |

## Zo leg je het uit

**Aan de directie.** "Nu schrijven we beleid, en daarna richt iemand de systemen in zoals hij denkt dat het bedoeld
is. Straks is de inrichting het beleid, en het document dat u leest komt daaruit. Het kan niet meer afwijken."

**Aan de ondernemingsraad.** "De agent kijkt niet naar wat medewerkers doen. Hij beheert alleen de instellingen.
Logs met gegevens van medewerkers komen pas aan bod na een DPIA en uw instemming."

**Aan IT-beheer.** "De agent doet voorstellen, jullie of het CAB beslissen. Niets gaat live zonder goedkeuring, en
elke wijziging staat met naam en datum in de historie."
