---
titel: Copilot en vergelijkbare assistenten, de configuratiekeuzes
vakgebied: security
type: aanpak
normen: [BIO2, AVG, AI Act]
peildatum: 2026-11-19
herkomst: CISO-praktijk bij gemeenten, naar aanleiding van een VNG-webinar over de beveiliging van AI
status: concept
route: geen
bronnen: [ibd-notitie-dpia-copilot, ibd-handreiking-ai-en-algoritmen, vng-kenniskaart-monitoring-ai]
samenvatting: De voorwaarden van Microsoft Copilot zijn niet te onderhandelen, de inrichting wel. Zes keuzes die je als organisatie zelf zet, met per keuze wat het afdekt en wat het kost - webzoeken via Bing aan of uit, gevoeligheidslabels en DLP (ook tegen promptinjectie via externe mail), wat Copilot kan vinden (oversharing), agents en connectoren, AI-modellen van derden als subverwerker, en logging. Met de volgorde waarin je ze aanpakt en het bewijs dat je kunt laten zien.
---

# Copilot en vergelijkbare assistenten, de configuratiekeuzes

> **Lees de aanpak online:** [security-commons-nl.github.io/kennisbank/security/copilot-configuratiekeuzes](https://security-commons-nl.github.io/kennisbank/security/copilot-configuratiekeuzes/)

"Staat de webzoekfunctie via Bing bij jullie aan of uit, en hoe maken jullie die afweging?" Die vraag kwam
in een VNG-webinar over de beveiliging van AI, en hij is typerend. De voorwaarden van een grote
AI-assistent zijn eenzijdig: je tekent of je tekent niet. Wat je wel zelf bepaalt, is de inrichting. Dit
stuk zet de keuzes op een rij die je als organisatie zelf maakt, met per keuze wat het afdekt en wat het
kost. Het voorbeeld is Microsoft Copilot, omdat dat bij de meeste overheidsorganisaties al in de tenant
zit; de vragen gelden voor elke assistent die in je kantooromgeving meedraait.

Microsoft wijzigt namen, standaardwaarden en menu's vaak. De keuzes hieronder zijn gecontroleerd op de
peildatum van dit stuk; loop ze elk kwartaal na.

## Eerst: welke Copilot

Er zijn er drie, en ze verschillen in wat ze zien en onder welke voorwaarden ze draaien.

| Variant | Wat hij ziet | Voorwaarden |
|---|---|---|
| **Microsoft 365 Copilot**, met licentie (Microsoft noemt hem ook Microsoft Copilot) | Alles in Microsoft 365 waar de gebruiker zelf bij kan: mail, chats, bestanden, sites | Productvoorwaarden en verwerkersovereenkomst van de tenant, *enterprise data protection* |
| **Copilot Chat**, zonder extra licentie | Het web en wat de gebruiker zelf in het gesprek zet of uploadt; geen mail of bestanden uit de tenant | Ook binnen de tenantvoorwaarden en *enterprise data protection*, als de gebruiker met zijn werkaccount is ingelogd |
| **Consumentenversie**, met een persoonlijk account | Wat de gebruiker erin plakt | Consumentenvoorwaarden, buiten de tenant |

Het gesprek over configuratie gaat over de eerste twee. De derde regel je met beleid, met blokkeren op
de werkplek of met beide. Weet je niet welke van de drie er bij jou gebruikt worden, begin dan daar:
[AI-gebruik in beeld](https://security-commons-nl.github.io/ai-gebruik-in-beeld/) meet het uit de
logging die je al hebt. "Copilot staat in de tenant" is nog geen besluit dat het gebruikt mag worden; de
autorisatie is een aparte stap, net als bij elke andere dienst.

## De zes keuzes

### 1. Webzoeken via Bing

**Wat het is.** Copilot en Copilot Chat kunnen een antwoord aanvullen met resultaten van Bing. Copilot
stuurt daarvoor een korte zoekvraag van een paar woorden, afgeleid uit de prompt, met het IP-adres van de
gebruiker. Niet de hele prompt en niet het document, maar werkt de gebruiker in Word met een document open,
dan kan de zoekvraag wel termen uit dat document bevatten.

**Wat je moet weten.** Voor die zoekvragen is Microsoft zelf verwerkingsverantwoordelijke. De
verwerkersovereenkomst (DPA) en de EU Data Boundary gelden er niet voor; de productvoorwaarden geven wel
aanvullende toezeggingen (niet voor advertenties, niet voor training). Zet je niets in, dan staat
webzoeken aan.

**Wat je zet.** De beleidsregel *Allow web search in Copilot* in de Cloud Policy service van Microsoft 365,
per gebruiker of groep: aan, uit, of uit in de werkmodus van Copilot en aan voor de webmodus en Copilot
Chat. Staat het aan, dan kan de gebruiker het zelf nog uitzetten; staat het uit, dan niet.

**De afweging.** Uit voor groepen die met dossiers over personen werken (sociaal domein, handhaving,
burgerzaken), aan voor de rest is een verdedigbare middenweg. Een fijnere weg is de DLP-regel onder keuze
2: webzoeken blijft aan, maar valt weg zodra een prompt gevoelige gegevens bevat. **Kost:** minder actuele
antwoorden voor wie het uit heeft, en een extra beleidsregel om bij te houden.

### 2. Gevoeligheidslabels en DLP

**Wat het is.** Microsoft Purview kan een DLP-beleid op Copilot zelf zetten. Vier mogelijkheden:
een prompt met gevoelige informatietypen (een BSN-patroon, een eigen type) wordt niet verwerkt; bij zo'n
prompt valt webzoeken weg; bestanden en mails met een bepaald gevoeligheidslabel worden niet gebruikt
voor een antwoord; en mail van buiten de organisatie wordt niet als bron gebruikt (bij de peildatum nog
een preview).

**Wat het afdekt.** Lekken via de prompt, en het ophalen van gelabelde stukken in een antwoord. De
laatste mogelijkheid dekt ook een deel van prompt-injectie af: een externe mail met verborgen instructies
komt dan niet in het antwoord terecht.

**Kost.** Werkt alleen als de labels er zijn en gebruikt worden; een labelbeleid op papier dekt niets
af. Hangt af van je licentie. En elke regel die vaak vuurt, wordt een melding die niemand leest: begin
met een paar typen die er echt toe doen.

### 3. Wat Copilot kan vinden

**Wat het is.** Copilot met licentie ziet alles waar de gebruiker al bij kan. Te ruime rechten op
SharePoint-sites en Teams, die nu niemand opvallen omdat niemand ernaar zoekt, worden met Copilot
vindbaar. Dat heet *oversharing* en het is bij de meeste organisaties het grootste risico van de invoering.

**Wat je zet.** Tijdelijk: *Restricted Content Discovery* per SharePoint-site haalt de site uit de
organisatiebrede zoekresultaten en uit Copilot, zonder rechten te wijzigen. Blijvend: de rechten zelf
opruimen, te beginnen bij de sites met de gevoeligste inhoud.

**Kost.** De tijdelijke maatregel maakt antwoorden minder volledig en wordt makkelijk permanent. Zet er
een einddatum op en koppel hem aan het opruimen. Het opruimen zelf is het echte werk; zie
[Rechten in de cloud terugbrengen tot gebruik](../least-privilege-cloud/).

### 4. Agents en connectoren

**Wat het is.** Copilot kan worden uitgebreid met agents (in Copilot Studio of kant-en-klaar) en met
connectoren die data van buiten Microsoft 365 binnenhalen. Een agent kan namens de gebruiker handelen; een
connector maakt een nieuwe bron doorzoekbaar.

**Wat je zet.** In het beheercentrum van Microsoft 365 wie agents en apps mag toevoegen, welke er
beschikbaar zijn en voor wie. Begin met: gebruikers installeren niets zelf, beheer voegt toe na een korte
toets.

**De toets.** Op wiens bevoegdheid handelt de agent, welke data haalt hij binnen, en wie keurt hem. Zie
[Wiens bevoegdheid gebruikt een AI-agent?](../agent-bevoegdheid/) en het
[keuzeblad bij de inzet van een agent](../ai-inzet-keuzeblad/). **Kost:** een aanvraagroute en iemand die
toetst.

### 5. AI-modellen van derden als subverwerker

**Wat het is.** Microsoft biedt in Copilot naast de eigen modellen ook modellen van andere aanbieders aan,
waaronder de Claude-modellen van Anthropic, die daarvoor subverwerker van Microsoft zijn geworden.

**Wat je moet weten.** Op de peildatum vallen die modellen buiten de EU Data Boundary. Voor organisaties in
de EU staan ze standaard uit, maar er komen aparte schakelaars bij voor afzonderlijke onderdelen, en een
schakelaar die standaard uit staat kan door een beheerder met één klik aan.

**Wat je zet.** In het beheercentrum van Microsoft 365, onder Copilot, de instelling voor AI-aanbieders als
subverwerker: aan of uit, en zo ja voor welke gebruikers of groepen. Leg de keuze vast als besluit, met de
DPIA erbij, en controleer elk kwartaal of er een schakelaar is bijgekomen.

### 6. Logging

**Wat het is.** Staat auditing in de tenant aan, dan legt Purview Audit de interacties met Copilot
vanzelf vast, inclusief de zoekvragen die naar Bing gingen. Gebruik van AI-toepassingen van andere
leveranciers wordt apart en tegen betaling gelogd.

**Wat je zet.** Controleer dat auditing aan staat, stuur de Copilot-gebeurtenissen door naar je
[centrale logverzameling](../centrale-logverzameling/) en kies een bewaartermijn die past bij je
[bewaartermijnen voor logging](../logging-en-retentie/). Bepaal vooraf wie de inhoud van prompts mag
inzien: dat zijn gesprekken van medewerkers, dus de FG hoort bij die afspraak.

**Kost.** Opslag, en een afspraak over inzage. Zonder logging kun je bij een incident of een verzoek van
een betrokkene niet navertellen wat er gebeurd is.

## Volgorde

1. Meet wat er nu gebruikt wordt, alle drie de varianten.
2. Zet de logging aan en stuur hem door, zodat alles hierna meetbaar is.
3. Besluit over webzoeken, per groep.
4. Pak oversharing aan op de sites met de gevoeligste inhoud, met een tijdelijke beperking waar het niet
   snel kan.
5. Zet DLP op een paar gevoelige informatietypen en op de labels die je echt gebruikt.
6. Sluit het zelf toevoegen van agents en connectoren af en richt een aanvraagroute in.
7. Controleer elk kwartaal de subverwerkers en de nieuwe schakelaars.

## Bewijs

- Het besluit over welke Copilot-varianten gebruikt mogen worden, met de DPIA.
- De ingestelde beleidsregel voor webzoeken, per groep, met de afweging.
- Het DLP-beleid voor Copilot en de lijst informatietypen en labels die het afdekt.
- De lijst sites met een tijdelijke beperking, met einddatum en eigenaar.
- De instelling voor agents, apps en subverwerkers, met de datum van de laatste controle.
- Een voorbeeld van een Copilot-gebeurtenis in de centrale logverzameling.

## Wat dit stuk niet doet

Het zegt niet welke keuze goed is: dat hangt af van wat je organisatie verwerkt en wat de DPIA zegt. Voor
de privacybeoordeling van Copilot zelf heeft de IBD een notitie; zie de bronnen onderaan. En het dekt de
voorwaarden niet af: die blijven eenzijdig. Wat je met inrichting niet kunt regelen, regel je in de
[Security Annex voor leveranciers](../security-annex-leveranciers/) of het hoort in de afweging of je het
gebruikt.

## Hoe dit samenhangt

Dit stuk is de praktische kant van "verdediging van AI" voor organisaties die AI inkopen in plaats van zelf
bouwen; wie zelf bouwt, kijkt bij [Open-source AI binnenhalen onder de Cbw](../open-source-ai-binnenhalen/).
Meten wat er gebruikt wordt: [AI-gebruik in beeld](https://security-commons-nl.github.io/ai-gebruik-in-beeld/).
Agents: [Wiens bevoegdheid gebruikt een AI-agent?](../agent-bevoegdheid/) en het
[keuzeblad bij de inzet van een agent](../ai-inzet-keuzeblad/). Gaat het mis:
[Wanneer meld je een AI-incident?](../ai-incident-melden/).

## Documentatie van de leverancier

Gecontroleerd op de peildatum.

- [Webzoeken in Copilot en Copilot Chat: gegevens, privacy en beheer](https://learn.microsoft.com/en-us/copilot/microsoft-365/manage-public-web-access)
- [Enterprise data protection in Copilot](https://learn.microsoft.com/en-us/copilot/microsoft-365/enterprise-data-protection)
- [DLP voor Microsoft 365 Copilot en Copilot Chat](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about)
- [Restricted Content Discovery voor SharePoint-sites](https://learn.microsoft.com/en-us/sharepoint/restricted-content-discovery)
- [Agents en apps beheren in het beheercentrum](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-copilot-agents-integrated-apps)
- [Claude-modellen van Anthropic als subverwerker in Copilot](https://learn.microsoft.com/en-us/copilot/microsoft-365/connect-to-ai-subprocessor)
- [Auditlogging voor Copilot en AI-toepassingen](https://learn.microsoft.com/en-us/purview/audit-copilot)

## Licentie

[EUPL-1.2](../../LICENSE).
