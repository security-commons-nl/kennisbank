# Sjabloon: intern auditprogramma over drie jaar

> **Herkomst:** concept-auditprogramma van de CISO van een regionale samenwerking van gemeenten (september 2026), nog niet vastgesteld en nog niet met de interne accountant afgestemd. Voor de commons generiek gemaakt: de eigen risico's en leveranciers zijn vervangen door de logica erachter. Norm: ISO/IEC 27001, clausule 9.2.

## 1. Doel en scope

**Doel.** Directie en colleges kunnen jaarlijks op basis van onafhankelijke toetsing zeggen of het ISMS voldoet aan
ISO 27001, BIO 2.0 en de eigen eisen, en of de maatregelen werken.

**Drie lagen in scope:**

1. **Het managementsysteem:** clausules 4 tot en met 10, dus de artefacten van deel 1.
2. **De maatregelen:** de onderwerpen van deel 2, getoetst tegen ISO 27002 en de overheidsmaatregelen van BIO 2.0,
   in de scope van de verklaring van toepasselijkheid per gemeente.
3. **De keten:** de kernleveranciers, via hun assurance-rapporten en, waar het contract het toelaat, eigen toetsing.

**Buiten het programma, wel in de kalender**, zodat niets dubbel gebeurt: ENSIA en de collegeverklaringen, de IT-audit
bij de jaarrekeningcontrole, DigiD- en Suwinet-assessments, toezicht door de RDI.

## 2. Onafhankelijkheid en rollen

| Rol | Doet | Doet niet |
|---|---|---|
| Interne accountant (concerncontrol) | is auditor: plant, voert uit, rapporteert; schakelt zo nodig een externe partij in voor techniek | meebesluiten over wat hij toetst. Zit hij in het tactische overleg, dan adviseert hij niet mee bij een agendapunt dat een audit raakt, en dat wordt genotuleerd |
| CISO | levert de risico-informatie voor de prioritering; is auditee voor de eigen producten; zet bevindingen in het afwijkingenregister | auditen; de tweede lijn toetst niet zichzelf |
| Concerncontroller | eigenaar van het programma; bewaakt onafhankelijkheid en capaciteit | |
| Auditee | levert bewijs; reageert binnen 2 weken op conceptbevindingen; is eigenaar van de opvolging | de bevinding herformuleren |
| Tactisch IMS-overleg | ontvangt elk rapport; bewaakt de opvolging | |
| Directie | stelt het programma vast; ontvangt de jaarlijkse auditrapportage in de directiebeoordeling | |

**Regel voor techniek.** Een audit op de werking van technische maatregelen (toegang, patching, logging, back-up)
gebeurt door of met iemand die de systemen kan uitlezen. Heeft de interne accountant die kennis niet, dan wordt een
externe partij ingehuurd onder zijn regie. De CISO levert de meetmethode, niet het oordeel.

## 3. Diepgang: opzet, bestaan, werking

| Niveau | Vraag | Bewijs | Wanneer |
|---|---|---|---|
| Opzet | beschreven en vastgesteld? | beleid, procedure, besluit | jaar 1, voor het managementsysteem en de eerste golf van deel 2 |
| Bestaan | ingericht zoals beschreven? | configuratie, register, rolbezetting, contract | jaar 1 voor de hoogste risico's, jaar 2 breed |
| Werking | werkt het over een periode? | logs, meetreeksen, steekproeven, oefeningen | jaar 2 voor de hoogste risico's, jaar 3 breed |

Elke audit rapporteert per maatregel op welk niveau is getoetst en met welke uitkomst. Zo vult het bewijsdossier per
gemeente zich vanzelf.

## 4. Prioritering

Volgorde op risico, niet op alfabet:

1. De risico's van klasse kritiek in het register, en hun operationele tegenhangers.
2. Onderwerpen met een verlopen deadline of een lege meting: meestal back-up en herstel, logische toegang, logging,
   incidentmanagement.
3. De kernleveranciers, als een groot deel van de maatregelen bij hen ligt.
4. Het managementsysteem zelf, zodra de artefacten zijn vastgesteld: eerst opzet, dan bestaan.
5. De rest van deel 2, in de volgorde van de implementatie: een onderwerp wordt geaudit een half jaar nadat zijn
   beleid is vastgesteld en de inrichting is opgeleverd.

## 5. Kalenderpatroon

