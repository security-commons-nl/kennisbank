# Procedure leveranciersmanagement

> **Herkomst:** procedure van de CISO van een regionale samenwerking van gemeenten, versie 1 (maart 2024). Voor de commons herschreven in een vaste opbouw; de vragenlijst voor het leveranciersoverleg is in eigen woorden opgesteld.

## Doel

Niet elke leverancier is hetzelfde. Sommige verwerken gevoelige informatie of leveren een dienst waar een
kritiek proces van afhangt. Die leveranciers verdienen meer aandacht, en het is aan de eigenaar binnen de
organisatie om te zorgen dat zij aan de eisen voldoen. Deze procedure geeft het team informatiebeveiliging
en privacy grip op die leveranciers: wie ze zijn, welke eisen gelden, en of die worden nageleefd.

## Wanneer

Bij elke leverancier die persoonsgegevens verwerkt, toegang heeft tot de eigen systemen, of een dienst
levert waarvan een kritiek proces afhangt. De classificatie van de applicatie (zie
[security classificatie](security-classificatie.md)) bepaalt de zwaarte: hoe hoger het niveau, hoe vaker en
dieper het overleg.

## Rollen

| Rol | Doet |
|---|---|
| Contracteigenaar of proceseigenaar | Eigenaar van de leveranciersrelatie; voert het overleg, bewaakt de afspraken |
| ISO of privacy officer | Stelt de eisen, beoordeelt de antwoorden en de verklaringen, signaleert risico's |
| CISO | Eindverantwoordelijk voor het proces; escaleert naar het management |
| Servicemanagement | Beheert de dienstverleningsovereenkomst en de rapportages van de leverancier |

## Stappen

1. **Inventariseren.** Welke leveranciers vallen onder deze procedure, met per leverancier: wat zij
   verwerken of leveren, de classificatie, de contracteigenaar, de overeenkomst en de verwerkersovereenkomst.
2. **Eisen stellen.** Vooraf, bij aanbesteding of contract: de beveiligingseisen en de verplichting om
   periodiek te rapporteren. Zie de [Security Annex voor leveranciers](../security-annex-leveranciers/).
3. **Periodiek overleg.** Minstens jaarlijks, bij kritieke leveranciers per kwartaal, langs de vragenlijst
   hieronder. Vraag de antwoorden vooraf op en leg vast waar het antwoord staat: in de servicerapportage of
   in het verslag van het overleg.
4. **Beoordelen.** Verklaringen toetsen met de
   [checklist assurance-verklaring](../../governance/hulpmiddelen-toegang-apparatuur-en-leveranciers/checklist-assurance-verklaring.md);
   openstaande acties en risico's vastleggen met eigenaar en termijn.
5. **Escaleren.** Komt een leverancier afspraken niet na, dan naar de contracteigenaar en zo nodig het
   management; een restrisico dat blijft, wordt vastgelegd als geaccepteerd risico in het register.
6. **Rapporteren.** De stand per kritieke leverancier gaat mee in de periodieke [rapportage](rapporteren.md).

## Vragenlijst voor het leveranciersoverleg

| Onderwerp | Vraag aan de leverancier | Wat je vastlegt |
|---|---|---|
| Openstaande acties | Staan er nog acties open uit de eerste risicoanalyse, een eerdere toets of een eerder overleg? | Welke acties, voortgang en status |
| Zekerheid (assurance) | Welke certificaten en verklaringen zijn er voor de dienst die wij afnemen, bijvoorbeeld ISAE 3402, SOC 2 of ISO 27001? | Scope en datum |
| Belangrijke wijzigingen | Is er iets wezenlijks veranderd in de beveiligingsorganisatie, in uitbesteding aan derden, in de locatie van de dienst, of in het gebruik van cloud? | Wat er veranderde en hoe het risico is afgedekt |
| Incidenten | Zijn er sinds het vorige overleg beveiligings- of privacyincidenten geweest die ons raken? | Welke gegevens, wanneer gemeld, datalek of niet, oorzaak |
| Oefenen | Is er dit jaar een incident- of crisisoefening gehouden? | Datum, bevindingen, vervolgacties |
| Herstel | Is er dit jaar een hersteltest gedaan voor onze dienst? | Welke test, datum, bevindingen, vervolgacties |
| Kwetsbaarheden | Worden de systemen die vanaf internet bereikbaar zijn, en de applicaties zelf, regelmatig gescand? | Datum laatste scan, ernstige bevindingen, vervolgacties |
| Penetratietest | Is er dit jaar een penetratietest gedaan op onze dienst? | Datum, ernstige bevindingen, vervolgacties |

## Aanvulling van de commons

> Wat de oorspronkelijke procedure open laat en BIO 2.0 en de Cbw wel vragen.

- **Ketenafhankelijkheden.** Vraag ook naar de onderaannemers van de leverancier en of die aan dezelfde eisen
  zijn gebonden. Zie [Ketenafhankelijkheden in beeld](../ketenafhankelijkheden/).
- **Meldtermijn in het contract.** Een leverancier moet een incident dat jou raakt binnen uren melden,
  anders haal je je eigen termijn van 24 uur onder de Cbw niet. Neem dat op in de overeenkomst.
- **Exit.** Wat gebeurt er met de gegevens als het contract eindigt, en is dat getest? Zie
  [Pentest- en exitverplichtingen bij leveranciers](../pentest-en-exit-bij-leveranciers/).

## Vastlegging en bewijs

- Het **leveranciersoverzicht** met classificatie, contracteigenaar en de datum van het laatste overleg.
- Per kritieke leverancier het **verslag van het overleg** langs de vragenlijst, en de beoordeelde
  verklaring.
- De **actielijst** met openstaande punten, eigenaar en termijn.

## BIO 2.0

| Maatregel | Wat deze procedure daarvoor levert |
|---|---|
| 5.19 Informatiebeveiliging in leveranciersrelaties | Het proces als geheel: inventariseren, eisen, overleg, escaleren |
| 5.20 Adresseren van informatiebeveiliging in leveranciersovereenkomsten | Stap 2: eisen en rapportageplicht in het contract |
| 5.21 Beheren van informatiebeveiliging in de ICT-toeleveringsketen | De aanvulling over onderaannemers |
| 5.22 Monitoren, beoordelen en het beheren van wijzigingen van leveranciersdiensten | Stap 3 en 4: het periodieke overleg en de beoordeling van verklaringen en wijzigingen |
