# Beleid informatieclassificatie

[Download als Word](classificatie.docx) · [Maak je eigen versie in de generator](beleidsset-generator.html)

| | |
|---|---|
| Documenttype | Beleid informatiebeveiliging onder het strategisch informatiebeveiligingsbeleid; BIO 2.0-domein *Informatie classificatie* |
| Status | Concept, vast te stellen door de organisatie |
| Eigenaar | **[eigenaar van dit beleid]** |
| Vaststeller | **[vaststeller]** |
| Evaluatie | Jaarlijks, in de plan-do-check-act-cyclus van het managementsysteem voor informatiebeveiliging |

**In het kort.** Over het classificeren, labelen en veilig overdragen van informatie op beschikbaarheid, integriteit en vertrouwelijkheid. Behandelt de classificatiemethode met vijf impactniveaus, de minimumeisen per label, het labelen van documenten en hardware, en de eisen aan websites, e-mail, certificaten en andere overdracht.

**Onderwerpen.** 3. Classificatiemethode; 4. Eisen per niveau; 5. Labelen; 6. Overdragen van informatie.

Zonder profiel: tekst die van een contextvraag afhangt, staat in een kader met de vraag erboven.

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor het classificeren, labelen en veilig
overdragen van informatie. Classificeren is het vaststellen hoe zwaar informatie beschermd moet worden op
beschikbaarheid, integriteit en vertrouwelijkheid (BIV). De classificatie bepaalt welke maatregelen uit de
andere beleidsstukken van toepassing zijn: de toegangsrechten, de versleuteling, de logging, de zone waarin
een systeem staat en de manier waarop een drager wordt afgevoerd. Het gaat over de ISO-beheersmaatregelen
5.12 tot en met 5.14.

**Voor wie.** Het beleid is primair bedoeld voor proceseigenaren, die de classificatie van hun informatie
vaststellen, en voor systeemeigenaren, die de maatregelen bij een classificatie toepassen. De regels voor
labelen en behandelen gelden voor iedereen die informatie van de organisatie verwerkt: medewerkers, inhuur,
stagiairs, vrijwilligers en leveranciers.

**Waarop.** Alle informatie van de organisatie, in alle systemen en op alle dragers: digitaal, op papier en
in gesprekken, en alle websites, webapplicaties, koppelvlakken en e-mailvoorzieningen waarmee de organisatie
informatie overdraagt. Is een systeem of een overdrachtsvoorziening uitbesteed, dan gelden de eisen uit dit
beleid als minimumeis voor die leverancier. De organisatie legt dat vast in het contract en toetst de
naleving met een onafhankelijke verklaring, zoals een ISO 27001-certificaat of een ISAE 3402- of ISAE
3000-rapport; het vastleggen loopt via het beleid informatiebeveiliging bij inkoop, het toetsen via het beleid
contractbeheer.

Buiten dit beleid vallen de versleutelingseisen zelf (beleid cryptografie), de toegangsrechten per
classificatie (beleid logische toegangsbeveiliging), de zone-indeling van ruimten (beleid fysieke toegang en
beveiliging) en het wissen en vernietigen van dragers (beleid afvoer en hergebruik van gegevensdragers).

## 2. Uitgangspunten

1. De eigenaar van de informatie (meestal de proceseigenaar) bepaalt de classificatie en accepteert het
   restrisico. De CISO en de privacy officer adviseren.
2. Zo laag als verantwoord: te hoog classificeren kost geld en belemmert openbaarheid. Wettelijke eisen gaan
   altijd voor.
3. Het meest gevoelige deel bepaalt de classificatie van het geheel. Een systeem krijgt de classificatie van
   de zwaarste informatie die het verwerkt, tenzij het systeem die informatie apart afschermt.
4. Eén schaal voor de hele organisatie: de vijf impactniveaus uit dit beleid sturen de zones, de
   toegangsrechten, de versleuteling en de bewaring, zodat een classificatie overal hetzelfde betekent.
