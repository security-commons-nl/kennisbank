# BIO 2.0-toets van de beleidsset

Per BIO 2.0-domein: welke overheidsmaatregelen de stukken in deze set afdekken. Peildatum 12-10-2026,
getoetst aan de BIO 2.0 versie 1.3 met de domeinindeling van het controleraamwerk. Een oordeel zegt of
er een beleidsregel staat die de maatregel invult, niet of de maatregel in de praktijk werkt.

- **gedekt**: een beleidsregel vult de maatregel in (vindplaats erbij);
- **deels**: een deel staat er, de toelichting zegt wat ontbreekt;
- **niet gedekt**: geen beleidsregel in deze set.

Maatregelen zonder overheidsmaatregel (alleen ISO 27002) staan per domein met nummer en titel; daar geldt
de ISO-maatregel zelf. De tekst daarvan is niet overgenomen.

## Overzicht

| Domein | Overheidsmaatregelen | Gedekt | Deels | Niet | Stuk in deze set |
|---|---|---|---|---|---|
| IV-beleid | 7 | 7 | 0 | 0 | [strategisch ib beleid](strategisch-ib-beleid.md) |
| Informatiebeveiliging binnen projecten | 1 | 0 | 1 | 0 | [beleid informatiebeveiliging in projecten](beleid-informatiebeveiliging-in-projecten.md) |
| Screening, bewustzijn & opleiding | 7 | 4 | 1 | 2 | [veilig personeel](veilig-personeel.md) |
| Bedrijfsmiddelenbeheer | 3 | 2 | 1 | 0 | [beheer van bedrijfsmiddelen](beheer-van-bedrijfsmiddelen.md) |
| Informatie classificatie | 6 | 3 | 2 | 1 | [dataclassificatie](dataclassificatie.md) |
| Logische toegangsbeveiliging | 14 | 7 | 3 | 4 | [logische toegangsbeveiliging](logische-toegangsbeveiliging.md), [functionele accounts en postbussen](functionele-accounts-en-postbussen.md) |
| Leveranciersbeheer - Inkoop | 9 | 8 | 0 | 1 | [beveiliging leveranciers en relaties](beveiliging-leveranciers-en-relaties.md), [webapplicaties](webapplicaties.md) |
| Leveranciersbeheer - contractbeheer | 5 | 1 | 4 | 0 | [beveiliging leveranciers en relaties](beveiliging-leveranciers-en-relaties.md) |
| Security Incident Management | 12 | 10 | 2 | 0 | [beveiligingsincidenten](beveiligingsincidenten.md) |
| Business Continuity & Disaster Recovery | 2 | 0 | 1 | 1 | geen (zie BCM-items) |
| IT-Compliance | 2 | 2 | 0 | 0 | [beleid it compliance](beleid-it-compliance.md) |
| Fysieke toegang & beveiliging | 2 | 2 | 0 | 0 | [fysieke toegang en beveiliging](fysieke-toegang-en-beveiliging.md), [controls fysieke toegang en beveiliging](controls-fysieke-toegang-en-beveiliging.md) |
| Afvoer en hergebruik gegevensdragers | 3 | 2 | 1 | 0 | [beheer van bedrijfsmiddelen](beheer-van-bedrijfsmiddelen.md) |
| Mobile Device Management | 2 | 1 | 1 | 0 | [beleid mobile device management](beleid-mobile-device-management.md), [wifi](wifi.md) |
| Vulnerability & patchmanagement | 9 | 5 | 4 | 0 | [kwetsbaarheidsmanagement](kwetsbaarheidsmanagement.md), [hardening](hardening.md) |
| Back-up & Recovery | 4 | 4 | 0 | 0 | [back up en recovery](back-up-en-recovery.md) |
| Logging & monitoring | 10 | 3 | 1 | 6 | [beleid logging en monitoring](beleid-logging-en-monitoring.md) |
| Netwerkbeveiliging | 7 | 5 | 2 | 0 | [netwerkbeveiliging](netwerkbeveiliging.md), [wifi](wifi.md) |
| Cryptografie | 4 | 2 | 2 | 0 | [cryptografie](cryptografie.md) |
| Secure Software Development | 2 | 1 | 1 | 0 | [webapplicaties](webapplicaties.md), [testdata](testdata.md) |
| Wijzigingsbeheer | 6 | 1 | 4 | 1 | [beleid wijzigingsbeheer](beleid-wijzigingsbeheer.md) |
| **Totaal** | **117** | **70** | **31** | **16** | |

