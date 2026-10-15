---
domein: mdm
titel: Beleid mobile device management
samenvatting: Regelt de inrichting, het beheer en het gebruik van laptops, smartphones en tablets met toegang tot bedrijfsinformatie. Gaat over zero footprint en bescherming op het apparaat, beheer via MDM en MAM, en de gebruikersovereenkomst mobiel werken.
invoeren:
  - Richt wissen op afstand in, met een meldroute voor verlies via de servicedesk (hoofdstuk 3).
  - Stel een reisrichtlijn apparatuur op met de landen en voorwaarden voor reisapparaten (hoofdstuk 3).
  - Schrijf elk mobiel apparaat met toegang tot bedrijfsinformatie in bij MDM of MAM (hoofdstuk 4).
  - Stel nalevingsregels in die versleuteling, vergrendeling, ondersteunde versie en wissen op afstand afdwingen (hoofdstuk 4).
  - Leg de inrichting van MDM en MAM vast als configuratiestandaard (hoofdstuk 4).
  - Richt een nalevingsrapportage per apparaat in voor de lijneigenaar en de CISO (hoofdstuk 4).
  - Stel een gebruikersovereenkomst mobiel werken op en laat elke mobiele gebruiker tekenen (hoofdstuk 5).
  - Richt een gastnetwerk in dat logisch gescheiden is van het bedrijfsnetwerk (hoofdstuk 5).
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor mobiele apparatuur waarmee
bedrijfsinformatie wordt verwerkt: laptops, smartphones en tablets van de organisatie en, waar dat is
toegestaan, eigen apparaten van medewerkers. Het regelt hoe die apparaten zijn ingericht, beheerd en gebruikt,
zodat bedrijfsinformatie beschermd blijft bij verlies, diefstal en werken buiten de locaties van de
organisatie. Het gaat over ISO-beheersmaatregel 8.1.

**Voor wie.** Het beleid is primair bedoeld voor de afdeling die het apparaatbeheer inricht en voor de
servicedesk die uitgifte, verlies en wissen afhandelt. De gedragsregels gelden voor iedereen die mobiel werkt
met bedrijfsinformatie: medewerkers, inhuur, stagiairs en vrijwilligers.

**Waarop.** Alle laptops, smartphones en tablets met toegang tot bedrijfsinformatie, de apps en diensten die
daarop draaien, en de voorzieningen voor apparaatbeheer (MDM) en appbeheer (MAM). Is het apparaatbeheer of
de werkplekdienst uitbesteed, dan gelden de eisen uit dit beleid als minimumeis voor die leverancier. De
organisatie legt dat vast in het contract en toetst de naleving met een onafhankelijke verklaring, zoals een
ISO 27001-certificaat of een ISAE 3402- of ISAE 3000-rapport; het vastleggen loopt via het beleid
informatiebeveiliging bij inkoop, het toetsen via het beleid contractbeheer.

Buiten dit beleid vallen de inventaris en uitgifte van apparatuur (beleid bedrijfsmiddelenbeheer), de
versleutelingseisen (beleid cryptografie), de netwerktoegang en het wifinetwerk (beleid netwerkbeveiliging),
de accounts en de meerfactorauthenticatie (beleid logische toegangsbeveiliging) en het wissen van
apparatuur bij afvoer (beleid afvoer en hergebruik van gegevensdragers).

## 2. Uitgangspunten

1. Bedrijfsinformatie blijft zo veel mogelijk in de centrale systemen. Op het apparaat staat niets, of zo min
   mogelijk en dan versleuteld.
2. Alleen beheerde apparaten of beheerde apps krijgen toegang tot bedrijfsinformatie.
3. De gebruiker weet wat de risico's van mobiel werken zijn en heeft getekend dat hij veilig werkt.
4. Een apparaat dat niet meer aan de eisen voldoet, verliest zijn toegang automatisch; de techniek dwingt
   het beleid af, de gebruiker hoeft er niet aan te denken.
5. Termijnen en frequenties in dit beleid die niet uit een wet of uit de BIO 2.0 komen, zijn standaardwaarden.
   De organisatie past ze aan op haar eigen risicoafweging en legt de keuze vast bij de vaststelling van dit beleid.

## 3. Zero footprint en bescherming op het apparaat

- De beheerder MDM richt apps en diensten voor mobiele apparaten zo in dat bedrijfsinformatie niet standaard
  op het apparaat wordt opgeslagen: werken gebeurt via de browser, een virtuele werkplek of een beheerde app
  die geen lokale kopie bewaart. [8.01.01]
