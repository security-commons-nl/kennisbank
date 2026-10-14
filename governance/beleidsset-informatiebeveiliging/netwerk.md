# Beleid netwerkbeveiliging

Beleid informatiebeveiliging, BIO 2.0-domein *Netwerkbeveiliging*. Status: concept, vast te stellen door de organisatie zelf.

Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor het ontwerp, de inrichting, het
beheer en de bewaking van de netwerken van de organisatie, inclusief wifi en externe koppelingen. Het doel
is dat een aanvaller die ergens binnenkomt niet vrij verder kan, dat aanvallen op het netwerk worden
gezien en dat gegevens onderweg beschermd zijn. Het gaat over de ISO-beheersmaatregelen 8.20 tot en met
8.23.

Het beleid geldt voor alle netwerken en netwerkdiensten die de organisatie gebruikt, ook als een
leverancier ze levert of beheert, en voor iedereen die netwerkcomponenten ontwerpt, beheert of aansluit.

Buiten dit beleid vallen de logging van netwerkcomponenten (beleid logging en monitoring), de keuze van
cryptografische middelen in het algemeen (beleid cryptografie) en de fysieke beveiliging van patchkasten
(beleid fysieke toegang en beveiliging).

## 2. Uitgangspunten

1. Het netwerk is opgedeeld in segmenten. Verkeer tussen segmenten is standaard dicht en wordt alleen
   toegestaan waar dat nodig is.
2. Elk segment heeft een beveiligingsniveau. Wat erin zit, en wat ermee verbonden is, voldoet aan dat
   niveau.
3. Toegang hangt af van de identiteit van gebruiker en apparaat, ook binnen het eigen netwerk.

## 3. Beleidsregels

### 3.1 Netwerkontwerp en segmentatie

- Er is een actueel netwerkontwerp met de segmenten, hun beveiligingsniveau, de koppelpunten en de
  toegestane verkeersstromen. De netwerkarchitect werkt het bij bij elke grote wijziging en beoordeelt het
  ten minste jaarlijks.
- Elk segment heeft een vastgelegd beveiligingsniveau, afgeleid van de hoogste classificatie van de
  informatie en systemen erin. Ten minste gescheiden zijn: gebruikers, servers, beheer, gasten en
  voorzieningen van derden. [8.22.01]
- De firewallregels tussen segmenten en naar buiten worden ten minste jaarlijks beoordeeld. Regels zonder
  eigenaar of zonder aantoonbare noodzaak worden verwijderd.
- Werkplekken kunnen geen verkeer tussen segmenten doorsturen.

> **Alleen als: Heb je operationele technologie (OT)? «Beperkt: gebouwbeheer, toegang, camera's»**
>
> - Gebouwbeheer, toegangscontrole en camera's staan in een eigen segment met een eigen beveiligingsniveau.
>   Vanuit dit segment is er geen verbinding met het kantoornetwerk; de leverancier krijgt beheertoegang
>   alleen via de beheerroute van de organisatie. [8.22.01]

> **Alleen als: Heb je operationele technologie (OT)? «Substantieel: bruggen, gemalen, verkeer, zuivering»**
>
> - Operationele technologie (gemalen, bruggen, sluizen, verkeersinstallaties, zuivering) staat in een
>   eigen netwerk, gescheiden van het kantoornetwerk volgens een zonemodel, bijvoorbeeld uit IEC 62443.
>   Elke zone heeft een beveiligingsniveau en elke verbinding tussen zones loopt via een gecontroleerd
>   koppelpunt. [8.22.01]
> - Het OT-netwerk heeft geen directe verbinding met internet. Toegang op afstand, ook van leveranciers,
>   verloopt via een aparte beheeromgeving met tweefactorauthenticatie, op verzoek aangezet en per sessie
>   gelogd. [8.20.02]
> - Verkeer van en naar het OT-netwerk wordt apart bewaakt met detectie die OT-protocollen herkent. [8.21.02]

### 3.2 Netwerkcomponenten en beheer

- Netwerkcomponenten voldoen ten minste aan het beveiligingsniveau van het segment waarin ze staan: een
  component in een segment met niveau hoog heeft de hardening, firmware-updates en beheerbeveiliging die
  bij dat niveau horen. [8.20.01]
- De beheerinterfaces van netwerkcomponenten zijn alleen bereikbaar vanuit een apart beheersegment en
  niet vanuit het gebruikersnetwerk of internet. Beheer gebeurt met persoonsgebonden accounts en
  tweefactorauthenticatie. [8.20.02]