Vervallen of verplaatste maatregelen uit versie 1.3 zijn weggelaten.

## IV-beleid

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 5.01.01 | IB-beleid vastgesteld door het bestuur, met de verplichte onderdelen | gedekt | [strategisch ib beleid](strategisch-ib-beleid.md) 1 t/m 8, bijlage A |  |
| 5.01.02 | Beleid jaarlijks beoordelen, aangesloten op P&C | gedekt | [strategisch ib beleid](strategisch-ib-beleid.md) 8.5 |  |
| 5.02.01 | Rollen en samenhang IB, privacy, OT en BCM vastgesteld | gedekt | [strategisch ib beleid](strategisch-ib-beleid.md) 5, 6 |  |
| 5.02.02 | CISO die onafhankelijk adviseert en rapporteert | gedekt | [strategisch ib beleid](strategisch-ib-beleid.md) 6.1, 6.2 |  |
| 5.05.01 | Overzicht formele contacten met instanties, jaarlijks bijgewerkt | gedekt | [strategisch ib beleid](strategisch-ib-beleid.md) 7 |  |
| 5.35.02 | Vastgesteld auditplan | gedekt | [strategisch ib beleid](strategisch-ib-beleid.md) 8.4 |  |
| 5.36.01 | Rapportage in P&C en PDCA, jaarlijkse ICV | gedekt | [strategisch ib beleid](strategisch-ib-beleid.md) 8.2, 8.3 |  |

Alleen ISO 27002: 5.03.01 Functiescheiding; 5.06.01 Contact met speciale belangengroepen; 5.07.01 Informatie en analyses over dreigingen.

## Informatiebeveiliging binnen projecten

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 5.08.01 | Risicoafweging bij nieuwe systemen en significante wijzigingen | deels | [privacy by design](../../privacy/privacybeleid-en-handboek/privacy-by-design.md) 2; [dataclassificatie](dataclassificatie.md) bepalen van classificatieniveaus | Alleen voor privacy (privacy by design) en via classificatie; geen eis voor de IB-risicoafweging per project. |

## Screening, bewustzijn & opleiding

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 5.04.01 | Bestuur en medewerkers volgen regelmatig scholing | gedekt | [strategisch ib beleid](strategisch-ib-beleid.md) 2.1; [veilig personeel](veilig-personeel.md) 3.2 |  |
| 6.01.01 | Vastgesteld screeningsbeleid, VOG op basis van risico | niet gedekt | [beveiliging leveranciers en relaties](beveiliging-leveranciers-en-relaties.md) VOG | Alleen voor medewerkers van leveranciers; veilig personeel noemt screening alleen in de normenbijlage. |
| 6.02.01 | Medewerkers bij aanstelling gewezen op hun IB-verantwoordelijkheden | gedekt | [veilig personeel](veilig-personeel.md) 5.1 |  |
| 6.03.01 | Iedereen kent de regels en verplichtingen | gedekt | [veilig personeel](veilig-personeel.md) 4; [strategisch ib beleid](strategisch-ib-beleid.md) 4.4 |  |
| 6.03.02 | Training I-bewustzijn binnen drie maanden na indiensttreding | gedekt | [veilig personeel](veilig-personeel.md) 3.2 | Het beleid is strenger: introductie binnen twee maanden en jaarlijkse training. |
| 6.03.03 | Management benadrukt het belang van training | deels | [veilig personeel](veilig-personeel.md) 5.2 | Wel aandacht bij functiewijziging; de rol van het management bij stimuleren staat er niet. |
| 6.03.04 | Veilig mobiel werken in het bewustwordingsprogramma | niet gedekt | - |  |

Alleen ISO 27002: 6.04.01 Disciplinaire procedure; 6.05.01 Verantwoordelijkheden na beëindiging of wijziging van het dienstverband; 6.06.01 Vertrouwelijkheids- of geheimhoudingsovereenkomsten.

