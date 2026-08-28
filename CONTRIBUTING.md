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