- Standaardwachtwoorden en ongebruikte diensten op netwerkcomponenten worden vóór ingebruikname
  verwijderd. De configuratie van elke component staat in een back-up en wijzigingen lopen via
  wijzigingsbeheer.
- Een apparaat krijgt pas toegang tot het bedrijfsnetwerk na authenticatie van apparaat en gebruiker.

> **Alleen als: Wie beheert je IT? «Eigen beheer»**
>
> - De eigen netwerkbeheerders beheren de componenten. Een beheerder die netwerkcomponenten beheert, beoordeelt
>   niet zelf de monitoring van dat beheer.

> **Alleen als: Wie beheert je IT? «Regie: eigen organisatie stuurt, beheer is uitbesteed» of «Volledig uitbesteed»**
>
> - De netwerkdienst is uitbesteed. Het contract legt de beveiligingseisen uit dit beleid vast:
>   segmentatie, beheer via een apart beheersegment, patchtermijnen voor netwerkcomponenten, de levering
>   van logging en een jaarlijkse rapportage waarmee de leverancier aantoont dat hij eraan voldoet. [8.20.01, 8.20.02]
> - De partij die het netwerk beheert, controleert niet zelf de beveiliging ervan; de organisatie laat de
>   controle doen door een andere partij of doet die zelf.

### 3.3 Koppelpunten en bewaking

- Elk koppelpunt met internet of een andere onvertrouwde zone heeft een firewall en maatregelen tegen
  aanvallen op de beschikbaarheid, zoals DDoS-bescherming. Tussen segmenten met een verschillend
  beveiligingsniveau zijn maatregelen die het misbruik van één segment beperken tot dat segment. [8.21.01]
- Verkeer van en naar de vertrouwde omgeving wordt bewaakt met detectievoorzieningen die verdacht verkeer
  signaleren, zoals een netwerkdetectiesysteem of de detectiefunctie van de firewall. [8.21.02]
- Nieuwe dreigingen die bij deze bewaking worden ontdekt, worden binnen de juridische kaders gedeeld met
  de sectorale CERT, zodat andere overheden zich kunnen beschermen. [8.21.03]
- Internetverkeer van werkplekken loopt via een webfilter dat bekende kwaadaardige en ongewenste sites
  blokkeert. Uitzonderingen vraagt de leidinggevende aan bij de servicedesk.

> **Alleen als: Wie bewaakt je omgeving op aanvallen? «Eigen SOC» of «Uitbesteed SOC of MDR-dienst»**
>
> - Het SOC beoordeelt de meldingen van de netwerkdetectie en deelt nieuwe dreigingen volgens de procedure
>   met de CERT. [8.21.02, 8.21.03]

> **Alleen als: Wie bewaakt je omgeving op aanvallen? «Geen structurele detectie»**
>
> - Er is geen SOC. De meldingen van de netwerkdetectie gaan naar de netwerkbeheerder, die ze elke werkdag
>   beoordeelt en opvallende meldingen aan de CISO doorzet. De CISO deelt nieuwe dreigingen met de CERT. [8.21.02, 8.21.03]

> **Alleen als: Waar draaien je systemen? «Eigen datacenter of serverruimte»**
>
> - Het eigen datacenter heeft een eigen koppelpunt met internet. De organisatie neemt DDoS-bescherming af
>   bij de internetleverancier en test die jaarlijks. [8.21.01]

> **Alleen als: Waar draaien je systemen? «Hostingpartij (IaaS, gedeeld datacenter)»**
>
> - De verbinding met de hostingpartij loopt over een versleutelde verbinding of een eigen lijn. De
>   hostingpartij scheidt de omgeving van de organisatie van die van andere klanten en levert
>   DDoS-bescherming op het koppelpunt met internet, vastgelegd in het contract. [8.21.01, 8.21.04]

> **Alleen als: Waar draaien je systemen? «Vooral SaaS en publieke cloud»**
>
> - De meeste diensten draaien bij SaaS- en cloudleveranciers. Werkplekken maken daarom rechtstreeks
>   verbinding met internet. Toegang tot clouddiensten hangt af van identiteit en apparaatstatus; de
>   leverancier levert de bescherming tegen aanvallen op de beschikbaarheid. De organisatie bewaakt het
>   verkeer naar clouddiensten via de werkplek en de logging van de clouddienst. [8.21.01, 8.21.02]

### 3.4 Versleuteling onderweg

