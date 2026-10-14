# Beleid bedrijfsmiddelenbeheer

Beleid informatiebeveiliging, BIO 2.0-domein *Bedrijfsmiddelenbeheer*. Status: concept, vast te stellen door de organisatie zelf.

Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor het beheer van bedrijfsmiddelen: de
informatie zelf en alles waarmee die wordt verwerkt, opgeslagen of doorgegeven. Het regelt welke
bedrijfsmiddelen de organisatie heeft, wie er eigenaar van is, hoe ze gebruikt mogen worden en hoe ze
terugkomen als iemand vertrekt. Het geldt voor medewerkers, inhuur, stagiairs, vrijwilligers en leveranciers
die bedrijfsmiddelen van de organisatie gebruiken. Het gaat over de ISO-beheersmaatregelen 5.09 tot en met
5.11, 7.06, 7.08, 7.09, 7.11 en 7.13.

Onder bedrijfsmiddelen vallen in dit beleid: hardware (servers, netwerkapparatuur, werkplekken, printers),
eindgebruikersapparaten en mobiele apparatuur, verwijderbare opslagmedia, authenticatiemiddelen (tokens,
smartcards, sleutels), software en clouddiensten, en gegevensverzamelingen.

Buiten dit beleid vallen het classificeren en labelen van informatie (beleid informatieclassificatie), het
wissen en afvoeren van opslagmedia (beleid afvoer en hergebruik van gegevensdragers) en de inrichting van
mobiele apparaten (beleid mobile device management).

## 2. Uitgangspunten

1. Wat niet in de inventaris staat, wordt niet beveiligd. De inventaris is daarom de basis voor
   patchmanagement, toegangsbeheer, back-up en controle.
2. Elk bedrijfsmiddel heeft één eigenaar: een functie of organisatieonderdeel dat over de hele levenscyclus
   verantwoordelijk is, van aanschaf tot afvoer.
3. Wie een bedrijfsmiddel gebruikt, kent de gedragsregels en heeft dat aantoonbaar bevestigd.

## 3. Beleidsregels

### 3.1 Inventaris

- De organisatie houdt één inventaris bij van alle bedrijfsmiddelen die van belang zijn voor
  informatieverwerking, bijvoorbeeld in een CMDB. De inventaris omvat ook bedrijfsmiddelen op afstand
  (thuiswerkplekken, mobiele apparatuur), clouddiensten en apparaten die regelmatig op het netwerk zijn
  aangesloten zonder dat de organisatie ze beheert, zoals apparatuur van leveranciers. [5.09.01]
- Per bedrijfsmiddel legt de inventaris ten minste vast: uniek kenmerk, type, eigenaar, locatie of
  leverancier, gebruiker of beheerder, classificatie, bedrijfsprocessen die ervan afhangen, versie of
  configuratie en de datum van ingebruikname en einde ondersteuning. [5.09.01]
- Elke wijziging in de levenscyclus (aanschaf, uitgifte, verplaatsing, reparatie, inname, afvoer) wordt in de
  inventaris verwerkt via het wijzigingsproces of de uitgifte- en innameprocedure.
- De organisatie controleert de volledigheid en actualiteit van de inventaris ten minste elk kwartaal voor
  werkplekken, mobiele apparatuur en clouddiensten en ten minste jaarlijks voor de overige bedrijfsmiddelen.
  Dat gebeurt door de inventaris te vergelijken met een tweede bron (netwerkscan, beheertool, facturen of
  licentieoverzichten). Bedrijfsmiddelen zonder eigenaar of zonder registratie worden binnen een maand
  opgelost of buiten gebruik gesteld. [5.09.01]

> **Alleen als: Hoe ziet je werkplek eruit? «Cloudwerkplek (bijvoorbeeld Microsoft 365)»**
>
> - Werkplekken en mobiele apparaten worden geregistreerd via het centrale endpointbeheer van de cloudwerkplek.
>   Alleen apparaten die daar zijn ingeschreven krijgen toegang tot bedrijfsinformatie, zodat de registratie
>   van werkplekken vanzelf volledig is. De lijst met cloudtenants, abonnementen en gekoppelde apps maakt deel
>   uit van de inventaris en wordt per kwartaal vergeleken met de inkoopadministratie. [5.09.01]

