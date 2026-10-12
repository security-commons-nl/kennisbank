# Beleid netwerkbeveiliging

### Afkortingen

| Afkorting | Omschrijving |
|---|---|
| GDI | Gemeenschappelijke Digitale infrastructuur |
| CISO | Chief Information Security Officer |
| NBV | Nationaal Bureau voor Verbindingsbeveiliging |
| PKI | Public Key Infrastructure |
| VLAN | Virtual Local Area Network |
| AdES | Advanced Electronic Signatures |
| CERT | Computer Emergency Response Team |
| RACI | Responsible, Accountable, Consulted, Informed |

### Relevante beleidsdocumenten

- Beleid Beveiligingsincidenten

- Beleid Beheer van Bedrijfsmiddelen

- Beleid Cryptografie

- Beleid Hardening

- Procedures voor verandermanagement

## Inleiding

### 1.1 Doel

Het doel van dit beleid is om de beveiligingsvereisten van de organisatie voor het ontwerpen en beheren van ondersteunende netwerken te bepalen.

### 1.2 Doelstellingen

Dit document heeft tot doel te verzekeren dat:

- Duidelijke vereisten worden gesteld aan het beveiligingsontwerp van het netwerk.

- De rollen en verantwoordelijkheden voor het beheer van het netwerk worden gedefinieerd en gedocumenteerd.

- Er voldoende controles zijn opgesteld voor de overdracht van gegevens van de organisatie.

### 1.3 Toepassingsgebied van het document

- Dit beleid is van toepassing op alle medewerkers, dienstenleveranciers en externe partijen die betrokken zijn bij het beheer, onderhoud en gebruik van de netwerkinfrastructuur van de organisatie. Het omvat zowel interne als uitbestede netwerkdiensten en is van kracht op alle locaties waar gemeentelijke informatie wordt verwerkt.

- Dit beleid vormt de basis voor een veilige informatiecultuur en is onderhevig aan regelmatige evaluatie en aanpassing om te blijven voldoen aan de veranderende dreigingslandschappen en normen op het gebied van informatiebeveiliging.

## Beleidsvereisten

### 2.1 Beheersmaatregelen voor Netwerken

Effectief netwerkbeheer vormt de basis voor het beschermen van gevoelige informatie. Het minimaliseert de kans op ongeautoriseerde toegang, dataverlies en onderbrekingen van de informatievoorziening. De organisatie streeft naar een effectief beheer van netwerken om de veiligheid van informatie in systemen en toepassingen te waarborgen.

#### 2.1.1 Netwerkbeveiligingsontwerp

De organisatie zal een netwerkontwerp vastleggen. Dit netwerkontwerp moet gebaseerd zijn op een duidelijke definitie van eisen, die de volgende factoren met betrekking tot beveiliging omvatten:

- Het niveau van vertrouwen tussen verschillende aangesloten componenten of organisaties.

- Het aantal uren dat het netwerk beschikbaar moet zijn en de mate van veerkracht die van het netwerk wordt vereist.

- De geografische spreiding van het netwerk.

- De beveiligingscontroles op locaties van waaruit toegang zal worden verkregen tot het netwerk.

- De beveiligingsmogelijkheden van bestaande computers of apparaten die voor toegang zullen worden gebruikt.

#### 2.1.2 Beveiliging van Netwerkdiensten

- Om te waarborgen dat alle netwerkdiensten voldoen aan de vereiste beveiligingsnormen, zal de organisatie beveiligingsmechanismen, dienstverleningsniveaus en beheereisen voor alle netwerkdiensten identificeren. Zowel voor intern geleverde als uitbestede diensten.

- Dienstenleveranciers zijn verantwoordelijk voor het opnemen van deze aspecten in overeenkomsten betreffende netwerkdiensten.

#### 2.1.3 Bewaking van Dataverkeer en Dreigingsdeling

- Door actieve monitoring worden de risico's van cyberaanvallen gereduceerd en kan er snel worden gereageerd op potentiële bedreigingen, waardoor de integriteit en beschikbaarheid van informatie wordt beschermd. Daarom zal het inkomend en uitgaand dataverkeer continu worden bewaakt op kwaadaardige elementen middels detectievoorzieningen zoals beschreven in de richtlijn voor implementatie van detectieoplossingen.

- Hiervoor kan de organisatie gebruik maken van de Generieke Digitale Infrastructuur (GDI).

- Vastlegging en monitoren van de organisatie netwerkservices en -systemen moeten in lijn zijn met het Beleid Vastlegging en Monitoren en de procedures van de organisatie. Vastlegging en monitoren van netwerkservices en -systemen wordt meegenomen in het maandelijkse rapportage overleg betreffende vastlegging en monitoren.

