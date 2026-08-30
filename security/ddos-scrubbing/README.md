---
titel: DDoS-scrubbing en robuuste DNS
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Volumetrische aanvallen laten afvangen bij een upstream partij, met robuuste en redundante DNS eronder. Zonder deze laag kan een aanval je dienstverlening plat leggen ongeacht wat je zelf hebt ingericht. Met de afspraken vooraf, de opschaling en het bewijs dat de mitigatie daadwerkelijk actief is.
barrieres: [upstream]
rol: fundering
---

# DDoS-scrubbing en robuuste DNS

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/ddos-scrubbing](https://security-commons-nl.github.io/kennisbank/security/ddos-scrubbing/)

> **Barriere:** borg upstream DDoS-mitigatie en robuuste DNS. Volumetrische en applicatie-DDoS wordt opgevangen door een scrubbing-dienst voordat het verkeer de gemeentelijke infrastructuur raakt, diensten blijven beschikbaar onder druk.

Hacktivistische DDoS, vooral pro-Russische groepen, richt zich gericht op publieke diensten in NL. Zonder scrubbing valt de website plat, en met de website vaak ook achterliggende publieksprocessen. De boodschap (verstoring) komt aan.

## Wanneer wel, wanneer niet

Voor elke publieke dienst met zichtbaarheid. Wanneer niet zonder back-up-plan: een scrubbing-dienst die de tunnel verkeerd door laat opzetten faalt op het moment dat het er toe doet.

## Zo richt je het in

Een upstream DDoS-scrubbing-dienst (cloudflare, Akamai, NaWas) ontvangt het verkeer eerst en filtert kwaadaardig verkeer. Bij grote aanvallen kan anycast load over meerdere PoPs verspreiden. Always-on of on-demand activatie; activatieprocedure is geoefend.

1. Bepaal welke diensten in scope zijn (website, publieke loketten, API's).
2. Kies een scrubbing-dienst (always-on of on-demand), sommige zijn beschikbaar via SURF/NaWas zonder commerciële prijs.
3. Configureer DNS/BGP-routing voor scrubbing.
4. Test activatie en failover periodiek.
5. Stel een communicatieplan op voor tijdens een DDoS-incident (woordvoering).
6. Monitor effectiviteit en patroon van aanvallen.

## Wat het kost en wat het oplevert

Kosten: midden.

**Wat het oplevert**

- Publieke diensten blijven onder hacktivistische DDoS overeind.
- Achterliggende systemen blijven gespaard van overspraak-effecten.
- NaWas-route (gratis voor publieke sector) bestaat als drempelloze optie.

**Waar je op moet letten**

- Always-on kost meer maar werkt zonder activatie-tijd; on-demand vraagt snelle activatie.
- DNS-/BGP-keuzes moeten passen, niet elke architectuur ondersteunt het direct.
- Application-layer DDoS-detectie vraagt extra inrichting bovenop pakket-scrubbing.

## Bewijs

- Het contract of de afspraak met de upstream partij, inclusief de capaciteit en de opschaalprocedure.
- De DNS-inrichting: redundante providers, TTL-waarden en wie er kan wijzigen tijdens een aanval.
- Een overzicht van welke diensten wel en niet achter de mitigatie staan.
- Het verslag van een oefening of een echte aanval, met de tijd tot mitigatie.

## Zo leg je het uit

**Aan de directie.** Hacktivistische DDoS richt zich gericht op overheid. Scrubbing houdt onze publieke diensten beschikbaar onder druk, beperkte kosten, grote bestuurlijke waarde bij incident.

**Aan de informatiemanager.** DNS-/BGP-routing-keuze plus activatieprocedure. Inpassing op publieke diensten zonder achterliggende systemen te raken.

**Aan het MT.** Periodieke tests; bij aanval activatie volgens procedure. Communicatie-afdeling weet welke boodschap te geven (zie crisiscommunicatie-patroon).

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `upstream` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

De response-kant staat los: het oefenen met provider en SOC hoort bij barriere `ddosresponse`, waarvoor nog geen handleiding bestaat.

## Licentie

[EUPL-1.2](../../LICENSE).
