# Procedure cyberdreigingen en kwetsbaarheden

> **Herkomst:** procedure van de CISO van een regionale samenwerking van gemeenten, september 2025, opgesteld met de informatiebeveiliger, de technische en de business information security officer en de projectmanager BCM. Voor de commons herschreven in een vaste opbouw; de bewijsregel en de koppeling aan BIO 2.0 zijn aanvullingen van de commons.

## Doel

Een dreiging is nog geen incident: een kwetsbaarheid is bekend, maar het is onduidelijk of zij de eigen
organisatie raakt. Voor incidenten bestaat een procedure; voor dreigingen meestal niet. Deze procedure zorgt
dat dreigingen en kwetsbaarheden gestructureerd worden beoordeeld op urgentie, impact en risico, en dat er
proportioneel en met duidelijk eigenaarschap wordt gehandeld. Het gaat over omgaan met onzekerheid: vlot
uitzoeken, voldoende duidelijkheid krijgen, en dan kiezen.

## Wanneer wel, wanneer niet

Altijd bij een signaal van buiten (IBD, NCSC, leverancier, SOC-dienstverlener) of van binnen (scanner,
beheerder) dat een kwetsbaarheid of dreiging meldt die mogelijk op de eigen omgeving van toepassing is.

Niet voor kwetsbaarheden die via het reguliere patchproces worden opgelost zonder dat iemand ze hoeft te
wegen; die lopen als change. Wel zodra er een afweging nodig is: misbruik is gaande, een patch is er niet,
of de maatregel heeft gevolgen voor de dienstverlening.

## Rollen

| Rol | Doet |
|---|---|
| ISO of informatiebeveiliger | Ontvangt het signaal, maakt de inschatting, is actiehouder richting de proceseigenaar; beheert deze procedure |
| Incidentcoördinator IT | Stemt met de ISO af bij gemiddeld en acuut risico, registreert in het servicedesksysteem |
| Proceseigenaar | Eigenaar van het risico voor zijn proces; krijgt het advies |
| CIO | Eigenaar als het risico procesoverstijgend is (bijvoorbeeld de IT-infrastructuur) |
| CISO | Escalatiepunt; adviseert de CIO over het activeren van het calamiteitenteam |
| Teammanager regie en processen | Escalatiepunt bij prioriteitsconflicten |
| Functioneel beheer, technisch applicatiebeheer, beheerpartij | Voeren de maatregel uit |

## Stappen

### 1. Signaal ontvangen en de klok zetten

- CVSS-score boven 9, of een melding van IBD of leverancier dat het acuut is: binnen **een uur** de
  risicoanalyse starten.
- Lagere dreiging: binnen **een week** behandelen.
- Als maatregelen nodig zijn of overwogen worden: altijd een melding in het servicedesksysteem.

### 2. Kans: raakt het ons?

Verzamel de dreigingsinformatie (CVSS, duiding van NCSC en IBD). Bepaal of de kwetsbaarheid op de eigen
systemen van toepassing is en welke aanvalspaden er zijn. Een actuele architectuurplaat en CMDB zijn hier de
randvoorwaarde; zonder die twee blijft dit gissen.

Lijkt het niet van toepassing, ga dan na hoe zeker dat is. Bij grote twijfel, een grote kans op misbruik en
een mogelijk grote impact: tóch analyseren. Dat is de "assume breach"-houding: wat je niet ziet, bestaat
daarmee niet niet.

### 3. Impact: wat raakt het?

Toets tegen de kritieke processen en kroonjuwelen uit de bedrijfscontinuïteitsanalyse, op beschikbaarheid,
integriteit, vertrouwelijkheid, privacy en bestuurlijke gevolgen. Eigenaar is de proceseigenaar; de ISO zorgt
dat die het advies krijgt. Is de proceseigenaar onbekend, dan toch doorgaan. Raakt het de infrastructuur,
dan is de CIO ook eigenaar en geldt het calamiteitenplan.

### 4. Risico en handelingskader

