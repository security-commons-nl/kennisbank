# Sjabloon: een leeg register

Bijlage bij [GRC voor security, privacy en continuïteit](README.md). Vijf tabellen, één per laag van
[het model](model.md). Vul ze in de volgorde waarin ze staan. Velden tussen vierkante haken zijn invulvelden;
de eerste regel van elke tabel is een voorbeeld dat je overschrijft.

Wil je het script gebruiken, zet het register dan in JSON zoals in
[`voorbeeld-register.json`](voorbeeld-register.json). De velden zijn dezelfde.

## Peildatum en klassen

- **Organisatie:** [naam]
- **Peildatum van het register:** [JJJJ-MM-DD]
- **Klassen op score (kans × impact, elk 1 tot en met 5):** laag vanaf 1, gemiddeld vanaf [5], hoog vanaf
  [10], kritiek vanaf [16]. Neem de grenzen over uit de eigen risicoanalyse.

## 1. Strategische risico's (SR)

Uit de strategische risicoanalyse. Geen analyse? Begin met drie: uitval van dienstverlening, verlies van
persoonsgegevens, misbruik van bevoegdheden.

| Code | Strategisch risico | Kans (1-5) | Impact (1-5) | Score |
|---|---|---|---|---|
| SR-01 | [Uitval van kritieke dienstverlening door een cyberaanval] | [4] | [5] | [20] |
| SR-02 | [ ] | [ ] | [ ] | [ ] |

## 2. Operationele risico's (OR)

Uit de standaardlijst van elk kader. Elk OR hangt onder één SR, of onder "buiten de risicoanalyse".

| Code | Kader | Uit de standaardlijst | Operationeel risico | SR |
|---|---|---|---|---|
| OR-01 | [BIO2] | [ISO 27002 8.8] | [Bekende kwetsbaarheden in systemen worden te laat verholpen] | [SR-01] |
| OR-02 | [ ] | [ ] | [ ] | [ ] |

## 3. Maatregelen

Overgenomen uit de bron van het kader, met de stand zoals die daar staat. Elke maatregel hangt onder een OR
van zijn eigen kader.

| Sleutel | Maatregel | OR | Stand in de bron | Beheerseigenaar (rol) |
|---|---|---|---|---|
| [BIO2:8.08.02] | [Patches binnen de afgesproken termijn installeren] | [OR-01] | [geïmplementeerd] | [teamleider technisch beheer] |
| [ ] | [ ] | [ ] | [ ] | [ ] |

Stand per kader: BIO 2.0 *geïmplementeerd* of *niet geïmplementeerd*; BCM *voltooid*, *deels* of *niets*;
privacy *opzet*, *bestaan* en *werking* als groen, oranje of rood.

## 4. Controls

Alleen controls met een toets tellen voor het niveau. Werking telt alleen na een toets door de tweede of
derde lijn.

| Code | Control | Toetst maatregel(en) | Frequentie | Laatste toets (datum, toetser) | Opzet | Bestaan | Werking | Bewijs |
|---|---|---|---|---|---|---|---|---|
| C-01 | [Kwartaalcontrole van toegangsrechten per afdeling] | [BIO2:5.18.01] | [elk kwartaal] | [JJJJ-MM-DD, tweede lijn] | [ja] | [ja] | [nee] | [steekproef, vindplaats] |
| C-02 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] |

## 5. Bevindingen

Eén blok per bevinding. Geen OR of SR invullen: die volgen uit de eerste maatregel.

### B-01 · [het gat als patroon, smaller dan het OR]

- **Aangetoond:** [wat is vastgesteld, door welke rol, wanneer]
- **Bronsoort:** [toets, incident, meting, test of analyse]
- **Bron:** [document en vindplaats]
- **Peildatum:** [JJJJ-MM-DD]
- **Maatregel [sleutel]:** [reden waarom deze maatregel niet werkt]
- **Maatregel [sleutel]:** [optioneel, een tweede maatregel met reden]
- **Kans:** [1-5] · **Impact:** [1-5]
- **Status:** [kandidaat, open, in behandeling, geaccepteerd of gesloten], sinds [JJJJ-MM-DD]
- **Besluit risico-eigenaar:** [alleen bij geaccepteerd: wat, tot wanneer]

## Controle voor je de prioriteit laat uitrekenen

- [ ] Elk OR hangt onder een SR of staat bewust buiten de risicoanalyse
- [ ] Elke maatregel hangt onder een OR van zijn eigen kader
- [ ] Elke bevinding noemt minstens één maatregel met een reden, of een uitzondering met motivering
- [ ] Geen kaderstand als bevinding opgenomen
- [ ] Geen namen, hostnamen, accountnamen of configuratie in het register
- [ ] Elke geaccepteerde bevinding heeft een besluit en een termijn
