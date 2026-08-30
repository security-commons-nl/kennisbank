---
titel: Besteed monitoring uit aan een MSSP
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Monitoring en detectie volledig uitbesteden aan een Managed Security Service Provider, wanneer een eigen securityteam er niet is en ook niet snel komt. Snel operationeel en zonder eigen nachtrooster, maar met leveranciersafhankelijkheid en beperkte kennisopbouw. Met de scope-eisen, de SLA-afspraken en het bewijs dat de opvolgtijden gehaald worden.
barrieres: [soc]
rol: alternatief
---

# Besteed monitoring uit aan een MSSP

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/uitbestede-soc](https://security-commons-nl.github.io/kennisbank/security/uitbestede-soc/)

> **Barriere:** borg 24/7 opvolging en escalatie van kritieke meldingen. Dit is de manier waarbij je de
> detectie zelf niet draait, maar de opvolging wel contractueel vastlegt.

Er is geen eigen securityteam, en dat komt er ook niet op korte termijn. Toch moet er detectie zijn;
wachten tot de capaciteit er is, is geen optie.

## Wanneer wel, wanneer niet

Past wanneer je geen eigen SOC kunt of wilt opbouwen en detectie snel geregeld moet zijn.

Wanneer niet: als je juist eigen kennis wilt opbouwen, of als maximale regie over de detectie een harde
eis is. Kijk dan naar [Co-managed SIEM](../co-managed-siem/) of
[Regionaal of gedeeld SOC](../regionaal-soc/).

## Zo richt je het in

De MSSP neemt de logs af, draait detectie op het eigen platform van de provider en levert alerts en
rapportages terug. De afhandeling van incidenten ligt bij jou, of wordt geheel of deels ook bij de
provider belegd.

1. Zorg dat [centrale logverzameling](../centrale-logverzameling/) op orde is.
2. Stel de eisen en de scope op: welke bronnen, welke dekking, welke rapportage.
3. Doorloop een aanbesteding of contracteringstraject.
4. Richt de logkoppeling met de provider in.
5. Leg escalatie- en responstijden vast in een SLA.
6. Beleg de rollen aan de eigen kant: wie ontvangt en handelt alerts af.
7. Evalueer de dienst periodiek op kwaliteit en aansluiting.

Stap 6 is de stap die het vaakst wordt overgeslagen. Een provider die meldt terwijl niemand de melding
oppakt, levert geen bescherming; het verplaatst alleen waar het misgaat.

## Wat het kost en wat het oplevert

**Wat het oplevert**

- Snel operationeel: detectie zonder een eigen team op te bouwen.
- Geen eigen 24/7-rooster nodig.
- Voorspelbare dienstkosten.

**Waar je op moet letten**

- Afhankelijkheid van een leverancier.
- Beperkte eigen kennisopbouw.
- De provider kent de lokale context maar beperkt; wat bij jou normaal is, ziet hij als afwijkend en
  andersom.
- Overstappen naar een andere provider is bewerkelijk. Leg daarom bij de start vast wat je meekrijgt als
  je vertrekt: de logs, de detectieregels en de historie.

## Bewijs

- Het contract of de SLA met de afgesproken triage-, reactie- en escalatietijden.
- Een meting of die tijden in de praktijk gehaald worden, niet alleen dat ze zijn afgesproken. Een melding
  zonder tijdige actie is nog geen bescherming.
- De scope: welke bronnen zijn aangesloten, tegenover de volledige lijst systemen.
- De rolverdeling aan de eigen kant: wie ontvangt de melding buiten kantooruren, en wie handelt hem af.
- De periodieke evaluatie van de dienst, met wat eruit kwam.

## Zo leg je het uit

**Aan de directie.** We kopen detectie in bij een gespecialiseerde partij, omdat we die kennis zelf niet
hebben en niet snel opbouwen. De afspraken over hoe snel er gereageerd wordt, staan in het contract.

**Aan de informatiemanager.** De logkoppeling met de provider is de belangrijkste technische stap; verder
verandert er weinig aan ons landschap. Let op de exit-afspraken: wat krijgen we mee als we ooit wisselen.

**Aan het MT.** Er moet aan onze kant iemand zijn die meldingen oppakt, ook buiten kantooruren. Dat is een
kleinere rol dan een eigen SOC, maar hij moet wel belegd zijn.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `soc` uit de
[zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/), en is een **alternatief**
naast [Co-managed SIEM](../co-managed-siem/), [MDR-dienst](../mdr-dienst/) en
[Regionaal of gedeeld SOC](../regionaal-soc/). De fundering onder alle vier is
[Richt centrale logverzameling in](../centrale-logverzameling/).

Ga je uitbesteden, dan zijn de eisen aan de leverancier zelf ook onderdeel van je beveiliging: zie
[Security Annex voor leveranciers](../security-annex-leveranciers/).

Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op
[Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

## Licentie

[EUPL-1.2](../../LICENSE).
