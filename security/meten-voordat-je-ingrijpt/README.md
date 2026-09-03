---
titel: Meten voordat je ingrijpt
vakgebied: security
type: aanpak
normen: [BIO2]
barrieres: [execution, mail, legacy, session, consent, segment, edr]
versie: 2026-08
herkomst: gegeneraliseerd uit een casus bij een gemeentelijke organisatie
status: in gebruik
samenvatting: De methode om je security posture te verhogen met data uit je eigen omgeving in plaats van met aannames: meet eerst wat er feitelijk draait, bepaal daarna pas wat je afdwingt. Dat voorkomt dat je legitiem werk breekt en laat de echte impact zien, meestal kleiner dan gedacht. Dit stuk geeft de drie uitgangspunten, de werkwijze van IST naar SOLL en de volgorde; de uitwerking per laag staat in de handleidingen die eronder hangen.
---

# Meten voordat je ingrijpt

> **Lees dit stuk online:** [security-commons-nl.github.io/kennisbank/security/meten-voordat-je-ingrijpt](https://security-commons-nl.github.io/kennisbank/security/meten-voordat-je-ingrijpt/)

**De aanval waar dit mee begon.** Bij ClickFix laat een nagemaakte pagina de gebruiker zelf een commando
plakken en uitvoeren, meestal via Win+R of PowerShell. Geen exploit, geen bijlage: de gebruiker doet het
werk. Wat daarna komt is een infostealer of remote access tool, en uiteindelijk exfiltratie.

De verleiding is dan om meteen te blokkeren: Win+R uit, PowerShell dicht. Dat is precies waar dit stuk
tegen waarschuwt. Bij een gemeentelijke organisatie bleek van miljoenen PowerShell-starts in een maand
bijna 99 procent machine-automatisering, waaronder de sensor van de eigen endpointbescherming. Een botte
blokkade had de eigen beveiliging gebroken.

Vandaar de aanpak: meet eerst wat er feitelijk draait, bepaal dan wat je afdwingt. ClickFix is het
vertrekpunt, maar de werkwijze is breder toepasbaar: van de werkplek tot het netwerk, en van detectie tot
de vraag wat er in je omgeving feitelijk gebeurt.

Dit stuk bevat de methode: waarom je eerst meet, en in welke volgorde. De uitwerking per laag staat in
eigen stukken die hierboven staan opgesomd, en het bestuurlijke deel (regie, strategie, besluitvorming)
in [Sturen op weerbaarheid](../sturen-op-weerbaarheid/).

Een deel van dit meetwerk is inmiddels gereedschap. De
[meting](https://security-commons-nl.github.io/aanvalspaden/meting/) leest exports die je al hebt
(firewallconfig, nmap, Nessus, Entra, backup, een Linux-dump) en toetst ze aan 41 regels, in je eigen
browser. Wat daar niet uit te halen is, heet daar een witte vlek; dat is precies waar dit stuk over
gaat, want die vlekken vul je met de werkwijze hieronder en niet met een aanname.

> Gegeneraliseerd uit een concrete casus. Pas de voorbeelden aan op je eigen organisatie, leveranciers en
> tenant. Let bij maatregelen die verkeer of gebruik inzichtelijk maken (zoals TLS-decryptie of
> script-logging) op privacy, BIO2 en eventuele medezeggenschapstrajecten.

## Wat je hier vindt

Dit stuk bevat de methode. De uitwerking per laag staat in eigen stukken, zodat je kunt lezen wat voor
jou geldt zonder de rest door te hoeven.

| Wil je dit | Voor wie | Ga naar |
|---|---|---|
| De werkwijze begrijpen: meten, IST naar SOLL, aantoonbaarheid | Allen | [De methode](#de-methode-evidence-based-posture-verhogen), hieronder |
| Meten wat er feitelijk draait op de werkplek, met KQL | Security, beheer | [Werkplekanalyse op het Microsoft-platform](../werkplekanalyse-e5/) |
| Identiteit en e-mail toetsen voordat je afdwingt | Security, beheer | [Identiteit en e-mail meten](../identiteit-en-mail-meten/) |
| Uit de data zien of je netwerk werkelijk segmenteert | Security, netwerk | [Netwerk en firewall analyseren uit data](../netwerkanalyse-uit-data/) |
| Je controls naast de volledige aanvalsketen leggen | Security | [De killchain naast je controls](../killchain-naast-je-controls/) |
| Weten waarop je stuurt: regie, RACI, lockdown of faciliteren | Bestuur, directie, CISO | [Sturen op weerbaarheid](../sturen-op-weerbaarheid/) |

## Drie uitgangspunten

1. **Meet voordat je ingrijpt.** Stel het feitelijke gebruik vast voordat je iets beperkt. Dat voorkomt
   uitval en laat zien hoe groot de impact werkelijk is, meestal kleiner dan gedacht.
2. **Vertrouw op data, niet op tekeningen.** Een netwerktekening of een "we hebben het aanstaan" is een
   aanname. Toets de werkelijkheid: rule-hits, configuratie-export, telemetrie.
3. **Aangezet is niet hetzelfde als beheerd.** Een tool met standaardconfiguratie die niemand bijhoudt,
   beschermt niet aantoonbaar. Leg bestaan, opzet, werking en eigenaarschap vast.

## Volgorde van aanpak

1. Meet de werkplek: wat draait er echt, wie gebruikt wat.
   [Werkplekanalyse](../werkplekanalyse-e5/).
2. Toets identiteit en e-mail: aan staan is niet hetzelfde als gekoppeld en actief.
   [Identiteit en e-mail meten](../identiteit-en-mail-meten/).
3. Analyseer netwerk en firewall uit data: brede regels, beheertoegang, zicht, segmentatie.
   [Netwerk en firewall analyseren uit data](../netwerkanalyse-uit-data/).
4. Leg de killchain naast je controls: waar knijp je, waar zit een gat.
   [De killchain naast je controls](../killchain-naast-je-controls/).
5. Beleg regie en resultaatverplichting, en kies een strategie.
   [Sturen op weerbaarheid](../sturen-op-weerbaarheid/).

## De methode: evidence-based posture verhogen

Deze aanpak is opzettelijk nuchter. Geen catchy oneliners, wel toetsbare stappen.

### Drie principes

#### 1. Meet voordat je ingrijpt
Voordat je een maatregel afdwingt (Win+R uit, PowerShell beperken, een firewallregel versmallen), stel je het
feitelijke gebruik vast. Dat doet twee dingen: het laat de werkelijke impact zien (meestal kleiner dan gevreesd)
en het voorkomt dat je legitiem werk of beheer breekt. Een voorbeeld uit de praktijk: van miljoenen
PowerShell-starts in een maand bleek bij een gemeente bijna 99% machine-automatisering - waaronder de eigen sensor 
van de endpointbescherming. Een botte blokkade had de eigen beveiliging gebroken.

#### 2. Vertrouw op data, niet op tekeningen
Een netwerktekening toont de bedoeling, niet de werkelijkheid. "We hebben ASR aanstaan" is een aanname totdat
je de koppeling aan een gebruikersgroep hebt geverifieerd. Toets met:
- telemetrie (Advanced Hunting, logs);
- configuratie-export (firewallregels, hit-counts, routeringstabellen);
- de daadwerkelijke koppeling/scope van een beleidsregel.

#### 3. Aangezet is niet hetzelfde als beheerd
Toets elke maatregel op vier niveaus van oplopende zekerheid:

| Niveau | Vraag |
|---|---|
| **Bestaan** | Is de maatregel aanwezig? |
| **Opzet** | Is hij correct ingericht volgens norm? |
| **Werking** | Is hij aantoonbaar effectief in de praktijk? |
| **Config beschikbaar** | Kunnen wíj de instelling zelf inzien? |

### Managed dienstverlening is meer dan de aanknop indrukken
Een "managed" dienst omvat gedurende de hele levenscyclus: bijhouden (updates, dreigingsinfo), beheren
(configuratie, afwijkingen, prestaties), optimaliseren, functionaliteit aanpassen, en verantwoorden
(rapportage, eigenaarschap). Een tool installeren met standaardinstellingen is daarvan alleen de eerste stap.
Als de dienstverlening managed is gecontracteerd dan is de optielijst klein, een fireall waar de regelset
niet periodiek wordt gevalideerd en voorzien wordt van een risicoletter aan de klant waar nodig is **geen managed** 
dienst.

### IST → SOLL als werkvorm

Beschrijf per component de huidige stand (IST) en de gewenste stand (SOLL), met een statuskleur en een
actiehouder. Houd de SOLL-ambitie expliciet: een verdedigbare ondergrens (richting BIO2 en audit) is iets
anders dan "best-practice". Maak die keuze bewust, anders overvraag je de organisatie.

Sjabloon:

| Component | IST (stand + bewijs) | SOLL | Statuskleur | Actiehouder |
|---|---|---|---|---|
| _bijv. ASR-regels_ | _2 regels, niet gekoppeld_ | _block-modus, juiste groep, incl. LSASS_ | rood | _beheerpartner werkplek_ |

Statuskleuren: groen = ingericht · oranje = deels/aandacht · rood = nog niet ingericht · grijs = te bevestigen.

### Volgorde

1. **[Meet de werkplek](../werkplekanalyse-e5/).** Daar is de meeste telemetrie en de meeste laaghangende winst.
2. **Toets de configuratie** op [de werkplek](../werkplekanalyse-e5/) en bij [identiteit en e-mail](../identiteit-en-mail-meten/). Onderscheid "aan" van "gekoppeld en actief".
3. **[Analyseer netwerk en firewall uit data](../netwerkanalyse-uit-data/).** Brede regels, beheertoegang, zicht op verkeer, segmentatie.
4. **[Leg de killchain naast je controls](../killchain-naast-je-controls/).** Waar knijp je de aanval, waar zit nog een gat.
5. **[Beleg regie en kies een strategie](../sturen-op-weerbaarheid/).**

### Aantoonbaarheid en herijking

Leg vast wat je hebt gemeten en wanneer. Een maatregel die ooit aanstond kan weer afvallen (drift). Plan
periodieke herijking en, waar mogelijk, een gecontroleerde aanvalssimulatie om detectie en preventie te
toetsen - niet aannemen dat het werkt, maar het laten zien.

## Herbruikbare query's

De zes KQL-query's voor Advanced Hunting staan bij de handleiding waar ze bij horen:
[Werkplekanalyse op het Microsoft-platform](../werkplekanalyse-e5/). Daar staat per query waarvoor hij
dient (ClickFix-detectie, Win+R-gebruik, PowerShell-categorisatie, mshta) en hoe je de parent-processen en
uitsluitingen op je eigen omgeving aanpast.

## Werken met een LLM

Dit stuk is geschreven om mee te werken in een taalmodel. Neem de tekst en de query's mee als context, en
laat het model je helpen bij het categoriseren van je eigen meetresultaten en het invullen van de IST/SOLL-
en RACI-sjablonen.

Weeg wel af wat je waar doet. Kun je het zelf, prima. Heb je een lokaal model op geschikte hardware, doe
het daarin. Anders is het een risicoafweging: wat is het risico van het niet gebruiken van een model tegen
het risico dat je meetgegevens bij een aanbieder terechtkomen? Zet je meetresultaten liever geanonimiseerd
in, en houd de uitkomsten onder versiebeheer zodat de verbetering aantoonbaar en herhaalbaar blijft.

## Hoe dit samenhangt met de andere stukken

| Wil je | Ga naar |
|---|---|
| Weten welke aanvalspaden bij jou openstaan, in een uur | [Zelfcheck aanvalspaden](https://security-commons-nl.github.io/aanvalspaden/) |
| Dit meten in plaats van invullen: 41 regels op exports die je al hebt | [Meting](https://security-commons-nl.github.io/aanvalspaden/meting/) |
| Die uitkomst omzetten in een risicolijst met eigenaar | [Risicoanalyse langs aanvalspaden](../risicoanalyse-aanvalspaden/) |
| De rode cellen structureel dichten met mandaat | [Een blue team opzetten](../blue-team-opzetten/) |
| AI-gebruik in je organisatie feitelijk meten | [AI-gebruik in beeld](https://security-commons-nl.github.io/ai-gebruik-in-beeld/) |
| Weten wat je met dit alles aantoont in BIO 2.0, NIST CSF, Wpg of AVG | [Van aanvalspad naar norm](https://security-commons-nl.github.io/aanvalspaden/normen/) |

## Herkomst

Gegeneraliseerd uit een concrete casus bij een gemeentelijke organisatie, ingebracht in de commons. De
voorbeelden en aantallen komen uit die casus; de aanpak is bedoeld om over te nemen, niet om na te doen.

## Licentie

EUPL-1.2, zie de [licentie van de kennisbank](../../LICENSE).
