---
titel: Neem een MDR-dienst met een handelingsmandaat
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Managed Detection and Response combineert detectie met een responsteam dat namens jou ingrijpt: een besmette machine isoleren, een account blokkeren, binnen een vooraf afgesproken mandaat. De snelste daadwerkelijke respons zonder eigen team, maar je geeft een handelingsmandaat uit handen. Met de mandaatvraag, het oefenscenario en het bewijs dat de containment werkt.
barrieres: [soc]
rol: alternatief
pijler: centrale-logverzameling
---

# Neem een MDR-dienst met een handelingsmandaat

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/mdr-dienst](https://security-commons-nl.github.io/kennisbank/security/mdr-dienst/)

> **Barriere:** borg 24/7 opvolging en escalatie van kritieke meldingen. Dit is de manier waarbij de
> opvolging niet stopt bij een melding, maar doorloopt tot ingrijpen.

Alleen alerts ontvangen is niet genoeg. Er is 's nachts en in het weekend niemand die daadwerkelijk
ingrijpt om een aanval te stoppen voordat de schade groot wordt.

## Wanneer wel, wanneer niet

Past wanneer snelle, actieve respons nodig is en je bereid bent een mandaat tot ingrijpen weg te geven.

Wanneer niet: als je elke handeling zelf in de hand wilt houden, of als het budget krap is. Dit is de
duurste van de vier manieren.

## Zo richt je het in

MDR combineert detectie, vaak endpoint-gericht, met een responsteam dat namens jou containment-acties
uitvoert: een besmette machine isoleren, een account blokkeren. Dat gebeurt binnen een vooraf afgesproken
mandaat.

1. Zorg dat [centrale logverzameling](../centrale-logverzameling/) op orde is.
2. Bepaal het mandaat: welke acties mag de dienst zelfstandig uitvoeren. Dit is de kernvraag; doe hem niet
   af als contractdetail.
3. Contracteer de dienst.
4. Richt de endpoint- en logkoppeling in.
5. Leg vast hoe er tijdens een incident gecommuniceerd wordt, en met wie.
6. Oefen met een realistisch aanvalsscenario, inclusief het moment waarop de dienst zelf ingrijpt.
7. Evalueer de dienst en het mandaat periodiek.

Stap 2 vraagt een bestuurlijk besluit, geen technisch. Een partij die zonder overleg een machine van een
wethouder isoleert, doet precies waarvoor hij is ingehuurd; de vraag is of dat vooraf is afgesproken.

## Wat het kost en wat het oplevert

**Wat het oplevert**

- De snelste daadwerkelijke respons van de vier manieren.
- 24/7-dekking zonder eigen team.
- Het beperkt de schade van een aanval actief, niet alleen op papier.

**Waar je op moet letten**

- Premium-kosten.
- Je geeft een handelingsmandaat uit handen.
- Afhankelijkheid van de dienst.
- Het vereist scherpe afspraken over wat de dienst wel en niet mag, en wat er gebeurt als hij ernaast zit.

## Bewijs

- Het vastgelegde mandaat: welke containment-acties de dienst zelfstandig mag uitvoeren, op welke
  systemen, en wanneer er eerst overlegd wordt.
- De afgesproken reactietijden, en een meting of ze gehaald worden.
- Het verslag van de oefening, inclusief hoe lang het duurde voordat er daadwerkelijk werd ingegrepen.
- Een overzicht van uitgevoerde containment-acties over een periode, met de afhandeling erbij.

## Zo leg je het uit

**Aan de directie.** Bij een aanval telt elk uur. Deze dienst grijpt zelf in, ook 's nachts, binnen
grenzen die wij vooraf vastleggen. Dat is de snelste manier om schade te beperken zonder een eigen team.

**Aan de informatiemanager.** De koppeling loopt via de endpoints, niet alleen via logs. Het mandaat
betekent dat een externe partij machines kan isoleren; leg vast op welke systemen dat wel en niet mag.

**Aan het MT.** Het kan gebeuren dat een laptop midden in een werkdag wordt afgesloten omdat er iets
verdachts op draait. Dat is de bedoeling, en het is goed om te weten dat het kan gebeuren.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `soc` uit de
[zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/), en is een **alternatief**
naast [Co-managed SIEM](../co-managed-siem/), [Uitbestede SOC](../uitbestede-soc/) en
[Regionaal of gedeeld SOC](../regionaal-soc/). De fundering onder alle vier is
[Richt centrale logverzameling in](../centrale-logverzameling/).

Snelle endpointisolatie is ook een barriere op zichzelf in de zelfcheck (`edr`); een MDR-dienst is een
manier om die te beleggen bij iemand die 24 uur per dag beschikbaar is.

Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op
[Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

## Licentie

[EUPL-1.2](../../LICENSE).