> **Alleen als: Hoe ziet je werkplek eruit? «Hybride: cloud naast een virtuele of lokale werkplek»**
>
> - Werkplekken staan zowel in het cloudendpointbeheer als in het beheer van de lokale of virtuele omgeving.
>   De kwartaalcontrole vergelijkt beide registraties met elkaar en met de inventaris; een apparaat dat in één
>   bron ontbreekt, is een afwijking. [5.09.01]

> **Alleen als: Hoe ziet je werkplek eruit? «On-premises»**
>
> - Werkplekken en servers in het eigen netwerk worden ten minste maandelijks met een netwerkscan of
>   beheertool vergeleken met de inventaris. Onbekende apparaten op het netwerk worden binnen een week
>   geïdentificeerd en geregistreerd of van het netwerk verwijderd. [5.09.01]

> **Alleen als: Heb je operationele technologie (OT)? «Beperkt: gebouwbeheer, toegang, camera's»**
>
> - Operationele technologie in gebouwen (gebouwbeheer, toegangscontrole, camera's) staat in dezelfde
>   inventaris, met per installatie de eigenaar, de leverancier die het onderhoud doet, de manier waarop die op
>   afstand toegang heeft en de softwareversie. [5.09.01]

> **Alleen als: Heb je operationele technologie (OT)? «Substantieel: bruggen, gemalen, verkeer, zuivering»**
>
> - Operationele technologie (bijvoorbeeld gemalen, bruggen, verkeersinstallaties, zuivering) heeft een eigen
>   OT-inventaris die deel uitmaakt van de inventaris van de organisatie. Per component staan daarin de
>   eigenaar, de fysieke locatie, het netwerksegment, de firmware- of softwareversie, de leverancier, de
>   toegang op afstand en de procesfunctie die ervan afhangt. [5.09.01]
> - De OT-inventaris wordt ten minste elk halfjaar gecontroleerd met een passieve netwerkinventarisatie of een
>   fysieke opname op locatie; actieve scans op OT-netwerken gebeuren alleen met akkoord van de eigenaar van de
>   installatie. [5.09.01]

### 3.2 Eigendom

- Elk bedrijfsmiddel in de inventaris heeft een eigenaar. Voor werkplekken, infrastructuur en ondersteunende
  software is dat
  **[eigenaar IT-middelen]**;
  voor bedrijfsapplicaties en gegevensverzamelingen is dat de proceseigenaar.
- De eigenaar zorgt dat het bedrijfsmiddel juist is geregistreerd, geclassificeerd en beveiligd, en dat het
  wordt afgevoerd als het niet meer nodig is.

### 3.3 Aanvaardbaar gebruik

- De organisatie heeft gedragsregels voor het gebruik van bedrijfsmiddelen, vastgelegd in
  **[gedragsregels bedrijfsmiddelen]**.
  Ze gaan ten minste over privégebruik, het installeren van software, het gebruik van clouddiensten buiten
  de organisatie, het meenemen van apparatuur en het melden van verlies of diefstal.
- Elke medewerker krijgt de gedragsregels bij indiensttreding en bevestigt met een handtekening of een
  digitale bevestiging dat hij ze kent, voordat hij een account of apparatuur krijgt. De bevestiging wordt in
  het personeelsdossier of in het uitgiftesysteem bewaard. Na een inhoudelijke wijziging van de gedragsregels
  bevestigen alle medewerkers opnieuw. [5.10.03]
- Voor inhuur, extern personeel en vrijwilligers staan de gedragsregels in het contract of de
  vrijwilligersovereenkomst, met een verwijzing naar de geldende huisregels. Inkoop en HR gebruiken daarvoor
  een vaste clausule. [5.10.02]
- Wie apparatuur in bruikleen krijgt, tekent een bruikleenovereenkomst waarin de gedragsregels staan.

### 3.4 Teruggeven

- Bij vertrek, einde van een contract of functiewijziging levert de gebruiker alle bedrijfsmiddelen in op of
  voor de laatste werkdag: apparatuur, toegangsmiddelen en informatie op papier of andere dragers. HR meldt
  het vertrek tijdig aan IT; IT verwerkt de inname in de inventaris.
- Informatie die de gebruiker op eigen apparatuur heeft, wordt verwijderd; waar het apparaat onder
  apparaatbeheer valt, gebeurt dat op afstand.

### 3.5 Apparatuur plaatsen, beschermen en onderhouden

- Servers, netwerkapparatuur en opslag staan in ruimten die passen bij hun classificatie volgens het beleid
  fysieke toegang en beveiliging. Werken in beveiligde zones gebeurt alleen door bevoegde personen; derden
  worden begeleid.
- Kritieke apparatuur heeft een stroomvoorziening en koeling die passen bij de hersteltijden uit het
  continuïteitsbeleid; de nutsvoorzieningen worden volgens het onderhoudsschema van de leverancier getest.
- Onderhoud aan apparatuur gebeurt volgens het schema van de fabrikant, door bevoegde partijen. Apparatuur die
  voor reparatie de organisatie verlaat, wordt eerst gewist of de opslag wordt eruit gehaald.
- Apparatuur buiten de locaties van de organisatie wordt niet onbeheerd achtergelaten op openbare plaatsen en
  is versleuteld volgens het beleid cryptografie.

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| **[lijneigenaar bedrijfsmiddelen]** | Uitvoering van dit beleid, de inventaris en de uitgifte- en innameprocedure |
| Beheerder van de inventaris | Registratie, kwartaal- en jaarcontroles, afhandeling van afwijkingen |
| Eigenaar van een bedrijfsmiddel | Juiste registratie, classificatie en beveiliging over de hele levenscyclus |
| HR en inkoop | Gedragsregels in arbeidsovereenkomst, inhuurcontract en vrijwilligersovereenkomst; tijdige melding van vertrek |
| CISO | Advies, toetsing van dit beleid en van de controles |
| Medewerkers | Gedragsregels naleven, verlies of diefstal direct melden, bedrijfsmiddelen inleveren bij vertrek |

## 5. Naleving en bewaking

- Per kwartaal: vergelijking van de inventaris met een tweede bron voor werkplekken, mobiele apparatuur en
  clouddiensten; bewijs is het vergelijkingsrapport met de afwijkingen en hun afhandeling.
- Jaarlijks: volledige controle van de inventaris inclusief eigendom; bewijs is het aantal bedrijfsmiddelen
  zonder eigenaar of registratie, voor en na de controle.
- Jaarlijks: steekproef van ten minste vijftien nieuwe medewerkers en vijftien externen op een bevestiging
  van de gedragsregels en een gedragsclausule in het contract.
- Per kwartaal: vergelijking van vertrokken medewerkers met de innameregistratie; niet ingeleverde middelen
  worden geblokkeerd en nagevorderd.
- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid
informatieclassificatie (classificatie in de inventaris), het beleid afvoer en hergebruik van
gegevensdragers, het beleid mobile device management, het beleid fysieke toegang en beveiliging, het beleid
screening en bewustzijn (gedragsregels bij indiensttreding) en het beleid vulnerability- en patchmanagement,
dat de inventaris als bron gebruikt.

## Bijlage: BIO 2.0-maatregelen

De overheidsmaatregelen van dit domein (3) en waar dit stuk ze invult. Nummers volgens BIO2 v1.3 definitief - 9 januari 2026; de tekst van de maatregel staat bij het CIP.

| Maatregel | Titel | In dit stuk |
|---|---|---|
| 5.09.01 | Inventarisatie van informatie en andere gerelateerde bedrijfsmiddelen | 3.1 Inventaris |
| 5.10.02 | Aanvaardbaar gebruik van informatie en andere gerelateerde bedrijfsmiddelen | 3.3 Aanvaardbaar gebruik |
| 5.10.03 | Aanvaardbaar gebruik van informatie en andere gerelateerde bedrijfsmiddelen | 3.3 Aanvaardbaar gebruik |

## Nog in te vullen

- **eigenaar IT-middelen**: de functie die eigenaar is van werkplekken en infrastructuur, bijvoorbeeld het hoofd IT
- **gedragsregels bedrijfsmiddelen**: het document met de huisregels of de gedragscode voor ICT-gebruik
- **lijneigenaar bedrijfsmiddelen**: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd IT
