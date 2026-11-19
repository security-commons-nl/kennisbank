---
titel: Keuzeblad bij de inzet van een AI-agent
vakgebied: security
type: aanpak
normen: [BIO2, AVG, AI Act]
versie: 2026-11
herkomst: CISO-praktijk bij gemeenten, naar aanleiding van een VNG-webinar over de beveiliging van AI
status: concept
route: geen
bronnen: [bzk-algoritmekader, ibd-fg-gesprekskaart-ai-en-algoritmen, vng-kenniskaart-inkoopvoorwaarden-ai, ibd-handreiking-ai-en-algoritmen]
samenvatting: Acht vragen die je beantwoordt voordat een AI-agent aan het werk gaat - welk probleem het oplost, waar het draait, open of gesloten model, welke data erin gaat en wat nooit, welke bevoegdheid, wie de agent keurt, wanneer je stopt, en wat het kost tegenover wat het bespaart. Als invulblad dat je per agent bewaart, zodat de inzet een besluit met onderbouwing is.
---

# Keuzeblad bij de inzet van een AI-agent

> **Lees de aanpak online:** [security-commons-nl.github.io/kennisbank/security/ai-inzet-keuzeblad](https://security-commons-nl.github.io/kennisbank/security/ai-inzet-keuzeblad/)

Een agent is snel gebouwd en nog sneller aangezet. Het besluit om hem in te zetten wordt daardoor vaak
niet genomen: hij draait gewoon. Dit keuzeblad maakt van de inzet een besluit. Acht vragen, elk met de
afweging erbij, en een invulblad dat je per agent bewaart. Het blad geldt voor elke agent, ook voor de
[agent-patronen voor beveiligingswerk](../agent-patronen-beveiliging/).

Het risico van achterlopen is ook een risico. Een spreker van de IBD zei het in een VNG-webinar over de
beveiliging van AI zo: weeg het risico van hoe je AI inzet tegen het risico dat je achterloopt. Het blad
is er om de inzet te onderbouwen, niet om hem tegen te houden.

## De acht vragen

### 0. Welk probleem lost het op?

Vóór alle andere vragen. Welke taak, voor wie, en hoeveel tijd kost die taak nu? Zonder antwoord heb je
een oplossing die een probleem zoekt, en dan zijn de vragen hieronder verspilde moeite.

### 1. Waar draait het?

Lokaal op een eigen apparaat, in de eigen tenant, of in de cloud van een derde. Lokaal houdt de data
binnen maar vraagt beheer en is vaak minder krachtig; de eigen tenant valt onder de voorwaarden die je al
hebt; de cloud van een derde vraagt een eigen beoordeling van de aanbieder. Zie voor de assistent in de
kantooromgeving [Copilot, de configuratiekeuzes](../copilot-configuratiekeuzes/).

### 2. Open of gesloten model?

Bij een open model bepaal je zelf de versie, en dus ook wanneer je bijwerkt: pin de versie en houd een
wachttijd aan voordat een nieuwe versie in gebruik gaat, zoals in
[Open-source AI binnenhalen onder de Cbw](../open-source-ai-binnenhalen/). Bij een gesloten model wisselt
de aanbieder het model wanneer hij wil; vraag of hij dat aankondigt en neem het op in de
[Security Annex](../security-annex-leveranciers/).

### 3. Welke data gaat erin, en wat nooit?

Schrijf beide op. Wat er nooit in gaat, is minstens zo belangrijk: geen persoonsgegevens als de taak ze
niet nodig heeft, en geen informatie over je eigen infrastructuur (netwerktekeningen, configuraties,
kwetsbaarheden) in een agent die buiten je eigen omgeving draait. Wie meeleest bij de aanbieder, heeft
dan een kant-en-klare aanvalsroute. Moet een document er toch in, anonimiseer het eerst, bijvoorbeeld met
de [anonimizer in de browser](https://security-commons-nl.github.io/anonimizer-browser/).

### 4. Welke bevoegdheid?

De zes velden van een gedelegeerde taakbevoegdheid: wie, welke agent, taak, scope, limieten en tijd. Zie
[Wiens bevoegdheid gebruikt een AI-agent?](../agent-bevoegdheid/). Begin met alleen lezen; schrijfrechten
krijgt een agent pas als de taak zonder niet kan, en dan met een goedkeuringsstap per gevoelige actie.

### 5. Wie keurt de agent, en hoe vaak?

Een ander model of een andere aanbieder dan wat de agent toetst, een mens die op de uitkomst beslist, en
een periodieke steekproef met de hand. Zet de frequentie op het blad: bij de start vaker, daarna per
kwartaal.

### 6. Wanneer stop je?

De signalen waarbij de agent uit gaat, vooraf vastgelegd: de agent vraagt gegevens buiten zijn taak op,
de uitkomsten wijken bij de steekproef af, de aanbieder wisselt van model zonder aankondiging, of de
tijdwinst blijkt er niet te zijn. Wie de agent uitzet, en hoe, staat erbij.

### 7. Wat kost het tegenover wat het bespaart?

De geclaimde tijdwinst tegenover de tijd die de borging kost: dit blad, de steekproef, de monitoring, het
gesprek met de leverancier. Een agent die een uur per week bespaart en een uur per week aan borging
vraagt, levert niets op. Voor het meten van de werking van een algoritmisch proces heeft het CPB een
handreiking; het [Algoritmekader](https://minbzk.github.io/Algoritmekader/) helpt bij de
risicoklasse en de rol onder de AI-verordening.

## Het invulblad

Kopieer dit blok, vul het in per agent en bewaar het bij het besluit. Het ingevulde blad is het bewijs dat
de inzet een besluit was.

```text
KEUZEBLAD AI-AGENT
Naam van de agent:
Eigenaar (functie):
Datum besluit:                       Herzien op:

0. Probleem en taak:
   Tijd die de taak nu kost:
1. Waar het draait:  lokaal / eigen tenant / cloud van een derde (welke):
2. Model:  open (welk, welke versie, wachttijd) / gesloten (welke aanbieder, aankondiging bij wissel):
3. Data die erin gaat:
   Data die er nooit in gaat:
   Geanonimiseerd vóór gebruik:  ja / nee / niet nodig
4. Bevoegdheid (zes velden):  wie / agent / taak / scope / limieten / tijd
   Schrijfrechten:  geen / ja, met goedkeuring voor:
5. Wie keurt de agent:
   Steekproef:  hoe vaak, door wie:
6. Stopsignalen:
   Wie zet uit, en hoe:
7. Verwachte tijdwinst per maand:
   Tijd voor borging per maand:

Besluit:  inzetten / proef tot (datum) / niet inzetten
Onderbouwing:
DPIA nodig:  ja / nee, want:
Akkoord (functie):
```

## Bewijs

- Per agent een ingevuld blad met besluit en onderbouwing.
- De resultaten van de steekproeven, met datum.
- Bij een gestopte agent: welk stopsignaal, en wat er daarna is besloten.

## Hoe dit samenhangt

De agent-patronen waar dit blad voor bedoeld is: [Verdediging met AI](../agent-patronen-beveiliging/). De
bevoegdheid: [Wiens bevoegdheid gebruikt een AI-agent?](../agent-bevoegdheid/). Ben je aanbieder of
gebruiksverantwoordelijke onder de AI-verordening: de
[aanbieder-toets](../../governance/aanbieder-onder-de-ai-act/). Gaat het mis:
[Wanneer meld je een AI-incident?](../ai-incident-melden/). Het gesprek met de FG over AI en algoritmen:
de gesprekskaart van de IBD in de bronnen hieronder.

## Licentie

[EUPL-1.2](../../LICENSE).
