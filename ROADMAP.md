# kennisbank — Roadmap

> Gedeelde kennisbank voor CISO's en ISO's in de publieke sector.

Peildatum: 12 oktober 2026. Loopt deze datum ver achter op wat de site laat zien, dan is dit stuk aan
herziening toe.

---

## Waar het staat

Zesenzestig items: eenenveertig handleidingen, veertien aanpakken, vier sjablonen, drie beleidsstukken en
een handvol referenties, lesmateriaal en een dataset. Per vakgebied: eenenvijftig onder `security`, negen
onder `privacy`, vier onder `governance`, twee onder `bcm`. De vorm ligt vast in het
[redactiestatuut](https://github.com/security-commons-nl/.github/blob/main/REDACTIESTATUUT.md) en wordt
gehandhaafd door `tools/build.py`: frontmatter (B2), map per stuk (B1), gegenereerde indexpagina's (B4),
bronnenregister (B15) en de anonimizer-check op elke pull request.

Sinds de vorige peildatum is `privacy` gevuld met de werkwijze van één privacyteam: DPIA, datalekken,
rechten van betrokkenen, register, overeenkomsten, eisen bij de start, Wpg, en het privacybeleid met
handboek. Onder `governance` staat nu een complete beleidsset informatiebeveiliging, geordend naar de 21
BIO 2.0-domeinen en getoetst op de 117 overheidsmaatregelen.

## Wat open staat

**De handleidingen afmaken.** Niet elke barrière uit de aanvalspaden heeft een handleiding. De lijst van wat
nog gevraagd is, staat als `gevraagd.json` in de aanvalspaden-repository; die lijst is afgeleid, dus hij
loopt niet achter.

**BCM vullen.** Twee items onder `bcm` terwijl de voorpagina het vakgebied wel belooft. Een BCP-sjabloon,
een risicosessie per proces of een calamiteitenplan is genoeg om te beginnen.

**Meer dan één herkomst.** Vrijwel alles komt nog uit dezelfde hoek. Een commons met kennis uit één
organisatie is een archief, geen commons. Het plan hieronder maakt daar werk van.

## Beleidsset op maat: van één herkomst naar profielgestuurd

De beleidsset informatiebeveiliging is geordend naar de 21 BIO 2.0-domeinen, met per domein een toets op
de 117 overheidsmaatregelen. Nu komt alles nog uit één samenwerking van gemeenten. Het doel is een set
waarin een gebruiker een handvol vragen beantwoordt en per domein het concept krijgt dat bij zijn
organisatie past, met aanwijzingen waarmee zijn AI-agent het stuk afmaakt.

| Stap | Wat | Resultaat | Omvang |
|---|---|---|---|
| 1 | Toets, sjablonen voor de vijf lege domeinen en een uitgewerkt voorbeeld (fysieke toegang) publiceren | Gedaan | |
| 2 | Profielschema: zes tot acht vragen met vaste antwoordruimte (grootte, beheermodel, hosting, OT, samenwerking, Wpg-domeinen) in `profiel.yaml`; elk stuk krijgt in de frontmatter de profielkenmerken van zijn herkomst en de maatregelen die het dekt | Varianten zijn vergelijkbaar en selecteerbaar | 1 sessie |
| 3 | Per stuk een blok "maatwerk": invulvelden, keuzes per profielantwoord, vervolgvragen voor een AI-agent; `llms.txt` wijst ernaar | Een agent kan het stuk gericht afmaken | 1 sessie |
| 4 | De eerste variant uniform maken naar het format van het beleid fysieke toegang: per ISO-control de eisen met maatregelnummer, bijlage normen, bijlage controls, rollen als invulveld; de vijf sjablonen gevuld met een voorgestelde regel per maatregel | Variant 1 compleet voor alle 21 domeinen | 2 tot 3 sessies |
| 5 | Selectie: `build.py` genereert per domein een tabel van profiel naar variant, met uitleg; later een invulpagina | De gebruiker krijgt per domein de beste match | 1 sessie |
| 6 | Aanleverformulier voor andere organisaties: dezelfde profielkenmerken, dezelfde toets; een script geeft per aangeleverd stuk een eerste oordeel per maatregel, een mens corrigeert | Volgende inzenders hoeven niets te verzinnen | 1 sessie |
| 7 | Uitvraag aan gemeenten en het corpus vullen | Meer dan één herkomst per domein | doorlopend |

Randvoorwaarde: elke variant is tegen dezelfde 117 maatregelen gelegd, anders zegt selectie niets over
dekking.

---

## Bijdragen

Documenten aanleveren? Gebruik de [anonimizer](https://github.com/security-commons-nl/anonimizer-local)
om ze te anonimiseren voor je een PR opent. Zie
[CONTRIBUTING.md](https://github.com/security-commons-nl/.github/blob/main/CONTRIBUTING.md) voor de vorm.