- Er moet een strikte scheiding zijn tussen ‘operatie’ en ‘controle’: een partij die operationele netwerkdiensten en/of infrastructuurdiensten levert mag geen controlediensten leveren.

- Nieuwe dreigingen worden verplicht gedeeld binnen de organisatie, bij voorkeur geautomatiseerd, rekening houdend met geldende juridische kaders. Waaronder het delen van informatie met de sectorale CERT, bij voorkeur door geautomatiseerde mechanismen (threat intelligence sharing).

- De toegang tot externe websites behoort te worden beheerd om de blootstelling aan kwaadaardige inhoud te beperken.

#### 2.1.4 Draadloze netwerken

- De organisatie moet ervoor zorgen dat draadloze netwerken worden beveiligd met passende beveiligde versleuteling in lijn met het inzetadvies van het Nationaal Bureau voor Verbindingsbeveiliging (NBV).

- Gast-wifi-netwerken moeten passend worden gesegmenteerd van de organisatie bedrijfsnetwerken om aanvallen tegen de netwerken van de organisatie vanuit het gastnetwerk te voorkomen.

- In koppelpunten met externe of onvertrouwde zones zijn maatregelen getroffen om mogelijke aanvallen die de beschikbaarheid van de informatievoorziening negatief beïnvloeden (bijvoorbeeld DDoS-aanvallen, Distributed Denial of Service attacks) te signaleren en hierop te reageren.

- Draadloze netwerkoplossingen moeten alle apparaten en gebruikers verifiëren voordat ze toegang krijgen tot het netwerk van de organisatie.

#### 2.1.5 Scheiding in Netwerken

- De organisatie moet ervoor zorgen dat het netwerk is opgesplitst in kleinere netwerken, gescheiden op basis van grenzen tussen verschillende netwerksegmenten zodat de gegevens van elke segment worden beschermd en gescheiden van de gegevens van andere segmenten. Informatiediensten, -gebruikers en -systemen worden gescheiden in netwerken met gedefinieerde beveiligingsniveaus.

- Dit kan de organisatie doen door middel van het segmenteren met virtuele lokale netwerken (VLAN’s).

- Alle gescheiden groepen hebben een gedefinieerd beveiligingsniveau.

#### 2.1.6 Fysieke beveiliging

- Netwerkapparatuur van de organisatie kantoren en gebouwen die onder het beheer vallen van de organisatie vallen moet zich bevinden in beveiligde kasten/kamers, die alleen toegankelijk zijn voor geautoriseerd personeel.

- Netwerkapparatuur in datacenters moet worden gehuisvest in beveiligde kasten die moeten worden vergrendeld en alleen toegankelijk zijn voor geautoriseerd personeel.

#### 2.1.7 Documentatie & Onderhoud

- Netwerkontwerpen moeten regelmatig worden onderhouden en bijgewerkt, zowel op regelmatige basis als wanneer er belangrijke wijzigingen worden aangebracht in de omgeving.

- IP-adres toewijzingsschema's en implementaties moeten worden onderhouden om tracking en eigendom te waarborgen.

- Er moet ten minste elke 12 maanden een beoordeling worden uitgevoerd van de bestaande routerregels.

#### 2.1.8 Netwerkveranderingen

- Netwerkveranderingen moeten worden geïmplementeerd volgens een goedgekeurde verandermanagementproces en -procedure. Dit verandermanagementproces omvat een wekelijks overleg waarin het Change Advisory Board alle veranderingen behandeld.

- Wijzigingen aan netwerkdiensten of het netwerkontwerp moeten worden geregistreerd in het servicedesksysteem.

#### 2.1.9 Beveiligingsincidenten

Een netwerkevenement/incident moet worden beheerd in overeenstemming met het Beleid Beveiligingsincidenten en de Incident Response procedures van de organisatie.

### 2.2 Informatieoverdrachten

#### 2.2.1 Beleid en Procedures voor Informatietransport

Formele beleidsregels, procedures en beheersmaatregelen zijn van kracht om informatietransport via alle communicatiefaciliteiten te beschermen. Deze formele beleidsregels, procedures en beheersmaatregelen moeten in lijn zijn met het Beleid Beheer van Bedrijfsmiddelen en het Beleid Cryptografie en Hardening van de organisatie.

#### 2.2.2 Overeenkomsten over Informatietransport

Overeenkomsten tussen de organisatie en externe partijen hebben betrekking op het beveiligd transporteren van bedrijfsinformatie. Door beveiligingseisen op te nemen in overeenkomsten, wordt de vertrouwelijkheid en integriteit van informatie tijdens transport gewaarborgd, zelfs bij externe communicatie.

