---
titel: Risicoanalyse langs aanvalspaden
vakgebied: security
type: aanpak
normen: [BIO2, ISO 27001, NIS2]
versie: 2026-08
herkomst: ontwikkeld door twee CISO's van gemeenten; bouwt op een eerder ontwerp voor een open dreigingsbeeld voor lokale overheid
status: concept
samenvatting: Methode om als CISO of ISO in één dag tot de grootste risico's te komen, en tot de maatregel en eigenaar per risico. Niet asset voor asset met geschatte kansen, maar kroonjuwelen tegen een handvol generieke aanvalspaden, met de dekking gemeten op bewijs. De rode cellen zijn de risicolijst. Met de aanvalspaden voor lokale overheid, een invulmatrix en een verzonnen voorbeeld als bijlagen.
---

# Risicoanalyse langs aanvalspaden

> **Lees de methode online:** [security-commons-nl.github.io/kennisbank/security/risicoanalyse-aanvalspaden](https://security-commons-nl.github.io/kennisbank/security/risicoanalyse-aanvalspaden/)

Een risicoanalyse hoort te eindigen in een korte lijst: dit zijn de risico's die er nu toe doen, dit is
de maatregel, dit is de eigenaar. De klassieke aanpak (asset voor asset, kans maal impact uit de duim)
eindigt zelden daar. Hij eindigt in een spreadsheet met "ransomware: hoog" die niemand kan toetsen en
die na een jaar nog precies zo is.

Deze methode vervangt het geschatte deel. De **impact** komt uit je kroonjuwelen, dat is het stuk waar
je de lijn voor nodig hebt. De **kans** is geen cijfer maar een vraag met bewijs: is dit aanvalspad bij
ons begaanbaar, en zien we het als het gebeurt? Wat overblijft is een matrix van kroonjuwelen tegen
aanvalspaden, en de rode cellen zijn je risicolijst.

Vier stappen, in één dag te zetten. Bijlagen in deze map:

| Bestand | Wat het is |
|---|---|
| [`aanvalspaden.md`](aanvalspaden.md) | De vijf generieke aanvalspaden voor lokale overheid, elk een halve pagina: hoe binnen, chokepoints, bewijsvragen |
| [`sjabloon-matrix.md`](sjabloon-matrix.md) | De matrix kroonjuwelen × aanvalspaden om in te vullen, plus de risicolijst die eruit volgt |
| [`voorbeeld.md`](voorbeeld.md) | Een ingevulde matrix van een verzonnen gemeente, om te zien hoe het eruitziet |
| [`index.html`](index.html) | Deze methode als leesversie, plakbaar in Word |

## Het verschil met de zelfcheck

De [zelfcheck](https://security-commons-nl.github.io/aanvalspaden/) zegt welke aanvalspaden openstaan;
deze methode zet die uitkomst om in risico's met een maatregel, een eigenaar en een termijn.

Het verschil zit in het bewijs. In de zelfcheck antwoord je zelf, en dat is genoeg om te bepalen waar je
moet kijken. Hier telt een antwoord niet: een cel wordt pas groen als er een artefact onder ligt.

## De som

> **risico = aanvalspad (begaanbaar?) × kroonjuweel (wat raakt het?) × dekking (zien we het, kunnen we reageren, houden we het tegen?)**

Ransomware en datadiefstal zijn het gevolg, niet de voordeur. Een aanvaller komt binnen langs een pad,
en dat pad heeft een paar plekken waar je hem kunt zien of stoppen: de chokepoints. Een risico is dus
niet "ransomware" maar: *dit pad, naar dit kroonjuweel, op dit chokepoint niet gedekt.* Zo'n risico heeft
meteen een maatregel (het chokepoint dichten) en een eigenaar (wie dat systeem beheert).

## Stap 1. Kroonjuwelen, maximaal tien

Welke processen, gegevens en systemen doen bestuurlijk pijn als ze uitvallen of lekken? Dit is het
enige stuk waar je de lijn bij nodig hebt, en het is bewust klein.

- **Tien is de grens.** De reden dat risicoanalyses stranden is dat de kroonjuwelenlijst een
  inventarisatie van alles wordt. Wie de top tien niet haalt, telt in deze ronde niet mee.
- **Vraag het aan de eigenaren, niet aan IT.** Een directeur weet wat er niet mag omvallen; IT weet wat
  er draait. Je hebt het eerste nodig.
- **Denk in processen, vertaal naar systemen.** "Uitkeringen betalen" is het kroonjuweel; de
  uitkeringsapplicatie, het financiële systeem en de identiteitsvoorziening eronder zijn waar het pad
  op uitkomt.
- **Heb je al een BIA of BIV-classificatie?** Dan is dit een selectie, geen nieuw werk. Een tool als
  [procescheck](https://github.com/security-commons-nl/procescheck) levert de lijst;
  [blast-radius](https://github.com/security-commons-nl/blast-radius) laat zien welke componenten
  eronder meerdere kroonjuwelen tegelijk raken.

Uitkomst: tien regels, elk met een eigenaar en de twee of drie systemen eronder.

## Stap 2. De aanvalspaden, generiek

De dreiging hoef je niet zelf te verzinnen en hoeft niet per organisatie. Lokale overheden delen één
dreigingsprofiel: Microsoft 365 en identiteit, leveranciersportalen, publieke dienstverlening,
ketenafhankelijkheid. De vijf paden in [`aanvalspaden.md`](aanvalspaden.md) dekken wat er de afgelopen
jaren bij gemeenten en waterschappen daadwerkelijk gebeurde:

1. **Gecompromitteerd account**: phishing, adversary-in-the-middle, hergebruikte wachtwoorden, MFA-moeheid.
2. **Werkplek via de gebruiker**: ClickFix en verwanten, de gebruiker voert zelf de code uit.
3. **Kwetsbare internetgerichte dienst**: VPN, firewall, portaal, een bekende kwetsbaarheid die te lang open staat.
4. **Leverancier en keten**: het account of de omgeving van een leverancier als opstap naar de jouwe.
5. **Misbruik van beheerrechten**: eenmaal binnen, van gewoon account naar domeinbeheer.

Per pad staat hoe het loopt, waar de chokepoints zitten en welke bewijsvragen je in stap 3 stelt. Neem de
paden zoals ze zijn. Een eigen zesde pad toevoegen mag, een pad schrappen omdat het "bij ons niet speelt"
niet: dat is precies de aanname die je wilt toetsen.

Uitkomst: vijf kolommen voor de matrix.

## Stap 3. Dekking meten, met bewijs

Nu de matrix: tien kroonjuwelen als rijen, vijf paden als kolommen. Per cel drie vragen, in deze volgorde:

| Vraag | Betekent | Bewijs dat telt |
|---|---|---|
| **D**etecteren: zien we het als het gebeurt? | Er is een detectieregel of signaal dat dit pad op dit systeem zichtbaar maakt | De regel bestaat (export uit de SIEM of het platform) én is beproefd (een test, een oefenverslag) |
| **R**eageren: weten we wat we dan doen? | Er is een route: wie belt wie, wat schakelen we af, hoe draaien we terug | Een playbook dat minstens één keer is gelopen |
| **P**reventief: houden we het tegen? | Het chokepoint is dicht: FIDO2 afgedwongen, patch binnen de termijn, segmentatie staat | Configuratie-export of scanresultaat, niet ouder dan het bewijs mag zijn |

De volgorde is D, R, P. Eerst zien, dan handelen, dan voorkomen. Een organisatie die niets tegenhoudt
maar alles ziet, staat er beter voor dan een die veel tegenhoudt en niets ziet.

**De gouden regel: bewijs stuurt status.** Groen is een gekoppelde, actieve maatregel én een
beproevingsverslag. "We hebben MFA" is geen bewijs; een export waaruit blijkt dat alle beheeraccounts
FIDO2 afdwingen wel. Geen bewijs, dan geel. Bewijs ouder dan een half jaar, dan ook geel: laat groen
vanzelf degraderen, anders wordt de matrix een dashboard dat liegt.

Waar het bewijs vandaan komt, staat per pad in de bijlage. Voor wie het gestructureerd wil doen: de
[security-posture-tool](https://github.com/security-commons-nl/security-posture-tool) leest exports
(Entra, nmap, Nessus, firewall-configuraties, SIEM-regels) en legt het bewijs onder de bevinding;
[Handelingsperspectief](https://security-commons-nl.github.io/Handelingsperspectief/) werkt pad 2
helemaal uit tot aan de query's.

Uitkomst: vijftig cellen, elk groen, geel of rood, met per groene cel een bewijslink.

## Stap 4. De rode cellen zijn de risicolijst

Sorteer de rode cellen. Elke cel is een risico dat je kunt uitspreken in één zin die iedereen begrijpt:

> *Via een gecompromitteerd leveranciersaccount (pad 4) is de uitkeringsapplicatie (kroonjuweel 3)
> bereikbaar, en we zien dat niet (D rood) en houden het niet tegen (P rood).*

Per rode cel drie dingen erbij:

1. **De maatregel**: het chokepoint uit de bijlage. Meestal is het er één, en meestal is hij bekend.
2. **De eigenaar**: wie het systeem beheert. Niet de CISO. De CISO voert het gesprek en bewaakt de
   lijst, de lijn draait aan de knoppen.
3. **De termijn**, of het besluit om het niet te doen. Een rode cel die open blijft, is een restrisico,
   en dat accepteert de risico-eigenaar expliciet. Niet stilzwijgend, niet de CISO namens hem.

Rood vóór oranje, oranje vóór geel. Meer dan tien rode cellen tegelijk oppakken werkt niet; kies op
kroonjuweel (hoogste impact eerst) en op pad (wat we nu daadwerkelijk zien gebeuren eerst; op dit
moment zijn dat pad 1, 2 en 4).

Uitkomst: de risicolijst. Eén A4, elke regel met maatregel, eigenaar en termijn of acceptatie.

## Ritme

Dit is geen jaarlijkse exercitie maar een matrix die je bijhoudt:

- **Elk kwartaal**: bewijs vernieuwen, cellen die degradeerden opnieuw beoordelen, de risicolijst naar
  de lijn en de risico-eigenaren.
- **Bij een nieuw pad** (een dreiging die zich aandient, een advies van het nationale CSIRT): één kolom
  erbij, tien cellen beoordelen, klaar.
- **Bij een nieuw kroonjuweel** (een nieuwe dienst, een nieuwe leverancier): één rij erbij.
- **Bij een incident**: welke cel was het, en stond die op groen? Dan was het bewijs niet goed genoeg.
  Dat is de leerlus.

## Wat deze methode niet is

- **Geen vervanging van je ISMS.** De matrix voedt de risicoregistratie van je managementsysteem; ze
  vervangt hem niet. Voor de formele kant (BIO2, ISO 27001, NIS2-zorgplicht) blijft het
  managementsysteem het kader, en een platform als [grc-platform](https://github.com/security-commons-nl/grc-platform)
  de plek waar controls en bewijs formeel landen.
- **Geen dreigingsbeeld.** De vijf paden zijn een gedeelde, stabiele set, geen maandelijkse
  nieuwsbrief. Een dreigingsbeeld vertelt wat er gebeurt; deze methode vertelt wat dat voor jou betekent.
- **Geen audit.** Groen betekent "bewijs aanwezig en beproefd", niet "conform norm X". De vertaling naar
  normen doe je daarna, met de matrix als onderbouwing.

## Hoe dit samenhangt met de andere stukken

Deze methode is de leeswijzer over de commons heen. Elke stap heeft een project dat hem invult:

| Stap | Wat helpt |
|---|---|
| 1. Kroonjuwelen | [procescheck](https://github.com/security-commons-nl/procescheck) (BIA/BIV), [blast-radius](https://github.com/security-commons-nl/blast-radius) (wat valt om) |
| 2. Aanvalspaden | de [zelfcheck](https://security-commons-nl.github.io/aanvalspaden/) (een uur, achttien routes) en de bijlage bij deze methode; pad 2 uitgewerkt in [Handelingsperspectief](https://security-commons-nl.github.io/Handelingsperspectief/) |
| 3. Dekking met bewijs | [security-posture-tool](https://github.com/security-commons-nl/security-posture-tool), [iamscan](https://github.com/security-commons-nl/iamscan) (pad 5 op Linux) |
| 4. Risicolijst en gesprek | naar leveranciers: [Security Annex](../security-annex-leveranciers/) (pad 4 als contract); naar binnen: [Een blue team opzetten](../blue-team-opzetten/) (de rode cellen dichten met mandaat) |

## Herkomst

Ontwikkeld door twee CISO's van gemeenten, vanuit dezelfde ervaring: de risico's die er nu toe doen
zijn geen scenario's maar paden, en de maatregelen die het verschil maken zijn de chokepoints erop.
De methode bouwt op een eerder ontwerp voor een open, aanvalspad-centrisch dreigingsbeeld voor lokale
overheid (mei 2026); dat ontwerp is hierin opgegaan.

## Licentie

[EUPL-1.2](../../LICENSE), vrij te hergebruiken en aan te passen. Feedback en verbeteringen welkom via een
[issue](https://github.com/security-commons-nl/kennisbank/issues/new/choose).