5. Termijnen en frequenties in dit beleid die niet uit een wet of uit de BIO 2.0 komen, zijn standaardwaarden.
   De organisatie past ze aan op haar eigen risicoafweging en legt de keuze vast bij de vaststelling van dit beleid.

## 3. Classificatiemethode

1. De organisatie classificeert met een vastgestelde impactmethode die deel uitmaakt van de
   risicomanagementmethode van de organisatie, bijvoorbeeld een baselinetoets of een BIA. De methode staat in
   **[classificatiemethode]**; de CISO beoordeelt
   de methode jaarlijks. [5.12.01]
2. De proceseigenaar schat per BIV-aspect de gevolgen van uitval, van onjuiste of onvolledige informatie en
   van ongewenste openbaarmaking, en kiest per aspect een van vijf impactniveaus. De beschikbaarheidswaarden
   in de tabel zijn standaardwaarden; de organisatie past ze aan in de classificatiemethode en legt per
   systeem de definitieve hersteltijd en het toelaatbaar gegevensverlies vast in het continuïteitsbeleid.
   [5.12.01]

   | Impactniveau | Beschikbaarheid | Integriteit | Vertrouwelijkheid |
   |---|---|---|---|
   | verwaarloosbaar | uitval langer dan een week en verlies van een week aan gegevens zijn aanvaardbaar | fouten hebben geen gevolgen voor besluiten of dienstverlening | geen schade bij openbaarmaking; label openbaar |
   | gering | uitval tot een week, gegevensverlies tot een werkdag | fouten geven hinder en extra werk, zijn achteraf te herstellen | beperkte schade, zoals ongemak of een klacht; label intern |
   | gemiddeld | uitval tot een werkdag, gegevensverlies tot vier uur | fouten leiden tot verkeerde besluiten of betalingen met herstelbare schade | schade voor burgers, partners of de organisatie, zoals een datalek met meldplicht; label vertrouwelijk |
   | ernstig | uitval tot vier uur, gegevensverlies tot een uur | fouten geven rechtsgevolgen of financiële schade die moeilijk te herstellen is | ernstige schade voor personen (veiligheid, bestaanszekerheid) of voor het functioneren van de organisatie; label strikt vertrouwelijk |
   | catastrofaal | uitval tot een uur, geen gegevensverlies | fouten raken leven, gezondheid of de rechtsstaat | schade voor de staat, de openbare orde of levens; weerstand tegen statelijke actoren en georganiseerde criminaliteit; label geheim |

3. De proceseigenaar classificeert de informatie in elk informatiesysteem op basis van een expliciete
   risicoafweging vóór ingebruikname, daarna bij elke ingrijpende wijziging en ten minste elke **[herzieningstermijn classificatie]**. De
   uitkomst staat in een classificatierapport met de ingevulde vragenlijsten, door de proceseigenaar
   ondertekend als besluit. [5.12.01]
4. De systeemeigenaar registreert de classificatie per systeem en per gegevensverzameling in de inventaris van
   bedrijfsmiddelen binnen een maand na het besluit. [5.12.01]
5. Het niveau catastrofaal vraagt altijd een eigen risicoanalyse door de CISO; de organisatie richt daar geen
   standaardmaatregelen voor in. [5.12.01]

> **Alleen als: Wat voor organisatie ben je? «Ministerie of kerndepartement» of «Rijksdienst, agentschap of inspectie» of «Zelfstandig bestuursorgaan»**
>
> 6. Bijzondere informatie van het Rijk krijgt naast het vertrouwelijkheidslabel de rubricering uit het
>    Voorschrift Informatiebeveiliging Rijksdienst Bijzondere Informatie. De classificatiemethode legt vast
>    welke rubricering bij welk label hoort; bij verschil geldt de zwaarste eis. [5.12.01]

## 4. Eisen per niveau

