# Controleraamwerk fysieke toegang en beveiliging

| | |
|---|---|
| Documenttype | Controleraamwerk (ICF) bij het materie-specifieke beleid Fysieke toegang en beveiliging |
| Thema-code | FTB |
| Versie | 1.2 |
| Status | Concept |
| Herkomst | Uitgewerkt in het werkblad van het controleraamwerk; FTB-006 is een voorstel en staat daar nog niet in. |
| Werkwijze | Zes stappen ICF: 1 vaststellen beleid, 2 concept ICF, 3 review materiedeskundige, 4 review management, 5 inrichten en testen in het servicedesksysteem, 6 uitvoeren |
| Eigenaar | Manager Facilitaire Zaken (FTB-001 tot en met FTB-005) |

## FTB-001 · Fysieke beveiligingszones

| Veld | Inhoud |
|---|---|
| Risico | Als beveiligingszones onjuist worden geclassificeerd in het zoneringsplan of onjuist worden geregistreerd in het fysieke toegangssysteem, kan dit resulteren in een te laag beschermingsniveau voor de beveiliging en bescherming van gegevens. |
| Beheersdoelstelling | Waarborgen van het vereiste beschermingsniveau voor fysieke informatie en IT-middelen. |
| Beschrijving | De functioneel beheerder exporteert de lijst met zones die zijn opgenomen in het fysieke toegangssysteem op basis van een voorgedefinieerd rapport. Dit systeemrapport wordt samen met het zoneringsplan opgenomen in het ticket dat jaarlijks geautomatiseerd wordt geregistreerd in het servicedesksysteem.<br><br>De eigenaar van een zone van categorie 2 of hoger beoordeelt vervolgens het zoneringsplan en het voorgedefinieerde rapport op de volgende aandachtspunten:<br>1. Zijn alle zones met de vereiste categorie 2 of hoger (conform het IB-beleid Fysieke toegang en beveiliging) als zodanig opgenomen in het zoneringsplan en het fysieke toegangssysteem?<br>2. Is het eigenaarschap van deze zones correct opgenomen in het zoneringsplan?<br><br>Opmerkingen of bijzonderheden worden geregistreerd in het ticket en opgevolgd door de functioneel beheerder van het toegangssysteem. Het ticket voor de uitvoering, vastlegging en opvolging van deze controle wordt afgerond voordat de status wordt gewijzigd naar "afgesloten" in het servicedesksysteem. |
| 6 W's | 1. Wat: controle juistheid eigenaarschap en classificatie zones<br>2. Waarom: classificatie zone bepaalt weerstandsniveau<br>3. Wie: eigenaar van de zone<br>4. Wanneer: jaarlijks<br>5. Waar: onderliggende documenten worden gearchiveerd in het servicedesksysteem<br>6. Waarmee: beleid FTB, zoneringsplan en autorisatiematrix toegangssysteem |
| Eigenaar | Manager Facilitaire Zaken |
| Frequentie | Jaarlijks |
| Werkdocumenten | ticket; zoneringsplan; systeemrapport FTB |
| Status | Niet geïmplementeerd |
| Maatregelen | 7.01.02 (7.01.01 is vervallen in de VvT 1.3) |
| Toelichting | |

## FTB-002 · Fysieke toegangsbeveiliging

| Veld | Inhoud |
|---|---|
| Risico | Onbevoegde fysieke toegang tot het archief of tot technische ruimtes voor de geautomatiseerde verwerking van gegevens. |
| Beheersdoelstelling | Waarborgen dat alleen bevoegde medewerkers op basis van een persoonlijke pas fysieke toegang hebben tot het archief en de technische ruimtes voor de geautomatiseerde verwerking van gegevens. |
| Beschrijving | De autorisaties in het fysieke toegangssysteem voor zones met categorie 2 of hoger worden pas aangemaakt en verstrekt na goedkeuring van de eigenaar van de betreffende zone (conform zoneringsplan).<br><br>De aanvraag wordt geregistreerd in het servicedesksysteem. De goedkeuring en het toekennen van de autorisaties worden in het bijbehorende ticket vastgelegd voordat de status wordt gewijzigd naar "afgesloten". |
| 6 W's | 1. Wat: beoordeling op basis van het need-to-know- en need-to-have-principe<br>2. Waarom: onbevoegde toegang kan ten koste gaan van BIV<br>3. Wie: eigenaar van de zone<br>4. Wanneer: per gebeurtenis<br>5. Waar: onderliggende documenten worden gearchiveerd in het servicedesksysteem<br>6. Waarmee: beleid FTB en aanvraag in ticket |
| Eigenaar | Manager Facilitaire Zaken |
| Frequentie | Per gebeurtenis |
| Werkdocumenten | ticket; zoneringsplan |
| Status | Niet geïmplementeerd |
| Maatregelen | 7.03.01, 7.04.01, 7.05.01 |
| Toelichting | |

