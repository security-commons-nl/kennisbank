---
domein: gegevensdragers
titel: Beleid afvoer en hergebruik van gegevensdragers
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor gegevensdragers: alles waarop
informatie van de organisatie is opgeslagen en dat los kan worden gebruikt, vervoerd, hergebruikt of
afgevoerd. Het doel is dat informatie niet uitlekt bij gebruik, transport, reparatie, hergebruik of afvoer
van die dragers, en dat informatie die niet meer nodig is ook uit de systemen verdwijnt. Het gaat over de
ISO-beheersmaatregelen 7.10, 7.14 en 8.10.

**Voor wie.** Het beleid is primair bedoeld voor de afdeling die dragers en apparatuur beheert, wist en
afvoert, en voor de eigenaren van de informatie die erop staat. De gedragsregels gelden voor iedereen die
gegevensdragers van de organisatie gebruikt, beheert of vervoert: medewerkers, inhuur, stagiairs,
vrijwilligers en leveranciers.

**Waarop.** Verwijderbare media (USB-sticks, externe schijven, geheugenkaarten, optische schijven,
back-uptapes), vaste opslag in apparatuur (harde schijven en SSD's in werkplekken, servers, printers,
multifunctionals en netwerkapparatuur), opslag in mobiele apparaten, papier, en de informatie in systemen en
clouddiensten die gewist moet worden als zij niet meer nodig is. Is het wissen, vernietigen, vervoeren of
opslaan uitbesteed, bijvoorbeeld aan een vernietigingsbedrijf, een koerier of een clouddienst, dan gelden de
eisen uit dit beleid als minimumeis voor die leverancier. De organisatie legt dat vast in het contract en
toetst de naleving met een onafhankelijke verklaring, zoals een ISO 27001-certificaat of een ISAE 3402- of
ISAE 3000-rapport; het vastleggen loopt via het beleid informatiebeveiliging bij inkoop, het toetsen via het
beleid contractbeheer.

Buiten dit beleid vallen de inventaris en de inname van apparatuur (beleid bedrijfsmiddelenbeheer), de
versleutelingseisen zelf (beleid cryptografie), de bewaartermijnen uit de Archiefwet en de selectielijsten
(archiefbeheer) en het maken en bewaren van back-ups (beleid back-up en recovery).

## 2. Uitgangspunten

1. Informatie hoort in de systemen van de organisatie. Een verwijderbaar medium is de uitzondering en vraagt
   een besluit.
2. Een drager die de organisatie verlaat, bevat geen leesbare informatie van de organisatie meer, tenzij het
   transport daarvoor bedoeld is en beveiligd is.
3. Wissen is pas klaar als het is gecontroleerd en vastgelegd.
4. Informatie die niet meer nodig is, wordt gewist: bewaren zonder doel vergroot de schade bij een incident.

## 3. Beleidsregels

### 3.1 Gebruik van verwijderbare media

- Het opslaan van informatie op verwijderbare media is standaard niet toegestaan en technisch geblokkeerd op
  beheerde werkplekken. Een uitzondering vraagt de gebruiker aan bij
  [[aanvraagpunt uitzonderingen: de functie die uitzonderingen op dit beleid registreert, bijvoorbeeld de servicedesk]],
  met akkoord van de leidinggevende en, voor informatie met het label vertrouwelijk of hoger, van de CISO.
  Een uitzondering geldt ten hoogste een jaar en staat in het uitzonderingenregister. [7.10.01]
- Toegestane media zijn eigendom van de organisatie, staan in de inventaris met de gebruiker als beheerder
  en zijn versleuteld volgens het beleid cryptografie. Privémedia worden niet gebruikt voor informatie van de
  organisatie. [7.10.01]
- Een medium met informatie met het label vertrouwelijk of hoger bewaart de gebruiker achter slot als hij
  het niet gebruikt, en meldt hij bij verlies direct als beveiligingsincident. [7.10.01]
