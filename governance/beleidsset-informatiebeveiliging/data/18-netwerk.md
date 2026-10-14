---
domein: netwerk
titel: Beleid netwerkbeveiliging
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor het ontwerp, de inrichting, het
beheer en de bewaking van de netwerken van de organisatie, inclusief wifi en externe koppelingen. Het doel
is dat een aanvaller die ergens binnenkomt niet vrij verder kan, dat aanvallen op het netwerk worden gezien
en dat gegevens onderweg beschermd zijn. Het gaat over de ISO-beheersmaatregelen 8.20 tot en met 8.23.

**Voor wie.** Het beleid is primair bedoeld voor de netwerkarchitect, de afdeling of leverancier die de
netwerkcomponenten beheert en de systeemeigenaren die verbindingen nodig hebben. De regels over het
aansluiten van apparatuur gelden voor iedereen die een apparaat op een netwerk van de organisatie aansluit.

**Waarop.** Alle netwerken en netwerkdiensten die de organisatie gebruikt: het bedrijfsnetwerk, het
beheersegment, wifi, de koppelpunten met internet en met ketenpartners, de verbindingen tussen locaties en
met leveranciers, en de netwerken waarop operationele technologie draait. Is het netwerk of een netwerkdienst
uitbesteed, dan gelden de eisen uit dit beleid als minimumeis voor die partij. De organisatie legt dat vast
in het contract en toetst de naleving met een onafhankelijke verklaring, zoals een ISO 27001-certificaat of
een ISAE 3402- of ISAE 3000-rapport; het vastleggen loopt via het beleid informatiebeveiliging bij inkoop,
het toetsen via het beleid contractbeheer.

Buiten dit beleid vallen de logging van netwerkcomponenten (beleid logging en monitoring), de keuze van
cryptografische middelen in het algemeen (beleid cryptografie), de beheeraccounts zelf (beleid logische
toegangsbeveiliging) en de fysieke beveiliging van patchkasten en bekabeling (beleid fysieke toegang en
beveiliging).

## 2. Uitgangspunten

1. Het netwerk is opgedeeld in segmenten. Verkeer tussen segmenten is standaard dicht en wordt alleen
   toegestaan waar dat nodig is.
2. Elk segment heeft een beveiligingsniveau, afgeleid van het hoogste impactniveau van de systemen erin. Wat
   erin zit, en wat ermee verbonden is, voldoet aan dat niveau.
3. Toegang hangt af van de identiteit van gebruiker en apparaat, ook binnen het eigen netwerk.
4. Beheer van het netwerk loopt via een eigen, afgeschermde route.
5. Termijnen en frequenties in dit beleid die niet uit een wet of uit de BIO 2.0 komen, zijn standaardwaarden.
   De organisatie past ze aan op haar eigen risicoafweging en legt de keuze vast bij de vaststelling van dit beleid.

## 3. Beleidsregels

### 3.1 Netwerkontwerp en segmentatie

- [[netwerkarchitect: de functie die het netwerkontwerp opstelt, eigen of bij de leverancier]] houdt een
  actueel netwerkontwerp bij met de segmenten, hun beveiligingsniveau, de koppelpunten en de toegestane
  verkeersstromen, werkt het bij bij elke grote wijziging en beoordeelt het ten minste jaarlijks; de
  beoordeling is vastgelegd. [8.22.01]
- Elk segment heeft een vastgelegd beveiligingsniveau, afgeleid van het hoogste impactniveau van de
  informatie en systemen erin. Ten minste gescheiden zijn: gebruikers, servers, beheer, gasten en
  voorzieningen van derden. [8.22.01]
- [[netwerkbeheer: de eigen afdeling of de leverancier die de componenten beheert]] beoordeelt de
  firewallregels tussen segmenten en naar buiten ten minste jaarlijks en verwijdert regels zonder eigenaar
  of zonder aantoonbare noodzaak; elke regel heeft een eigenaar en een reden in de regelset. [8.21.01, 8.22.01]
- Werkplekken kunnen geen verkeer tussen segmenten doorsturen; [[netwerkbeheer]] dwingt dat af in de
  configuratie van de werkplek en van de switches. [8.22.01]

::: als ot=beperkt
- Gebouwbeheer, toegangscontrole en camera's staan in een eigen segment met een eigen beveiligingsniveau.
  Vanuit dit segment is er geen verbinding met het kantoornetwerk; de leverancier krijgt beheertoegang
  alleen via de beheerroute van de organisatie. [8.22.01]
