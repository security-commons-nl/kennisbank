---
titel: Sessies beschermen tegen tokendiefstal
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Sessietokens binden aan het apparaat en de sessieduur beperken, zodat een gestolen token buiten zijn context niets waard is. Dit is de tegenmaatregel tegen cookie-replay na een adversary-in-the-middle-aanval. Met de inrichting, de gebruikersimpact en het bewijs van dekking.
barrieres: [session]
rol: fundering
---

# Sessies beschermen tegen tokendiefstal

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/sessiebescherming](https://security-commons-nl.github.io/kennisbank/security/sessiebescherming/)

> **Barriere:** beperk tokenmisbruik met apparaatbinding en sessiebeleid. De browser is gehardd, extensies zijn beperkt en sessiecookies zijn aan apparaat gebonden, token-diefstal via infostealer levert niet meer een werkende sessie elders.

Infostealers stelen sessiecookies en refresh tokens uit browserprofielen. Daarmee omzeilt een aanvaller alle MFA, de sessie is al geauthenticeerd. Zonder bescherming op browserniveau valt MFA tegen het lek dat na de login plaatsvindt.

## Wanneer wel, wanneer niet

Past op iedere beheerde werkplek; vooral relevant in een cloud-werkplek-context. Wanneer niet als losse stap zonder phishingbestendige MFA, een gestolen sessie van een phishbaar account is even erg.

## Zo richt je het in

Beheerde browser (Edge for Business, Chrome Enterprise) met allowlist voor extensies; opslag van credentials uit; token-binding aan het apparaat zodat een geëxporteerde cookie elders niet werkt. Sessiebeleid in de identity-provider verkort de geldigheidsduur voor gevoelige bewerkingen.

1. Stel een beheerde browser in als standaard, met centraal beheer.
2. Beperk browserextensies tot een allowlist; verwijder onbeheerde extensies.
3. Schakel password-opslag in de browser uit; verwijs naar wachtwoordmanager of passkeys.
4. Configureer token- of device-binding waar de identity-provider dat ondersteunt.
5. Verkort sessie-/refresh-token-levensduur voor gevoelige scenario's.
6. Monitor afwijkende sessie-locaties via de identity-provider.

## Wat het kost en wat het oplevert

Kosten: laag.

**Wat het oplevert**

- Tokens en cookies elders zijn waardeloos zonder het oorspronkelijke apparaat.
- Extensie-misbruik (data-exfiltratie via extensie) wordt onmogelijk.
- Past binnen bestaande browser- en identity-platformen.

**Waar je op moet letten**

- Een aantal handige extensies wordt verboden, verwacht weerstand.
- Token-binding werkt nog niet overal en is leverancier-afhankelijk.
- Vereist een beheerde browser; mengvormen werken slecht.

## Bewijs

- Het beleid met token binding of device binding, en op welke applicaties het geldt.
- De sessieduur en de momenten waarop toegang opnieuw wordt beoordeeld.
- De dekking: hoeveel gebruikers en applicaties vallen eronder, en welke niet.
- De uitzonderingen met hun reden en termijn.

## Zo leg je het uit

**Aan de directie.** MFA is niet genoeg als de sessie zelf wordt gestolen. Browser- en sessiebescherming maakt dat een gestolen sessie elders niet werkt, sluit het laatste grote gat na de invoering van passkeys.

**Aan de informatiemanager.** Inpassing op de beheerde browser en in het sessiebeleid van de identity-provider. Extensie-allowlist vraagt een beheerd proces.

**Aan het MT.** Gebruikers kunnen niet meer alle extensies installeren en zien de password-opslag uitgeschakeld. Korte instructie en doorverwijzing naar de wachtwoordmanager.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `session` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

Sterke authenticatie is de eerste barriere; sessiebescherming is wat daarna nog fout kan gaan. Zie [Passkeys invoeren](../passkeys-invoeren/).

## Licentie

[EUPL-1.2](../../LICENSE).