Per halfjaar twee tot drie audits, afgestemd op de beschikbare auditcapaciteit plus inhuur voor techniek. MS is
managementsysteem, D2 een onderwerp van deel 2.

| Periode | Audit | Laag | Diepgang |
|---|---|---|---|
| Jaar 1, H1 | Clausule 4, 5 en 6 (context, leiderschap, planning) | MS | opzet |
| Jaar 1, H1 | Logische toegang: beheerrechten, MFA-uitzonderingen, tijdelijke rechten, leverancierstoegang | D2 | bestaan |
| Jaar 1, H2 | Clausule 7 tot en met 10 (ondersteuning, uitvoering, evaluatie, verbetering) | MS | opzet |
| Jaar 1, H2 | Back-up en herstel, inclusief hersteltests en de cloudback-up | D2 | bestaan en werking |
| Jaar 1, H2 | Incidentmanagement en meldplicht: keten in het servicedesksysteem, melding aan het NCSC binnen 24 en 72 uur, mandaat voor containment | D2 | bestaan |
| Jaar 2, H1 | Kernleverancier beheer: beheerrechten, patching servers, wijzigingsproces, uitwijk | keten | bestaan |
| Jaar 2, H1 | Logging en monitoring: aangesloten bronnen, bewaartermijnen, rapportage van de detectiedienst | D2 | bestaan en werking |
| Jaar 2, H1 | Risicomanagement in werking: register, eigenaren, acceptaties, herbeoordelingen | MS | bestaan |
| Jaar 2, H2 | Patch- en kwetsbaarheidsbeheer, werkplek en server | D2 | werking |
| Jaar 2, H2 | Netwerkbeveiliging en segmentatie | D2 | bestaan |
| Jaar 2, H2 | Kernleverancier detectie: dienstverlening tegen het contract | keten | werking |
| Jaar 2, H2 | Bedrijfsmiddelenbeheer, classificatie en afvoer | D2 | bestaan |
| Jaar 3, H1 | Volledige cyclus in werking: doelstellingen, directiebeoordeling, verbetercyclus | MS | werking |
| Jaar 3, H1 | Cloud, veilig ontwikkelen en projecten | D2 | bestaan |
| Jaar 3, H1 | Continuïteit en uitwijk: BIA's, herstelplannen, oefening | D2 | werking |
| Jaar 3, H2 | Screening, bewustzijn, fysieke toegang, inkoop en leveranciersbeheer | D2 | bestaan |
| Jaar 3, H2 | Herhaling op de twee hoogste risico's | D2 | werking |

Na drie jaar is elke clausule twee keer getoetst en elk onderwerp van deel 2 ten minste één keer; de onderwerpen achter
de hoogste risico's twee keer.

## 6. Spelregels per audit

| Onderdeel | Afspraak |
|---|---|
| Aankondiging | 6 weken vooraf: scope, criteria, diepgang, gevraagd bewijs, auditee |
| Criteria | ISO 27001, ISO 27002, BIO 2.0, het eigen beleid; de VvT per gemeente bepaalt de scope |
| Bewijs | uit het systeem waar dat kan, met datum; een zelfverklaring is geen bewijs voor bestaan of werking |
| Bevindingen | criterium, waarneming, oorzaak, gevolg, ernst (klassen van het risicomanagementbeleid), aanbeveling, auditee |
| Wederhoor | auditee reageert binnen 2 weken op de feiten, niet op het oordeel |
| Rapport | binnen 4 weken aan auditee, CISO, tactisch overleg en concerncontroller; samenvatting in de halfjaarrapportage |
| Opvolging | elke bevinding in het [afwijkingenregister](afwijkingenprocedure-sjabloon.md); de auditor toetst de opvolging bij de volgende audit op hetzelfde onderwerp |
| Dossier | per audit een dossier; per gemeente een verwijzing in het bewijsdossier |

## 7. Vóór vaststelling

1. Afstemmen met de interne accountant: kalender, capaciteit, inhuur voor techniek, rolzuiverheid in het tactische overleg.
2. Afstemmen met de ENSIA-coördinatie, zodat een proceseigenaar niet twee keer in een kwartaal bewijs levert.
3. Aansluiten op de implementatieplanning van deel 2: schuift een onderwerp, dan schuift de audit mee.
4. Vaststelling door de directie, met de eerste auditrapportage in de directiebeoordeling van jaar 1.
