---
titel: Netwerk en firewall analyseren uit data
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: gegeneraliseerd uit een casus bij een gemeentelijke organisatie
status: in gebruik
samenvatting: Vertrouw niet op de netwerktekening maar op de configuratie en het verkeer. Stel uit hit-counts, routeringstabellen en flow-logs vast welke regels te breed staan, of oost-west-verkeer werkelijk langs de firewall gaat en of beheertoegang beperkt is. Met de werkwijze om brede regels veilig te versmallen via schaduwregels, en het bewijs dat je aan het eind kunt laten zien.
barrieres: [segment]
rol: verdieping
pijler: meten-voordat-je-ingrijpt
---

# Netwerk en firewall analyseren uit data

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/netwerkanalyse-uit-data](https://security-commons-nl.github.io/kennisbank/security/netwerkanalyse-uit-data/)

> **Barriere:** beperk lateral movement met segmentatie en minimale rechten. Deze handleiding gaat over
> het vaststellen of dat werkelijk zo is, uit de configuratie en het verkeer in plaats van uit de tekening.

Het kernprincipe: **vertrouw niet op de tekening, maar op de configuratie en het verkeer.** Een
netwerkdiagram toont de bedoeling. Of het netwerk werkelijk segmenteert, of beheertoegang werkelijk
beperkt is, en welke regels werkelijk gebruikt worden, blijkt uit de data, niet uit het plaatje.

Dit is defensieve configuratie-analyse: je zoekt naar te brede toegang, ontbrekend zicht en ontbrekende
beperking, om die te verkleinen. De aanpak is vendor-neutraal; voorbeelden zijn indicatief.

## Wanneer wel, wanneer niet

Doe dit zodra er segmentatie op papier staat en je wilt weten of hij ook echt geldt. Wanneer niet als
eerste stap: zonder een vastgesteld segmentatiebeleid weet je niet waar je de meting tegen afzet. Begin
dan bij [Netwerksegmentatie](../netwerksegmentatie/).

## Wat je exporteert en analyseert

### 1. Regels op feitelijk gebruik (hit-counts)

Exporteer de regelset met **hit-counters** en, indien beschikbaar, applicatie-identificatie
(bijvoorbeeld App-ID of Apps-Seen). Doel: vind brede of "any"-achtige regels en rangschik ze op gebruik.

- Zoek naar regels met zeer hoge hit-counts en brede bron, bestemming of poort. Een full-access- of
  any-any-regel is een klassiek voorbeeld en is bijna altijd te breed ontworpen.
- Indicatief: Palo Alto `show rule-hit-count` en traffic-logs met App-ID; Cisco `show access-list` met
  hit-counts, en NetFlow of IPFIX voor het werkelijke verkeer.

### 2. Werkplek naar datacenter: beweegt verkeer langs de firewall?

Toets of oost-west-verkeer daadwerkelijk **langs** de firewall gaat, of er onderling omheen beweegt.
Oost-west is verkeer binnen je eigen netwerk, bijvoorbeeld tussen onderdelen in het datacenter of tussen
locaties. Vergelijk de **routeringstabellen** en de flow- en sessielogs met de bedoelde segmentatie.
Verkeer dat niet langs de firewall komt, kan de firewall niet zien of tegenhouden; dat is het pad
waarover lateral movement na een besmetting verloopt.

Is **Citrix nog in gebruik**, kijk dan of die omgeving in het datacenter als onvertrouwde securityzone is
ingericht. In de praktijk blijkt zo'n omgeving vaak directe toegang tot applicatieservers te hebben, en
dat is een groot risico.

> Een kantoor- of Citrix-omgeving die niet met een firewall van de servers is gescheiden, is een rode
> vlag. Let ook op de laag waarop die scheiding staat: alleen een **L4**-firewall (poort en protocol) in
> plaats van **L7** (applicatie en identiteit) is eveneens een risico. Toets dit; ga niet uit van "het is
> gescheiden".

### 3. Beheertoegang tot firewall en core

- **MFA op beheeraccounts.** Tel de beheeraccounts en controleer of ze allemaal een koppeling met MFA,
  SAML of RADIUS hebben. Het komt voor dat alle beheeraccounts zonder MFA werken; dat is een directe en
  eenvoudig te dichten bevinding. MFA kan ook met persoonlijke certificaten: netwerkapparatuur werkt
  daarmee, en je wilt daar geen afhankelijkheid van een authenticator-app.
- **Out-of-band beheer.** Loopt beheer van firewall en core-interfaces via een apart beheernetwerk, of
  via het productienetwerk? Kun je vanaf een gewone werkplek direct bij de firewall, dan is dat een groot
  probleem. Dat is niet alleen techniek maar vooral werkwijze bij de beheerders.
- **Superuser- en break-glass-accounts**, vier ogen op regelwijzigingen, en een audit-log naar een
  onafhankelijke bestemming.

### 4. Zicht op versleuteld verkeer

Staat er **TLS-decryptie of IPS** op het uitgaande werkplek- en serververkeer? Zonder decryptie blijft
veel moderne malware- en C2-verkeer onzichtbaar, want dat gaat versleuteld over 443. Overleg waar nodig
met de privacyafdeling hoe je dit inzet, want er wordt geautomatiseerd in de data gekeken. Onderbouw het
met een DPIA waarin vooral het doel duidelijk is: geen controle op de inhoud, maar bescherming van onder
meer persoonsgegevens tegen cyberaanvallen. De Autoriteit Persoonsgegevens heeft hier meerdere opinies
over gepubliceerd.

### 5. Core-routers en switches, vaak een blinde vlek

Deze laag blijft in analyses vaak op "te bevestigen" staan. Toets actief:

- firmware- en OS-versies en bekende kwetsbaarheden van switch en router;
- of de beheernetwerken bereikbaar zijn vanuit de werkpleknetwerken;
- poortbeveiliging en technieken zoals **802.1X**, en of de routering verkeer langs de firewall dwingt.

### 6. Egress-hygiene richting derden

Brede uitgaande regels naar keten- en leveranciersnetwerken. Het eigen risico is vaak laag, maar het is
slordig ontwerp. Versmal ze in eigen tempo, in dialoog met de ketenpartners.

### 7. Onbeheerde paden

Let op werkplekken en op VPN- of externe toegangsroutes die wel routering naar het datacenter kennen maar
niet in beheer zijn. Stel de bewegingsvrijheid vast met een gerichte scan vanaf zo'n apparaat; neem het
niet aan. Zorg dat een leverancier voor regulier beheer **altijd** via een PAM-oplossing werkt. Accepteer
**nooit** directe RDP via een eigen VPN zonder restricties.

## Hoe je brede regels veilig versmalt

Hetzelfde principe als bij de werkplek: **meet voordat je ingrijpt.** Zet brede regels niet blind dicht.

1. Lees per brede regel uit wat er werkelijk overheen gaat (App-ID of Apps-Seen, flow-logs).
2. Bouw **schaduwregels** naast de brede regel: specifieker, en alleen loggend.
3. Monitor of de schaduwregels het verkeer dekken.
4. Knijp daarna pas de brede regel dicht, met een terugrolplan en in een onderhoudsvenster.

Houd het **break-risk** per wijziging expliciet. Brede regels waar productie overheen rijdt, hebben een
hoog break-risk; maatregelen op beheer en zicht (MFA op beheer, het besluit over decryptie) zijn meestal
onafhankelijk door te voeren met laag risico.

## Volgorde

1. **Nu, laag risico:** MFA of passkey op alle beheeraccounts, out-of-band beheer, en een besluit over
   TLS-decryptie.
2. **Nu, hoog break-risk, datagedreven:** brede en any-regels versmallen via meten en schaduwregels.
3. **Parallel:** de core- en switchlaag in beeld brengen (firmware, beheer-VLAN, 802.1X).
4. **Langere termijn:** segmentatiebeleid vaststellen, en L7 tussen de meest kritische segmenten.

## Bewijs

- De regelexport met hit-counts, met de brede regels gemarkeerd en gerangschikt op gebruik.
- De routeringstabel naast de bedoelde segmentatie, met de plekken waar oost-west-verkeer de firewall
  omzeilt.
- Een overzicht van de beheeraccounts op firewall en core met per account of er MFA op staat, en of
  beheer via een apart netwerk loopt.
- De lijst versmalde regels met de datum, de schaduwregel die eraan voorafging, en wat er is teruggerold.
- Het besluit over TLS-decryptie met de onderbouwing, en de DPIA als het is ingevoerd.

## Zo leg je het uit

De netwerktekening is de bedoeling, niet de werkelijkheid. Deze analyse zegt wat er feitelijk gebeurt:
welke regels echt gebruikt worden, of verkeer werkelijk langs de firewall komt, en wie er bij de firewall
kan. Vrijwel altijd blijkt een deel van de segmentatie op papier te bestaan en in de praktijk niet. Dat
is geen verwijt aan beheer; het is de optelsom van jaren aan uitzonderingen die niemand heeft opgeruimd.

Voor bestuur is de kern: we knijpen niet blind dicht, want dan breken we werk. We meten eerst wat er
overheen gaat, bouwen een specifiekere regel ernaast, en pas als die het verkeer dekt gaat de brede regel
dicht. Dat kost meer tijd en levert een uitrol op die niemand merkt.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `segment` uit de
[zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in
BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op
[Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

De fundering onder deze barriere is [Netwerksegmentatie](../netwerksegmentatie/): daar staat hoe je de
zones bepaalt en afdwingt. [Microsegmentatie](../microsegmentatie/) trekt dat door tot op werklastniveau.
Deze handleiding gaat over de vraag die daaraan voorafgaat en erop volgt: klopt wat we denken dat er
staat? De methode erachter staat in [Meten voordat je ingrijpt](../meten-voordat-je-ingrijpt/).

## Licentie

[EUPL-1.2](../../LICENSE).
