---
titel: Onveranderbare back-ups
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Back-ups die niet gewijzigd of gewist kunnen worden, ook niet door een gecompromitteerd beheeraccount, met beheer dat gescheiden is van de rest. De aanvaller zoekt tegenwoordig eerst de back-up. Met de inrichting, de scheiding en het bewijs dat de onveranderbaarheid technisch is afgedwongen.
barrieres: [backup]
rol: fundering
---

# Onveranderbare back-ups

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/onveranderbare-backups](https://security-commons-nl.github.io/kennisbank/security/onveranderbare-backups/)

> **Barriere:** bescherm back-ups met onveranderbaarheid en gescheiden beheer. Back-ups staan buiten het bereik van een aanvaller, write-once, offline of in een apart vertrouwensdomein, zodat ze ransomware en sabotage overleven.

Back-ups staan in dezelfde vertrouwensgrens als productie. Een aanvaller met beheerrechten kan ze versleutelen of vernietigen, en doet dat ook, als eerste stap voor ransomware. Een back-up die in een aanval geraakt wordt, is geen back-up.

## Wanneer wel, wanneer niet

Altijd zinvol, voor elke organisatie waar dienstverlening afhangt van digitale data. Wanneer niet als losse stap: zonder geoefend herstel weet niemand of de back-up bruikbaar is wanneer je hem nodig hebt.

## Zo richt je het in

Back-ups worden geschreven naar opslag die geen wijziging of verwijdering toestaat gedurende de retentieperiode (immutable, write-once, object lock). Eén exemplaar staat in een ander vertrouwensdomein (offline, andere cloud, ander beheer). De back-up-keten heeft eigen credentials, niet die van productie.

1. Inventariseer welke data en configuratie kritiek is voor herstel (RPO per systeem).
2. Kies een back-upoplossing met immutability/object-lock op de doel-opslag.
3. Plaats minimaal één kopie in een ander vertrouwensdomein (offline of andere cloud).
4. Scheid back-up-credentials van productie-beheer-credentials.
5. Test technisch herstel, niet alleen of de back-up bestaat, of hij ook restoret.
6. Monitor back-up-status en alarmeer bij wijzigingen op de back-up-keten.

## Wat het kost en wat het oplevert

Kosten: midden.

**Wat het oplevert**

- Ransomware en sabotage overleven dit type back-up niet, fundamentele weerbaarheid.
- Sluit aan op de NIS2-eis voor bedrijfscontinuïteit en herstel.
- Levert ook bescherming tegen 'gewone' beheerfouten.

**Waar je op moet letten**

- Hogere opslagkosten dan reguliere back-ups.
- Immutability betekent dat je tijdens de retentieperiode niet kunt opruimen, capaciteit moet vooraf geregeld.
- Vereist discipline om kopieën daadwerkelijk in een ander vertrouwensdomein te zetten.

## Bewijs

- De configuratie waaruit blijkt dat back-ups onveranderbaar zijn, met de bewaartermijn van die onveranderbaarheid.
- De scheiding van beheer: welk account beheert de back-ups, en waarom kan een gecompromitteerd domeinbeheeraccount daar niet bij.
- De dekking: welke kritieke systemen en data zitten erin, en welke niet.
- Een test waarin is geprobeerd een back-up te wijzigen of te verwijderen, met de uitkomst.

## Zo leg je het uit

**Aan de directie.** Een aanvaller versleutelt de productie én de back-up als die binnen handbereik is. Immutable en offline back-ups maken dat onmogelijk, fundamentele voorwaarde voor herstel na een groot incident.

**Aan de informatiemanager.** Inpassing op het back-up-platform en de opslag. Vraagt een tweede locatie of een ander vertrouwensdomein, met eigen credentials.

**Aan het MT.** Het back-up-beheer wordt strikter; herstel-oefeningen worden onderdeel van het ritme. Reken op periodiek geoefend herstel als reguliere taak.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `backup` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

Een back-up is pas een back-up als je hebt teruggezet: zie [Hersteltest tegen RTO en RPO](../hersteltest/).

## Licentie

[EUPL-1.2](../../LICENSE).
