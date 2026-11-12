# De sessie, slide voor slide

> De volledige inhoud van de awareness-sessie (26 slides in zes acts). Bouw er je eigen presentatie van in je eigen
> huisstijl, of geef de sessie direct vanaf deze pagina. Vervang de plaatshouders (`[Naam spreker]`, `[telefoon]`,
> `[e-mailadres]`, `[link]`) door je eigen gegevens. Classificatie van alle slides: Public, TLP:CLEAR.

## Opening

**Slide 1. Learning digitale veiligheid, voor managers.** Hacks en datalekken: ben jij je bewust?
`[Naam spreker]`, CISO.

## Act 1. Dichtbij

**Slide 2. Waarom zit jij hier vandaag?** Dit gaat niet over IT. Dit gaat over jou, en je team.
- Geen enkele grote hack van 2026 begon met een gekraakte server. Ze begonnen met een mens die klikte, plakte, belde of
  goedkeurde.
- Techniek vangt veel op. Maar de laatste stap, herkennen dat iets niet klopt, doet een mens.
- Ben je leidinggevende? Dan zit je hier met een extra reden: jouw team kijkt naar jou. Wat jij normaal vindt, wordt de
  norm. Voer jij dit gesprek, dan voert je team het ook.

Vandaag geen IT-college. Wel het verhaal achter de hacks, wat AI verandert, en drie dingen die je morgen anders doet,
thuis en op het werk.

**Slide 3. Icebreaker.** "Wie had ooit een abonnement bij Odido, T-Mobile, Tele2 of Ben?"

**Slide 4. Odido: hoe één telefoontje een derde van Nederland blootlegde.**
- De aanvaller belde de klantenservice. Vloeiend Nederlands, rustig en deskundig: hij zei dat hij van de interne
  IT-afdeling was, bezig met een storing. Zo bellen echte IT-collega's ook.
- Hij stuurde de medewerker naar een inlogpagina die er net zo uitzag als die van Odido, maar van hem was. De medewerker
  logde daar in en gaf zo gebruikersnaam, wachtwoord en inlogcode weg. (Dat is "inloggen op een nepje".)
- Met die gegevens kon hij in het klantsysteem en downloadde hij in minuten de hele database: namen, adressen, IBAN,
  paspoortnummers, gevoelige notities.

Het motief was gewoon geld. Een afpersmail volgde: betaal 1 miljoen euro, anders gaat alles online. Odido betaalde niet;
de afpersers lekten daarna dagelijks data en zetten op 1 maart alles op het darkweb.

| Niemand verifieerde wie er belde | Eén medewerker kon bij alles | Niemand zag de data weggaan |
|---|---|---|
| Terugbellen naar een bekend intern IT-nummer was nodig; dat gebeurde niet. | Eén klantenservice-account had toegang tot de complete database. | Tientallen gigabytes verlieten het bedrijf zonder dat een alarm afging. |

**Slide 5. Epe: dezelfde truc, een gemeente vlakbij.** Een gemeente zoals wij. Bijna alle inwoners op straat.
- Een medewerker kreeg een nep-foutmelding: "er is iets mis, klik hier om te verifiëren". Ze plakte een stukje tekst
  dat de pagina haar gaf, in werkelijkheid een opdracht die haar computer voor de aanvaller liet werken. (Dit heet
  ClickFix.)
- "Maar wij hebben toch MFA?" Epe ook. Dat account had MFA. Het hielp niet: bij deze truc voer je de aanval zelf uit.
  MFA alleen is niet genoeg.
- De data stond op een bestandsserver die al gepland stond om uitgefaseerd te worden (migratie naar SharePoint en Teams),
  net niet op tijd opgeruimd.
- In één nacht circa 871 GB, ruim 550.000 bestanden, gestolen. Op straat: een BRP-export met naam, adres, geboortedatum
  en BSN van vrijwel alle inwoners, en 1.022 kopieën van identiteitsbewijzen (845 nog geldig). Kosten tot nu: € 345.258, en nog niet af.

