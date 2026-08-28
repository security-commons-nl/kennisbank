---
titel: Voorbeeld ingevulde matrix (verzonnen gemeente)
vakgebied: security
type: lesmateriaal
normen: []
versie: 2026-08
herkomst: bijlage bij "Risicoanalyse langs aanvalspaden"; alle gegevens verzonnen voor lesdoeleinden
status: sjabloon
samenvatting: Een ingevulde matrix en risicolijst van een verzonnen middelgrote gemeente, om te laten zien hoe de vier stappen eruitzien als je ze zet en hoe hard de rode cellen binnenkomen.
---

# Voorbeeld: gemeente Duinstad (verzonnen)

Bijlage bij [Risicoanalyse langs aanvalspaden](README.md). Gemeente Duinstad bestaat niet; de cijfers
zijn gekozen omdat ze herkenbaar zijn. Eén dag werk: ochtend stap 1 en 2 met de directie en de
CISO, middag stap 3 met de beheerders, stap 4 aan het eind van de dag.

## Stap 1. Kroonjuwelen

De directie kwam tot twaalf en schrapte er twee ("als dat een dag plat ligt, merkt niemand het").

| # | Kroonjuweel | Eigenaar | Systemen eronder |
|---|---|---|---|
| 1 | Uitkeringen en toeslagen betalen | directeur Sociaal Domein | uitkeringsapplicatie, financieel systeem, identiteitsvoorziening |
| 2 | Basisregistratie personen | hoofd Burgerzaken | BRP-applicatie, koppeling landelijke voorziening |
| 3 | Vergunningen en handhaving | directeur Ruimte | zaaksysteem, GIS, DSO-koppeling |
| 4 | Salarisbetaling | hoofd HR | HR-systeem (SaaS), financieel systeem |
| 5 | Meldkamer openbare orde en crisisorganisatie | gemeentesecretaris | Teams, telefonie, crisisportaal |
| 6 | Belastingen en WOZ | hoofd Belastingen | belastingapplicatie (SaaS), koppeling BAG |
| 7 | Website en digitale balie | hoofd Communicatie | CMS (gehost), DigiD-koppeling |
| 8 | Werkplek en mail voor 900 medewerkers | manager IV | Microsoft 365, Entra, endpoints |
| 9 | Jeugdzorg-dossiers | directeur Sociaal Domein | jeugdapplicatie (SaaS), zaaksysteem |
| 10 | Back-up en herstel van alles hierboven | manager IV | back-upplatform, offsite-kopie |

## Stap 3. Matrix

Ingevuld op basis van exports (Entra, endpointplatform, firewall, SIEM-regels, leverancierslijst) en
twee uur met de beheerders. Groen alleen waar een export of testverslag ligt.

| Kroonjuweel | 1. Account | 2. Werkplek | 3. Internetgericht | 4. Leverancier | 5. Beheerrechten |
|---|---|---|---|---|---|
| 1 Uitkeringen | D🟡 R🔴 P🟡 | D🟢 R🟡 P🟡 | D🟡 R🟡 P🟢 | D🔴 R🔴 P🔴 | D🔴 R🟡 P🟡 |
| 2 BRP | D🟡 R🔴 P🟡 | D🟢 R🟡 P🟡 | D🟢 R🟡 P🟢 | D🟡 R🔴 P🟡 | D🔴 R🟡 P🟡 |
| 3 Vergunningen | D🟡 R🔴 P🟡 | D🟢 R🟡 P🟡 | D🟡 R🟡 P🟡 | D🔴 R🔴 P🔴 | D🔴 R🟡 P🟡 |
| 4 Salaris | D🟡 R🔴 P🟡 | D🟢 R🟡 P🟡 | n.v.t. (SaaS) | D🔴 R🔴 P🟡 | D🟡 R🟡 P🟡 |
| 5 Crisisorganisatie | D🟡 R🟡 P🟡 | D🟢 R🟡 P🟡 | D🟡 R🟢 P🟡 | D🟡 R🟡 P🟡 | D🔴 R🟡 P🟡 |
| 6 Belastingen | D🟡 R🔴 P🟡 | D🟢 R🟡 P🟡 | n.v.t. (SaaS) | D🔴 R🔴 P🟡 | D🟡 R🟡 P🟡 |
| 7 Website en balie | D🟡 R🟡 P🟡 | n.v.t. | D🟢 R🟢 P🟢 | D🟡 R🟡 P🟢 | D🟡 R🟡 P🟡 |
| 8 Werkplek en mail | D🟡 R🔴 P🔴 | D🟢 R🟡 P🔴 | D🟡 R🟡 P🟡 | D🟡 R🟡 P🟡 | D🔴 R🟡 P🔴 |
| 9 Jeugdzorg | D🟡 R🔴 P🟡 | D🟢 R🟡 P🟡 | n.v.t. (SaaS) | D🔴 R🔴 P🔴 | D🟡 R🟡 P🟡 |
| 10 Back-up | D🔴 R🔴 P🔴 | D🟢 R🟡 P🟡 | D🟢 R🟡 P🟢 | D🟡 R🟡 P🟡 | D🔴 R🔴 P🔴 |

