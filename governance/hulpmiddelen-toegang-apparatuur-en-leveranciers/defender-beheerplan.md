# Beheerplan Microsoft Defender

### Inleiding

Microsoft Defender biedt geavanceerde beveiligingsoplossingen voor organisaties om zich te beschermen tegen cyberdreigingen. Dit beheerplan beschrijft de strategieën, processen en best practices voor het effectief implementeren, configureren en onderhouden van Microsoft Defender binnen onze IT-omgeving. Het doel is om een robuuste beveiligingsstructuur te waarborgen die proactieve detectie, preventie en respons op bedreigingen mogelijk maakt.

Dit document dient als leidraad voor IT-beheerders en securityteams bij het beheren van Microsoft Defender en bevat richtlijnen voor monitoring, incidentrespons, updates en continue verbetering van de beveiligingsinstellingen.

### Wat is Microsoft Defender?

Microsoft 365 Defender is een geïntegreerde enterprise defense-suite voor pre- en post-breach die systeemeigen detectie, preventie, onderzoek en reactie coördineert tussen eindpunten, identiteiten, e-mail en toepassingen om geïntegreerde bescherming te bieden tegen geavanceerde aanvallen.

Met de geïntegreerde Microsoft 365 Defender-oplossing kunnen beveiligingsprofessionals de bedreigingssignalen die elk van deze producten ontvangen samenbrengen en bepalen wat het volledige bereik en de impact van de bedreiging is; hoe de bedreiging in de omgeving is terechtgekomen, wat de gevolgen ervan zijn en hoe dit op dit moment van invloed is op de organisatie. Microsoft 365 Defender automatisch actie onderneemt om de aanval te voorkomen of te stoppen en de getroffen postvakken, eindpunten en gebruikersidentiteiten zelf te herstellen.

Uitgebreide documentatie staat op de site van Microsoft.

Wat gebruiken wij?

Microsoft Defender voor Eindpunt is een beveiligingsplatform voor bedrijfseindpunten dat is ontworpen om bedrijfsnetwerken te helpen geavanceerde bedreigingen te voorkomen, detecteren, onderzoeken en erop te reageren.

Wat kan Microsoft Defender voor Eindpunt?

- Gedragssensoren voor eindpunten: deze sensoren zijn ingesloten in Windows 10 en verzamelen en verwerken gedragssignalen van het besturingssysteem en verzenden deze sensorgegevens naar uw persoonlijke, geïsoleerde cloudexemplaar van Microsoft Defender for Endpoint.

- Cloudbeveiligingsanalyse: door gebruik te maken van big data, apparaatleren en unieke Microsoft-optica in het Windows-ecosysteem, zakelijke cloudproducten (zoals Office 365) en onlineactiva, worden gedragssignalen vertaald in inzichten, detecties en aanbevolen antwoorden op geavanceerde bedreigingen.

- Bedreigingsinformatie: gegenereerd door Microsoft-jagers, beveiligingsteams en uitgebreid met bedreigingsinformatie van partners, stelt bedreigingsinformatie Defender voor Eindpunt in staat om hulpprogramma's, technieken en procedures van aanvallers te identificeren en waarschuwingen te genereren wanneer ze worden waargenomen in verzamelde sensorgegevens.

### Functionaliteiten Microsoft Defender

Incidenten, meldingen waarschuwingen Deze pagina biedt overzicht op incidenten, meldingen en waarschuwingen. Aan de rechterzijde van het scherm kan je eventueel ook meldingen en email notificaties instellen. Hieronder volgen de functionaliteiten welke op dit tabblad te vinden zijn:

Functionaliteiten:

Incidentbeheer: Groepeert meldingen in incidenten voor efficiënte analyse.

Meldingen bekijken: Inzicht in verdachte activiteiten, inclusief tijdlijn en betrokken entiteiten.

Impactanalyse: Beoordeel de impact op apparaten, gebruikers en cloud services.

Responsacties: Neem maatregelen zoals isoleren van apparaten, blokkeren van bestanden of starten van geautomatiseerde onderzoeken.

Filteren & prioriteren: Sorteer meldingen op ernst, status en categorie.

Geavanceerde opsporing (Advanced hunting) Op deze pagina kun je uitgebreide zoekopdrachten uitvoeren om beveiligingsbedreigingen en verdachte activiteiten te identificeren. Dit tabblad biedt een krachtige Kusto Query Language (KQL)-gestuurde zoekfunctie waarmee je diep in loggegevens kunt duiken. Hieronder volgt een overzicht van de verschillende mogelijkheden:

Functionaliteiten:

Geavanceerd zoeken naar bedreigingen

- Handmatig zoeken naar verdachte activiteiten, zoals ongebruikelijke aanmeldingen of procesuitvoeringen.

- Identificeren van mogelijk geïnfecteerde apparaten of accounts met abnormaal gedrag.

- Correlaties maken tussen verschillende logbestanden, zoals device, identity, en cloud events.

Analyseren van loggegevens