Aan de zaal: "Hebben wij ook servers die 'nog even' niet zijn opgeruimd? Zou onze servicedesk een nep-melding herkennen?
Hoe snel weten wij wat er weg is?"

**Slide 6. Het is geen incident, het is een patroon.** Vijf grote lekken in een paar maanden, steeds dezelfde fouten:
Odido, gemeente Epe, Booking.com, Basic-Fit, Canvas. Steeds opnieuw: niemand checkte wie er belde, één account kon bij te
veel, en niemand zag de data weggaan. Wij houden een lijst bij; dit zijn de bekendste vijf, er staan er nog tientallen op.

## Act 2. Hoe het werkt

**Slide 7. Aanvallers hebben keuze: de hoofdvormen.**

| Hoe het werkt | In gewone taal |
|---|---|
| Je verleiden | Een bericht of telefoontje dat je iets laat doen: nep-mail, nep-telefoontje, nep-sms, valse QR-code |
| Je identiteit overnemen | Je login of inlogcode aftroggelen, zodat ze namens jou binnenkomen |
| Jou het zelf laten doen | Je een "handige" tool of "verplichte stap" laten installeren of uitvoeren |
| Via een ander binnenkomen | Eerst een leverancier of website hacken, en zo bij jou uitkomen |

Twee daarvan laten we zo in een demo zien. De rest is net zo echt, en soms voor een paar euro te koop.

**Slide 8. Twee technieken die alles omzeilen.** Geen bijlage. Geen verdachte link. Geen scanner die piept.

| De truc | Wat ze je vragen | Wat jij ziet |
|---|---|---|
| De nep-IT-helpdesk | "Voer deze code in" of "doorloop deze verificatie" | Een echte Microsoft-pagina; je inlog werkt gewoon |
| De "los het zelf op"-melding | "Kopieer dit en plak het, dan is het opgelost" | Een nep-foutmelding of nep-controle |

In beide gevallen: echte, betrouwbaar ogende systemen, en jij bent de schakel die het afmaakt. Vuistregel: code intypen
op een pagina die jij niet zelf opende, of iets plakken om iets "op te lossen"? Doe het niet. Stop en check via een
vertrouwd nummer.

**Slide 9. Demo: zo gaat een aanval echt.** Reconstructie op basis van publieke informatie (MIVD-jaarbericht 2026,
Microsoft, NCSC-NL). Alle schermen, accounts en data zijn nep; geen werkende aanval. Spreektekst: "Wat je nu ziet is geen
Hollywood. De tweede techniek, die 'los het zelf op'-melding, is precies hoe Epe begon. Twee ingangen, één keten
erachter. Ik praat je erdoorheen."

**Slide 10. Demo in drie scènes (ongeveer 10 minuten).**
1. Een "handige" browser-tool: één klik, en je sessies liggen op straat. Geen wachtwoord nodig.
2. Een Teams-bericht van "IT Support" (extern): drie stappen, en de aanval draait. Let op het label External.
3. Wat er daarna gebeurt, in een gesplitst scherm: jij merkt niets, de aanvaller ziet alles binnenkomen.

Plaats hier je eigen schermopname; de spreker geeft live commentaar.

**Slide 11.** Tegen wat we kennen, zetten we techniek. Tegen wat we niet kennen: jou.

## Act 3. Wat AI verandert

**Slide 12. En nu met AI erbij.** AI verzint geen nieuwe aanval. Het haalt de signalen weg waaraan we het vroeger
herkenden.

| Stelling: waar of niet waar? | Het antwoord |
|---|---|
| "Phishing herken je aan spelfouten en raar Nederlands." | Niet meer waar. AI schrijft foutloos, in de juiste toon. Herken het aan het verzoek, niet aan de taal. |
| "Een bekende stem aan de telefoon kun je vertrouwen." | Niet meer waar. Een stem is uit seconden audio te klonen. Daarom: terugbellen via een bekend nummer. |
| "Videobellen is veilig, je ziet wie het is." | Steeds minder waar. Deepfake-calls bestaan: "de leidinggevende die om een spoedbetaling vraagt". |