#### 2.3.3 Elektronische Berichten

Informatie die is opgenomen in elektronische berichten behoord passend te zijn beschermd.

- Elektronische (e-mail)berichten voldoen aan vastgestelde open standaarden tegen phishing en afluisteren.

- Veilige berichtenuitwisseling met externe basisregistraties gebeurt volgens de 'pas toe of leg uit'-lijst van het Forum.

- Gebruik van PKI bij web- en mailverkeer van gevoelige gegevens.

- Elektronische handtekeningen voldoen aan de AdES Baseline Profile standaard.

- Bij het versturen van vertrouwelijke informatie via e-mail, wordt deze informatievia beveiligde mail verstuurd.

- De organisatie streeft naar het gebruik van two-way SSL voor koppelingen met externe partijen via de Enterprise Service Bus ESB.

#### 2.3.4 Vertrouwelijkheids- of Geheimhoudingsovereenkomst

Eisen voor vertrouwelijkheids- of geheimhoudingsovereenkomsten die de behoeften van de organisatie betreffende het beschermen van informatie weerspiegelen, behoren te worden vastgesteld, regelmatig te worden beoordeeld en gedocumenteerd.

## Evaluatie en Verbetering van het Beleid

Het Beleid Netwerkbeveiliging wordt jaarlijks geëvalueerd om de doeltreffendheid ervan te waarborgen. Op basis van evaluatieresultaten worden indien nodig verbeteringen aangebracht in het beleid.

## Vrijwaring

In het kader van voortdurende verbetering en naleving van beleidsdoelstellingen, wordt erkend dat bepaalde vereisten momenteel niet kunnen worden vervuld volgens het huidige beleidsstuk. Echter, met het oog op toekomstige inzet voor progressieve ontwikkeling, zijn deze niet nagekomen verplichtingen opgenomen in de veranderkalender voor 2024. Hoewel ze momenteel buiten bereik liggen, is uitgesproken om tegen de aangegeven tijdlijn aan alle gestelde eisen te voldoen, waarmee het beleid wordt versterkt in lijn met gemeentelijke doelstellingen en in lijn met de vereisten van de BIO 2.0.

## Rollen en verantwoordelijkheden

Dit RACI-diagram biedt een overzicht van de verdeling van verantwoordelijkheden binnen de implementatie en handhaving van het netwerkbeveiligingsbeleid van de organisatie. De matrix identificeert de rollen van verschillende belanghebbenden bij specifieke taken en activiteiten die essentieel zijn voor een effectieve beveiliging van het netwerk. Hieronder wordt de betekenis van de gebruikte afkortingen toegelicht:

- R (Responsible): De persoon of groep die verantwoordelijk is voor de uitvoering van een specifieke taak of activiteit.

- A (Accountable): De individuele persoon die uiteindelijk verantwoordelijk is en beslissingsbevoegdheid heeft voor het betreffende onderdeel.

- C (Consulted): Personen of afdelingen die geraadpleegd moeten worden voor input en feedback bij de uitvoering van taken.

- I (Informed): Personen of afdelingen die op de hoogte moeten worden gehouden van de voortgang en resultaten van specifieke taken.

| Activiteit | R | A | C | I |
|---|---|---|---|---|
| 2.1.1 Netwerkbeveiligingsontwerp | Netwerk Architect | CISO | het securityteam | CISO |
| 2.1.2 Beveiliging van Netwerkdiensten | Netwerk Architect | CISO | het securityteam | CISO |
| 2.1.3 Bewaking van Dataverkeer en Dreigingsdeling | SOC-dienstverlener | SOC-dienstverlener |  | CISO |
| 2.1.4 Draadloze netwerken | Netwerk Architect | CISO | het securityteam | CISO |
| 2.1.5 Scheiding in Netwerken | Netwerk Architect | CISO | het securityteam | CISO |
| 2.1.6 Fysieke beveiliging | Facilitair de hostingpartij | CISO | het securityteam | CISO |
| 2.1.7 Documentatie & Onderhoud | Netwerk Architect | CISO | het securityteam | CISO |
| 2.1.8 Netwerkveranderingen | Change Manager | CISO | het securityteam | CISO |
| 2.1.9 Beveiligingsincidenten | Incident Manager | CISO | het securityteam | CISO |
| 2.2.2 Overeenkomsten over Informatietransport | Juridisch team | CISO | het securityteam | CISO |
| 2.2.3 Elektronische Berichten | Netwerk Architect | CISO | het securityteam | CISO |
| 2.2.4 Vertrouwelijkheids- of Geheimhoudingsovereenkomst | Juridisch team | CISO | het securityteam | CISO |
