# Sjabloon: doelstellingen en KPI-set voor het ISMS

> **Herkomst:** concept-doelstellingen en KPI-set van de CISO van een regionale samenwerking van gemeenten (september 2026), nog niet vastgesteld. Voor de commons generiek gemaakt: de nulmetingen van de regio zijn weggelaten, omdat ze de beveiligingsstand van een echte organisatie beschrijven. Norm: ISO/IEC 27001, clausule 6.2 en 9.1.

De set heeft twee niveaus: acht bestuurlijke indicatoren voor directie en college, en daaronder meetpunten per
onderwerp die uit een systeem komen. Deze set staat naast de [KPI-matrix van de IMS-rapportage](../ims-rapportage/kpi-matrix.md):
die meet opzet, bestaan en werking van alle maatregelen; deze set meet of de organisatie de gekozen doelen haalt.

## 1. Vijf doelstellingen

Leid de doelstellingen af uit de contextanalyse en de strategische risico's. Een voorbeeld dat voor veel gemeenten past:

| Nr | Doelstelling | Waarom |
|---|---|---|
| D1 | Elk risico en elk ISMS-product heeft een eigenaar | zonder eigenaar werkt niets in het managementsysteem |
| D2 | Het managementsysteem draait één volledige PDCA-cyclus | de Cbw eist opzet, bestaan én werking |
| D3 | Beheerrechten en toegang zijn onder controle | de snelste route van een aanvaller loopt via beheerders zonder MFA en met permanente rechten |
| D4 | De basishygiëne op werkplek, server en cloud is aantoonbaar op orde | het gereedschap staat vaak uit terwijl het betaald is |
| D5 | Herstel is bewezen, niet gekocht | een back-up zonder hersteltest is een aanname |

## 2. Acht bestuurlijke indicatoren

| Nr | Indicator | Nulmeting | Doel | Doelstelling |
|---|---|---|---|---|
| K1 | Strategische risico's met een eigenaar en een behandelplan | «aantal van totaal, datum, bron» | alle met eigenaar binnen een kwartaal; alle met plan binnen twee | D1 |
| K2 | ISMS-producten van deel 1 met een trekker, en vastgesteld door de aangewezen vaststeller | | | D1, D2 |
| K3 | Tactisch beleid door een gremium vastgesteld | | de eerste golf van deel 2 | D2 |
| K4 | Kritieke processen met vastgestelde eigenaar, en hun applicaties met BIV, RTO en RPO in de architectuurtool | | 100% | D1, D5 |
| K5 | Beheeraccounts buiten de MFA-eis, en permanent actieve bevoorrechte rollen | | 0 uitzonderingen; permanent actief hooguit 10%; een klein aantal globale beheerders, waarvan twee noodaccounts | D3 |
| K6 | Kritieke kwetsbaarheden met een patch die langer dan 60 dagen beschikbaar is, werkplek en server | | 0, en alle servers meetbaar | D4 |
| K7 | Beheerde mobiele apparaten en versleutelde werkplekken | | mobiel 90% beheerd; werkplek 100% versleuteld met sleutel centraal opgeslagen | D4 |
| K8 | Hersteltests uitgevoerd en geslaagd, per kwartaal, op een kritiek systeem | | vier per jaar met verslag, naam en datum; elk kritiek systeem minstens eens per jaar | D5 |

**Leesregel voor het bestuur.** K1 en K2 zeggen of het managementsysteem bestaat. K5 tot en met K8 zeggen of de
organisatie veiliger wordt. Bewegen K1 en K2 niet, dan bewegen de andere zes ook niet, want niemand is er dan van.

## 3. Meetpunten per onderwerp

Per onderwerp van deel 2 een of twee meetpunten uit een systeem. Dit is de bron onder de indicatoren.

