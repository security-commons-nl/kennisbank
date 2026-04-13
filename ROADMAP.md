# kennisbank — Roadmap

> Gedeelde kennisbank voor CISO's en ISO's in de publieke sector.

---

## Huidige staat

Basisstructuur aanwezig (security, privacy, bcm, overig). CI-scanner actief: PRs worden automatisch gecontroleerd op privacygevoelige informatie (adviserende check via anonimizer).

---

## Fase 1 — Vullen met geanonimiseerde documenten

- [ ] Beleidsdocumenten anonimiseren via anonimizer CLI en toevoegen
- [ ] Startset: informatiebeveiliging, AVG/privacy, business continuïteit
- [ ] Naamgevingsconventie vastleggen voor bestandsnamen en mapstructuur
- [ ] README per sectie met uitleg over bijdragen

## Fase 2 — Gestructureerde metadata

- [ ] Frontmatter per document: sector, norm(en), type (beleid/procedure/template), versiedatum
- [ ] Indexpagina per sectie op basis van metadata
- [ ] Zoekbare index via statische sitegeneratie (bijv. mkdocs of docsify)

## Fase 3 — Koppeling met tooling

- [ ] Kennisbank als RAG-bron voor cisochat
- [ ] Kennisbank als normatieve bron voor beleid-assistent
- [ ] Automatische kwaliteitscheck bij PR: volledigheid metadata, anonimisering

---

## Bijdragen

Documenten aanleveren? Gebruik de [anonimizer](https://github.com/security-commons-nl/anonimizer) om ze te anonimiseren voor je een PR opent. Zie [CONTRIBUTING.md](https://github.com/security-commons-nl/.github/blob/main/CONTRIBUTING.md).
