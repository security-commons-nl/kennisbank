# Beleid webapplicaties

### Relevante beleidsdocumenten

- Strategisch Informatiebeveiligingsbeleid

- Beleid leveranciersrelaties

- OWASP top 10

## Webapplicaties

### Webapplicaties

Het gebruik van webapplicaties neemt sterk toe binnen gemeenten. Dat betekent dat applicaties en systemen niet langer beheerd worden in het eigen datacenter van de gemeente. De applicatie draait op een webserver bij een leverancier en wordt door de gebruikers benaderd via een webbrowser. Voorbeelden van webapplicaties zijn: internetsites, extranetten, intranetten, software-as-a-service (SaaS)-applicaties, webservices en web-api’s.

De gemeenten ontwikkelen zelf geen webapplicaties, maar moeten wel eisen stellen aan de partijen die deze ontwikkelen (SaaS-leveranciers). Zo moet voor alle applicaties de beveiligingslevenscyclus worden gevolgd, waarbij kwetsbaarheden worden voorkomen, gedetecteerd en gecorrigeerd.

### Sessies

Een belangrijk element van een webapplicatie is de gebruikerssessie (in het Engels session genoemd). Een gebruikersessie zorgt ervoor dat de verschillende scripts van een applicatie weten welke gebruiker het script aanroept. Een webbrowser ontvangt bij het opvragen van het eerste script van een applicatie een speciaal cookie, het session cookie, dat een unieke waarde bevat. Een browser stuurt deze cookie bij elke volgende aanvraag in de webapplicatie mee als header. Op een webserver kan op basis van de unieke waarde van deze cookie, worden bijgehouden of bijvoorbeeld de zender is aangemeld, en zo ja welke gebruiker het is. Dit voorkomt dat gebruikers op elke pagina opnieuw moeten aanmelden. Een webapplicatie kan op basis van de waarde van de session variables een verschillende inhoud aan pagina's geven.

### Kwetsbaarheden

Webapplicaties kunnen kwetsbaarheden bevatten die door hackers kunnen worden misbruikt. Daarom is het belangrijk om aan de ontwikkeling en het beheer van webapplicaties beveiligingseisen te stellen. De beveiligingseisen gesteld aan webapplicaties zijn voornamelijk gebaseerd op de OWASP (Open Web Application Project) Web Application Security Risico’s, deze zijn o.a.:

- Niet-gevalideerde input

- Fouten in de toegangscontrole

- Fouten met authenticatie en in sessiemanagement

- Cross-site Scripting (XSS)

- Bufferoverloop

- SQL-injectie

- Onjuiste foutafhandeling

- Onvoldoende beschermde opslag

- Denial of Service

- Fouten in configuratiebeheer

### Doelstelling

Dit beleid geeft een overzicht van beveiligingsmaatregelen. Deze hebben niet alleen betrekking op de webapplicatie, maar ook op de beheeromgeving en de omringende hard- en softwareomgeving die noodzakelijk is om de webapplicatie te laten functioneren

## Beveiligingseisen webapplicaties

