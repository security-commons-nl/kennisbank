---
titel: WAF en virtual patching
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Een web application firewall met rate limiting en Layer 7-bescherming voor je publieke diensten, die bekende aanvalspatronen blokkeert en tijd koopt wanneer een patch nog niet uitgerold kan worden. Met de overgang van detecteren naar blokkeren, het beheersen van vals-positieven en het bewijs van dekking.
barrieres: [l7]
rol: fundering
---

# WAF en virtual patching

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/waf-en-virtual-patching](https://security-commons-nl.github.io/kennisbank/security/waf-en-virtual-patching/)

> **Barriere:** richt WAF, rate limiting en Layer-7-bescherming in. Als patchen niet direct kan, wordt de kwetsbaarheid afgeschermd door een WAF-/IPS-regel of een tijdelijke filter, exploit-pogingen worden geblokkeerd terwijl het echte patch nog onderweg is.

Een nieuwe CVE komt uit. De patch is er, maar testen en uitrollen kost dagen of weken. Tot dan toe is er een open gat, en aanvallers scannen vanaf dag één.

## Wanneer wel, wanneer niet

Voor exposed kritieke applicaties (publieke webdiensten, API's). Wanneer niet als vervanging van echt patchen, virtual patching is tijdelijke afdekking, niet structurele oplossing.

## Zo richt je het in

Een Web Application Firewall (WAF) of Intrusion Prevention System (IPS) voor de applicatie. Bij een nieuwe kwetsbaarheid wordt een specifieke regel uitgerold die exploit-pogingen blokkeert. Regel wordt verwijderd zodra de daadwerkelijke patch geïnstalleerd is.

1. Identificeer welke applicaties achter een WAF/IPS staan (en welke niet, en waarom).
2. Configureer beheer-toegang voor het snel uitrollen van regels.
3. Bouw een proces: nieuwe CVE → triage → tijdelijke regel → patch → regel weg.
4. Test regels in audit-mode voor productie-impact.
5. Log triggers; analyseer wat er wordt geblokkeerd.
6. Beoordeel periodiek of tijdelijke regels nog nodig zijn.

## Wat het kost en wat het oplevert

Kosten: midden.

**Wat het oplevert**

- Sluit aanvalsroutes in uren, niet weken.
- Geeft patch-traject ruimte zonder permanent gat.
- WAF/IPS biedt ook brede bescherming tegen OWASP-Top-10-aanvallen.

**Waar je op moet letten**

- Niet alle kwetsbaarheden zijn virtual-patchable.
- WAF-regels kunnen legitiem verkeer raken, audit-mode eerst.
- Verleiding om virtual patches structureel te laten staan in plaats van echt patchen.

## Bewijs

- De WAF-configuratie met per regelset of hij in detect- of in blokkeerstand staat; alleen blokkeren telt als maatregel.
- Een overzicht van beschermde applicaties tegenover alle publiek bereikbare applicaties, zodat de dekking zichtbaar is.
- De rate-limitinginstellingen per dienst.
- Bij virtual patching: welke kwetsbaarheid tijdelijk wordt afgevangen, en wanneer de echte patch komt. Een tijdelijke maatregel zonder einddatum wordt een permanente.

## Zo leg je het uit

**Aan de directie.** Tussen 'nieuwe CVE' en 'patch geïnstalleerd' zit vaak een paar weken. Virtual patching sluit dat gat in uren, verschil tussen aanvallers wel of niet binnenkomen.

**Aan de informatiemanager.** WAF/IPS voor exposed applicaties; proces voor snel uitrollen van tijdelijke regels.

**Aan het MT.** Security-team rolt regels uit bij nieuwe CVE; applicatie-teams patchen in eigen tempo wetende dat het gat tijdelijk dicht is.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `l7` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

Werkt samen met [DDoS-scrubbing en robuuste DNS](../ddos-scrubbing/) voor de netwerkkant.

## Licentie

[EUPL-1.2](../../LICENSE).
