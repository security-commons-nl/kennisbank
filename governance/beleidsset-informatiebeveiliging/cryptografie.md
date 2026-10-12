# Beleid cryptografie

### Afkortingen

| Afkorting | Omschrijving |
|---|---|
| CISO | Chief Information Security Officer |
| PKI | Public Key Infrastructure |
| CAR/UWO | Collectieve Arbeidsvoorwaardenregeling en Uitwerkingsovereenkomst |
| BIO | Basisnormenkader Informatiebeveiliging Overheid |
| IBD | Informatiebeveiligingsdienst voor gemeenten |
| CA | Certificaatautoriteit |
| HTTPS | Hyper Text Transfer Protocol Secure |
| HSTS | HTTP Strict Transport Security |
| DKIM | DomainKeys Identified Mail |
| DMARC | Domain-based Messagee Authentication, Reporting and Conformance |
| DNSSEC | Domain Name System Security Extension |
| DANE | DNS-based Authentication of Named Entities |
| STARTTLS | Start Transport Layer Security |
| BYOD | Bring Your Own Device |
| TLS | Transport Layer Security |
| WEH | Wet Elektronische Handtekening |
| CRL | Certificate Revocation List |
| OCSP | Online Certificate Status Protocol |
| RACI | Responsible, Accountable, Consulted, Informed |

### Relevante beleidsdocumenten

- Beleid Data Classificatie

- Beleid Beheer van Bedrijfsmiddelen

## Inleiding

### 1.1 Doel

Dit document beschrijft het beleid van de organisatie met betrekking tot Cryptografie (encryptie en Public Key Infrastructure). Het beleid omvat gedragsregels en implementatie van technieken om de vertrouwelijkheid, integriteit, onweerlegbaarheid en authenticatie van digitale informatie te waarborgen.

### 1.2 Verantwoordelijkheid

Het IT-team is verantwoordelijk voor de implementatie en handhaving van dit cryptografie beleid.

De Chief Information Security Officer (CISO) houdt toezicht op de naleving van het beleid en zorgt voor regelmatige evaluaties.

### 1.3 Toepassingsgebied van het document

- Dit beleid is van toepassing op alle systemen, applicaties en gegevens die onder de verantwoordelijkheid van de organisatie vallen.

- Dit beleid is van groot belang voor een veilige informatiecultuur en is onderhevig aan regelmatige evaluatie en aanpassing om te blijven voldoen aan de veranderende dreigingslandschappen en normen op het gebied van informatiebeveiliging.

## Beleidsvereisten Cryptografie

Het Cryptografie Beleid van de organisatie hanteert de volgende uitgangspunten, ontleend aan de BIO, Handreiking Encryptiebeleid van de IBD, met integratie van aanvullende regels:

### 2.1 Gebruiksvoorwaarden voor versleuteling van gegevens

De organisatie dient gebruiksvoorwaarden waarin aanwijzingen staan over hoe omgegaan dient te worden met de private sleutel, het versleutelen van gegevens, de applicaties voor versleuteling en hoe adequaat gereageerd dient te worden op incidenten, op te stellen.

#### 2.1.1 Regels voor acceptabel gebruik

- Alle medewerkers van de organisatie dienen regels voor acceptabel gebruik te accepteren en ondertekenen. Hierin wordt aandacht besteed aan het proces bij verlies, diefstal of compromittering van de private sleutel, waarbij meldingen binnen 4 uur moeten plaatsvinden.

- Niet voldoen aan beleid en regels kan resulteren in een disciplinair proces volgens de CAR/UWO.

- Medewerkers dienen zich te houden aan ICT-standaarden en nader gemaakte afspraken.

#### 2.1.2 Regels voor versleuteling van informatie

De organisatie heeft regels schreven voor het versleutelen van informatie, waarbij aandacht wordt besteed aan de impliciete toestemming aan gebruikers over welke informatie zij wel of niet mogen inzien tijdens het telewerken. Medewerkers dienen zich ervan bewust te zijn dat zij achteraf ter verantwoording geroepen kunnen worden.

### 2.2 Classificatieniveaus en versleuteling

De organisatie hanteert classificatieregels voor gemeentelijke gegevens en andere gegevens onder haar beheer en zorgt voor passende maatregelen om deze gegevens te beschermen

De organisatie dient duidelijk te hebben van welke gegevens de beschikbaarheid, vertrouwelijkheid en integriteit gegarandeerd dienen te worden. Tevens dient duidelijk te zijn hoe dit wordt gegarandeerd. Denk hierbij aan de volgende maatregelen:

- Er is een overzicht van gegevens waarin is aangegeven op welke wijze deze versleuteld dienen te worden. Dit betreft de gegevenseigenaar, de te volgen procedure en de beschikbare hulpmiddelen om de versleuteling uit te voeren.