## FTB-003 · Intrekken fysieke toegang na personeelsmutaties

| Veld | Inhoud |
|---|---|
| Risico | Onbevoegde fysieke toegang tot het archief of tot technische ruimtes voor de geautomatiseerde verwerking van gegevens. |
| Beheersdoelstelling | Waarborgen dat autorisaties voor toegang tot beveiligingszones tijdig worden ingetrokken in het fysieke toegangssysteem. |
| Beschrijving | In het servicedesksysteem worden door IAM, op basis van personeelsmutaties in het HR-systeem, taken aangemaakt voor het tijdig intrekken van fysieke toegangsrechten van de betreffende medewerker. De manager Facilitaire Zaken stelt op basis van een standaardrapportage vast dat deze geregistreerde taken tijdig door de medewerkers zijn uitgevoerd.<br><br>Het ticket voor de uitvoering, vastlegging en opvolging van deze controle wordt afgerond voordat de status wordt gewijzigd naar "afgesloten" in het servicedesksysteem. |
| 6 W's | 1. Wat: tijdig intrekken van bevoegdheden op passen bewaken<br>2. Waarom: onbevoegde toegang kan ten koste gaan van BIV<br>3. Wie: beleidsmedewerker Facilitaire Zaken<br>4. Wanneer: maandelijks<br>5. Waar: onderliggende documenten worden gearchiveerd in het servicedesksysteem<br>6. Waarmee: beleid FTB, systeemrapport met status van de taken "intrekken autorisaties op de toegangspas" en het ticket |
| Eigenaar | Manager Facilitaire Zaken |
| Frequentie | Maandelijks |
| Werkdocumenten | ticket; functionaliteit van de IAM-tool |
| Status | Niet geïmplementeerd |
| Maatregelen | 7.02.01 (ISO-control 7.2 Fysieke toegangsbeveiliging) |
| Toelichting | |

## FTB-004 · Periodieke controle van autorisaties door de eigenaar van de zone

| Veld | Inhoud |
|---|---|
| Risico | Onbevoegde fysieke toegang tot het archief of tot technische ruimtes voor de geautomatiseerde verwerking van gegevens. |
| Beheersdoelstelling | Waarborgen dat autorisaties voor toegang tot beveiligingszones tijdig worden ingetrokken in het fysieke toegangssysteem. |
| Beschrijving | De autorisaties in het fysieke toegangssysteem voor zones met categorie 2 of hoger worden op juistheid gecontroleerd door de eigenaar van de betreffende zone (conform zoneringsplan), op basis van een voorgedefinieerd systeemrapport.<br><br>Deze controle wordt geregistreerd in het servicedesksysteem. De beoordeling en de opmerkingen worden in het bijbehorende ticket vastgelegd voordat de status wordt gewijzigd naar "afgesloten". |
| 6 W's | 1. Wat: tijdig intrekken van bevoegdheden op passen bewaken<br>2. Waarom: onbevoegde toegang kan ten koste gaan van BIV<br>3. Wie: eigenaar van de zone<br>4. Wanneer: halfjaarlijks (niveau 2), per kwartaal (niveau 3)<br>5. Waar: onderliggende documenten worden gearchiveerd in het servicedesksysteem<br>6. Waarmee: ticket, beleid FTB, systeemrapport met autorisaties van het fysieke toegangssysteem voor categorie 2 en hoger |
| Eigenaar | Manager Facilitaire Zaken |
| Frequentie | Halfjaarlijks (niveau 2), per kwartaal (niveau 3). |
| Werkdocumenten | ticket; zoneringsplan; systeemrapport FTB |
| Status | Niet geïmplementeerd |
| Maatregelen | 7.02.01 (ISO-control 7.2 Fysieke toegangsbeveiliging) |
| Toelichting | |

