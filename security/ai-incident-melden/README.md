---
titel: Wanneer meld je een AI-incident?
vakgebied: security
type: aanpak
normen: [Cbw, AVG, AI Act]
peildatum: 2026-09-25
herkomst: uitgewerkt vanuit de CISO-praktijk bij gemeenten, op basis van de Cyberbeveiligingsregeling sector overheid, de AVG en de AI Act
status: concept
samenvatting: Bij een incident met een AI-toepassing kunnen drie meldplichten gelden: Cbw, AVG en AI Act, elk met een eigen drempel en termijn. Voor gemeenten telt onder de Cbw vooral uitval van dienstverlening van vier uur of meer; een lek via een AI-assistent haalt die drempel meestal niet, maar is vaak wel een datalek. Vijf scenario's uitgewerkt, met wat je vooraf regelt.
---

# Wanneer meld je een AI-incident?

> **Lees de aanpak online:** [security-commons-nl.github.io/kennisbank/security/ai-incident-melden](https://security-commons-nl.github.io/kennisbank/security/ai-incident-melden/)

Een AI-assistent geeft een medewerker stukken uit een dossier waar die niet bij mag. Een gateway blijkt
een kwaadaardige versie te draaien. Een chatbot voor inwoners geeft een week lang verkeerde informatie.
Moet je dat melden, en bij wie? Er kunnen drie meldplichten tegelijk gelden, elk met een eigen drempel en
een eigen termijn. De eerste vierentwintig uur zijn de verkeerde tijd om die uit te zoeken.

## Drie meldplichten naast elkaar

| | Cyberbeveiligingswet | AVG | AI Act |
|---|---|---|---|
| **Wat** | significant incident | inbreuk op de beveiliging van persoonsgegevens | ernstig incident met een hoog-risicosysteem |
| **Wie meldt** | de gemeente | de gemeente als verwerkingsverantwoordelijke | de aanbieder van het systeem; de gemeente als gebruiker meldt aan de aanbieder |
| **Bij wie** | CSIRT en toezichthouder, in één melding via het portaal van het NCSC | Autoriteit Persoonsgegevens, en bij hoog risico de betrokkenen | markttoezichthouder |
| **Termijn** | vroegtijdige waarschuwing binnen 24 uur, melding binnen 72 uur, eindverslag binnen een maand | binnen 72 uur | uiterlijk 15 dagen; 2 dagen bij een wijdverbreide inbreuk of verstoring van kritieke infrastructuur, 10 dagen bij een dode |
| **Geldt sinds** | 15 augustus 2026 | 25 mei 2018 | 2 december 2027 voor systemen uit bijlage III |

Voor gemeenten is de AI Act-meldplicht voorlopig de kleinste. Hij geldt alleen voor hoog-risicosystemen,
pas vanaf december 2027, en ligt bij de aanbieder. Bouwt de gemeente zelf een hoog-risicotoepassing, dan
is zij die aanbieder. Of dat zo is, kun je nagaan met [Ben ik aanbieder onder de AI Act?](../../governance/aanbieder-onder-de-ai-act/).

## De Cbw-drempel voor gemeenten

De wet noemt een incident significant als het een ernstige operationele verstoring of financiële verliezen
veroorzaakt of kan veroorzaken, of anderen aanzienlijke schade toebrengt (art. 25). De regeling voor de
sector overheid maakt dat concreet. Voor decentrale overheden is een incident significant als het leidt
of kan leiden tot (art. 6 lid 2):

1. uitval van de dienstverlening van ten minste vier uur;
2. financiële gevolgen die niet in de begroting kunnen worden opgevangen;
3. de ernstige verwonding of de dood van ten minste één persoon.

Gepland onderhoud telt niet mee (art. 6 lid 3).

Twee dingen vallen op. De lijst voor decentrale overheden heeft **geen drempel voor vertrouwelijkheid**.
De lijst voor het Rijk heeft die wel: daar is onbevoegde kennisname van gerubriceerde informatie een
significant incident. Een lek van gegevens via een AI-toepassing is voor een gemeente dus zelden een
Cbw-melding. Het is wel vaak een datalek onder de AVG.

Het tweede zit in de woorden **kan leiden tot**. Een gecompromitteerde AI-gateway ligt misschien zelf niet
plat, maar de sleutels die erop stonden kunnen toegang geven tot systemen waarvan de uitval de
dienstverlening wel raakt. Beoordeel dus wat het incident kan veroorzaken, en leg die afweging vast, ook
als de uitkomst "niet melden" is.

## Vijf scenario's

| Scenario | Cbw | AVG | AI Act |
|---|---|---|---|
| **1. Kwaadaardige versie van een AI-component**, geheimen van de server gestolen | waarschijnlijk wel, via "kan leiden tot": wat openen de gestolen sleutels? | wel, als die sleutels toegang geven tot persoonsgegevens | nee |
| **2. Prompt injection**: een assistent geeft vertrouwelijke stukken aan iemand die er niet bij mag | meestal niet, geen vertrouwelijkheidsdrempel | wel bij persoonsgegevens, tenzij een risico voor betrokkenen onwaarschijnlijk is | nee, tenzij het een hoog-risicosysteem is |
| **3. De AI-omgeving voor medewerkers ligt zes uur plat**, het werk gaat handmatig door | niet, de dienstverlening valt niet uit | nee | nee |
| **4. Ransomware via een agent met te ruime rechten**, het zaaksysteem ligt een dag plat | wel, uitval van meer dan vier uur | wel, als er gegevens zijn ingezien of weggehaald | nee |
| **5. Een chatbot voor inwoners geeft wekenlang verkeerde informatie** over een voorziening | niet, dit is geen beveiligingsincident | nee | alleen als het systeem hoog risico is; een informatiechatbot is dat meestal niet |

Scenario 5 hoort bij geen van de drie meldplichten en is toch het incident dat een wethouder het eerst uit
de krant hoort. Behandel het als klacht en als kwaliteitsincident: stop de chatbot, stel vast wie
verkeerd is geïnformeerd, en herstel het. Een toepassing voor inwoners valt onder de
transparantieplicht van de AI Act (art. 50), dus inwoners moeten al weten dat ze met AI te maken hadden.

## Wat je vooraf regelt

1. **Leg AI-incidenten vast als eigen categorie** in je incidentprocedure, met deze drie meldplichten
   erbij. De beoordeling "significant of niet" moet binnen uren kunnen, door iemand met mandaat.
2. **Zorg dat je kunt melden.** Het portaal van het NCSC werkt met eHerkenning op niveau EH2+. Regel dat
   middel voor meer dan één persoon, voordat je het nodig hebt.
3. **Zorg dat je kunt vaststellen wat er gebeurde.** Zonder logging van vragen, antwoorden, gebruikte
   bronnen en aanroepen van een agent kun je niet zeggen wie wat heeft gezien. Afspraken over wat je logt
   en hoe lang, staan in [Bewaartermijnen voor logging en forensiek](../logging-en-retentie/). Let op: logging per gebruiker
   raakt het instemmingsrecht van de ondernemingsraad.
4. **Zorg dat je de AI kunt uitzetten.** Een schakelaar per toepassing en per agent, bediend door de
   incidentcoördinator, zonder dat daar een wijzigingsverzoek voor nodig is.
5. **Leg vast wat leveranciers melden.** Bij ingekochte AI moet de leverancier een compromittering of
   ernstig incident binnen uren aan jou melden, anders haal je je eigen 24 uur niet.

## Bewijs

- De incidentprocedure met de categorie AI-incidenten en de drie meldplichten.
- Per AI-incident de afweging tegen de drempels van art. 6 lid 2 van de regeling, ook als er niet is
  gemeld, met naam en tijdstip van wie besloot.
- De eHerkenningsmiddelen voor het NCSC-portaal, met houders.
- Voor elke AI-toepassing: de schakelaar, wie hem bedient, en de laatste keer dat hij is getest.

## Hoe dit samenhangt

Dit is een aanvulling op [Incidentprocedures die je hebt geoefend](../incident-response-procedures/),
toegespitst op AI. Scenario 1 is uitgewerkt in [Open-source AI binnenhalen onder de Cbw](../open-source-ai-binnenhalen/),
scenario 4 in [Wiens bevoegdheid gebruikt een AI-agent?](../agent-bevoegdheid/). Of een gemeenschappelijke
regeling zelf onder de meldplicht valt, toets je met [Val ik onder de Cbw?](../../governance/val-ik-onder-de-cbw/).

## Bronnen

- [Cyberbeveiligingswet](https://wetten.overheid.nl/BWBR0052872/), art. 25 (significant incident) en art. 26 (vroegtijdige waarschuwing binnen 24 uur)
- [Cyberbeveiligingsregeling sector overheid](https://wetten.overheid.nl/BWBR0052963/), art. 6 (drempelwaarden)
- [Digitale Overheid, voorlopige CSIRT-dienstverlening voor gemeenten](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cyberbeveiligingswet/veelgestelde-vragen-voorlopige-csirt-dienstverlening-gemeenten-en-gemeenschappelijke-regelingen/): het NCSC vervult voorlopig de CSIRT-taak
- [AVG](https://eur-lex.europa.eu/eli/reg/2016/679/oj), art. 33 en 34
- [AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj), art. 26 lid 5, art. 50 en art. 73, met de toepassingsdata zoals gewijzigd door Verordening (EU) 2026/1744

## Licentie

[EUPL-1.2](../../LICENSE).