- Waar dat nog niet kan, staat bedrijfsinformatie alleen in een beheerde, versleutelde container of op een
  volledig versleuteld apparaat. Het apparaat is beveiligd met een pincode van ten minste zes cijfers, een
  wachtwoord of biometrie, met automatische vergrendeling na ten hoogste vijf minuten; de beheerder MDM
  dwingt die instellingen af. [8.01.01]
- Van elk apparaat met toegang tot bedrijfsinformatie kan de organisatie de bedrijfsinformatie op afstand
  wissen. Bij verlies of diefstal meldt de gebruiker dat direct bij de servicedesk; de servicedesk wist
  binnen [[wistermijn: standaard vier uur na de melding]], blokkeert de toegang van het apparaat en registreert de melding als
  beveiligingsincident volgens het beleid beveiligingsincidenten. [8.01.01]
- Informatie met het label strikt vertrouwelijk of geheim uit het beleid informatieclassificatie staat nooit lokaal
  op een mobiel apparaat; de beheerder MDM blokkeert downloaden en offline beschikbaar maken voor die labels
  waar de systemen dat ondersteunen. [8.01.01]
- Bij reizen naar landen waar de organisatie een verhoogd risico ziet, geeft de servicedesk op verzoek een
  schoon reisapparaat uit, dat na terugkomst wordt gewist; welke landen dat zijn, staat in
  [[reisrichtlijn apparatuur: het document met de landen en de voorwaarden voor reisapparatuur]].
  [8.01.01]

## 4. Beheer van apparaten

- Elk mobiel apparaat met toegang tot bedrijfsinformatie valt onder een MDM-oplossing (beheer van het hele
  apparaat) of, voor eigen apparaten, een MAM-oplossing (beheer van de bedrijfsapps). De beheerder MDM
  schrijft het apparaat in vóór uitgifte; inschrijving is een voorwaarde voor toegang. [8.01.02]
- Via MDM of MAM dwingt de beheerder MDM ten minste af: versleuteling, schermvergrendeling, een ondersteunde
  versie van het besturingssysteem, geen root of jailbreak, geen onbekende appbronnen en wissen op afstand.
  Een apparaat dat niet voldoet, verliest automatisch de toegang tot bedrijfsinformatie en de gebruiker
  krijgt een melding met wat hij moet doen. [8.01.02]
- Mobiele apparaten vallen onder patchmanagement en hardening volgens het beleid vulnerability- en
  patchmanagement. De beheerder MDM installeert beveiligingsupdates van het besturingssysteem en de
  bedrijfsapps binnen de termijnen uit dat beleid, of dwingt de installatie af bij de gebruiker; apparaten
  waarvoor de fabrikant geen updates meer levert, worden binnen drie maanden uitgefaseerd. [8.01.02]
- Apps op beheerde apparaten komen uit de officiële winkel of uit de beheerde bedrijfscatalogus. De
  beheerder MDM beoordeelt elk kwartaal de lijst van geïnstalleerde apps op apps die bedrijfsinformatie
  kunnen lezen of doorsturen, en blokkeert apps die niet zijn toegestaan. [8.01.02]
- De beheerder MDM houdt een nalevingsrapportage bij met per apparaat de inschrijving, de versie van het
  besturingssysteem, de laatste contactdatum en de nalevingsstatus, en rapporteert die elk kwartaal aan
  [[lijneigenaar mobiele apparatuur: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd IT]] en de
  CISO. Apparaten zonder contact in de afgelopen drie maanden worden geblokkeerd en bij de gebruiker
  nagevraagd. [8.01.02]
- De beheerder MDM legt de inrichting van MDM en MAM (nalevingsregels, app-beleid, voorwaardelijke toegang)
  vast als configuratiestandaard en beheert wijzigingen daarin via het beleid wijzigingsbeheer. [8.01.02]

::: als byod=ja
- Eigen apparaten zijn toegestaan onder de voorwaarden in
  [[regeling eigen apparaten: welke apparaten, besturingssystemen en diensten zijn toegestaan]].
  Op een eigen apparaat staat bedrijfsinformatie alleen in beheerde apps (MAM); de organisatie wist bij vertrek
  of verlies alleen die apps en hun gegevens, niet het hele apparaat. De medewerker stemt daar vooraf
  schriftelijk mee in; HR bewaart de instemming bij de gebruikersovereenkomst. [8.01.01]
