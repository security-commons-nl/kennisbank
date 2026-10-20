# De Cbw-registratie invullen bij het NCSC, veld voor veld

> **Herkomst:** invulblad van de CISO van een regionale samenwerking van vier gemeenten, opgesteld tijdens de eerste registratie (augustus 2026). Voor de commons ontdaan van namen, telefoonnummers, IP-reeksen, domeinnamen en ticketnummers. Wat overblijft, zijn de vaste antwoorden met de redenering erachter, zodat elke gemeente identiek en navolgbaar registreert.

**Portaal:** mijn.ncsc.nl, inloggen met eHerkenning op niveau EH2+, dienst MijnNCSC. Tussentijds opslaan kan,
dus je hoeft een gemeente niet in één sessie af te maken. Elke gemeente registreert zelf; met een
ketenmachtiging kan één gemeente het voor de andere doen.

## Stap 1. Organisatiegegevens

Worden automatisch opgehaald, voor overheidsorganisaties uit het Register van Overheidsorganisaties, niet uit
het handelsregister.

- Alleen controleren. Klopt iets niet, corrigeer het **in de bron**, niet in het formulier.
- Controleer dat de getoonde organisatie de gemeente is die je nu registreert. Bij een ketenmachtiging is dit
  de plek waar een verwisseling zichtbaar wordt.

## Stap 2. Cbw-gegevens

| Veld | Antwoord | Waarom |
|---|---|---|
| Hoofdsector | Overheid | Voorgevuld, laten staan |
| Subsector | Overheid - Gemeenten | Voorgevuld, laten staan |
| Soort dienstverlening | **Overheidsinstanties op regionaal niveau** | De keuzelijst volgt letterlijk bijlage I van NIS2 en kent alleen centraal en regionaal. Nederland heeft gemeenten in de Cbw ondergebracht bij de decentrale overheden, en dat is in richtlijntermen regionaal |
| EU-lidstaten | Alleen Nederland | De gemeente levert geen diensten in andere lidstaten |
| Hoofdvestiging | Nederland | |
| Uitwisselingsregelingen | **Leeg laten**, tenzij aantoonbaar | Zie hieronder |
| Aantal fte, jaaromzet, balanstotaal | **Leeg laten** | Optioneel en niet bepalend; de indicatie staat al op essentieel omdat die uit de sector volgt. En alles wat je invult valt onder de mutatieplicht van 14 dagen |
| Type entiteit | **Essentieel** | Niet "belangrijk" en niet "vrijwillig" |

**Waarom essentieel vaststaat.** Voor de sector overheid is de omvang niet relevant; gemeenten voldoen in elk
geval aan de criteria voor een overheidsinstantie uit artikel 6, onderdeel 35, van NIS2. Artikel 2 van de
Cyberbeveiligingsregeling sector overheid bevestigt het.

**Waarom "regionaal" geen vormkwestie is.** De keuze bepaalt onder welk regime je in het register komt. De
regeling knipt precies daarop: centrale overheid gaat naar een andere tabel, decentrale overheid naar de
impactniveaus hoog en zeer hoog, en de meldplichtdrempels voor decentrale overheden (onder meer vier uur
uitval) staan in artikel 6, tweede lid. Dat zijn de drempels waarop de
[meldplichtprocedure](meldplichtprocedure.md) is gebouwd. "Centraal" aanvinken zet de registratie haaks op
die procedure.

**Waarom uitwisselingsregelingen meestal leeg blijft.** Het veld vraagt naar deelname op dit moment en valt
onder de verklaring naar waarheid. Voor gemeenten geldt meestal: er is geen gemeente-ISAC; de ISAC van de
veiligheidsregio's is voor de veiligheidsregio's zelf; de erkende uitwisselingsorganisaties in de lijst
passen niet of zijn niet aangegaan; en wat de gemeente aan de IBD heeft, loopt via het VNG-lidmaatschap, niet
via een uitwisselingsregeling in de zin van dit veld. Niets aanvinken wat niet aantoonbaar is. Verandert het
later, dan is dat een mutatie binnen 14 dagen.

## Stap 3. Contactpersonen

Gevraagd: naam, telefoon, e-mail, functie. Het NCSC adviseert iemand met inhoudelijke kennis van
cybersecurity én hoge beslissingsbevoegdheid.

- **Geef de indiener ook op als contactpersoon**, anders is die niet benaderbaar over de registratie.
- **Eén contactpersoon voor meerdere gemeenten is een single point of failure.** Voeg per gemeente minstens
  twee toe: iemand met inhoudelijke kennis (CISO en plaatsvervanger) en iemand met beslissingsbevoegdheid
  (CIO, directeur bedrijfsvoering of gemeentesecretaris).
- Contactpersoon is de aanspreeklijn, niet de aansprakelijke; de aansprakelijkheid blijft bestuurlijk.
- **Vraag na of de bestuurlijke contactpersoon weet dat hij dat is,** en of hij de crisisorganisatie kent.
  Iemand als NCSC-contact opgeven die dat zelf niet weet, is precies de verrassing die je bij een significant
  incident niet wilt.

## Stap 4. Netwerkgegevens

Gevraagd: publieke IP-adressen of -reeksen, domeinnamen, AS-nummer. Vaste invulbesluiten:

1. **AS-nummer leeg als je er geen hebt.** Vul niet het AS-nummer van je provider in; dat koppelt de gemeente
   aan de complete aankondiging van die provider.
2. **Scope: wat je zelf beheert of laat beheren.** Publieke adressen van hosting- en SaaS-partijen kun je in
   eerste instantie buiten houden, als bewuste en vastgelegde keuze. Herzie dat als het beeld compleet is.
3. **Domeinnamen niet leeg laten.** Vul de hoofddomeinen in die zeker zijn en vul aan als de inventaris er is.
   Te goeder trouw en beter verdedigbaar dan een leeg wettelijk veld. Een domein dat niet naar je eigen
   reeksen wijst, is geen fout: websites draaien vaak bij een hoster.
4. **Snelste route naar alle domeinen:** wie de domeinen factureert, weet welke er zijn. Na de registratie
   kun je via CSV in bulk aanvullen.
5. **Leg vast wat je invult,** per gemeente, met datum.

Laat je dit door een assistent of browser-agent invullen, geef dan harde grenzen mee: alleen stap 4, nooit
doorklikken naar stap 5, tussentijds opslaan, niets verzinnen, stoppen als het veld iets anders vraagt dan
verwacht, en de letterlijke eindlijst terugrapporteren.

## Stap 5. Samenvatting en verklaring

Controleren, en dan verklaren dat het formulier naar waarheid is ingevuld en dat wijzigingen **binnen 14 dagen**
worden doorgegeven. Dat is een juridische handeling; die zet de bevoegde persoon zelf.

De registratie is daarmee een levend record. Werkregel: **onvolledig maar op tijd is beter dan volledig te
laat**; correcties gaan als mutatie.

## Logboek per gemeente

| Gemeente | Registratiedatum | Ingelogd met | Contactpersonen | Domeinnamen | IP-reeksen | Bijzonderheden |
|---|---|---|---|---|---|---|
| | | | | | | |