- Media die de organisatie niet meer nodig heeft, levert de gebruiker in bij
  [[uitgiftepunt apparatuur: de functie die apparatuur en media uitgeeft en inneemt, bijvoorbeeld de servicedesk]];
  het uitgiftepunt wist of vernietigt ze volgens paragraaf 3.2. [7.10.01]

### 3.2 Wissen en vernietigen

- [[lijneigenaar gegevensdragers: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd IT]] stelt een
  verwijderinstructie voor gegevensdragers vast en beoordeelt die jaarlijks. Die schrijft voor dat van elk
  herbruikbaar medium dat de organisatie verlaat (verkoop, retour aan leverancier, reparatie, schenking,
  einde lease) eerst alle informatie onherstelbaar wordt verwijderd. Het gaat daarbij om de hele drager,
  niet alleen om de bestanden die de gebruiker kent. [7.10.01]
- De verwijderinstructie noemt per type drager en per vertrouwelijkheidslabel de toegestane methode:
  cryptografisch wissen of overschrijven met een erkende methode voor herbruikbare dragers, en fysieke
  vernietiging (versnipperen, desintegreren) voor dragers die niet betrouwbaar te wissen zijn, defecte
  dragers en dragers met informatie met het label geheim. [7.10.01]
- Voor het wissen gebruikt de organisatie waar mogelijk producten met een positief inzetadvies van het NBV.
  Wijkt de organisatie daarvan af, dan legt de CISO de reden en het gekozen alternatief vast. [7.10.02]
- Na het wissen controleert de uitvoerder per drager met een steekproef of een verificatiefunctie van het
  wisproduct dat er geen informatie meer te herstellen is. Van elke gewiste of vernietigde drager maakt de
  uitvoerder een verslag met: kenmerk uit de inventaris, methode, product en versie, datum, uitvoerder en
  uitkomst van de controle. Het verslag wordt ten minste zeven jaar bewaard. [7.10.02]
- Laat de organisatie het wissen of vernietigen uitvoeren door een leverancier, dan staan de methode, de
  controle en het verslag per drager (vernietigingscertificaat met serienummers) in het contract.
  [[uitgiftepunt apparatuur]] vergelijkt elke levering van certificaten met de lijst van afgegeven dragers en
  legt verschillen vast als afwijking. [7.10.02]
- Papier met informatie met het label intern of hoger gaat in afgesloten containers voor vernietiging; de
  vernietigingsleverancier levert per lediging een certificaat. [7.10.01]

### 3.3 Afvoer en hergebruik van apparatuur

- Apparatuur met vaste opslag die de organisatie verlaat of een andere gebruiker krijgt (verkoop, schenking,
  einde lease, hergebruik binnen de organisatie, afvoer als afval) gaat eerst langs
  [[uitgiftepunt apparatuur]]. Het uitgiftepunt stelt vast of de apparatuur opslag bevat, wist die volgens
  de verwijderinstructie of haalt de opslag eruit voor vernietiging, en legt dat vast in het wisverslag.
  [7.14.01]
- Bij hergebruik binnen de organisatie wordt de apparatuur teruggezet naar de fabrieksinstellingen of
  opnieuw geïnstalleerd, zodat de nieuwe gebruiker geen gegevens, accounts of licenties van de vorige
  gebruiker ziet. [7.14.01]
- Voor afvoer verwijdert het uitgiftepunt licenties en registraties van de apparatuur (apparaatbeheer,
  cloudtenant, netwerkbeheer), haalt stickers en labels van de organisatie eraf en zet de apparatuur in de
  inventaris op afgevoerd met de datum en de bestemming. [7.14.01]
- Apparatuur die voor reparatie of garantie de organisatie verlaat, gaat zonder opslag weg of wordt eerst
  gewist. Kan dat niet, dan gaat de reparatie alleen naar een leverancier met een geheimhoudingsclausule en
  wordt de drager bij terugkomst gewist of vervangen; het uitgiftepunt legt dat per reparatie vast.
  [7.14.01]
- Printers, multifunctionals en netwerkapparatuur met opslag vallen onder dezelfde regels; bij einde van een
  huur- of leasecontract staat in het contract dat de leverancier de opslag wist of afgeeft en daarvan een
  verslag levert. [7.14.01]

