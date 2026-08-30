---
titel: Identiteit en e-mail meten voordat je afdwingt
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: gegeneraliseerd uit een casus bij een gemeentelijke organisatie
status: in gebruik
samenvatting: Twee lagen die met Microsoft 365 E5 grotendeels afgedekt kunnen worden, maar in de praktijk vaak op standaard of "deels" staan. Toets de feitelijke inrichting van Defender for Office, Conditional Access, app-consent en legacy authentication, met per punt wat "goed" eruitziet. In veel gemeenten komt het merendeel van de incidenten via e-mail en identiteit binnen, niet via de werkplek.
barrieres: [mail, legacy, session, consent]
rol: verdieping
pijler: meten-voordat-je-ingrijpt
---

# Identiteit en e-mail meten voordat je afdwingt

> **Barrieres:** een sterke e-mailbaseline, legacy authentication blokkeren, tokenmisbruik beperken en
> app-toestemming beheersen. Deze handleiding toetst wat er feitelijk aanstaat, want "we hebben E5" zegt
> niets over het beleid dat actief is.

Twee lagen die met E5 grotendeels afgedekt kunnen worden, maar in de praktijk vaak op standaard of
"deels" staan. Het incidentbeeld onderstreept hun belang: in veel gemeenten komt het merendeel van de
incidenten via e-mail en identiteit binnen, niet via de werkplek-uitvoering zelf.

## Wanneer wel, wanneer niet

Altijd, en bij voorkeur voordat je in de werkplek gaat ingrijpen. E-mail is doorgaans de grootste instroom
van incidenten en daarmee de hoogste hefboom.

Deze handleiding is een **toets**, geen inrichtingsplan. Hij vertelt je wat je moet controleren en wat
goed eruitziet; het invoeren van passkeys staat in [Passkeys invoeren](../passkeys-invoeren/), en de
methode achter deze aanpak in [Meten voordat je ingrijpt](../meten-voordat-je-ingrijpt/).

## Zo richt je het in

### E-mail: Defender for Office 365 (MDO)

Controleer of MDO meer doet dan de standaard:

- **Preset security policies (Standard of Strict)** of een gelijkwaardig eigen beleid actief, niet alleen
  defaults met losse Safe Links en Safe Attachments.
- **Anti-phishing** met impersonation- en spoofbescherming.
- **Quarantine-notificaties** ingericht.

Omdat e-mail vaak de grootste instroom van incidenten is, is dit doorgaans de **hoogste hefboom**. Toets
de feitelijke inrichting; "we hebben MDO" zegt niets over het beleid dat actief is.

### Identiteit: Entra ID en Defender for Identity (MDI)

Loop deze punten langs:

- **MFA-dekking.** Voor alle gebruikers, niet "voor sommige". Controleer ook break-glass-accounts.
  Overweeg sterk passkeys.
- **Legacy authentication.** Geblokkeerd, niet alleen "report only".
- **Conditional Access.** Met device-compliance en **token binding**. Dit is de tegenmaatregel tegen
  AitM-cookiereplay (gestolen sessietokens), een veelgebruikte vervolgstap na credential-diefstal.
  Gebruikers worden steeds vaker naar malafide inlogpagina's geleid; er zijn Nederlandse
  securityleveranciers die daar gratis beschermingsdiensten voor aanbieden.
- **Privileged Identity Management (PIM).** Just-in-time verhoogde rechten in plaats van staande rechten.
  Let op het aantal global admins; staande beheerrechten zonder PIM zijn een veelvoorkomend risico.
- **Defender for Cloud Apps (MDCA).** Minimaal voor OAuth- en app-consentmisbruik, en sowieso handig om
  schaduwgebruik van cloud-apps inzichtelijk te maken. Afhankelijk van de keuze tussen reguleren
  (lockdown) en veilig faciliteren blokkeer je app-gebruik, of kijk je naar de voorwaarden die nodig zijn
  om de apps veilig te ondersteunen.
- **User-consent voor niet-geverifieerde apps.** Zet op "do not allow user consent". Dit is een
  eenvoudige, effectieve maatregel tegen malafide software die zich langdurig toegang tot Microsoft 365
  wil verschaffen.
- **MDI-sensors.** Op domain controllers, en waar van toepassing op ADCS en ADFS, voor detectie van
  verdachte AD-recon (BloodHound-achtige collectie, complete groepsdumps).

### ADCS (Active Directory Certificate Services)

Detectie van certificaatmisbruik (de ESC1 tot en met ESC8-technieken) zit **niet** standaard in MDE of
EDR. Zonder te veel in detail te gaan: dit is een populaire aanval om snel beheerrechten te verkrijgen op
een lokale infrastructuur. Ga niet uit van de aanname dat dit door de endpointbescherming gedekt is.
Verifieer het, en richt aanvullende logging in op de interne CA als die er is.

## Wat het kost en wat het oplevert

De toets zelf kost een dagdeel per laag. Het aanzetten van preset security policies en het blokkeren van
legacy authentication is goedkoop; token binding en het intrekken van staande beheerrechten kosten meer
afstemming, omdat je daar mensen in hun werk raakt.

Wat "goed" eruitziet:

- E-mailbeleid actief en aantoonbaar effectief, niet op standaardinstellingen.
- MFA overal, of nog liever werken met passkeys. Legacy auth dicht, Conditional Access met
  device-compliance en token binding.
- Privileged access just-in-time (PIM), beperkt aantal vaste beheerders.
- App-consent beperkt; MDCA actief voor consent en forwarding.
- MDI-sensors uitgerold en AD-recon-detectie aantoonbaar.

## Bewijs

Export of configuratie waaruit blijkt dat de maatregel technisch is afgedwongen, met de dekking en de
uitzonderingen erbij. Concreet per barriere:

- **E-mail:** de actieve MDO-policy met het beschermingsniveau, en het aantal postbussen dat eronder valt
  tegenover het totaal.
- **Legacy authentication:** het Conditional Access-beleid in *enforce* (niet report-only), met de
  uitzonderingen en hun reden.
- **Sessies:** het beleid met device-compliance en token binding, en het aantal gebruikers dat eronder
  valt.
- **App-consent:** de instelling voor user-consent, plus de lijst met bestaande toestemmingen die je hebt
  beoordeeld en opgeschoond.

## Zo leg je het uit

**Aan de directie.** De meeste incidenten komen binnen via e-mail en gestolen inloggegevens, niet via de
werkplek. Wij controleren of de bescherming die we al betalen ook echt aanstaat, en zetten aan wat op
standaard bleef staan.

**Aan de informatiemanager.** Dit is grotendeels configuratie in producten die we al hebben. De
zwaarste ingrepen zijn het blokkeren van legacy authentication en het beperken van app-toestemming; beide
vragen een inventarisatie van wat er nu op leunt.

**Aan het MT.** Medewerkers merken hier weinig van, behalve dat ze soms een app niet meer zelf kunnen
goedkeuren. Die aanvraag loopt dan via een korte route bij beheer.

## Hoe dit samenhangt

Deze handleiding hoort bij de barrieres `mail`, `legacy`, `session` en `consent` uit de
[zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/), en is een uitwerking van de
methode [Meten voordat je ingrijpt](../meten-voordat-je-ingrijpt/). Voor het invoeren van
phishingbestendige authenticatie zelf is er [Passkeys invoeren](../passkeys-invoeren/). Wat je hiermee
aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op
[Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

## Licentie

[EUPL-1.2](../../LICENSE).