| # | Onderwerp | Beschrijving |
|---|---|---|
| 1 | Gebruikte domeinen moeten voldoen aan DNSSEC | DNSSEC voorziet DNS records van een digitale handtekening om DNS spoofing te voorkomen. |
| 2 | Sterke verificatie- en sessiebeheercontroles | Er moeten sterke verificatie- en sessiebeheer besturingselementen worden gebruikt die voldoen aan het beleid voor Logische toegangsbeveiliging en het wachtwoordbeleid. |
| 3 | Gebruik sterke sessietokens en bescherm deze | Sessietokens mogen niet voorspelbaar en kwetsbaar zijn voor brute force aanvallen: De sessie-ID moet een id aan de clientzijde zijn en de waarde ervan mag nooit gevoelige informatie (of persoonlijk identificeerbare informatie) bevatten. De contexten die aan een sessie-id zijn gekoppeld, moeten aan de serverzijde worden opgeslagen. Sessietokens mogen niet via andere kanalen worden blootgesteld. Sessie-id's moeten een entropie van ten minste 112-bits hebben en de waarde moet worden afgeleid van een cryptografisch beveiligde willekeurige nummergenerator. Sessie-ID's moeten een geschikte geldigheidsperiode hebben. Sessie-ID's moeten na het inloggen worden vervangen en verwijderd met een time-out aan de serverzijde. Alle bestaande sessietokens/actieve sessies moeten onmiddellijk verlopen zodra inloggegevens met succes zijn gewijzigd, zodat bestaande sessies op andere apparaten/apps/etc. (op basis van de oude accountinformatie) niet geldig blijven tot de normale verlooptijd van de sessie. |
| 4 | Indirecte objectverwijzingen per gebruiker of sessie | Directe objectverwijzingen moeten indien mogelijk worden vermeden. Per gebruiker of sessie moeten indirecte objectverwijzingen worden gebruikt. De toepassing moet de indirecte objectverwijzing per gebruiker toewijzen aan de werkelijke databasesleutel, het bestand of een ander object op de server. |
| 5 | Sessie time-out | Wanneer een gebruiker gedurende een bepaald interval (gedefinieerd door de webserver) geen actie op een website uitvoert, moet de status van de gebruikerssessie aan de serverzijde worden gewijzigd in "niet meer gebruikt" en de webserver instrueren om de gebruikerssessie te vernietigen (alle gegevens die erin zijn opgenomen te verwijderen).  Stel de sessietime-out in op de minimaal mogelijke waarde, afhankelijk van de context van de toepassing. Vermijd een "oneindige" sessietime-out. De sessiecookie moet verlopen wanneer de browser wordt gesloten. |
| 6 | Sessiebeheer | Elke implementatie die sessiebeheer toepast, moet voldoen aan de volgende verklaringen:  Sessiebeheer moet correct worden afgehandeld en beveiligde protocollen gebruiken, die na de eerste verificatie worden voortgezet. Gebruik onvoorspelbare sessie-id's. Sessies moeten ongeldig worden gemaakt bij het uitloggen. Sessiebeheer moet worden beheerd/beheerd aan de serverzijde en moet ongeldigheid aan de serverzijde toestaan in geval van schending/misbruik van sessies. |
| 7 | Toegang controleren bij het gebruik van Directe objectverwijzingen | Elk gebruik van een directe objectreferentie van een niet-vertrouwde bron moet een toegangscontrolecontrole omvatten om ervoor te zorgen dat de gebruiker is geautoriseerd voor het gevraagde object. |
| 8 | Voorkomen van Cross-Site Request Forgery (CSRF) | CSRF-tokens moeten (redelijk) bestand zijn tegen brute-force-aanvallen. Een onvoorspelbaar token moet worden opgenomen in het serverantwoord, bij voorkeur in een verborgen veld in de hoofdtekst van het formulier. Dit token moet worden geretourneerd door de client en gevalideerd door de server. Dergelijke tokens moeten minimaal uniek zijn per gebruikerssessie, maar kunnen ook uniek zijn per aanvraag. |
| 9 | Updaten en patchen van de (web)applicatie | Alle broncode, inclusief bibliotheken die worden gebruikt voor het genereren van de (web)applicatie, moet worden onderhouden en gepatcht voor kwetsbaarheden en stabiliteitsproblemen. Toepassing (code) die in productie gaat, moet worden getest op beveiliging via codebeoordelingen of penetratietests. |
| 10 | Applicatie security architectuur | Shared hosting of virtuele hosting mag niet worden gebruikt zonder scheiding op alle lagen van de applicatie, inclusief het platform waarop de applicatie actief is, het framework, applicatie specifieke code en de database. |
| 11 | Authenticatie | De informatie die een gebruiker verstrekt bij het inloggen moet de applicatie in staat stellen om te verifiëren of het digitale profiel van een gebruiker overeenkomt met de 'echte' natuurlijke persoon achter het apparaat.  Webapplicaties worden ontsloten met SSO (Single Sign On) en wanneer dit niet mogelijk is met MFA. |
| 12 | Verificatie en autorisatie voor elke pagina, API en gegevens | Het afdwingingsmechanisme moet standaard alle toegang weigeren en expliciete toekenningen aan specifieke gebruikers en rollen vereisen voor toegang tot elke pagina, API en gegevens. |
| 13 | Pagina autorisatie in een workflow | Als de pagina betrokken is bij een workflow, moet worden gecontroleerd of de omstandigheden in de juiste staat zijn om toegang toe te staan. |
| 14 | Transport Layer Protection met TLS | Alle pagina's met gevoelige gegevens moeten TLS gebruiken. Ook moet de locatie waarnaar gevoelige gegevens worden gepost TLS gebruiken zonder omleiding van een niet-TLS-doel. |
| 15 | Transport Layer Protection: vertrouwelijke cookies | De vlag HttpOnly en Secure moet worden ingesteld op vertrouwelijke cookies. Stel het kenmerk expires, max-age, domain, path en samesite zo strikt mogelijk in. |
| 16 | Alle certificaten moeten geldig zijn | Alle certificaten moeten geldig zijn volgens internationale normen, waaronder:  ondertekend door een vertrouwde uitgever met een actief beleid geldig in de tijd niet herroepen overeenkomen met het activum of de persoon aan wie het is uitgegeven. |
| 17 | Verbindingen met de backend en andere verbindingen | Backend en andere verbindingen die zijn opgezet via een kanaal dat wordt beheerd door een derde partij, moeten ook TLS of andere coderingstechnologieën gebruiken. |
| 18 | Behoud van de integriteit van de verwerkte informatie | De integriteit van de door toepassingen verwerkte informatie moet worden gehandhaafd door ervoor te zorgen dat:  informatie wordt niet beschadigd wanneer deze door meer dan één gebruiker wordt gewijzigd; informatie kan niet per ongeluk worden overschreven; ongeautoriseerde of onjuiste wijzigingen in informatie worden gedetecteerd. |
| 19 | Voorkomen van onjuiste invoer van informatie | Onjuiste invoer van informatie moet worden voorkomen door: Alleen gegevens accepteren uit vertrouwde en geverifieerde informatiebronnen voor gegevenswijzigingen (maken, wijzigen, verwijderen) Nieuwe records hebben initialisatiewaarden Foutmeldingen gebruiken |
| 20 | Brute-Force protection | Internet-facing applicaties moeten hun (gebruikers)accounts beschermen tegen brute-force aanvallen. Er moet een proces zijn om misbruik op te sporen en er moet een proces zijn om op het misbruik te reageren.  Mogelijke acties: Detecteer (snelle) geautomatiseerde inlogpogingen en reageer door het IP-adres tijdelijk te blokkeren. Rapporteer aan SOC. Na detectie: forceer het account om in te loggen met een tweede factor. Deze optie veronderstelt dat er een mogelijkheid is om sms of een andere out-of-band communicatiemethode te gebruiken. Rapporteer aan SOC. |
| 21 | HTTP Strict Transport Security (HSTS) inschakelen | De HTTP Strict Transport Security-antwoordheader moet worden ingesteld om HTTPS af te dwingen.  Zorg ervoor dat alle subdomeinen HTTPS gebruiken voordat u subdomeinen opneemt in de HTTP Strict Transport Security-antwoordheader. |
| 22 | Inventarisatie van de gebruiker (Enumeration) | Gebruikersinventarisatie is niet beperkt tot gebruikersnaam van een account. Alle identificeerbare eigendommen van een account kunnen worden gebruikt voor gebruikersinventarisatie.  Mogelijke uitzondering: interfaces die opzettelijk zijn ontwikkeld om gebruikers, accounts of identificeerbare objecten te vermelden, zijn toegestaan. |
| 23 | Opslag van beveiligingsgerelateerde gegevens | Gegevens die een specifieke beveiligingswaarde hebben, zoals wachtwoorden, sleutels en inlogtokens, moeten worden opgeslagen met behulp van de beveiligde opslagfaciliteiten van het platform voor beveiligingsgerelateerde gegevens. |
| 24 | Certificaat vastzetten en wederzijdse verificatie | Het vastzetten van certificaten mag niet worden gebruikt en verwijderd wanneer dit wordt geïmplementeerd. Pas cryptografische standaarden toe voor veilige gegevensoverdracht en implementeer CAA-records |
| 25 | Gebruikersverificatie door de backend | Als gebruiker specifieke gegevens worden verkregen van de back-endserver, de app de gebruikersreferenties doorgeeft aan de back-endserver, moeten alle verificatieaanvragen server-side worden uitgevoerd. Dit zorgt ervoor dat toepassingsgegevens alleen beschikbaar zijn na succesvolle verificatie. |
| 26 | Gebruikersverificatie door de app | Als gebruiker specifieke gegevens worden verkregen van de back-endserver en/of worden opgeslagen in de app-gegevens, moet de gebruiker zich bij de app verifiëren. Het is niet voldoende om alleen te vertrouwen op apparaat verificatie. |
| 27 | Gegevensinvoer uit andere bronnen | Gegevensinvoer via alternatieve bronnen die rechtstreeks in de app worden geladen, is verboden. Dit mag alleen gebeuren via de expliciet opgegeven backend server. |
| 28 | Inhoud ophalen van externe locaties | Als inhoud wordt opgehaald van externe locaties (via internet), communiceer dan altijd via HTTPS, zelfs als de inhoud geen persoonlijke / gevoelige informatie bevat. |
| 29 | Bestanden uploaden | De uploadfunctionaliteit van een toepassing of systeem moet worden aangescherpt om de uitvoering van code of een denial-of-service-situatie te voorkomen. |
| 30 | Beveiliging van transportlagen | De hoogst beschikbare TLS-versie moet zijn ingeschakeld.  Bescherming tegen downgrade-aanvallen moet worden geactiveerd. TLSv1.3 moet zijn ingeschakeld, indien beschikbaar. Schakel 0-RTT uit in TLSv1.3 om herhalingsaanvallen te voorkomen. TLSv1.2 moet worden ingeschakeld en gebruikt. |
| 31 | Gevoelige gegevens in URL of GET-verzoek | Persoonlijk identificeerbare informatie, tokens en wachtwoorden mogen niet zichtbaar zijn in de URL of parameters van een GET-verzoek. Eventuele bijbehorende referenties moeten in de koptekst of gegevensvelden worden geplaatst |
| 32 | Referer header | Wanneer een toepassing naar een toepassing van derden linkt, moet het lekken van gevoelige informatie worden voorkomen. Voor relevante pagina's moet de webtoepassing het juiste referrer-beleid in de koptekst opnemen. |
| 33 | CSP (Content Security Policy) toepassen | Een webtoepassing moet voor elk object een inhoudsbeveiligingsbeleid (CSP) definiëren. De webserver moet worden geconfigureerd om de CSP te leveren. Het http-antwoordheaderveld Inhoudsbeveiligingsbeleid is het voorkeursmechanisme voor het leveren van een beleid van een server aan een client. Als alternatief kan de CSP in een element worden gedefinieerd. |
| 34 | Voorkom path traversal | Voorkom path traversal, of directory traversal, aanvallen.  Zorg ervoor dat gebruikersinvoer wordt beperkt en opgeschoond en voorzie dat u niet met gebruikersinvoer werkt bij het gebruik van bestandssysteemaanroepen. |
| 35 | Website, API en portal registratie | Websites, API's en portals moeten als asset worden geregistreerd in de juiste CMDB. |
| 36 | Veilige protocolcombinaties | Wanneer een protocol is samengesteld uit andere protocollen en de onderliggende protocolset een onveilig protocol bevat (bijvoorbeeld HTTP), moet de gecombineerde beveiliging en integriteit worden beschouwd, inclusief de integriteitsgaranties van de payload.  Als de lading die over het onveilige kanaal wordt verzonden zijn eigen integriteitsgaranties heeft, kan dit als een veilig transport worden beschouwd. Wanneer de integriteit op dit niveau niet kan worden gegarandeerd, wordt verkeer genegeerd of omgeleid naar het beveiligde protocolkanaal. Wanneer het protocol voldoet aan deze manier van werken kan het beschouwd worden als een veilig protocol. |
| 37 | Systemen moeten voorkomen dat gegevens als logica worden verwerkt | Systemen moeten voorkomen dat gegevens als logica worden verwerkt om te voorkomen dat hun eigen functionaliteit, evenals die van andere systemen waarmee ze communiceren, in afwijking van het beoogde ontwerp wordt gewijzigd. |
| 38 | Beveiligingstests voor SaaS-services | Voor internetgerichte producten en diensten die worden geleverd is het uitvoeren van een penetratietest vereist voor in gebruik name.  De volgende beoordelingen moeten worden uitgevoerd en bewijs moet worden geleverd door de SaaS-provider voor het geval het niet mogelijk is om een pentest uit te voeren:  SaaS-providers moeten regelmatig intern applicatie-, netwerk- en infrastructuurbeveiligingstests uitvoeren op zijn cloudinfrastructuur en de bevindingen dienovereenkomstig aanpakken. SaaS-provider moet minimaal één keer per jaar een penetratietest uitvoeren door een geloofwaardige externe partij en de resultaten, gerapporteerde bevindingen, resoluties en tijdlijnen delen. De omvang van de uitgevoerde penetratietest moet dezelfde zijn als de omvang van de aan gemeenten geleverde dienst. |
| 39 | Responsible Disclosure | Een verwijzing naar de pagina met responsible Disclosure moet op de bedrijfswebsite worden opgenomen. Deze verwijzing mag niet meer dan één klik verwijderd zijn van de hoofdpagina. |

