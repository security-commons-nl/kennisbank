# Beleid afvoer en hergebruik van gegevensdragers

Beleid informatiebeveiliging, BIO 2.0-domein *Afvoer en hergebruik gegevensdragers*. Status: concept, vast te stellen door de organisatie zelf.

Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor gegevensdragers: alles waarop
informatie van de organisatie is opgeslagen en dat los kan worden gebruikt, vervoerd, hergebruikt of
afgevoerd. Het doel is dat informatie niet uitlekt bij gebruik, transport, reparatie, hergebruik of afvoer
van die dragers. Het geldt voor iedereen die gegevensdragers van de organisatie gebruikt, beheert of
vervoert, ook leveranciers. Het gaat over de ISO-beheersmaatregelen 7.10, 7.14 en 8.10.

Gegevensdragers zijn in dit beleid: verwijderbare media (USB-sticks, externe schijven, geheugenkaarten,
optische schijven, back-uptapes), vaste opslag in apparatuur (harde schijven en SSD's in werkplekken,
servers, printers, multifunctionals en netwerkapparatuur), opslag in mobiele apparaten en papier.

Buiten dit beleid vallen de inventaris en de inname van apparatuur (beleid bedrijfsmiddelenbeheer) en de
versleutelingseisen zelf (beleid cryptografie).

## 2. Uitgangspunten

1. Informatie hoort in de systemen van de organisatie, niet op losse dragers. Een verwijderbaar medium is de
   uitzondering.
2. Een drager die de organisatie verlaat, bevat geen leesbare informatie van de organisatie meer, tenzij het
   transport daarvoor bedoeld is en beveiligd is.
3. Wissen is pas klaar als het is gecontroleerd en vastgelegd.

## 3. Beleidsregels

### 3.1 Gebruik van verwijderbare media

- Het opslaan van informatie op verwijderbare media is standaard niet toegestaan en technisch geblokkeerd op
  beheerde werkplekken. Een uitzondering vraagt de gebruiker aan bij
  **[aanvraagpunt uitzonderingen]**,
  met akkoord van de leidinggevende en, voor informatie met een vertrouwelijkheid van BBN2 of hoger, van de
  CISO. Uitzonderingen gelden ten hoogste een jaar.
- Toegestane media zijn eigendom van de organisatie, staan in de inventaris en zijn versleuteld volgens het
  beleid cryptografie. Privémedia worden niet gebruikt voor informatie van de organisatie.

### 3.2 Wissen en vernietigen

- De organisatie heeft een verwijderinstructie voor gegevensdragers. Die schrijft voor dat van elk
  herbruikbaar medium dat de organisatie verlaat (verkoop, retour aan leverancier, reparatie, schenking,
  einde lease) eerst alle informatie onherstelbaar wordt verwijderd. Het gaat daarbij om de hele drager, niet
  alleen om de bestanden die de gebruiker kent. [7.10.01]
- De verwijderinstructie noemt per type drager en per classificatie de toegestane methode: cryptografisch
  wissen of overschrijven met een erkende methode voor herbruikbare dragers, en fysieke vernietiging
  (versnipperen, desintegreren) voor dragers die niet betrouwbaar te wissen zijn, defecte dragers en dragers
  met informatie van BBN3. [7.10.01]
- Voor het wissen gebruikt de organisatie waar mogelijk producten met een positief inzetadvies van het
  Nationaal Bureau voor Verbindingsbeveiliging. Wijkt de organisatie daarvan af, dan legt de CISO de reden en
  het gekozen alternatief vast. [7.10.02]
- Na het wissen controleert de uitvoerder per drager met een steekproef of een verificatiefunctie van het
  wisproduct dat er geen informatie meer te herstellen is. Van elke gewiste of vernietigde drager wordt een
  verslag gemaakt met: kenmerk uit de inventaris, methode, product en versie, datum, uitvoerder en uitkomst
  van de controle. Het verslag wordt ten minste zeven jaar bewaard. [7.10.02]
- Laat de organisatie het wissen of vernietigen uitvoeren door een leverancier, dan staan de methode, de
  controle en het verslag per drager (vernietigingscertificaat met serienummers) in het contract. De
  organisatie vergelijkt elke levering van certificaten met de lijst van afgegeven dragers. [7.10.02]
