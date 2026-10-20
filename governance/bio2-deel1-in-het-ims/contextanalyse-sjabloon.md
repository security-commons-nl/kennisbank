# Sjabloon: contextanalyse en belanghebbenden

> **Herkomst:** opbouw van de concept-contextanalyse van de CISO van een regionale samenwerking van gemeenten (september 2026), nog niet vastgesteld. De inhoud van de regio (dreigingsbeeld, volwassenheid, SWOT) is weggelaten; wat blijft is de opbouw, het wettelijk kader en de belanghebbenden die voor elke gemeente gelden. Norm: ISO/IEC 27001, clausule 4.1 en 4.2.

Dit stuk beantwoordt twee vragen: in welke omgeving werkt de organisatie (4.1), en wie stelt eisen aan haar
informatiebeveiliging (4.2). Houd het feitelijk: elke bewering met een bron, elke meting met een datum. Oordelen en
adviezen apart gemarkeerd.

| | |
|---|---|
| Versie | «versie, status, datum» |
| Opsteller | «CISO» |
| Vaststeller | «één vaststeller voor het geheel; twee voor één document is onnodig» |
| Herziening | jaarlijks vóór de directiebeoordeling, en bij een wijziging in wet, organisatie of scope |

## 1. Wie de organisatie is

«Gemeente of samenwerking, wie voert wat uit voor wie, de gedeelde infrastructuur, de omvang.»

## 2. Externe factoren

### 2.1 Wettelijk kader

- **Cyberbeveiligingswet**, in werking sinds 15 augustus 2026. De Cyberbeveiligingsregeling sector overheid maakt de
  normen hard:
  - **artikel 3:** de essentiële entiteit past ISO/IEC 27001 toe op het managementsysteem en op het vaststellen van
    het toepassingsgebied. Deze contextanalyse en het scopedocument zijn daarmee wettelijk verplicht;
  - **artikel 5, eerste lid:** ten minste de maatregelen van ISO/IEC 27002 (behalve 5.32 en 5.34) en de relevante
    overheidsmaatregelen van BIO 2.0;
  - **artikel 5, derde lid:** opzet, bestaan én werking zijn aantoonbaar;
  - **bijlage 2:** de impactniveaus voor decentrale overheden; een systeem is cruciaal als het op één categorie
    hoog of zeer hoog scoort.
- **Registratie- en meldplicht** bij het NCSC, toezicht door de RDI. Zie
  [De Cbw-meldplicht inrichten](../cbw-meldplicht-inrichten/).