## Bedrijfsmiddelenbeheer

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 5.09.01 | Inventaris van bedrijfsmiddelen, ook OT, cloud en op afstand | deels | [beheer van bedrijfsmiddelen](beheer-van-bedrijfsmiddelen.md) 2.1 | Inventaris is geregeld; OT, cloud en bedrijfsmiddelen op afstand worden niet genoemd. |
| 5.10.02 | Gedragsregels voor extern personeel in het contract | gedekt | [beheer van bedrijfsmiddelen](beheer-van-bedrijfsmiddelen.md) 2.1.4 |  |
| 5.10.03 | Medewerkers aantoonbaar gewezen op de gedragsregels | gedekt | [beheer van bedrijfsmiddelen](beheer-van-bedrijfsmiddelen.md) 2.1.4 |  |

Alleen ISO 27002: 5.10.01 Aanvaard gebruik van informatie en andere gerelateerde bedrijfsmiddelen; 5.11.01 Retourneren van bedrijfsmiddelen; 7.06.01 Werken in beveiligde zones; 7.08.01 Plaatsen en beschermen van apparatuur; 7.09.01 Beveiligen van bedrijfsmiddelen buiten het terrein; 7.11.01 Nutsvoorzieningen; 7.13.01 Onderhoud van apparatuur.

## Informatie classificatie

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 5.12.01 | Classificatie via een vastgestelde methodiek en risicoafweging | gedekt | [dataclassificatie](dataclassificatie.md) principes en stappen; [beheer van bedrijfsmiddelen](beheer-van-bedrijfsmiddelen.md) 2.2.1 |  |
| 5.14.01 | Internetfacing en mail voldoen aan de verplichte standaarden | deels | [cryptografie](cryptografie.md) 2.2.1.1 | De standaarden staan erin; sturing op internet.nl en het Cyberbeveiligingsbesluit niet. |
| 5.14.02 | OV-certificaten of PKIoverheid voor gevoelig webverkeer | deels | [cryptografie](cryptografie.md) 2.3 | Certificaatsoorten beschreven, de OV-eis niet. |
| 5.14.03 | Elektronische handtekeningen volgens AdES Baseline Profiles | gedekt | [netwerkbeveiliging](netwerkbeveiliging.md) 2.3.3 |  |
| 5.14.04 | Registratie van internetfacing systemen, IP-adressen en API's | gedekt | [webapplicaties](webapplicaties.md) eis 35; [netwerkbeveiliging](netwerkbeveiliging.md) 2.1.7 |  |
| 5.14.05 | Websites gemeld in het Register Internetdomeinen Overheid | niet gedekt | - |  |

Alleen ISO 27002: 5.13.01 Labelen van informatie.

## Logische toegangsbeveiliging

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 5.15.01 | Toegang tot een vertrouwde zone alleen vanaf geauthentiseerde apparatuur | niet gedekt | - |  |
| 5.16.01 | Sluitende registratie- en afmeldprocedure | gedekt | [logische toegangsbeveiliging](logische-toegangsbeveiliging.md) autorisatie en toegang; bijlage 3.1 |  |
| 5.16.02 | Groepsaccounts alleen gemotiveerd en afgestemd met de CISO | gedekt | [logische toegangsbeveiliging](logische-toegangsbeveiliging.md) uitgangspunten; [functionele accounts en postbussen](functionele-accounts-en-postbussen.md) 2.1 |  |
| 5.17.01 | MFA voor de werkomgeving, internetvoorzieningen en beheeraccounts | deels | [webapplicaties](webapplicaties.md) eis 11, 45; [wifi](wifi.md) thuis; [functionele accounts en postbussen](functionele-accounts-en-postbussen.md) 3.1 | MFA voor cloud, SaaS en leveranciers; niet als algemene eis voor het primaire aanloggen en beheeraccounts. |
| 5.17.02 | Wachtwoordmanager voor alle medewerkers | gedekt | [logische toegangsbeveiliging](logische-toegangsbeveiliging.md) uitgangspunten |  |
| 5.17.03 | Wachtwoordeisen geautomatiseerd afgedwongen | gedekt | [logische toegangsbeveiliging](logische-toegangsbeveiliging.md) uitgangspunten |  |
| 5.18.01 | Aanmaken en wijzigen van accounts met bijzondere rechten gemonitord | niet gedekt | - |  |
| 5.18.02 | Toegangsrechten minstens jaarlijks beoordeeld | gedekt | [logische toegangsbeveiliging](logische-toegangsbeveiliging.md) autorisatie en toegang; bijlage 3.1 | Het beleid is strenger: meerdere keren per jaar, overzicht per kwartaal. |
| 8.02.01 | Speciale bevoegdheden elk kwartaal beoordeeld | deels | [logische toegangsbeveiliging](logische-toegangsbeveiliging.md) bijlage 3.1 | Kwartaaloverzicht van alle autorisaties; speciale bevoegdheden niet apart. |
| 8.03.01 | Informatie met specifiek belang fysiek of logisch geïsoleerd | niet gedekt | - |  |
| 8.03.02 | Alleen toegang tot informatie die nodig is voor de taak | gedekt | [logische toegangsbeveiliging](logische-toegangsbeveiliging.md) uitgangspunten |  |
| 8.05.01 | Netwerktoegang voor leveranciers na risicoafweging, met registratie | gedekt | [functionele accounts en postbussen](functionele-accounts-en-postbussen.md) 3.1 |  |
| 8.18.01 | Systeemhulpmiddelen alleen voor bevoegd personeel | deels | [hardening](hardening.md) maatregelen | Installeren alleen door geautoriseerd personeel; systeemhulpmiddelen niet benoemd. |
| 8.18.02 | Gebruik van systeemhulpmiddelen gelogd, een halfjaar bewaard | niet gedekt | - |  |

