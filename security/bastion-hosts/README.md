---
titel: Beheertoegang via een bastion host
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Beheertoegang loopt via een bastion of jump host in plaats van rechtstreeks vanaf internet, met sterke authenticatie en sessieregistratie op dat ene punt. Zo verklein je het aanvalsoppervlak tot een systeem dat je echt kunt bewaken. Met de inrichting, de alternatieven en het bewijs dat er geen directe route meer is.
barrieres: [remote]
rol: fundering
---

# Beheertoegang via een bastion host

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/bastion-hosts](https://security-commons-nl.github.io/kennisbank/security/bastion-hosts/)

> **Barriere:** scherm publieke beheerinterfaces af. Beheer-toegang tot systemen verloopt via gehardde tussenstations, geen directe SSH/RDP van een werkplek naar een server, alles via een beheer-bastion.

Beheer van servers verloopt direct vanaf de werkplek via SSH of RDP. Eén compromittering op een werkplek geeft direct beheer-toegang tot productie. En de logging van wie wanneer welke server raakte is verspreid over alle servers.

## Wanneer wel, wanneer niet

Past zodra er servers worden beheerd. Wanneer niet zonder identity-koppeling: een bastion zonder MFA en logging is gewoon een tussenserver.

## Zo richt je het in

Een bastion-server (jump host of cloud-bastion-dienst) is het enige punt van waaruit beheer-toegang tot servers verloopt. Authenticatie via de identity-provider met phishingbestendige MFA; sessies worden gelogd en kunnen worden afgesloten. Directe SSH/RDP buiten de bastion om is geblokkeerd.

1. Stel een bastion-host op (eigen of cloud-dienst zoals Azure Bastion).
2. Configureer authenticatie via de identity-provider met phishingbestendige MFA.
3. Beperk netwerkrouting: directe SSH/RDP naar servers van werkplekken is uit.
4. Activeer sessie-logging op het bastion.
5. Geef beheerders instructie over de nieuwe werkwijze.
6. Monitor pogingen om de bastion te omzeilen.

## Wat het kost en wat het oplevert

Kosten: laag.

**Wat het oplevert**

- Eén punt van controle voor alle beheer-toegang.
- Sessie-logging concentreert audit-trails.
- Gecompromitteerde werkplek geeft niet langer directe productie-toegang.

**Waar je op moet letten**

- Extra hop voelt voor beheerders trager.
- Bastion zelf wordt aantrekkelijk doelwit, hardening cruciaal.
- Uitval van bastion blokkeert beheer; HA-inrichting noodzakelijk.

## Bewijs

- Een scan of inventarisatie waaruit blijkt dat er geen beheerinterface meer rechtstreeks vanaf internet bereikbaar is.
- De configuratie van de bastion: welke authenticatie, welke bronadressen, en of sessies worden vastgelegd.
- De uitzonderingen, met de reden en de termijn waarop ze verdwijnen.
- Sessielogs, zodat achteraf te reconstrueren is wie welk systeem heeft benaderd.

## Zo leg je het uit

**Aan de directie.** Beheerders kunnen nu direct vanaf hun laptop bij servers, dat schakelt onze identity-laag effectief uit. Een bastion herstelt die controle voor weinig geld.

**Aan de informatiemanager.** Bastion-positionering in het netwerk; identity-koppeling; sessie-logging. Past in bestaande architectuur.

**Aan het MT.** Beheerders werken via de bastion, kleine procedurele wijziging, één korte instructie.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `remote` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

Beheer op afstand valt ook onder [Beheerwerkplek voor administratieve taken](../beheerwerkplek/): de bastion beperkt de route, de beheerwerkplek het startpunt.

## Licentie

[EUPL-1.2](../../LICENSE).
