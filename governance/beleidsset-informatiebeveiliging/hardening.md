# Beleid hardening

### Afkortingen

| Afkorting | Omschrijving |
|---|---|
| BIO | Baseline Informatiebeveiliging Overheid |

### Verwante beleidsdocumenten

- Strategisch IB-beleid

- Beleid Mobile Device Management

- Wachtwoordbeleid

- Aanwijzing patchmanagement

## Inleiding

Hardening is het proces om overbodige functies in besturingssystemen uit te schakelen en te verwijderen, periodiek te controleren en bij te stellen. Het niet uitvoeren van hardening vormt een onnodig risico, kwaadwillenden gebruiken deze functionaliteiten om zich onbevoegd toegang tot systemen te verschaffen, met ernstige schade aan gemeentelijke informatievoorziening tot gevolg. Hardening dient gestructureerd te worden aangepakt, daarom moeten procedures worden vastgesteld om hardening doeltreffend en ordelijk te laten plaatsvinden. Dit beleid is van toepassing op alle systemen die in gebruik zijn van de organisatie VOORBEELDGEMEENTE.

## Uitgangspunten

Om te voldoen aan de eisen voor hardening uit de BIO hanteert de organisatie de volgende uitgangspunten:

Overbodige software, services, gebruikersaccounts, en gebruikersrechten worden uitgeschakeld en/of van het systeem verwijderd, of aangepast naar een acceptabel niveau.

## Operationele maatregelen

De operationele maatregelen voor hardening zijn de volgende:

- Gegevensuitwisseling tussen vertrouwde en niet vertrouwde zones zoals communicatie via internet, e-mail, of andere elektronische wijze, dient inhoudelijk geautomatiseerd gecontroleerd te worden op aanwezigheid van kwaadaardige software (zoals virussen en malware).

- Communicatiekanalen, diensten en soortgelijke voorzieningen op een netwerk of computer die niet vereist zijn voor de dienst dienen te worden afgesloten door systeembeheerders.

- Voor toegang tot systemen door middel van wachtwoorden dient men zich te houden aan het vigerende wachtwoordbeleid voor de organisatie.

- Wachtwoorden die bij default (af-fabriek) zijn meegeleverd met de apparatuur worden vervangen door wachtwoorden die voldoen aan het vigerende wachtwoordbeleid.

- Op alle apparatuur worden (waar mogelijk) beschikbare firewalls, antivirusscanners en andere beschermende maatregelen geactiveerd, voor serversystemen is core-installatie het uitgangspunt.

- Op alle apparatuur wordt (waar mogelijk) systeem logging geactiveerd om detectie mogelijk te maken van malware en ongebruikelijke systeem activiteiten.

- Het centraal beperken van toegang tot bestanden of objecten door gebruikers of systeemprocessen door de inzet van verplichte toegangscontrole, Mandatory Access Control (MAC), op systemen.

- Rechten op bestandssystemen worden zo optimaal mogelijk toegekend.

- Werkstations worden zo ingericht dat routeren van verkeer tussen verschillende zones of netwerken niet mogelijk is.

- De indeling van zones binnen de technische infrastructuur vindt plaats volgens een operationeel beleidsdocument waarin is vastgelegd welke uitgangspunten voor zonering worden gehanteerd. Van systemen wordt bijgehouden in welke zone ze staan. Er wordt periodiek, minimaal één keer per jaar, geëvalueerd of het systeem nog steeds in de optimale zone zit of verplaatst moet worden.

- Zonering wordt ingericht met voorzieningen waarvan de functionaliteit is beperkt tot het strikt noodzakelijke (hardening van voorzieningen).

- Alle dataverbindingen zijn voorzien van versleuteling.

- Accounts die niet zijn toe te wijzen aan een (actieve) gebruiker worden verwijderd of gedeactiveerd.

- Alleen geautoriseerd personeel kan functies en software installeren of activeren.

- Alleen noodzakelijke software is toegestaan, overige software dient verwijderd of gedeactiveerd te worden.

- Alle apparatuur moet regelmatig worden getest op bekende zwakheden zoals beschreven in de aanwijzing patchmanagement

- De gemeentelijke infrastructuur is via het defense-in-depth principe op diverse lagen beveiligd.