- Een eigen apparaat krijgt pas toegang als het een ondersteunde versie van het besturingssysteem heeft, een
  schermvergrendeling en versleuteling van de opslag. De toegangsvoorziening controleert dat bij elke
  aanmelding; de beheerder MDM ziet eigen apparaten in dezelfde nalevingsrapportage als apparaten van de
  organisatie. [8.01.02]
:::

::: als byod=nee
- Eigen apparaten krijgen geen toegang tot bedrijfsinformatie, ook niet via webmail of de browser. De
  toegangsvoorziening laat alleen apparaten toe die de organisatie beheert; de beheerder MDM test dat
  jaarlijks met een niet-beheerd apparaat. [8.01.01]
:::

::: als werkplek=cloud
- Toegang tot de cloudwerkplek vanaf een mobiel apparaat loopt via voorwaardelijke toegang: meerfactor plus
  een apparaat of app die volgens het MDM of MAM aan de eisen voldoet. Opslaan, kopiëren naar niet-beheerde
  apps en lokaal synchroniseren van bestanden zijn op niet-beheerde apparaten uitgeschakeld. De beheerder MDM
  test de regels voor voorwaardelijke toegang bij elke wijziging en ten minste jaarlijks. [8.01.01, 8.01.02]
:::

::: als werkplek=hybride
- Mobiele apparaten krijgen toegang tot clouddiensten via voorwaardelijke toegang op basis van de MDM- of
  MAM-status, en tot de lokale of virtuele werkplek alleen via een beveiligde verbinding (bijvoorbeeld een
  VPN of een gateway voor de virtuele werkplek) vanaf een beheerd apparaat. De beheerder MDM stemt de
  beheerinstellingen voor beide routes op elkaar af, zodat een apparaat dat voor de ene route is
  geblokkeerd, ook de andere verliest, en test dat ten minste jaarlijks. [8.01.02]
:::

::: als werkplek=on-premises
- Mobiele apparaten krijgen toegang tot de interne omgeving alleen via een beveiligde verbinding
  (bijvoorbeeld een VPN of een gateway voor een virtuele werkplek) vanaf een apparaat dat onder MDM valt.
  Mail en agenda op smartphones lopen via een beheerde app. Werken via een virtuele werkplek is de standaard,
  zodat er geen bedrijfsinformatie op het apparaat komt; de beheerder MDM controleert jaarlijks dat er geen
  andere routes naar de interne omgeving openstaan. [8.01.01, 8.01.02]
:::

## 5. Gebruikersovereenkomst en gedrag

- Voordat een medewerker mobiel werkt, tekent hij een gebruikersovereenkomst mobiel werken. Daarin verklaart
  hij de risico's te kennen en veilig te werken. De overeenkomst geldt voor alle mobiele apparatuur die hij
  zakelijk gebruikt, ook een eigen apparaat. HR bewaart de getekende overeenkomst in het personeelsdossier of
  het uitgiftesysteem; de servicedesk geeft geen apparaat uit zonder getekende overeenkomst. [8.01.02]
- De overeenkomst gaat ten minste over: direct melden van verlies of diefstal, geen bedrijfsinformatie in
  privéapps of privécloudopslag, geen gedeeld gebruik van het apparaat met anderen, updates installeren, het
  apparaat niet onbeheerd achterlaten, voorzichtig zijn met openbare wifi en het accepteren van wissen op
  afstand. [[lijneigenaar mobiele apparatuur]] beoordeelt de overeenkomst jaarlijks en laat haar opnieuw
  tekenen na een inhoudelijke wijziging. [8.01.02]
- De gebruiker werkt in openbare ruimten en in het openbaar vervoer zo dat anderen niet kunnen meekijken
  (privacyfilter op het scherm, geen gevoelige gesprekken), en voert geen handelingen met informatie met het
  label strikt vertrouwelijk of hoger uit buiten een beveiligde verbinding. [8.01.01]
- Op de locaties van de organisatie gebruiken beheerde apparaten het beveiligde bedrijfsnetwerk; niet-beheerde
  apparaten en gasten gebruiken een gastnetwerk dat logisch gescheiden is van het bedrijfsnetwerk, volgens
  het beleid netwerkbeveiliging. Er is geen open, onbeveiligd wifinetwerk. [8.01.02]
- Bij vertrek of functiewijziging levert de gebruiker het apparaat in volgens het beleid
  bedrijfsmiddelenbeheer; de servicedesk wist het apparaat of de beheerde apps op de laatste werkdag en
  verwijdert het uit het apparaatbeheer. [8.01.01]

