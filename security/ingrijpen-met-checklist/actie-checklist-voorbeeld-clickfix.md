# Actie-checklist, ingevuld voorbeeld: ClickFix

| Interventieteam — actie-checklist (vóór T-0) |  |
|---|---|
| Doel | Eén vaste vragenlijst die het kernteam vóór elke actie van het interventieteam langsloopt, zodat 2L ([naam]) en 3L ([naam]) zien dat de relevante afwegingen op tafel hebben gelegen — zonder dat zij elke meeting hoeven bij te wonen. |
| Hoe gebruiken | Kopieer dit bestand naar de actie-map (Acties/<naam-actie>/checklist.md) en vul per punt het antwoord in. Geen antwoord beschikbaar = expliciet "nog open + eigenaar + deadline" noteren, niet leeg laten. |
| Wanneer | Vóór T-0. Bij hoge urgentie kunnen sommige punten ná T-0 worden ingevuld; markeer dat dan expliciet ("post-T-0 vastgelegd op [datum]"). |
| Herkomst | Vragenlijst opgesteld door [naam] (2L, concernadviseur risicomanagement) op 4 mei 2026, aangevuld met punten uit de eigen werkwijze van het interventieteam (plan van aanpak, protocol mandaat en actie, leerpuntenlijst). |

| Dreiging en impact |  |
|---|---|
| Aanleiding — welke kwetsbaarheid of dreiging? | ClickFix is een social engineering + execution attack pattern waarbij gebruikers worden verleid om zelf malafide code uit te voeren (bijv. via PowerShell, osascript of bash). Kern-TTP’s: Fake CAPTCHA / “You’re not a robot” Kopiëren/plakken van commandos door gebruiker Misbruik van: - Win+R / PowerShell - File Explorer (FileFix-variant) - search-ms protocol (nieuwe variant) Verspreiding via: Phishing e-mail Gecompromitteerde websites Lookalike domeinen |
| Actief misbruik — bewijs? | ClickFix wordt aantoonbaar actief misbruikt. Recent is gemeente Epe slachtoffer geworden van een dergelijk aanval. https://www.epe.nl/datalek-gemeente-epe Binnen de gemeente VOORBEELDGEMEENTE zijn geen gevallen bekend van een dergelijke aanval. |
| Geraakt gebied — welke kroonjuwelen of kritieke processen lopen risico? | Concreet: welke applicatie, welk dienstverleningsproces, welke gegevens. Vermeld waar onbekend. Elke applicatie die wordt gebruikt, loopt een risico. |
| Business impact — wat gebeurt er als het misloopt? | Downtime-orde-grootte, betrokken inwoners/medewerkers, juridische/financiële/reputationele consequenties. Onderscheid kwalitatief (waar) en kwantitatief (orde-grootte) waar mogelijk. |

| Aanpak en mandaat |  |
|---|---|
| Bestaande maatregelen — wat staat er nu en waarom volstaat dat niet? | Niet "we hebben niets" — meestal staan er wel maatregelen, maar zijn ze ontoereikend. Benoem welke en waarom ze hier falen. |
| Voorgestelde aanpak — wat doen we, in welke fasering? | Volgorde van stappen, scope (welke systemen/gebruikers), wat wel en wat niet. |
| R/E/C-score — voorlopig en definitief, met onderbouwing per dimensie. | Bron: de R/E/C-rubriek. Niet alleen kleur — ook waarom Reversibel/Explosief/Containment-criteria zo gescoord. |
| Mandaat-niveau — 1, 2 of 3 conform PvA §4d? | Wie is beslisser? Wie wordt geïnformeerd? Welke timing-eisen (T-X, T+1u, T+2u, T+24u)? Bron: het plan van aanpak §4d. |
| Buiten reguliere route? — op welke mandaat-grond? | Loopt deze actie via §4a-bevoegdheid (buiten change-venster, dienst tijdelijk afsluiten, externe partij raadplegen) of via reguliere change met prioriteit van het interventieteam? Beide zijn legitiem — onbewust mengen niet (zie de leerpuntenlijst). |
| Containment | NVT |

| Veiligheid van de actie zelf |  |
|---|---|
| Roll-back — wie, hoe snel, getest door wie? | Concreet: bediener (primair + back-up), terugschakel-tijd, SLA met uitvoerende partij. Bij A-keuzes zonder pilot: roll-back-procedure móet vóór T-0 daadwerkelijk gedraaid zijn — niet alleen op papier (zie de leerpuntenlijst). |
| Termijn — wanneer T-0, wanneer eindstand? | Doorlooptijd inclusief eventuele audit-mode-periode en CAB-cyclus. |
| Pilot of brede uitrol — bewuste keuze + onderbouwing. | Bij brede uitrol zonder pilot: roll-back is enige veiligheidsklep — extra eisen. |

| Stakeholders en communicatie |  |
|---|---|
| Stakeholders ingelicht — bestuurlijk, operationeel, externen, wanneer? | Loop het communicatieplan §3 doelgroepen-matrix langs en markeer voor deze actie wat status is per groep. Open punten: eigenaar + deadline. |
| Externe afstemming — leveranciers, ketengemeenten, NCSC/IBD? | Welke externen geraakt? Wie heeft de afstemmingen? Bevestiging gehad? |
| Communicatieplan gebruikers — intranet, intranet, FAQ. | Wat ligt klaar? De vaste communicatieadviseur van het interventieteam heeft de tekst gezien? De servicedesk op de hoogte? |

| Vastlegging en evaluatie |  |
|---|---|
| Besluitenregister — wie schrijft wat? | de teammanager informatiebeveiliging conform protocol §6 (T+24u). Welke besluiten zijn al genomen die hierin moeten? |
| Leerpunten — wat willen we onthouden voor volgende actie? | Wat is uniek aan deze actie? Toevoegen aan de leerpuntenlijst na T-0. |
| Post-T-0 evaluatie — wanneer en met wie? | Er is nog geen termijn afgesproken, “learn as you go” voor ClickFix. Evaluatie inplannen aan het einde van de cyclus. |