Alleen ISO 27002: 6.07.01 Werken op afstand; 8.04.01 Toegangsbeveiliging op broncode.

## Leveranciersbeheer - Inkoop

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 5.19.01 | IB-eisen in offerteaanvragen, op basis van risico | gedekt | [beveiliging leveranciers en relaties](beveiliging-leveranciers-en-relaties.md) beveiligingseisen in inkoopvoorwaarden |  |
| 5.20.01 | Beveiligingseisen expliciet in het contract | gedekt | [beveiliging leveranciers en relaties](beveiliging-leveranciers-en-relaties.md) tabel inkoopvoorwaarden |  |
| 5.20.02 | Algemene voorwaarden van de leverancier uitgesloten | gedekt | [beveiliging leveranciers en relaties](beveiliging-leveranciers-en-relaties.md) tabel inkoopvoorwaarden |  |
| 5.20.03 | Leverancier toont opzet, bestaan en werking aan via onafhankelijke derden | gedekt | [beveiliging leveranciers en relaties](beveiliging-leveranciers-en-relaties.md) toezien op naleving; tabel controle en toezicht |  |
| 5.20.04 | Eigen onderzoek en recht op externe audit | gedekt | [beveiliging leveranciers en relaties](beveiliging-leveranciers-en-relaties.md) tabel inkoopvoorwaarden |  |
| 5.20.05 | Leverancier transparant over kwetsbaarheden en incidenten | gedekt | [beveiliging leveranciers en relaties](beveiliging-leveranciers-en-relaties.md) tabel inkoopvoorwaarden |  |
| 5.20.06 | Afhankelijkheid beoordeeld, exitstrategie in het contract | gedekt | [beveiliging leveranciers en relaties](beveiliging-leveranciers-en-relaties.md) tabel inkoopvoorwaarden |  |
| 5.21.02 | Inzicht in de keten van toeleveranciers vóór het contract | gedekt | [beveiliging leveranciers en relaties](beveiliging-leveranciers-en-relaties.md) tabel inkoopvoorwaarden |  |
| 5.21.05 | Toeleveringsketen onderdeel van de eigen risicoanalyse | niet gedekt | - |  |

