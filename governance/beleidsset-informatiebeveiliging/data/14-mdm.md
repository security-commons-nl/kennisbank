---
domein: mdm
titel: Beleid mobile device management
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor mobiele apparatuur waarmee
bedrijfsinformatie wordt verwerkt: laptops, smartphones en tablets van de organisatie en, waar dat is
toegestaan, privéapparaten van medewerkers. Het regelt hoe die apparaten zijn ingericht, beheerd en gebruikt,
zodat bedrijfsinformatie beschermd blijft bij verlies, diefstal en werken buiten de locaties van de
organisatie. Het geldt voor medewerkers, inhuur en stagiairs die mobiel werken. Het gaat over
ISO-beheersmaatregel 8.01.

Buiten dit beleid vallen de inventaris en uitgifte van apparatuur (beleid bedrijfsmiddelenbeheer), de
versleutelingseisen (beleid cryptografie) en de netwerktoegang (beleid netwerkbeveiliging).

## 2. Uitgangspunten

1. Bedrijfsinformatie blijft zo veel mogelijk in de centrale systemen. Op het apparaat staat niets, of zo min
   mogelijk en dan versleuteld.
2. Alleen beheerde apparaten of beheerde apps krijgen toegang tot bedrijfsinformatie.
3. De gebruiker weet wat de risico's van mobiel werken zijn en heeft getekend dat hij veilig werkt.

## 3. Beleidsregels

### 3.1 Zero footprint en bescherming op het apparaat

- Apps en diensten voor mobiele apparaten zijn zo ingericht dat bedrijfsinformatie niet standaard op het
  apparaat wordt opgeslagen: werken gebeurt via de browser, een virtuele werkplek of een beheerde app die
  geen lokale kopie bewaart. [8.01.01]
- Waar dat nog niet kan, staat bedrijfsinformatie alleen in een beheerde, versleutelde container of op een
  volledig versleuteld apparaat, en is het apparaat beveiligd met een pincode van ten minste zes cijfers, een
  wachtwoord of biometrie, met automatische vergrendeling na ten hoogste vijf minuten. [8.01.01]
- Van elk apparaat met toegang tot bedrijfsinformatie kan de organisatie de bedrijfsinformatie op afstand
  wissen. Bij verlies of diefstal meldt de gebruiker dat direct bij de servicedesk; de servicedesk wist
  binnen vier uur na de melding en registreert de melding als beveiligingsincident. [8.01.01]

### 3.2 Beheer van apparaten

- Elk mobiel apparaat met toegang tot bedrijfsinformatie valt onder een MDM-oplossing (beheer van het hele
  apparaat) of, voor privéapparaten, een MAM-oplossing (beheer van de bedrijfsapps). Inschrijving is een
  voorwaarde voor toegang. [8.01.02]
- Via MDM of MAM dwingt de organisatie ten minste af: versleuteling, schermvergrendeling, een ondersteunde
  versie van het besturingssysteem, geen root of jailbreak, en wissen op afstand. Een apparaat dat niet
  voldoet, verliest automatisch de toegang tot bedrijfsinformatie. [8.01.02]
- Mobiele apparaten vallen onder patchmanagement en hardening volgens het beleid vulnerability- en
  patchmanagement. Beveiligingsupdates van het besturingssysteem en de bedrijfsapps worden binnen de
  termijnen uit dat beleid geïnstalleerd; apparaten waarvoor de fabrikant geen updates meer levert, worden
  uitgefaseerd. [8.01.02]
- Apps op beheerde apparaten komen uit de officiële winkel of uit de beheerde bedrijfscatalogus.
::: als byod=ja
- Privéapparaten zijn toegestaan onder de voorwaarden in
  [[regeling eigen apparaten: welke apparaten, besturingssystemen en diensten zijn toegestaan]].
  Op een privéapparaat staat bedrijfsinformatie alleen in beheerde apps (MAM); de organisatie wist bij vertrek
  of verlies alleen die apps, niet het hele apparaat. De medewerker stemt daar vooraf schriftelijk mee in.
  [8.01.01]
- Een privéapparaat krijgt pas toegang als het een ondersteunde versie van het besturingssysteem heeft, een
  schermvergrendeling en versleuteling van de opslag. De toegangsvoorziening controleert dat bij elke
  aanmelding. [8.01.02]
:::

::: als byod=nee
- Privéapparaten krijgen geen toegang tot bedrijfsinformatie, ook niet via webmail of de browser. De
  toegangsvoorziening laat alleen apparaten toe die de organisatie beheert. [8.01.01]
