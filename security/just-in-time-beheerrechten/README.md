---
titel: Just-in-time beheerrechten
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Permanente beheerrollen vervangen door rechten die je per keer activeert, met een reden en een tijdslimiet. Zo is het aantal accounts met staande rechten op elk moment vrijwel nul, en levert een gestolen beheeraccount buiten een activering niets op. Met de uitfasering, de noodaccounts en het activeringslogboek als bewijs.
barrieres: [jit]
rol: fundering
---

# Just-in-time beheerrechten

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/just-in-time-beheerrechten](https://security-commons-nl.github.io/kennisbank/security/just-in-time-beheerrechten/)

> **Barriere:** verwijder permanente rollen en gebruik PIM/JIT. Beheerrechten worden niet permanent toegekend, maar tijdelijk en op aanvraag, met goedkeuring, een tijdvenster en logging van elke activatie.

Beheerrechten staan permanent op accounts. Een gecompromitteerd beheeraccount geeft direct toegang tot alles waar dat account ooit recht op had, niet alleen tot wat het op dat moment doet. De aanvaller hoeft niet meer te wachten op het juiste moment.

## Wanneer wel, wanneer niet

Past zodra er een centrale identity-provider draait en de beheer-rolgroepen op orde zijn. Wanneer niet: zonder goedkeurings- of reviewproces erachter, JIT als rubberstamp levert nauwelijks risicoreductie op.

## Zo richt je het in

Beheer-rolgroepen worden 'eligible' in plaats van 'permanent' toegewezen. Een gebruiker activeert een rol bij behoefte, optioneel met goedkeuring door een tweede persoon, voor een tijdvenster (bijv. 4 uur). Activatie en deactivatie worden gelogd. Buiten het venster valt de rol weg.

1. Inventariseer alle accounts met permanente beheerrechten.
2. Bepaal per rolgroep: tijdvenster, goedkeuringsroute, MFA-eis bij activatie.
3. Configureer de rolgroepen in de identity-provider als 'eligible'.
4. Test de activatie- en goedkeuringsflow met een pilot van beheerders.
5. Rol uit naar alle beheer-rolgroepen, met persoonlijke begeleiding.
6. Stuur activatie-events naar de centrale logverzameling.
7. Beoordeel periodiek welke activaties echt beheer waren en welke daginzage.

## Wat het kost en wat het oplevert

Kosten: laag, binnen licentie.

**Wat het oplevert**

- Het aanvalsoppervlak van een gecompromitteerd beheeraccount krimpt: alleen ge-activeerde rollen werken.
- Activaties leveren een audit-trail; ongebruikte rechten worden zichtbaar.
- Past binnen bestaande licenties van de meeste identity-providers.

**Waar je op moet letten**

- Beheerders ervaren extra klikken; goede defaults en korte tijdvensters verzachten dat.
- Zonder goedkeuring of review wordt het procedureel zonder dat de risicoreductie volgt.
- Werkt alleen als de beheer-rolgroepen al uitgesplitst zijn, geen monolithische 'admin'-rol.

## Bewijs

- Een overzicht van rollen met permanente toekenning tegenover just-in-time, met de uitzonderingen en hun reden.
- Het activeringslogboek: wie activeerde welke rol, wanneer, hoe lang en waarom.
- De inrichting van noodaccounts (break-glass): hoeveel er zijn, waar ze bewaard worden en hoe elk gebruik wordt gemonitord.
- Het aantal accounts met staande global-adminrechten, idealiter nul buiten de noodaccounts.

## Zo leg je het uit

**Aan de directie.** Beheerrechten zijn nu permanent, wie het account heeft, heeft alles. Just-in-time draait dat om: rechten gelden alleen op het moment van gebruik. Lage drempel, lage kosten, fundamentele risicoreductie.

**Aan de informatiemanager.** Inpassing in het toegangsbeleid van de centrale identity-provider. Rolgroepen moeten op functie zijn uitgesplitst; activatie-events lopen naar de centrale logverzameling.

**Aan het MT.** Beheerders wennen aan het activeren van een rol vóór gebruik. Reken op een pilot van twee weken en een korte instructie.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `jit` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

Zonder [Tiered administration](../tiered-administration/) is de winst beperkt: just-in-time op een account dat overal mag, blijft overal mogen zodra het is geactiveerd.

## Licentie

[EUPL-1.2](../../LICENSE).
