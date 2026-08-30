---
titel: Richt centrale logverzameling in
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Logs van systemen, applicaties en netwerk centraal verzamelen en bewaren, met kloksynchronisatie zodat tijdlijnen over bronnen heen kloppen. Dit is de fundering onder elke vorm van detectie en onder 24/7 opvolging: zonder verzamelde logs is er niets om op te triageren. Met de zeven stappen, de retentievraag en het bewijs dat een auditor wil zien.
barrieres: [soc]
rol: fundering
---

# Richt centrale logverzameling in

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/centrale-logverzameling](https://security-commons-nl.github.io/kennisbank/security/centrale-logverzameling/)

> **Barriere:** borg 24/7 opvolging en escalatie van kritieke meldingen. Dit is de eerste stap: zonder
> centraal verzamelde logs is er niets om op te melden, laat staan om binnen een afgesproken tijd op te
> volgen.

Logs staan vaak verspreid over servers, applicaties en netwerkapparatuur. Ze worden lokaal en kort
bewaard, of overschreven. Bij een incident valt er dan weinig te reconstrueren: je weet niet wat er
gebeurd is, wanneer, of via welke weg.

## Wanneer wel, wanneer niet

Altijd zinvol. Centrale logverzameling is de randvoorwaarde voor elke manier waarop je detectie
organiseert, of je die nu zelf doet, samen met een leverancier, of helemaal uitbesteedt.

Wanneer niet: als losse stap zonder vervolg. Logs verzamelen en er daarna niets mee doen levert een
datakerkhof op, opslagkosten zonder zicht. Plan dus meteen wat de volgende stap wordt, ook als die er pas
over een half jaar komt.

## Zo richt je het in

Logbronnen sturen hun gebeurtenissen via forwarders of agents naar een centrale opslag. Daar worden ze
genormaliseerd naar een gemeenschappelijk formaat en volgens een vaste retentietermijn bewaard.
Kloksynchronisatie via NTP zorgt dat tijdlijnen over bronnen heen kloppen; zonder dat kun je een aanval
niet reconstrueren, ook al heb je alle logs.

1. Inventariseer de logbronnen: servers, endpoints, netwerkapparatuur, vakapplicaties en clouddiensten.
2. Bepaal de retentietermijn per brontype, mede op basis van de AVG en de reconstructiebehoefte.
3. Kies een centrale opslag. Een open-source log-store volstaat voor deze stap.
4. Richt forwarders of agents in op de logbronnen.
5. Standaardiseer de tijd met NTP, zodat tijdstempels onderling vergelijkbaar zijn.
6. Test of een incident te reconstrueren valt uit de verzamelde logs. Doe dat met een echt scenario, niet
   met een steekproef op een enkele regel.
7. Beleg het beheer: wie bewaakt aansluitingen, retentie en opslaggroei.

## Wat het kost en wat het oplevert

De drempel is laag; dit is te starten zonder groot project, en leverancier-onafhankelijk.

**Wat het oplevert**

- De randvoorwaarde voor elke vorm van detectie.
- Bewijsmateriaal en reconstructie bij incidenten.

**Waar je op moet letten**

- Logopslag bevat gevoelige gegevens en moet zelf goed beveiligd worden.
- Zonder analyselaag levert het nog geen detectie op; dat is de volgende stap.
- Opslagkosten groeien mee met het aantal bronnen en de retentietermijn.

## Bewijs

- Een overzicht van aangesloten logbronnen tegenover de volledige lijst systemen, zodat de dekking
  zichtbaar is en niet alleen het aantal.
- De retentietermijn per brontype, met de onderbouwing vanuit de AVG en de reconstructiebehoefte.
- Het verslag van de reconstructietest: welk scenario, welke bronnen, en of de tijdlijn klopte.
- De NTP-configuratie, want zonder gelijkgezette klokken is een tijdlijn over bronnen heen niet hard te
  maken.

## Zo leg je het uit

**Aan de directie.** Zonder centrale logverzameling is er bij een incident geen zicht en geen bewijs van
wat er gebeurd is. De investering is beperkt en vormt de basis voor elke verdere stap in detectie.

**Aan de informatiemanager.** Centrale logverzameling raakt elk systeem dat logs levert. Het
standaardiseren van logbronnen en formaten loont, juist met het oog op de vervolgstappen.

**Aan het MT.** De lijnteams moeten hun logbronnen aanleveren en aangesloten houden. Dat is een
terugkerende beheertaak, geen eenmalige actie.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `soc` uit de
[zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/) en is daarvan de
**fundering**. Wat je erop bouwt is een keuze; er zijn vier manieren om de opvolging te organiseren:

- [Co-managed SIEM](../co-managed-siem/), regie zelf houden met een leverancier ernaast
- [Uitbestede SOC](../uitbestede-soc/), de dienst volledig bij een externe partij
- [MDR-dienst](../mdr-dienst/), detectie en response als dienst, inclusief ingrijpen
- [Regionaal of gedeeld SOC](../regionaal-soc/), samen met andere organisaties

Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op
[Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

## Licentie

[EUPL-1.2](../../LICENSE).