- Gegevens die over draadloze verbindingen gaan, en over bedrade verbindingen buiten het gebied dat de
  organisatie fysiek beheert, worden versleuteld. Alleen gegevens die nodig zijn om de verbinding tot
  stand te brengen, blijven onversleuteld. [8.21.04]
- De sterkte van de versleuteling volgt uit de classificatie en uit hoe lang de gegevens beschermd moeten
  blijven. Waar mogelijk gebruikt de organisatie middelen met een positief inzetadvies van het NBV. Is er
  geen geadviseerd middel, dan kiest de netwerkarchitect in overleg met de CISO een andere geschikte
  methode en legt die keuze vast. [8.21.04]
- Verbindingen tussen locaties en met externe partijen lopen via een VPN of versleutelde lijn. Thuiswerkers
  maken verbinding via een versleutelde verbinding met tweefactorauthenticatie.

### 3.5 Wifi

- Het bedrijfswifi is alleen toegankelijk voor beheerde apparaten, na authenticatie van apparaat en
  gebruiker, en is versleuteld volgens de geldende standaard. [8.21.04]
- Gastwifi, ook een landelijk roamingnetwerk voor bezoekende ambtenaren, staat in een apart segment zonder
  toegang tot het bedrijfsnetwerk. Er is geen open en onversleuteld netwerk. [8.22.01]
- De organisatie zoekt jaarlijks naar toegangspunten die niet van haar zijn en schakelt ze uit.

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| **[netwerkarchitect]** | Netwerkontwerp, segmentatie, beveiligingsniveaus en keuze van versleuteling |
| **[netwerkbeheer]** | Inrichting en beheer van componenten, firewallregels en wifi |
| **[lijneigenaar netwerkbeveiliging]** | Uitvoering van dit beleid en de contracten met netwerkleveranciers |
| CISO | Advies, toetsing, goedkeuring van afwijkende versleuteling, delen van dreigingen |
| Systeemeigenaar | Aangeven welke verbindingen zijn systeem nodig heeft en welke classificatie geldt |

## 5. Naleving en bewaking

- Jaarlijks: beoordeling van het netwerkontwerp en van alle firewallregels; bewijs is het verslag met de
  verwijderde en aangepaste regels.
- Jaarlijks: controle dat elk segment een beveiligingsniveau heeft en dat de componenten erin daaraan
  voldoen; bewijs is het overzicht van segmenten met de afwijkingen.
- Jaarlijks: een penetratietest of segmentatietest die vanuit het gebruikers- en het gastsegment probeert
  het beheersegment te bereiken.
- Jaarlijks: zoektocht naar onbekende toegangspunten voor wifi en een test van de DDoS-bescherming.
- Maandelijks: rapportage over netwerkdetecties en gedeelde dreigingen aan de CISO.
- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid logging en
monitoring (logging en detectie op netwerkcomponenten), het beleid cryptografie (versleutelingsmiddelen),
het beleid logische toegangsbeveiliging (beheeraccounts en tweefactorauthenticatie), het beleid
wijzigingsbeheer (netwerkwijzigingen), het beleid fysieke toegang en beveiliging (patchkasten) en het
beleid leveranciersbeheer (contracten met netwerk- en hostingleveranciers).

## Bijlage: BIO 2.0-maatregelen

De overheidsmaatregelen van dit domein (7) en waar dit stuk ze invult. Nummers volgens BIO2 v1.3 definitief - 9 januari 2026; de tekst van de maatregel staat bij het CIP.

| Maatregel | Titel | In dit stuk |
|---|---|---|
| 8.20.01 | Beveiliging netwerkcomponenten | 3.2 Netwerkcomponenten en beheer |
| 8.20.02 | Beveiliging netwerkcomponenten | 3.1 Netwerkontwerp en segmentatie |
| 8.21.01 | Beveiliging van netwerkdiensten | 3.3 Koppelpunten en bewaking |
| 8.21.02 | Beveiliging van netwerkdiensten | 3.1 Netwerkontwerp en segmentatie |
| 8.21.03 | Beveiliging van netwerkdiensten | 3.3 Koppelpunten en bewaking |
| 8.21.04 | Beveiliging van netwerkdiensten | 3.3 Koppelpunten en bewaking |
| 8.22.01 | Netwerksegmentatie | 3.1 Netwerkontwerp en segmentatie |

## Nog in te vullen

- **netwerkarchitect**: de functie die het netwerkontwerp opstelt, eigen of bij de leverancier
- **netwerkbeheer**: de eigen afdeling of de leverancier die de componenten beheert
- **lijneigenaar netwerkbeveiliging**: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd ICT