1. Elk vertrouwelijkheidslabel heeft een vaste set minimumeisen; de basis is de BIO 2.0 en de
   risicoafweging van de proceseigenaar. De systeemeigenaar past ten minste de volgende eisen toe en toont
   dat aan bij de ingebruikname: [5.12.01]

   | Label | Authenticatie | Autorisatie | Opslag en transport |
   |---|---|---|---|
   | openbaar | geen eis voor lezen; persoonsgebonden account voor wijzigen | iedereen mag lezen; wijzigen alleen door aangewezen medewerkers | integriteit van de bron bewaakt; transport via de standaarden voor internetverkeer |
   | intern | persoonsgebonden account; meerfactor bij toegang van buiten | toegang voor medewerkers van de organisatie | versleuteld transport buiten het eigen netwerk |
   | vertrouwelijk | meerfactor | toegang per rol, door de eigenaar toegekend en jaarlijks beoordeeld | versleuteld transport en versleutelde opslag; zo min mogelijk kopieën; niet op verwijderbare media zonder uitzondering |
   | strikt vertrouwelijk | meerfactor met een sterk middel; geen toegang vanaf niet-beheerde apparaten | toegang per persoon met doelbinding, door de eigenaar toegekend en elk halfjaar beoordeeld; vierogenprincipe bij wijzigingen met rechtsgevolg | versleuteld met sleutels in eigen beheer; opslag alleen in systemen in zone 3 of hoger of bij een leverancier met gelijkwaardige verklaring; logging van elke toegang |
   | geheim | meerfactor met een sterk middel, geen single sign-on | toegang per persoon, vierogenprincipe bij toegang en wijziging | aanvullende maatregelen op basis van een eigen risicoanalyse door de CISO |

2. Voor integriteit van gemiddeld en hoger geldt het vierogenprincipe bij wijzigingen van gegevens die
   rechtsgevolgen hebben, en logt het systeem elke wijziging met wie, wat en wanneer volgens het beleid logging
   en monitoring. [5.12.01]
3. Voor beschikbaarheid legt de proceseigenaar per systeem de hersteltijd en het toelaatbaar gegevensverlies
   vast in het continuïteitsbeleid, op basis van het impactniveau uit de tabel in hoofdstuk 3. [5.12.01]
4. De zone-indeling in het beleid fysieke toegang en beveiliging volgt de impactniveaus: een systeem staat in
   de zone die bij zijn hoogste impactniveau hoort. De systeemeigenaar controleert dat bij ingebruikname en bij
   elke herclassificatie. [5.12.01]

> **Alleen als: In welke gevoelige domeinen verwerk je persoonsgegevens? «Sociaal domein» of «Jeugd»**
>
> 5. Informatie over cliënten in het sociaal domein of de jeugdhulp krijgt ten minste vertrouwelijk voor
>    vertrouwelijkheid en gemiddeld voor integriteit. Een lagere classificatie kan alleen met een gedocumenteerd
>    besluit van de proceseigenaar na advies van de privacy officer. [5.12.01]

> **Alleen als: In welke gevoelige domeinen verwerk je persoonsgegevens? «Gezondheid (WvGGZ, NTA 7516)»**
>
> 6. Gezondheidsinformatie is een bijzonder persoonsgegeven en krijgt ten minste strikt vertrouwelijk. Ad-hoc
>    uitwisseling per e-mail of chat voldoet aan de NTA 7516: gezondheidsinformatie hoort in het vakinhoudelijke
>    systeem, gaat per e-mail alleen als dat niet kan en dan alleen versleuteld via beveiligde mail, met een
>    vastgestelde grond om te verzenden en een gecontroleerde ontvanger. Automatisch doorsturen,
>    leesbevestigingen en het delen van inloggegevens zijn niet toegestaan; wie namens een ander mailt, doet dat
>    via een zichtbare mandaatfunctie. [5.12.01]
> 7. De organisatie biedt burgers een beveiligde mailvoorziening aan en vermeldt die op de website;
>    **[beheerder internetfacing systemen]**
>    controleert jaarlijks dat de voorziening werkt en vindbaar is. [5.14.01]

