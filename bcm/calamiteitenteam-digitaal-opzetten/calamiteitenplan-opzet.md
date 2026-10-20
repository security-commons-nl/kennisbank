# Opzet van een cyber- en IT-calamiteitenplan

Het team staat, de taakkaarten liggen klaar. Wat dan nog ontbreekt is het plan dat zegt wanneer dat team in
actie komt, wie het mag activeren en hoe het zich verhoudt tot de crisisorganisatie die er al is. Dit is
de opzet van zo'n plan, afgeleid van een plan dat een gemeente sinds 2025 gebruikt voor zichzelf en de
gemeenten waaraan zij de bedrijfsvoering levert. Neem de hoofdstukken over en vul ze in voor je eigen
organisatie.

In BIO 2.0 helpt een vastgesteld en geoefend plan bewijs leveren voor **5.24** *Plannen en voorbereiden van het
beheer van informatiebeveiligingsincidenten*, **5.26** *Reageren op informatiebeveiligingsincidenten*, **5.29**
*Informatiebeveiliging tijdens een verstoring* en **5.30** *ICT-gereedheid voor bedrijfscontinuïteit*. Het plan alleen
is geen bewijs; het verslag van de oefening wel.

## 1. Reikwijdte: wat het plan wel en niet doet

Leg drie grenzen vast, anders gaat het plan over alles en wordt het nergens gebruikt.

- **Alleen het hoogste escalatieniveau.** De gewone storingen en beveiligingsincidenten lopen via
  incidentmanagement en de procedures van IT-beheer en informatiebeveiliging. Het plan begint waar die
  ophouden.
- **Alleen de eigen organisatie.** Een ransomware-aanval op een zorginstelling in de gemeente of een
  storing bij een internetprovider is maatschappelijk wel relevant, maar valt onder de gewone
  crisisbeheersing, niet onder dit plan.
- **Niet bedrijfscontinuïteit.** Het plan bestrijdt de calamiteit; wat afdelingen doen om door te werken
  staat in hun continuïteitsplannen. Hoe beter die op orde zijn, hoe minder het team hoeft te
  coördineren.

Datalekken vallen alleen onder het plan als ze uit een IT- of cybercalamiteit voortkomen. Een verkeerd
verstuurde brief blijft bij de gewone datalekprocedure.

## 2. Drie niveaus, en het onderscheid tussen storing en aanval

| Niveau | Wat het is |
|---|---|
| Gebeurtenis | Een waarneembaar signaal in een systeem: een melding van een beveiligingstool, een monitor die buiten de normale waarden komt. Kan onschuldig zijn, kan het begin van iets zijn. |
| Incident | Een verstoring van de dienstverlening, of informatie die ongeoorloofd is ingezien, gewijzigd of naar buiten gebracht. |
| Calamiteit | Een ernstig incident met risico op grote gevolgen voor de dienstverlening of grote schade (financieel, imago, bestuurlijk, veiligheid), of waarvoor geen standaardoplossing bestaat. |

Maak daarnaast onderscheid naar oorzaak. Een **IT-calamiteit** komt door een storing zonder kwade opzet:
stroom, een leverancier, een menselijke fout. Een **cybercalamiteit** komt door een aanval. Het team is
hetzelfde, maar wie alarmeert en wie bij afwezigheid voorzit verschilt (zie 5 en 6).

## 3. Waar het team zich op richt

Vijf taken, en niet meer. Het team lost de storing niet zelf op; dat doen IT-beheer en, bij een aanval,
het securityteam.

1. **Impact bepalen**: wat werkt er niet, en wat dreigt nog uit te vallen.
2. **Impact beperken**: welke ingrepen de schade kleiner maken, en wat hun bijwerkingen zijn.
3. **Oplossen faciliteren**: externe hulp inschakelen, prioriteit stellen, knopen doorhakken.
4. **Besluitvorming stroomlijnen**: snel besluiten op onvolledige informatie, en dat navolgbaar vastleggen.
5. **Communicatie stroomlijnen**: wie vertelt wat aan wie.

## 4. Verhouding tot de crisisorganisatie

Het calamiteitenteam valt buiten de wettelijke crisisorganisatie. Leg daarom vast wanneer het overdraagt.

- Is de impact hoog, kritiek of langdurig, dan adviseert de voorzitter de gemeentesecretaris om het
  team bevolkingszorg of een gemeentelijk crisisteam te activeren. De gemeentesecretaris besluit.
- Is de maatschappelijke impact groot, dan kan de gemeentesecretaris de burgemeester adviseren op te
  schalen naar een GRIP-situatie.
- Omgekeerd kan de gemeentesecretaris het calamiteitenteam activeren bij een andersoortige crisis die
  digitaal kan doorslaan.

| Hoogste actieve team | Beslist | Eindverantwoordelijk |
|---|---|---|
| Team bevolkingszorg of gemeentelijk crisisteam | Gemeentesecretaris | Gemeentesecretaris |
| Alleen het calamiteitenteam | Voorzitter calamiteitenteam | Gemeentesecretaris |

**Noodprocedure.** Moet er direct worden ingegrepen om verdere schade te voorkomen, bijvoorbeeld een
applicatie uitzetten, dan mag de voorzitter of diens plaatsvervanger dat doen en meldt hij het zo snel
mogelijk aan wie beslissingsbevoegd is. Ligt er een spoedbesluit vóór het eerste overleg, dan zijn de
leden die op dat moment beschikbaar zijn bevoegd.

**Zit het team grotendeels in het managementteam bedrijfsvoering?** Maak dan het verschil scherp: het
calamiteitenteam bestrijdt de calamiteit, het managementteam beheerst de gevolgen voor de rest van de
eigen dienstverlening.

