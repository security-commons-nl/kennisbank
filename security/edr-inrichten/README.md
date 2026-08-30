---
titel: EDR inrichten met dekking en isolatie
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Endpointdetectie met tamper protection en bewaakte dekking, plus de mogelijkheid om een besmet apparaat snel te isoleren. Een EDR die op de helft van de apparaten draait, is geen dekking. Met de uitrol, de dekkingsmeting en de isolatietest als bewijs.
barrieres: [edr]
rol: fundering
---

# EDR inrichten met dekking en isolatie

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/edr-inrichten](https://security-commons-nl.github.io/kennisbank/security/edr-inrichten/)

> **Barriere:** borg EDR, tamper protection en snelle endpointisolatie. Op elke werkplek en server draait een endpoint detection & response-agent die verdacht gedrag detecteert, isoleert en aan de centrale logverzameling rapporteert.

Antivirus alleen ziet bekende signatures. Moderne malware en living-off-the-land-technieken (PowerShell, WMI, scheduled tasks) blijven onder de radar. Zonder gedrags-detectie merkt niemand wat er draait.

## Wanneer wel, wanneer niet

Past zodra werkplekken beheerd zijn (eerste patroon). Wanneer niet zonder centrale logging of SOC-respons, een EDR die signalen produceert die niemand opvolgt is een dure ruisbron.

## Zo richt je het in

Een agent op het endpoint observeert proces-, netwerk- en bestandsacties, correleert gedrag tegen aanvalspatronen en kan automatisch reageren (isoleren, proces stoppen). Telemetrie gaat naar een centraal platform of naar de centrale logverzameling.

1. Kies een EDR/XDR-product dat aansluit op het werkplekbeheer en de identity-provider.
2. Rol de agent uit naar alle werkplekken en servers (inclusief beheer- en server-tier).
3. Configureer de basis-detectieregels en het isolatie-beleid voor verdachte processen.
4. Sluit aan op de centrale logverzameling of het SIEM-platform.
5. Stem alert-afhandeling af met de SOC-functie (eigen of uitbesteed).
6. Beoordeel detectiedekking en regels periodiek.

## Wat het kost en wat het oplevert

Kosten: midden.

**Wat het oplevert**

- Detectie op gedrag, niet alleen op signature, vangt living-off-the-land en onbekende malware.
- Actieve respons: een besmet endpoint kan binnen seconden geïsoleerd worden.
- Levert telemetrie voor threat hunting en incidentonderzoek.

**Waar je op moet letten**

- Premium licentiekosten per endpoint.
- Tuning vraagt aandacht; slecht afgestemd geeft alertmoeheid.
- Vereist een SOC-functie die de signalen opvolgt, anders zonde van de investering.

## Bewijs

- De dekking: op hoeveel beheerde endpoints draait de EDR, van hoeveel in totaal, en welke ontbreken.
- Dat tamper protection aanstaat, zodat een aanvaller de sensor niet kan uitzetten.
- Een testverslag van endpointisolatie: hoe lang duurde het voordat een apparaat daadwerkelijk was afgesloten.
- Het playbook voor malware en infostealers, en wanneer het voor het laatst is gebruikt of geoefend.

## Zo leg je het uit

**Aan de directie.** Klassieke antivirus zit op de eind van zijn leven; aanvallen verlopen via legitieme tools en gedrag. EDR/XDR ziet dat gedrag en kan automatisch ingrijpen, voorwaarde voor moderne detectie.

**Aan de informatiemanager.** Inpassing op alle endpoints en servers, koppeling met de centrale logverzameling en de SOC-functie. Tuning is een doorlopende activiteit.

**Aan het MT.** De SOC-functie krijgt signalen die opgevolgd moeten worden. Reken op een afstemmoment over isolatie-mandaat (mag de tool zelf een laptop isoleren?).

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `edr` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

De configuratiecontrole hoort bij [Werkplekanalyse op het Microsoft-platform](../werkplekanalyse-e5/): aan is niet hetzelfde als gekoppeld en actief.

## Licentie

[EUPL-1.2](../../LICENSE).
