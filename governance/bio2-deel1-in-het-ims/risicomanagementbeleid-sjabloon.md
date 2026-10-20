# Sjabloon: risicomanagementbeleid informatiebeveiliging

> **Herkomst:** concept-risicomanagementbeleid van de CISO van een regionale samenwerking van gemeenten (september 2026), nog niet vastgesteld. Voor de commons generiek gemaakt: de eigen risico's, besluitnummers en voorbeelden zijn weggelaten. Vul in tussen «…».

| | |
|---|---|
| Document | Risicomanagementbeleid informatiebeveiliging |
| Versie | «versie, status, datum» |
| Opsteller | «CISO» |
| Review | «concernadviseur risicomanagement, BCM-manager, team IB&P, CIO» |
| Vaststeller | «directieteam» |
| Norm | ISO/IEC 27001, clausule 6.1.2, 6.1.3, 8.2 en 8.3; ISO/IEC 27005 als leidraad; BIO 2.0 deel 1; Cyberbeveiligingsregeling sector overheid, bijlage 2 (impactniveaus) |
| Herziening | jaarlijks na de directiebeoordeling; direct bij een wijziging van bijlage 2 van de regeling |

## 1. Doel en uitgangspunten

Elk besluit over informatiebeveiliging is terug te voeren op een risico dat iemand kent, heeft gewogen en waarvan
iemand eigenaar is. Het beleid geldt voor het hele IMS (informatiebeveiliging, privacy, continuïteit): één register,
één methode. DPIA en BIA leveren input en vervangen het niet.

1. **Geen herkomst, geen risico.** Elk risico komt uit een analyse, meting, incident of audit, met datum en bron.
2. **Geen eigenaar, dan ONBELEGD, en dat is een actie.** Een risico zonder eigenaar staat op de agenda van het
   tactische overleg tot het belegd is.
3. **De impact volgt de wet.** De impactschalen zijn die van bijlage 2 bij de Cyberbeveiligingsregeling. Een risico
   dat in één categorie hoog of zeer hoog scoort, raakt een cruciaal systeem.
4. **Klassen zijn narekenbaar.** De klasse volgt uit een vaste tabel, niet uit een oordeel per geval.
5. **Accepteren is een besluit met een naam, een datum, voorwaarden en een houdbaarheidsdatum.**

## 2. Toepassingsgebied en niveaus

| Niveau | Wat | Wie initieert | Hoe vaak |
|---|---|---|---|
| Strategisch | de grootste risico's voor de organisatie als geheel | concernadviseur risicomanagement, met CISO en BCM-manager; FG adviseert | jaarlijks, vóór de directiebeoordeling |
| Operationeel | risico's op een proces, systeem, leverancier of locatie | discipline-eigenaar of proceseigenaar | doorlopend, bij de triggers in paragraaf 5 |
| Project | risico's van een nieuw of gewijzigd systeem, contract of verwerking | projectleider of opdrachtgever; IB&P toetst | bij de start en bij elke belangrijke wijziging |

## 3. Rollen

| Rol | Doet | Doet niet |
|---|---|---|
| Risico-eigenaar (lijnmanager, proceseigenaar) | kent het risico, kiest de behandeling, stelt het behandelplan op, accepteert binnen zijn mandaat, rapporteert | het risico wegdelegeren naar een adviseur of leverancier |
| Discipline-eigenaar (ISO, BCM-manager, privacy officer) | voert operationele analyses uit, valideert scores, bewaakt de kwaliteit van het register | risico's accepteren namens de lijn |
| CISO | stelt het kader, signaleert, escaleert, rapporteert onafhankelijk | eigenaar zijn van een lijnrisico; assurance geven |
| Concernadviseur risicomanagement | initieert de strategische analyse, bewaakt de aansluiting op planning en control en de weerstandsparagraaf | |
| FG | adviseert bij risico's met persoonsgegevens; toezichthoudend | operationele privacyrisico's beheren |
| Tactisch IMS-overleg | toetst acceptaties op klasse gemiddeld, beslist over behandelplannen, agendeert onbelegde risico's | strategische risico's accepteren |
| Stuurgroep | adviseert de directie over klasse hoog; kan een acceptatie van het tactische overleg terugdraaien | |
| Directieteam | stelt risicobereidheid en klassegrenzen vast, beslist over kritiek en hoog, stelt de eigenaren van strategische risico's aan | |
| Interne accountant | toetst achteraf of het proces is gevolgd | scoren of accepteren |