## SaaS-Leveranciers

Aanvullend aan de beveiligingseisen aan webapplicaties worden er ook specifieke eisen gesteld aan de SaaS-leverancier. Deze eisen zijn aanvullende op de eisen benoemt in het beleid leveranciersrelaties:

| # | Onderwerp | Beschrijving |
|---|---|---|
| 40 | Vulnerability management in de cloud | De Cloud serviceprovider moet beleid en procedures vaststellen en ondersteunende bedrijfsprocessen en technische maatregelen implementeren voor de tijdige detectie van beveiligingskwetsbaarheden van de (beheerde) applicaties, infrastructuurnetwerk- en systeemcomponenten van het bedrijf. Kwetsbaarheidsscans moeten regelmatig worden uitgevoerd volgens de huidige en up-to-date industrienormen, best practices en wettelijke verplichtingen. |
| 41 | Beoordeling van SaaS-serviceproviders | De SaaS-provider moet in staat zijn om informatie, technische en functionele documentatie, certificeringen, pentestrapporten en/of auditrapporten te verstrekken om de gemeenten een adequate beveiligingsbeoordeling te laten uitvoeren op hun beveiligingshouding, beleid, processen, procedures en implementaties. |
| 42 | Bewijs van een analyse door de leverancier | Leverancier dient aan te tonen dat een zorgvuldige analyse van haar beheersmaatregelen/architectuur/processen is uitgevoerd om te voldoen aan geldende normenkaders en toepasselijke wet- en regelgeving. |
| 43 | Gegevenscategorisatie van Cloud serviceproviders voor tenant | De cloud serviceprovider moet een identiteits- en toegangsbeheersysteem hebben dat gegevens voor zijn tenant categoriseert om rol- en contextafhankelijke gegevens en functionele toegangsrechten mogelijk te maken. |
| 44 | Interne verificatie van Cloud serviceproviders | Het interne authenticatie- en wachtwoordbeleid voor het beheer en de ontwikkeling van het systeem of de applicatie dat door de clou service provider wordt verstrekt, moet op controleerbare wijze voldoen aan de BIO |
| 45 | SaaS-service Multi Factor Authentication | SaaS-applicaties worden ontsloten met SSO (Single Sign On), wanneer dit mogelijk is, is MFA verplicht. |
| 46 | Vereisten voor niet-productieplatforms (OTA) | Alle platformen voor ontwikkeling, testen en acceptatie ('OTA' in OTAP) van software of hardware moeten logisch gescheiden zijn van elkaar en van de productieomgeving voor data, functionaliteit, processen en rollen. Logische verdeling en scheiding moeten ook worden toegepast in het geval van meerdere huurders op het platform. De acceptatieomgeving moet qua architectuur en opzet lijken op het productieplatform. Tests moeten worden uitgevoerd op een testplatform. Het gebruik van gevoelige informatie (bijv. privacy, zakelijke verplichtingen) in een ontwikkel- en testomgeving is uitdrukkelijk verboden. |
| 47 | Afzonderlijke gebruikerstoegang in omgevingen met meerdere tenants | Multi-tenant applicaties en infrastructuursysteem- en netwerkcomponenten moeten zodanig worden ontworpen, ontwikkeld, geïmplementeerd en geconfigureerd dat gebruikerstoegang wordt gescheiden van andere tenants (klanten), op basis van de volgende overwegingen: Vastgesteld beleid en procedures; Isolatie van bedrijf kritische middelen en/of gevoelige gebruikersgegevens en sessies die sterkere interne controles en een hogere mate van zekerheid vereisen; Naleving van wettelijke verplichtingen. |
| 48 | Ongebruikte accounts | Wanneer een gebruikersaccount niet langer nodig is, moet deze worden verwijderd of uitgeschakeld. |
| 49 | Standaardaccounts | Standaardaccounts moeten zijn uitgeschakeld. Als het gebruik ervan noodzakelijk is, moeten aanvullende maatregelen worden genomen om misbruik van deze accounts te voorkomen en moeten de accounts worden toegewezen aan een manager die verantwoordelijk is voor gebruik en autorisatie. |
| 50 | Beheer op afstand | Extra toegangscontroles, bovenop sterke authenticatie (MFA), moeten aanwezig zijn voor iedereen, inclusief ICT-personeel, die externe toegang nodig heeft om onderhoud en configuratiebeheer van een systeem of applicatie uit te voeren. Er moeten technische en operationele maatregelen worden genomen om dit te verifiëren en te handhaven. |
| 51 | Bescherming van infrastructuurinformatie | De toegang tot broncode en bijbehorende items moet worden gecontroleerd om de introductie van ongeautoriseerde functionaliteit en onbedoelde wijzigingen te voorkomen. |
| 52 | Bevoegdheden van SaaS-serviceoplossingen | De geboden oplossing moet worden geïmplementeerd volgens het principe van de minste bevoegdheid voor alle componenten die bij de werking ervan worden gebruikt. |
| 53 | SaaS-servicebescherming | Systemen die worden gebruikt om een internetservice aan te bieden, moeten zijn uitgerust met aanvullende beschermingsmechanismen (bijvoorbeeld EPP, antivirus, antimalware, WAF, IDS, enz.). SaaS-provider moet de werking van deze mechanismen kunnen aantonen. |
| 54 | Update detectiesystemen door leverancier | De leverancier moet ervoor zorgen dat systemen die handtekeningen, lijsten of bepaalde gedragspatronen gebruiken om beveiligingsrisico's te detecteren, regelmatig worden bijgewerkt in alle infrastructuurcomponenten binnen een industriestandaard tijdsbestek. |
| 55 | Blokkeer malware door leverancier | Leverancier moet technische maatregelen hebben geïmplementeerd om te voorkomen dat malware wordt uitgevoerd op eigen endpoint-apparaten en netwerk- en systeemcomponenten van de IT-infrastructuur. |
| 56 | Database auditing | Toegang tot de gegevens die in een database zijn opgeslagen, moet controleerbaar zijn via voldoende logboekregistratie. |
| 57 | Business Continuity Management | Leverancier moet Business Continuity hebben geïmplementeerd voor het waarborgen van de overeengekomen continuïteit en serviceniveaus aan klanten in geval van verstorende incidenten. Het ontwerp en de implementatie van technische diensten en platforms moeten zorgen voor het vereiste niveau van beschikbaarheid (RTO) en de maximale periode van gegevensverlies (RPO) tijdens afzonderlijke storingen. Er vindt periodiek overleg plaats met de leverancier en er wordt op toegezien dat de leverancier de overeengekomen eisen nastreeft. |
