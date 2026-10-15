# kennisbank — Roadmap

> Gedeelde kennisbank voor CISO's en ISO's in de publieke sector.

Peildatum: 15 oktober 2026. Loopt deze datum ver achter op wat de site laat zien, dan is dit stuk aan
herziening toe.

---

## Waar het staat

Tweeënzeventig items: tweeënveertig handleidingen, zeventien aanpakken, zes sjablonen, drie beleidsstukken
en een handvol referenties, lesmateriaal en een dataset. Per vakgebied: eenenvijftig onder `security`, negen
onder `privacy`, zes onder `governance`, zes onder `bcm`. De vorm ligt vast in het
[redactiestatuut](https://github.com/security-commons-nl/.github/blob/main/REDACTIESTATUUT.md) en wordt
gehandhaafd door `tools/build.py`: frontmatter (B2), map per stuk (B1), gegenereerde indexpagina's (B4),
bronnenregister (B15) en de anonimizer-check op elke pull request.

Sinds de vorige peildatum is `privacy` gevuld met de werkwijze van één privacyteam: DPIA, datalekken,
rechten van betrokkenen, register, overeenkomsten, eisen bij de start, Wpg, en het privacybeleid met
handboek. De beleidsset informatiebeveiliging die op 12 oktober onder `governance` kwam, is op 14 oktober
teruggetrokken: de meeste stukken waren nog onder BIO 1 vastgesteld, en een gemeente heeft actuele stukken
nodig. Dezelfde dag kwam hij terug, herschreven op BIO 2.0 versie 1.3 als 21 bouwstenen met een generator
die per antwoordprofiel op zestien contextvragen een eigen set maakt; een test bewijst bij elk profiel dat
alle 117 overheidsmaatregelen en de 40 ISO-beheersmaatregelen zonder overheidsmaatregel gedekt zijn, elk met een controle.

Op 15 oktober kregen de AI-stukken verwijzingen naar wat BZK, VNG en de IBD al hebben, zodat de kennisbank daar niet
naast gaat zitten. De security-annex ging naar versie 1.4: artikel 19 lid 19.1a zet AI-functionaliteiten van een
leverancier pas aan na schriftelijke toestemming, ook als ze via een update binnenkomen. De stelselkaart wordt
sindsdien gebouwd uit de data, met een check in de CI.

Op 15 oktober kwamen er vier stukken onder `bcm` bij, uitgewerkt voor een interbestuurlijke werkgroep
bedrijfscontinuïteit: een basissjabloon voor de BIA en de risicoanalyse per kritieke dienst, een handleiding
om uitwijk te regelen (met de uitwijkkaart als invulformat, ook voor clouddiensten), een compact
bedrijfscontinuïteitsplan voor elke bestuurslaag, en een twee-pager om BCM aan de bestuurder uit te leggen.

## Wat open staat

**De handleidingen afmaken.** Niet elke barrière uit de aanvalspaden heeft een handleiding. De lijst van wat
nog gevraagd is, staat als `gevraagd.json` in de aanvalspaden-repository; die lijst is afgeleid, dus hij
loopt niet achter.

**BCM verder vullen.** Zes items onder `bcm`, van kritieke processen tot het continuïteitsplan. Wat nog
ontbreekt: een uitgewerkte oefening per scenario uit het plan, en een tweede herkomst; alle zes komen uit
dezelfde hoek.

**Meer dan één herkomst.** Vrijwel alles komt nog uit dezelfde hoek. Een commons met kennis uit één
organisatie is een archief, geen commons. Het plan voor de AI-securitylijn (hieronder) zoekt die tweede
herkomst via de VNG-werkgroep AI en Algoritmen.

**De beleidsset verder op maat.** De set staat, met generator. Open in het plan
[beleidsset op maat](https://github.com/security-commons-nl/.github/blob/main/plannen/2026-10-12-beleidsset-op-maat.md):
IBD-materiaal en stukken van andere organisaties verwerken als regel of blok, en AI-hulp met eigen sleutel
bij het invullen.

**De AI-securitylijn.** Het plan
[AI-securitylijn](https://github.com/security-commons-nl/.github/blob/main/plannen/2026-10-15-ai-securitylijn.md)
(issue #83) loopt tot 1 december in vier sporen: verwijzen naar wat er al is (klaar), zeven nieuwe stukken met als
eerste de Copilot-configuratiekeuzes, materiaal van Amsterdam en Utrecht via de VNG-werkgroep, en verdediging met
AI: agent-patronen, een use-case-lijst en een keuzeblad.

---

## Bijdragen

Documenten aanleveren? Gebruik de [anonimizer](https://github.com/security-commons-nl/anonimizer-local)
om ze te anonimiseren voor je een PR opent. Zie
[CONTRIBUTING.md](https://github.com/security-commons-nl/.github/blob/main/CONTRIBUTING.md) voor de vorm.
