# Classificatieschema voor beschikbaarheid, integriteit en vertrouwelijkheid

> **Herkomst:** classificatieschema en invulsjabloon van het team informatiebeveiliging, privacy en bedrijfscontinuïteit van een regionale samenwerking van gemeenten (2025), gebruikt in de risicosessies per kritiek proces. Voor de commons omgezet van spreadsheet naar tekst; de kanttekeningen zijn van de commons.

Met dit schema classificeer je een proces of een systeem op vijf niveaus, per aspect: beschikbaarheid (B),
integriteit (I) en vertrouwelijkheid (V). Het hoogste niveau van de drie bepaalt hoe kritiek het proces is.
Gebruik het in een [risicosessie per proces](../risicosessie-per-proces/), samen met de proceseigenaar.

## De vijf niveaus

| Niveau | Beschikbaarheid | Integriteit | Vertrouwelijkheid |
|---|---|---|---|
| **1 Verwaarloosbaar** | Een week of meer uitval of dataverlies wordt zonder merkbare schade opgevangen. Kernactiviteiten lopen door, hooguit met lichte vertraging. | Beslissingen blijven correct; fraude is verwaarloosbaar; geen juridische gevolgen of extra kosten. | *Openbaar.* Mag met iedereen gedeeld worden, bijvoorbeeld op de website. Moet wel nog kloppen en beschikbaar zijn. |
| **2 Gering** | Tot een week uitval of 24 uur dataverlies geeft hinder, maar de dienstverlening loopt grotendeels door. Herstel vraagt enige planning. | Beslissingen worden incidenteel beïnvloed; beperkt fraudrisico; kortdurende hinder; herstel relatief eenvoudig. | *Intern.* Hoort binnen de organisatie te blijven; openbaarmaking geeft hinder of lichte reputatieschade, maar is herstelbaar. |
| **3 Gemiddeld** | Tot twee werkdagen uitval of 8 tot 24 uur dataverlies raakt kernactiviteiten aanzienlijk: klachten, minder dienstverlening, extra kosten. | Beleid of keuzes kunnen duidelijk ontsporen; significant fraudrisico; kernprocessen lopen vertraging op; herstel kostbaar. | *Vertrouwelijk.* Openbaarmaking is schadelijk: reputatieschade, juridische claims, verstoorde samenwerking. Minimaal BIO 2.0, aangevuld met risicomanagement. |
| **4 Kritiek / zeer ernstig** | Tot 8 uur uitval of 4 tot 8 uur dataverlies kan strategische processen stilleggen, met brede maatschappelijke ontwrichting en bestuurlijke druk. | Bestuur beslist op verkeerde informatie; omvangrijke fraude aannemelijk; kernprocessen grotendeels stil; herstel zeer moeilijk. | *Confidentieel.* Openbaarmaking is ernstig schadelijk; staatsbelangen kunnen meespelen. BIO 2.0 alleen is dan niet genoeg. |
| **5 Catastrofaal** | Enkele uren uitval is onaanvaardbaar en kan leiden tot onherstelbare schade en een bestuurlijke crisis. Bijna permanente beschikbaarheid nodig. | Structurele fouten in bestuur en beleid; grootschalige fraude; vertrouwen blijvend weg; schade grotendeels onomkeerbaar. | *Geheim.* Openbaarmaking heeft catastrofale gevolgen voor samenleving of nationale veiligheid. Komt bij gemeenten vrijwel niet voor. |

Op de niveaus confidentieel en geheim gelden naast BIO 2.0 de aanvullende beveiligingseisen voor
rijksoverheids- of defensieopdrachten (ABRO, ABDO). Een gemeente komt daar zelden, maar het is goed te weten
waar de grens ligt.

## Vertaling naar hersteleisen

De regio koppelde de eigen niveaus aan herstelnormen per niveau. Zo levert de classificatie meteen een
uitgangspunt voor de hersteltijd (RTO) en het toelaatbare dataverlies (RPO), die in de afspraken met IT-beheer
en leveranciers terugkomen.

