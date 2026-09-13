---
titel: Wiens bevoegdheid gebruikt een AI-agent?
vakgebied: security
type: aanpak
normen: [BIO2, AI Act]
versie: 2026-09
herkomst: ontwerpregel uit de praktijk van een CISO-organisatie bij een gemeente, gebouwd op een publiek gedeeld zesstappenmodel voor agent-autorisatie
status: concept
samenvatting: Een AI-agent die een API aanroept werkt niet op de bevoegdheid van de medewerker en niet op een eigen staande bevoegdheid, maar op een gedelegeerde taakbevoegdheid met zes velden, een goedkeuringsstap voor gevoelige acties en een audit die vijf vragen beantwoordt. Vertaald naar Entra, Copilot-agents en MCP-koppelingen op gemeentelijke systemen, met de vragen aan de leverancier en het bewijs dat je moet kunnen laten zien.
---

# Wiens bevoegdheid gebruikt een AI-agent?

> **Lees de aanpak online:** [security-commons-nl.github.io/kennisbank/security/agent-bevoegdheid](https://security-commons-nl.github.io/kennisbank/security/agent-bevoegdheid/)

Een medewerker vraagt een AI-agent om een dossier na te lopen. De agent leest het zaaksysteem, raadpleegt
een externe bron en zet een concept klaar. Op wiens bevoegdheid deed hij dat? In de meeste inrichtingen
van vandaag is het antwoord: op die van de medewerker, met alles wat die mag. Of erger: op die van een
serviceaccount dat al drie jaar overal bij mag. In beide gevallen is achteraf niet te reconstrueren wie
wat heeft gevraagd, wat de agent mocht en wie een gevoelige actie heeft goedgekeurd.

Dit stuk beschrijft een ontwerpregel die dat oplost. Hij is niet nieuw voor wie zero trust kent, maar hij
is zelden uitgeschreven voor agents, en precies daar gaat het mis.

## De regel in een zin

Een agent werkt nooit op de bevoegdheid van de mens en nooit op een eigen staande bevoegdheid, maar op
een **gedelegeerde, begrensde en tijdgebonden taakbevoegdheid**, met een menselijke goedkeuringsstap
voor gevoelige of onomkeerbare acties en een audit die de hele keten kan navertellen.

## Zes stappen

1. **Menselijke identiteit.** De medewerker is geauthenticeerd (MFA), spreekt een intentie uit en delegeert
   een taak. De mens blijft aan het stuur.
2. **Agent-identiteit.** De agent heeft een eigen workload-identiteit, los van de mens, die bewijst welke
   instantie er handelt. Geen gedeeld serviceaccount, geen doorgegeven gebruikerstoken.
3. **Gedelegeerde taakbevoegdheid.** De delegatie is een object met zes velden (hieronder). Kortlevend,
   least privilege, precies voor deze taak.
4. **Policy-beslissing.** Elke aanroep gaat door een beslisregel. Laag risico en binnen de delegatie: door.
   Hoog risico of onomkeerbaar (verzenden, verwijderen, betalen, rechten wijzigen): step-up naar een mens
   die die ene actie beoordeelt en goedkeurt.
5. **De aanroep zelf.** De agent roept de API aan met de goedgekeurde bevoegdheid. Voor systemen op locatie
   loopt dat via OAuth, mTLS of Kerberos; legacy zonder moderne authenticatie gaat achter een gateway.
6. **Audit.** Elke stap is vastgelegd, van vraag tot uitkomst.

## De zes velden van een taakbevoegdheid

| Veld | Vraag | Voorbeeld |
|---|---|---|
| Wie | welke mens heeft gedelegeerd | medewerker Burgerzaken, MFA-geverifieerd |
| Welke agent | welke workload-identiteit handelt | `agent-dossiercheck`, instantie 7 |
| Taak | wat is het doel | volledigheidscontrole op zaak 2026-01187 |
| Scope | welke API's, welke data | zaaksysteem lezen, alleen die zaak; geen BRP |
| Limieten | hoeveel, welke acties | maximaal 50 aanroepen, geen schrijfacties |
| Tijd | geldig van en tot | vandaag 09:00 tot 12:00 |

Ontbreekt een veld, dan is de bevoegdheid niet compleet en weigert de policy-engine. Dat is de kern:
niet "de agent mag lezen in het zaaksysteem", maar "deze agent mag namens deze medewerker voor deze taak
dit deel van het zaaksysteem lezen, zo vaak, tot dat tijdstip".

## De vijf auditvragen

Een logregel over een agent-actie is pas bruikbaar als hij deze vijf vragen beantwoordt:

1. Wie heeft het gevraagd?
2. Welke agent heeft gehandeld?
3. Wat was gedelegeerd?
4. Welke actie is uitgevoerd?
5. Wie heeft het goedgekeurd?

Een logregel zonder antwoord op vraag 3 hoort een alarm te zijn: er handelde een agent zonder delegatie.

## Vertaling naar de gemeentelijke praktijk

**Microsoft-platform.** Een Copilot-agent of een eigen agent in Azure krijgt een eigen identiteit in Entra
(workload-identiteit of agent-identiteit), geen gebruikersaccount en geen gedeeld serviceaccount. Voorwaardelijke
toegang geldt ook voor die identiteit. Rechten op Graph en op de eigen API's zijn per agent gescopeerd, en
verhoogde rechten lopen via just-in-time-activering met een tijdvenster, precies zoals bij beheerders. De
delegatie zelf (wie, taak, tijd) staat niet in Entra; die leg je vast in de orkestratielaag van de agent en
je logt hem mee met elke aanroep.

**MCP-koppelingen op eigen systemen.** Een MCP-server die het zaaksysteem, de financiële administratie of
de BRP-koppeling ontsluit is een API met een nieuwe deur. Regels: de server authenticeert de agent, niet
de mens; elke tool op de server heeft een eigen scope; schrijvende tools staan standaard uit en gaan alleen
aan met een goedkeuringsstap; de server logt de vijf vragen zelf, onafhankelijk van wat de agent logt.

**Leveranciers.** Vraag bij elk product met een agent-functie: krijgt de agent een eigen identiteit of leent
hij die van de gebruiker? Kan ik scope, limieten en tijd per taak instellen? Waar zit de goedkeuringsstap
voor onomkeerbare acties, en kan ik zelf bepalen welke acties dat zijn? Levert het product per actie de
vijf auditvragen aan mijn centrale logverzameling? Een leverancier die op de eerste vraag "de gebruiker"
antwoordt, heeft het model nog niet.

## Wat het kost en wat het oplevert

Kosten: laag tot middel. De identiteiten en de voorwaardelijke toegang zitten in de licentie die je al hebt;
het werk zit in het uitschrijven van de delegatie per agent-taak en in de goedkeuringsstap.

Wat het oplevert: een agent die niet meer kan dan de taak vraagt, een keten die je aan een toezichthouder
kunt laten zien, en een intrekbare bevoegdheid per taak in plaats van een serviceaccount dat je niet durft
uit te zetten. Het is ook de praktische invulling van menselijk toezicht zoals de AI-verordening die vraagt:
niet een mens die meekijkt, maar een mens die per gevoelige actie beslist.

Waar je op moet letten: een goedkeuringsstap die bij elke actie vuurt wordt binnen een week weggeklikt.
Bepaal per agent welke acties gevoelig zijn en laat de rest door; de audit vangt de rest op.

## Bewijs

- Per agent een eigen identiteit in de identity-provider, met eigenaar en vervaldatum.
- Per agent-taak een uitgeschreven delegatie met de zes velden.
- De lijst acties die step-up vereisen, met een voorbeeld van een geweigerde en een goedgekeurde actie.
- Een logregel uit de centrale logverzameling waarin de vijf vragen beantwoord zijn.

## Hoe dit samenhangt

Dit is het agent-hoofdstuk van [Just-in-time beheerrechten](../just-in-time-beheerrechten/) en
[Rechten in de cloud terugbrengen tot gebruik](../least-privilege-cloud/): dezelfde principes, nu voor
een identiteit die geen mens is. De vijf auditvragen landen in [Richt centrale logverzameling in](../centrale-logverzameling/).
Voor het meten van AI-gebruik voordat je agents toelaat: [AI-gebruik in beeld](https://security-commons-nl.github.io/ai-gebruik-in-beeld/).

## Licentie

[EUPL-1.2](../../LICENSE).
