---
titel: Open-source AI binnenhalen onder de Cbw
vakgebied: security
type: aanpak
normen: [Cbw, BIO2, ISO 27001]
versie: 2026-09
herkomst: uitgewerkt vanuit de CISO-praktijk bij gemeenten die een eigen AI-voorziening op open-source componenten opzetten
status: concept
samenvatting: Wie een eigen AI-voorziening bouwt uit open-source onderdelen (chatomgeving, gateway, vectordatabase, open modellen) valt met die keten onder de zorgplicht van de Cyberbeveiligingswet. Zes maatregelen die dat aantoonbaar maken, van componentenlijst en versie-pinning tot een wachttijd voor nieuwe versies, met de LiteLLM-compromittering van maart 2026 als casus.
---

# Open-source AI binnenhalen onder de Cbw

> **Lees de aanpak online:** [security-commons-nl.github.io/kennisbank/security/open-source-ai-binnenhalen](https://security-commons-nl.github.io/kennisbank/security/open-source-ai-binnenhalen/)

Steeds meer gemeenten bouwen een eigen AI-voorziening naast of in plaats van een product van een grote
leverancier. De bouwstenen zijn bijna altijd open source: een chatomgeving voor medewerkers, een gateway
die vragen naar het juiste taalmodel stuurt, een vectordatabase voor de eigen documenten en open modellen
van een publieke modelbank. Dat geeft keuzevrijheid en een exitroute. Het betekent ook dat er geen
leverancier is die de keten voor je bewaakt. Tussen de ontwikkelaar van een pakket en jouw server staat
niemand, behalve jij.

Sinds 15 augustus 2026 is het bewaken van die keten een wettelijke plicht. De Cyberbeveiligingswet vraagt maatregelen voor de
beveiliging van de toeleveringsketen en voor beveiliging bij het verwerven, ontwikkelen en onderhouden van
systemen (art. 21 lid 3 onder d en e). De Cyberbeveiligingsregeling sector overheid legt de lat bij de
BIO2 en eist dat opzet, bestaan en werking van de maatregelen **aantoonbaar** zijn (art. 5 lid 3). Een
AI-stack die je met een paar installatiecommando's hebt binnengehaald, voldoet daar niet aan.

## De casus: LiteLLM, 24 maart 2026

LiteLLM is een veelgebruikte open-source gateway die één ingang geeft naar tientallen taalmodellen. Op
24 maart 2026 verschenen om 10:39 UTC twee kwaadaardige versies (1.82.7 en 1.82.8) in de publieke
pakketbank PyPI. Na ongeveer veertig minuten haalde PyPI ze offline.

1. **De ingang was een beveiligingsscanner.** De aanvaller kwam aan de publicatiesleutels van het project
   via een gecompromitteerde scanner in de eigen bouwstraat van LiteLLM. Het gereedschap dat de keten
   moest bewaken, was de zwakke schakel.
2. **De buit waren sleutels.** De code zocht omgevingsvariabelen, SSH-sleutels, cloudsleutels,
   Kubernetes-tokens en databasewachtwoorden en stuurde ze naar een domein dat op dat van het project
   leek. Een AI-gateway is daarvoor een ideale plek: hij houdt de API-sleutels van alle modelaanbieders
   tegelijk vast.
3. **Wie had gepind, had geen last.** De officiële container van LiteLLM zette alle afhankelijkheden op
   een vaste versie en was niet geraakt. Getroffen waren installaties die zonder versienummer de nieuwste
   versie ophaalden, direct of via een ander pakket.

Pinnen is niet het hele verhaal. Tussen april en september 2026 verschenen voor hetzelfde pakket zestien
beveiligingsadviezen voor gewone kwetsbaarheden: authenticatie-omzeiling, SQL-injectie, het uitvoeren van
commando's. Wie op één versie blijft staan, verzamelt die gaten. Je moet dus allebei kunnen: vastzetten wat
er draait, en in een vast ritme gecontroleerd bijwerken.

## Zes maatregelen

1. **Een componentenlijst per voorziening.** Leg per AI-voorziening vast uit welke pakketten, containers
   en modellen zij bestaat, met versie en bron. Dat is de SBOM (software bill of materials). Genereer hem
   bij elke nieuwe versie van de voorziening, met gereedschap als
   [Syft](https://github.com/anchore/syft), en neem de modellen erin op: naam, versie of hash, en de bron
   waar je ze vandaan haalde. Zonder deze lijst kun je bij een melding als die van LiteLLM niet binnen een
   uur zeggen of je geraakt bent.
2. **Alles op een vaste versie, met hash.** Geen `latest`, geen versiebereik. Pakketten via een lockfile
   met hashes (`pip install --require-hashes`, of `uv lock`), containers op digest (`@sha256:...`) in
   plaats van op tag. Dan draait er alleen wat je hebt gezien, ook als iemand onder dezelfde naam iets
   anders publiceert.
3. **Herkomst controleren voordat je installeert.** Kijk of het project zijn uitgaven ondertekent en
   controleer die handtekening, bijvoorbeeld met [cosign](https://github.com/sigstore/cosign) voor
   containers. Haal modellen alleen bij de uitgever zelf vandaan en kies voor het `safetensors`-formaat.
   Oudere modelformaten kunnen bij het laden code uitvoeren.
4. **Een wachttijd voor nieuwe versies.** Laat een nieuwe versie pas toe als hij een paar dagen oud is.
   Kwaadaardige versies worden vaak binnen uren tot dagen ontdekt en teruggetrokken; LiteLLM stond veertig
   minuten online. Een wachttijd van zeven dagen had hem tegengehouden. Updategereedschap kan dit
   afdwingen: [`minimumReleaseAge`](https://docs.renovatebot.com/configuration-options/#minimumreleaseage)
   in Renovate, [`exclude-newer`](https://docs.astral.sh/uv/reference/settings/#exclude-newer) in uv.
   Beveiligingsupdates voor een actief misbruikte kwetsbaarheid gaan met een bewuste uitzondering voor.
5. **Bijwerken in een vast ritme.** Koppel de componentenlijst aan een bron van beveiligingsadviezen,
   zoals [OSV](https://osv.dev/) of de GitHub Advisory Database, en behandel een advies voor een AI-component
   zoals elk ander: binnen de termijnen van je patchbeleid. Test een update eerst buiten productie. De
   wachttijd uit maatregel 4 en dit ritme bijten elkaar niet: de wachttijd bepaalt wanneer een versie
   mag, het ritme bepaalt dat hij er ook komt.
6. **Ga ervan uit dat een component ooit kwaadaardig is.** Beperk wat hij dan kan. Geef de gateway alleen
   de sleutels die hij nodig heeft, met een korte looptijd en een limiet op kosten. Houd sleutels uit de
   bouwstraat. Laat de AI-servers alleen verbinden met de modelaanbieders die je gebruikt; de
   LiteLLM-code stuurde zijn buit naar een extern domein, en een uitgaand verbod had dat geblokkeerd.

## Wanneer wel, wanneer niet

Deze aanpak geldt voor alles wat je zelf installeert en beheert: een eigen chatomgeving, een eigen gateway,
open modellen op eigen of gehuurde servers. Neem je de hele voorziening af als dienst, dan verschuift het
werk naar de leverancier en naar je contract. Vraag dan om de componentenlijst, de updatetermijnen en een
meldplicht bij compromittering, bijvoorbeeld via de [security-annex voor leveranciers](../security-annex-leveranciers/).
Een samenwerkingsverband dat voor meerdere gemeenten een voorziening beheert, zit voor de deelnemers in die
tweede rol en moet het werk dus zelf doen.

## Bewijs

Dit laat je zien als een toezichthouder of auditor vraagt hoe je de keten beheerst. De nummers zijn die
van ISO 27002:2022, die de BIO2 volgt.

- De componentenlijst van de draaiende versie, met datum, inclusief modellen (5.21, 8.19).
- De lockfile en de containerdefinities met hashes of digests, in versiebeheer (8.19, 8.32).
- De lijst met toegestane bronnen voor pakketten, containers en modellen, met eigenaar (5.21).
- De ingestelde wachttijd, en de uitzonderingen die daarop zijn gemaakt, met reden (8.32).
- Een overzicht van beveiligingsadviezen voor AI-componenten in het afgelopen kwartaal, met per advies de
  datum van de update of de reden om te wachten (8.8).
- De netwerkregels die uitgaand verkeer van de AI-servers beperken (8.20, 8.22).

## Zo leg je het uit

Aan een bestuurder: "Onze AI-voorziening bestaat uit onderdelen die vrijwilligers en bedrijven wereldwijd
publiceren. In maart zat er in zo'n onderdeel veertig minuten lang code die wachtwoorden stal. Wie op een
vaste, gecontroleerde versie zat, merkte niets. Wij zorgen dat wij bij die groep horen, en de wet vraagt
dat wij dat kunnen aantonen."

## Hoe dit samenhangt

De componentenlijst is een verfijning van [Ketenafhankelijkheden in beeld](../ketenafhankelijkheden/) voor
de AI-keten. Het bijwerkritme hoort bij [Kwetsbaarheden scannen en opvolgen](../kwetsbaarheden-scannen/). Wat een AI-agent
met de sleutels van de gateway mag, staat in [Wiens bevoegdheid gebruikt een AI-agent?](../agent-bevoegdheid/).
Gaat het toch mis, dan staat in [Wanneer meld je een AI-incident?](../ai-incident-melden/) welke meldplicht
geldt.

## Bronnen

- [Cyberbeveiligingswet](https://wetten.overheid.nl/BWBR0052872/), art. 21 lid 3 onder d en e (zorgplicht, toeleveringsketen)
- [Cyberbeveiligingsregeling sector overheid](https://wetten.overheid.nl/BWBR0052963/), art. 5 (ISO 27002 en BIO2, aantoonbaarheid)
- [GitHub Advisory GHSA-5mg7-485q-xm76](https://github.com/advisories/GHSA-5mg7-485q-xm76): twee LiteLLM-versies met malware die inloggegevens verzamelt
- [LiteLLM, security update maart 2026](https://docs.litellm.ai/blog/security-update-march-2026): tijdlijn, oorzaak en de niet-geraakte container
- [OSV](https://osv.dev/list?ecosystem=PyPI&q=litellm): de beveiligingsadviezen voor LiteLLM, peildatum 25 september 2026

## Licentie

[EUPL-1.2](../../LICENSE).
