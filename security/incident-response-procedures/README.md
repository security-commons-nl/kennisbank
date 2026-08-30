---
titel: Incidentprocedures die je hebt geoefend
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Vastgelegde en geoefende procedures voor de incidenttypen die je het vaakst treffen: een overgenomen account, een phishing- of BEC-melding, en misbruik van een externe kwetsbaarheid. Met de rollen, de escalatie en de oefenverslagen als bewijs dat er echt gehandeld wordt.
barrieres: [mailresponse, idresponse, exploitresponse]
rol: fundering
---

# Incidentprocedures die je hebt geoefend

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/incident-response-procedures](https://security-commons-nl.github.io/kennisbank/security/incident-response-procedures/)

> **Barriere:** test mail-remediation en het phishing/BEC-playbook; test response op identity- en app-compromise; test detectie en response op externe exploits. Een vastgelegd, geoefend incident response-proces, wie doet wat, op welk moment, met welke bevoegdheden, voor de eerste 24 uur en daarna.

Een incident is geen procedure waard tot het er is, maar dan is het te laat. Zonder vastgelegd proces is de eerste reactie ad-hoc: meldingen blijven hangen, escalaties komen laat, juridische- en AP-meldplichten worden gemist.

## Wanneer wel, wanneer niet

Altijd nodig, geen organisatie zonder digitale dienstverlening kan zonder. Wanneer niet zonder oefenen: een proces op papier dat niemand kent werkt niet onder druk.

## Zo richt je het in

Een gedocumenteerd proces beschrijft de fases (detectie → triage → containment → eradicatie → herstel → lessons learned), de rollen, mandaten, escalatieroutes en externe meldplichten (AP, NCSC, leveranciers). Tabletop-oefeningen valideren het proces.

1. Documenteer de fases en de rolverdeling per fase (RACI).
2. Beleg mandaten: wie mag isoleren, wie mag publiceren, wie mag escaleren.
3. Leg externe meldplichten vast met deadlines (AP binnen 72 uur, NCSC, NIS2).
4. Stel runbooks op voor de meest waarschijnlijke incidenten (ransomware, datalek, AiTM).
5. Oefen het proces met een tabletop (zie het tabletop-patroon).
6. Update na elk oefen- of echt incident.

## Wat het kost en wat het oplevert

Kosten: laag.

**Wat het oplevert**

- Onder druk hebben mensen iets om op terug te vallen, geen ad-hoc.
- Meldplichten worden gehaald, juridisch risico beperkt.
- Lessons learned voeden structurele verbetering.

**Waar je op moet letten**

- Een proces dat niemand kent en niet wordt geoefend is alleen papier.
- Vereist eigenaarschap; zonder vaste IR-rol verzandt het.
- Externe deadlines (72 uur AP) zijn niet inhaalbaar, voorbereiding is voorwaarde.

## Bewijs

- De playbooks per incidenttype, met wie wat doet en binnen welke tijd.
- Voor identity-compromise: dat sessies kunnen worden ingetrokken, accounts geblokkeerd en schadelijke apps verwijderd, met een testverslag.
- Voor phishing en BEC: automatische remediation van al afgeleverde berichten, en de verificatie van betaal- en rekeningwijzigingen.
- Voor externe exploits: een test waaruit blijkt dat detectie en response werken.
- De oefenverslagen met de gemeten doorlooptijden.

## Zo leg je het uit

**Aan de directie.** Een crisis komt nu, het proces moet er al zijn. Het IR-proces legt vast wie wat doet, met welke mandaten en deadlines. Tijdens een incident is geen tijd om het uit te denken.

**Aan de informatiemanager.** Vraagt afstemming met juridisch, communicatie, IT-beheer en de IB-functie. Externe meldplichten komen in het proces; runbooks per scenario.

**Aan het MT.** Lijnverantwoordelijken krijgen rollen binnen het proces. Eenmalige instructie en jaarlijkse oefening houden het levend.

## Hoe dit samenhangt

Deze handleiding hoort bij de barrieres `mailresponse`, `idresponse`, `exploitresponse` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

Deze handleiding dekt drie barrieres tegelijk, omdat de procedures dezelfde zijn en alleen het scenario verschilt. De organisatievorm eromheen staat in [Een blue team opzetten](../blue-team-opzetten/).

## Licentie

[EUPL-1.2](../../LICENSE).
