# Security-assessment leverancier bij een DPIA

Vragen voor de security officer bij hoofdstuk 6.2 van het [sjabloon](sjabloon-dpia.md). De onderwerpen liggen niet vast: pas ze aan als dat nodig is.

## 1. Leveranciersbeoordeling

**Certificeringen en compliance**

- Heeft de leverancier een ISO/IEC 27001-certificaat?
- Is de bijbehorende verklaring van toepasselijkheid beschikbaar?
- Zijn er andere certificeringen, zoals NEN 7510 (zorg) of een SOC 2-verklaring?

**Patchbeleid en kwetsbaarhedenbeheer**

- Is er een gedocumenteerd patchbeleid?
- Hoe snel worden kwetsbaarheden opgelost (bijvoorbeeld binnen x dagen)?
- Staan afspraken daarover in de SLA of de dossierafspraken?

## 2. Architectuur van de oplossing

**Netwerktekening**

- Is er een actuele netwerktekening?
- Staan segmentatie en beveiligingszones er duidelijk op?

**Gegevensuitwisseling**

- Welke gegevens worden uitgewisseld (bijvoorbeeld persoonsgegevens of financiële gegevens)?
- Hoe gebeurt dat (bijvoorbeeld via een API, SFTP of een webservice)?
- Worden de gegevens tijdens transport versleuteld?

## 3. Authenticatie

**Gebruikersauthenticatie**

- Hoe verloopt de authenticatie (bijvoorbeeld via SSO, LDAP of OAuth)?

**Meerfactorauthenticatie**

- Is MFA verplicht voor alle gebruikers?
- Welke vormen worden ondersteund (bijvoorbeeld sms, een authenticator-app of een hardwaretoken)?

## 4. Beschikbaarheid

- Welke maatregelen garanderen een hoge beschikbaarheid?
- Zijn er SLA's met uptime-garanties?

**Back-up en herstel**

- Worden er regelmatig back-ups gemaakt?
- Wat is de bewaartermijn van de back-ups?
- Worden er hersteltests gedaan?

**Redundantie**

- Zijn de kritieke componenten redundant uitgevoerd?
- Is er failover en loadbalancing?

## 5. Integriteit

- Is er een autorisatiematrix met rollen, taken en rechten?
- Zijn de taken gescheiden, bijvoorbeeld tussen gebruikers en beheerders?
- Hoe worden in-, door- en uitstroom van gebruikers beheerd? Zijn er vaste procedures voor aanvragen?
- Worden kritieke handelingen gelogd? Zijn de logs onveranderbaar en centraal opgeslagen?
- Wordt er actief gemonitord op afwijkend gedrag?

## 6. Vertrouwelijkheid

- Worden gegevens versleuteld tijdens transport, en in rust?
- Worden de encryptie-algoritmen actueel gehouden?
- Is er een wachtwoordbeleid? Wordt SSO gebruikt of een eigen authenticatiesysteem?

## 7. Samenvatting en conclusie

Wat is de algemene indruk, en welke restrisico's moeten worden geaccepteerd of aangepakt?