- Apparatuur met vaste opslag die voor reparatie of garantie de organisatie verlaat, gaat zonder die opslag
  weg of wordt eerst gewist. Kan dat niet, dan gaat de reparatie alleen naar een leverancier met een
  geheimhoudingsclausule en wordt de drager bij terugkomst gewist of vervangen.
- Papier met informatie van BBN1 of hoger gaat in afgesloten containers voor vernietiging.

### 3.3 Transport

- Gegevensdragers met informatie worden vervoerd volgens een vaste transportprocedure: versleuteld, in een
  verzegelde verpakking en met een registratie van inhoud, afzender, ontvanger, vervoerder, datum van
  verzending en bevestiging van ontvangst.
- Wie dragers met informatie van BBN2 of hoger vervoert of laat vervoeren, is daartoe door de eigenaar van de
  informatie gemachtigd.
- De organisatie zet voor het vervoer van geclassificeerde informatie alleen koeriers of transporteurs in die
  voldoen aan vooraf vastgestelde betrouwbaarheidseisen. Die eisen staan in
  **[eisen aan koeriers]**
  en worden bij de selectie en bij elke contractverlenging getoetst. [7.10.03]
- Kan informatie op een drager niet worden versleuteld, dan vervoert een gemachtigde medewerker de drager
  persoonlijk of gaat het transport in een verzegelde, afgesloten verpakking met overdracht tegen handtekening.

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| **[lijneigenaar gegevensdragers]** | Uitvoering van dit beleid, de verwijderinstructie en de transportprocedure |
| Servicedesk of beheer | Wissen, vernietigen, controle en verslag per drager; registratie in de inventaris |
| Eigenaar van de informatie | Machtiging voor transport van informatie van BBN2 of hoger |
| Inkoop | Eisen aan wis- en vernietigingsleveranciers en aan koeriers in het contract |
| CISO | Advies, toetsing van dit beleid, akkoord op uitzonderingen en op afwijkingen van het NBV-advies |
| Medewerkers | Geen informatie op losse dragers zonder uitzondering, verlies van een drager direct melden als incident |

## 5. Naleving en bewaking

- Per kwartaal: vergelijking van de afgevoerde dragers in de inventaris met de wisverslagen en
  vernietigingscertificaten; bewijs is de vergelijking met de dragers zonder verslag en hun afhandeling.
- Jaarlijks: steekproef van ten minste vijf gewiste dragers die met forensische software worden gecontroleerd
  op herstelbare informatie.
- Jaarlijks: controle van de lijst met uitzonderingen voor verwijderbare media; verlopen uitzonderingen worden
  ingetrokken.
- Jaarlijks: toets van de ingezette koeriers en vernietigingsleveranciers aan de vastgestelde eisen.
- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie; een verloren drager met
  informatie is een beveiligingsincident.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid
bedrijfsmiddelenbeheer (inventaris en inname), het beleid informatieclassificatie (niveaus die de methode
bepalen), het beleid cryptografie (versleuteling van dragers), het beleid mobile device management (wissen op
afstand) en het beleid back-up en recovery (transport en opslag van back-upmedia).

## Bijlage: BIO 2.0-maatregelen

De overheidsmaatregelen van dit domein (3) en waar dit stuk ze invult. Nummers volgens BIO2 v1.3 definitief - 9 januari 2026; de tekst van de maatregel staat bij het CIP.

| Maatregel | Titel | In dit stuk |
|---|---|---|
| 7.10.01 | Opslagmedia | 3.2 Wissen en vernietigen |
| 7.10.02 | Opslagmedia | 3.2 Wissen en vernietigen |
| 7.10.03 | Opslagmedia | 3.3 Transport |

## Nog in te vullen

- **aanvraagpunt uitzonderingen**: de functie die uitzonderingen op dit beleid registreert, bijvoorbeeld de servicedesk
- **eisen aan koeriers**: het document met de betrouwbaarheidseisen, zoals VOG of screening van chauffeurs, verzegeling, volgsysteem en overdrachtsprotocol
- **lijneigenaar gegevensdragers**: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd IT
