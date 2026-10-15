---
domein: ssd
titel: Beleid veilige softwareontwikkeling
samenvatting: Over beveiliging in software die de organisatie bouwt, laat bouwen of afneemt, voordat die in gebruik gaat. Behandelt architectuurprincipes, beveiligingseisen per toepassing, veilig ontwikkelen of de eisen daarvoor aan leveranciers, afspraken bij uitbestede ontwikkeling en testen met fictieve gegevens.
invoeren:
  - Leg de beveiligingsprincipes voor het ontwerp van informatiesystemen vast in een architectuurdocument (hoofdstuk 3).
  - Richt een vastgelegde toets van elk project en elke aanschaf aan de architectuurprincipes in (hoofdstuk 3).
  - Stel per nieuwe toepassing beveiligingseisen op, op basis van een erkende eisenset zoals OWASP ASVS (hoofdstuk 4).
  - Plan voor elke internetvoorziening een penetratietest vóór ingebruikname (hoofdstuk 4).
  - Neem de eisen uit het beleid op in het programma van eisen en het contract (hoofdstuk 6).
  - Regel in contracten auditrecht, toegang tot broncode, oplostermijnen en een meldregeling voor kwetsbaarheden (hoofdstuk 6).
  - Richt per oplevering een acceptatiedossier in met testverslag, penetratietest en componentenoverzicht (hoofdstuk 6).
  - Stel een formulier testgegevens op voor testen met persoonsgegevens (hoofdstuk 7).
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor het ontwerpen, bouwen, aanpassen en
testen van software. Het legt vast welke beveiligingsprincipes en eisen vooraf gelden, hoe veilig wordt
gebouwd, welke bewijzen bij een oplevering horen en wat de organisatie van een leverancier eist, zodat
beveiliging in de software zit voordat die in gebruik gaat. Het gaat over de ISO-beheersmaatregelen 8.25
tot en met 8.28 en 8.30; de regels voor testgegevens (8.33) staan hier mee ingevuld, omdat ze bij het
testen van software horen.

**Voor wie.** Het beleid is primair bedoeld voor de architect, de systeemeigenaren, de ontwikkelaars en
functioneel beheerders van de organisatie en voor de inkopers die software of maatwerk afnemen. Het geldt
ook voor ingehuurde ontwikkelaars en voor leveranciers die software voor de organisatie bouwen of
aanpassen.

**Waarop.** Alle software die de organisatie bouwt, laat bouwen of als maatwerk of SaaS-dienst afneemt:
applicaties, webapplicaties, apps, koppelingen (API), scripts en configuraties met logica, zoals low-code,
formulieren en workflows in een standaardpakket. Is de ontwikkeling uitbesteed, dan gelden de eisen uit
dit beleid als minimumeis voor de leverancier. De organisatie legt dat vast in het contract en toetst de
naleving met een onafhankelijke verklaring, zoals een ISO 27001-certificaat of een ISAE 3402- of ISAE
3000-rapport; het vastleggen loopt via het beleid informatiebeveiliging bij inkoop, het toetsen via het
beleid contractbeheer.

Buiten dit beleid vallen het in productie nemen van wijzigingen en het scheiden van omgevingen (beleid
wijzigingsbeheer), het verhelpen van kwetsbaarheden na ingebruikname (beleid kwetsbaarheden en
patchmanagement), de toegang tot broncode en omgevingen (beleid logische toegangsbeveiliging) en de
beveiligingstoets aan het begin van een project (beleid informatiebeveiliging in projecten).

::: als ontwikkeling=nee
De organisatie bouwt zelf geen software. Dit beleid is daarom vooral een set eisen die de organisatie stelt
aan leveranciers bij inkoop, maatwerk en configuratie. Ook configuratie met logica (formulieren, workflows,
koppelingen in een standaardpakket) door functioneel beheer valt eronder.
:::

## 2. Uitgangspunten

1. Beveiliging en privacy zitten in het ontwerp (security en privacy by design) en de veiligste instelling
   is de standaard (security by default).
2. Beveiligingseisen worden vastgesteld voordat er gebouwd of gekocht wordt, en getoetst voordat iets in
   gebruik gaat. Hoe hoger het impactniveau van de informatie, hoe zwaarder de eisen en de toets.
3. Voor uitbestede ontwikkeling gelden dezelfde eisen als voor eigen ontwikkeling.
4. Er wordt getest met fictieve gegevens; persoonsgegevens in test zijn een onderbouwde uitzondering.
5. Termijnen en frequenties in dit beleid die niet uit een wet of uit de BIO 2.0 komen, zijn standaardwaarden.
   De organisatie past ze aan op haar eigen risicoafweging en legt de keuze vast bij de vaststelling van dit beleid.

## 3. Architectuurprincipes

