---
titel: Werkplekken beheerd, gehard en gepatcht
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Patchen van besturingssysteem en third-party software met controle op dekking, zodat je niet alleen weet dat er gepatcht wordt maar ook op hoeveel apparaten het niet lukt. Met risicogestuurde termijnen, versnelde uitrol bij actief misbruik en de achterblijverslijst als bewijs.
barrieres: [patch]
rol: fundering
---

# Werkplekken beheerd, gehard en gepatcht

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/patchen-met-dekking](https://security-commons-nl.github.io/kennisbank/security/patchen-met-dekking/)

> **Barriere:** borg OS- en third-party-patching met controle op dekking. Werkplekken zijn beheerd, gehardd volgens een baseline en hebben geen lokale beheerrechten voor gebruikers.

Werkplekken staan in default-configuratie, gebruikers hebben lokale beheerrechten en de hardening-baseline is óf afwezig óf onbewaakt. Malware krijgt zo de speelruimte die het nodig heeft.

## Wanneer wel, wanneer niet

Altijd zinvol, dit is de basis waarop andere endpoint-maatregelen rusten. Wanneer niet als losse stap: zonder detectie (EDR) merk je nog niet wat er gebeurt; zonder app-control kan veel toch nog draaien.

## Zo richt je het in

Een centrale werkplekbeheer-oplossing levert een gehardde baseline (Defender for Endpoint baselines, CIS, gemeentelijke baseline). Gebruikers zijn standaard-gebruiker; lokale beheerrechten zijn de uitzondering. De compliance van de werkplek is voorwaarde voor toegang (device compliance in het toegangsbeleid).

1. Inventariseer welke werkplekken beheerd zijn en welke niet, inclusief BYOD en externen.
2. Kies een hardening-baseline (CIS of leveranciersbaseline) en stel deze in via het werkplekbeheer.
3. Verwijder lokale beheerrechten van gewone gebruikers; richt een uitzonderingsproces in.
4. Koppel device compliance aan het toegangsbeleid van de identity-provider.
5. Monitor afwijkingen van de baseline en compliance-status.
6. Beoordeel periodiek de baseline tegen actuele dreigingen.

## Wat het kost en wat het oplevert

Kosten: laag.

**Wat het oplevert**

- Sluit de meest gebruikte aanvalsroutes (uitvoer van willekeurige code als beheerder).
- Standaardiseert het werkplekbeheer en maakt afwijkingen zichtbaar.
- Zonder dit werken EDR, app-control en passkeys minder effectief.

**Waar je op moet letten**

- Bestaande lokale-admin-gewoontes vragen changemanagement bij specifieke gebruikersgroepen.
- Vereist een werkend werkplekbeheer-platform, die schaalt mee met de beheerlast.
- BYOD en externe apparaten vragen aparte route, niet altijd te hardden.

## Bewijs

- De patchdekking als percentage met de teller en de noemer erbij: hoeveel apparaten zijn bij, van hoeveel in totaal.
- De achterblijverslijst: welke apparaten missen updates, hoe lang al, en waarom.
- De afgesproken termijnen per risicoklasse, en de gemeten realisatie.
- De procedure voor versnelde uitrol bij actief misbruik, met een voorbeeld.

## Zo leg je het uit

**Aan de directie.** Werkplekken zijn de meest geraakte aanvalsroute. Een beheerde, gehardde werkplek zonder lokale beheerrechten beperkt wat een aanvaller op die werkplek voor elkaar krijgt, en is voorwaarde voor alles wat daarop volgt.

**Aan de informatiemanager.** Inpassing in het bestaande werkplekbeheer en in het toegangsbeleid (device compliance). Vraagt een uitzonderingsproces voor specifieke gebruikersgroepen.

**Aan het MT.** Eén baseline voor alle werkplekken; lokale beheerrechten alleen via uitzondering. Beperkte gewenning, eenmalig instructiewerk.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `patch` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

Voor de meetkant op werkplekken: [Werkplekanalyse op het Microsoft-platform](../werkplekanalyse-e5/).

## Licentie

[EUPL-1.2](../../LICENSE).