Kans maal impact, beide op een schaal van 1 tot 5. Zolang de risicobereidheid van de organisatie niet is
vastgesteld, is dit een vuistregel. Een niet-pluis-gevoel mag altijd escaleren; professionaliteit gaat boven
de procedure.

| Niveau | Score | Aanpak | Doorlooptijd |
|---|---|---|---|
| Laag | onder 5 | ISO schat de aanpak in, stemt af met functioneel beheer, technisch beheer en zo nodig de beheerpartij via het servicedesksysteem; reactie binnen een werkdag, oplossen via de reguliere planning | maximaal 10 werkdagen |
| Gemiddeld | 5 tot en met 14 | ISO en incidentcoördinator verkennen binnen een uur gezamenlijk de vervolgstappen; registratie in het servicedesksysteem; escalatie zo nodig naar CISO en teammanager regie en processen | maximaal 5 werkdagen |
| Acuut | 15 en hoger | ISO en incidentcoördinator stemmen af en informeren hun coördinator; geen oplossing binnen een uur, dan escalatie naar de CISO; de CISO kan de CIO adviseren het calamiteitenteam te activeren | zo kort mogelijk, bij voorkeur binnen een werkdag |

Bij acuut risico kan het nodig zijn preventief een systeem uit te zetten, ook als dat de kritieke
dienstverlening raakt. Schakel dan het calamiteitenteam in en nodig de proceseigenaar uit. Is de dreiging
echt acuut: eerst de maatregel, dan informeren.

### 5. Opties afwegen en kiezen

Vermijden, verminderen, overdragen of accepteren (ISO 27005), getoetst aan de Cbw en BIO 2.0. Er zijn vaak
meerdere maatregelen met verschillende kosten en restrisico's. Koppel terug aan de proceseigenaar en, als het
de infrastructuur raakt, de systeemeigenaar. Leg een omvangrijke of langlopende maatregel vast in het
servicedesksysteem.

### 6. Uitvoeren en bewaken

Monitor de voortgang in het servicedesksysteem of het ISMS. Escaleer bij vertraging of onvoldoende effect.

### 7. Risicoacceptatie

Zijn maatregelen niet of niet tijdig uitvoerbaar, leg het dan voor aan de bevoegde beslisser:
gemeentesecretaris of directie, afhankelijk van het impactniveau. Documenteer expliciet in een
risicoacceptatieformulier. Eigenaar is de bestuurder of directeur, na advies van de CISO.

## Wie informeer je, waarover en wie doet dat

| Niveau | Wie | Door wie | Waarover |
|---|---|---|---|
| Laag | Functioneel beheerder | ISO | Technische aard, aanpak, realistische termijn |
| | Gebruikersgroepen | Functioneel beheerder | Tijdelijke beperkingen of alternatieven |
| Gemiddeld | Incidentcoördinator | ISO | Risico-inschatting, onzekerheden, oplossing en tijdpad |
| | CISO en teammanager regie en processen (bij escalatie) | Incidentcoördinator of ISO | Dreigingsbeeld, knelpunten, noodzaak van prioriteit, bedrijfsimpact van de oplossing |
| | Gebruikersorganisatie | Incidentcoördinator of ISO | Verwachte impact en alternatieven |
| Acuut | Incidentcoördinator | ISO | Als bij gemiddeld, plus de escalatieaanpak |
| | CISO en teammanager | Incidentcoördinator of ISO | Onmogelijkheid van snelle mitigatie, besluit over het calamiteitenteam |
| | CIO | CISO | Advies om het calamiteitenteam te activeren |
| | Leden calamiteitenteam | CISO of secretaris | Dreigingsbeeld, besluitvorming, rollen |
| | Communicatieadviseur | CISO of secretaris | Of en hoe intern en extern wordt gecommuniceerd (IBD, clusters, regio) |
| | Direct betrokken afdelingen | Communicatie of incidentcoördinator | Aard van de verstoring, impact, herstelplanning, alternatieve werkwijze |

## Samenwerking en vuistregels