> **Alleen als: Verwerk je politiegegevens (boa's, opsporing, handhaving)? «Ja»**
>
> 8. Politiegegevens die de organisatie verwerkt (bijvoorbeeld door boa's of in de handhaving) worden apart
>    geclassificeerd en krijgen ten minste strikt vertrouwelijk. Ze worden gescheiden gehouden van de overige informatie
>    in een systeem of omgeving waarvoor de autorisatie-, logging- en bewaareisen van de Wet politiegegevens
>    gelden, en gaan niet via gewone e-mail of chat naar ontvangers buiten de kring die de wet toestaat.
>    [5.12.01]

## 5. Labelen

1. Informatie met het label vertrouwelijk of hoger is herkenbaar gelabeld: digitaal met een
   classificatielabel in de metagegevens van het document, het bericht of de gegevensverzameling, en op
   papier met het label op elke pagina. Wie een document maakt of verzendt, labelt het; de proceseigenaar
   bepaalt het label van een gegevensverzameling. [5.13.01]
2. Informatie zonder label geldt als intern. Openbare informatie hoeft geen label; wie informatie als openbaar
   publiceert, doet dat alleen na een besluit van de proceseigenaar. [5.13.01]
3. Systemen die labels ondersteunen, passen bij het label automatisch de bijbehorende beveiliging toe:
   versleuteling, beperking van delen en afdrukken, en blokkering van verzending naar ontvangers buiten de
   organisatie bij strikt vertrouwelijk en geheim. De systeemeigenaar richt dat in en test het bij elke wijziging van
   het labelbeleid. [5.13.01]
4. Een label verandert alleen als de proceseigenaar daartoe besluit, bijvoorbeeld bij openbaarmaking na een
   besluit op grond van de Wet open overheid; de wijziging wordt vastgelegd met datum en reden. [5.13.01]
5. Hardware krijgt een sticker met het kenmerk uit de inventaris; de classificatie van de hardware zelf staat
   in de inventaris en niet op de sticker, zodat een gevonden apparaat niet prijsgeeft wat erop staat.
   [5.13.01]
6. De proceseigenaar controleert jaarlijks met een steekproef of de informatie in zijn systemen en
   documentopslag juist is gelabeld, en laat afwijkingen binnen een maand herstellen. [5.13.01]

## 6. Overdragen van informatie

1. Websites, webapplicaties, API's en het e-mailverkeer van de organisatie die vanaf internet bereikbaar zijn,
   voldoen aan de verplichte standaarden van de lijst van het Forum Standaardisatie en aan de eisen uit het
   Cyberbeveiligingsbesluit. De systeemeigenaar stelt die zo in dat de beveiliging maximaal is zonder dat de
   dienst ervan uitvalt. [5.14.01]
2. **[beheerder internetfacing systemen]** meet elke maand alle domeinen met internet.nl, rapporteert de scores
   aan de CISO en zet tekortkomingen binnen drie maanden om in een wijziging of een geaccepteerd risico.
   [5.14.01]
3. Voor openbaar webverkeer met gevoelige gegevens gebruikt de organisatie ten minste publiek vertrouwde
   OV-certificaten; voor intern webverkeer met gevoelige gegevens ten minste publiek vertrouwde OV-certificaten
   of PKIoverheid-certificaten uit een private stam. Zwaardere certificaten volgen uit een risicoanalyse,
   aansluitvoorwaarden of wetgeving. De beheerder houdt een certificaatregister bij met de vervaldatum en
   vernieuwt certificaten ten minste twee weken voor afloop. [5.14.02]
4. Gebruikt de organisatie geavanceerde of gekwalificeerde elektronische handtekeningen, dan voldoen die aan
   de AdES Baseline Profiles van de lijst open standaarden. Bij aanschaf van een ondertekendienst neemt inkoop
   dat als eis op in de uitvraag; de systeemeigenaar toetst het bij acceptatie. [5.14.03]
5. **[beheerder internetfacing systemen]** houdt één actuele registratie bij van alle internetfacing systemen,
   webapplicaties, IP-adressen en API's, als onderdeel van de inventaris van bedrijfsmiddelen. Een nieuw
   systeem komt pas online na registratie; de beheerder vergelijkt de registratie elk halfjaar met een externe
   scan van de domeinen en IP-reeksen van de organisatie. [5.14.04]
6. Alle publiek toegankelijke websites van de organisatie staan in het Register Internetdomeinen Overheid.
   **[beheerder internetfacing systemen]** werkt de registratie bij binnen een maand na elke wijziging en
   controleert haar ten minste elk halfjaar. [5.14.05]
7. Wie informatie met het label vertrouwelijk of hoger buiten de organisatie deelt, gebruikt een
   overdrachtsvoorziening die bij het label past (beveiligde mail, een beveiligd uitwisselplatform of een
   gecontroleerde koppeling) en controleert vooraf de ontvanger. Informatie met het label strikt vertrouwelijk of
   hoger gaat alleen naar ontvangers met wie een schriftelijke afspraak over vertrouwelijkheid bestaat.
   [5.14.01]

## 7. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| Proceseigenaar (eigenaar van de informatie) | Classificatie, classificatierapport, acceptatie van het restrisico, labels van gegevensverzamelingen, jaarlijkse steekproef op labels, besluiten over openbaarmaking |
| Systeemeigenaar | Toepassen van de minimumeisen bij de classificatie, registratie in de inventaris, zone van het systeem, automatische toepassing van labels |
| **[beheerder internetfacing systemen]** | Metingen met internet.nl, certificaatregister, registratie van internetfacing systemen en het Register Internetdomeinen Overheid |
| CISO | Classificatiemethode, advies bij classificatie, risicoanalyse bij catastrofaal en geheim, jaarlijkse toetsing van opzet en werking van dit beleid |
| Privacy officer of FG | Advies bij classificatie van persoonsgegevens en bij een lagere classificatie van gevoelige domeinen |
| Inkoop en contractbeheer | Eisen uit dit beleid in uitvragen en contracten, toetsen van verklaringen van leveranciers |
| Medewerkers en inhuur | Informatie labelen, volgens het label behandelen en via de passende voorziening overdragen |

## 8. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in **[registratie van controles]**;
afwijkingen gaan als bevinding naar het risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| CLS-01 | Elk systeem en elke gegevensverzameling in de inventaris heeft een classificatie per BIV-aspect die niet ouder is dan drie jaar, met een ondertekend classificatierapport | CISO | Jaarlijks | Lijst uit de inventaris met ontbrekende of verlopen classificaties en de afhandeling | 5.12.01 |
| CLS-02 | De systemen met het label strikt vertrouwelijk of geheim voldoen aan de minimumeisen voor authenticatie, autorisatie, opslag en zone | CISO | Jaarlijks | Toetsverslag per systeem met de afwijkingen | 5.12.01 |
| CLS-03 | Informatie in de documentopslag en de systemen van de proceseigenaar draagt het juiste label en systemen passen bij het label de beveiliging toe | Proceseigenaar | Jaarlijks | Steekproef van ten minste twintig documenten of gegevensverzamelingen, testverslag van de automatische toepassing | 5.13.01 |
| CLS-04 | Alle domeinen voldoen aan de verplichte internetstandaarden; tekortkomingen zijn binnen drie maanden omgezet in een wijziging of een geaccepteerd risico | **[beheerder internetfacing systemen]** | Maandelijks, met een kwartaaloverzicht aan de CISO | internet.nl-scores per domein, overzicht van de opvolging | 5.14.01 |
| CLS-05 | De registratie van internetfacing systemen en het Register Internetdomeinen Overheid komen overeen met een externe scan van de domeinen en IP-reeksen van de organisatie | **[beheerder internetfacing systemen]** | Halfjaarlijks | Scanrapport met de vergelijking en de afhandeling van verschillen | 5.14.04, 5.14.05 |
| CLS-06 | Internetfacing systemen met gevoelige gegevens gebruiken certificaten van het vereiste type en geen certificaat is verlopen | CISO | Jaarlijks | Steekproef op het certificaatregister en de systemen | 5.14.02 |
| CLS-07 | Ondertekendiensten in gebruik voldoen aan de AdES Baseline Profiles en de eis staat in de uitvragen van dat jaar | Systeemeigenaar van de ondertekendienst | Jaarlijks | Verklaring of testrapport van de leverancier, uitvraagdocumenten | 5.14.03 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De
proceseigenaar dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de looptijd. De
afwijking geldt pas na acceptatie van het risico door **[risico-eigenaar]**
en staat in het risicoregister; afwijkingen worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 9. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. De classificatie stuurt het beleid
logische toegangsbeveiliging (rechten per label), het beleid cryptografie (versleuteling per label), het
beleid logging en monitoring (logging van wijzigingen en toegang), het beleid fysieke toegang en beveiliging
(zones per impactniveau), het beleid afvoer en hergebruik van gegevensdragers (methode per label), het beleid
mobile device management (toegang vanaf beheerde apparaten) en het continuïteitsbeleid (hersteltijd en
gegevensverlies). De inventaris uit het beleid bedrijfsmiddelenbeheer bevat de classificaties en de
registratie van internetfacing systemen; het beleid informatiebeveiliging bij inkoop en contractbeheer regelt
de eisen aan leveranciers.

## Bijlage A: BIO 2.0-maatregelen

De maatregelen van dit domein (7, waarvan 6 overheidsmaatregelen), waar dit stuk ze invult en welke controle ze aantoont. Nummers volgens BIO2 v1.3 definitief - 9 januari 2026; de tekst van de maatregel staat bij het CIP. Waar de BIO 2.0 geen overheidsmaatregel kent, geldt de ISO 27002-beheersmaatregel.

| Maatregel | Titel | Soort | In dit stuk | Controle |
|---|---|---|---|---|
| 5.12.01 | Classificeren van informatie | overheidsmaatregel | 3. Classificatiemethode | CLS-01, CLS-02 |
| 5.13.01 | Labelen van informatie | ISO-beheersmaatregel | 5. Labelen | CLS-03 |
| 5.14.01 | Overdragen van informatie | overheidsmaatregel | 4. Eisen per niveau | CLS-04 |
| 5.14.02 | Overdragen van informatie | overheidsmaatregel | 6. Overdragen van informatie | CLS-06 |
| 5.14.03 | Overdragen van informatie | overheidsmaatregel | 6. Overdragen van informatie | CLS-07 |
| 5.14.04 | Overdragen van informatie | overheidsmaatregel | 6. Overdragen van informatie | CLS-05 |
| 5.14.05 | Overdragen van informatie | overheidsmaatregel | 6. Overdragen van informatie | CLS-05 |

## Bijlage B: Afkortingen

| Afkorting | Betekenis |
|---|---|
| API | Application programming interface, een koppelvlak tussen systemen |
| BIA | Business impact analyse |
| BIO | Baseline Informatiebeveiliging Overheid |
| BIV | Beschikbaarheid, integriteit en vertrouwelijkheid |
| CISO | Chief Information Security Officer |
| FG | Functionaris gegevensbescherming |
| IP | Internet protocol |
| ISAE | International Standard on Assurance Engagements |
| ISO | International Organization for Standardization |
| NTA | Nederlandse technische afspraak |
| OV | Organization validated, een certificaattype |
| WvGGZ | Wet verplichte geestelijke gezondheidszorg |

## Nog in te vullen

- **classificatiemethode**: het vastgestelde document met vragenlijsten en impactschaal
- **herzieningstermijn classificatie**: standaard drie jaar
- **beheerder internetfacing systemen**: de functie die de metingen uitvoert, bijvoorbeeld de netwerkbeheerder
- **registratie van controles**: het systeem waarin controles worden vastgelegd, bijvoorbeeld het ticketsysteem of het managementsysteem
- **risico-eigenaar**: de manager die restrisico's accepteert
- **eigenaar van dit beleid**: de manager die dit beleid uitvoert en laat naleven
- **vaststeller**: wie het beleid vaststelt, bijvoorbeeld de directie of het bestuur