:::

::: als werkplek=cloud
- Toegang tot de cloudwerkplek vanaf een mobiel apparaat loopt via voorwaardelijke toegang: meerfactor plus
  een apparaat of app die volgens het MDM of MAM aan de eisen voldoet. Opslaan, kopiëren naar niet-beheerde
  apps en lokaal synchroniseren van bestanden zijn op niet-beheerde apparaten uitgeschakeld. [8.01.01, 8.01.02]
:::

::: als werkplek=hybride
- Mobiele apparaten krijgen toegang tot clouddiensten via voorwaardelijke toegang op basis van de MDM- of
  MAM-status, en tot de lokale of virtuele werkplek alleen via een beveiligde verbinding (bijvoorbeeld een
  VPN of een gateway voor de virtuele werkplek) vanaf een beheerd apparaat. De beheerinstellingen voor beide
  routes zijn op elkaar afgestemd, zodat een apparaat dat voor de ene route is geblokkeerd, ook de andere
  verliest. [8.01.02]
:::

::: als werkplek=on-premises
- Mobiele apparaten krijgen toegang tot de interne omgeving alleen via een beveiligde verbinding
  (bijvoorbeeld een VPN of een gateway voor een virtuele werkplek) vanaf een apparaat dat onder MDM valt.
  Mail en agenda op smartphones lopen via een beheerde app. Werken via een virtuele werkplek is de standaard,
  zodat er geen bedrijfsinformatie op het apparaat komt. [8.01.01, 8.01.02]
:::

### 3.3 Gebruikersovereenkomst en gedrag

- Voordat een medewerker mobiel werkt, tekent hij een gebruikersovereenkomst mobiel werken. Daarin verklaart
  hij de risico's te kennen en veilig te werken. De overeenkomst geldt voor alle mobiele apparatuur die hij
  zakelijk gebruikt, ook een eigen apparaat. De getekende overeenkomst wordt in het personeelsdossier of het
  uitgiftesysteem bewaard. [8.01.02]
- De overeenkomst gaat ten minste over: direct melden van verlies of diefstal, geen bedrijfsinformatie in
  privéapps of privécloudopslag, geen gedeeld gebruik van het apparaat met anderen, updates installeren, het
  apparaat niet onbeheerd achterlaten, voorzichtig zijn met openbare wifi en het accepteren van wissen op
  afstand.
- Op de locaties van de organisatie gebruiken beheerde apparaten het beveiligde bedrijfsnetwerk; niet-beheerde
  apparaten en gasten gebruiken een gastnetwerk dat logisch gescheiden is van het bedrijfsnetwerk. Er is geen
  open, onbeveiligd wifinetwerk.

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| [[lijneigenaar mobiele apparatuur: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd IT]] | Uitvoering van dit beleid en de inrichting van MDM en MAM |
| Beheerder MDM/MAM | Inschrijving, nalevingsregels, rapportages en wissen op afstand |
| Servicedesk | Melding van verlies of diefstal, wissen binnen vier uur, registratie als incident |
| HR | Gebruikersovereenkomst mobiel werken bij indiensttreding en bij uitgifte |
| CISO | Advies, toetsing van dit beleid en van de nalevingsrapportages |
| Medewerkers | Overeenkomst naleven, updates installeren, verlies of diefstal direct melden |

## 5. Naleving en bewaking

- Per kwartaal toetst de organisatie of mobiele apparaten onder MDM of MAM vallen, bijgewerkt zijn en of de
  gebruikers de overeenkomst hebben getekend, en rapporteert de uitkomst aan de CISO. [8.01.02]
- Het bewijs van die toets bestaat uit:
  - het aantal apparaten met toegang tot bedrijfsinformatie tegenover het aantal ingeschreven apparaten in
    MDM of MAM;
  - het aantal apparaten met een verouderd besturingssysteem of ontbrekende updates;
  - een vergelijking van mobiele gebruikers met de getekende gebruikersovereenkomsten.
- Jaarlijks: test van wissen op afstand op een testapparaat en controle dat bij de gemelde verliezen van dat
  jaar binnen vier uur is gewist.
- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid
bedrijfsmiddelenbeheer (uitgifte, inventaris en inname), het beleid cryptografie (versleuteling op het
apparaat), het beleid vulnerability- en patchmanagement, het beleid logische toegangsbeveiliging
(meerfactor en voorwaardelijke toegang), het beleid netwerkbeveiliging (wifi en externe toegang) en het
beleid afvoer en hergebruik van gegevensdragers.
