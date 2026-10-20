# Procedure security classificatie (BIV)

> **Herkomst:** procedure van het team informatiebeveiliging en privacy (IB&P) van een regionale samenwerking van gemeenten, in gebruik. Voor de commons herschreven in een vaste opbouw en gekoppeld aan BIO 2.0; de vragenlijst en de niveaus zijn ongewijzigd overgenomen.

## Doel

Elke applicatie en elk informatiesysteem krijgt een classificatie op beschikbaarheid, integriteit en
vertrouwelijkheid (BIV). Die classificatie is de eerste stap van risicomanagement: zij bepaalt of de
standaardmaatregelen volstaan of dat een aanvullende risicoanalyse nodig is. De risicoanalyse zelf en de
keuze van extra maatregelen vallen buiten deze procedure.

## Wanneer

Bij elke nieuwe applicatie vóór ingebruikname, bij bestaande applicaties in een inhaalslag, en opnieuw bij
een significante wijziging: ander gebruik, andere gegevens, andere leverancier, verhuizing naar de cloud.

## Rollen

| Rol | Doet |
|---|---|
| ISO | Leidt de classificatie, begeleidt en daagt de proceseigenaar uit, legt het resultaat vast in de architectuurtool, test steekproefsgewijs de maatregelen |
| Proceseigenaar | Beantwoordt de vragen en tekent het resultaat af; herziet bij wijzigingen |
| CISO | Wordt geïnformeerd; geraadpleegd bij een aanvullende risicoanalyse en bij herziening |
| Afdelingsmanager | Wordt geïnformeerd bij herziening |

## Stappen

| # | Stap | Wat | R | A | C | I |
|---|---|---|---|---|---|---|
| 1 | Uitvoeren | De ISO loopt de vragenlijst met de proceseigenaar door, in de architectuurtool | ISO | Proceseigenaar | | CISO |
| 2 | Aftekenen | ISO en proceseigenaar tekenen het resultaat af | ISO | Proceseigenaar | | |
| 3 | Steekproef | De ISO toetst of de maatregelen die bij het niveau horen, zijn ingericht | ISO | | Proceseigenaar | |
| 4 | Aanvullende risicoanalyse | Staat een van de drie aspecten op het hoogste niveau, dan volgt de procedure risicoanalyse | ISO | | CISO | Team IB&P |
| 5 | Herziening | Bij significante wijzigingen wordt de classificatie herzien | Proceseigenaar | ISO | CISO | Afdelingsmanager |

## De vragenlijst

Hulpmiddel om per aspect het niveau te bepalen. Kies per vraag het antwoord dat het dichtst bij de
werkelijkheid ligt; het hoogste antwoord per aspect bepaalt het niveau.

### Beschikbaarheid

- **Maximale uitval zonder ernstige gevolgen:** 4 uur · 1 dag · 2 dagen · 1 week · 2 weken.
- **Acceptabel gegevensverlies:** 4 uur · 1 dag · 2 dagen · 1 week · 2 weken.
- **Direct geraakte gebruikers of inwoners:** minder dan 5% · minder dan 20% · ongeveer 50% · tot 75% · meer dan 75%.
- **Hoe snel moet de data hersteld zijn:** niet, het proces draait ook zonder · minstens gedeeltelijk · volledig tot een zekere datum · volledig tot een datum op korte termijn · volledig tot het moment van uitval.
- **Toelaatbaar prestatieverlies:** tot 100% · maximaal 75% · maximaal 50% · maximaal 25% · 0%.

### Integriteit

