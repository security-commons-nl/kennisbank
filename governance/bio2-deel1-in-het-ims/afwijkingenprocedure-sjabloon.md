# Sjabloon: procedure afwijkingen en correctieve maatregelen

> **Herkomst:** conceptprocedure van de CISO van een regionale samenwerking van gemeenten (september 2026), nog niet vastgesteld. Voor de commons generiek gemaakt; de eerste vulling van het register (echte bevindingen) is weggelaten. Norm: ISO/IEC 27001, clausule 10.1 en 10.2.

Een managementsysteem bewijst zichzelf niet in het beleid, maar in wat er gebeurt als iets niet klopt.

## 1. Wat een afwijking is, en wat niet

| Begrip | Definitie | Waar het landt |
|---|---|---|
| Afwijking (non-conformiteit) | een eis uit norm, wet, eigen beleid of contract wordt niet nageleefd, of een maatregel uit de verklaring van toepasselijkheid bestaat niet of werkt niet zoals beschreven | afwijkingenregister |
| Incident | een gebeurtenis die beschikbaarheid, integriteit of vertrouwelijkheid raakt of dreigt te raken | incidentproces; een incident kan een afwijking blootleggen |
| Risico | een mogelijke toekomstige gebeurtenis met kans en impact | risicoregister; een onbehandeld risico buiten de risicobereidheid is een afwijking |
| Verbetermogelijkheid | iets dat beter kan zonder dat een eis wordt geschonden | verbeterregister |

Twee voorbeelden. Niemand kan een hersteltest met naam en datum noemen, terwijl het beleid "maandelijks" zegt: een
afwijking, want de maatregel werkt niet zoals beschreven. De klimaatbeheersing van de serverruimte valt uit: een
incident. Blijkt daarna dat niemand eigenaar is van die randvoorwaarde: een afwijking.

## 2. Bronnen

Interne en externe audits; ENSIA en toezicht; metingen en KPI's (twee kwartalen rood zonder plan is een afwijking);
incidenten en hun evaluatie; zelfassessments; meldingen van medewerkers; leveranciersrapportages; de
directiebeoordeling. Elke bron levert aan bij de ISO, die registreert.

## 3. Rollen

| Rol | Doet |
|---|---|
| ISO (team IB&P) | registreert, kent nummer en voorlopige ernst toe, bewaakt termijnen, rapporteert |
| Eigenaar van de afwijking (de proces- of discipline-eigenaar bij wie de eis hoort) | oorzaakanalyse, correctie en corrigerende maatregel, uitvoering, gereedmelding |
| CISO | valideert de ernst bij hoog en kritiek, toetst de oorzaakanalyse, escaleert |
| Tactisch IMS-overleg | ziet elk kwartaal het register; beslist bij meningsverschil |
| Stuurgroep en directie | krijgen kritieke afwijkingen direct, de rest in de halfjaarrapportage |
| Interne accountant | toetst bij de volgende audit of de maatregel is uitgevoerd en werkt |

## 4. Zeven stappen

| Stap | Wat | Wie | Termijn |
|---|---|---|---|
| 1 Registreren | bron, datum, eis, waarneming, voorlopige ernst, eigenaar | ISO | binnen 5 werkdagen |
| 2 Beheersen | directe gevolgen beperken: gat dichten, toegang intrekken, bestand herstellen | eigenaar | direct; bij kritiek en hoog vóór stap 3 |
| 3 Oorzaak | waarom bestond de afwijking? Vijf keer waarom is genoeg; bij kritiek en hoog schriftelijk | eigenaar met ISO | binnen 4 weken (kritiek: 2 weken) |
| 4 Elders? | komt dezelfde afwijking ook op andere plekken, systemen of gemeenten voor? | eigenaar en ISO | met stap 3 |
| 5 Corrigerende maatregel | neemt de oorzaak weg; met eigenaar, datum, verwacht effect. Structurele oorzaak (geen beleid, geen eigenaar): verbeteractie en zo nodig een risico | eigenaar; CISO toetst bij kritiek en hoog | plan binnen de termijn van stap 3 |
| 6 Effect | vaststellen dat het niet terugkomt (meting, steekproef, audit); pas dan sluiten | ISO; interne accountant bij de volgende audit | binnen 3 maanden na uitvoering |
| 7 Leren | zit de oorzaak in het systeem zelf, dan het systeem bijwerken | CISO, via het tactische overleg | bij de eerstvolgende herziening |