- De architect stelt beveiligingsprincipes voor het ontwerp van informatiesystemen vast en houdt ze bij in
  [[architectuurdocument: het document of de omgeving waarin de architectuurprincipes staan]]. Ze gelden
  voor elke ontwikkeling en aanschaf. Ten minste: [8.27.01]
  - toegang standaard geweigerd en per rol expliciet toegekend, voor elke pagina, functie, koppeling en
    gegevensverzameling;
  - aanmelden via de centrale identiteitsvoorziening met SSO en MFA volgens het beleid logische
    toegangsbeveiliging;
  - alleen versleutelde verbindingen, ook naar de achterliggende systemen, volgens het beleid cryptografie;
  - minimale gegevensverwerking en standaard de meest privacyvriendelijke instelling;
  - scheiding tussen klanten of omgevingen bij gedeelde (multi-tenant) platforms;
  - foutafhandeling die geen technische details prijsgeeft en invoer die aan de serverkant wordt
    gecontroleerd;
  - logging van beveiligingsrelevante gebeurtenissen volgens het beleid logging en monitoring.
- De architect en de CISO herzien de principes jaarlijks; [[lijneigenaar veilige ontwikkeling: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd IT of informatievoorziening]]
  stelt ze na elke herziening vast. [8.27.01]
- Bij elk project of elke aanschaf toetst de architect het ontwerp aan de principes en legt de toets vast.
  Een afwijking wordt vastgelegd en door de systeemeigenaar als risico geaccepteerd. [8.27.01]

## 4. Beveiligingseisen per toepassing

- Voor elke nieuwe toepassing of grote wijziging stelt de systeemeigenaar beveiligingseisen op, afgeleid
  uit het impactniveau, de vertrouwelijkheidsklasse en de risicoanalyse, en legt ze vast in het programma
  van eisen of de ontwerpdocumentatie. Voor webapplicaties en koppelingen gebruikt de organisatie een
  erkende eisenset als basis, bijvoorbeeld de OWASP ASVS: niveau 1 bij impactniveau gering of lager, niveau
  2 bij gemiddeld of hoger en niveau 3 bij informatie met het label strikt vertrouwelijk of geheim. [8.26.01]
- Voor webapplicaties gelden in elk geval: veilig sessiebeheer met een time-out, bescherming tegen
  brute-force-aanmeldingen, controle van alle invoer, geen gevoelige gegevens in de URL,
  beveiligingsheaders (zoals HSTS en een Content Security Policy) en registratie van de website of
  koppeling in de inventaris van bedrijfsmiddelen. De systeemeigenaar toont dat bij de acceptatie aan.
  [8.26.01]
- De beveiligingseisen gaan over de hele keten van de toepassing: de toegang, de verwerking, de opslag, de
  koppelingen met andere systemen en de gegevens die de toepassing uitwisselt. Bij een transactie met een
  burger of bedrijf eist de systeemeigenaar dat de identiteit van beide kanten vaststaat, de transactie
  niet te wijzigen of te ontkennen is en de gegevens onderweg en in rust versleuteld zijn. [8.26.01]
- Een internetvoorziening krijgt voor ingebruikname een penetratietest; de bevindingen met een hoog risico
  zijn opgelost voordat de voorziening live gaat. Het rapport hoort bij het acceptatiedossier. [8.26.01]

## 5. Veilig ontwikkelen

::: als ontwikkeling=ja
- [[lijneigenaar veilige ontwikkeling]] stelt een richtlijn voor veilig programmeren vast per gebruikte
  taal of platform, gebaseerd op een erkende bron zoals de OWASP-richtlijnen, en herziet die jaarlijks.
  Ontwikkelaars werken volgens die richtlijn en krijgen jaarlijks training in veilig ontwikkelen; de
  deelname staat in het opleidingsregister. [8.28.01]
- De organisatie legt het ontwikkelproces vast in [[ontwikkelrichtlijn: het document dat de werkwijze van de bouwstraat beschrijft]]:
  wie welke stap doet, welke beveiligingsactiviteit bij elke fase hoort (eisen, ontwerp, bouw, test,
  release), welke controles de bouwstraat afdwingt en hoe de omgevingen en de broncode beveiligd zijn. De
  lijneigenaar herziet de beschrijving jaarlijks. [8.25.01]
- Elke wijziging in code gaat via versiebeheer en wordt beoordeeld door een tweede ontwikkelaar voordat hij
  in de hoofdtak komt. De beoordeling let ook op beveiliging en is terug te vinden in het versiebeheer.
  [8.25.01, 8.28.01]
- De bouwstraat controleert elke wijziging automatisch met statische codeanalyse, controle op kwetsbare
  bibliotheken en op geheimen (wachtwoorden, sleutels) in de code. Bevindingen met een hoog risico houden de
  release tegen en de uitkomst van elke controle wordt bewaard. [8.25.01, 8.28.01]