- **Gevolgen van onjuiste of gemanipuleerde informatie:** het proces staat enkele fouten toe · enige financiële of imagoschade · grote schade · zeer grote schade · niet van toepassing.
- **Risico voor het primaire proces:** geen impact · onderbreking van maximaal een dag · een week · een tot twee maanden · niet te overzien · niet van toepassing.
- **Reputatie:** verlies van publiek respect, klachten · nationale negatieve publiciteit en motivatieverlies · wekenlange negatieve berichtgeving en grote financiële schade · niet van toepassing.
- **Juridisch:** geen impact · financiële schade voor individuen · gevolgen niet op te vangen binnen de begroting.
- **Operationeel en financieel:** irritatie bij medewerkers of inwoners, interne negatieve publiciteit · juridische of strafrechtelijke vervolging · niet van toepassing.

### Vertrouwelijkheid

- **Met wie mag de informatie gedeeld worden:** openbaar · op verzoek publiek · intern zonder restricties · beperkte groep · lekken heeft zeer grote impact · geheim.
- **Gevolgen van onrechtmatige vrijgave:** geen · beperkte imagoschade · aanzienlijke imagoschade · grote financiële gevolgen.
- **Is de informatie vertrouwelijk en vereist zij extra bescherming:** ja · nee.
- **Is de informatie geheim:** ja · nee.
- **Leidt openbaarmaking tot politieke schade:** ja · nee.
- **Leidt openbaarmaking tot verlies van publiek respect, klachten of motivatieverlies:** ja · nee.

## De niveaus

**Beschikbaarheid**

- *Niet zeker:* mag langere tijd niet beschikbaar zijn zonder gevolgschade.
- *Belangrijk:* incidentele uitval is toegestaan; de organisatie functioneert nog; continuïteit op redelijke termijn hervatten.
- *Noodzakelijk:* mag bijna nooit uitvallen; continuïteit snel hervatten; serieuze schade bij uitval.
- *Essentieel:* mag alleen bij een calamiteit uitvallen; continuïteit zeer snel hervatten.

**Integriteit**

- *Verwaarloosbaar:* mag veranderd worden; geen extra bescherming.
- *Gering:* enkele fouten zijn toegestaan; basisniveau van beveiliging.
- *Ernstig:* zeer weinig fouten toegestaan; bescherming absoluut noodzakelijk.
- *Desastreus:* geen fouten toegestaan; schending geeft zeer grote schade.

**Vertrouwelijkheid**

- *Openbaar:* voor iedereen toegankelijk.
- *Intern:* voor alle medewerkers van de eigen organisatie(s).
- *Vertrouwelijk:* alleen voor een beperkte groep, op basis van vertrouwen.
- *Geheim:* alleen voor de direct geadresseerde; schending geeft zeer grote schade.

## Aanvulling van de commons

> Twee punten die de oorspronkelijke procedure open laat.

- **Vertrouwelijkheid en persoonsgegevens.** Verwerkt de applicatie bijzondere persoonsgegevens, BSN of
  gegevens over kwetsbare groepen, dan is het niveau minimaal *vertrouwelijk* en hoort de DPIA-vraag erbij.
  Koppel stap 1 aan de [DPIA-procedure](../../privacy/dpia-in-vijf-stappen/).
- **Herziening met vaste termijn.** Naast "bij significante wijziging": elke classificatie wordt uiterlijk
  na drie jaar opnieuw bekeken, anders verouderen de hoogste niveaus ongemerkt.

## Vastlegging en bewijs

- Per applicatie de **afgetekende classificatie** in de architectuurtool, met datum en wie tekende.
- Het **overzicht van alle applicaties** met niveau per aspect en de datum van de laatste herziening.
- De **steekproefverslagen** van de ISO.

## BIO 2.0

| Maatregel | Wat deze procedure daarvoor levert |
|---|---|
| 5.12 Classificeren van informatie | De classificatie zelf, met vastgelegde criteria en niveaus |
| 5.9 Inventarisatie van informatie en andere gerelateerde bedrijfsmiddelen | Het overzicht van applicaties met eigenaar en classificatie in de architectuurtool |
| 5.13 Labelen van informatie | Het niveau per aspect is het label waarop de maatregelen worden gekozen |