- Er zijn procedures voor gebruikers, voor het versleutelen van gegevens.

Alle gegevens anders dan met classificatie ‘geen’, worden versleuteld conform beveiligingseisen in de gemeentelijke informatiebeveiligingsarchitectuur:

- Classificatieniveau ‘laag’: transportbeveiliging buiten het interne netwerk

- Classificatieniveau ‘midden’: transportbeveiliging

- Classificatieniveau ‘hoog’: transport en berichtbeveiliging

#### 2.2.1 Versleuteling van gegevens

De organisatie dient een basis aan cryptografische maatregelen te implementeren om te voldoen aan regelgeving. Denk hierbij aan transportbeveiliging buiten het interne netwerk. Als de organisatie informatie verwerkt met een hoger vertrouwelijkheidsniveau (gemeentelijk) dan ‘vertrouwelijk’, zullen mogelijk aanvullende maatregelen geïmplementeerd moeten worden. Deze aanvullende maatregelen dienen gebaseerd te zijn op de resultaten van een risicoanalyse die de organisatie heeft uitvoert. Hieronder wordt aangegeven welk beveiligingsaspect wordt ondersteund door welke cryptografische techniek.

• Integriteit: encryptie (hashing)

• Vertrouwelijkheid: encryptie

• Onweerlegbaarheid: digitale handtekening

• Authenticatie: digitale handtekening

De sterkte van de cryptografie wordt waar mogelijk gebaseerd op de actuele adviezen van het NCSC.

##### 2.2.1.1 Versleuteling van gegevens tijdens transport

Versleuteling vindt plaats conform ‘best practices’ (de stand der techniek), waarbij geldt dat de vereiste encryptie sterker is naarmate gegevens gevoeliger zijn. Hiervoor wordt gebruik gemaakt van het Forum standaardisatie op basis van pas toe of leg uit. Onderstaand de standaarden voor encryptie die vanuit het Forum verplicht zijn en binnen de organisatie minstens worden toegepast.

- Om webverkeer te versleutelen: HTTPS en HSTS moeten worden toegepast op de communicatie tussen klanten (zoals webbrowsers) en servers voor alle websites en webservices.

- DKIM (DomainKeys Identified Mail) moet worden toegepast op alle overheidsdomeinnamen waarvandaan wordt gemaild én op alle mailservers waarmee de overheid e-mail verstuurt en ontvangt.

- DMARC (Domain-based Messagee Authentication, Reporting and Conformance) moet worden toegepast op alle overheidsdomeinnamen, ook op domeinen waarvan niet wordt gemaild, én op alle mailservers waarmee de overheid e-mail ontvangt.

- DNSSEC (Domain Name System Security Extension) moet worden toegepast op alle overheidsdomeinnamen én op DNS-resolvers die clients van overheidsorganisaties direct of indirect van DNS-antwoorden voorzien.

- TLS (transport Layer Secuity) moet worden toegepast op de uitwisseling van gegevens tussen clients en servers, inclusief machine-to-machine communicatie.

- STARTTLS en DANE moeten in combinatie worden toegepast op ontvangende en verzendende e-mailservers.

- Om vertrouwelijke en geheime informatie te beschermen is het niet toegestaan om dit type informatie te delen via voorzieningen als webmail, als ook sociale netwerken en clouddiensten (Dropbox, Gmail, et cetera.). Dit vanwege het lage beschermingsniveau, veelal alleen naam en wachtwoord, en het ontbreken van versleuteling.

##### 2.2.1.2 Versleuteling van opgeslagen gegevens

- Gevoelige gegevens die worden opgeslagen in databases, repositories of andere opslagmedia dienen te worden versleuteld.

- Versleutel opgeslagen back-ups van cruciale gegevens. Zorg ervoor dat de versleutelingssleutels veilig worden beheerd en dat herstelprocedures getest zijn om de beschikbaarheid van gegevens te waarborgen, zelfs na een incident.

- Om een correcte en veilige bediening van mobiele (privé-)apparatuur en thuiswerkplek te waarborgen, is de gemeente bevoegd om beveiligingsinstellingen af te dwingen. Dit heeft betrekking op zowel door de gemeente verstrekte middelen, als privé-apparatuur ('bring your own device' (BYOD)). Dit betreft onder meer versleuteling.

### 2.3 Certificaatbeheer

Een strikt certificaatbeheer wordt gehandhaafd conform de BIO en IBD-richtlijnen om de veiligheid van de certificaten te waarborgen. Er zijn (contractuele) afspraken over reservecertificaten van een alternatieve leverancier als uit risicoafweging blijkt dat deze noodzakelijk zijn.

Binnen de organisatie worden er drie soorten certificaten uitgegeven:

- Externe certificaten: worden gebruikt om de beveiliging van communicatie op internet te waarborgen. Deze certificaten worden uitgegeven door een certificaatautoriteit (CA) en worden toegepast op websites, servers en applicaties om een veilige en versleutelde verbinding tot stand te brengen.

- PKI Overheidscertificaten: verwijzen naar digitale certificaten die gebruikt worden door overheidsinstanties en die worden uitgegeven onder toezicht van Logius, een initiatief van de Nederlandse overheid. Deze certificaten spelen een cruciale rol bij het waarborgen van de beveiliging en betrouwbaarheid van digitale communicatie en transacties in overheidsinstellingen. Deze certificaten worden door een certificaatleverancier aan de organisatie uitgegeven.

- Interne certificaten: worden uitgegeven door de hostingpartij voor intern gebruik. In tegenstelling tot externe certificaten, die worden verstrekt door openbare certificaatautoriteiten (CA's) en wereldwijd worden vertrouwd, zijn interne certificaten bedoeld voor beveiligingsdoeleinden binnen de infrastructuur van de organisatie

In geval van PKIoverheid-certificaten hanteer de PKIoverheid-eisen ten aanzien van het sleutelbeheer. In overige situaties hanteer de norm ISO 11770-1 voor het beheer van cryptografische sleutels.

Onder Certificaatbeheer binnen de organisatie worden de volgende activiteiten verstaan:

#### 2.3.1 Bepalen van de levensduur van de certificaten

Het bepalen van de levensduur van certificaten is uitbesteed aan de certificaatbeheerders. Deze beheerders dienen:

- Van alle certificaten bij te houden, wanneer ze zijn uitgegeven en wanneer deze weer verlopen.

- Een procedure op te stellen over hoe op de certificaateigenaren op de hoogte worden gebracht van het feit dat de publieke sleutel is geverifieerd door de certificaatbeheerder.

#### 2.3.2 Genereren (en registeren) van certificaten

De Wet Elektronische Handtekening (WEH) stelt eisen aan de manier waarop certificaten die gebruikt worden voor digitale handtekeningen gegenereerd worden.

De organisatie en daarmee de certificaateigenaren en certificaatbeheerders dienen:

Alle relevante informatie, zoals de cryptografische eigenschappen, het eigenaarschap en de levensfases van certificaten, vast te leggen in een geautomatiseerd registratiesysteem.

De taken, verantwoordelijkheden en bevoegdheden met betrekking tot het aanvragen en generen van certificaten vast te leggen.

De certificaatbeheerder:

- Verzamelt en verifieert de identiteitsgegevens van de aanvrager en autoriseert de aanvraag.

- Fungeert voor certificaataanvragen als Externe Registration Authority (RA). Denk hierbij aan de volgende activiteiten: identificatie, authenticatie en autorisatie van de aanvraag, het bepalen en aanvullen van de juiste inhoud.

Vast te leggen waar beveiligingsincidenten gemeld moeten worden, wie een certificaat mag intrekken, hoe dat gecommuniceerd dient te worden, welke stappen verder moeten worden genomen en welke ingetrokken certificaten op een ‘revocation list’ komen.

#### 2.3.3 Distribueren van de certificaten

Het distribueren van de certificaten dient op een veilige en gecontroleerde wijze te gebeuren.

- De organisatie en daarmee de certificaateigenaren en externe certificaatbeheerders dienen:

- Alle uitgegegeven certificaten worden bijgehouden en bij verdenking van compromittering kan de beheerder het certificaat intrekken en ongeldig maken.

#### 2.3.4 Vervangen (en updaten) van de certificaten

Het vervangen van certificaten is noodzakelijk op het moment dat de gebruiker zijn wachtwoord is vergeten, waarmee de private sleutel is beveiligd of het opslagmedium defect of gestolen is. Een andere reden kan zijn dat een certificaat met een vermelde geldigheidsduur verlopen is.

- De organisatie en daarmee de certificaatbeheerders dienen:

Vast te leggen in welke specifieke gevallen het herstellen van sleutels toegepast mag worden, voor welk type sleutels, welke methode/oplossing wordt geïmplementeerd, wie een aanvraag mag indienen en wie de herstelprocedure mag uitvoeren.

#### 2.3.5 Intrekken van de certificaten

- Certificaatbeheerders hebben als enige de mogelijkheid hebben om certificaten in te trekken (revocation). Het intrekken van certificaten heeft alleen zin op het moment dat de geldigheidsduur van het certificaat nog niet is verlopen.

- De organisatie en daarmee de certificaatbeheerders dienen:

Vast te leggen in welke specifieke gevallen het intrekken van certificaten wordt toegepast, wie een aanvraag mag indienen, wie de procedure mag uitvoeren en via welke methode het overzicht van ingetrokken certificaten wordt gepubliceerd (Certificate Revocation List (CRL) en/of Online Certificate Status Protocol (OCSP)).

### 2.4 PKIoverheid

- Op het moment dat de gemeente gebruik gaat maken van PKIoverheid certificaten, dient de gemeente zorg te dragen dat:

Geen enkele andere persoon, dan de certificaathouder, toegang zal hebben tot de private sleutel die is gekoppeld aan de publieke sleutel in het PKIoverheid certificaat.

De toegangscodes van smartcards en/of USB-tokens,waarin de private sleutel is opgeslagen, steeds veilig en gescheiden van de smartcards en/of USB-tokens bewaard zullen worden.

Het PKIoverheid certificaat enkel zal worden gebruikt voor de doelen waartoe deze is uitgereikt.

Direct na ontvangst van het certificaat, maar in ieder geval alvorens over te gaan tot installatie en gebruik, het digitale certificaat op haar volledige en juiste inhoud zal worden gecontroleerd.

Direct tot intrekking van het PKIoverheid certificaat zal worden overgegaan en elk gebruik daarvan direct zal worden gestaakt, wanneer:

- Er onvolledigheden en/of onjuistheden in het PKIoverheid certificaat worden geconstateerd dan wel deze door gewijzigde omstandigheden dreigen te ontstaan of zijn ontstaan

- De private sleutel verloren, gestolen of anderszins gecompromitteerd is geraakt

- Smartcards en/of USB-tokens of de toegangscodes van smartcards en/of USB-tokens in onbevoegde handen zijn gekomen, of kunnen zijn gekomen.

## Evaluatie en Verbetering van het Beleid

Het Beleid Cryptografie wordt jaarlijks geëvalueerd om de doeltreffendheid ervan te waarborgen. Op basis van evaluatieresultaten worden indien nodig verbeteringen aangebracht in het beleid.

## Rollen en verantwoordelijkheden

Dit RACI-diagram biedt een overzicht van de verdeling van verantwoordelijkheden binnen de implementatie en handhaving van het netwerkbeveiligingsbeleid van de organisatie. De matrix identificeert de rollen van verschillende belanghebbenden bij specifieke taken en activiteiten die essentieel zijn voor een effectieve beveiliging van het netwerk. Hieronder wordt de betekenis van de gebruikte afkortingen toegelicht:

- R (Responsible): De persoon of groep die verantwoordelijk is voor de uitvoering van een specifieke taak of activiteit.

- A (Accountable): De individuele persoon die uiteindelijk verantwoordelijk is en beslissingsbevoegdheid heeft voor het betreffende onderdeel.

- C (Consulted): Personen of afdelingen die geraadpleegd moeten worden voor input en feedback bij de uitvoering van taken.

- I (Informed): Personen of afdelingen die op de hoogte moeten worden gehouden van de voortgang en resultaten van specifieke taken.

| Activiteit | R | A | C | I |
|---|---|---|---|---|
| 2.1 Gebruikersvoorwaarden voor versleuteling van gegevens | het securityteam | CISO |  | CIO |
| 2.1.1 Regels voor acceptabel gebruik | het securityteam | CISO |  | CIO |
| 2.1.2 Regels voor versleuteling van informatie | het securityteam | CISO |  | CIO |
| 2.2 Classificatieniveaus en versleuteling | Information Security Officers | Management |  | CISO |
| 2.2.1 Versleuteling van gegevens | Medewerkers | Mangement |  | CISO |
| 2.2.1.1 Versleuteling van Gegevens tijdens transport | Architecten | Management |  | CISO |
| 2.2.1.2 Versleuteling van opgeslagen gegevens | Database beheerders | Management |  | CISO |
| 2.3 Certificaatbeheer | Beheerder certificaat | Certificaat eigenaar |  | CISO |
| 2.3.1 Bepalen van de levensduur van de certificaten | Certificaatleverancier | Certificaat eigenaar |  | CISO |
| 2.3.2 Genereren (en registreren) van certificaten | Certificaatleverancier | Certificaat eigenaar |  | CISO |
| 2.3.3 Distribueren van de certificaten | Certificaatleverancier | Certificaat eigenaar |  | CISO |
| 2.3.4 Vervangen (en updaten) van de seutels | Certificaatleverancier | Certificaat eigenaar |  | CISO |
| 2.3.5 Herstellen van de sleutels | Certificaatleverancier | Certificaat eigenaar |  | CISO |
| 2.3.6 Intrekken van de sleutels | Certificaatleverancier / Certificaat eigenaar | Certificaatleverancier / Certificaat eigenaar |  | CISO |
| 2.3.7 Archiveren van de sleutels | Certificaatleverancier | Certificaat eigenaar |  | CISO |
| 2.3.8 Vernietigen van de sleutels | Certificaatleverancier | Certificaat eigenaar |  | CISO |
| 2.4 PKI Overheid | Certificaatbeheerder | Certificaat eigenaar |  | CISO |