## Leveranciersbeheer - contractbeheer

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 5.21.03 | Eisen gelden door in de keten van toeleveranciers | gedekt | [beveiliging leveranciers en relaties](beveiliging-leveranciers-en-relaties.md) tabel inkoopvoorwaarden |  |
| 5.21.04 | Leverancier meldt veranderingen in de keten tijdens de looptijd | deels | [beveiliging leveranciers en relaties](beveiliging-leveranciers-en-relaties.md) tabel inkoopvoorwaarden | Transparantie over de keten bij aanvang; wijzigingen tijdens de looptijd niet. |
| 5.22.01 | Proceseigenaar beoordeelt de leverancier jaarlijks | deels | [beveiliging leveranciers en relaties](beveiliging-leveranciers-en-relaties.md) tabel inkoopvoorwaarden; [procedure privacy overeenkomsten](../../privacy/privacy-overeenkomsten/procedure-privacy-overeenkomsten.md) stap 5 | Jaarlijkse toets alleen voor verwerkers van persoonsgegevens. |
| 5.22.02 | Actuele registratie van leveranciers en contracten | deels | [procedure privacy overeenkomsten](../../privacy/privacy-overeenkomsten/procedure-privacy-overeenkomsten.md) stap 4 | Alleen voor privacyovereenkomsten. |
| 5.23.01 | Beleid voor cloud service providers, eens per drie jaar herzien | deels | [webapplicaties](webapplicaties.md) eis 40 t/m 57 | Eisen aan SaaS-leveranciers; geen beleid voor selectie, beheer en beëindiging van CSP's. |

## Security Incident Management

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 5.24.01 | Toegankelijk meldloket voor IB-incidenten | gedekt | [beveiligingsincidenten](beveiligingsincidenten.md) 2.2 |  |
| 5.24.02 | Meldprocedure met taken van het meldloket | gedekt | [beveiligingsincidenten](beveiligingsincidenten.md) 2.2 | Via verwijzing naar de incident response procedure. |
| 5.24.03 | Proceseigenaar lost incidenten op | gedekt | [beveiligingsincidenten](beveiligingsincidenten.md) 2.2 |  |
| 5.24.04 | Maandelijkse rapportage aan de eindverantwoordelijke voor de bedrijfsvoering | deels | [beveiligingsincidenten](beveiligingsincidenten.md) 2.2 | Maandelijks, maar aan de CISO. |
| 5.24.05 | Verwijzing naar de procedure voor crisisbeheersing | gedekt | [strategisch ib beleid](strategisch-ib-beleid.md) 5.4 |  |
| 5.24.07 | Melden bij het CSIRT en informeren binnen de wettelijke termijn | deels | [beveiligingsincidenten](beveiligingsincidenten.md) 2.2; [strategisch ib beleid](strategisch-ib-beleid.md) 2.1, 5.4 | Het vastgestelde beleid noemt nog het oude regime (72 uur, NCSC alleen voor het Rijk); het concept verwijst naar de meldprocedure Cbw. |
| 5.24.08 | CVD-procedure ingericht en gepubliceerd | gedekt | [beveiligingsincidenten](beveiligingsincidenten.md) 2.3 |  |
| 5.26.02 | Afhandeling via incidentbeheer, melden bij toezichthouders | gedekt | [beveiligingsincidenten](beveiligingsincidenten.md) 2.5; [privacybeleid](../../privacy/privacybeleid-en-handboek/privacybeleid.md) datalekken |  |
| 5.27.01 | Afhandeling via incidentbeheer, melden bij toezichthouders | gedekt | [beveiligingsincidenten](beveiligingsincidenten.md) 2.5; [privacybeleid](../../privacy/privacybeleid-en-handboek/privacybeleid.md) datalekken |  |
| 5.27.02 | Incidenten geanalyseerd op oorzaken | gedekt | [beveiligingsincidenten](beveiligingsincidenten.md) 2.6 |  |
| 5.28.01 | Incidentinformatie minimaal drie jaar bewaard | gedekt | [beveiligingsincidenten](beveiligingsincidenten.md) 2.7 |  |
| 6.08.01 | Alle medewerkers kennen de meldprocedure aantoonbaar | gedekt | [beveiligingsincidenten](beveiligingsincidenten.md) 2.2 |  |

Alleen ISO 27002: 5.25.02 Beoordelen van en besluiten over informatiebeveiligingsgebeurtenissen.

## Business Continuity & Disaster Recovery

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 5.30.01 | Proceseigenaar test continuïteitsplannen jaarlijks | niet gedekt | - | Hoort bij BCM; zie de BCM-items van deze kennisbank. |
| 5.30.02 | Kritieke systemen geïdentificeerd, eens per drie jaar bijgewerkt | deels | [strategisch ib beleid](strategisch-ib-beleid.md) 3.3 | Kritieke processen en IT-middelen als grondslag van de scope, jaarlijks beoordeeld. |