- AVG en UAVG (Autoriteit Persoonsgegevens; de FG is toezichthoudend), Wet politiegegevens (boa's), Woo,
  Archiefwet, en de ENSIA-verantwoording.
- De Wwke geldt voor gemeenten niet rechtstreeks; zie [Valt een gemeente onder de Wwke?](../val-ik-onder-de-wwke/).

### 2.2 Dreigingsbeeld

«Dreigingsbeeld uit NCSC, IBD en eigen incidenten, met bron en datum.»

### 2.3 Ketens en leveranciers

«De kernleveranciers en wat er bij hen ligt.»

### 2.4 Technologie en markt

«Cloud, AI, soevereiniteit, wat verandert.»

## 3. Interne factoren

«Volwassenheid (met de meting en de datum), beleid en documentatie (wat is vastgesteld, wat concept), mensen,
capaciteit en cultuur, en een SWOT.»

## 4. Belanghebbenden en hun eisen

Per belanghebbende: wat die verwacht, waar dat staat, en of het ISMS de eis adresseert. "Deels" en "nee" zijn
expliciete keuzes die het scopedocument bevestigt.

| Nr | Belanghebbende | Soort | Eis of verwachting | Bron | In het ISMS |
|---|---|---|---|---|---|
| 1 | College(s) van B en W | bestuurlijk | aantoonbaar voldoen aan Cbw en BIO 2.0; inzicht in restrisico's; persoonlijke verantwoordelijkheid kunnen dragen; ENSIA-verklaring | Cbw, regeling, ENSIA | «ja, deels, nee» |
| 2 | Gemeenteraad | bestuurlijk | verantwoording over incidenten en risico's; kaderstelling | Gemeentewet, ENSIA | |
| 3 | Directieteam | intern | in control zijn; één risicobeeld; strategische ISMS-producten vaststellen | IMS-handboek | |
| 4 | Gemeentesecretarissen van partnergemeenten (bij een samenwerking) | bestuurlijk | weten wat de uitvoerende gemeente namens hen doet; werkafspraken over detectie, melding en bewijs | dienstverleningsovereenkomst | |
| 5 | Rijksinspectie Digitale Infrastructuur | toezicht | opzet, bestaan en werking aantoonbaar; toepassingsgebied vastgesteld; registratie actueel | regeling, artikel 3 en 5 | |
| 6 | NCSC | toezicht en keten | tijdige melding van significante incidenten; actuele contact- en netwerkgegevens | Cbw | |
| 7 | Autoriteit Persoonsgegevens en de FG | toezicht | rechtmatige verwerking; meldplicht datalekken; DPIA's | AVG, UAVG | |
| 8 | Inwoners en ondernemers | extern | beschikbare loketten; bescherming van hun gegevens; transparantie bij incidenten | AVG, Woo, dienstverleningsnormen | |
| 9 | Medewerkers en de OR | intern | werkbare regels; duidelijke verantwoordelijkheden; afspraken over simulaties en monitoring | Wet op de ondernemingsraden | |
| 10 | Lijnmanagement en proceseigenaren | intern | weten welk risico van hen is en wat acceptabel is; niet verrast worden | IMS-handboek | |
| 11 | Kernleveranciers (beheer, detectie) | leverancier | duidelijke opdracht; één wijzigingsproces; afspraken over beheerrechten, logbronnen en mandaat | contracten | |
| 12 | Interne en externe accountant | toetsing | toetsbare beheersing; opvolging van bevindingen | verslag van bevindingen | |
| 13 | Gemeenschappelijke regelingen | keten | duidelijke verdeling: wie meldt, wie registreert | Cbw | |
| 14 | Veiligheidsregio | keten | aansluiting van digitale crisisbeheersing op de crisisorganisatie | crisisplan | |
| 15 | VNG en IBD | kennisnetwerk | gebruik van landelijke kaders in plaats van eigen varianten | handreikingen | |

## 5. Eisen die uit de context volgen

De eisen waaraan het ISMS moet voldoen: input voor toepassingsgebied, beleid, risicoanalyse en verklaring van
toepasselijkheid. Voor een samenwerking van gemeenten gelden er vaak deze tien:

1. Eén ISMS voor alle gemeenten, met per gemeente een eigen verklaring van toepasselijkheid die zegt welke
   maatregelen bij de uitvoerende gemeente liggen en welke bij de gemeente zelf.
2. Het toepassingsgebied is expliciet vastgesteld (artikel 3 van de regeling).
3. Opzet, bestaan en werking per maatregel aantoonbaar, met een bewijsdossier per gemeente en metingen met datum.
4. Elk risico heeft een eigenaar in de lijn; elk ISMS-product een trekker en een vaststeller.
5. De risicobereidheid is vastgesteld en reproduceerbaar: impactschalen uit bijlage 2, klassegrenzen door de directie.
6. Leveranciersafhankelijkheid is beheerst: register, eigenaar per leverancier, afspraken over beheerrechten,
   logbronnen en meldtermijnen, een exitmogelijkheid.
7. De meldplicht werkt binnen de wettelijke termijnen voor alle gemeenten, met een belegd mandaat voor containment.
8. De werkafspraken met de partnergemeenten staan in de dienstverleningsovereenkomst of een module daarvan.
9. Het ISMS is niet persoonsafhankelijk: kennis, toegang en rollen hangen aan functies, niet aan personen.
10. Landelijke kaders gaan voor eigen schrijfwerk.

## 6. Besluiten die dit stuk nodig heeft

«Bijvoorbeeld: het toepassingsgebied; werkafspraken met partnergemeenten; eigenaar per strategisch risico; trekker
per ISMS-product; de vaststeller van dit stuk.»