## 6. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| [[lijneigenaar mobiele apparatuur]] | Eigenaar van dit beleid, de inrichting van MDM en MAM, de gebruikersovereenkomst en de reisrichtlijn; ontvangst van de kwartaalrapportage |
| Beheerder MDM | Inschrijving, nalevingsregels, voorwaardelijke toegang, app-beleid, updates, nalevingsrapportage en wissen op afstand |
| Servicedesk | Uitgifte na getekende overeenkomst, melding van verlies of diefstal, wissen binnen de wistermijn, registratie als incident, reisapparatuur, inname bij vertrek |
| HR | Gebruikersovereenkomst mobiel werken en instemming met wissen bij indiensttreding en bij uitgifte |
| CISO | Advies, jaarlijkse toetsing van opzet en werking van dit beleid, beoordeling van de nalevingsrapportages en van afwijkingen |
| Inkoop en contractbeheer | Eisen uit dit beleid in het contract met een uitbestede werkplek- of beheerdienst, toetsen van de verklaring |
| Medewerkers en inhuur | Overeenkomst naleven, updates installeren, apparaat niet delen, verlies of diefstal direct melden |

## 7. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in [[registratie van controles: het systeem waarin controles worden vastgelegd, bijvoorbeeld het ticketsysteem of het managementsysteem]];
afwijkingen gaan als bevinding naar het risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| MDM-01 | Elk apparaat met toegang tot bedrijfsinformatie is ingeschreven in MDM of MAM, voldoet aan de nalevingsregels en heeft een ondersteund en bijgewerkt besturingssysteem | Beheerder MDM | Per kwartaal | Nalevingsrapportage: aantal apparaten met toegang tegenover aantal ingeschreven, aantal apparaten met verouderd systeem of ontbrekende updates, afhandeling | 8.01.02 |
| MDM-02 | Elke mobiele gebruiker heeft een getekende gebruikersovereenkomst en, bij een eigen apparaat, een instemming met wissen op afstand | HR | Per kwartaal | Vergelijking van de lijst mobiele gebruikers uit MDM en MAM met de getekende overeenkomsten | 8.01.02 |
| MDM-03 | Wissen op afstand werkt en gemelde verliezen zijn binnen de wistermijn gewist en als incident geregistreerd | Beheerder MDM | Jaarlijks | Testverslag van wissen op een testapparaat, incidentregistratie met meldtijd en wistijd per verlies | 8.01.01 |
| MDM-04 | Niet-beheerde apparaten krijgen geen toegang tot bedrijfsinformatie en de regels voor voorwaardelijke toegang en de blokkering van lokaal opslaan werken zoals ingericht | CISO | Jaarlijks | Testverslag met een niet-beheerd apparaat en een beheerd apparaat per route, configuratiestandaard | 8.01.01, 8.01.02 |
| MDM-05 | De geïnstalleerde apps op beheerde apparaten zijn toegestaan en apparaten zonder contact in drie maanden zijn geblokkeerd | Beheerder MDM | Per kwartaal | Applijst met de beoordeling, lijst van geblokkeerde apparaten en de opvolging | 8.01.02 |
| MDM-06 | Een uitbestede werkplek- of beheerdienst levert een geldige onafhankelijke verklaring over het apparaatbeheer | Contractbeheer | Jaarlijks | Verklaring van de leverancier, beoordeling van de uitzonderingen | 8.01.01, 8.01.02 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging.
[[lijneigenaar mobiele apparatuur]] dient het verzoek in bij de CISO, met de reden, de compenserende
maatregelen en de looptijd. De afwijking geldt pas na acceptatie van het risico door
[[risico-eigenaar: de manager die restrisico's accepteert]] en staat in het risicoregister; afwijkingen
worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 8. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid
bedrijfsmiddelenbeheer (uitgifte, inventaris, inname en gedragsregels), het beleid informatieclassificatie
(labels die niet lokaal mogen staan), het beleid cryptografie (versleuteling op het apparaat), het beleid
vulnerability- en patchmanagement (updates en hardening), het beleid logische toegangsbeveiliging (meerfactor
en voorwaardelijke toegang), het beleid netwerkbeveiliging (wifi en externe toegang), het beleid
wijzigingsbeheer (configuratiestandaard), het beleid beveiligingsincidenten (verlies en diefstal), het beleid
afvoer en hergebruik van gegevensdragers (wissen bij afvoer) en het beleid informatiebeveiliging bij inkoop en
contractbeheer (uitbestede werkplekdienst).