- Onderzoeken van endpoint-, netwerk- en cloudgebeurtenissen.

- Koppelen van data uit Microsoft Defender for Endpoint, Defender for Office 365, Defender for Cloud Apps en Defender for Identity.

- Controleren op indicatoren van compromittering (IoCs) zoals verdachte IP-adressen, domeinen of hashes.

Automatisering en detectieregels instellen

- Aangepaste detectieregels maken op basis van specifieke dreigingspatronen.

- Automatisch meldingen genereren voor terugkerende verdachte activiteiten.

- Integratie met Microsoft Sentinel voor bredere SIEM-functionaliteit.

Data exporteren en rapportages maken

- Query-resultaten exporteren naar CSV of JSON voor verdere analyse.

- Dashboards maken met inzichten over gedetecteerde bedreigingen en trends.

Kortom, Advanced Hunting geeft securityteams krachtige tools om proactief dreigingen te detecteren en te analyseren voordat ze schade aanrichten.

Acties & ingediende items

Op de Acties en Inzendingen-pagina kun je beveiligingsmaatregelen uitvoeren en verdachte bestanden of URL’s indienen voor analyse.

Functionaliteiten:

- Actiebeheer – Bekijk en beheer lopende en voltooide beveiligingsacties.

- Geautomatiseerde acties – Overzicht van acties die Defender automatisch heeft uitgevoerd.

- Handmatige acties – Zelf maatregelen nemen zoals bestanden blokkeren, apparaten isoleren of gebruikersaccounts beperken.

- Bestandsinzendingen – Verdachte bestanden, URL’s of e-mails indienen bij Microsoft voor diepgaande analyse.

- Analyse-resultaten – Ontvang feedback van Microsoft over ingediende bestanden en mogelijke dreigingen.

Hieronder een voorbeeld van een URL inzending:

Deze pagina helpt bij het actief mitigeren van bedreigingen en diepgaand onderzoeken van verdachte activiteiten.

Bedreigingsanalyse (Threat Analytics)

De Threat Analytics-pagina biedt diepgaande analyses van actuele en opkomende cyberdreigingen, inclusief impact op je organisatie en aanbevolen acties.

Functionaliteiten:

- Actuele dreigingsrapporten – Inzicht in de nieuwste cyberdreigingen en aanvallen.

- Impactanalyse – Controleer of en hoe je omgeving is blootgesteld aan specifieke dreigingen.

- Aanbevolen acties – Stappen om je verdediging te verbeteren, zoals updates of configuratiewijzigingen.

- Indicatoren van compromittering (IoCs) – Lijst met verdachte hashes, IP’s en domeinen om op te jagen in Advanced Hunting.

- Trendanalyse – Overzicht van dreigingsevoluties en hun relevantie voor je organisatie.

Met Threat Analytics kunnen securityteams proactief dreigingen begrijpen en beheersen voordat ze schade aanrichten.

Secure Score

De Secure Score-pagina geeft inzicht in de beveiligingsstatus van je organisatie en biedt aanbevelingen om deze te verbeteren.

Functionaliteiten:

- Beveiligingsscore – Een overzichtelijke score die aangeeft hoe goed je beveiliging is geconfigureerd.

- Aanbevolen verbeteringen – Concrete acties om risico’s te verkleinen, zoals het inschakelen van MFA of het updaten van kwetsbare software.

- Impactanalyse – Bekijk hoe elke maatregel je score en beveiligingsniveau beïnvloedt.

- Vergelijking met peers – Benchmark je beveiliging ten opzichte van vergelijkbare organisaties.

- Integratie met compliance – Koppeling met NIS2, ISO 27001 en andere standaarden.

Assets

In Microsoft Defender verwijst Assets naar alle digitale en fysieke entiteiten die beveiligd en gemonitord worden. Dit omvat:

- Apparaten – Werkstations, servers, mobiele apparaten en IoT-apparaten.

- Identiteiten – Gebruikersaccounts, serviceaccounts en beheerders.

- Applicaties & Cloudresources – SaaS-apps, Azure-resources en andere cloudservices.

Functionaliteiten:

- Overzicht van alle geregistreerde en actieve assets.

- Detectie van risico’s en beveiligingsproblemen per asset.

- Inzicht in de relatie tussen apparaten, identiteiten en cloudresources.

Door assets centraal te beheren, kunnen securityteams dreigingen sneller detecteren en risico’s minimaliseren.

Bij het selecteren van een apparaat krijg je een Device Summary te zien met de volgende secties:

- Overview: Basisinformatie over het apparaat, inclusief status en beveiligingsniveau.

- Alerts: Overzicht van meldingen en incidenten gekoppeld aan het apparaat.

- Timeline: Gedetailleerde weergave van alle (kern)processen en activiteiten.

- Security recommendations: Adviezen om kwetsbaarheden te verhelpen of de beveiliging te verbeteren.

- Software inventory: Lijst met alle geïnstalleerde software.

- Discovered vulnerabilities: Geïdentificeerde kwetsbaarheden op het apparaat.

