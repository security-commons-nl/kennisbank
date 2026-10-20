# De KPI-matrix: opzet, bestaan en werking per domein

> **Herkomst:** KPI-definities van het geïntegreerde managementsysteem van een regionale samenwerking van gemeenten, versie 0.2 (juli 2026). Voor de commons generiek gemaakt; de aantallen maatregelen zijn die van de bron en moet je vervangen door die van je eigen normenkader.

## Structuur

Drie domeinen maal drie fasen is negen KPI's.

| Domein | Normenkader | Noemer in de bron |
|---|---|---|
| Veiligheid (ISMS) | BIO 2.0 / ISO 27001 | de toepasselijke BIO-maatregelen |
| Privacy (PIMS) | AVG / ISO 27701 | ongeveer 40 kernverplichtingen uit de AVG (de volledige set wordt beheerd, niet op KPI-niveau gerapporteerd) |
| Continuïteit (BCMS) | ISO 22301 | de BCM-maatregelen uit de eigen set |

| Fase | Vraag | In één woord |
|---|---|---|
| Opzet | Is er een maatregel ontworpen die het risico afdekt? | Bedacht? |
| Bestaan | Bestaat de maatregel in de praktijk? | Is het er? |
| Werking | Werkt de maatregel aantoonbaar? | Doet het wat het moet? |

Beleid telt niet als eigen fase. Of er beleid is, is een randvoorwaarde die je kwalitatief duidt in het
operationele beeld en de expert views.

## De negen cellen

| ID | Cel | Meting | Bron | Eigenaar |
|---|---|---|---|---|
| SEC-1 | Opzet veiligheid | Aantal maatregelen met een gedocumenteerde beschrijving (wie, wat, wanneer, hoe), gedeeld door het totaal | Maatregelenbibliotheek, interne controlecyclus in het servicedesksysteem | Discipline-eigenaar ISMS |
| SEC-2 | Bestaan veiligheid | Aantal ontworpen maatregelen met bewijs van implementatie, gedeeld door het aantal ontworpen | Bewijsregistratie, self-assessments, configuraties | Discipline-eigenaar ISMS |
| SEC-3 | Werking veiligheid | Aantal geïmplementeerde maatregelen met een positief toetsresultaat, gedeeld door het aantal geïmplementeerde | Audits, pentests, ENSIA, monitoring | Discipline-eigenaar ISMS en interne auditor |
| PRI-1 | Opzet privacy | Aantal kernverplichtingen met een gedocumenteerde maatregel, gedeeld door het totaal | Maatregelenbibliotheek, procesbeschrijvingen | Privacy officer |
| PRI-2 | Bestaan privacy | Aantal ontworpen maatregelen met bewijs van bestaan, gedeeld door het aantal ontworpen | Register van verwerkingen, DPIA-dossiers, verwerkersovereenkomsten, datalekregister | Privacy officer |
| PRI-3 | Werking privacy | Aantal bestaande maatregelen met een positief toetsresultaat, gedeeld door het aantal bestaande | Expert view FG, privacy-audit, datalekanalyse | Privacy officer en FG |
| BCM-1 | Opzet continuïteit | Aantal BCM-maatregelen met een gedocumenteerde maatregel (BIA, herstelplan, uitwijk), gedeeld door het totaal | BIA's, herstelplannen, uitwijkprocedures | BCM-manager |
| BCM-2 | Bestaan continuïteit | Aantal ontworpen maatregelen met bewijs van bestaan | Back-upconfiguraties, SLA's, uitwijklocaties | BCM-manager |
| BCM-3 | Werking continuïteit | Aantal bestaande maatregelen met een positief testresultaat (oefening, test, echte inzet) | Oefenverslagen, testresultaten, lessen na incidenten | BCM-manager |

## Meetregels

**Score.** Elke cel is een percentage, of **onbekend**. Onbekend betekent: te weinig data voor een betrouwbare
score. Dat is een governance gap en wordt nooit als nul weergegeven. Een cel kan ook een **inschatting** zijn,
gebaseerd op expert judgement in plaats van data; dat wordt expliciet gemarkeerd.

**Wanneer telt een maatregel mee?**

| Fase | Telt mee als |
|---|---|
| Opzet | er een gedocumenteerde beschrijving is (wie, wat, wanneer, hoe) |
| Bestaan | er bewijs is dat de maatregel is geïmplementeerd (configuratie, proces, registratie) |
| Werking | er een toetsresultaat is (audit, test, review) dat aantoont dat de maatregel effectief is |

**Cascade.** Bestaan is nooit hoger dan opzet: je kunt niet hebben wat niet is ontworpen. Werking is nooit hoger
dan bestaan: je kunt niet testen wat er niet is.

**Geen totaalscore.** Er wordt niet geaggregeerd naar één score per domein of één IMS-cijfer. Het doel is
transparantie per fase, niet één getal.

**Kleuren en trend.** Rood onder 40%, oranje 40 tot 70%, groen boven 70%, grijs onbekend. Trend: hoger, lager,
stabiel, of n.v.t. bij de eerste meting. Stem de drempels af in het tactische overleg en evalueer ze na de
eerste meting.

## Dataverzameling bij de eerste meting

| Cellen | Methode | Verwachte kwaliteit |
|---|---|---|
| Opzet | Review van de interne controlecyclus en expert judgement | Matig, niet alles is gedocumenteerd |
| Bestaan | Self-assessment door de discipline-eigenaren | Laag, geen structurele bewijsregistratie |
| Werking | Inventaris van bestaande audits, tests en oefeningen | Zeer laag |

Werkwijze: (1) opzetscan per maatregel, (2) inschatting bestaan ja, nee of onbekend, (3) inventaris van
toetsresultaten, (4) consolidatie tot de negen cellen door de CISO.

Een realistische eerste meting in de bron: opzet veiligheid 40 tot 65%, bestaan grotendeels onbekend, werking
onder 20% of onbekend; privacy en continuïteit lager. Dat is geen falen; het is het startpunt.

## Groeipad

| | Eerste meting | Tweede halfjaar | Daarna |
|---|---|---|---|
| Opzet | Controlecyclus en expert judgement | Maatregelenbibliotheek met de kernmaatregelen gevuld | Volledig uit het canonieke model |
| Bestaan | Self-assessment | Eerste bewijsuploads | Geautomatiseerde bewijsregistratie |
| Werking | Inventaris bestaande tests | Eerste effectiviteitstoetsen | Structureel testprogramma |
| Datakwaliteit | Laag | Matig | Hoog |

**Streefwaarden.** Zonder streefwaarden kun je tussentijds niet sturen. Stel ze per halfjaar vast in het
tactische overleg, bijvoorbeeld opzet veiligheid 50% na een half jaar en 80% na een jaar. Een cel onder de
streefwaarde is geen falen maar een stuursignaal.

**Per cluster.** Wil je sturen op organisatieonderdelen, registreer dan bij de dataverzameling de bron per
cluster. De rapportage verandert niet; het wordt een extra doorsnede.