Alleen ISO 27002: 5.29.01 Informatiebeveiliging tijdens een verstoring; 8.14.01 Redundantie van informatieverwerkende faciliteiten.

## IT-Compliance

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 5.33.01 | Bewaartermijnen per informatiesysteem vastgelegd en ingeregeld | gedekt | [privacybeleid](../../privacy/privacybeleid-en-handboek/privacybeleid.md) uitgangspunten; [privacyhandboek](../../privacy/privacybeleid-en-handboek/privacyhandboek.md) 7 |  |
| 7.07.01 | Vergrendeling bij het verwijderen van een chipcardtoken | gedekt | [logische toegangsbeveiliging](logische-toegangsbeveiliging.md) uitgangspunten |  |

Alleen ISO 27002: 5.31.01 Wettelijke, statutaire, regelgevende en contractuele eisen; 5.32.01 Intellectuele-eigendomsrechten; 5.34.01 Privacy en bescherming van persoonsgegevens; 8.06.01 Capaciteitsbeheer; 8.11.01 Maskeren van gegevens; 8.12.01 Voorkomen van gegevenslekken (data leakage prevention); 8.17.01 Kloksynchronisatie; 8.34.01 Bescherming van informatiesystemen tijdens audits.

## Fysieke toegang & beveiliging

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 7.01.02 | Kritieke informatie nooit via één beveiligde zone bereikbaar | gedekt | [fysieke toegang en beveiliging](fysieke-toegang-en-beveiliging.md) 2.4 |  |
| 7.02.01 | Waarschuwingen bij concrete beveiligingsrisico's gedeeld binnen de overheid | gedekt | [fysieke toegang en beveiliging](fysieke-toegang-en-beveiliging.md) 3 |  |

Alleen ISO 27002: 7.03.01 Beveiligen van kantoren, ruimten en faciliteiten; 7.04.01 Monitoren van de fysieke beveiliging; 7.05.01 Beschermen tegen fysieke en omgevingsdreigingen; 7.12.01 Beveiligen van bekabeling.

## Afvoer en hergebruik gegevensdragers

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 7.10.01 | Herbruikbare media onherstelbaar gewist voor ze de organisatie verlaten | gedekt | [beheer van bedrijfsmiddelen](beheer-van-bedrijfsmiddelen.md) 2.3.2 |  |
| 7.10.02 | Controle en verslag van het wissen, NBV-producten waar mogelijk | deels | [beheer van bedrijfsmiddelen](beheer-van-bedrijfsmiddelen.md) 2.3.2 | Registratie van verwijderverzoeken; verslag per medium en NBV-producten niet. |
| 7.10.03 | Betrouwbaarheidseisen aan koeriers | gedekt | [beheer van bedrijfsmiddelen](beheer-van-bedrijfsmiddelen.md) 2.3.3 |  |

Alleen ISO 27002: 7.14.01 Veilig verwijderen of hergebruiken van apparatuur; 8.10.01 Wissen van informatie.

## Mobile Device Management

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 8.01.01 | Zero footprint op mobiele apparatuur, anders versleuteling | gedekt | [wifi](wifi.md) beleid |  |
| 8.01.02 | MDM of MAM, patchen, gebruikersovereenkomst mobiel werken | deels | [cryptografie](cryptografie.md) 2.2.1.2; [beheer van bedrijfsmiddelen](beheer-van-bedrijfsmiddelen.md) 2.3.2 | Instellingen afdwingen en wissen op afstand; geen MDM-eis en geen gebruikersovereenkomst. |