## 5. Ernst en termijnen

De ernst volgt de klassen van het [risicomanagementbeleid](risicomanagementbeleid-sjabloon.md): kans dat de afwijking
tot een incident leidt, maal de impact daarvan.

| Ernst | Voorbeeld | Correctie | Corrigerende maatregel uitgevoerd | Melden aan |
|---|---|---|---|---|
| Kritiek | beheeraccounts zonder MFA; geen werkende back-up van een kritiek systeem; wettelijke meldtermijn gemist | uiterlijk 5 werkdagen | binnen 3 maanden | directie via de stuurgroep, direct |
| Hoog | maatregel uit de VvT bestaat niet; auditbevinding na 4 weken zonder eigenaar; KPI twee kwartalen rood | binnen 4 weken | binnen 6 maanden | stuurgroep via het tactische overleg |
| Gemiddeld | procedure niet gevolgd zonder gevolg; register niet actueel | binnen 3 maanden | binnen 12 maanden | tactisch overleg |
| Laag | documentatie niet bijgewerkt; formele afwijking zonder risico | bij de herziening | binnen 12 maanden | register |

Overschreden termijn: de ISO meldt het aan de CISO, die het agendeert. Twee keer over de termijn: de afwijking wordt
een risico in het risicoregister, met de eigenaar van de afwijking als risico-eigenaar.

## 6. Verbeterregister en verbeterplan

Naast het afwijkingenregister een verbeterregister voor verbetermogelijkheden: uit de directiebeoordeling, uit
aanbevelingen van audits, uit evaluaties, uit medewerkers. Elk item met eigenaar, verwacht effect en status.
Jaarlijks na de directiebeoordeling stelt het tactische overleg uit beide registers het **verbeterplan** op, met
eigenaar, datum en de KPI waarop het effect zichtbaar moet worden. De directie stelt het vast.

## 7. Waar het register staat

Een eigen register naast het risicoregister, met dezelfde opzet en eigenaarslogica, tot een GRC-voorziening er is.
Het servicedesksysteem blijft de bron voor incidenten en wijzigingen; een afwijking uit een incident verwijst naar
het ticketnummer. Kies je voor inrichting in het servicedesksysteem, beleg dan wie die inrichting doet en bewaakt.

## 8. Rapportage

| Wanneer | Wat | Aan wie |
|---|---|---|
| direct | nieuwe kritieke afwijking | CISO, stuurgroep, directie |
| elke vergadering | nieuwe afwijkingen, overschreden termijnen, gesloten afwijkingen | tactisch overleg |
| halfjaarlijks | totalen per klasse, bron en gemeente; doorlooptijd; openstaand over termijn | stuurgroep, directie |
| jaarlijks | trend, effectiviteit, verbeterplan | directie (directiebeoordeling) |
| jaarlijks | afwijkingen die de collegeverklaring raken | colleges (ENSIA) |

## Bijlage. Velden

**Afwijkingenregister:** nummer (AFW-jjjj-nnn) · datum constatering · bron · eis (norm, wet, beleid, contract,
VvT-nummer) · waarneming · gemeente(n) · ernst · eigenaar · correctie met datum · oorzaak · elders ja of nee ·
corrigerende maatregel met eigenaar en datum · effect vastgesteld (hoe, wanneer, door wie) · status · verwijzing
naar risico of verbeteractie.

**Verbeterregister:** nummer · bron · verbetermogelijkheid · eigenaar · verwacht effect · KPI · status · opgenomen in
verbeterplan ja of nee.