### 3.4 Wissen van informatie in systemen

- De proceseigenaar legt per gegevensverzameling vast hoe lang de informatie nodig is, op basis van de
  bewaartermijnen uit de selectielijst en de wet, en zorgt dat de systeemeigenaar de informatie na afloop van
  die termijn wist of vernietigt, tenzij een wettelijke bewaarplicht of een lopend juridisch geschil dat
  verhindert. [8.10.01]
- Systemen zijn zo ingericht dat verlopen informatie automatisch wordt gewist of ter vernietiging wordt
  aangeboden; waar dat niet kan, voert de systeemeigenaar het wissen ten minste jaarlijks handmatig uit en
  legt dat vast. [8.10.01]
- Verzoeken van betrokkenen om wissing op grond van de AVG handelt de proceseigenaar af binnen de wettelijke
  termijn van een maand, in alle systemen en back-ups waarin de gegevens staan, met een vastlegging van wat
  is gewist. [8.10.01]
- Bij het einde van een clouddienst of een contract met een leverancier staat in het contract dat de
  leverancier de informatie van de organisatie binnen een afgesproken termijn wist, ook uit back-ups, en dat
  schriftelijk bevestigt. Contractbeheer controleert de bevestiging bij elke beëindiging. [8.10.01]
- Test- en ontwikkelomgevingen bevatten geen productiegegevens met het label vertrouwelijk of hoger, tenzij
  de proceseigenaar daar schriftelijk mee instemt; die gegevens worden na afloop van de test direct gewist.
  [8.10.01]
- Informatie die de organisatie wist, verdwijnt ook uit kopieën die medewerkers lokaal of in
  samenwerkingsomgevingen hebben bewaard; de gedragsregels uit het beleid bedrijfsmiddelenbeheer verbieden
  het bewaren van eigen kopieën buiten de systemen van de organisatie. [8.10.01]

### 3.5 Transport

- Gegevensdragers met informatie worden vervoerd volgens een vaste transportprocedure: versleuteld, in een
  verzegelde verpakking en met een registratie van inhoud, afzender, ontvanger, vervoerder, datum van
  verzending en bevestiging van ontvangst. [[uitgiftepunt apparatuur]] houdt de transportregistratie bij.
  [7.10.03]
- Wie dragers met informatie met het label vertrouwelijk of hoger vervoert of laat vervoeren, is daartoe
  door de eigenaar van de informatie gemachtigd; de machtiging staat in de transportregistratie. [7.10.03]
- De organisatie zet voor het vervoer van geclassificeerde informatie alleen koeriers of transporteurs in die
  voldoen aan vooraf vastgestelde betrouwbaarheidseisen. Die eisen staan in
  [[eisen aan koeriers: het document met de betrouwbaarheidseisen, zoals VOG of screening van chauffeurs, verzegeling, volgsysteem en overdrachtsprotocol]]
  en inkoop toetst ze bij de selectie en bij elke contractverlenging. [7.10.03]
- Kan informatie op een drager niet worden versleuteld, dan vervoert een gemachtigde medewerker de drager
  persoonlijk of gaat het transport in een verzegelde, afgesloten verpakking met overdracht tegen
  handtekening. [7.10.03]
- Back-upmedia die naar een andere locatie gaan, volgen dezelfde transportprocedure; het beleid back-up en
  recovery zegt hoe vaak en waarheen. [7.10.03]

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| [[lijneigenaar gegevensdragers]] | Eigenaar van dit beleid, de verwijderinstructie en de transportprocedure; jaarlijkse beoordeling ervan |
| [[uitgiftepunt apparatuur]] | Wissen, vernietigen, controle en verslag per drager en per apparaat; registratie in de inventaris; transportregistratie; vergelijking van vernietigingscertificaten |
| Proceseigenaar (eigenaar van de informatie) | Bewaartermijnen per gegevensverzameling, wissing na afloop, afhandeling van wisverzoeken, machtiging voor transport, instemming met productiegegevens in testomgevingen |
| Systeemeigenaar | Inrichting van automatisch wissen, jaarlijks handmatig wissen waar nodig, vastlegging |
| Inkoop en contractbeheer | Eisen aan wis- en vernietigingsleveranciers, koeriers en clouddiensten in het contract; controle van wisbevestigingen bij beëindiging |
| CISO | Advies, jaarlijkse toetsing van opzet en werking van dit beleid, akkoord op uitzonderingen voor vertrouwelijk en hoger, besluit bij afwijking van het NBV-advies |
| Medewerkers en inhuur | Geen informatie op losse dragers zonder uitzondering, media achter slot bewaren, verlies van een drager direct melden als incident |

