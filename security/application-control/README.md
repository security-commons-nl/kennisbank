---
titel: Application- en scriptcontrol
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: patroon uit de security-shop-catalogus van security-commons-nl, herschreven als handleiding
status: concept
samenvatting: Alleen toegestane software en scripts laten draaien, met een trustmodel in plaats van een uitzonderingenlijst. Verdieping op de werkplekanalyse: eerst meten wat er draait, dan afdwingen. Met de auditfase, de uitrol en het bewijs van dekking.
barrieres: [execution]
rol: verdieping
---

# Application- en scriptcontrol

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/application-control](https://security-commons-nl.github.io/kennisbank/security/application-control/)

> **Barriere:** beperk software- en scriptuitvoering met application control en ASR. Alleen vooraf goedgekeurde software en scripts mogen draaien, willekeurige binaries en PowerShell-scripts zijn standaard geblokkeerd.

Werkplekken kunnen vrijwel elke binary of script uitvoeren. ClickFix, infostealers en ransomware leunen daar volledig op: zodra de gebruiker het uitvoert, gaat het draaien. Detectie achteraf is dan al te laat.

## Wanneer wel, wanneer niet

Past in volwassen organisaties die changemanagement op de werkplek aankunnen. Wanneer niet zonder grondige inventarisatie van wat er draait, een te strakke allowlist breekt werkprocessen en wordt direct teruggedraaid.

## Zo richt je het in

Een allowlist-mechanisme (zoals Windows Defender Application Control of vergelijkbaar) blokkeert alle uitvoerbare bestanden die niet expliciet zijn toegestaan. Scripts kunnen via Constrained Language Mode of script-handtekeningen beperkt worden. Uitzonderingen lopen via een beheerd proces.

1. Inventariseer de software die op werkplekken draait, per afdeling indien nodig.
2. Stel de allowlist op (ondertekenende uitgever, hash of pad).
3. Begin in audit-mode: log wat zou worden geblokkeerd zonder daadwerkelijk te blokkeren.
4. Analyseer de logs, vul de allowlist aan, herhaal.
5. Schakel handhaving in, eerst per pilot-afdeling, dan organisatiebreed.
6. Beleg een snel afhandelingsproces voor nieuwe toepassingen.

## Wat het kost en wat het oplevert

Kosten: midden.

**Wat het oplevert**

- Onbekende malware kan niet draaien, preventie in plaats van alleen detectie.
- ClickFix en script-gebaseerde aanvallen worden direct gestopt.
- Maakt zichtbaar wat er feitelijk op werkplekken draait.

**Waar je op moet letten**

- Inrichtings- en onderhoudslast is fors, software-landschap veranderingen vragen onderhoud.
- Vraagt cultuur die niet 'even iets installeren' verwacht.
- Te strak ingericht breekt werkprocessen en leidt tot terugdraaien.

## Bewijs

- De application-controlconfiguratie met per regelset of hij in audit- of in afdwingstand staat.
- De dekking: op hoeveel apparaten geldt het beleid, van hoeveel in totaal.
- De bevindingen uit de auditfase: wat zou er geblokkeerd zijn, en wat is daarmee gedaan.
- De uitzonderingen met hun reden en termijn.

## Zo leg je het uit

**Aan de directie.** De meeste aanvallen leunen op het feit dat alles kan draaien op een werkplek. Door alleen vooraf goedgekeurde software toe te staan, breken we die afhankelijkheid. Vraagt discipline, levert structurele preventie.

**Aan de informatiemanager.** Geïntegreerd in het werkplekbeheer; vraagt een proces voor het beoordelen van nieuwe applicaties.

**Aan het MT.** Gebruikers kunnen niet zomaar nieuwe software installeren. Een snel, voorspelbaar uitzonderingsproces is essentieel om frustratie en schaduw-IT te voorkomen.

## Hoe dit samenhangt

Deze handleiding hoort bij barriere `execution` uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/). Wat je hiermee aantoont in BIO 2.0, NIST CSF, het Wpg-kader en de AVG staat op [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/).

Doe eerst [Werkplekanalyse op het Microsoft-platform](../werkplekanalyse-e5/): zonder te meten wat er draait, breek je legitiem werk.

## Licentie

[EUPL-1.2](../../LICENSE).
