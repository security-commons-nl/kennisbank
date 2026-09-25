---
titel: Ben ik aanbieder onder de AI Act?
vakgebied: governance
type: sjabloon
normen: [AI Act]
peildatum: 2026-09-25
herkomst: uitgewerkt vanuit de CISO-praktijk bij gemeenten die eigen AI-toepassingen bouwen, op basis van de tekst van de AI Act na de wijziging van juli 2026
status: concept
samenvatting: Klikbare toets waarmee een gemeente per AI-toepassing vastlegt of zij aanbieder of gebruiksverantwoordelijke is, en of de toepassing hoog risico is. Wie zelf een toepassing samenstelt, ook op een ingekocht platform en ook voor intern gebruik, is aanbieder. Bij hoog risico is dat het verschil tussen een gebruikersplicht en een conformiteitsbeoordeling met CE-markering. Levert een classificatiebesluit met onderbouwing. Rekent in de browser.
---

# Ben ik aanbieder onder de AI Act?

> **Doe de toets online:** [security-commons-nl.github.io/kennisbank/governance/aanbieder-onder-de-ai-act](https://security-commons-nl.github.io/kennisbank/governance/aanbieder-onder-de-ai-act/)

De AI Act kent twee hoofdrollen. De **aanbieder** ontwikkelt een AI-systeem, of laat het ontwikkelen, en
brengt het onder eigen naam in de handel of in gebruik. De **gebruiksverantwoordelijke** gebruikt een
AI-systeem onder eigen verantwoordelijkheid. De meeste gemeenten gaan er stilzwijgend van uit dat zij
gebruiker zijn. Dat klopt zolang ze een product afnemen en gebruiken zoals de leverancier het bedoelt.

Het kantelt zodra de gemeente zelf iets samenstelt. Een assistent op een ingekocht platform, met eigen
instructies, een eigen kennisbron of een eigen agent, is een AI-systeem dat de gemeente heeft ontwikkeld.
"In gebruik stellen" omvat ook gebruik door de eigen organisatie (art. 3 lid 11). Ook bij uitsluitend
intern gebruik ben je dus aanbieder van wat je zelf samenstelt. Je rol hangt af van wat je op het platform
bouwt, en niet van wie het platform levert.

## Waarom dat ertoe doet

Voor een toepassing zonder hoog risico is het verschil klein. Beide rollen hebben dan vooral de
transparantieplicht (art. 50) en de plicht om AI-geletterdheid te ondersteunen (art. 4).

Bij hoog risico is het verschil groot. Een **gebruiksverantwoordelijke** gebruikt het systeem volgens de
instructies, organiseert menselijk toezicht, bewaart de logs, registreert als overheid het gebruik in de
EU-databank en voert een grondrechteneffectbeoordeling uit (art. 26, 27 en 49). Een **aanbieder** heeft
een kwaliteitsbeheersysteem en technische documentatie nodig, laat de conformiteit beoordelen, brengt een CE-markering aan, registreert
het systeem in de EU-databank, houdt het na ingebruikname in de gaten en meldt ernstige incidenten
(art. 16, 43, 49, 72 en 73). Reken op maanden werk per toepassing. Deel je de toepassing met andere
gemeenten, dan ben je ook hun aanbieder, met de aansprakelijkheid die daarbij hoort.

Voor systemen uit bijlage III gelden de hoog-risicoverplichtingen vanaf 2 december 2027. Die datum is in
juli 2026 verschoven door Verordening (EU) 2026/1744. De transparantieplicht geldt al sinds 2 augustus
2026.

## Wat de toets doet

De toets loopt vijf stappen langs:

1. **Is het een AI-systeem?** Een vaste rekenregel valt erbuiten, een taalmodel valt erbinnen.
2. **Hoe komt de toepassing tot stand?** Ongewijzigd ingekocht, zelf samengesteld op een platform of
   model, of zelf (laten) ontwikkeld. En: gaat hij ook naar andere organisaties?
3. **Is hij hoog risico?** Gemeenten raken vooral bijlage III punt 5 onder a (beoordelen of inwoners
   recht hebben op een uitkering, voorziening of dienst, en die toekennen, verlagen, intrekken of
   terugvorderen) en punt 4 (werving, selectie en beoordeling van medewerkers). De uitzondering van
   art. 6 lid 3 geldt voor een beperkte procedurele of voorbereidende taak, en nooit bij profilering.
4. **Word je aanbieder van andermans systeem?** Een ingekocht systeem wordt het jouwe als je er je
   eigen naam op zet, het wezenlijk wijzigt, of het doel zo verandert dat het hoog risico wordt
   (art. 25 lid 1). Denk aan een algemeen taalmodel dat je inzet om aanvragen te beoordelen.
5. **Wie ziet de uitkomst?** Hebben inwoners rechtstreeks met de toepassing te maken, of gaat wat zij
   maakt naar buiten, dan geldt de transparantieplicht van art. 50, bij elk risiconiveau.

De toets levert een **classificatiebesluit**: rol, risiconiveau, de verplichtingen die daaruit volgen,
per vraag je onderbouwing, en de punten die naar een jurist moeten. Leg dat besluit per toepassing vast en
toets opnieuw als het doel van de toepassing verandert.

## Waar het kantelt

**Intern of voor inwoners.** Een subsidiewijzer die medewerkers helpt de juiste regeling te vinden, is
laag risico. Dezelfde wijzer als chatbot die inwoners vertelt of zij in aanmerking komen, beoordeelt
geschiktheid voor een publieke dienst en valt onder bijlage III. Het model en de code zijn gelijk; het
doel is anders.

**Voorbereiden of beslissen.** Een samenvatting van een dossier voor de behandelaar is voorbereidend
werk. Een advies "toekennen" of "afwijzen" dat de behandelaar meestal overneemt, beïnvloedt het besluit.
De uitzondering van art. 6 lid 3 vraagt dat je dat verschil onderbouwt en vastlegt (art. 6 lid 4).

**Samen bouwen.** Een voorziening die meerdere gemeenten samen gebruiken, heeft één aanbieder nodig die
de plichten draagt. Leg vast wie dat is voordat de eerste toepassing live gaat.

## Wat je erbij nodig hebt

Een beschrijving van de toepassing en het doel waarvoor hij wordt ingezet · de gebruikersgroep (medewerkers,
inwoners, of beide) · het contract en de gebruiksvoorwaarden van leverancier of platform · een overzicht
van wat de gemeente zelf heeft toegevoegd (instructies, kennisbronnen, koppelingen, agents) · het proces
waarin de uitkomst wordt gebruikt en wie daarin beslist.

## Daarna

Hoog risico en aanbieder: overweeg of je dit zelf wilt dragen. Een leverancier of een samenwerkingsverband
dat de rol van aanbieder op zich neemt, kan dezelfde techniek leveren terwijl de zwaarste plichten bij hen
liggen. Kies je er bewust voor, begroot dan de conformiteitsbeoordeling en het beheer erna.

Laag risico: leg het classificatiebesluit vast en zet de toepassing in het algoritmeregister. Noteer
wat hem hoog risico zou maken, zodat een wijziging van het doel opvalt.

Voor de beveiliging van een zelf gebouwde voorziening: [Open-source AI binnenhalen onder de Cbw](../../security/open-source-ai-binnenhalen/).
Voor de meldplicht bij incidenten: [Wanneer meld je een AI-incident?](../../security/ai-incident-melden/).
Voor het beleid eromheen: [AI-beleid van een regionale samenwerking](../ai-beleid/).

## Bronnen

- [AI Act, Verordening (EU) 2024/1689](https://eur-lex.europa.eu/eli/reg/2024/1689/oj), art. 3 lid 3, 4 en 11 (aanbieder, gebruiksverantwoordelijke, in gebruik stellen), art. 6 (classificatie en uitzondering), art. 25 lid 1 (verantwoordelijkheden in de keten), art. 26 en 27 (gebruiksverantwoordelijke en grondrechteneffectbeoordeling), art. 50 (transparantie), bijlage III punt 4 en 5
- Verordening (EU) 2026/1744 (digitale omnibus AI), in werking sinds 27 juli 2026: hoog-risicoverplichtingen voor bijlage III vanaf 2 december 2027, art. 4 omgezet in een inspanningsverplichting

Deze toets structureert en documenteert de analyse. Hij vervangt geen juridisch advies.

## Licentie

[EUPL-1.2](../../LICENSE).