:::

::: als ot=substantieel
- Operationele technologie (gemalen, bruggen, sluizen, verkeersinstallaties, zuivering) staat in een
  eigen netwerk, gescheiden van het kantoornetwerk volgens een zonemodel, bijvoorbeeld uit IEC 62443.
  Elke zone heeft een beveiligingsniveau en elke verbinding tussen zones loopt via een gecontroleerd
  koppelpunt dat de netwerkarchitect in het ontwerp vastlegt. [8.22.01]
- Het OT-netwerk heeft geen directe verbinding met internet. Toegang op afstand, ook van leveranciers,
  verloopt via een aparte beheeromgeving met MFA, op verzoek aangezet en per sessie gelogd. [8.20.02]
- Verkeer van en naar het OT-netwerk wordt apart bewaakt met detectie die OT-protocollen herkent. [8.21.02]
:::

### 3.2 Netwerkcomponenten en beheer

- Netwerkcomponenten voldoen ten minste aan het beveiligingsniveau van het segment waarin ze staan: een
  component in een segment met impactniveau kritiek of hoger heeft de hardening, firmware-updates en
  beheerbeveiliging die bij dat niveau horen. [[netwerkbeheer]] legt per component vast welke
  hardeningsrichtlijn geldt. [8.20.01]
- De beheerinterfaces van netwerkcomponenten zijn alleen bereikbaar vanuit een apart beheersegment en
  niet vanuit het gebruikersnetwerk of internet. Beheer gebeurt met persoonsgebonden accounts en MFA.
  [8.20.02]
- [[netwerkbeheer]] verwijdert standaardwachtwoorden en ongebruikte diensten op netwerkcomponenten voor
  ingebruikname. De configuratie van elke component staat in een back-up en wijzigingen lopen via
  wijzigingsbeheer. [8.20.01]
- Een apparaat krijgt pas toegang tot het bedrijfsnetwerk na authenticatie van apparaat en gebruiker, via
  netwerktoegangscontrole die [[netwerkbeheer]] inricht. [8.20.02]
- [[netwerkbeheer]] patcht netwerkcomponenten binnen de termijnen uit het beleid kwetsbaarheden en
  patchmanagement en vervangt componenten die geen beveiligingsupdates meer krijgen. [8.20.01]

::: als beheer=eigen
- De eigen netwerkbeheerders beheren de componenten. Een beheerder die netwerkcomponenten beheert,
  beoordeelt niet zelf de monitoring van dat beheer; de CISO wijst aan wie dat doet. [8.20.02]
:::

::: als beheer=regie,uitbesteed
- De netwerkdienst is uitbesteed. Het contract legt de beveiligingseisen uit dit beleid vast:
  segmentatie, beheer via een apart beheersegment, patchtermijnen voor netwerkcomponenten, de levering
  van logging en een jaarlijkse rapportage waarmee de leverancier aantoont dat hij eraan voldoet. [8.20.01, 8.20.02]
- De partij die het netwerk beheert, controleert niet zelf de beveiliging ervan; de organisatie laat de
  controle doen door een andere partij of doet die zelf. [8.20.02]
:::

### 3.3 Koppelpunten en bewaking

- Elk koppelpunt met internet of een andere onvertrouwde zone heeft een firewall en maatregelen tegen
  aanvallen op de beschikbaarheid, zoals DDoS-bescherming. Tussen segmenten met een verschillend
  beveiligingsniveau zijn maatregelen die het misbruik van één segment beperken tot dat segment. [8.21.01]
- Verkeer van en naar de vertrouwde omgeving wordt bewaakt met detectievoorzieningen die verdacht verkeer
  signaleren, zoals een netwerkdetectiesysteem of de detectiefunctie van de firewall. [8.21.02]
- Nieuwe dreigingen die bij deze bewaking worden ontdekt, worden binnen de juridische kaders gedeeld met
  de sectorale CERT, zodat andere overheden zich kunnen beschermen; wat is gedeeld, wordt vastgelegd.
  [8.21.03]
- Een systeemeigenaar die een nieuwe koppeling met een externe partij nodig heeft, vraagt die aan bij de
  netwerkarchitect, die de koppeling toetst aan het ontwerp en vastlegt welke verkeersstromen zijn
  toegestaan. [8.21.01]