Wat opviel bij het invullen:

- **Kolom 2 is grotendeels groen op D** omdat de endpointdetectie de ClickFix-keten ziet en dat in
  april is getest. Maar P is geel: 140 van de 900 werkplekken hebben nog lokale beheerrechten.
- **Kolom 4 is de rode kolom.** Zeven leveranciers hebben permanente VPN- of beheertoegang; niemand
  kon zeggen of die toegang phishing-resistent is ingelogd, en er zijn geen inlogmeldingen op die
  accounts. De contracten eisen "passende maatregelen" zonder bewijs.
- **Kolom 5, rij 10: de back-up.** De back-upserver staat in het domein en is met een
  domeinbeheeraccount te benaderen. Een hersteltest is drie jaar geleden gedaan, op één applicatie.
- **R is bijna overal geel of rood.** Er zijn playbooks, maar ze zijn niet geoefend. Dat ene groene
  vakje (crisisorganisatie, pad 3) komt van een tabletop in het voorjaar.
- **Kolom 1 P is overal geel:** MFA staat aan, maar via pushnotificatie. Vier beheeraccounts hebben
  FIDO2, de overige 31 niet.

## Stap 4. Risicolijst

Zeventien rode cellen. Tien in deze ronde, gesorteerd op impact en op wat nu gebeurt.

| # | Risico | Maatregel | Eigenaar | Termijn of acceptatie |
|---|---|---|---|---|
| 1 | Via een leveranciersaccount (pad 4) zijn de uitkerings-, vergunning- en jeugdapplicaties bereikbaar; we zien het niet, we houden het niet tegen, we weten niet wat we dan doen | leverancierstoegang inventariseren, FIDO2 afdwingen op die toegang, inlogmeldingen aan; Annex in de eerstvolgende contractverlenging | manager IV (toegang), inkoop (contract) | inventarisatie 4 weken, FIDO2 op toegang 3 maanden |
| 2 | Back-up (kroonjuweel 10) is vanuit het domein te vernietigen (pad 5) en niet aantoonbaar herstelbaar | back-up buiten het domein, immutable kopie, volledige hersteltest | manager IV | immutable 6 weken, hersteltest 3 maanden |
| 3 | Beheeraccounts loggen in met push-MFA (pad 1, P geel op alles), en een overgenomen beheeraccount zien we niet (pad 5, D rood) | FIDO2 verplicht op alle 35 beheeraccounts; detectie op wijziging in beheerdersgroepen | manager IV | 6 weken |
| 4 | Bij een gecompromitteerd account weet niemand wie de sessies intrekt en wie de keten waarschuwt (pad 1, R rood op 7 rijen) | playbook accountcompromittering schrijven en één keer oefenen | CISO (schrijven), servicedesk (oefenen) | 8 weken |
| 5 | 140 werkplekken met lokale beheerrechten (pad 2 en 5, P rood op rij 8) | lokale beheerrechten weg, LAPS op alle apparaten | manager IV | 3 maanden |
| 6 | Salaris- en belastingapplicaties (SaaS) zonder bewijs van de leverancier over pad 1 t/m 3 aan hun kant (pad 4) | assurance en pentestrapport opvragen; ontbreekt het, dan Annex-eisen in het gesprek | inkoop, contracteigenaren | 2 maanden |
| 7 | Kritieke patch op de VPN buiten het change-venster is niet geregeld (pad 3, R geel op alles) | mandaat op één A4: wie beslist, binnen hoeveel uur | CIO | 4 weken |
| 8 | Geen overzicht van wat er aan het internet hangt (pad 3, D geel) | extern aanvalsoppervlak in kaart, kwartaalscan | manager IV | 6 weken |
| 9 | Jeugdzorg-dossiers via gecompromitteerd account bereikbaar zonder dat het opvalt (pad 1, D geel op rij 9) | conditional access op de jeugdapplicatie: alleen beheerde apparaten | manager IV, directeur Sociaal Domein | 2 maanden |
| 10 | Playbooks bestaan maar zijn nooit geoefend (R geel op bijna alles) | twee tabletops per jaar, eerste in het najaar | CISO | eerste tabletop 3 maanden |

Zeven rode cellen blijven open, allemaal in kolom 4 en 5 op kroonjuwelen 3, 6 en 9. De directeur
Bedrijfsvoering heeft die als risico-eigenaar expliciet geaccepteerd tot de volgende ronde, met de
aantekening dat regel 1 en 2 hierboven de meeste ervan meenemen.

## Wat de directie eruit haalde

Niet "we scoren 40% op detectie", maar: *als een van onze zeven leveranciers gehackt wordt, kunnen ze
bij de uitkeringen, en dat merken we niet.* Die ene zin deed meer dan de matrix. De matrix is voor de
CISO en de beheerders; de risicolijst is voor de lijn.
