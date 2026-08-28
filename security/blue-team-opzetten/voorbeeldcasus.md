---
titel: Voorbeeldcasus blue team (verzonnen)
vakgebied: security
type: lesmateriaal
normen: [BIO2]
versie: 2026-08
herkomst: bijlage bij "Een blue team opzetten"; alle cijfers verzonnen voor lesdoeleinden
status: sjabloon
samenvatting: Een verzonnen nulmeting en coverage-heatmap van een regionale samenwerking, om te laten zien hoe de foto uit stap 1 en de heatmap uit stap 6 eruitzien als je ze invult. Geen weergave van een bestaande organisatie.
---

# Voorbeeldcasus (verzonnen)

Bijlage bij [Een blue team opzetten](README.md). Alle cijfers zijn verzonnen; ze zijn gekozen omdat ze
herkenbaar zijn, niet omdat ze van een bestaande organisatie komen. Gebruik dit om te zien hoe hard een
nulmeting binnenkomt en hoe een heatmap de aandacht stuurt.

## De trigger

Meerdere autoriteiten waarschuwen onafhankelijk voor AI-gedreven aanvalscapaciteit: modellen die
zelfstandig kwetsbaarheden vinden en tot werkende aanvalsketens koppelen, brengen de tijd van
"kwetsbaarheid bekend" naar "actief misbruikt" terug van dagen naar uren. Zodra die capaciteit breed
beschikbaar is, kan in feite iedereen een aanvaller worden. De casus rekent met een handelingsvenster tot
`[einddatum venster]`.

## De nulmeting (stap 1)

| Bevinding | Stand |
|---|---|
| Accounts zonder MFA | ± 640, waarvan 61 beheerdersaccounts |
| Direct exploiteerbare kwetsbaarheden | 152; daarnaast 2.180 HIGH en 34 CRITICAL met een patch ouder dan 60 dagen |
| Identity Secure Score / Zero Trust / ransomware-bescherming | 29% / 41% / 52% |
| Netwerk | geen DNS-filtering; beheerpaden bereikbaar vanuit het werkplek-VLAN; end-of-life-component in de keten |
| Pentest (zonder AI) | Domain Admin in één dag; 47% van de wachtwoordhashes gekraakt |

Stuk voor stuk bekende, dichtbare gaten. Te veel om in de reguliere cyclus op tijd weg te werken; dat is
het argument voor het venster.

## De coverage-heatmap (stap 6)

Uitkomst van de eerste run: per zone de dekking op Detect, Respond en Prevent.

| Zone | Detect | Respond | Prevent |
|---|---|---|---|
| Eindgebruiker / werkplek | 60% | 55% | 75% |
| Identiteit (AD, Entra) | 50% | 35% | 55% |
| Datacenter / servers | 45% | 50% | 70% |
| Cloud (IaaS, PaaS, SaaS) | 25% | 20% | 45% |
| OT / openbaar | 50% | 45% | 55% |
| Leveranciers / keten | 10% | 5% | 15% |

Lezen: groen is grotendeels gedekt, geel deels, rood nauwelijks. In dit beeld is de zone leveranciers en
keten de schreeuwer, precies waar veel organisaties blind zijn. De eerste Rood-kaarten komen daar vandaan.

## De governance in deze casus

Regionale samenwerking van vier gemeenten met één gedeelde digitale infrastructuur. Opdrachtgever: de
directeur Bedrijfsvoering. Beslisser en budgethouder: de CIO. Groen licht: de gemeentesecretaris, mede
namens de regiogemeenten. Kernteam van zes, schil van vier. Einddatum en afbouwbesluit vooraf vastgelegd.

Wat een ingreep hier kon betekenen, in de woorden van de memo aan het college: (A) 's avonds een spoedpatch
op een internetgerichte dienst, inwoners merken hooguit enkele minuten onderbreking; (B) bij verdenking van
accountmisbruik een dienst een dag stil voor onderzoek, met balie en telefoon als terugval; (C) bij een
bevestigd incident een gespecialiseerde partij inschakelen, mogelijk fysiek op locatie. In alle gevallen
hoort het bestuur het op het moment zelf, niet achteraf.
