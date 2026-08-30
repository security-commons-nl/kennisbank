---
titel: Web en API testen in de ontwikkelketen
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Beveiliging van webapplicaties en API-koppelingen testen in de ontwikkelketen, met scanning op afhankelijkheden erbij, zodat kwetsbaarheden worden gevonden voordat ze live staan. Met de plek in de pijplijn, wat blokkerend is voor livegang, en het bewijs van herstel.
barrieres: [webtest]
rol: fundering
---

# Web en API testen in de ontwikkelketen

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/web-en-api-testen](https://security-commons-nl.github.io/kennisbank/security/web-en-api-testen/)

> **Barriere:** test web/API-beveiliging en herstel kwetsbaarheden. Veiligheid is in elke fase van softwareontwikkeling ingebed, niet als pen-test aan het einde, maar als ontwerp-, code- en review-discipline doorheen.

Beveiliging wordt pas in productie gemerkt, door incidenten of pentests. Wijzigingen die toen al eenvoudig waren in ontwerp, kosten in productie ordes meer. En kwetsbaarheden lekken in via voor-de-hand-liggende fouten die in review opgevangen hadden kunnen worden.

## Wanneer wel, wanneer niet

Past in organisaties die zelf ontwikkelen of substantieel aanpassen. Wanneer niet: voor pure inkooporganisaties, daar verschuift de eis naar leveranciers (Annex).

## Zo richt je het in

Threat modelling bij ontwerp; secure coding-richtlijnen; code review met security-bril; SAST/DAST in de pipeline; security-acceptatiecriteria in user stories; pen-test vóór productie. Geen losse tools, maar één doorlopend ritme.

1. Stel secure-coding-richtlijnen vast voor de gebruikte talen en frameworks.
2. Voeg threat modelling toe aan het ontwerpproces voor nieuwe componenten.
3. Integreer SAST in de CI/CD-pipeline; faal builds bij hoge-severity-bevindingen.
4. Maak peer-review met security-checklist verplicht voor merges naar main.
5. Plan periodieke pentest voor major releases.
6. Train ontwikkelaars in de actuele aanvalsklassen (OWASP Top 10, supply chain).

## Wat het kost en wat het oplevert

Kosten: midden.

**Wat het oplevert**

- Kwetsbaarheden worden opgevangen in goedkope fases (ontwerp/code), niet pas in productie.
- Sluit aan op de Cyber Resilience Act en NIS2-eisen voor veilig ontwikkelen.
- Bouwt security-cultuur op in plaats van een afzonderlijke gate.

**Waar je op moet letten**

- Investering in cultuur, niet in een tool, vraagt langere adem.
- Pipelines bouwen of aanpassen kost tijd; rust en commitment nodig.
- Strakke security-acceptatiecriteria botsen met snelle releases, onderhandelen onvermijdelijk.

## Bewijs

- De testresultaten per applicatie, met de datum en de gebruikte methode.
- Welke bevindingen blokkerend zijn voor livegang, en wat er gebeurt als ze toch doorgaan.
- De scanning op afhankelijkheden: welke bibliotheken zijn kwetsbaar, en wat is de doorlooptijd tot een update.
- Het herstel van eerdere bevindingen, aantoonbaar in een volgende test.

## Zo leg je het uit

**Aan de directie.** Bugs die we pas in productie zien zijn duur. SSDLC bouwt veiligheid in van ontwerp tot oplevering, beter werk, minder herstel, betere aansluiting op CRA en NIS2.

**Aan de informatiemanager.** Inpassing in de bestaande CI/CD-pipelines en in het ontwerpproces. Tooling-keuze is een eigen traject.

**Aan het MT.** Ontwikkelaars en architecten krijgen extra discipline; pipelines worden uitgebreid. Reken op cultuurinvestering, niet alleen toolkeuze.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `webtest` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

De brede periodieke test staat in [Periodiek pentesten](../periodiek-pentesten/); deze handleiding gaat over de doorlopende variant in de keten.

## Licentie

[EUPL-1.2](../../LICENSE).