- Ontwikkelaars gebruiken alleen bibliotheken en componenten uit bronnen die de organisatie heeft
  goedgekeurd, met een onderhouden versie, en vernieuwen ze binnen de termijnen van het beleid
  kwetsbaarheden en patchmanagement. Van elke applicatie is een overzicht van gebruikte componenten (SBOM)
  beschikbaar dat bij elke release wordt bijgewerkt. [8.25.01, 8.28.01]
- Geheimen staan in een sleutelkluis en niet in code of configuratiebestanden in de repository. De
  bouwstraat blokkeert een wijziging waarin een geheim staat. [8.28.01]
- Ontwikkel- en testomgevingen van de bouwstraat zijn beveiligd volgens het beleid logische
  toegangsbeveiliging: persoonlijke accounts, rechten per rol en geen schrijfrechten van ontwikkelaars in
  productie. [8.25.01]
:::

::: als ontwikkeling=nee
- Bij inkoop van software of maatwerk vraagt de inkoopadviseur de leverancier hoe die veilig ontwikkelt:
  een richtlijn voor veilig programmeren, codereview, geautomatiseerde controle op kwetsbare componenten,
  beveiliging van de ontwikkelomgeving en een proces voor kwetsbaarheden. Het antwoord weegt mee in de
  gunning en wordt bij het contract bewaard. [8.25.01, 8.28.01]
- De systeemeigenaar vraagt bij elke grote release een recente pentestrapportage of een ASVS-verklaring, en
  een overzicht van gebruikte componenten (SBOM) als de toepassing informatie met impactniveau kritiek of
  hoger verwerkt. [8.25.01]
- Configuratie met logica door functioneel beheer (formulieren, workflows, koppelingen) volgt de
  architectuurprincipes, wordt door een tweede functioneel beheerder beoordeeld en gaat via het beleid
  wijzigingsbeheer. [8.25.01, 8.28.01]
:::

## 6. Uitbestede ontwikkeling

- De eisen uit dit beleid gelden onverkort voor ontwikkeling door een leverancier, voor maatwerk en voor
  SaaS-diensten. De inkoopadviseur en de systeemeigenaar nemen ze op in het programma van eisen en in het
  contract. [8.30.01]
- Daarbovenop regelt het contract: het recht op audit of een onafhankelijke verklaring over het
  ontwikkelproces, het eigendom van of de toegang tot de broncode (bijvoorbeeld via escrow als de
  continuïteit dat vraagt), de termijn voor het oplossen van kwetsbaarheden, een regeling voor het melden
  van kwetsbaarheden bij de leverancier en de manier van opleveren en accepteren. [8.30.01]
- De systeemeigenaar controleert bij elke oplevering of de afgesproken bewijzen er zijn (testverslag,
  penetratietest, componentenoverzicht) en accepteert pas daarna. Het acceptatiebesluit en de bewijzen
  staan in het acceptatiedossier bij de wijziging. [8.30.01]
- De contracteigenaar beoordeelt jaarlijks per leverancier of de verklaring over het ontwikkelproces nog
  geldig is en of de leverancier de termijnen voor kwetsbaarheden heeft gehaald. [8.30.01]

::: als ontwikkeling=ja
- Huurt de organisatie ontwikkelaars in voor het eigen team, dan werken die in de eigen bouwstraat, met
  persoonlijke accounts en volgens dezelfde richtlijnen als eigen ontwikkelaars. Hun rechten vervallen op
  de laatste werkdag van de opdracht. [8.30.01]
:::

## 7. Testgegevens

- Er wordt getest met fictieve gegevens. Kan een test daar aantoonbaar niet mee, dan beoordeelt de
  opdrachtgever van de test stap voor stap of het kan met geanonimiseerde gegevens, daarna met
  gepseudonimiseerde gegevens en pas als laatste met productiegegevens. [8.33.01]
- Voor het maken van een geanonimiseerde of gepseudonimiseerde set en voor testen met gepseudonimiseerde of
  productiegegevens vult de opdrachtgever
  [[formulier testgegevens: het formulier of de registratie voor testen met persoonsgegevens]] in met doel,
  onderbouwing, benodigde gegevens en bewaartermijn. De privacy officer en de CISO geven advies. Volgt de
  opdrachtgever het advies niet, dan accepteert de proceseigenaar het risico schriftelijk. [8.33.01]
- Een testomgeving met persoonsgegevens krijgt dezelfde beveiliging als productie, alleen de minimaal
  nodige gegevens en een vaste einddatum waarop de beheerder de gegevens verwijdert. Het verwijderen wordt
  vastgelegd. [8.33.01]