## 4. Methode

### 4.1 Zes stappen

| Stap | Uitkomst | Wie |
|---|---|---|
| 1 Identificatie | risico als gebeurtenis, oorzaak en gevolg; asset of proces; bron en datum; eigenaar | discipline-eigenaar met proceseigenaar |
| 2 Analyse | kans en impact onderbouwd; score en klasse | discipline-eigenaar; CISO valideert bij hoog en kritiek |
| 3 Evaluatie | vergelijking met de risicobereidheid; prioriteit; besluit behandelen of accepteren | risico-eigenaar |
| 4 Behandeling | behandelplan: maatregelen met eigenaar, datum, verwachte netto-score, kosten | risico-eigenaar |
| 5 Acceptatie | restrisico geaccepteerd op het juiste niveau, met voorwaarden en herbeoordelingsdatum | risico-eigenaar, tactisch overleg, stuurgroep of directie, naar klasse |
| 6 Monitoring | voortgang; herbeoordeling op datum of trigger; rapportage | risico-eigenaar; CISO bewaakt |

### 4.2 Kans en impact

**Kans** in vijf stappen: 1% (hypothetisch), 10% (er is een kans), 30% (aanzienlijk), 50% (fifty-fifty), meer dan
50% (waarschijnlijk). Onderbouwd met dreigingsbeeld, aanvalsvlak en aanwezige of ontbrekende maatregelen. Gebruik
1% alleen als er bewijs is dat de gebeurtenis bij vergelijkbare organisaties niet voorkomt.

**Impact** in vijf niveaus (1 zeer laag tot 5 zeer hoog), op de zes categorieën van bijlage 2 bij de
Cyberbeveiligingsregeling: dataverlies (RPO), hersteltijd (RTO), financieel, juridisch en bestuurlijk,
maatschappelijk, veiligheid van personen. De hoogste ingevulde categorie bepaalt het niveau. Voor hoog en kritiek
zijn ten minste drie categorieën ingevuld, altijd maatschappelijk en juridisch-bestuurlijk. Alleen financieel
scoren onderschat risico's op bijvoorbeeld operationele technologie.

**Score** is kans (1 tot 5) maal impact (1 tot 5).

### 4.3 Klassen

Een impact van 4 of 5 is nooit groen. Laat de grenzen vaststellen door het directieteam.

| Impact ↓ / Kans → | 1% | 10% | 30% | 50% | >50% |
|---|---|---|---|---|---|
| 5 Zeer hoog | Gemiddeld (5) | Hoog (10) | Kritiek (15) | Kritiek (20) | Kritiek (25) |
| 4 Hoog | Gemiddeld (4) | Gemiddeld (8) | Hoog (12) | Kritiek (16) | Kritiek (20) |
| 3 Middel | Laag (3) | Gemiddeld (6) | Hoog (9) | Hoog (12) | Kritiek (15) |
| 2 Laag | Laag (2) | Laag (4) | Gemiddeld (6) | Gemiddeld (8) | Hoog (10) |
| 1 Zeer laag | Laag (1) | Laag (2) | Laag (3) | Laag (4) | Gemiddeld (5) |

Kritiek: 15 en hoger. Hoog: 9 tot en met 12. Gemiddeld: 5 tot en met 8. Laag: 1 tot en met 4, behalve bij impact
4 of 5.

### 4.4 Risicobereidheid en acceptatieladder

