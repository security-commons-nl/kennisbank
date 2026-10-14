---
domein: bedrijfsmiddelen
titel: Beleid bedrijfsmiddelenbeheer
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor het beheer van bedrijfsmiddelen: de
informatie zelf en alles waarmee de organisatie die verwerkt, opslaat of doorgeeft. Het legt vast welke
bedrijfsmiddelen de organisatie heeft, wie er eigenaar van is, hoe ze gebruikt mogen worden, hoe apparatuur
wordt geplaatst, beschermd en onderhouden, en hoe bedrijfsmiddelen terugkomen als iemand vertrekt. Het gaat
over de ISO-beheersmaatregelen 5.9 tot en met 5.11, 7.6, 7.8, 7.9, 7.11 en 7.13.

**Voor wie.** Het beleid is primair bedoeld voor de afdeling die de inventaris en de uitgifte van apparatuur
beheert en voor de eigenaren van bedrijfsmiddelen. De gedragsregels gelden voor iedereen die een
bedrijfsmiddel van de organisatie gebruikt: medewerkers, inhuur, stagiairs, vrijwilligers en leveranciers.

**Waarop.** Alle bedrijfsmiddelen die van belang zijn voor de informatieverwerking: hardware (servers,
netwerkapparatuur, werkplekken, printers), eindgebruikersapparaten en mobiele apparatuur, verwijderbare
opslagmedia, authenticatiemiddelen (tokens, smartcards, sleutels), software en clouddiensten,
gegevensverzamelingen en operationele technologie. Is het beheer van apparatuur, een serverruimte of een
clouddienst uitbesteed, dan gelden de eisen uit dit beleid als minimumeis voor die leverancier. De organisatie
legt dat vast in het contract en toetst de naleving met een onafhankelijke verklaring, zoals een ISO
27001-certificaat of een ISAE 3402- of ISAE 3000-rapport; het vastleggen loopt via het beleid
informatiebeveiliging bij inkoop, het toetsen via het beleid contractbeheer.

Buiten dit beleid vallen het classificeren en labelen van informatie (beleid informatieclassificatie), het
wissen en afvoeren van opslagmedia en apparatuur (beleid afvoer en hergebruik van gegevensdragers), de
inrichting van mobiele apparaten (beleid mobile device management), de zone-indeling en de toegang tot
ruimten (beleid fysieke toegang en beveiliging) en clear desk en clear screen (beleid IT-compliance).

## 2. Uitgangspunten

1. Wat niet in de inventaris staat, wordt niet beveiligd. De inventaris is daarom de basis voor
   patchmanagement, toegangsbeheer, back-up en controle.
2. Elk bedrijfsmiddel heeft één eigenaar: een functie of organisatieonderdeel dat over de hele levenscyclus
   verantwoordelijk is, van aanschaf tot afvoer.
3. Wie een bedrijfsmiddel gebruikt, kent de gedragsregels en heeft dat aantoonbaar bevestigd.
4. Apparatuur staat, werkt en wordt onderhouden op een manier die past bij het impactniveau van de informatie
   die zij verwerkt en bij de zone waarin zij staat (beleid fysieke toegang en beveiliging).

## 3. Beleidsregels

### 3.1 Inventaris

- [[beheerder inventaris: de functie die de inventaris bijhoudt, bijvoorbeeld de configuratiebeheerder]]
  houdt één inventaris bij van alle bedrijfsmiddelen die van belang zijn voor de informatieverwerking,
  bijvoorbeeld in een CMDB. De inventaris omvat ook bedrijfsmiddelen op afstand (thuiswerkplekken, mobiele
  apparatuur), clouddiensten en apparaten die regelmatig op het netwerk zijn aangesloten zonder dat de
  organisatie ze beheert, zoals apparatuur van leveranciers. [5.09.01]
- Per bedrijfsmiddel legt de inventaris ten minste vast: uniek kenmerk, type, eigenaar, locatie of
  leverancier, gebruiker of beheerder, classificatie, bedrijfsprocessen die ervan afhangen, versie of
  configuratie, onderhoudsschema en de datum van ingebruikname en einde ondersteuning. [5.09.01]
