---
domein: ssd
titel: Beleid veilige softwareontwikkeling
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor het ontwerpen, bouwen, aanpassen en
testen van software: applicaties, webapplicaties, apps, koppelingen (API's), scripts en configuraties met
logica, zoals low-code en workflows. Het geldt voor ontwikkeling door de organisatie zelf en voor
ontwikkeling die ze uitbesteedt of als maatwerk of SaaS-dienst afneemt. Het gaat over de
ISO-beheersmaatregelen 8.25 tot en met 8.28 en 8.30.

Buiten dit beleid vallen het in productie nemen van wijzigingen en het scheiden van omgevingen (beleid
wijzigingsbeheer), het oplossen van kwetsbaarheden na ingebruikname (beleid vulnerability- en
patchmanagement) en de toegang tot broncode (beleid logische toegangsbeveiliging).

::: als ontwikkeling=nee
De organisatie bouwt zelf geen software. Dit beleid is daarom vooral een set eisen die de organisatie stelt
aan leveranciers bij inkoop, maatwerk en configuratie. Ook configuratie met logica (formulieren, workflows,
koppelingen in een standaardpakket) valt eronder.
:::

## 2. Uitgangspunten

1. Beveiliging en privacy zitten in het ontwerp (security en privacy by design) en de veiligste instelling
   is de standaard (security by default).
2. Beveiligingseisen worden vastgesteld voordat er gebouwd of gekocht wordt, en getoetst voordat iets in
   gebruik gaat.
3. Voor uitbestede ontwikkeling gelden dezelfde eisen als voor eigen ontwikkeling.
4. Er wordt getest met fictieve gegevens; persoonsgegevens in test zijn een onderbouwde uitzondering.

## 3. Beleidsregels

### 3.1 Architectuurprincipes

- De organisatie stelt beveiligingsprincipes voor het ontwerp van informatiesystemen vast en houdt ze
  bij in de architectuur. Ze gelden voor elke ontwikkeling en aanschaf. Ten minste: [8.27.01]
  - toegang standaard geweigerd en per rol expliciet toegekend, voor elke pagina, functie, API en
    gegevensverzameling;
  - aanmelden via de centrale identiteitsvoorziening met single sign-on en MFA volgens het beleid logische
    toegangsbeveiliging;
  - alleen versleutelde verbindingen, ook naar de backend, volgens het beleid cryptografie;
  - minimale gegevensverwerking en standaard de meest privacyvriendelijke instelling;
  - scheiding tussen klanten of omgevingen bij gedeelde (multi-tenant) platforms;
  - logging van beveiligingsrelevante gebeurtenissen volgens het beleid logging en monitoring.
- De principes worden jaarlijks door de architect en de CISO herzien en na elke herziening vastgesteld. [8.27.01]
- Bij elk project of elke aanschaf toetst de architect het ontwerp aan de principes. Een afwijking wordt
  vastgelegd en door de systeemeigenaar als risico geaccepteerd. [8.27.01]

### 3.2 Beveiligingseisen per toepassing

- Voor elke nieuwe toepassing of grote wijziging stelt de systeemeigenaar beveiligingseisen op, afgeleid uit
  de classificatie en de risicoanalyse. Voor webapplicaties en API's gebruikt de organisatie een erkende
  eisenset als basis, bijvoorbeeld de OWASP Application Security Verification Standard (ASVS) op een niveau
  dat past bij de classificatie. [8.26.01]
- Voor webapplicaties gelden in elk geval: veilig sessiebeheer met een time-out, bescherming tegen
  brute-force-aanmeldingen, controle van alle invoer, geen gevoelige gegevens in de URL, beveiligingsheaders
  (zoals HSTS en een Content Security Policy) en een register van websites en API's in de inventaris van
  bedrijfsmiddelen. [8.26.01]
- Een internetvoorziening krijgt voor ingebruikname een penetratietest; de bevindingen met een hoog risico
  zijn opgelost voordat de voorziening live gaat. [8.26.01]

### 3.3 Veilig ontwikkelen

::: als ontwikkeling=ja
- Ontwikkelaars werken volgens een vastgestelde richtlijn voor veilig programmeren en krijgen jaarlijks
  training in veilig ontwikkelen. [8.28.01]
- Elke wijziging in code gaat via versiebeheer en wordt beoordeeld door een tweede ontwikkelaar voordat hij
  in de hoofdtak komt. [8.25.01, 8.28.01]
- De bouwstraat controleert elke wijziging automatisch met statische codeanalyse, controle op kwetsbare
  bibliotheken en op geheimen (wachtwoorden, sleutels) in de code. Bevindingen met een hoog risico houden de
  release tegen. [8.25.01, 8.28.01]
- Van elke applicatie is een overzicht van gebruikte componenten (een SBOM) beschikbaar, zodat een nieuwe
  kwetsbaarheid in een bibliotheek snel te vinden is. [8.25.01]
- Geheimen staan in een sleutelkluis en niet in code of configuratiebestanden in de repository. [8.28.01]
:::

::: als ontwikkeling=nee
- Bij inkoop van software of maatwerk vraagt de organisatie aan de leverancier hoe die veilig ontwikkelt:
  een richtlijn voor veilig programmeren, codereview, geautomatiseerde controle op kwetsbare componenten en
  een proces voor kwetsbaarheden. Het antwoord weegt mee in de gunning. [8.25.01, 8.28.01]
- De organisatie vraagt bij elke grote release een recente pentestrapportage of een ASVS-verklaring, en
  een overzicht van gebruikte componenten (SBOM) als de toepassing informatie met classificatie hoog
  verwerkt. [8.25.01]
- Configuratie met logica door functioneel beheer (formulieren, workflows, koppelingen) volgt de
  architectuurprincipes en gaat via wijzigingsbeheer. [8.25.01]
:::

### 3.4 Uitbestede ontwikkeling

- De eisen uit dit beleid gelden onverkort voor ontwikkeling door een leverancier, voor maatwerk en voor
  SaaS-diensten. De organisatie neemt ze op in het programma van eisen en in het contract. [8.30.01]
- Daarbovenop regelt het contract: het recht op audit of een onafhankelijke verklaring over het
  ontwikkelproces, het eigendom van of de toegang tot de broncode (bijvoorbeeld via escrow als de
  continuïteit dat vraagt), de termijn voor het oplossen van kwetsbaarheden, een regeling voor het melden van
  kwetsbaarheden (responsible disclosure) bij de leverancier en de manier van opleveren en accepteren. [8.30.01]
- De systeemeigenaar controleert bij elke oplevering of de afgesproken bewijzen er zijn (testverslag,
  pentest, componentenoverzicht) en accepteert pas daarna. [8.30.01]

::: als ontwikkeling=ja
- Huurt de organisatie ontwikkelaars in voor het eigen team, dan werken die in de eigen bouwstraat, met
  persoonlijke accounts en volgens dezelfde richtlijnen als eigen ontwikkelaars. [8.30.01]
:::

### 3.5 Testgegevens

- Er wordt getest met fictieve gegevens. Kan een test daar aantoonbaar niet mee, dan beoordeelt de
  opdrachtgever van de test stap voor stap of het kan met geanonimiseerde gegevens, daarna met
  gepseudonimiseerde gegevens en pas als laatste met productiegegevens. [8.33.01]
- Voor het maken van een geanonimiseerde of gepseudonimiseerde set en voor testen met gepseudonimiseerde of
  productiegegevens vult de opdrachtgever een formulier in met doel, onderbouwing, benodigde gegevens en
  bewaartermijn. De privacy officer en de CISO geven advies. Volgt de opdrachtgever het advies niet, dan
  accepteert de proceseigenaar het risico schriftelijk. [8.33.01]
- Een testomgeving met persoonsgegevens krijgt dezelfde beveiliging als productie, alleen de minimaal nodige
  gegevens en een vaste einddatum waarop de gegevens worden verwijderd. Het verwijderen wordt vastgelegd. [8.33.01]

## 4. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| [[lijneigenaar veilige ontwikkeling: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd IT of informatievoorziening]] | Uitvoering van dit beleid en de eisen in inkoop en ontwikkeling |
| Architect | Opstellen en bijhouden van de architectuurprincipes, toets op ontwerpen |
| Systeemeigenaar | Beveiligingseisen per toepassing, acceptatie van opleveringen en van afwijkingen |
| Privacy officer of FG | Advies bij testen met persoonsgegevens en bij privacy by design |
| CISO | Advies, toetsing van dit beleid en van afwijkingen |
| Leveranciers en ontwikkelaars | Bouwen volgens de eisen en het aanleveren van bewijs |

## 5. Naleving en bewaking

- Bij elke oplevering of release: controle van de bewijzen (testverslag, pentest, codeanalyse of
  leveranciersverklaring); bewijs is het acceptatiedossier.
- Jaarlijks: herziening van de architectuurprincipes; bewijs is de vastgestelde versie.
- Jaarlijks: steekproef op testomgevingen met persoonsgegevens, met het formulier, het advies en de
  verwijdering.
- Afwijkingen gaan als bevinding naar het risicoregister van de organisatie.

## 6. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid
informatiebeveiliging in projecten, het beleid wijzigingsbeheer (testen, acceptatie en scheiding van
omgevingen), het beleid leveranciersbeheer (eisen in inkoop en contract), het beleid
vulnerability- en patchmanagement en het privacybeleid (privacy by design en testen met persoonsgegevens).