**Lever je bedrijfsvoering aan andere gemeenten?** Een calamiteit raakt dan bijna altijd iedereen.
Spreek af dat de gemeentesecretaris van de leverende gemeente aanspreekpunt is en afstemt met de
collega-secretarissen. Raakt het één afnemer, dan stuurt die zelf aan en wordt de leverende gemeente
geïnformeerd. Zolang alleen het calamiteitenteam actief is, communiceert de voorzitter namens de
gemeentesecretaris; is de crisisorganisatie actief, dan communiceert die.

## 5. Samenstelling en vervanging

De vaste kern, met de rollen uitgewerkt in [taakkaarten.md](taakkaarten.md):

| Rol | Vervanger |
|---|---|
| Voorzitter (directeur bedrijfsvoering of CIO) | CIO, daarna manager IT-beheer |
| Manager IT-beheer | Teammanager regie en processen |
| CISO | Information security officer |
| Secretaris | Vaste vervanger of pool |
| Communicatieadviseur | Vaste vervanger; extra capaciteit uit de crisiscommunicatiepool |

Bij afwezigheid van beide voorzitters zit bij een **cybercalamiteit** de CISO voor, bij een
**IT-calamiteit** de manager IT-beheer. Op afroep sluiten aan: servicemanagement (als de beheerpartij
betrokken is), relatiebeheer (bij veel afstemming met regiopartners), juridische zaken, externe
specialisten, en bij langdurige calamiteiten een vertegenwoordiger van de getroffen afdeling.

Loop vooraf na dat niemand tegelijk in het calamiteitenteam en in het team bevolkingszorg zit. Een
dubbelfunctie blijkt pas tijdens de calamiteit, en dan is het te laat.

## 6. Activeren

- De **manager IT-beheer** (bij een IT-incident) of de **CISO** (bij een cyberincident) alarmeert het team
  of informeert het alleen, via de afgesproken kanalen.
- De **voorzitter** besluit tot activeren, na overleg met de vaste leden.
- Tijdens kantoortijd is de kern **binnen een half uur** bij elkaar. Spreek af wat er buiten kantoortijd
  geldt. Zonder piketregeling heb je alleen een bellijst ("zacht piket"), en dat is niet zeker.
- Leg de kanalen vast: een Teams-omgeving voor informatie, een chatkanaal voor signalering, en een
  reservekanaal buiten de eigen omgeving voor als Teams zelf plat ligt. De secretaris beheert de
  toegang.

**Wanneer opschalen.** Geen zwart-wit regels, wel richtsnoeren:

- Impact helder, protocollen bestaan, oplossing in zicht: niet opschalen.
- Risico op grote schade, breed opgevat (letsel, veiligheid, geld, imago, politiek, gegevens): opschalen.
- De hele organisatie of de kritieke dienstverlening geraakt, en onzeker hoe lang: opschalen. Kritieke
  dienstverlening is alles in direct contact met inwoners (balie, klantcontact) en zaken als bruggen en
  verkeerslichten; de lijst komt uit de bedrijfscontinuïteitsanalyse.
- Impact onduidelijk: mag opschalen.
- Alleen niet-kritieke processen, maar lange oplostijd: mag opschalen.

Alleen incidenten met de hoogste twee prioriteiten in incidentmanagement komen in aanmerking.

## 7. Communicatie

Twee stromen, en houd ze uit elkaar.

- **Over het incident zelf** communiceert het calamiteitenteam, met de communicatieadviseur.
- **Over de gevolgen voor de dienstverlening** communiceert de afdeling die de dienst levert, of de
  crisisorganisatie als die actief is.

Voorbeeld: het team meldt dat de gemeente is getroffen door malware op het systeem voor reisdocumenten.
Burgerzaken meldt dat er tijdelijk geen paspoorten worden uitgegeven. IT-beheer blijft de gebruikers
informeren via het vaste storingsprotocol: wat werkt niet, wanneer is het verwachte herstel, wat is het
alternatief.

## 8. Afschalen, nazorg en evaluatie

- Afschalen besluit de gemeentesecretaris (als de crisisorganisatie actief is) of de voorzitter.
- De voorzitter zorgt voor een warme overdracht naar de lijn. De secretaris sluit het dossier af.
- Bij een aanval regelt de CIO de aangifte, voor zover die nog niet is gedaan.
- Na elke inzet: een oorzaakanalyse (IT-beheer), de risicoanalyse bijwerken (CISO), nieuwe inzichten in
  de architectuurtool vastleggen, en een evaluatie van het optreden van het team met het
  [evaluatiesjabloon](evaluatiesessie-sjabloon.pptx).
- Vergeet de mensen niet. Wie dagen een calamiteit heeft bestreden, heeft na afloop aandacht nodig, en
  tijdens de calamiteit ook: pauzes, eten, aflossing.

## 9. Borging

- Elk lid van het team kent het plan en is getraind op de eigen rol.
- Het team oefent **minstens eens per jaar** met een realistisch scenario.
- **Eens per twee jaar** een bestuurlijke oefening, met bestuur, team bevolkingszorg en calamiteitenteam.
- Het plan wordt jaarlijks herzien op basis van oefeningen en echte inzet.

Een plan op papier is het begin, geen bewijs. Het bewijs is een team dat bereikbaar is, weet wie wat
doet, het draaiboek op tafel legt en op tijd besluit om bij elkaar te komen. Dat haal je alleen uit
oefenen.

## Do's en don'ts

- **Doe:** geef je telefoon in beheer bij iemand die bepaalt of je gestoord moet worden.
- **Doe:** zorg voor koffie, eten, pauzes en rust.
- **Niet:** voicemail als bereikbaarheid.