- Advanced Features: Bevat functies zoals het blokkeren van kwetsbare applicatieversies, instellen van baseline-profielen en inzicht in browserextensies.

- Missing Security Updates: Overzicht van ontbrekende beveiligingsupdates.

Verder kan je ook:

- Apparaat isoleren – Verbreek netwerkverbindingen om verdere besmetting te voorkomen.

- "Go Hunt": Voer aangepaste KQL-query’s uit op het apparaat om kwetsbaarheden, malware, events en andere security-inzichten te verkrijgen.

- Manage Tags: Wijs labels toe aan apparaten voor betere organisatie.

Vulnerability management Vulnerability Management helpt bij het identificeren, beoordelen en verhelpen van kwetsbaarheden binnen de IT-omgeving. Ook de “Exposure score” is hier zichtbaar.

Functionaliteiten:

- Overzicht kwetsbaarheden: Lijst met bekende kwetsbaarheden op apparaten en software.

- Risico-inschatting: Beoordeling van de impact en exploitkansen van kwetsbaarheden.

- Remediatie-acties: Aanbevolen stappen om beveiligingsrisico’s te verminderen.

- Software Inventory: Inzicht in geïnstalleerde software en bijbehorende kwetsbaarheden.

- Integratie met Threat Intelligence: Context over hoe kwetsbaarheden worden misbruikt in het wild.

Met Vulnerability Management kunnen securityteams proactief risico’s aanpakken en de beveiliging versterken.

Evaluatie en zelfstudies

- Zoals de tekst beschrijft kan je hier test devices in een lab omgeving zetten. Hiermee kan je aanvallen testen op je apparaten.

- Configuratiebeheer

- In configuratiebeheer kan ik de apparaten zien die “onboarded” zijn. Dit houd in dat ze in Microsoft defender staan.

- Verder kan je:

- Compliance aanmaken voor een Security Baseline.

- Web protection instellen - Whitelisten van websites - Blacklisten van websites - Vooraf ingestelde categorieën van websites blokkeren.

Wat nu ingesteld staat:

RACI

| TAKEN | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Incidenten/Meldingen | de uitvoeringsorganisatie | de uitvoeringsorganisatie Bij P1 wachtdienst de hostingpartij | de uitvoeringsorganisatie/de hostingpartij | de uitvoeringsorganisatie/de hostingpartij (security) |
| Threat Analytics | de uitvoeringsorganisatie | de uitvoeringsorganisatie | de uitvoeringsorganisatie/de hostingpartij | de uitvoeringsorganisatie/de hostingpartij (security) |
| Secure score | de uitvoeringsorganisatie | de uitvoeringsorganisatie | de uitvoeringsorganisatie/de hostingpartij | de uitvoeringsorganisatie/de hostingpartij (security) |
| Endpoints | de uitvoeringsorganisatie/de hostingpartij | de uitvoeringsorganisatie/de hostingpartij | de uitvoeringsorganisatie/de hostingpartij | de uitvoeringsorganisatie/de hostingpartij (security) |
| Configuratiebeheer | de uitvoeringsorganisatie/de hostingpartij | de uitvoeringsorganisatie/de hostingpartij | de uitvoeringsorganisatie/de hostingpartij Microsoft | de uitvoeringsorganisatie/de hostingpartij (security) |
| Onboarding proces / sccm | de hostingpartij | de hostingpartij | de hostingpartij | de uitvoeringsorganisatie/de hostingpartij (security) |
| Web configuratie | de uitvoeringsorganisatie | de uitvoeringsorganisatie | de uitvoeringsorganisatie/de hostingpartij | de uitvoeringsorganisatie/de hostingpartij (security) |
| Remediation | de uitvoeringsorganisatie/de hostingpartij | de uitvoeringsorganisatie/de hostingpartij | de uitvoeringsorganisatie/de hostingpartij | de uitvoeringsorganisatie/de hostingpartij |

Legenda:

- de uitvoeringsorganisatie: Hierin is de uitvoeringsorganisatie verantwoordelijk – Informatiebeveiliging?

- de hostingpartij: Dit is in combinatie met het klantteam en het securityteam van de hostingpartij.

- Microsoft: Leverancier kan benaderd worden voor advies / hulp.

Taken kort uitgelegd:

- Incidenten/meldingen: het registreren van meldingen die voortkomen uit Defender en deze oplossen.

- Threat analytics: Het onderzoeken van kwetsbaarheden/ security meldingen.

- Secure score: In de gaten houden van of verbeteren van de algemene veiligheid van alle apparaten.

- Endpoints: Het beheren, naleven en configureren van Defender + ATP.

- Configuratiebeheer: Het configureren van security-instellingen op onze devices.

- Onboardingproces / SCCM: Zorgen dat ATP goed op de werkplekapparaat komt.

- Web configuratie: Webfiltering white en blacklisting.

- Remediation: Oplossen van kwetsbaarheden en het up-to-date houden van devices.
