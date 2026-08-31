---
titel: Kritieke processen en herstelprioriteiten vaststellen
vakgebied: bcm
type: handleiding
normen: [ISO 22301, BIO2, NIS2]
peildatum: 2026-08-31
herkomst: in gebruik bij de continuiteitsorganisatie van een gemeente
status: in gebruik
samenvatting: Hoe je samen met de lijn vaststelt welke processen echt niet mogen uitvallen, welke
  continuiteitseisen daarbij horen en in welke volgorde je herstelt. Met de vuistregels per proces als
  checklist, en het deel dat meestal ontbreekt, namelijk hoe je die keuze houdbaar houdt als de
  organisatie verandert.
barrieres: [critical]
rol: fundering
---

# Kritieke processen en herstelprioriteiten vaststellen

> **Lees deze handleiding online:** [security-commons-nl.github.io/kennisbank/bcm/kritieke-processen-vaststellen](https://security-commons-nl.github.io/kennisbank/bcm/kritieke-processen-vaststellen/)

Vraag tien mensen in een publieke organisatie welke processen kritiek zijn en je krijgt tien lijsten. Vraag
het aan de staf en je krijgt er een die klopt maar die niemand kent. Dat tweede is het echte probleem: een
lijst kritieke processen die niet van de lijn is, stuurt niets aan. Hij komt tevoorschijn bij een audit en
verdwijnt daarna weer.

Deze handleiding gaat over hoe je zo'n lijst maakt met de lijn in plaats van voor de lijn, welke eisen je
eraan hangt, en hoe je hem overleeft als de organisatie op de schop gaat. Dat laatste is het deel waar de
meeste aanpakken zwijgen, en het is precies waar een lijst gewoonlijk sneuvelt.

## Begin bij ontwrichting, niet bij systemen

De verleiding is om te beginnen bij de applicatielijst. Dat levert een inventarisatie op, geen prioritering,
want techniek zegt niets over maatschappelijke gevolgen.

Begin bij deze vraag: **welke processen mogen niet uitvallen omdat inwoners er direct last van hebben, of
omdat er een wettelijke termijn op zit?** Denk aan uitkeringen die betaald moeten worden, een overlijden dat
geregistreerd moet worden, een telefoonlijn die het moet doen, een besluit dat binnen een termijn valt.

Twee dingen om vast te houden bij die eerste ronde:

- **Kritiek is niet hetzelfde als groot.** Een proces dat een keer per jaar draait kan kritieker zijn dan
  een proces dat dagelijks draait, als het moment vastligt en niet verplaatst kan worden.
- **Het moment telt.** Dezelfde uitval is op een dinsdagochtend iets anders dan tijdens een betaalronde,
  een verkiezing of een piek in de paspoortuitgifte. Noteer dus niet alleen het proces maar ook wanneer het
  pijn doet.

Een werkbare startomvang is twintig processen. Meer wordt niet onderhouden, minder mist te veel.

## Zeven vragen per proces

Voor elk proces dat de lijst haalt, loop je langs zeven assen. Ze staan uitgewerkt in
[vuistregels-per-proces.md](vuistregels-per-proces.md), met per as wat er geregeld hoort te zijn.

| As | De vraag die je stelt |
|---|---|
| **Mensen** | Zonder wie kan dit proces niet draaien of hersteld worden, en is daar vervanging voor? |
| **Apparatuur** | Wat valt om als een apparaat kapot gaat, en is het dubbel uitgevoerd of analoog te bedienen? |
| **Programmatuur** | Welke servicelevels zijn afgesproken, en wordt daarop gemonitord en gerapporteerd? |
| **Gegevens** | Zijn de gegevens gedefinieerd en geclassificeerd, en bij clouddiensten: kun je eruit? |
| **Organisatie** | Wie is waarvoor verantwoordelijk, aanwijsbaar en niet in algemene termen? |
| **Omgeving** | Wat heb je nodig aan gebouw, stroom en ruimte, en wat als dat wegvalt? |
| **Diensten** | Welke leveringen zijn nodig, en ligt er een exitplan voor de kritische? |

De vuistregel bij **mensen** is de nuttigste van de zeven en tegelijk de meest genegeerde: **drie personen
per onmisbare functie.** Met drie vang je verloop, verlof en ziekte tegelijk op. Met twee niet, want dan is
één vakantie plus één ziekmelding genoeg. Tel dat eerlijk na en je vindt in elke organisatie processen die
op één persoon draaien.

De vuistregel bij **diensten** is de politiek lastigste: een exitplan voor kritische leveranciers. Niet
omdat je van plan bent te vertrekken, maar omdat je zonder dat plan niet gelijkwaardig kunt onderhandelen.

## Drie eisen, en de derde wordt vergeten

Per kritiek proces leg je vast:

1. **Maximale uitvalsduur.** Binnen welke termijn moet het proces weer draaien na een calamiteit.
2. **Maximaal gegevensverlies.** Hoeveel werk mag er verloren gaan, uitgedrukt in tijd tussen de calamiteit
   en het laatste moment waarop gegevens veiliggesteld waren.
3. **Het minimumniveau.** Op welk niveau kan de dienstverlening tijdens de verstoring doorgaan. Aangepaste
   servicenormen, een tijdelijk hogere foutmarge, een handmatige route.

Die derde is de belangrijkste en staat het minst vaak ingevuld. De eerste twee gaan over herstel, en herstel
duurt altijd langer dan je hoopt. Het minimumniveau gaat over de uren of dagen daartussen, en dat is precies
de periode waarin je organisatie in de krant komt. Wie geen plan B heeft afgesproken, improviseert er een op
het slechtste moment.

## Herstelprioriteit is een verdelingsvraag

Als alles tegelijk uitvalt, kun je niet alles tegelijk herstellen. Er moet dus een volgorde zijn, en die
volgorde is geen technisch besluit.

Dat is de kern: **de volgorde bepaalt wie langer wacht.** Als de uitkeringsrun voorgaat op de
vergunningverlening, dan is dat een keuze over welke inwoner eerst geholpen wordt. Zo'n keuze hoort bij de
directie, niet bij een beheerder om drie uur 's nachts.

Werkwijze die standhoudt: laat de lijn de volgorde vaststellen als een besluit, met de motivering erbij, en
leg vast wat er expliciet níet in de eerste ronde zit. Dat laatste voorkomt de discussie tijdens de
calamiteit, want dan is iedereen ervan overtuigd dat zijn proces vooraan stond.

## Houdbaar houden als de organisatie verandert

Hier sneuvelt het gewoonlijk. Een lijst die is vastgesteld onder de oude afdelingsindeling is na een
reorganisatie onbruikbaar: processen heten anders, eigenaren zijn vertrokken, en niemand voelt zich
verantwoordelijk voor bijwerken. Vier dingen die dat vertragen.

**Hang het aan het proces, niet aan de afdeling.** Afdelingen worden hernoemd en samengevoegd, processen
blijven bestaan. Noteer bij elk proces de wettelijke of dienstverlenende grondslag, niet de organisatorische
plek. Dan is een reorganisatie een verhuizing in plaats van een herbouw.

**Maak de eigenaar een rol, geen naam.** "De proceseigenaar van burgerzaken" overleeft een vertrek,
"J. Jansen" niet. Wie de rol overneemt, erft de lijst.

**Laat verandering zelf de trigger zijn.** Een jaarlijkse herijking loopt altijd achter, want reorganisaties
volgen geen jaarritme. Spreek af dat een organisatiewijziging, een nieuwe aanbesteding of een uitbesteding
automatisch een herijking van de geraakte processen vraagt. Dat is een afspraak van een regel en het scheelt
maanden achterstand.

**Koppel de jaarlijkse toets aan iets dat toch al gebeurt.** Een losse jaarlijkse ronde wordt uitgesteld. Een
toets die meelift op de planning-en-controlcyclus of op de managementrapportage gebeurt wel, want daar staat
een datum op die niemand mist.

En één dat vaak wordt overgeslagen: **leg vast wat er níet geregeld is en waarom.** Wijkt een proceseigenaar
af van de vuistregels, dan is dat prima, maar dan moet er staan wat er dan wél is geregeld en waarom hij dat
afdoende vindt. Dat is de enige manier waarop een lijst een gesprek blijft in plaats van een norm waar
iedereen omheen werkt.

## Wat er in deze map staat

- [vuistregels-per-proces.md](vuistregels-per-proces.md) — de zeven assen uitgewerkt, met per as wat er
  geregeld hoort te zijn en welke uitgangspunten daaronder liggen

## Bewijs

Wat je aan het eind kunt laten zien:

- Een **vastgestelde lijst kritieke processen**, met een besluit van de lijn eronder en niet alleen een
  stafnotitie.
- Per proces de **drie continuiteitseisen** ingevuld, inclusief het minimumniveau.
- Een **herstelvolgorde** die als besluit is genomen, met de motivering en met wat er bewust buiten de
  eerste ronde valt.
- Per onmisbare functie een **bezettingstelling**, waaruit blijkt welke processen op minder dan drie
  personen draaien.
- Een **herijkingsafspraak** met een trigger die niet aan een kalender hangt maar aan gebeurtenissen, plus
  de datum van de laatste herijking.
- De **afwijkingen met motivering**: waar een proceseigenaar van de vuistregels afwijkt en wat hij in plaats
  daarvan heeft geregeld.

## Zo leg je het uit

Tegen een directie die vraagt waarom dit nodig is, terwijl er toch back-ups zijn:

> "Een back-up zegt dat we de gegevens terugkrijgen. Hij zegt niets over de volgorde waarin we weer gaan
> draaien, en dat is de vraag die op tafel ligt als er iets ligt. Als we die volgorde niet vooraf bepalen,
> bepaalt de toevalligheid van dat moment hem, of degene die het hardst roept."

Tegen een proceseigenaar die dit als extra werk ziet:

> "Ik kom niet vragen of jouw proces belangrijk is. Ik kom vragen wat er gebeurt als het drie dagen stilligt,
> en of jij daar dan mee kunt leven. Als het antwoord ja is, zijn we in vijf minuten klaar."

De kortste versie: **niet alles kan tegelijk terug, dus iemand kiest de volgorde. De vraag is alleen of dat
vooraf gebeurt of tijdens de calamiteit.**