## Vulnerability & patchmanagement

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 8.07.01 | Downloaden beheerst, antimalware beoordeelt alles | deels | [hardening](hardening.md) maatregelen | Gegevensuitwisseling gecontroleerd op malware; downloadbeleid niet. |
| 8.07.02 | Voorlichting over surfgedrag en links | gedekt | [veilig personeel](veilig-personeel.md) 4 |  |
| 8.07.03 | Antimalware actueel | deels | [hardening](hardening.md) maatregelen | Antivirus geactiveerd; actualiteit niet. |
| 8.07.04 | Malwarescan op alle omgevingen en ontvangen bestanden | deels | [hardening](hardening.md) maatregelen |  |
| 8.08.01 | Bij hoog risico mitigeren binnen een week | gedekt | [kwetsbaarheidsmanagement](kwetsbaarheidsmanagement.md) 2.4.1 |  |
| 8.08.02 | Mitigatie op basis van een expliciete risicoafweging | gedekt | [kwetsbaarheidsmanagement](kwetsbaarheidsmanagement.md) 2.4.1 |  |
| 8.08.03 | Tussentijds mitigeren als patchen niet binnen een week lukt | deels | [kwetsbaarheidsmanagement](kwetsbaarheidsmanagement.md) 2.4 | Alternatieve maatregelen genoemd, de termijn niet. |
| 8.08.04 | Jaarlijkse technische controle, internetfacing continu | gedekt | [kwetsbaarheidsmanagement](kwetsbaarheidsmanagement.md) 2.1.2 |  |
| 8.08.05 | Pentest bij elke release van internetfacing systemen | gedekt | [kwetsbaarheidsmanagement](kwetsbaarheidsmanagement.md) 2.1.2; [webapplicaties](webapplicaties.md) eis 38 |  |

Alleen ISO 27002: 8.09.01 Configuratiebeheer.

## Back-up & Recovery

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 8.13.01 | Back-upbeleid met aandacht voor ransomware | gedekt | [back up en recovery](back-up-en-recovery.md) back-up strategie, NIS2 |  |
| 8.13.02 | Maximaal dataverlies en hersteltijd op basis van risico | gedekt | [back up en recovery](back-up-en-recovery.md) risico-afweging |  |
| 8.13.03 | Back-up op een andere locatie | gedekt | [back up en recovery](back-up-en-recovery.md) algemene uitgangspunten (3-2-1) |  |
| 8.13.04 | Herstel minstens jaarlijks getest | gedekt | [back up en recovery](back-up-en-recovery.md) controleren en testen |  |

## Logging & monitoring

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 8.15.01 | Minimale inhoud van een logregel | niet gedekt | - |  |
| 8.15.02 | Geen gevoelige gegevens in logregels | niet gedekt | - |  |
| 8.15.03 | Overzicht van logbestanden | niet gedekt | - |  |
| 8.15.04 | Bewaartermijn van logs en SIEM op basis van risico | deels | [dataclassificatie](dataclassificatie.md) 4.2.2; [beveiligingsincidenten](beveiligingsincidenten.md) 2.7 | Bewaartermijnen per classificatieniveau; SIEM niet. |
| 8.15.05 | Wijzigen van loggegevens melden als incident | niet gedekt | - |  |
| 8.15.06 | Periodieke toets op ongewijzigde logbestanden | niet gedekt | - |  |
| 8.16.01 | Nieuwe dreigingen delen met het CERT | gedekt | [kwetsbaarheidsmanagement](kwetsbaarheidsmanagement.md) 2.1.4; [netwerkbeveiliging](netwerkbeveiliging.md) 2.1.3 |  |
| 8.16.02 | Regels voor rapportage van SIEM- of SOC-meldingen aan management | niet gedekt | - |  |
| 8.16.03 | Detectie- en response-oplossing | gedekt | [netwerkbeveiliging](netwerkbeveiliging.md) 2.1.3 |  |
| 8.16.04 | Logging en monitoring op actieve netwerkcomponenten | gedekt | [netwerkbeveiliging](netwerkbeveiliging.md) 2.1.3 |  |

