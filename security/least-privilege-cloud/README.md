---
titel: Rechten in de cloud terugbrengen tot gebruik
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Rechten in cloudomgevingen terugbrengen tot wat werkelijk gebruikt wordt, op basis van gemeten gebruik in plaats van aanname. Verdieping op het beheersen van toegang tot cloudportalen. Met de meetmethode, de uitfasering en het bewijs dat overtollige rechten weg zijn.
barrieres: [consent]
rol: verdieping
---

# Rechten in de cloud terugbrengen tot gebruik

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/least-privilege-cloud](https://security-commons-nl.github.io/kennisbank/security/least-privilege-cloud/)

> **Barriere:** beperk app-toestemming en richt gecontroleerde admin consent in. Cloud-identiteiten, gebruikers, service-accounts, workloads, krijgen alleen de rechten die ze daadwerkelijk gebruiken, niet de rechten die ooit handig waren.

Cloud-rollen krijgen vaak ruime startrechten 'voor de zekerheid' en blijven daarna ongewijzigd. Het account voor één app heeft uiteindelijk toegang tot half het tenant, en bij compromittering is dat dan beschikbaar.

## Wanneer wel, wanneer niet

Past voor elke cloud-tenant. Wanneer niet zonder ondersteunende tools, IAM-recommendation-engines van de provider helpen substantieel.

## Zo richt je het in

Per identiteit periodiek toetsen welke rechten daadwerkelijk gebruikt worden (analyseren cloud-activity-logs). Ongebruikte rechten worden ingetrokken. Nieuwe rollen worden minimaal aangemaakt en pas uitgebreid als activiteit dat vraagt.

1. Inventariseer huidige IAM-rollen en hun toewijzingen.
2. Gebruik de cloud-recommendation-engine (AWS Access Analyzer, Azure PIM-rapporten) om ongebruikte rechten te identificeren.
3. Trek ongebruikte rechten in volgens een afgesproken cyclus.
4. Stel beleid in voor nieuwe rollen: minimale rechten, uitbreiding via aanvraag.
5. Combineer met PIM/JIT voor cloud-beheerrollen (zie het PIM-patroon).
6. Audit jaarlijks de toewijzingen op afwijkingen.

## Wat het kost en wat het oplevert

Kosten: laag.

**Wat het oplevert**

- Beperkt de impact van een gecompromitteerd account drastisch.
- Maakt audit-rapportages eenvoudiger; minder uitleg over excessieve rechten.
- Vrijwel altijd zonder extra licenties, de tools zijn in de cloud-platforms ingebouwd.

**Waar je op moet letten**

- Ongebruikte rechten intrekken kan onverwacht iets breken, vraagt voorbereide reversie.
- Cultuur 'rechten erbij voor de zekerheid' moet om; verwacht weerstand.
- Workloads die periodiek iets bijzonders doen vragen extra aandacht.

## Bewijs

- Een rapportage van toegekende tegenover daadwerkelijk gebruikte rechten, per rol of identiteit.
- Wat er is ingetrokken op basis van die meting, en wanneer.
- De procedure voor het aanvragen van een recht dat iemand toch nodig blijkt te hebben.
- De frequentie waarmee dit wordt herhaald; rechten groeien vanzelf terug.

## Zo leg je het uit

**Aan de directie.** In de cloud zijn rechten elastisch, ze groeien met de tijd. Least-privilege maakt dat we niet sluipenderwijs een tenant-wide-admin-aanval mogelijk maken.

**Aan de informatiemanager.** Gebruik van cloud-recommendation-engines; rolbeleid voor nieuwe IAM-toewijzingen.

**Aan het MT.** Workload-teams krijgen periodieke 'rechten-opruiming'; eenmalige cultuurverandering, daarna ritme.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `consent` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

Bouwt op [Cloudportalen harden](../cloudportalen-harden/).

## Licentie

[EUPL-1.2](../../LICENSE).