- Vaste rollen met back-ups. Een warme start: direct contact per telefoon of videogesprek; het
  servicedesksysteem is de plek voor registratie en bewaking, niet om de samenwerking mee te beginnen.
- Beslisbevoegdheden vooraf afgestemd, of expliciet aan het management gevraagd (mandaat om de stekker eruit
  te trekken).
- ISO en incidentcoördinatoren stemmen periodiek af, bijvoorbeeld elk kwartaal.
- **Zien is doen.** Wie het signaal ontvangt, zorgt dat het tot actie leidt. Je hoeft niet alles zelf op te
  lossen; regie nemen is het werk.
- **We zijn er bijna? Toch escaleren.** Hoeveel tijd het oplossen nog kost, is zelden goed in te schatten.
  Te vaak te vroeg aan de bel? Dan passen we de procedure aan.

## Onderhoud

De ISO beheert deze procedure en past hem jaarlijks aan, of na een evaluatie. Een acute dreiging wordt
binnen een week na afhandeling geëvalueerd.

## Aanvulling van de commons

> Drie punten die de oorspronkelijke procedure open laat en die BIO 2.0 wel vraagt.

- **Leg de afspraken met de SOC-dienstverlener en de beheerpartij vast** in de dienstverleningsovereenkomst:
  mandaat, piket, alarmering en spoedmaatregelen. Zonder die afspraken hangt stap 4 bij acuut risico aan
  goodwill.
- **Maak van het handelingskader een beslisboom** en zet die in het servicedesksysteem als kennisitem, zodat
  de servicedesk en functioneel beheer dezelfde route volgen als de ISO.
- **Bewaar per dreiging de afweging**, ook als de uitkomst "niet van toepassing" was. Dat is het bewijs
  voor 5.7: niet alleen dat je dreigingsinformatie ontvangt, maar dat je er iets mee doet.

## Bewijs

- Het **overzicht van behandelde dreigingen** van het jaar: signaal, datum, score, besluit, doorlooptijd,
  ook de afgewezen.
- Per acuut risico: de **melding in het servicedesksysteem** met de tijdstempels van signaal, eerste analyse
  en maatregel, en het **evaluatieverslag** binnen een week.
- Per geaccepteerd risico: het **risicoacceptatieformulier** met handtekening van de beslisser.
- De **vastgelegde afspraken** met SOC-dienstverlener en beheerpartij over mandaat en spoedmaatregelen.

## BIO 2.0

| Maatregel | Wat deze procedure daarvoor levert |
|---|---|
| 5.7 Informatie en analyses over dreigingen | Stap 1 en 2: dreigingsinformatie ontvangen, duiden en omzetten in een besluit |
| 8.8 Beheer van technische kwetsbaarheden | Het handelingskader met doorlooptijden per risiconiveau, de spoedroute bij CVSS boven 9 |
| 5.25 Beoordelen van en besluiten over informatiebeveiligingsgebeurtenissen | Stap 4: de weging en de escalatieroute naar incident of calamiteit |
| 5.4 Managementverantwoordelijkheden | Stap 7: risicoacceptatie op het bevoegde niveau, vastgelegd |
| 5.19 en 5.20 Leveranciersrelaties en -overeenkomsten | De aanvulling: mandaat en spoedmaatregelen contractueel vastleggen |

## Zo leg je het uit

**Aan de directie.** "Als het NCSC vandaag een kwetsbaarheid meldt, weten we morgen of die ons raakt, en
niet pas als het misgaat. En als de oplossing betekent dat we een systeem uitzetten, is vooraf afgesproken
wie dat mag beslissen."

**Aan de proceseigenaar.** "Je krijgt van ons geen technisch verhaal maar een advies: dit is het risico voor
jouw proces, dit zijn de opties, dit kosten ze. Jij kiest, en als je accepteert, leggen we dat samen vast."

**Aan de beheerders.** "Zien is doen. Je hoeft het niet zelf op te lossen, maar je zorgt dat het bij de
juiste persoon landt en niet blijft liggen. En escaleer liever een keer te veel dan te laat."
