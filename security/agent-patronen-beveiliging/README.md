---
titel: Verdediging met AI, vijf agent-patronen voor beveiligingswerk
vakgebied: security
type: aanpak
normen: [BIO2, AI Act, Cbw]
versie: 2026-11
herkomst: CISO-praktijk bij gemeenten, naar aanleiding van een VNG-webinar over de beveiliging van AI
status: concept
route: geen
bronnen: [ibd-handreiking-ai-en-algoritmen, vng-kenniskaart-monitoring-ai, vng-utrecht-aansluitvoorwaarden-ai, bzk-algoritmekader]
samenvatting: Vijf patronen waarin een AI-agent het beveiligingswerk voorbereidt en een mens beslist - de toets-agent, de risico-voorbereider, de voorschriften-navigator, de monitoring-agent en de leveranciersantwoord-toetser. Per patroon wat de agent doet, wat de mens doet, welke bevoegdheid de agent krijgt en wat het bewijs is, plus het antwoord op de vraag wie de agent keurt. Met een startlijst van use-cases waar organisaties op kunnen aanvullen.
---

# Verdediging met AI, vijf agent-patronen voor beveiligingswerk

> **Lees de aanpak online:** [security-commons-nl.github.io/kennisbank/security/agent-patronen-beveiliging](https://security-commons-nl.github.io/kennisbank/security/agent-patronen-beveiliging/)

Over AI en beveiliging bestaan vier gesprekken: de aanval *op* AI, de aanval *met* AI, de verdediging *van*
AI en de verdediging *met* AI. De meeste stukken, ook in deze kennisbank, gaan over de verdediging van AI:
hoe je een assistent of agent veilig inzet. Over het vierde gesprek, AI als hulp in het eigen
beveiligingswerk, is in de publieke sector weinig uitgeschreven. Tegelijk heeft een CISO-organisatie bij
een gemeente meer werk dan mensen, en veel van dat werk is lezen, vergelijken en samenvatten: precies wat
een agent goed kan.

Dit stuk beschrijft vijf patronen. Elk patroon is een taakverdeling: de agent bereidt voor, de mens
beslist. Dat is geen voorzichtigheid voor de vorm. Het is de enige verdeling waarin je achteraf kunt
uitleggen wie wat besloot, en de enige die past bij menselijk toezicht zoals de AI-verordening dat vraagt.

## De vijf patronen

| Patroon | Wat de agent doet | Wat de mens doet |
|---|---|---|
| **Toets-agent** | Toetst code of configuratie van een leverancier aan een vaste lijst maatregelen, rapporteert per maatregel en stelt een correctie voor | Stelt de lijst vast, bespreekt de uitkomst met de leverancier, beslist |
| **Risico-voorbereider** | Stelt voor een beschreven toepassing kandidaat-risico's voor uit openbare lijsten, met per risico de bron | Weegt, schrapt, vult aan, en neemt het besluit in het risicoregister |
| **Voorschriften-navigator** | Loopt stap voor stap de vragen van Cbw, AVG en AI-verordening langs en noemt per stap de bron | Beantwoordt de vragen; de uitkomst is een classificatie met onderbouwing |
| **Monitoring-agent** | Leest logging en markeert afwijkingen tegen een vaste lijst signalen | Beoordeelt elke markering en past de lijst aan |
| **Leveranciersantwoord-toetser** | Legt de antwoorden van een leverancier naast de gestelde eis en markeert waar een antwoord de vraag ontwijkt | Voert het gesprek met de leverancier |

### Toets-agent

Twee grote gemeenten lieten in een openbaar VNG-webinar een proefopstelling zien waarin een open-source
agent de code van een leverancier naloopt op bekende risico's en mitigerende maatregelen, rapporteert en
correcte code voorstelt, met een mens aan het begin en aan het eind. Dat is dit patroon.

- **Bevoegdheid:** alleen lezen op de aangeleverde code of configuratie, in een afgeschermde omgeving.
  Geen toegang tot productie, geen schrijfrechten in de repository van de leverancier.
- **Laag:** de toepassing zelf (code, configuratie), vóór ingebruikname of bij een release.
- **Bewijs:** de lijst maatregelen waartegen getoetst is, met versie; het rapport per maatregel; het
  besluit van de mens met de afspraken met de leverancier.
- **Let op:** de lijst bepaalt de uitkomst. Een agent die "geen bevindingen" meldt op een te korte lijst,
  geeft schijnzekerheid. Gebruik een openbare lijst als basis, zoals de
  [OWASP Top 10 voor LLM-toepassingen](https://genai.owasp.org/llm-top-10/) of de aansluitvoorwaarden voor
  algoritmen en AI (zie de bronnen), en vul aan met je eigen eisen.

### Risico-voorbereider

Een risicoanalyse begint met een leeg vel, en het lege vel is de grootste drempel. De agent vult het met
kandidaat-risico's uit openbare lijsten (OWASP, [MITRE ATLAS](https://atlas.mitre.org/), de
aansluitvoorwaarden), afgestemd op de beschreven toepassing, met bij elk risico de bron.

- **Bevoegdheid:** geen toegang tot systemen; werkt op een beschrijving die de mens aanlevert.
- **Laag:** de business en de toepassing, vóór de bouw of de inkoop.
- **Bewijs:** de voorgestelde lijst, de lijst na weging, en per geschrapt risico waarom.
- **Let op:** de agent kent de context niet. Wat hij niet voorstelt, is daarmee niet afwezig. Gebruik de
  uitkomst als start van het gesprek met de proceseigenaar, niet als de analyse zelf; zie
  [Risicoanalyse langs aanvalspaden](../risicoanalyse-aanvalspaden/).

### Voorschriften-navigator

Valt deze toepassing onder hoog risico, ben je aanbieder of gebruiksverantwoordelijke, raakt het de
Cbw? De navigator stelt de vragen in vaste volgorde en noemt bij elke stap het artikel of de bron. Het is
dezelfde logica als de [aanbieder-toets](../../governance/aanbieder-onder-de-ai-act/) en het
[Algoritmekader](https://minbzk.github.io/Algoritmekader/), maar als gesprek in plaats van een formulier.

- **Bevoegdheid:** geen toegang tot systemen; werkt op de antwoorden van de mens.
- **Bewijs:** de vragen, de antwoorden en de uitkomst, met per stap de bron.
- **Let op:** een navigator die de wet samenvat in plaats van de vragen te stellen, gaat interpreteren. De
  vragen en de beslisregels komen uit een vaste bron; de agent leest voor en noteert.

### Monitoring-agent

Logging over AI-gebruik is volumineus en de signalen zijn nieuw: een connector die er gisteren niet was,
een agent die buiten zijn taak gegevens opvraagt, uitvoer die naar buiten gaat, een model dat de
leverancier zonder aankondiging wisselt. De monitoring-agent leest mee en markeert.

- **Bevoegdheid:** alleen lezen op de logging; geen rechten om iets uit te zetten.
- **Laag:** platform en orchestratie, doorlopend.
- **Bewijs:** de lijst signalen met versie, de markeringen en per markering het oordeel van de mens.
- **Let op:** de markeringen landen in de werkvoorraad van je SOC of
  [centrale logverzameling](../centrale-logverzameling/), niet in een apart scherm dat niemand opent. Een
  monitoring-agent mag nooit zelf blokkeren; dat is een ingreep en die beslist een mens, zie
  [Ingrijpen met een checklist](../ingrijpen-met-checklist/).

### Leveranciersantwoord-toetser

Een leverancier beantwoordt een vragenlijst, de annex of de aansluitvoorwaarden. Veel antwoorden zijn
waar en toch geen antwoord: "wij volgen de best practices", "dat is geregeld in ons beleid". De agent legt
elk antwoord naast de gestelde eis en markeert waar het antwoord de vraag ontwijkt, niet concreet is of
naar een document verwijst dat niet is meegestuurd.

- **Bevoegdheid:** geen toegang tot systemen; werkt op de eis en het antwoord.
- **Bewijs:** de eisen, de antwoorden, de markeringen en de vervolgvragen die de mens heeft gesteld.
- **Let op:** antwoorden van een leverancier kunnen vertrouwelijk zijn. Kies een agent die je
  inkoopvoorwaarden toestaan, of anonimiseer eerst; zie het
  [keuzeblad bij de inzet van een agent](../ai-inzet-keuzeblad/). Hoort bij
  [Leveranciersbeoordeling met vaste cyclus](../leveranciersbeoordeling/).

## Wie keurt de agent

In het webinar viel de vraag of dit niet de slager is die zijn eigen vlees keurt. Het antwoord is
hetzelfde als bij een pentester en een bouwer: scheiding.

1. **Een ander model of een andere aanbieder** dan wat getoetst wordt. Een agent die code toetst die met
   hetzelfde model is geschreven, deelt de blinde vlekken.
2. **Alleen leesrechten** waar dat kan. Elk patroon hierboven werkt zonder schrijfrechten.
3. **De mens beslist** op de uitkomst, met naam in het verslag.
4. **Een steekproef met de hand**, periodiek: neem een uitkomst en doe hem zelf over. Wijkt het af, dan is
   dat een bevinding over de agent.
5. **De lijsten zijn data met een versie**: de maatregelen, de signalen, de eisen. Wie de lijst wijzigt,
   wijzigt de uitkomst; dus de lijst heeft een eigenaar.

## Use-cases, een startlijst

Dit is een begin. De lijst groeit met wat organisaties zelf in gebruik hebben of willen proberen.

| Doel | Patroon | Laag | Wat er in gaat | Status |
|---|---|---|---|---|
| Code van een leverancier toetsen vóór ingebruikname | Toets-agent | Toepassing | Code, configuratie | proef |
| Kandidaat-risico's voor een nieuwe AI-toepassing | Risico-voorbereider | Business, toepassing | Beschrijving van de toepassing | idee |
| Classificatie onder AI-verordening en Cbw | Voorschriften-navigator | Business | Antwoorden op vaste vragen | idee |
| Nieuwe connectoren en agents in de tenant signaleren | Monitoring-agent | Platform | Auditlogging | idee |
| Antwoorden op de security-annex beoordelen | Leveranciersantwoord-toetser | Inkoop | Eisen en antwoorden | idee |
| Configuratie van cloud-beheerportalen naast een baseline leggen | Toets-agent | Platform | Configuratie-export | idee |

Heb je een use-case in gebruik of in proef, of zoek je er een? Een
[issue in de kennisbank](https://github.com/security-commons-nl/kennisbank/issues/new) is genoeg, met het
doel, het patroon en wat er in gaat. Wat erbij komt, landt in deze tabel; wat uitgroeit tot een eigen
aanpak, krijgt een eigen stuk. Beschrijf de use-case, niet de situatie van je organisatie.

## Wat het kost en wat het oplevert

Kosten: laag tot middel. De patronen draaien op een assistent die je al hebt of op een open model; het
werk zit in de lijsten (maatregelen, signalen, eisen) en in de afspraak wie beslist. Wat het oplevert:
tijd op lees- en vergelijkwerk, en een vaste vorm waarin je uitkomsten kunt laten zien. Wat het niet
oplevert: een oordeel. Elke tijdwinst die verdwijnt in het nalopen van de agent, is een signaal dat het
patroon niet past; weeg dat mee op het keuzeblad.

## Hoe dit samenhangt

Vóór de inzet van elk patroon: het [keuzeblad](../ai-inzet-keuzeblad/). De bevoegdheid van de agent:
[Wiens bevoegdheid gebruikt een AI-agent?](../agent-bevoegdheid/). Als de agent op een assistent in de
kantooromgeving draait: [Copilot, de configuratiekeuzes](../copilot-configuratiekeuzes/). De risico's van
agents zelf staan in de [OWASP Top 10 voor agentic applications](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/);
voor een breder kader het [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework).

## Licentie

[EUPL-1.2](../../LICENSE).