::: als detectie=eigen-soc,uitbesteed
- Het SOC beoordeelt de meldingen van de netwerkdetectie binnen de afgesproken termijn en deelt nieuwe
  dreigingen volgens de procedure met de CERT. [8.21.02, 8.21.03]
:::

::: als detectie=geen
- Er is geen SOC. De meldingen van de netwerkdetectie gaan naar [[netwerkbeheer]], die ze elke werkdag
  beoordeelt en opvallende meldingen aan de CISO doorzet. De CISO deelt nieuwe dreigingen met de CERT.
  [8.21.02, 8.21.03]
:::

::: als hosting=eigen-dc
- Het eigen datacenter heeft een eigen koppelpunt met internet. De organisatie neemt DDoS-bescherming af
  bij de internetleverancier en [[netwerkbeheer]] test die jaarlijks. [8.21.01]
:::

::: als hosting=hostingpartij
- De verbinding met de hostingpartij loopt over een versleutelde verbinding of een eigen lijn. De
  hostingpartij scheidt de omgeving van de organisatie van die van andere klanten en levert
  DDoS-bescherming op het koppelpunt met internet, vastgelegd in het contract. [8.21.01, 8.21.04]
:::

::: als hosting=saas
- De meeste diensten draaien bij SaaS- en cloudleveranciers. Werkplekken maken daarom rechtstreeks
  verbinding met internet. Toegang tot clouddiensten hangt af van identiteit en apparaatstatus; de
  leverancier levert de bescherming tegen aanvallen op de beschikbaarheid. De organisatie bewaakt het
  verkeer naar clouddiensten via de werkplek en de logging van de clouddienst. [8.21.01, 8.21.02]
:::

### 3.4 Webfilter

- Internetverkeer van werkplekken en servers loopt via een webfilter dat bekende kwaadaardige sites,
  phishingsites en sites met malware blokkeert en dat verkeer naar anonimiseringsdiensten en onbeheerde
  opslagdiensten tegenhoudt. [[netwerkbeheer]] houdt de blokkeerlijsten automatisch actueel. [8.23.01]
- De CISO stelt vast welke categorieën websites geblokkeerd zijn en beoordeelt die lijst jaarlijks. Een
  uitzondering vraagt de leidinggevende aan bij de servicedesk, met een reden en een einddatum; de
  servicedesk legt de uitzondering vast. [8.23.01]
- Medewerkers horen via het bewustzijnsprogramma welke sites geblokkeerd zijn en waarom, en hoe ze een
  geblokkeerde site melden die ze voor hun werk nodig hebben. [8.23.01]

### 3.5 Versleuteling onderweg

- Gegevens die over draadloze verbindingen gaan, en over bedrade verbindingen buiten het gebied dat de
  organisatie fysiek beheert, worden versleuteld. Alleen gegevens die nodig zijn om de verbinding tot
  stand te brengen, blijven onversleuteld. [8.21.04]
- De sterkte van de versleuteling volgt uit het vertrouwelijkheidslabel en uit hoe lang de gegevens
  beschermd moeten blijven. Waar mogelijk gebruikt de organisatie middelen met een positief inzetadvies van
  het NBV. Is er geen geadviseerd middel, dan kiest de netwerkarchitect in overleg met de CISO een andere
  geschikte methode en legt die keuze vast. [8.21.04]
- Verbindingen tussen locaties en met externe partijen lopen via een VPN of versleutelde lijn. Thuiswerkers
  maken verbinding via een versleutelde verbinding met MFA. [8.21.04]

### 3.6 Wifi

- Het bedrijfswifi is alleen toegankelijk voor beheerde apparaten, na authenticatie van apparaat en
  gebruiker, en is versleuteld volgens de geldende standaard. [8.21.04]
- Gastwifi, ook een landelijk roamingnetwerk voor bezoekende ambtenaren, staat in een apart segment zonder
  toegang tot het bedrijfsnetwerk. Er is geen open en onversleuteld netwerk. [8.22.01]
