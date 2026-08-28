---
titel: Sjabloon matrix kroonjuwelen × aanvalspaden
vakgebied: security
type: sjabloon
normen: []
versie: 2026-08
herkomst: bijlage bij "Risicoanalyse langs aanvalspaden"
status: sjabloon
samenvatting: De matrix om in te vullen (tien kroonjuwelen tegen vijf aanvalspaden, per cel D/R/P met bewijslink) en de risicolijst die uit de rode cellen volgt, met maatregel, eigenaar en termijn of acceptatie.
---

# Sjabloon: matrix en risicolijst

Bijlage bij [Risicoanalyse langs aanvalspaden](README.md), stap 3 en 4. Kopieer, vul in, bewaar
intern. Een ingevuld voorbeeld met verzonnen cijfers staat in [`voorbeeld.md`](voorbeeld.md).

## Kroonjuwelen (stap 1)

Maximaal tien. Eigenaar is de lijn, niet IT.

| # | Kroonjuweel (proces of gegevens) | Eigenaar | Systemen eronder |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |
| 10 | | | |

## Matrix (stap 3)

Per cel drie letters, elk groen, geel of rood:

- **D** detecteren: zien we het als het gebeurt
- **R** reageren: weten we wat we dan doen, en is dat geoefend
- **P** preventief: houden we het tegen

Groen alleen met bewijs (link naar export, testverslag of playbook, niet ouder dan zes maanden).
Geen bewijs, dan geel. Niet aanwezig, dan rood.

| Kroonjuweel | 1. Gecompromitteerd account | 2. Werkplek via gebruiker | 3. Internetgerichte dienst | 4. Leverancier en keten | 5. Beheerrechten |
|---|---|---|---|---|---|
| 1 | D · R · P | D · R · P | D · R · P | D · R · P | D · R · P |
| 2 | D · R · P | D · R · P | D · R · P | D · R · P | D · R · P |
| 3 | D · R · P | D · R · P | D · R · P | D · R · P | D · R · P |
| 4 | D · R · P | D · R · P | D · R · P | D · R · P | D · R · P |
| 5 | D · R · P | D · R · P | D · R · P | D · R · P | D · R · P |
| 6 | D · R · P | D · R · P | D · R · P | D · R · P | D · R · P |
| 7 | D · R · P | D · R · P | D · R · P | D · R · P | D · R · P |
| 8 | D · R · P | D · R · P | D · R · P | D · R · P | D · R · P |
| 9 | D · R · P | D · R · P | D · R · P | D · R · P | D · R · P |
| 10 | D · R · P | D · R · P | D · R · P | D · R · P | D · R · P |

Tip: veel cellen in een kolom delen hetzelfde bewijs. FIDO2 op alle beheeraccounts is de P van kolom 1
voor élk kroonjuweel. Vul de kolom dan in één keer, en noteer het bewijs één keer.

## Bewijsregister

| Cel (kroonjuweel, pad, letter) | Bewijs | Bron | Datum | Volgende toets |
|---|---|---|---|---|
| | | | | |

## Risicolijst (stap 4)

Alle rode cellen, hoogste impact eerst. Eén regel per cel, in gewone taal.

| # | Risico (pad → kroonjuweel, wat ontbreekt) | Maatregel (chokepoint) | Eigenaar | Termijn, of geaccepteerd door en op |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

Meer dan tien regels tegelijk oppakken werkt niet. Wat niet in deze ronde past, blijft rood in de
matrix en komt in de volgende ronde terug; het verdwijnt niet.

## Ritme

- Kwartaal: bewijs vernieuwen, matrix bijwerken, risicolijst naar lijn en risico-eigenaren.
- Nieuw pad of nieuw kroonjuweel: één kolom of rij erbij.
- Na een incident: welke cel was het, stond die op groen, en waarom was het bewijs dan niet goed genoeg.
