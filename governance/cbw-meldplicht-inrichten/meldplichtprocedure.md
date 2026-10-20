# Meldplichtprocedure Cyberbeveiligingswet

> **Herkomst:** procedure van de CISO van een regionale samenwerking van vier gemeenten, versie 1.0, vastgesteld 29 september 2026 door het managementteam bedrijfsvoering, jaarlijkse herziening. Voor de commons ontdubbeld en geanonimiseerd; de figuren (meldstructuur, stroomdiagram, meldplichtkaart) zijn niet overgenomen. Neem de procedure over en vervang de rollen door die van je eigen organisatie.

| Kenmerk | Waarde |
|---|---|
| Eigenaar procedure | CISO |
| Vaststeller | Managementteam bedrijfsvoering |
| Wettelijke grondslag | Cyberbeveiligingswet en Cyberbeveiligingsregeling sector overheid |
| Herzieningstermijn | Jaarlijks |

## 1. Inleiding

### 1.1 Doel

Met de inwerkingtreding van de Cyberbeveiligingswet (Cbw) op 15 augustus 2026 zijn gemeenten essentiële
entiteiten. De zorgplicht, de meldplicht en de registratieplicht gelden daarmee rechtstreeks. Deze
procedure beschrijft hoe de gemeenten invulling geven aan de meldplicht. Zij is bedoeld voor gebruik
tijdens significante incidenten, binnen het calamiteitenteam digitaal (CTD).

### 1.2 Wat de meldplicht inhoudt

De gemeente meldt elk significant incident aan haar CSIRT en aan haar bevoegde autoriteit. Voor gemeenten is
het **Nationaal Cyber Security Centrum (NCSC)** het CSIRT en de **Rijksinspectie Digitale Infrastructuur (RDI)**
de bevoegde autoriteit. De melding loopt via het centrale meld- en registratieportaal van het NCSC, dat haar
doorgeleidt naar de RDI. Na de melding kan ook telefonisch contact worden opgenomen met het NCSC om snel te
schakelen.

> **Noot van de commons.** Wie het CSIRT voor gemeenten wordt, was in augustus 2026 nog niet definitief; het
> NCSC levert de dienstverlening voorlopig, in elk geval tot eind 2026. Zie de
> [stelselkaart security-gremia](../../security/stelselkaart-security-gremia/) voor de actuele stand.

De meldplicht is geen eenmalige handeling maar een keten van meldingen met eigen termijnen, die begint bij
kennisname en eindigt met het eindverslag. Vier eigenschappen bepalen hoe zij uitpakt:

1. **"Leidt of kan leiden tot."** Een incident is significant zodra het een drempelwaarde kán bereiken. De
   gemeente meldt dus ook op basis van mogelijke gevolgen.
2. **De klok loopt vanaf kennisname, niet vanaf begrip.** Melden voordat oorzaak, omvang en dader bekend
   zijn. Onvolledige informatie is geen reden om te wachten; aanvullen volgt later.
3. **Er is ook een informatieplicht** richting de ontvangers van gemeentelijke diensten, met een eigen doel
   en een eigen termijn. Die wacht niet op de melding aan het NCSC.
4. **De meldplicht is handhaafbaar.** Een te late, onvolledige of achterwege gebleven melding kan worden
   beboet.

### 1.3 Reikwijdte

De procedure geldt voor alle netwerk- en informatiesystemen die randvoorwaardelijk zijn voor kritieke
processen, ook als ze bij een leverancier draaien. Dat een systeem door een derde wordt beheerd of gehost,
verplaatst de meldplicht niet naar die derde. Een incident bij een leverancier dat de gemeentelijke
dienstverlening raakt of kan raken, is een incident van de gemeente, en de gemeente meldt.

**Waarom dit strak moet.** De RDI kan bij overtreding van zorg- of meldplicht een bestuurlijke boete opleggen
van maximaal € 10 miljoen, bij andere verplichtingen zoals de registratieplicht tot € 1 miljoen.
Burgemeesters en wethouders kunnen individueel een boete van maximaal € 25.000 krijgen als zij de verplichte
training niet volgen.

### 1.4 Meldkanalen

Melden via MijnNCSC of het meldformulier van het NCSC. Leg vooraf een terugvalroute vast voor als de eigen
omgeving (mail, Teams) zelf getroffen is.

## 2. Uitvoering voor meerdere gemeenten

Elke gemeente is een zelfstandige essentiële entiteit met een eigen meldplicht. Voert één gemeente de ICT uit
voor de andere, dan kan die de meldingen feitelijk doen. Dat is een uitvoeringsafspraak, geen overdracht van
verantwoordelijkheid: de Cbw kent geen constructie waarbij de meldplicht van de ene entiteit overgaat op de
andere.