- [[netwerkbeheer]] zoekt jaarlijks naar toegangspunten die niet van de organisatie zijn, schakelt ze uit
  en legt de uitkomst vast. [8.20.01]

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| [[lijneigenaar netwerkbeveiliging: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd ICT]] | Eigenaar van dit beleid en de contracten met netwerkleveranciers |
| [[netwerkarchitect]] | Netwerkontwerp, segmentatie, beveiligingsniveaus, toetsing van nieuwe koppelingen en keuze van versleuteling |
| [[netwerkbeheer]] | Inrichting en beheer van componenten, firewallregels, netwerktoegangscontrole, webfilter en wifi |
| CISO | Advies, toetsing, categorieën van het webfilter, goedkeuring van afwijkende versleuteling, delen van dreigingen, beoordeling van afwijkingen |
| Systeemeigenaar | Aangeven welke verbindingen zijn systeem nodig heeft en welk impactniveau en label gelden |
| Inkoop en contractbeheer | Vastleggen van de eisen uit dit beleid bij netwerk- en hostingleveranciers en toetsen van hun verklaringen |
| Medewerkers | Alleen beheerde apparaten aansluiten, geen eigen toegangspunten plaatsen, geblokkeerde sites melden via de servicedesk |

## 5. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in [[registratie van controles: het systeem waarin controles worden vastgelegd, bijvoorbeeld het ticketsysteem of het managementsysteem]];
afwijkingen gaan als bevinding naar het risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| NWB-01 | Het netwerkontwerp is actueel, elk segment heeft een beveiligingsniveau en de segmenten in de configuratie komen overeen met het ontwerp | [[netwerkarchitect]] | Jaarlijks | Netwerkontwerp met beoordeling, configuratierapport van de segmenten, afwijkingen | 8.22.01 |
| NWB-02 | Alle firewallregels hebben een eigenaar en een reden; regels zonder noodzaak zijn verwijderd | [[netwerkbeheer]] | Jaarlijks | Verslag met de verwijderde en aangepaste regels | 8.21.01, 8.22.01 |
| NWB-03 | Netwerkcomponenten voldoen aan de hardening en de patchtermijnen van hun segment en zijn alleen beheerbaar vanuit het beheersegment met MFA | CISO | Jaarlijks | Overzicht van componenten met hardeningsrichtlijn en patchstand, configuratierapport van de beheerinterfaces | 8.20.01, 8.20.02 |
| NWB-04 | Een segmentatietest vanuit het gebruikers- en het gastsegment bereikt het beheersegment en het serversegment niet | Onafhankelijke tester aangewezen door de CISO | Jaarlijks | Testrapport met bevindingen en opvolging | 8.22.01, 8.20.02 |
| NWB-05 | De DDoS-bescherming en de netwerkdetectie op de koppelpunten werken en meldingen zijn binnen de termijn beoordeeld | CISO | Jaarlijks, meldingen per maand | Testrapport DDoS-bescherming, maandrapportage van de netwerkdetectie | 8.21.01, 8.21.02 |
| NWB-06 | Nieuwe dreigingen uit de netwerkbewaking zijn volgens de procedure met de CERT gedeeld | CISO | Jaarlijks | Registratie van gedeelde dreigingen | 8.21.03 |
| NWB-07 | Het webfilter blokkeert de vastgestelde categorieën, de blokkeerlijsten zijn actueel en elke uitzondering heeft een reden en een einddatum | [[netwerkbeheer]] | Halfjaarlijks | Configuratierapport van het webfilter, lijst van uitzonderingen | 8.23.01 |
| NWB-08 | Draadloze en externe verbindingen zijn versleuteld volgens de geldende adviezen, het bedrijfswifi vraagt authenticatie van apparaat en gebruiker, en er zijn geen onbekende toegangspunten | [[netwerkbeheer]] | Jaarlijks | Configuratierapport van wifi en VPN, verslag van de zoektocht naar toegangspunten | 8.21.04, 8.20.01 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De
netwerkarchitect dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de looptijd.
De afwijking geldt pas na acceptatie van het risico door [[risico-eigenaar: de manager die restrisico's accepteert]]
en staat in het risicoregister; afwijkingen worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid logging en
monitoring (logging en detectie op netwerkcomponenten), het beleid cryptografie (versleutelingsmiddelen),
het beleid logische toegangsbeveiliging (beheeraccounts en MFA), het beleid kwetsbaarheden en
patchmanagement (patchtermijnen), het beleid wijzigingsbeheer (netwerkwijzigingen), het beleid fysieke
toegang en beveiliging (patchkasten en bekabeling), het beleid screening, bewustzijn en opleiding (het
webfilter in het bewustzijnsprogramma) en het beleid informatiebeveiliging bij inkoop en contractbeheer
(contracten met netwerk- en hostingleveranciers).