## 8. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| [[lijneigenaar veilige ontwikkeling]] | Eigenaar van dit beleid; vaststellen van de architectuurprincipes, de richtlijn voor veilig programmeren en de beschrijving van het ontwikkelproces; de middelen voor de bouwstraat en training |
| Architect | Opstellen en bijhouden van de architectuurprincipes, toets op ontwerpen, vastleggen van afwijkingen |
| Systeemeigenaar | Beveiligingseisen per toepassing, acceptatie van opleveringen en van afwijkingen, opvragen van bewijzen bij leveranciers |
| Ontwikkelaars en functioneel beheerders | Bouwen en configureren volgens de richtlijn, codereview, bijhouden van het componentenoverzicht |
| Inkoopadviseur en contracteigenaar | Eisen uit dit beleid in het programma van eisen en het contract, jaarlijkse beoordeling van leveranciersverklaringen |
| Privacy officer of FG | Advies bij testen met persoonsgegevens en bij privacy by design |
| CISO | Advies, jaarlijkse herziening van de principes met de architect, toetsing van dit beleid en van afwijkingen |
| Leveranciers | Bouwen volgens de eisen en aanleveren van bewijs bij elke oplevering |

## 9. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in [[registratie van controles]]; afwijkingen gaan als bevinding naar het
risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| SSD-01 | De architectuurprincipes zijn in het afgelopen jaar herzien en vastgesteld, en elk project of elke aanschaf van het afgelopen jaar heeft een vastgelegde toets aan de principes | CISO | Jaarlijks | Vastgestelde versie van de principes, lijst van projecten en aanschaffen met de toets per project | 8.27.01 |
| SSD-02 | Elke nieuwe toepassing of grote wijziging heeft vastgelegde beveiligingseisen op het niveau dat bij het impactniveau past, en de eisen zijn bij de acceptatie aantoonbaar getoetst | [[lijneigenaar veilige ontwikkeling]] | Halfjaarlijks | Steekproef van vijf opleveringen met de eisen en het acceptatiedossier | 8.26.01 |
| SSD-03 | Elke internetvoorziening die in gebruik is gegaan, heeft een penetratietestrapport van vóór de ingebruikname zonder open bevindingen met hoog risico | CISO | Halfjaarlijks | Lijst van nieuwe internetvoorzieningen uit de inventaris met het rapport per voorziening | 8.26.01 |
| SSD-04 | De beschrijving van het ontwikkelproces en de richtlijn voor veilig programmeren zijn ten hoogste een jaar oud, elke ontwikkelaar heeft in het afgelopen jaar training gevolgd, en elke wijziging in de hoofdtak heeft een beoordeling door een tweede persoon en een geslaagde automatische controle | [[lijneigenaar veilige ontwikkeling]] | Per kwartaal | Vastgestelde documenten, opleidingsregister, rapport uit het versiebeheer en de bouwstraat over een steekproef van tien wijzigingen | 8.25.01, 8.28.01 |
| SSD-05 | Elke applicatie heeft een actueel componentenoverzicht en er staan geen geheimen in de repository | [[lijneigenaar veilige ontwikkeling]] | Per kwartaal | Componentenoverzichten met datum, uitkomst van de scan op geheimen | 8.25.01, 8.28.01 |
| SSD-06 | Elke oplevering van een leverancier is pas geaccepteerd na controle van de afgesproken bewijzen, en elk contract voor ontwikkeling, maatwerk of SaaS bevat de eisen uit dit beleid | Contracteigenaar | Jaarlijks | Steekproef van vijf opleveringen met het acceptatiedossier, contracten met de eisen, verklaringen van leveranciers | 8.30.01, 8.25.01, 8.28.01 |
| SSD-07 | Elke testomgeving met persoonsgegevens heeft een ingevuld formulier met advies en een einddatum, en de gegevens zijn op de einddatum verwijderd | Privacy officer | Jaarlijks | Steekproef van vijf testomgevingen met formulier, advies en registratie van de verwijdering | 8.33.01 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De
systeemeigenaar dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de looptijd.
De afwijking geldt pas na acceptatie van het risico door [[risico-eigenaar: de manager die restrisico's accepteert]]
en staat in het risicoregister; afwijkingen worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 10. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid
informatiebeveiliging in projecten (de toets aan het begin), het beleid wijzigingsbeheer (testen, acceptatie
en scheiding van omgevingen), het beleid informatieclassificatie (impactniveau en vertrouwelijkheidslabel
als maat voor de eisen), het beleid informatiebeveiliging bij inkoop en contractbeheer (eisen in inkoop en
contract), het beleid logische toegangsbeveiliging (toegang tot broncode en omgevingen), het beleid
cryptografie (versleutelde verbindingen en sleutelkluis), het beleid kwetsbaarheden en patchmanagement
(kwetsbare componenten en penetratietesten na ingebruikname) en het privacybeleid (privacy by design en
testen met persoonsgegevens).