Voorwaarden:

- Het college van elke deelnemende gemeente heeft de CISO van de uitvoerende gemeente **gemandateerd** om
  namens dat college Cbw-meldingen te doen.
- Het college van elke gemeente heeft het **CTD aangewezen** als het orgaan dat toetst of een incident
  meldplichtig is. De uitvoering blijft bij de CISO.
- Het is altijd duidelijk **namens welke gemeente** de melding wordt gedaan.

| Scenario | Situatie | Meldingen | Toelichting |
|---|---|---|---|
| 1 | Eén incident met gevolgen voor alle gemeenten | Eén per gemeente | Elke gemeente meldt met haar eigen impact. Technische beschrijving en impactbeoordeling mogen gelijk zijn als dat zo is |
| 2 | Eén incident met gevolgen voor één gemeente | Eén | Namens de gemeente die de gevolgen ondervindt; de andere melden niet |

## 3. De procedure

De verantwoordelijkheid voor de melding ligt bij het CTD. Zodra het CTD is geactiveerd, doorloopt het de
toets (hoofdstuk 4), de meldingsketen (hoofdstuk 5) en de informatieplicht (hoofdstuk 6). Zie voor het
activeren het [cyber- en IT-calamiteitenplan](../../bcm/calamiteitenteam-digitaal-opzetten/calamiteitenplan-opzet.md).

## 4. De meldplicht-toets

### 4.1 Incident

Een onverwachte of onbedoelde gebeurtenis die verband houdt met een verstoring van netwerk- en
informatiesystemen. Er hoeft geen schade te zijn: een gebeurtenis die schade had kunnen veroorzaken, telt ook.

### 4.2 Significant incident

Significant, en dus meldplichtig, is een incident dat ten minste één drempelwaarde uit de
Cyberbeveiligingsregeling sector overheid voor decentrale overheden haalt of kan halen:

| Drempelwaarde | Operationele lezing voor de gemeente |
|---|---|
| A. Uitval van de dienstverlening van de essentiële entiteit voor ten minste vier uur | Een kritiek proces is geheel of gedeeltelijk ten minste vier aaneengesloten uren onbeschikbaar, of dreigt dat te worden. Vier uur is een vaste ondergrens |
| B. Financiële gevolgen die niet in de begroting kunnen worden opgevangen | De verwachte kosten of gederfde inkomsten (herstel, inhuur, uitval) zijn zo groot dat aanvullende besluitvorming en een begrotingswijziging nodig zijn |
| C. Ernstige verwonding of de dood van ten minste één natuurlijke persoon | Het incident raakt of kan de fysieke veiligheid raken, bijvoorbeeld via een systeem dat een fysiek proces of de hulpverlening ondersteunt |

Eén drempelwaarde volstaat. Bij twijfel melden: afwijken van de drempels kan alleen leiden tot méér melden,
nooit tot minder.

### 4.3 Gevolgen, niet oorzaken

De toets kijkt naar de gevolgen, maar de oorzaak moet wel verband houden met een netwerk- en
informatiesysteem. Een vuilniswagen die iemand aanrijdt is geen Cbw-incident. Een zelfrijdende vuilniswagen
die door een storing in zijn systemen iemand aanrijdt, wel.

### 4.4 Geplande onderbrekingen

Gepland onderhoud of een contractueel afgesproken onderbreking is geen significant incident, ook niet als het
langer dan vier uur duurt. Dat geldt alleen voor de geplande gevolgen. Een mislukte update die tot onvoorziene
uitval leidt, valt er niet onder.

### 4.5 Onder de drempel

Incidenten onder de drempel, bijna-incidenten en cyberdreigingen zijn niet meldplichtig, maar kunnen
vrijwillig worden gemeld.

### 4.6 Datalekken

De drempelwaarden gaan over beschikbaarheid, geld en veiligheid. Een incident dat alleen de vertrouwelijkheid
van persoonsgegevens raakt, ook van bijzondere persoonsgegevens of het BSN, is op zichzelf geen significant
incident onder de Cbw, tenzij het ook drempel A, B of C (kan) halen. Voor zo'n datalek geldt de eigen meldplicht
bij de Autoriteit Persoonsgegevens, los van de Cbw.

## 5. De meldingsketen

### 5.1 Kennisname: T0

De termijnen lopen vanaf het moment dat de gemeente kennis kreeg van het significante incident: **T0**. Niet
het moment waarop het CTD bijeenkomt. De opschaling voegt zich naar de klok, niet andersom.

Kennisname is er zodra een medewerker met een rol in de incidentafhandeling informatie heeft waaruit een
redelijk handelend professional zou concluderen dat er mogelijk een significant incident is. Die medewerker
legt het incident direct vast in het incidentregistratiesysteem; het tijdstip van die registratie is T0.