## FTB-005 · Fysieke bescherming en beveiliging van informatiemiddelen en bekabeling

| Veld | Inhoud |
|---|---|
| Risico | Informatiemiddelen worden gecompromitteerd, gestolen of beschadigd. |
| Beheersdoelstelling | Het vereiste beschermings- en beveiligingsniveau van het archief en de technische ruimtes voor de geautomatiseerde verwerking van gegevens waarborgen. |
| Beschrijving | De manager Facilitaire Zaken beoordeelt op basis van een standaardchecklist of de positionering, beveiliging en bescherming van informatiemiddelen en bekabeling op de ambtelijke locaties conform het IB-beleid Fysieke toegang en beveiliging is ingericht en uitgevoerd.<br><br>Het ticket voor de uitvoering, vastlegging en opvolging van deze controle wordt afgerond voordat de status wordt gewijzigd naar "afgesloten" in het servicedesksysteem. |
| 6 W's | 1. Wat: beoordelen compliance met IB-beleid FTB<br>2. Waarom: onvoldoende bescherming of beveiliging kan ten koste gaan van BIV<br>3. Wie: eigenaar van de zone<br>4. Wanneer: halfjaarlijks<br>5. Waar: onderliggende documenten worden gearchiveerd in het servicedesksysteem<br>6. Waarmee: ticket, beleid FTB, checklist FTB |
| Eigenaar | Manager Facilitaire Zaken |
| Frequentie | Halfjaarlijks |
| Werkdocumenten | ticket; checklist FTB |
| Status | Niet geïmplementeerd |
| Maatregelen | 7.04.01, 7.05.01, 7.12.01 |
| Toelichting | |

## FTB-006 · Waarschuwingen bij concrete beveiligingsrisico's (voorstel)

| Veld | Inhoud |
|---|---|
| Risico | Een concreet beveiligingsrisico voor de fysieke beveiliging bereikt de relevante collega's binnen het beveiligingsdomein van de overheid niet, of een ontvangen waarschuwing bereikt de eigenaren van de betrokken zones niet, waardoor maatregelen uitblijven. |
| Beheersdoelstelling | Waarborgen dat concrete beveiligingsrisico's voor de fysieke beveiliging tijdig worden gemeld, beoordeeld en langs de afgesproken lijnen gedeeld, in beide richtingen. |
| Beschrijving | Meldingen van concrete beveiligingsrisico's voor de fysieke beveiliging komen via de incidentmeldroute bij de CISO. De CISO legt per melding vast of het risico andere overheidsorganisaties raakt en of, langs welke lijn en wanneer een waarschuwing is verzonden. Ontvangen waarschuwingen worden met advies doorgezet naar de afdeling Facilitaire Zaken en de eigenaren van de betrokken zones; de opvolging wordt in het servicedesksysteem vastgelegd.<br><br>Jaarlijks toetst team IB&P aan de hand van de registratie of de meldingen en waarschuwingen volgens deze afspraak zijn afgehandeld. |
| 6 W's | 1. Wat: melden, beoordelen en doorzetten van concrete beveiligingsrisico's<br>2. Waarom: de BIO 2.0 verlangt waarschuwingen binnen het beveiligingsdomein van de overheid (7.02.01)<br>3. Wie: CISO, met team IB&P<br>4. Wanneer: per gebeurtenis, jaarlijks getoetst<br>5. Waar: incidentregistratie en het servicedesksysteem<br>6. Waarmee: beleid FTB paragraaf 3, Strategisch IB-beleid (formele contacten), incidentmeldroute |
| Eigenaar | CIO / manager IT-ontwikkeling; uitvoering team IB&P (conform de VvT) |
| Frequentie | Per gebeurtenis; jaarlijkse toets |
| Werkdocumenten | Incidentregistratie; ticket; overzicht formele contacten uit het Strategisch IB-beleid |
| Status | Niet geïmplementeerd (voorstel, nog niet in het werkblad) |
| Maatregelen | 7.02.01 |
| Toelichting | Voorstel. Nog te besluiten of deze control hier hoort of bij beveiligingsincidenten. |