- Elke wijziging in de levenscyclus (aanschaf, uitgifte, verplaatsing, reparatie, inname, afvoer) verwerkt
  de beheerder van de inventaris binnen vijf werkdagen, via het wijzigingsproces of de uitgifte- en
  innameprocedure. [5.09.01]
- De beheerder van de inventaris controleert de volledigheid en actualiteit ten minste elk kwartaal voor
  werkplekken, mobiele apparatuur en clouddiensten en ten minste jaarlijks voor de overige bedrijfsmiddelen,
  door de inventaris te vergelijken met een tweede bron (netwerkscan, beheertool, facturen of
  licentieoverzichten). Het vergelijkingsrapport met de afwijkingen en hun afhandeling is het bewijs.
  Bedrijfsmiddelen zonder eigenaar of zonder registratie zijn binnen een maand opgelost of buiten gebruik
  gesteld. [5.09.01]

::: als werkplek=cloud
- De beheerder van de inventaris registreert werkplekken en mobiele apparaten via het centrale
  endpointbeheer van de cloudwerkplek. Alleen apparaten die daar zijn ingeschreven krijgen toegang tot
  bedrijfsinformatie, zodat de registratie van werkplekken vanzelf volledig is. De lijst met cloudtenants,
  abonnementen en gekoppelde apps maakt deel uit van de inventaris en wordt elk kwartaal vergeleken met de
  inkoopadministratie. [5.09.01]
:::

::: als werkplek=hybride
- Werkplekken staan zowel in het cloudendpointbeheer als in het beheer van de lokale of virtuele omgeving.
  De beheerder van de inventaris vergelijkt bij de kwartaalcontrole beide registraties met elkaar en met de
  inventaris; een apparaat dat in één bron ontbreekt, is een afwijking. [5.09.01]
:::

::: als werkplek=on-premises
- De beheerder van de inventaris vergelijkt werkplekken en servers in het eigen netwerk ten minste
  maandelijks met een netwerkscan of beheertool met de inventaris. Onbekende apparaten op het netwerk worden
  binnen een week geïdentificeerd en geregistreerd of van het netwerk verwijderd. [5.09.01]
:::