### 5.2 De klok

De termijnen zijn kalendertermijnen. Ze lopen door in avonden, weekenden en vakanties. Kennisname op
vrijdagavond betekent uiterlijk zaterdagavond melden.

### 5.3 Termijnen en interne streeftijden

De wettelijke termijnen zijn uiterste grenzen, geen streeftijden.

| Fase | Product | Wettelijke deadline | Interne streeftijd |
|---|---|---|---|
| 1 | Vroegtijdige waarschuwing | Onverwijld, uiterlijk T0 + 24 uur | T0 + 8 uur |
| 1 | Informatieplicht | Onverwijld | T0 + 8 uur |
| 2 | Melding met initiële beoordeling | Onverwijld, uiterlijk T0 + 72 uur | T0 + 48 uur |
| - | Tussentijds verslag | Binnen de termijn die de verzoeker stelt | Een werkdag vóór die termijn gereed |
| - | Voortgangsverslag, als het incident na een maand nog loopt | Een maand na de melding van fase 2 | Drie werkdagen vóór de deadline gereed |
| 3 | Eindverslag | Een maand na de melding van fase 2; bij een lopend incident een maand na afhandeling | Drie werkdagen vóór de deadline gereed |

De maandtermijn loopt vanaf de melding van fase 2, niet vanaf T0 en niet vanaf het moment van herstel.

### 5.4 Inhoud per fase

| Fase | Wat | Aan wie | Kern |
|---|---|---|---|
| 1 | Vroegtijdige waarschuwing | NCSC | Signaal, geen analyse: vermoeden van kwaadwillige opzet, mogelijke grensoverschrijdende gevolgen, contactgegevens |
| 1 | Informeren van ontvangers van diensten | Inwoners, bedrijven, instellingen, ketenpartners | Bij een incident: kennisgeving. Bij een dreiging: welke maatregelen zij zelf kunnen nemen |
| 2 | Melding met initiële beoordeling | NCSC | Update van de waarschuwing, ernst en gevolgen, indicatoren van aantasting, grensoverschrijdende gevolgen |
| - | Tussentijds verslag | Op verzoek van CSIRT of bevoegde autoriteit | Relevante updates; kan meermaals worden gevraagd |
| - | Voortgangsverslag | CSIRT en bevoegde autoriteit | Dezelfde onderdelen als het eindverslag |
| 3 | Eindverslag | NCSC | Gedetailleerde beschrijving, grondoorzaak, toegepaste en lopende maatregelen, grensoverschrijdende gevolgen |

## 6. De informatieplicht

De informatieplicht staat naast de meldplicht en heeft een eigen doel: ontvangers van gemeentelijke diensten
in staat stellen zich te beschermen.

| Situatie | Verplichting |
|---|---|
| A. Significant incident dat de dienstverlening nadelig kan raken | De ontvangers van de diensten onverwijld in kennis stellen |
| B. Significante cyberdreiging die ontvangers kan treffen | Onverwijld meedelen welke maatregelen zij zelf kunnen nemen, en indien nodig de dreiging zelf |

Gelden beide, dan beide. **De volgorde is niet vrijblijvend:** eerst het handelingsperspectief, pas "indien
nodig" de dreiging. Het handelingsperspectief staat bovenaan het bericht.

| Stap | Verantwoordelijk | Termijn |
|---|---|---|
| Beoordelen of de informatieplicht geldt | CTD | Uiterlijk tegelijk met fase 1 |
| Inhoud van de kennisgeving opstellen | CTD | Streeftijd T0 + 8 uur |
| Vaststellen en verzenden aan inwoners, bedrijven en ketenpartners | CTD | Onverwijld |

## Bijlage A. Meldformulier (fase 1 en 2)

| Veld | Invulling |
|---|---|
| Meldende gemeente | |
| Intern incidentnummer | |
| Kennisname: datum en tijd (T0) | |
| Bron van kennisname | |
| Korte feitelijke omschrijving | Maximaal vijf regels: wat, welke dienst of welk systeem, sinds wanneer |
| Vermoeden van kwaadwillige of onrechtmatige handeling | ☐ Ja ☐ Nee ☐ Nog niet vast te stellen |
| Mogelijke grensoverschrijdende gevolgen | ☐ Ja ☐ Nee ☐ Nog niet vast te stellen. Zo ja: andere gemeenten, andere overheden, ketenpartners, andere EU-lidstaten |
| Contactgegevens verantwoordelijke functionaris | Naam, functie, telefoon (24/7), e-mail, alternatief kanaal bij compromittering |
| Aard en merkbare gevolgen | |
| Initiële beoordeling van ernst en gevolgen | Getroffen systemen en diensten; aantasting van ☐ beschikbaarheid ☐ integriteit ☐ vertrouwelijkheid ☐ authenticiteit; aantal getroffen inwoners, bedrijven of medewerkers; start en verwachte duur; gegevens ingezien, gewijzigd of geëxfiltreerd? ☐ Ja ☐ Nee ☐ Onbekend; geschatte financiële impact; status van herstel |
| Prognose hersteltijd | ☐ Nog niet te geven |
| Genomen en voorgenomen maatregelen | |
| Indicatoren van aantasting | IP-adressen, domeinnamen, hashes, misbruikte kwetsbaarheid (CVE), tijdstippen van activiteit |