Open vraag: "Je krijgt een belletje of spraakbericht van je leidinggevende, de stem klopt, met de vraag snel iets te
regelen of te betalen. Wat doe je?" AI maakt nep lastiger te herkennen, dus onze drie stappen veranderen niet, ze worden
belangrijker. En thuis geldt precies hetzelfde.

## Act 4. Ons huis

**Slide 13. Hoe staat een gemeente ervoor: wat IV en IB&P doen, en waarom jij ook nodig bent.**
- Wat IV en IB&P doen: software up-to-date houden, verdachte mail filteren en monitoren op vreemd gedrag op de systemen;
  sterke inlog (MFA) en beperken wat verdachte programma's op werkplekken mogen doen; gaat er iets mis, dan kunnen zij
  ingrijpen en herstellen.
- Waarom techniek alleen niet genoeg is: de nieuwste trucs gebruiken echte, legitieme systemen en vragen jou om de
  laatste stap. Daar kan geen filter tussen. Alles dichttimmeren kan niet, want dan kun je je werk niet meer doen.
  Veiligheid is een balans.

Er gebeurt veel achter de schermen. Maar de laatste meter loopt door jouw team. En toch is elk cluster van een gemeente
een doelwit.

**Slide 14. Een gemeente: waar zou een aanvaller toeslaan?** Een aanvaller kiest niet willekeurig, maar op wat een
cluster heeft.

| Cluster | Waar een aanvaller op uit is |
|---|---|
| Beheer | Een proces platleggen: gemalen, riolering, verkeers- en parkeerinstallaties |
| Interne dienstverlening en advisering | Geld en toegang: de sleutels tot alles |
| Publiekszaken, handhaving en veiligheid | Identiteit en adres van inwoners |
| Participatie en maatschappelijke ontwikkeling | Dossiers van kwetsbare inwoners |
| Stedelijke ontwikkeling | Grote transacties en vastgoed |
| Projectbureau | Continuïteit van projecten, en de leverancier als ingang |

Vijf redenen waarom je een doelwit bent: geld, gevoelige data, toegangsrechten, een vertrouwde naam, ontwrichting.

**Slide 15. Cluster beheer: een aanval hoeft geen data te stelen.**
- Doelwit: operationele techniek (gemalen, riolering, verkeers- en parkeerinstallaties).
- Scenario: niet via een mail naar een ambtenaar, maar via de leverancier die op afstand onderhoud doet. Eén gekaapt
  onderhoudsaccount en een aanvaller kan processen verstoren: geen euro gestolen, wel ontwrichting. Statelijke actoren
  hebben hier expliciet interesse (NCSC, AIVD).
- De AI-twist: een AI-stem die de leverancier nabelt ("ik moet even op afstand inloggen voor een storing") klinkt perfect.
- Aan de zaal: "Weten we van alle installaties wie er op afstand bij kan, en zou het opvallen als iemand 's nachts
  inlogt?"
- Wat helpt: verifiëren wie er belt (terugbellen via een bekend nummer) en geen toegang zonder sterke, unieke inlog.

**Slide 16. Cluster interne dienstverlening en advisering: de sleutels tot alles.**
- Doelwit: twee soorten buit tegelijk, geld (financieel beheer en debiteuren, inkoop) en toegang (servicedesk ICT,
  functioneel beheer: beheeraccounts die bij alles kunnen).
- Scenario: precies de Odido-truc, maar bij een gemeente. Iemand belt de servicedesk, doet zich voor als collega met
  spoed, en laat een account resetten. Of een "gewijzigd rekeningnummer" bij een grote crediteur glipt door.
- Wat Epe ons leert: daar kraakte de aanvaller een beheerderswachtwoord en kwam bij een noodaccount zonder MFA, een loper
  die op alle sloten past. Eén zo'n account is bij alles.
