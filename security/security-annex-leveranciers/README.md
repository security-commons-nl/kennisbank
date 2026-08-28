---
titel: Security Annex voor leveranciers, risicogedreven en verankerd in BIO2
sector: security
normen:
  - BIO2
  - ISO/IEC 27001
  - NIS2 / Cyberbeveiligingswet
  - Cyber Resilience Act (CRA)
  - AI Act
  - GIBIT 2025
type: contractbijlage / sjabloon
doelgroep: CISO's, ISO's, inkoop en contractmanagement in de publieke sector
versie: 1.3 (herzien BIO2)
versiedatum: 2026-08
herkomst: CISO-organisatie van een Nederlandse gemeente, gedeeld met toestemming
licentie: EUPL-1.2
status: sjabloon met invulvelden
---

# Security Annex voor leveranciers

Een contractbijlage die vastlegt wat een gemeente van een leverancier verwacht op het gebied van informatiebeveiliging: 20 artikelen, van normenkader en cloudsoevereiniteit tot FIDO2, SSDLC en AI. Ontwikkeld door en in gebruik bij een Nederlandse gemeente, hier gedeeld als sjabloon.

**Bestand:** [`security-annex-v1.3.md`](security-annex-v1.3.md) (bron) en [`security-annex-v1.3.html`](security-annex-v1.3.html) (plakbaar in Word).

## Lees dit eerst: risico's, niet de norm

Elk artikel in de Annex draagt BIO2-nummers. Dat wekt de indruk van een normlijst. Dat is hij niet. De auteur, in zijn eigen woorden:

> We hebben de Security Annex uiteraard gebaseerd op logische overheidsmaatregelen vanuit de BIO2, maar misschien nog wel belangrijker: we hebben hem vanuit risico's opgebouwd.
>
> Dus niet alleen: wat schrijft een norm voor? Maar vooral: welke aanvallen en incidenten zien we vandaag daadwerkelijk gebeuren, waar zijn leveranciers kwetsbaar en welke maatregelen maken daar aantoonbaar het verschil?

Vanuit die vraag springen er drie onderwerpen uit. Het zijn dezelfde risico's die gemeenten zelf lopen.

| Risico | Wat we nu zien gebeuren | Maatregel die het verschil maakt | Artikelen |
|---|---|---|---|
| **Identity**: accounts van leveranciers worden overgenomen en tegen ons misbruikt | phishing vanuit gecompromitteerde leveranciersaccounts, Adversary-in-the-Middle (AiTM) tegen push-MFA en number matching | phishing-resistente authenticatie (passkeys/FIDO2), just-in-time beheerrechten, minimale tenant-brede rollen | 14, 16, 17 |
| **Werkplek**: een besmette of slecht beveiligde leverancierswerkplek geeft toegang tot onze gegevens, applicaties of ontwikkelomgeving | besmette werkplekken en ontwikkelomgevingen als springplank | werkplekhardening, endpointbeveiliging, geen beheer vanaf werkplekken met lokale adminrechten | 15, 20.2 |
| **Kwetsbaarheden en softwareontwikkeling**: is de applicatie en de ontwikkelstraat technisch weerbaar genoeg? | kwetsbaarheden in applicaties en afhankelijkheden, aanvallen op de ontwikkelketen | pentesten (CCV-keurmerk), red teaming, structureel vulnerability management, SSDLC met SAST/DAST en SBOM | 7, 18, 20.1 |

De overige artikelen (normenkader, cloudsoevereiniteit, assurance, continuïteit, keten, incidenten, exit, sancties, AI) vormen het fundament waarop deze drie rusten.

**Zelftest van de auteur:** log je zelf nog in op gemeentelijke systemen met MFA via een pushnotificatie of een tweecijferige number match? Dan ben je vatbaar voor moderne AiTM-phishing. Precies daarom staat phishing-resistente authenticatie zo hoog.

## Geen vinklijst maar een gesprek

De Annex is nadrukkelijk geen statisch lijstje met vinkjes. Dreigingen veranderen, techniek verandert, en daarmee ook de maatregelen die het zwaarst wegen.

Niet iedere leverancier kan morgen aan iedere eis voldoen. Dat is juist het gesprek: waar staan we nu, welk risico lopen we, wat kunnen we verbeteren en binnen welke termijn? De CISO of ISO voert dat gesprek en ondersteunt de lijn daarbij, omdat die als geen ander de risico's ziet en kan uitleggen. Blijft er een restrisico over, dan bepaalt de bevoegde risico-eigenaar of dat acceptabel is.

Het doel is een volwassen partnership: open over kwetsbaarheden en risico's, leverancier én gemeente, zodat de keten steeds een stukje weerbaarder wordt.

## Zo gebruik je het sjabloon

1. Vul de invulvelden in (staan tussen `[ ]`):
   - art. 7.1: scope van de jaarlijkse pentest
   - art. 13.1: e-mailadres van het security-contact van de opdrachtgever
   - art. 13.2: aantal en rol van de vaste contactpersonen
   - art. 14.3: identity provider van de opdrachtgever (bijvoorbeeld Microsoft Entra ID)
2. Check de aannames die in de tekst zitten:
   - de Annex veronderstelt de **GIBIT 2025** als onderliggende voorwaarden (art. 6.2, 10.1, 12.3, 12.4, 18.6);
   - RTO/RPO verwijzen naar GIBIT; vul concrete waarden in als je die per dienst afspreekt;
   - beschikbaarheid staat op 99,9% per kalendermaand (art. 6.10);
   - hoofdstuk 3 (Europese zeggenschap, 25%-drempel) is een zware eis; bepaal per aanbesteding of je hem volledig oplegt.
3. Artikelen met de tag *(CRA)* komen voort uit de Cyber Resilience Act en gelden voor producten met digitale elementen.
4. Kopieer de HTML-versie in Word als je een contractbijlage nodig hebt. De markdown is de bron voor wijzigingen en pull requests.

## Herkomst en licentie

- Opgesteld door de CISO-organisatie van een Nederlandse gemeente en daar in gebruik. Versie 1.3, herzien op BIO2, augustus 2026.
- Gedeeld met toestemming van de auteur, op diens verzoek met de risicogedreven toelichting hierboven. Organisatie- en persoonsgegevens zijn verwijderd of vervangen door invulvelden.
- Licentie: EUPL-1.2, zoals de hele kennisbank.

## Feedback en verbeteringen

Gebruik je de Annex, of heb je een betere formulering voor een artikel? Open een [issue](https://github.com/security-commons-nl/kennisbank/issues/new/choose) of start een [discussion](https://github.com/security-commons-nl/kennisbank/discussions). Geen Git-ervaring nodig.