| Onderwerp | Meetpunt | Bron (voorbeeld) | Hoe vaak |
|---|---|---|---|
| Bedrijfsmiddelenbeheer | applicaties in het servicedesksysteem en in de architectuurtool, en het verschil; kritieke applicaties met eigenaar | assetregistratie, architectuurtool | kwartaal |
| Informatieclassificatie | gepubliceerde gevoeligheidslabels; actieve DLP-regels; applicaties met BIV-vulling | compliance-portaal, architectuurtool | kwartaal |
| Cryptografie | verlopen certificaten en app-geheimen; VPN-tunnels met verouderde instellingen | identiteitsplatform, certificaatinventaris, firewallexport | kwartaal |
| Afvoer en hergebruik | wipes gestart, afgerond, mislukt; apparaten hergebruikt zonder wipe-spoor | apparaatbeheer, servicedesksysteem | kwartaal |
| Cloud | abonnementen met eigenaar; cloudbeveiliging aan; SaaS met verwerkersovereenkomst | cloudportaal, register | kwartaal |
| Logische toegang | K5, plus accounts zonder verloopdatum; laatste toegangsreview | identiteitsplatform, directory-export | maand |
| Fysieke toegang | passen ingetrokken bij uitdiensttreding binnen een werkdag | toegangssysteem, uitdienstsjabloon | kwartaal |
| Patchbeheer | K6, plus mediane tijd tot patch voor kritiek | kwetsbaarheidsbeheer, update-rapportage | maand |
| Wijzigingsbeheer | spoedwijzigingen als aandeel; wijzigingen met CAB-akkoord | servicedesksysteem | kwartaal |
| Netwerkbeveiliging | firewallregels met "any"; segmenten; zicht op verkeer binnen het netwerk | firewallexport, detectiedienst | kwartaal |
| Veilig ontwikkelen | repositories met branch protection en secret scanning | codeplatform | kwartaal |
| Mobiele apparaten | K7 | apparaatbeheer | maand |
| Incidentmanagement | open beveiligingsmeldingen en doorlooptijd; meldingen aan het NCSC binnen 24 en 72 uur | servicedesksysteem, meldregister Cbw | maand |
| Logging en monitoring | aangesloten bronnen; ingestie; bewaartermijn | SIEM | maand |
| Back-up en herstel | K8, plus laatste geslaagde back-up per kritiek systeem; onveranderbaar ja of nee | back-upplatform | maand |
| Continuïteit | BIA's met eigenaar; herstelplannen geaccordeerd; oefeningen per jaar | BCM-werkmap | halfjaar |
| Screening en bewustzijn | afgeronde e-learning; klikpercentage phishing-simulatie (na afspraak met de OR) | leerplatform, simulatie | halfjaar |
| Inkoop en contracten | aanbestedingen met IB-eisen; contracten met verwerkersovereenkomst | inkoopdossiers, contractregister | halfjaar |
| Leveranciersbeheer | leveranciers met eigenaar; uitgevoerde beoordelingen | leveranciersregister | halfjaar |
| Projecten | projecten met IB-toets vóór de start; DPIA's vóór ingebruikname | projectportfolio, DPIA-register | kwartaal |
| Beleid | K3 | beleidsbibliotheek | halfjaar |
| Compliance | auditbevindingen over termijn; afwijkingen in het register | [afwijkingenregister](afwijkingenprocedure-sjabloon.md) | kwartaal |

Meetpunten waarvan de bron nog niet toegankelijk is of nog niet bestaat, staan er bewust in. De eerste meting is
dan "bron ontbreekt", en dat is zelf een bevinding.

## 4. Meetplan

| Onderdeel | Afspraak |
|---|---|
| Wie meet | de eigenaar van het meetpunt levert; de ISO verzamelt; de CISO toetst een steekproef op de bron |
| Hoe | uit het systeem, met export of query en datum; per meting hetzelfde nummer, zodat de delta zichtbaar is |
| Waar het landt | maandcijfers bij de ISO, kwartaalcijfers op het teambord, halfjaarcijfers in de [IMS-rapportage](../ims-rapportage/), jaarcijfers in ENSIA en de directiebeoordeling |
| Kleur | groen op koers; oranje achter, met plan; rood achter zonder plan of bron ontbreekt. Volgens een vaste rekenregel per indicator |
| Bij rood | de eigenaar levert binnen 4 weken een plan; twee kwartalen rood is een afwijking |
| Beheer | de CISO is eigenaar; wijzigingen via het tactische overleg; doelwaarden jaarlijks door de directie |

**Vaststeller.** Laat de directie de set en de doelwaarden vaststellen, en geef de colleges de acht indicatoren
jaarlijks in de ENSIA-verantwoording. Vier colleges laten stemmen over een KPI-set kost een jaar en levert niets op.

## Bijlage. Rekenregels voor de kleur (voorbeeld)

| Indicator | Groen | Oranje | Rood |
|---|---|---|---|
| K1 | alle met eigenaar | ten minste de helft, met datum voor de rest | minder, of geen datum |
| K2 | op of boven het kwartaalpad | tot 2 producten achter | meer dan 2 achter |
| K3 | eerste golf op schema | 1 stuk achter | 2 of meer achter |
| K4 | 100% eigenaar en 80% of meer BIV, RTO, RPO | eigenaar 100%, vulling 50 tot 80% | eigenaar onder 100% of vulling onder 50% |
| K5 | 0 uitzonderingen, permanent actief 10% of minder | 1 tot 3 uitzonderingen of permanent actief tot 25% | meer |
| K6 | 0 kritiek ouder dan 60 dagen én servers meetbaar | tot 10, of servers deels meetbaar | meer dan 10, of servers niet meetbaar |
| K7 | mobiel 90% of meer, werkplek 100% versleuteld | mobiel 70 tot 90%, werkplek 95 tot 100% | minder |
| K8 | 4 geslaagde tests per jaar met verslag | 2 of 3 | 0 of 1, of geen verslag |