- De AI-twist: foutloze mail in de huisstijl; een gekloonde stem die de servicedesk belt.
- Aan de zaal: "Als 'een collega' de servicedesk belt met spoed, hoe checken we dat het echt een collega is?"
- Wat helpt: uniek sterk wachtwoord plus MFA op elk account, en terugbellen bij elk spoedverzoek over geld of toegang.

**Slide 17. Cluster publiekszaken, handhaving en veiligheid: identiteit en adres van inwoners.**
- Doelwit: burgerzaken (identiteitsbewijzen, BRP) en, extra gevoelig, de geheime adressen van bedreigde mensen. Ook de
  aanpak van ondermijning is interessant voor wie criminele belangen heeft.
- Scenario: met BRP- en adresgegevens worden aanvallen op inwoners levensecht; voor sommige mensen (stalking, bedreiging)
  gaat het om fysieke veiligheid. Bij Epe lagen precies dit soort gegevens (BSN, 1.022 ID-kopieën) op straat.
- De AI-twist: met gelekte persoonsgegevens en AI is een geloofwaardige nep-benadering van een inwoner zo gemaakt.
- Aan de zaal: "Wie kan bij adres- en identiteitsgegevens, en hoe beschermen we juist de mensen met een geheim adres?"
- Wat helpt: minimale toegang, sterke inlog, en bij twijfel verifiëren. Nooit gegevens vrijgeven op basis van één
  telefoontje.

**Slide 18. Cluster participatie en maatschappelijke ontwikkeling: dossiers van kwetsbare inwoners.**
- Doelwit: schuldhulpverlening, jeugdhulp en Wmo, werk en inkomen: dossiers over mensen in een kwetsbare positie.
- Scenario: dit soort data is ideaal voor afpersing en chantage, van de gemeente en rechtstreeks van die inwoners, die
  toch al kwetsbaar zijn.
- De AI-twist: AI maakt gerichte, persoonlijke misleiding (richting medewerker of inwoner) sneller en geloofwaardiger.
- Aan de zaal: "Waar staan de gevoeligste dossiers, en zou iemand het merken als die in bulk worden gekopieerd?"
- Wat helpt: verdacht verzoek of melding? Meld het bij de servicedesk of IB&P. Liever tien valse meldingen dan één
  gemiste aanval.

**Slide 19. Cluster stedelijke ontwikkeling: grote transacties en vastgoed.**
- Doelwit: grond- en vastgoedbedrijf en aanbestedingen, waar grote bedragen omgaan.
- Scenario: factuurfraude op niveau, een "gewijzigd rekeningnummer" of een spoedbetaling bij een vastgoed- of
  aanbestedingsdeal. Eén doorgeglipte wijziging kan om veel geld gaan.
- De AI-twist: een perfecte mail "namens" een bekende partij, of een gekloonde stem die de wijziging bevestigt.
- Aan de zaal: "Hoe controleren we een gewijzigd rekeningnummer of een spoedbetaling, en bij welk bedrag gaat er een
  extra check overheen?"
- Wat helpt: terugbellen via een bekend nummer voordat je betaalt of een rekeningnummer wijzigt. Altijd, ongeacht de haast.

**Slide 20. Cluster projectbureau: continuïteit en de leverancier als ingang.**
- Doelwit: grote projecten en programma's, en de vele leveranciers die meedraaien.
- Scenario: een aanvaller komt binnen via een ingehuurde partij of een leveranciersaccount (supply chain) en raakt zo de
  continuïteit van een heel project.
- De AI-twist: nep-correspondentie "namens" een leverancier of projectpartner is met AI nauwelijks van echt te
  onderscheiden.
- Aan de zaal: "Weten we van de leveranciers wie toegang heeft tot wat, en wat er gebeurt als één van hen gehackt wordt?"
- Wat helpt: behandel een leveranciersverzoek als elk ander: verifiëren via een bekend kanaal, en minimale toegang.

## Act 5. Wat doe jij