## 5. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in [[registratie van controles: het systeem waarin controles worden vastgelegd, bijvoorbeeld het ticketsysteem of het managementsysteem]];
afwijkingen gaan als bevinding naar het risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| AHG-01 | Elke drager en elk apparaat met opslag dat in de inventaris op afgevoerd, gerepareerd of hergebruikt staat, heeft een wisverslag of een vernietigingscertificaat met serienummer | [[lijneigenaar gegevensdragers]] | Per kwartaal | Vergelijking van de inventaris met de wisverslagen en certificaten, lijst van dragers zonder verslag en hun afhandeling | 7.10.01, 7.10.02, 7.14.01 |
| AHG-02 | Gewiste dragers bevatten geen herstelbare informatie en de gebruikte wisproducten hebben een NBV-inzetadvies of een vastgelegd alternatief | CISO | Jaarlijks | Steekproef van ten minste vijf gewiste dragers, gecontroleerd met forensische software; lijst van wisproducten | 7.10.02 |
| AHG-03 | Uitzonderingen voor verwijderbare media zijn geregistreerd, goedgekeurd en niet ouder dan een jaar; de blokkering op beheerde werkplekken werkt | [[aanvraagpunt uitzonderingen]] | Jaarlijks | Uitzonderingenregister, testverslag van de blokkering, lijst van ingetrokken uitzonderingen | 7.10.01 |
| AHG-04 | Transporten van dragers zijn geregistreerd met machtiging en ontvangstbevestiging, en ingezette koeriers en vernietigingsleveranciers voldoen aan de vastgestelde eisen | Contractbeheer | Jaarlijks | Transportregistratie, toetsverslag per leverancier, verklaringen van leveranciers | 7.10.03 |
| AHG-05 | Informatie waarvan de bewaartermijn is verlopen is gewist, wisverzoeken van betrokkenen zijn binnen een maand afgehandeld en beëindigde leveranciers hebben wissing bevestigd | Proceseigenaar, met een overzicht van de CISO | Jaarlijks | Overzicht per gegevensverzameling van de bewaartermijn en de laatste wissing, register van wisverzoeken, wisbevestigingen van leveranciers | 8.10.01 |
| AHG-06 | Hergebruikte en afgevoerde apparatuur is teruggezet naar de fabrieksinstellingen, uit de registraties verwijderd en in de inventaris bijgewerkt | [[uitgiftepunt apparatuur]] | Halfjaarlijks | Steekproef van ten minste vijf apparaten tegen apparaatbeheer, cloudtenant en inventaris | 7.14.01 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De eigenaar
van de informatie dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de
looptijd. De afwijking geldt pas na acceptatie van het risico door
[[risico-eigenaar: de manager die restrisico's accepteert]] en staat in het risicoregister; afwijkingen
worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid
bedrijfsmiddelenbeheer (inventaris, inname en gedragsregels), het beleid informatieclassificatie (labels die
de methode bepalen), het beleid cryptografie (versleuteling van dragers), het beleid mobile device management
(wissen op afstand), het beleid back-up en recovery (transport en opslag van back-upmedia, wissen uit
back-ups), het beleid beveiligingsincidenten (verloren dragers), het beleid informatiebeveiliging bij inkoop
en contractbeheer (eisen aan en verklaringen van leveranciers) en het archiefbeheer van de organisatie
(bewaartermijnen en selectielijsten).
