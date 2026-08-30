---
titel: Phishingbestendige MFA voor beheeraccounts
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Een aparte fysieke sleutel eisen voor beheertaken, zodat een gecompromitteerde werkplek geen beheerrechten oplevert. De zwaarste vorm van authenticatie op de zwaarste rechten. Met de uitgifte, het herstelproces en het bewijs dat de eis technisch is afgedwongen.
barrieres: [key]
rol: fundering
---

# Phishingbestendige MFA voor beheeraccounts

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/fido2-voor-beheerders](https://security-commons-nl.github.io/kennisbank/security/fido2-voor-beheerders/)

> **Barriere:** vereis een aparte fysieke FIDO2-key voor elevation. Accounts met verhoogde rechten, beheerders en functioneel beheerders, verplicht laten authenticeren met een phishingbestendige methode (FIDO2/passkey of hardware-token), zonder terugval op phishbare MFA.

De zwaarste accounts, beheerders, functioneel beheerders, beheeraccounts, leunen vaak nog op MFA-methoden die een aanvaller kan omzeilen: SMS-codes, eenmalige codes (TOTP) en push-meldingen. Reverse-proxy-phishing, MFA-fatigue en sessiecookie-diefstal zijn inmiddels standaard-aanvalstechnieken. Juist de accounts die de meeste schade kunnen aanrichten, zijn zo het zwakst beschermd, en in de praktijk blijken beheeraccounts soms zelfs helemaal zonder MFA te staan.

## Wanneer wel, wanneer niet

Altijd zinvol, en de logische eerste stap. De groep accounts met verhoogde rechten is klein en overzichtelijk; ze beschermen kan binnen weken, zonder grote organisatie-impact. Wanneer niet als losse eindstap: het beschermt alleen de beheerlaag, de reguliere accounts blijven kwetsbaar. Beschouw dit als de quick win die de weg vrijmaakt voor de bredere overstap.

## Zo richt je het in

Een phishingbestendige methode is gebaseerd op een cryptografisch sleutelpaar (FIDO2/WebAuthn). De privésleutel verlaat het apparaat van de gebruiker niet; authenticatie gebeurt met een lokale handeling, gezichtsherkenning, vingerafdruk of pincode. Voor de beheerlaag wordt deze methode verplicht gesteld in het toegangsbeleid van de centrale identity-provider, met de phishbare methoden uitgezet voor deze rolgroepen. Waar een persoonlijk apparaat onwenselijk is, vervult een hardware-token (FIDO2 security key) dezelfde rol.

1. Inventariseer alle accounts met verhoogde rechten: beheerders, functioneel beheerders, beheer- en noodaccounts. Leg per account eigenaar, gebruiksdoel en apparaat-context vast.
2. Kies de phishingbestendige methode per situatie: een passkey op een beheerd apparaat, of een hardware-token waar een persoonlijk apparaat niet passend is.
3. Richt voor elk account de methode in via persoonlijk contact, niet via een massale mail-uitvraag.
4. Scherp het toegangsbeleid aan voor de beheer-rolgroepen: phishingbestendige methode verplicht, terugval op phishbare MFA uit.
5. Richt een uitzonderingenproces in: per account, met eigenaar, motivatie en einddatum.
6. Verifieer dat geen enkel account met verhoogde rechten nog zonder of met uitsluitend phishbare MFA kan inloggen.
7. Beleg het beheer en de periodieke herijking van de lijst met beheeraccounts.

## Wat het kost en wat het oplevert

Kosten: laag.

**Wat het oplevert**

- Beschermt de gevaarlijkste accounts het eerst, grootste risicoreductie per inspanning.
- Kleine, afgebakende groep: te realiseren in weken, niet maanden.
- Geen organisatiebrede verandering nodig; lage impact op de gebruiker.
- Maakt de weg vrij voor de bredere wachtwoordloze overstap.

**Waar je op moet letten**

- Beschermt alleen de beheerlaag, reguliere accounts blijven kwetsbaar.
- Hardware-tokens voor de beheerlaag brengen een beperkte aanschaf- en beheerlast mee.
- Zonder het sluiten van bypass-routes (zie het handhavingspatroon) blijft de verplichting te omzeilen.

## Bewijs

- De configuratie die de aparte hardwarefactor afdwingt voor de kritieke beheerrollen, met de dekking.
- Het uitgifteproces: hoe komt een beheerder aan zijn sleutel, en hoe wordt vastgesteld dat hij het is.
- De beperking op registratie en herstel: wie mag een nieuwe sleutel koppelen, en onder welke voorwaarden.
- De uitzonderingen met hun reden.

## Zo leg je het uit

**Aan de directie.** De accounts die de meeste schade kunnen aanrichten zijn nu het zwakst beschermd. Deze stap dicht dat gat voor een kleine, afgebakende groep, beperkte investering, grote risicoreductie, te realiseren binnen weken.

**Aan de informatiemanager.** Het raakt het toegangsbeleid van de centrale identity-provider en de rolgroepen voor beheer. De inpassing is klein, maar de wijziging moet zorgvuldig: een fout in het beleid raakt direct de beheerbaarheid.

**Aan het MT.** Een beperkt aantal beheerders en functioneel beheerders moet een phishingbestendige methode instellen, het liefst met persoonlijke begeleiding. Reken op enkele weken doorlooptijd en korte een-op-een-ondersteuning.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `key` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

Voor de organisatiebrede overstap op passkeys: [Passkeys invoeren](../passkeys-invoeren/). Werkt samen met [Beheerwerkplek voor administratieve taken](../beheerwerkplek/).

## Licentie

[EUPL-1.2](../../LICENSE).