| Niveau | Impactniveau | RPO (dataverlies) | RTO (uitval en herstel) | Impact op de organisatie |
|---|---|---|---|---|
| 1 Verwaarloosbaar | Zeer laag | 36 uur | maximaal een week uitval, herstel in twee werkdagen | Minimale invloed op kernactiviteiten |
| 2 Gering | Laag | 24 uur | maximaal twee dagen uitval, herstel in een werkdag | Beperkte invloed op sommige kernactiviteiten; bevat persoonsgegevens |
| 3 Gemiddeld | Midden | 12 uur | maximaal een dag uitval, herstel in uren | Duidelijke invloed op meerdere kernactiviteiten; bijzondere persoonsgegevens of meerdere collecties persoonsgegevens |
| 4 Kritiek / zeer ernstig | Hoog | 4 uur | maximaal vier uur uitval, herstel in een uur | Strategische doelen ernstig in gevaar; meerdere collecties bijzondere persoonsgegevens |
| 5 Catastrofaal | Zeer hoog | 1 uur | maximaal een uur uitval, nauwelijks hersteltijd | Voortbestaan van de organisatie in gevaar |

> **Kanttekening van de commons.** In de bron zijn de uitvalduren in de beschikbaarheidskolom van het schema
> (bovenste tabel) ruimer dan in de hersteltabel. Op niveau 2 staat boven "tot een week", hieronder "maximaal
> twee dagen". Kies één set en leg die vast, anders spreken de proceseigenaar en IT-beheer bij een storing
> over verschillende normen. De impactniveaus hierboven zijn de eigen vertaling van de regio, geen tabel uit
> BIO 2.0 zelf.

## Invulvragen voor de sessie

Stel per aspect deze vragen en kies daarna het niveau dat het best past.

**Beschikbaarheid**

- Dit proces valt morgenochtend volledig uit. Wanneer wordt dat echt een probleem, niet alleen vervelend?
- Op welk moment ga je naar je leidinggevende en zeg je: dit is geen gewoon incident meer?
- Zijn er wettelijke termijnen of contractuele afspraken die bepalen hoe lang het proces mag stilliggen?
- Als het systeem terug is maar de gegevens van de laatste uren zijn weg, is dat acceptabel?
- Hoe snel veranderen de gegevens: doorlopend of af en toe?

**Integriteit**

- Wat gebeurt er als achteraf blijkt dat de gebruikte informatie niet klopte? Welke beslissingen zijn erop genomen?
- Hoeveel afwijking is nog acceptabel?
- Hoe makkelijk is een fout te herstellen, in tijd, moeite en impact?
- Wat gebeurt er als iemand de gegevens doelbewust aanpast, en hoe snel merken we dat?

**Vertrouwelijkheid**

- Welke informatie mag absoluut niet bij onbevoegden komen? Waar ligt de grens van echt ernstig?
- De informatie ligt morgen bij iemand die haar niet mag zien. Wat zijn de gevolgen?
- Maakt het uit hoeveel er lekt: één dossier of alles?
- Is de schade nog te herstellen als het eenmaal op straat ligt?

**Aanvullende impactgebieden** om mee te wegen: politieke schade aan een bestuurder, diplomatieke schade,
financiële gevolgen, directe imagoschade, verlies van publiek vertrouwen, organisatiebrede negatieve
publiciteit, motivatieverlies bij medewerkers, verlies van managementcontrole.

## BIO 2.0

| Maatregel | Wat dit schema daarvoor levert |
|---|---|
| 5.12 Classificeren van informatie | Vijf niveaus per aspect, met criteria |
| 5.30 ICT-gereedheid voor bedrijfscontinuïteit | De hersteltabel vertaalt het niveau in RTO en RPO |
| 5.29 Informatiebeveiliging tijdens een verstoring | De classificatie bepaalt welk beveiligingsniveau ook tijdens een verstoring moet blijven gelden |

Zie voor de procedure rond de classificatie de
[procedure security classificatie](../../security/procedures-informatiebeveiliging/security-classificatie.md).
