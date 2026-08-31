---
titel: De killchain naast je controls leggen
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: gegeneraliseerd uit een casus bij een gemeentelijke organisatie
status: in gebruik
samenvatting: Leg je controls naast de volledige aanvalsketen, van ClickFix via infostealer tot exfiltratie, met de MITRE-fasen erbij. Per fase een chokepoint waar je knijpt of zicht krijgt, en of dat preventie, detectie of herstel is. Maakt zichtbaar waar meerdere lagen op elkaar liggen en welke restrisico's je bewust accepteert.
barrieres: [edr, execution]
rol: verdieping
pijler: meten-voordat-je-ingrijpt
---

# De killchain naast je controls leggen

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/killchain-naast-je-controls](https://security-commons-nl.github.io/kennisbank/security/killchain-naast-je-controls/)

> **Barriere:** borg EDR, tamper protection en snelle endpointisolatie, en beperk software- en
> scriptuitvoering met application control en ASR. Deze handleiding laat zien waar die maatregelen in de
> keten vallen, en wat er zonder hen open blijft staan.

## Wanneer wel, wanneer niet

Doe dit als je EDR en application control hebt staan en wilt weten wat ze samen wel en niet afdekken.
Wanneer niet als eerste stap: zonder detectie op de werkplek vul je een tabel met lege cellen. Begin dan
bij [EDR inrichten met dekking en isolatie](../edr-inrichten/) en
[Werkplekanalyse op het Microsoft-platform](../werkplekanalyse-e5/).

Leg je controls naast de aanvalsketen. Per fase is er een chokepoint: een plek waar je de aanval kunt
knijpen of zichtbaar maken. Niet elke fase hoeft preventief afgedekt; detectie + herstel kan volstaan voor de
restrisico's. Maak bewust zichtbaar wat je (nog) niet afdekt.

De keten hieronder volgt ClickFix → infostealer/RAT → exfiltratie, met MITRE ATT&CK-fasen. Per fase: het
chokepoint, en of het om preventie of detectie gaat.

| Fase (MITRE) | Voorbeeld | Chokepoint | Preventie / detectie |
|---|---|---|---|
| Initial Access | ClickFix via e-mail/website | Webproxy/SWG (URL-filter, Mark-of-the-Web), e-mailfilter | Preventie |
| Execution | `powershell -enc`, `mshta` via Win+R | EDR · AMSI · script-block-logging · PowerShell CLM · Win+R uit | Beide |
| Persistence (endpoint) | Run-key, scheduled task, startup-folder | EDR/autoruns · Sysmon (EID 13) | Detectie |
| Persistence (M365) | OAuth-consent, mailbox-forwarding | App-consent beperken · MDCA · Entra audit | Beide |
| Privilege Escalation | UAC-bypass (fodhelper/sdclt), loaders | EDR · LSA protection · ASR LSASS-regel | Preventie |
| Defense Evasion | Obfuscatie, LOLBins (regsvr32, msbuild, mshta) | ASR-regels · EDR LOLBin-detectie | Beide |
| Credential Access | Browser-SQLite, DPAPI, LSASS | ASR LSASS · browser-hardening · beheerde password manager | Beide |
| Discovery (AD) | `net group /domain`, BloodHound-collectie | Defender for Identity (AD-recon-detectie) | Detectie |
| Lateral Movement | SMB/WMI/RDP met gestolen creds, cookie-replay | Segmentatie · LAPS · Conditional Access (token binding) · SIEM | Beide |
| Collection | Browser-profielen, fileshare-mount | Audit-logging op shares (EID 4663) · DLP/UEBA | Detectie |
| Exfiltration | HTTPS POST naar C2, WebDAV-variant | Firewall-egress · TLS-inspectie · ASR 'block WebDAV' | Beide |
| Command & Control | Dead-drop resolvers, HTTPS C2 | DNS-filter · domain-reputation in SIEM | Detectie |
| Impact | Datadiefstal + leaksite | Immutable back-up · geteste restore (incl. DC) · IR-runbook · crisisplan | Herstel |

## Preventie versus detectie

- **Preventie** stopt de stap (ASR, CLM, segmentatie, egress-block).
- **Detectie** ziet de stap en maakt opvolging mogelijk (SIEM-regels, EDR, MDI, DNS-reputatie).
- **Herstel** vangt op wat doorkomt (back-up/restore, runbook).

Een gezonde posture heeft op het kritieke pad **meerdere** chokepoints, zodat het uitvallen van één laag niet
meteen de hele keten opent.

## Restrisico's die je bewust accepteert

Niet alles is realistisch af te dekken. Maak deze expliciet in plaats van ze te verzwijgen:

- **Geavanceerde C2/exfiltratie via DNS** is lastig volledig te blokkeren; leun hier op detectie en reputatie.
- **Oost-west-verkeer binnen het datacenter** valt vaak buiten de scope van een NDR rond de campus/access-laag.
  Beleg expliciet wie dit afdekt.

## Impact-anker

Het scenario dat je wilt voorkomen is publiek geïllustreerd door de aanval op een Nederlandse gemeente in
maart 2026: na een ClickFix-uitvoering werden binnen twee dagen honderdduizenden bestanden geëxfiltreerd. Eén
geslaagde keten kan dus een groot incident worden - de business case voor deze maatregelen is risicogebaseerd,
niet gebaseerd op het aantal incidenten.

## Bronnen (publiek)

- MITRE ATT&CK: T1204.004 (Malicious Copy and Paste), T1059.001 (PowerShell), T1219 (Remote Access Software),
  T1566.002 (Spearphishing Link).
- Publieke threat-intelligence over ClickFix en infostealers (o.a. Microsoft Threat Intelligence).
- Publieke berichtgeving over de gemeentelijke ClickFix-casus (maart 2026).

> **Verhouding tot de zelfcheck aanvalspaden.** De tabel hierboven volgt de volledige keten van een
> aanval, met alle MITRE-fasen. De [zelfcheck](https://security-commons-nl.github.io/aanvalspaden/) toetst
> per pad een handvol barrieres; ClickFix is daar AP09, met application control en ASR, browserhardening,
> lokale administratorrechten en EDR als chokepoints. Deze tabel is dus de uitgewerkte keten, de zelfcheck
> de snelle toets. Wijzigt de bron `paden.json`, dan volgt de zelfcheck; deze tabel is een eigen,
> gedetailleerdere snit en wordt met de hand onderhouden.

## Bewijs

- De ingevulde ketentabel voor je eigen omgeving: per fase het chokepoint dat je hebt, en of het om
  preventie, detectie of herstel gaat. Lege cellen zijn hier het resultaat, niet een tekortkoming van de
  analyse.
- Per chokepoint de verwijzing naar het bewijs dat het werkt: de dekkingsrapportage van de EDR, de
  ASR-regels in afdwingstand, de segmentatieregels, de laatste hersteltest.
- De lijst restrisico's die je bewust accepteert, met wie ze heeft geaccepteerd en op welke datum.
- Het kritieke pad met daarop het aantal lagen: valt er een weg, houdt de keten dan nog?

## Zo leg je het uit

Een aanval is geen moment maar een reeks stappen, en je hoeft niet elke stap te stoppen. Waar je preventie
hebt, stopt de aanval; waar je alleen detectie hebt, zie je hem en kun je ingrijpen; waar je niets hebt,
loopt hij door. Deze tabel maakt dat zichtbaar in plaats van dat het een aanname blijft.

Voor bestuur is de kern dat we bewust kiezen. Sommige stappen dekken we niet af omdat het niet kan of niet
in verhouding staat, en dat schrijven we op met een naam erbij. Dat is iets anders dan het over het hoofd
zien.

## Hoe dit samenhangt

Deze handleiding hoort bij de barrieres `edr` en `execution` uit de
[zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in
BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op
[Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

De funderingen onder die twee barrieres zijn [EDR inrichten met dekking en isolatie](../edr-inrichten/)
en [Werkplekanalyse op het Microsoft-platform](../werkplekanalyse-e5/); deze handleiding legt ze naast de
keten. De methode erachter staat in [Meten voordat je ingrijpt](../meten-voordat-je-ingrijpt/).

## Licentie

[EUPL-1.2](../../LICENSE).