## Bijlage B. Tussentijds of voortgangsverslag

| Veld | Invulling |
|---|---|
| Meldende gemeente, intern incidentnummer | |
| Soort verslag | ☐ Tussentijds verslag, op verzoek (artikel 28 Cbw): vul in tot en met "relevante updates". ☐ Voortgangsverslag (artikel 29, tweede lid, Cbw): het incident loopt nog wanneer het eindverslag verschuldigd is; vul ook a tot en met d in |
| Verwijzing naar de melding van fase 2 | Kenmerk, verzonden op |
| Datum waarop het eindverslag verschuldigd was | Een maand na fase 2 |
| Status | ☐ Duurt voort ☐ Onder controle, herstel loopt ☐ Afgehandeld op ... (eindverslag volgt binnen een maand) |
| Relevante updates sinds de laatste melding | Nieuwe feiten, gewijzigde impact, nieuwe indicatoren, genomen maatregelen, grensoverschrijdende gevolgen |
| a. Beschrijving, ernst en gevolgen | Chronologie, getroffen systemen en gegevens, omvang, gevolgen voor dienstverlening en derden |
| b. Soort bedreiging of grondoorzaak | Type dreiging; grondoorzaak (technisch, organisatorisch, menselijk, keten); wijze van binnenkomst; waarom bestaande maatregelen het niet voorkwamen; ☐ onderzoek loopt nog |
| c. Toegepaste en lopende maatregelen | Uitgevoerd met datum; lopend met eigenaar en datum; verwachte datum van afhandeling |
| d. Grensoverschrijdende gevolgen | ☐ Niet van toepassing ☐ Wel, namelijk |
| Verzonden aan | Tussentijds: de verzoeker. Voortgang: CSIRT en bevoegde autoriteit via het portaal. Datum en tijd |

## Bijlage C. Eindverslag

| Veld | Invulling |
|---|---|
| Meldende gemeente, intern incidentnummer, datum melding fase 2 | |
| Datum van afhandeling | Afgehandeld = verstoring beëindigd, toegang van de aanvaller weggenomen, dienstverlening hersteld. Nazorg en evaluatie staan daar niet aan in de weg |
| a. Beschrijving, ernst en gevolgen | Chronologie tot herstel, getroffen systemen en gegevens, omvang, gevolgen |
| b. Soort bedreiging of grondoorzaak | |
| c. Toegepaste en lopende maatregelen | Inclusief structurele verbeteringen in de zorgplichtmaatregelen |
| d. Grensoverschrijdende gevolgen | |

## Bijlage D. Sjablonen informatieplicht

**Variant 1. Significant incident**

| Onderdeel | Tekst |
|---|---|
| Onderwerp | Verstoring van [dienst] bij de gemeente [naam] |
| Wat is er aan de hand | Sinds [datum en tijd] is [dienst] geheel of gedeeltelijk niet beschikbaar door een cyberincident. |
| Wat betekent dit voor u | [Welke handelingen kunnen niet, welke gegevens kunnen zijn geraakt, welk alternatief is er.] |
| Wat doen wij | [Herstelmaatregelen in begrijpelijke taal. Vermeld dat het incident is gemeld bij de bevoegde instanties.] |
| Wat kunt u doen | [Alleen bij concreet handelingsperspectief. Anders: op dit moment hoeft u zelf niets te doen.] |
| Wanneer hoort u meer | Uiterlijk op [datum en tijd], ook als er dan nog geen nieuws is. |
| Waar kunt u terecht | [Telefoon, e-mail, pagina, en een kanaal dat werkt als de website onbereikbaar is.] |

**Variant 2. Significante cyberdreiging**

| Onderdeel | Tekst |
|---|---|
| Onderwerp | Belangrijk: maatregelen die u zelf kunt nemen |
| Welke maatregelen kunt u nemen | [Verplicht onderdeel. Concreet, genummerd, uitvoerbaar zonder technische kennis.] |
| Waarom vragen wij dit | [De dreiging, voor zover delen nodig is en de mitigatie niet schaadt.] |
| Wat doet de gemeente zelf | [Maatregelen van de gemeente.] |
| Waar kunt u terecht | [Contactgegevens.] |
