---
titel: Je aanvalsoppervlak in beeld houden
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Ontdekken en blijven bewaken wat er vanaf internet van je organisatie te zien is, inclusief de diensten die niemand meer kent. Wat je niet weet dat bestaat, patch je niet. Met de ontdekmethode, het eigenaarschap per dienst en het bewijs dat de lijst actueel blijft.
barrieres: [assets]
rol: fundering
---

# Je aanvalsoppervlak in beeld houden

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/aanvalsoppervlak-bewaken](https://security-commons-nl.github.io/kennisbank/security/aanvalsoppervlak-bewaken/)

> **Barriere:** ontdek en bewaak het externe aanvalsoppervlak. Continue ontdekking van wat de gemeente vanaf het internet aan diensten en assets aanbiedt, bekende én vergeten, met inzicht in wat aanvallers daar zien.

Niemand weet meer wat er allemaal aanstaat op het internet onder de gemeentelijke domeinen. Een oude testserver, een vergeten subdomain, een verlaten cloud-account, elk is een aanvalsoppervlak dat niet in audits zit.

## Wanneer wel, wanneer niet

Past voor elke organisatie met substantiële externe footprint. Wanneer niet zonder opvolging: een ASM-rapport zonder opruim-actie wordt cynisch.

## Zo richt je het in

Een ASM-tool of -dienst scant continu vanaf het internet voor alles wat onder de gemeentelijke domeinen, IP-ranges, ASN's of cloud-accounts hoort. Vindt vergeten assets, verkeerd geconfigureerde diensten en blootgestelde gegevens.

1. Identificeer de 'attack surface domains' (DNS-zones, IP-ranges, cloud-tenants).
2. Kies een ASM-tool/dienst (commercieel of open-source als amass).
3. Voer een eerste discovery uit; review bevindingen.
4. Beleg eigenaarschap per bevinding-type (DNS-team, applicatie-team).
5. Stel een proces in voor opruimen van vergeten assets.
6. Houd een externe-footprint-register bij dat doorlopend wordt geüpdatet.

## Wat het kost en wat het oplevert

Kosten: midden.

**Wat het oplevert**

- Vergeten assets komen aan het licht, vaak het meest kwetsbaar.
- Geeft het perspectief van de aanvaller: wat zien zij?
- Sluit aan op kwetsbaarheidsbeheer en exposure management.

**Waar je op moet letten**

- Eerste discovery levert vaak verrassend veel op, opruim-werk.
- Sommige bevindingen zijn van legacy partners, opruimen is afstemming.
- Tool-keuze niet triviaal; gratis tools dekken niet alles.

## Bewijs

- Een actueel overzicht van alles wat vanaf internet bereikbaar is, met per dienst een eigenaar.
- De frequentie waarmee dat overzicht wordt ververst, en hoe: passief, actief scannen of via een dienst.
- Wat er is gevonden dat niemand kende, en wat daarmee is gebeurd.
- De koppeling naar kwetsbaarhedenbeheer: nieuwe diensten komen automatisch in scope.

## Zo leg je het uit

**Aan de directie.** Wat heeft de gemeente eigenlijk aanstaan op het internet? Daar krijgen we vandaag geen scherp antwoord op. ASM levert dat, en vindt regelmatig vergeten assets die aanvallers anders eerder vinden.

**Aan de informatiemanager.** DNS, IP, cloud-tenant-administratie als scope-input. Bevindingen lopen langs domein-eigenaren.

**Aan het MT.** Eigenaren van applicaties en netwerken krijgen periodieke opruim-acties uit ASM-rapportage.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `assets` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

Voedt [Kwetsbaarheden scannen](../kwetsbaarheden-scannen/): de scan is niet meer waard dan de volledigheid van de lijst.

## Licentie

[EUPL-1.2](../../LICENSE).
