---
titel: Beheerwerkplek voor administratieve taken
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Beheertaken gebeuren vanaf een apart gehard werkstation zonder e-mail en zonder browsen, zodat een phishingmail of besmette website nooit op dezelfde machine landt als de beheersessie. Met de inrichting, de uitzonderingen en het bewijs dat de toegestane toegang technisch is afgedwongen.
barrieres: [adminhard]
rol: fundering
---

# Beheerwerkplek voor administratieve taken

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/beheerwerkplek](https://security-commons-nl.github.io/kennisbank/security/beheerwerkplek/)

> **Barriere:** hard de beheerwerkplek en dwing de toegestane toegang af. Beheerhandelingen vinden plaats vanaf een aparte, gehardde werkplek, niet vanaf dezelfde laptop waarmee de beheerder mail en internet doet.

Beheerders gebruiken dezelfde werkplek voor mail, browsen en beheer. Eén phishingmail of één browser-exploit op die laptop levert de aanvaller directe toegang tot beheerrechten, en daarmee tot alles wat die rechten mogen.

## Wanneer wel, wanneer niet

Past voor accounts met verhoogde rechten, zeker tier-0 (identity-admin, tenant-admin). Wanneer niet: zonder dat de scheiding doorgevoerd is in beleid en hardware-toewijzing, een PAW die toch mail en web krijgt is geen PAW.

## Zo richt je het in

De beheerder krijgt een tweede, gehardde werkplek, fysiek of als beveiligde virtuele machine, waarop alleen beheer-tools draaien. Mail en internet zijn uitgeschakeld of strikt allowlist-beperkt. Beheer-accounts kunnen alleen vanaf deze werkplek inloggen.

1. Bepaal welke accounts onder PAW vallen: tier-0 in elk geval, eventueel tier-1.
2. Kies vorm: fysieke laptop of beheerde virtuele beheerdesktop.
3. Hard de werkplek op: beperkte software, geen mail, browsen uit of allowlist.
4. Configureer de identity-provider zodat beheeraccounts alleen vanaf de PAW inloggen.
5. Geef de PAW uit aan de betreffende beheerders, met instructie.
6. Monitor pogingen tot inloggen met een beheeraccount buiten de PAW.

## Wat het kost en wat het oplevert

Kosten: midden.

**Wat het oplevert**

- Eén verkeerde klik op de dagelijkse werkplek treft niet meer direct het beheer.
- Beheerhandelingen zijn herkenbaar en herleidbaar, ze komen vanaf één type apparaat.
- De PAW kan strenger geconfigureerd worden zonder dagelijkse productiviteit te raken.

**Waar je op moet letten**

- Hardware- en beheerlast voor een aparte werkplek.
- Beheerders ervaren ongemak bij het wisselen van apparaat.
- Vereist dat het identity-beleid het inloggen vanaf alleen-PAW kan afdwingen.

## Bewijs

- De configuratie van de beheerwerkplek: welke hardening-baseline, en welke functies bewust uit staan.
- Het beleid dat beheertoegang alleen vanaf die werkplek toestaat, met de dekking en de uitzonderingen.
- Een overzicht van beheersessies met het bronapparaat, zodat zichtbaar is dat de regel ook echt geldt.
- Wat er is afgesproken met leveranciers die meebeheren; zij vallen onder dezelfde eis of onder een vastgelegd alternatief.

## Zo leg je het uit

**Aan de directie.** Een beheerder die phishing krijgt op zijn dagelijkse laptop verliest daarmee meteen het beheer. Een aparte beheerwerkplek breekt die directe lijn, beperkte kosten, fundamentele verbetering.

**Aan de informatiemanager.** Aandacht voor de inrichting van de PAW (welke tools wel, welke niet) en voor de Conditional Access-regels die alleen vanaf de PAW inloggen toestaan voor beheer.

**Aan het MT.** Beheerders krijgen een tweede device of een secure desktop. Discipline nodig: beheer ALLEEN vanaf de PAW, mail en browsen op de gewone werkplek.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `adminhard` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

Werkt het beste samen met [Tiered administration](../tiered-administration/) en [FIDO2 voor beheerders](../fido2-voor-beheerders/).

## Licentie

[EUPL-1.2](../../LICENSE).