| Klasse | Wat er moet gebeuren | Wie accepteert | Termijn |
|---|---|---|---|
| Kritiek | direct via de stuurgroep naar de directie, met behandelplan; mitigeren is verplicht | alleen de directie, en alleen tijdelijk met einddatum | plan binnen 4 weken; herbeoordeling elke 3 maanden |
| Hoog | via het tactische overleg naar de stuurgroep, met plan; mitigeren tenzij de directie accepteert | directie, op advies van de stuurgroep | plan binnen 8 weken; maximaal 6 maanden onbehandeld met lopend plan; herbeoordeling halfjaarlijks |
| Gemiddeld | melden bij het tactische overleg met een voorstel | tactisch overleg, onderbouwd; stuurgroep kan terugdraaien | plan binnen 3 maanden; herbeoordeling jaarlijks |
| Laag | registreren; de eigenaar beslist | risico- of discipline-eigenaar; tactisch overleg kan terugdraaien | herbeoordeling jaarlijks |

Een acceptatie bevat altijd: naam en functie, datum, netto-score, voorwaarden, herbeoordelingsdatum. Vervalt een
voorwaarde, dan vervalt de acceptatie.

### 4.5 Behandeling

In volgorde van voorkeur: verminderen, vermijden, overdragen (contract, verzekering, leverancier; de
verantwoordelijkheid gaat niet mee), accepteren. De gekozen maatregelen komen in de verklaring van toepasselijkheid
met motivering; wat niet wordt toegepast in de bijlage uitzonderingen. Een maatregel zonder eigenaar is geen maatregel.

## 5. Wanneer

**Triggers voor een (her)beoordeling:** de start van een project; een belangrijke wijziging in organisatie, techniek
of leverancier; een nieuw contract of verlenging; een significant incident of bijna-incident; een auditbevinding;
een meting die een aanname weerlegt; een wijziging in wet- of regelgeving; een verzoek van een proceseigenaar of
gremium. Een overeenkomst die wordt getekend zonder analyse vooraf, terwijl zij toegang of netwerk raakt, is precies
wat deze paragraaf moet voorkomen.

| Wanneer | Wat |
|---|---|
| Q1 | strategische risicoanalyse, met herbeoordeling van de strategische risico's en hun eigenaren |
| Q2 | risicoworkshop met de directie: risicobereidheid bevestigen of bijstellen |
| doorlopend | operationele en projectanalyses; onbelegde risico's op de agenda |
| halfjaarlijks | top-risico's, acceptaties, voortgang en het aantal onbelegde risico's in de [halfjaarrapportage](../ims-rapportage/) |
| Q4 | directiebeoordeling: register, acceptaties en effectiviteit van dit beleid |

## 6. Het register

Eén register voor de drie disciplines. **Rubriceer per veld, niet per document:** beschrijving, score en eigenaar
zijn werkmateriaal; de technische onderbouwing van een bevinding is need-to-know. Een register met exploiteerbare
details is zelf een risico. Zie voor een opzet het [sjabloonregister](../risicogestuurd-managementsysteem/sjabloon-register.md).

| Veld | Vulling |
|---|---|
| ID | per niveau een prefix (strategisch, operationeel, project) |
| Risico | gebeurtenis, oorzaak, gevolg |
| Domein | ISMS, BCMS, PIMS of combinatie |
| Asset of proces | met verwijzing naar de lijst kritieke processen |
| Herkomst | analyse, meting, incident of audit, met datum en bron |
| Kans en onderbouwing | |
| Impact per categorie | hoogste bepaalt |
| Score en klasse | bruto en netto |
| Herkomst van de score | vastgesteld, voorstel of gevalideerd, door wie en wanneer |
| Eigenaar | naam en functie, of ONBELEGD |
| Behandeling en behandelplan | maatregelen met eigenaar, datum, verwachte netto-score |
| Acceptatie | wie, datum, voorwaarden, herbeoordelingsdatum |
| Status | open, in behandeling, geaccepteerd, gesloten |
| Technische onderbouwing | verwijzing naar het gerubriceerde dossier (need-to-know) |
| Samenhang | verwante risico's en maatregelen |
| Planning-en-controllabel | ja of nee, met financiële raming |

## 7. Rapportage

De CISO rapporteert onafhankelijk: aan het tactische overleg elke vergadering (onbelegde risico's, nieuwe
acceptaties, verlopen herbeoordelingen), aan stuurgroep en directie halfjaarlijks, aan de colleges jaarlijks.