## Netwerkbeveiliging

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 8.20.01 | Netwerkcomponenten op het niveau van hun netwerk | deels | [netwerkbeveiliging](netwerkbeveiliging.md) 2.1.5 |  |
| 8.20.02 | Beheerinterfaces gescheiden van het gebruikersnetwerk | gedekt | [logische toegangsbeveiliging](logische-toegangsbeveiliging.md) uitgangspunten |  |
| 8.21.01 | Aanvallen op beschikbaarheid in koppelpunten signaleren en mitigeren | gedekt | [netwerkbeveiliging](netwerkbeveiliging.md) 2.1.4 |  |
| 8.21.02 | Dataverkeer bewaakt met detectievoorzieningen | gedekt | [netwerkbeveiliging](netwerkbeveiliging.md) 2.1.3 |  |
| 8.21.03 | Nieuwe dreigingen gedeeld binnen de overheid | gedekt | [netwerkbeveiliging](netwerkbeveiliging.md) 2.1.3 |  |
| 8.21.04 | Versleuteling over wifi en bedrading buiten gecontroleerd gebied | deels | [netwerkbeveiliging](netwerkbeveiliging.md) 2.1.4; [wifi](wifi.md) beleid | Wifi wel; bedrade verbindingen buiten het gecontroleerde gebied niet. |
| 8.22.01 | Elk netwerksegment heeft een beveiligingsniveau | gedekt | [netwerkbeveiliging](netwerkbeveiliging.md) 2.1.5 |  |

Alleen ISO 27002: 8.23.01 Toepassen van webfilters.

## Cryptografie

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 8.24.01 | Cryptografiebeleid met de verplichte onderwerpen | gedekt | [cryptografie](cryptografie.md) 1 t/m 2.4 |  |
| 8.24.02 | Cryptografische maatregelen in de inventaris van bedrijfsmiddelen | deels | [cryptografie](cryptografie.md) 2.3.2 | Eigen registratiesysteem voor certificaten, niet in de inventaris van bedrijfsmiddelen. |
| 8.24.04 | Sterkte volgens NCSC en NBV | deels | [cryptografie](cryptografie.md) 2.2.1 | NCSC wel, NBV niet. |
| 8.24.05 | Reservecertificaten bij een alternatieve leverancier | gedekt | [cryptografie](cryptografie.md) 2.3 |  |

## Secure Software Development

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 8.27.01 | Security en privacy by design als vastgestelde architectuurprincipes | deels | [webapplicaties](webapplicaties.md) eis 9 t/m 37; [beveiliging leveranciers en relaties](beveiliging-leveranciers-en-relaties.md) tabel inkoopvoorwaarden; [privacy by design](../../privacy/privacybeleid-en-handboek/privacy-by-design.md) 1, 2 | Wel als uitgangspunt; niet als vastgestelde, gedocumenteerde principes voor alle ontwikkeling. |
| 8.30.01 | Eisen gelden ook voor uitbestede ontwikkeling | gedekt | [webapplicaties](webapplicaties.md) inleiding, SaaS-leveranciers |  |

Alleen ISO 27002: 8.25.01 Beveiligen tijdens de ontwikkelcyclus; 8.26.01 Toepassingsbeveiligingseisen; 8.28.01 Veilig coderen.

## Wijzigingsbeheer

| Maatregel | Waar het over gaat | Oordeel | Vindplaats | Toelichting |
|---|---|---|---|---|
| 8.19.01 | Installatie van niet-geautoriseerde software beheerst | gedekt | [hardening](hardening.md) maatregelen |  |
| 8.29.01 | Gestructureerde acceptatietesten met verslag | deels | [testdata](testdata.md) formulier | Testtypes genoemd; geen eis aan methodiek en verslag. |
| 8.31.01 | Niet testen in productie | deels | [testdata](testdata.md) uitzondering 3; [webapplicaties](webapplicaties.md) eis 46 | Scheiding OTA en strenge eisen aan productiedata; het verbod zelf staat er niet zo. |
| 8.31.02 | Significante wijzigingen getest vóór productie | deels | [functionele accounts en postbussen](functionele-accounts-en-postbussen.md) 3.1 | Alleen voor wijzigingen door leveranciers. |
| 8.32.01 | Wijzigingsbeheer met administratie, risicoafweging, rollback en goedkeuring | deels | [functionele accounts en postbussen](functionele-accounts-en-postbussen.md) 3.1; [netwerkbeveiliging](netwerkbeveiliging.md) 2.1.8 | Voor leverancierswijzigingen en het netwerk; geen algemeen wijzigingsbeleid. |
| 8.32.02 | Wijzigingsbeheer volgens een gangbaar beheerraamwerk | niet gedekt | - |  |

Alleen ISO 27002: 5.37.01 Gedocumenteerde bedieningsprocedures; 8.33.01 Testgegevens.
