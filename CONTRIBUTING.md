# Bijdragen aan de kennisbank

Dit is een commons voor CISO's en ISO's in de publieke sector. Iedereen die werkende kennis wil delen of verbeteren is welkom.

## 1. Iets aanbieden of melden — geen Git-ervaring nodig

→ [**Bijdrage aanbieden**](https://github.com/security-commons-nl/kennisbank/issues/new?template=bijdrage-aanbieden.md)
  Een document, aanpak of ervaring die je met anderen wilt delen.

→ [**Fout of verbetering**](https://github.com/security-commons-nl/kennisbank/issues/new?template=fout-of-verbetering.md)
  Iets klopt niet, is verouderd, of kan beter.

Vul alleen de vragen in die voor jou relevant zijn — we helpen je met de rest.

**Geen GitHub-account?** [Maak er gratis een](https://github.com/signup) (2 minuten), of vraag iemand in je netwerk om namens jou te posten.

## 2. Meediscussiëren

→ [**Discussions**](../../discussions)

Voor vragen, ervaringen en ideeën zonder directe actie.

## 3. Voor auteurs — direct een document indienen

### Mapstructuur

```
kennisbank/
├── security/    ← informatiebeveiliging (BIO, ISO 27001, NIS2)
├── privacy/     ← privacy en gegevensbescherming (AVG, ISO 27701)
├── bcm/         ← bedrijfscontinuïteit (ISO 22301, BIA)
└── governance/  ← beleid, organisatie, inkoop, bestuur
```

### Vóór indienen

De spelregels staan in het [redactiestatuut](https://github.com/security-commons-nl/.github/blob/main/REDACTIESTATUUT.md); `python tools/build.py --check` controleert ze. Kort:

- **Elk stuk is een map met `README.md`** onder een vakgebied, met de acht vaste frontmatter-velden (titel, vakgebied, type, normen, peildatum of versie, herkomst, status, samenvatting). De indexpagina's worden daaruit gegenereerd.

- **Anonimiseer** het document: geen namen, e-mailadressen, interne systeem-URLs of andere persoonsgegevens. Gebruik de [anonimizer](https://github.com/security-commons-nl/anonimizer-local) of vervang handmatig door functieomschrijvingen.
- **Geen auteursvermelding.** Alles hier komt van vakgenoten; dat hoeft er dus niet bij. Geen `auteur:` in frontmatter, geen kopje "Auteur", geen inzender-vermelding, geen namen in bronverwijzingen ("via X op LinkedIn" wordt "via LinkedIn"). Wel toegestaan als het de lezer helpt: de **herkomst als rol of organisatietype** ("in gebruik bij de CISO-organisatie van een gemeente"). Organisatienamen alleen als de organisatie zelf publiceert of instemt. Wie deelt, hoeft daar zijn naam niet aan te verbinden; dat verlaagt de drempel voor iedereen.
- **Naamgeving**: beschrijvend, zonder spaties, bv. `bia-template-gemeente.docx` of `privacybeleid-voorbeeld.pdf`.
- **Plaatsing**: in de juiste map (zie hierboven).

### Fork → PR

Standaard GitHub-flow. Maintainers beoordelen op:
- Inhoudelijke relevantie
- Anonimisering (geen persoonsgegevens)
- Plaatsing in de juiste map

---

**Organisatiebrede richtlijnen**: [security-commons-nl/.github](https://github.com/security-commons-nl/.github/blob/main/CONTRIBUTING.md)

## 4. Een handleiding toevoegen

Een **handleiding** is een instructie: hoe richt je één maatregel in. Hij hoort bij een of meer
*barrieres* uit de [zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/), zodat
iemand die de zelfcheck heeft gedaan meteen ziet hoe hij een openstaande barriere aanpakt. Een `aanpak`
is iets anders: dat is een methode of een verhaal, die lees je; een handleiding voer je uit.

De koppeling is niet vrijblijvend. Elke handleiding is de bron van *Hoe pak ik het aan* op
[Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/); `tools/build.py`
exporteert dat naar `handelingsperspectief.json` en de aanvalspaden-repo kopieert dat bestand.

### Frontmatter

```yaml
---
titel: Richt centrale logverzameling in
vakgebied: security
type: handleiding
normen: [BIO2]
versie: 2026-09
herkomst: <waar het vandaan komt, als rol of organisatietype>
status: concept
samenvatting: <twee tot vier zinnen: welke barriere, wat je aan het eind hebt staan, welk bewijs dat oplevert>
barrieres: [soc]
rol: fundering
---
```

- **`barrieres`** is verplicht en bevat `vraag_id`'s uit `paden.json` van de aanvalspaden-repo. De build
  controleert of ze bestaan; een verzonnen id blokkeert. Zet die repo naast de kennisbank (in CI gebeurt
  dat vanzelf).
- **`rol`** is `fundering`, `alternatief` of `verdieping`. Meerdere handleidingen mogen dezelfde barriere
  dekken: één fundering, daarnaast alternatieven (vijf manieren om detectie te organiseren) of
  verdiepingen (microsegmentatie naast segmentatie).
- **`pijler`** is optioneel: de mapnaam van het item waar deze handleiding uit voortkomt, bijvoorbeeld
  `meten-voordat-je-ingrijpt`.

### Vaste koppen

De koppen **Bewijs** en **Zo leg je het uit** zijn verplicht; de build blokkeert als ze ontbreken.

```markdown
# <Titel, gelijk aan de frontmatter>

> **Lees de handleiding online:** [security-commons-nl.github.io/kennisbank/security/<mapnaam>](https://security-commons-nl.github.io/kennisbank/security/<mapnaam>/)

> **Barriere:** <titel van de barriere>. <Een zin over wat deze handleiding oplost.>

## Wanneer wel, wanneer niet

## Zo richt je het in

## Wat het kost en wat het oplevert

## Bewijs
Wat je aan het eind kunt laten zien: welke export, rapportage of configuratie. Begin bij het `bewijs`-veld
van de barriere in `paden.json`.

## Zo leg je het uit
**Aan de directie.** ...
**Aan de informatiemanager.** ...
**Aan het MT.** ...

## Hoe dit samenhangt
Verwijs naar de zelfcheck, naar de normverankering, en naar eventuele alternatieven voor dezelfde barriere.

## Licentie
[EUPL-1.2](../../LICENSE).
```

*Bewijs* is er omdat de hele keten op één scheidslijn rust: een antwoord is geen bewijs. *Zo leg je het
uit* is er omdat een CISO een maatregel zelden alleen technisch hoeft te verdedigen.

### Bouwen

```bash
python tools/leesversie.py security/<mapnaam>   # maakt index.html uit README.md
python tools/build.py                           # controleert, bouwt de indexpagina's en de export
```

`leesversie.py` is bedoeld voor nieuwe items. Een paar bestaande leesversies zijn met de hand gemaakt;
overschrijf die alleen als je hebt gekeken wat je kwijtraakt.

Zet de nieuwe map daarna in de lijst onder `## Volgorde` in `security/README.md`; de build blokkeert als
een item daar ontbreekt.

Twee dingen die een aparte workflow controleert en die de build zelf niet vangt:

- De regel met de **live-URL** moet binnen de eerste twintig regels van de README staan. De workflow
  *Live-URL in README* faalt anders, nadat de build al groen was.
- De **leesversie** moet na elke wijziging opnieuw: eerst `leesversie.py`, dan `build.py`. Wijzig je
  alleen de README, dan meldt de build dat de leesversie achterloopt.