::: als ot=beperkt
- Operationele technologie in gebouwen (gebouwbeheer, toegangscontrole, camera's) staat in dezelfde
  inventaris, met per installatie de eigenaar, de leverancier die het onderhoud doet, de manier waarop die op
  afstand toegang heeft en de softwareversie. [5.09.01]
:::

::: als ot=substantieel
- Operationele technologie (bijvoorbeeld gemalen, bruggen, verkeersinstallaties, zuivering) heeft een eigen
  OT-inventaris die deel uitmaakt van de inventaris van de organisatie. Per component staan daarin de
  eigenaar, de fysieke locatie, het netwerksegment, de firmware- of softwareversie, de leverancier, de
  toegang op afstand en de procesfunctie die ervan afhangt. [5.09.01]
- De eigenaar van de installatie controleert de OT-inventaris ten minste elk halfjaar met een passieve
  netwerkinventarisatie of een fysieke opname op locatie; actieve scans op OT-netwerken gebeuren alleen met
  akkoord van de eigenaar van de installatie. [5.09.01]
:::

### 3.2 Eigendom

- Elk bedrijfsmiddel in de inventaris heeft een eigenaar. Voor werkplekken, infrastructuur en ondersteunende
  software is dat
  [[eigenaar IT-middelen: de functie die eigenaar is van werkplekken en infrastructuur, bijvoorbeeld het hoofd IT]];
  voor bedrijfsapplicaties en gegevensverzamelingen is dat de proceseigenaar. De inventaris toont per
  bedrijfsmiddel de eigenaar. [5.09.01]
- De eigenaar zorgt dat het bedrijfsmiddel juist is geregistreerd, geclassificeerd en beveiligd, en dat het
  wordt afgevoerd als het niet meer nodig is. De eigenaar bevestigt dat jaarlijks bij de inventariscontrole.
  [5.09.01]

### 3.3 Aanvaardbaar gebruik

- De organisatie heeft gedragsregels voor het gebruik van informatie en bedrijfsmiddelen, vastgelegd in
  [[gedragsregels bedrijfsmiddelen: het document met de huisregels of de gedragscode voor ICT-gebruik]].
  Ze gaan ten minste over privégebruik, het installeren van software, het gebruik van clouddiensten buiten
  de organisatie, het meenemen van apparatuur, het delen en bewaren van informatie en het melden van
  verlies of diefstal. [[lijneigenaar bedrijfsmiddelen: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd IT]]
  stelt de gedragsregels vast en beoordeelt ze jaarlijks. [5.10.01]
- De gedragsregels zeggen per vertrouwelijkheidslabel uit het beleid informatieclassificatie (openbaar,
  intern, vertrouwelijk, confidentieel, geheim) hoe de gebruiker informatie mag bewaren, delen, afdrukken en
  meenemen, en dat de gebruiker informatie en apparatuur alleen gebruikt voor het werk waarvoor hij ze heeft
  gekregen. [5.10.01]
- Elke medewerker krijgt de gedragsregels bij indiensttreding en bevestigt met een handtekening of een
  digitale bevestiging dat hij ze kent, voordat hij een account of apparatuur krijgt. HR bewaart de
  bevestiging in het personeelsdossier of in het uitgiftesysteem. Na een inhoudelijke wijziging van de
  gedragsregels bevestigen alle medewerkers binnen drie maanden opnieuw. [5.10.03]
- Voor inhuur, extern personeel en vrijwilligers staan de gedragsregels in het contract of de
  vrijwilligersovereenkomst, met een verwijzing naar de geldende huisregels. Inkoop en HR gebruiken daarvoor
  een vaste clausule. [5.10.02]
- Wie apparatuur in bruikleen krijgt, tekent een bruikleenovereenkomst waarin de gedragsregels staan.
  [[uitgiftepunt apparatuur: de functie die apparatuur uitgeeft en inneemt, bijvoorbeeld de servicedesk]]
  bewaart de overeenkomst in het uitgiftesysteem. [5.10.01]

::: als byod=ja
- De gedragsregels gelden ook voor eigen apparaten die een medewerker voor het werk gebruikt. Welke apparaten
  en diensten daarvoor zijn toegestaan en hoe ze zijn ingericht, staat in het beleid mobile device
  management. [5.10.01]
:::

### 3.4 Teruggeven

- Bij vertrek, einde van een contract of functiewijziging levert de gebruiker alle bedrijfsmiddelen in op of
  voor de laatste werkdag: apparatuur, toegangsmiddelen, authenticatiemiddelen, software en licenties, en
  informatie op papier of andere dragers. HR meldt het vertrek ten minste twee weken van tevoren aan
  [[uitgiftepunt apparatuur]]; het uitgiftepunt registreert de inname per bedrijfsmiddel en de beheerder van
  de inventaris verwerkt die. [5.11.01]
- Het uitgiftepunt vergelijkt elk kwartaal de vertrokken medewerkers en beëindigde contracten met de
  innameregistratie. Niet ingeleverde bedrijfsmiddelen worden geblokkeerd en teruggevorderd; de uitkomst
  staat in de innameregistratie. [5.11.01]
- Heeft een vertrekkende gebruiker kennis die de organisatie nodig heeft, bijvoorbeeld van een systeem of
  een lopend dossier, dan zorgt de leidinggevende dat die kennis vóór de laatste werkdag is vastgelegd of
  overgedragen aan een collega. [5.11.01]
- Informatie van de organisatie die de gebruiker op eigen apparatuur heeft, wordt op de laatste werkdag
  verwijderd. Valt het apparaat onder apparaatbeheer, dan wist de beheerder MDM de bedrijfsgegevens op
  afstand volgens het beleid mobile device management; anders bevestigt de gebruiker schriftelijk dat de
  informatie is verwijderd. [5.11.01]

### 3.5 Werken in beveiligde zones

De zones staan in het beleid fysieke toegang en beveiliging, paragraaf 3.1.

- Werken in zone 3 of 4 gebeurt alleen door personen die de eigenaar van de zone daarvoor heeft
  geautoriseerd, en alleen voor werkzaamheden die daar nodig zijn. De eigenaar van de zone legt werkzaamheden
  in zone 4 vooraf vast, met wie, wat en wanneer. [7.06.01]
- Wie alleen in zone 4 werkt, meldt zich bij binnenkomst en vertrek bij
  [[meldpunt beveiligde zones: de functie die weet wie er in een beveiligde zone werkt, bijvoorbeeld de receptie of de servicedesk]].
  Leveranciers werken in zone 3 en 4 onder begeleiding van een bevoegde medewerker, tenzij de eigenaar van de
  zone daar vooraf schriftelijk van afwijkt. [7.06.01]
- Een beveiligde zone die niet in gebruik is, is afgesloten. De eigenaar van de zone controleert elk kwartaal
  dat de zone afgesloten is en dat er geen apparatuur of informatie onbeheerd is achtergelaten. [7.06.01]

### 3.6 Apparatuur plaatsen en beschermen

- Servers, netwerkapparatuur en opslag staan in een zone die past bij het impactniveau van de informatie die
  ze verwerken, volgens de tabel in het beleid fysieke toegang en beveiliging. De eigenaar van het
  bedrijfsmiddel kiest de plaats bij ingebruikname en legt die in de inventaris vast. [7.08.01]
- Apparatuur staat zo opgesteld dat onbevoegden niet kunnen meekijken of meelezen: schermen zijn van de
  publieksruimte afgekeerd, printers in zone 2 geven afdrukken pas na aanmelding met een pas, en
  netwerkapparatuur staat in afgesloten kasten. [7.08.01]
- De eigenaar van het bedrijfsmiddel beschermt apparatuur tegen stof, water, warmte, trillingen en
  elektromagnetische storing, en beoordeelt dat bij elke verplaatsing. [7.08.01]
- Apparatuur met impactniveau kritiek of zeer ernstig of hoger voor beschikbaarheid staat zo dat één
  gebeurtenis (brand, water, stroomuitval) niet alle exemplaren tegelijk treft; redundante onderdelen staan
  in gescheiden ruimten. De eigenaar beoordeelt dat jaarlijks. [7.08.01]

### 3.7 Nutsvoorzieningen

- Apparatuur in zone 3 en 4 heeft stroom, koeling, netwerk en waar nodig water met een capaciteit en
  continuïteit die passen bij de hersteltijd uit het continuïteitsbeleid. [[lijneigenaar bedrijfsmiddelen]]
  legt per ruimte vast welke voorziening nodig is en welke capaciteit die moet hebben. [7.11.01]
- De beheerder van de ruimte bewaakt de nutsvoorzieningen op uitval en afwijkingen, met een automatische
  melding bij de beheerder, en laat ze onderhouden en testen volgens het schema van de leverancier en ten
  minste jaarlijks. De testrapporten zijn het bewijs. Noodstroom (UPS en aggregaat) volgt de eisen en
  testfrequenties uit het beleid fysieke toegang en beveiliging. [7.11.01]
- Noodverlichting en noodschakelaars voor stroom zijn aanwezig bij de in- en uitgangen van zone 3 en 4.
  Aansluitingen op stroom en netwerk voor apparatuur met impactniveau kritiek of zeer ernstig of hoger hebben
  meer dan één toevoer. [7.11.01]
- De leveranciers van nutsvoorzieningen en de contactgegevens voor storingen staan in
  [[storingslijst nutsvoorzieningen: het document met leveranciers en storingsnummers per locatie]]; de
  beheerder van de ruimte controleert die lijst jaarlijks. [7.11.01]

### 3.8 Apparatuur buiten de locaties

- Apparatuur die buiten de locaties van de organisatie wordt gebruikt (laptops, telefoons, tokens, apparatuur
  op thuiswerkplekken) staat in de inventaris met de gebruiker als beheerder. De gebruiker laat de apparatuur
  niet onbeheerd achter op openbare plaatsen, laat haar niet zichtbaar in een voertuig liggen en neemt haar
  op reis mee als handbagage. [7.09.01]
- De opslag van apparatuur buiten de locaties is versleuteld volgens het beleid cryptografie; mobiele
  apparaten voldoen aan het beleid mobile device management. Het meenemen van apparatuur die niet voor
  mobiel gebruik is uitgegeven, vraagt toestemming van de eigenaar van het bedrijfsmiddel; het uitgiftepunt
  registreert wie wat wanneer heeft meegenomen. [7.09.01]
- Verlies, diefstal of schade meldt de gebruiker direct bij [[uitgiftepunt apparatuur]]; het uitgiftepunt
  registreert de melding als beveiligingsincident volgens het beleid beveiligingsincidenten. [7.09.01]
- Voor thuiswerkplekken en werkplekken bij derden staan in de gedragsregels de eisen aan de werkplek: een
  ruimte die de gebruiker kan afsluiten, geen meekijken door huisgenoten of bezoekers, geen gedeeld gebruik
  van de apparatuur en geen aansluiting van onbekende randapparatuur. [7.09.01]

### 3.9 Onderhoud van apparatuur

- De eigenaar van het bedrijfsmiddel laat apparatuur onderhouden volgens het schema en de specificaties van
  de fabrikant, door bevoegde en geautoriseerde personen, en legt het onderhoudsschema in de inventaris vast.
  [7.13.01]
- Van elk onderhoud, elke storing en elke reparatie houdt de beheerder een registratie bij: datum,
  uitvoerder, wat is gedaan, en of er informatie op het apparaat stond. De beheerder bewaart de registratie
  zolang het apparaat in gebruik is en daarna nog een jaar. [7.13.01]
- Onderhoud op afstand door een leverancier gebeurt alleen via een toegang die de beheerder per
  onderhoudsbeurt opent en daarna sluit. De sessie wordt gelogd volgens het beleid logging en monitoring.
  [7.13.01]
- Apparatuur die voor onderhoud of reparatie de organisatie verlaat, gaat zonder opslag weg of wordt eerst
  gewist volgens het beleid afvoer en hergebruik van gegevensdragers. Na terugkomst controleert de beheerder
  of de apparatuur werkt zoals voor het onderhoud en of er geen ongeautoriseerde wijzigingen in hardware of
  configuratie zijn aangebracht, en legt dat vast in de onderhoudsregistratie. [7.13.01]

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| [[lijneigenaar bedrijfsmiddelen]] | Eigenaar van dit beleid en van de gedragsregels; de inventaris, de uitgifte- en innameprocedure en de eisen aan nutsvoorzieningen per ruimte |
| [[beheerder inventaris]] | Registratie, verwerking van mutaties, kwartaal- en jaarcontroles, afhandeling van afwijkingen |
| Eigenaar van een bedrijfsmiddel | Juiste registratie, classificatie, plaatsing, bescherming en onderhoud over de hele levenscyclus; toestemming voor meenemen buiten de locaties |
| [[uitgiftepunt apparatuur]] | Uitgifte en inname van apparatuur, bruikleenovereenkomsten, kwartaalvergelijking van vertrek met inname, registratie van verlies en diefstal |
| Eigenaar van een zone | Autoriseren van wie in zone 3 en 4 werkt, vooraf vastleggen van werkzaamheden in zone 4, kwartaalcontrole van afgesloten zones |
| HR en inkoop | Gedragsregels in arbeidsovereenkomst, inhuurcontract en vrijwilligersovereenkomst; tijdige melding van vertrek; eisen aan leveranciers in het contract |
| CISO | Advies over dit beleid, jaarlijkse toetsing van opzet en werking, beoordeling van afwijkingen |
| Medewerkers en inhuur | Gedragsregels naleven, apparatuur buiten de locaties beschermen, verlies of diefstal direct melden, bedrijfsmiddelen inleveren bij vertrek |

## 5. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in [[registratie van controles: het systeem waarin controles worden vastgelegd, bijvoorbeeld het ticketsysteem of het managementsysteem]];
afwijkingen gaan als bevinding naar het risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| BMB-01 | De inventaris van werkplekken, mobiele apparatuur en clouddiensten komt overeen met een tweede bron; afwijkingen zijn binnen een maand afgehandeld | [[beheerder inventaris]] | Per kwartaal | Vergelijkingsrapport met de afwijkingen en hun afhandeling | 5.09.01 |
| BMB-02 | Elk bedrijfsmiddel in de inventaris heeft een eigenaar, een classificatie en een onderhoudsschema, en de eigenaar heeft de registratie bevestigd | [[beheerder inventaris]] | Jaarlijks | Aantal bedrijfsmiddelen zonder eigenaar of registratie voor en na de controle, bevestigingen van de eigenaren | 5.09.01 |
| BMB-03 | Nieuwe medewerkers hebben de gedragsregels bevestigd voordat zij een account of apparatuur kregen, en contracten van externen bevatten de gedragsclausule | CISO | Jaarlijks | Steekproef van ten minste vijftien medewerkers en vijftien externen met de bevestigingen en contracten | 5.10.01, 5.10.02, 5.10.03 |
| BMB-04 | Vertrokken medewerkers en beëindigde contracten hebben alle bedrijfsmiddelen ingeleverd; niet ingeleverde middelen zijn geblokkeerd en teruggevorderd | [[uitgiftepunt apparatuur]] | Per kwartaal | Vergelijking van de personeelsmutaties met de innameregistratie | 5.11.01 |
| BMB-05 | Apparatuur in zone 3 en 4 staat in de zone die bij het impactniveau hoort, is beschermd tegen meekijken en omgevingsinvloeden, en alleen geautoriseerde personen hebben er gewerkt | Eigenaar van de zone | Halfjaarlijks | Rondgang met checklist per ruimte, vergelijking van de werkregistratie met de autorisaties | 7.06.01, 7.08.01 |
| BMB-06 | De nutsvoorzieningen van zone 3 en 4 zijn getest en onderhouden volgens schema, en het onderhoud aan apparatuur is uitgevoerd en geregistreerd | [[lijneigenaar bedrijfsmiddelen]] | Jaarlijks | Testrapporten van de nutsvoorzieningen, onderhoudsregistratie, storingslijst | 7.11.01, 7.13.01 |
| BMB-07 | Apparatuur buiten de locaties is versleuteld, geregistreerd op de gebruiker en meldingen van verlies of diefstal zijn als incident afgehandeld | CISO | Jaarlijks | Steekproef van ten minste tien apparaten uit de inventaris, incidentregistratie | 7.09.01 |
| BMB-08 | Leveranciers die apparatuur, ruimten of clouddiensten beheren leveren een geldige onafhankelijke verklaring over hun bedrijfsmiddelenbeheer en onderhoud | Contractbeheer | Jaarlijks | Verklaring per leverancier, beoordeling van de uitzonderingen | 5.09.01, 7.08.01, 7.11.01, 7.13.01 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De eigenaar
van het bedrijfsmiddel dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de
looptijd. De afwijking geldt pas na acceptatie van het risico door
[[risico-eigenaar: de manager die restrisico's accepteert]] en staat in het risicoregister; afwijkingen
worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid
informatieclassificatie (classificatie in de inventaris en de labels in de gedragsregels), het beleid fysieke
toegang en beveiliging (zones, noodstroom), het beleid afvoer en hergebruik van gegevensdragers (wissen voor
reparatie en afvoer), het beleid mobile device management (mobiele en eigen apparaten), het beleid
cryptografie (versleuteling buiten de locaties), het beleid screening en bewustzijn (gedragsregels bij
indiensttreding), het beleid logging en monitoring (onderhoud op afstand), het continuïteitsbeleid
(hersteltijden voor nutsvoorzieningen) en het beleid vulnerability- en patchmanagement, dat de inventaris als
bron gebruikt.
