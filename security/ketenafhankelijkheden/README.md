---
titel: Ketenafhankelijkheden in beeld
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: In beeld brengen welke kritieke processen op welke systemen en leveranciers leunen, en wat er omvalt als er een uitvalt. Uit bronnen die je vaak al hebt. Met de opbouw, het actueel houden en het overzicht als bewijs.
barrieres: [dependencies]
rol: fundering
---

# Ketenafhankelijkheden in beeld

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/ketenafhankelijkheden](https://security-commons-nl.github.io/kennisbank/security/ketenafhankelijkheden/)

> **Barriere:** breng kritieke systemen en leveranciers in samenhang in beeld. Per kritiek proces is in kaart welke leveranciers, koppelingen en data-stromen onmisbaar zijn, en wat het effect is als één van die ketens uitvalt.

De gemeente weet niet welke leveranciers en koppelingen kritiek zijn voor welke processen. Wanneer een leverancier uitvalt, door incident, faillissement, of contract-eind, is de eerste vraag 'wat raakt dit?' en niemand heeft het antwoord paraat.

## Wanneer wel, wanneer niet

Past voor elke organisatie met meerdere kritieke leveranciers. Wanneer niet als statisch overzicht: een ketenanalyse die niet wordt geactualiseerd verliest binnen een jaar haar waarde.

## Zo richt je het in

Per kritiek proces in kaart: welke leveranciers, koppelingen, datastromen zijn nodig. Wat is de impact bij uitval, en wat is de fallback? De analyse voedt het IR-proces, het crisisplan en de Annex-eisen aan kritieke leveranciers.

1. Identificeer de kritieke gemeentelijke processen (vaak 10-20).
2. Per proces: noteer leveranciers, koppelingen en data-afhankelijkheden.
3. Bepaal impact bij uitval (uren, dagen, weken) en de fallback (handmatig, alternatief).
4. Markeer single-points-of-failure en concentratierisico's.
5. Voed de uitkomst terug naar de Annex-eisen voor de kritieke leveranciers.
6. Actualiseer jaarlijks en bij grote contractwisselingen.

## Wat het kost en wat het oplevert

Kosten: laag.

**Wat het oplevert**

- Single-points-of-failure worden zichtbaar voordat ze raken.
- Voedt IR en crisiscommunicatie met concrete impactinformatie.
- Sluit aan op NIS2-bedrijfscontinuïteit en toeleveringsketen-eisen.

**Waar je op moet letten**

- De inventarisatie is werk; bij krap bezet team kost de eerste keer fors.
- Verouderde inventarisatie is bijna erger dan geen, geeft schijnzekerheid.
- Vraagt samenwerking met inkoop, IT en proceseigenaren, afstemmingstijd.

## Bewijs

- Het overzicht van kritieke processen met de onderliggende systemen en leveranciers.
- De keten achter een leverancier: wie levert aan hem, en wat betekent dat voor jou.
- De datum van de laatste actualisatie, en wie daar eigenaar van is.
- Wat het overzicht heeft opgeleverd: welke afhankelijkheid kende niemand.

## Zo leg je het uit

**Aan de directie.** Wij weten globaal welke leveranciers belangrijk zijn, niet welke onmisbaar zijn voor welk proces. Bij een crisis is dat het eerste wat we willen weten. De ketenanalyse maakt dat vooraf inzichtelijk.

**Aan de informatiemanager.** De analyse loopt langs proceseigenaren, inkoop en IT-architectuur. Resultaat is een levend register.

**Aan het MT.** Per kritiek proces wordt eens per jaar de keten opnieuw nagelopen. Beperkte structurele inspanning, fundamenteel inzicht.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `dependencies` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

Voedt de leveranciersbeoordeling: zie [Leveranciersbeoordeling](../leveranciersbeoordeling/) en [Security Annex voor leveranciers](../security-annex-leveranciers/).

## Licentie

[EUPL-1.2](../../LICENSE).
