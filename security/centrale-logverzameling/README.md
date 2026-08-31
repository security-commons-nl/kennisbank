---
titel: Richt centrale logverzameling in
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Logs van systemen, applicaties en netwerk centraal verzamelen en bewaren, zodat je bij een incident zicht en bewijs hebt. Dit is de fundering onder elke vorm van detectie: zonder logverzameling valt er niets te monitoren, hoe je de opvolging ook organiseert. Met de stappen, het bewijs dat je aan het eind kunt laten zien, en een vergelijking van de vier routes waaruit je daarna kiest.
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

## Kiezen tussen de routes

Logverzameling heb je in elke vorm nodig. Wat je erop bouwt is een keuze uit vier routes die elkaar
uitsluiten: je organiseert de opvolging op een van deze manieren, niet op meer tegelijk. Wat elke route
van je vraagt en oplevert staat in het eigen stuk; hieronder staat waarin ze verschillen, zodat je niet
vier pagina's naast elkaar hoeft te leggen.

| Route | Wie draait de dienst | Wat je zelf in huis moet hebben | Waar de regie ligt | Wanneer dit de logische keuze is |
|---|---|---|---|---|
| [Co-managed SIEM](../co-managed-siem/) | jij, met een leverancier ernaast | eigen analisten, geheel of deels | volledig bij jou; eigen data en detectieregels | middelgroot tot groot, en je wilt eigen detectievermogen opbouwen |
| [Uitbestede SOC](../uitbestede-soc/) | een externe partij | opdrachtgeverschap en opvolging van meldingen | bij de leverancier; jij stuurt op afspraken | geen eigen SOC te bouwen, en detectie moet snel geregeld zijn |
| [MDR-dienst](../mdr-dienst/) | een externe partij, die ook ingrijpt | een mandaat dat je durft weg te geven | bij de leverancier, inclusief handelen | snelle actieve respons nodig; de duurste van de vier |
| [Regionaal of gedeeld SOC](../regionaal-soc/) | jullie samen | bestuurlijke bereidheid om governance te delen | gedeeld en publiek | klein tot middelgroot, en er is al een samenwerkingsverband |

Twee dingen die de keuze in de praktijk bepalen. Ten eerste: een SIEM zonder mensen die hem bedienen en
tunen levert vooral ruis op, en die ruis kost meer dan hij oplevert. Ten tweede: bij een regionaal SOC is
de techniek zelden het probleem, maar het delen van governance wel.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `soc` uit de
[zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/) en is daarvan de
**fundering**. Welke vorm je erop bouwt is een keuze; zie [Kiezen tussen de routes](#kiezen-tussen-de-routes)
hierboven.

Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op
[Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

## Licentie

[EUPL-1.2](../../LICENSE).