**Slide 21. Ben jij gelekt? Check het nu, pak je telefoon.** `politie.nl/checkjehack` (zet hier een grote QR-code).
Voer je e-mailadres in; de politie mailt je bij treffers in bekende datalekken. Duurt een paar minuten, check straks je
inbox. Gebruik alleen officiële bronnen. Download nooit gelekte data: dat is strafbaar.

**Slide 22. Doen, thuis en op het werk: drie stappen die je vandaag zet.**

| # | Stap | Concreet |
|---|---|---|
| 1 | Wachtwoordmanager en sterke inlog (MFA) | Eén uniek wachtwoord per account, zeker voor mail en bank. Authenticator-app, geen sms. |
| 2 | Bel terug bij twijfel | Gebeld over IT, fraude of je bank? Hang op. Bel zelf terug via een officieel nummer dat je opzoekt. |
| 3 | Pushmeldingen op je bank | Elke afschrijving zie je direct. Eén tik en je weet of het klopt. |

Dit zijn dezelfde drie antwoorden die bij elke hack van vandaag terugkwamen, en ze werken thuis precies zo goed als op het
werk. Later thuis: BKR-check via mijnkredietregistratie.nl, en de KopieID-app voor scans van paspoort of rijbewijs.

**Slide 23. En op het werk? De link met je eigen organisatie.**
- Het goede nieuws: de eigen dienstverlening is bij Odido of Epe niet verstoord, en medewerkergegevens zijn daar niet bij
  geraakt.
- Het minder goede nieuws: AIVD en MIVD waarschuwen voor aanvallen op overheidsmedewerkers, vaak via WhatsApp of Signal.
  Epe laat zien: gemeenten zijn ook doelwit, en het raakt elk cluster.
- Wat we van je vragen: WhatsApp en Signal zijn geen kanaal voor werk, gebruik Teams, Outlook en de telefoon. Twijfel over
  een telefoontje "van IT"? Hang op, bel zelf terug. Iets verdachts? Meld het bij de servicedesk of het IB&P-team. Liever
  tien valse meldingen dan één gemiste aanval.

## Act 6. Jouw team

**Slide 24. Voor jou als leidinggevende: jij vertaalt dit naar je team.** Denk aan je eigen team: wie zou een aanvaller
uitkiezen? Wie keurt betalingen goed? Wie ziet de dossiers van de kwetsbaarste inwoners? Wie heeft toegang tot veel
systemen? Wie kan namens een leidinggevende iets in gang zetten?
- Bespreek het in je eerstvolgende teamoverleg; tien minuten is genoeg. Gebruik de drie stappen en één recent voorbeeld
  (Odido of Epe).
- Deel de A4-handleiding, die je na deze sessie per mail ontvangt: één pagina die je één op één kunt doorsturen.
- Maak melden normaal: liever tien valse meldingen dan één gemiste aanval. Reageer nooit met "had je dat niet moeten zien?"
- Geef zelf het goede voorbeeld: bel terug bij twijfel, gebruik geen WhatsApp voor werk. Jouw gedrag is de norm.

## Slot

**Slide 25. Onthoud deze drie dingen.**

| | |
|---|---|
| 1. Het begint altijd bij een mens | Geen hack begint met een gekraakte server. Het begint met iemand die klikt, plakt, belt of goedkeurt. |
| 2. Het is geen incident, het is een patroon | Vijf grote lekken in een paar maanden, steeds dezelfde fouten. En AI maakt ze geloofwaardiger. |
| 3. Jij bent de eerste filter | Wij houden tegen wat we kennen. Jij ziet wat wij niet zien, thuis en op het werk. Daarom hoor jij erbij. |

"Het is geen incident, het is een patroon. Jij bent de eerste filter."

**Slide 26. Vragen?** Bedankt voor jullie tijd. Vragen, zorgen, of iets melden? `[Naam spreker]`, CISO,
`[telefoon]`, `[e-mailadres]`. Op de hoogte blijven van dit soort sessies? Meld je aan via `[link]`.
