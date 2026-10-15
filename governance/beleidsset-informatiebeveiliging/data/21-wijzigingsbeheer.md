---
domein: wijzigingsbeheer
titel: Beleid wijzigingsbeheer
samenvatting: Regelt hoe een wijziging in productie wordt aangevraagd, beoordeeld, getest, goedgekeurd en doorgevoerd. Behandelt het wijzigingsproces met standaard-, normale en spoedwijzigingen, werkinstructies voor beheertaken, het installeren van software, de scheiding van omgevingen en acceptatietesten.
invoeren:
  - Kies een beheerraamwerk, zoals ITIL of BiSL, en leg de processtappen vast (hoofdstuk 3).
  - Richt een wijzigingsregister in met risicoklasse, testplan, rollbackplan en besluit per wijziging (hoofdstuk 3).
  - Wijs een wijzigingsmanager en een spoedgoedkeurder aan (hoofdstuk 3).
  - Leg de goedkeuring per soort wijziging vast en maak draaiboeken voor standaardwijzigingen (hoofdstuk 3).
  - Leg werkinstructies voor terugkerende beheertaken vast in de beheerdocumentatie (hoofdstuk 4).
  - Trek lokale beheerrechten in en stel een lijst van toegestane software op (hoofdstuk 5).
  - Scheid ontwikkel-, test-, acceptatie- en productieomgevingen met eigen accounts en rechten (hoofdstuk 6).
  - Stel een vaste testmethode voor acceptatietesten vast, met testplan en testverslag (hoofdstuk 7).
---

## 1. Doel en reikwijdte

Dit beleid werkt het strategisch informatiebeveiligingsbeleid uit voor wijzigingen in informatiesystemen,
infrastructuur, software en configuratie in de productieomgeving. Het regelt hoe een wijziging wordt
aangevraagd, beoordeeld, getest, goedgekeurd en doorgevoerd, hoe omgevingen gescheiden zijn, hoe
beheertaken zijn beschreven en wie software mag installeren, zodat een wijziging de beschikbaarheid,
integriteit en vertrouwelijkheid van informatie niet onbedoeld aantast. Het gaat over de
ISO-beheersmaatregelen 5.37, 8.19, 8.29, 8.31, 8.32 en 8.33.

**Voor wie.** Het beleid is primair bedoeld voor de beheerorganisatie, de wijzigingsmanager, functioneel
beheer en de systeem- en proceseigenaren. Het geldt ook voor leveranciers die wijzigingen doorvoeren op
systemen van de organisatie en voor iedereen die software op een apparaat van de organisatie wil
installeren.

**Waarop.** Alle systemen, netwerken, clouddiensten en werkplekken waarmee de organisatie informatie
verwerkt, en de ontwikkel-, test- en acceptatieomgevingen die daarbij horen. Is het beheer uitbesteed, dan
gelden de eisen uit dit beleid als minimumeis voor de leverancier. De organisatie legt dat vast in het
contract en toetst de naleving met een onafhankelijke verklaring, zoals een ISO 27001-certificaat of een
ISAE 3402- of ISAE 3000-rapport; het vastleggen loopt via het beleid informatiebeveiliging bij inkoop, het
toetsen via het beleid contractbeheer.

Buiten dit beleid vallen de eisen aan het bouwen van software en de regels voor testgegevens (beleid
veilige softwareontwikkeling; de regel over testgegevens staat hier verkort herhaald), de termijnen voor
het verhelpen van kwetsbaarheden (beleid kwetsbaarheden en patchmanagement; het doorvoeren van een patch
loopt wel via dit proces, als standaardwijziging) en de rechten in productie (beleid logische
toegangsbeveiliging).

::: als beheer=regie
De organisatie stuurt, een leverancier voert het beheer uit. Het wijzigingsproces van de leverancier is
leidend voor de uitvoering; de organisatie houdt de goedkeuring van wijzigingen met gevolgen voor haar
processen of informatie en legt dit beleid als eis in het contract.
:::

::: als beheer=uitbesteed
Het beheer is volledig uitbesteed. De leverancier voert wijzigingsbeheer uit volgens dit beleid, zoals
vastgelegd in het contract. De organisatie keurt wijzigingen goed die haar processen of informatie raken en
ontvangt elke maand een overzicht van alle doorgevoerde wijzigingen.
:::

## 2. Uitgangspunten

1. Elke wijziging in productie is vastgelegd, beoordeeld en goedgekeurd voordat hij wordt doorgevoerd.
   Spoedwijzigingen worden achteraf binnen vijf werkdagen beoordeeld.
2. Er wordt niet getest in productie.
3. Elke wijziging heeft een weg terug.
4. Hoe groter het risico van een wijziging, hoe zwaarder de beoordeling en de goedkeuring. Het
   impactniveau van de betrokken informatie weegt daarin mee.
5. Terugkerend beheerwerk staat beschreven, zodat het niet van één persoon afhangt en elke uitvoerder
   het op dezelfde manier doet.
6. Termijnen en frequenties in dit beleid die niet uit een wet of uit de BIO 2.0 komen, zijn standaardwaarden.
   De organisatie past ze aan op haar eigen risicoafweging en legt de keuze vast bij de vaststelling van dit beleid.

## 3. Het wijzigingsproces

- [[lijneigenaar wijzigingsbeheer: de manager die dit beleid uitvoert, bijvoorbeeld het hoofd IT]] richt
  wijzigingsbeheer in volgens een algemeen geaccepteerd beheerraamwerk, bijvoorbeeld ITIL of ISO/IEC 20000
  voor technisch beheer en BiSL voor functioneel beheer, en legt vast welk raamwerk geldt en welke
  processtappen daaruit volgen. [8.32.02]
- Elke wijziging staat in [[wijzigingsregister: het systeem waarin wijzigingen worden vastgelegd, bijvoorbeeld het ticketsysteem]]
  met: omschrijving, aanvrager, betrokken systemen, risicoklasse, testplan en testresultaten, rollbackplan,
  besluit en datum van doorvoeren. De wijzigingsmanager bewaakt dat geen wijziging buiten het register om
  gaat. [8.32.01]
- Elke wijziging krijgt van de aanvrager een risicoafweging van de mogelijke gevolgen voor
  beschikbaarheid, integriteit en vertrouwelijkheid, met een beschreven plan om terug te gaan naar de vorige
  situatie (rollback). [8.32.01]
- Wijzigingen vallen in drie soorten, elk met een eigen goedkeuring: [8.32.01]
  - standaardwijzigingen: vooraf beoordeelde, terugkerende wijzigingen met laag risico (zoals reguliere
    updates en patches), als type goedgekeurd door het wijzigingsoverleg en uitgevoerd volgens een vast
    draaiboek;
  - normale wijzigingen: beoordeeld en goedgekeurd door het wijzigingsoverleg (CAB), met de
    systeemeigenaar en, bij een hoog risico of informatie met impactniveau kritiek of hoger, advies van de
    CISO;
  - spoedwijzigingen: goedgekeurd door
    [[spoedgoedkeurder: de functie die buiten het overleg mag goedkeuren, bijvoorbeeld de dienstdoende IT-manager]]
    en achteraf binnen vijf werkdagen in het wijzigingsoverleg beoordeeld.
- Na het doorvoeren controleert de uitvoerder of de wijziging werkt zoals bedoeld en sluit hij de
  wijziging pas af na die controle, met het resultaat in het register. Een mislukte wijziging draait de
  uitvoerder terug volgens het rollbackplan en meldt hij aan de wijzigingsmanager. [8.32.01]
- Wijzigingen door leveranciers op systemen van de organisatie lopen via hetzelfde register en dezelfde
  goedkeuring, ook als de leverancier eigen accounts gebruikt. [8.32.01]
- De wijzigingsmanager rapporteert maandelijks aan de lijneigenaar het aantal wijzigingen per soort, de
  mislukte en teruggedraaide wijzigingen en de spoedwijzigingen met hun beoordeling achteraf. [8.32.01]

::: als beheer=eigen
- Het wijzigingsoverleg komt ten minste wekelijks bijeen, onder voorzitterschap van de wijzigingsmanager
  van de eigen IT-afdeling, en legt zijn besluiten vast in het register. De uitvoerder van een wijziging
  keurt zijn eigen wijziging niet goed. [8.32.01]
:::

::: als beheer=regie,uitbesteed
- In het contract staat welke wijzigingen de leverancier zelf mag goedkeuren (standaardwijzigingen) en
  welke de organisatie vooraf goedkeurt. De organisatie heeft een vaste vertegenwoordiger in het
  wijzigingsoverleg van de leverancier. Het wijzigingsregister van de leverancier is voor de organisatie in
  te zien en de contracteigenaar toetst het jaarlijks aan dit beleid. [8.32.01, 8.32.02]
:::

## 4. Bedieningsprocedures

- Voor terugkerende beheertaken (starten en stoppen van systemen, back-up en herstel, standaardwijzigingen,
  verwerken van batches, afhandelen van storingen en meldingen, onderhoud en opschonen van logging) legt de
  beheerorganisatie werkinstructies vast in
  [[beheerdocumentatie: de plek waar werkinstructies staan, bijvoorbeeld de kennisbank van de beheerorganisatie]].
  [5.37.01]
- Een werkinstructie beschrijft ten minste: wie de taak uitvoert, de stappen in volgorde, de
  afhankelijkheden van andere systemen, wat te doen bij een fout, wie te waarschuwen en waar de uitkomst
  wordt vastgelegd. [5.37.01]
- De werkinstructies zijn beschikbaar voor wie ze nodig heeft en voor niemand anders. De eigenaar van het
  systeem of de dienst werkt ze bij na elke wijziging die de taak raakt en beoordeelt ze ten minste jaarlijks
  op actualiteit; een wijziging van een werkinstructie wordt als wijziging goedgekeurd. [5.37.01]

::: als beheer=regie,uitbesteed
- De leverancier houdt de werkinstructies voor de uitbestede taken bij; de organisatie heeft inzage in de
  instructies die haar systemen raken en in de instructies voor herstel na een storing. [5.37.01]
:::

## 5. Software installeren

- Gebruikers hebben geen lokale beheerrechten op hun werkplek. Software komt alleen op werkplekken en
  servers via de softwarecatalogus of een goedgekeurde wijziging, geïnstalleerd door de beheerorganisatie
  of door een geautomatiseerde uitrol onder haar beheer. [8.19.01]
- De beheerorganisatie houdt een lijst bij van toegestane software, met per product de versie die in
  gebruik mag zijn. Het installeren of uitvoeren van software buiten die lijst wordt technisch
  tegengehouden, bijvoorbeeld met applicatiewhitelisting, of minstens gedetecteerd en binnen
  [[termijn verwijderen software: bijvoorbeeld vijf werkdagen]] verwijderd. [8.19.01]
- Een verzoek om nieuwe software toetst de beheerorganisatie op leverancier, licentie, beveiliging en
  privacy voordat de software in de catalogus komt; de CISO adviseert bij software die toegang krijgt tot
  informatie met impactniveau kritiek of hoger. [8.19.01]
- Van software op servers en werkplekken bewaart de beheerorganisatie de vorige versie zolang die nodig
  is om terug te kunnen, en verwijdert zij versies die de leverancier niet meer ondersteunt volgens het
  beleid kwetsbaarheden en patchmanagement. [8.19.01]

## 6. Scheiding van omgevingen

- Ontwikkeling, test, acceptatie en productie zijn gescheiden omgevingen, met eigen accounts en rechten,
  zodat een fout of een aanval in de ene omgeving de andere niet raakt. Voor een systeem zonder eigen
  test- of acceptatieomgeving legt de systeemeigenaar vast hoe wijzigingen wel vooraf worden getest. [8.31.01]
- In de productieomgeving wordt niet getest. Is een test in productie onvermijdelijk, dan keurt de
  proceseigenaar die vooraf schriftelijk goed, met de omvang, het tijdvak en de maatregelen om schade te
  voorkomen; de goedkeuring hoort bij de wijziging in het register. [8.31.01]
- Significante wijzigingen worden getest in een omgeving buiten productie voordat ze in productie gaan.
  Afwijken kan alleen met voorafgaande goedkeuring van de proceseigenaar, die het risico vastlegt. [8.31.02]
- Ontwikkel- en testomgevingen zijn herkenbaar als zodanig, bijvoorbeeld in de naam en op het scherm, en
  hebben geen koppeling naar productiesystemen van andere organisaties zonder goedkeuring van de
  systeemeigenaar. [8.31.01]
- Testgegevens volgen de regels in het beleid veilige softwareontwikkeling: fictieve gegevens, en
  persoonsgegevens alleen als onderbouwde uitzondering met advies van de privacy officer en de CISO. De
  systeemeigenaar legt bij elke acceptatietest vast welke gegevens zijn gebruikt. [8.33.01]
- Zijn in een testomgeving toch productiegegevens gebruikt, dan heeft die omgeving dezelfde beveiliging als
  productie en verwijdert de beheerorganisatie de gegevens direct na de test; het verwijderen staat in het
  register bij de wijziging. [8.33.01]

## 7. Testen en acceptatie

- Acceptatietesten volgen een vaste testmethode: een testplan met testgevallen afgeleid van de
  functionele eisen en de beveiligingseisen, uitgevoerd door of namens de systeemeigenaar. Bij een wijziging
  met een hoog risico of aan een internetbereikbaar systeem bevat het testplan ook een beveiligingstest,
  zoals een controle van de instellingen of een penetratietest. [8.29.01]
- Tests die vaker terugkomen (regressietests, controles op beveiligingsinstellingen) automatiseert de
  beheerorganisatie waar het kan, en de uitkomst wordt bij de wijziging bewaard. [8.29.01]
- Van elke acceptatietest maakt de tester een verslag met de uitgevoerde tests, de resultaten, de
  openstaande bevindingen en het besluit tot acceptatie door de systeemeigenaar. Het verslag hoort bij de
  wijziging in het register. [8.29.01]

::: als ontwikkeling=ja
- Voor eigen software voert de bouwstraat bij elke wijziging automatisch unit-, integratie- en
  beveiligingstests uit. Uitrol naar productie gebeurt alleen via de bouwstraat, na goedkeuring in het
  wijzigingsregister; ontwikkelaars hebben geen schrijfrechten in productie. [8.29.01, 8.31.01, 8.32.01]
:::

::: als ontwikkeling=nee
- Bij een nieuwe versie van een leverancier test de organisatie zelf in de acceptatieomgeving de eigen
  processen, koppelingen en autorisaties, naast het testverslag van de leverancier, voordat de
  systeemeigenaar de versie accepteert. [8.29.01, 8.31.02]
:::

## 8. Rollen en verantwoordelijkheden

| Rol | Verantwoordelijk voor |
|---|---|
| [[lijneigenaar wijzigingsbeheer]] | Eigenaar van dit beleid; inrichting van het wijzigingsproces en de middelen ervoor; opvolging van de maandrapportage |
| Wijzigingsmanager | Het wijzigingsregister, het wijzigingsoverleg, de beoordeling van spoedwijzigingen achteraf en de maandrapportage |
| [[beheerorganisatie: de eigen afdeling of de leverancier die de systemen beheert]] | Werkinstructies, de lijst van toegestane software, het installeren van software, de scheiding van omgevingen en het uitvoeren van wijzigingen |
| Systeemeigenaar | Beoordeling van wijzigingen op zijn systeem, acceptatietests en acceptatiebesluit, vastleggen van de testaanpak en de gebruikte testgegevens |
| Proceseigenaar | Goedkeuring van afwijkingen: testen in productie of niet vooraf testen |
| [[spoedgoedkeurder]] | Goedkeuring van spoedwijzigingen buiten het overleg |
| Contracteigenaar | Vastleggen van dit beleid in contracten met beheerpartijen en toetsen van hun wijzigingsregister en verklaringen |
| CISO | Advies bij wijzigingen met een hoog risico en bij nieuwe software met toegang tot kritieke informatie, jaarlijkse toetsing van dit beleid |
| Leveranciers | Wijzigingen aanmelden en doorvoeren volgens dit beleid, werkinstructies voor uitbestede taken bijhouden |

## 9. Naleving en controle

**Controleraamwerk.** De naleving van dit beleid wordt met de volgende controles aangetoond. De uitkomst en
het bewijs worden vastgelegd in [[registratie van controles]]; afwijkingen gaan als bevinding naar het
risicoregister.

| Nr | Controle | Uitvoerder | Frequentie | Bewijs | Maatregelen |
|---|---|---|---|---|---|
| WZB-01 | Elke doorgevoerde wijziging staat in het register met risicoafweging, rollbackplan, testverslag, goedkeuring door de juiste rol en de controle na doorvoeren | Wijzigingsmanager | Per kwartaal | Steekproef van tien wijzigingen uit het register, vergeleken met de wijzigingslogging van de systemen | 8.32.01 |
| WZB-02 | Elke spoedwijziging is binnen vijf werkdagen achteraf beoordeeld en het aandeel spoedwijzigingen is gerapporteerd | [[lijneigenaar wijzigingsbeheer]] | Maandelijks | Maandrapportage met de spoedwijzigingen en de datum van de beoordeling achteraf | 8.32.01 |
| WZB-03 | Het wijzigingsproces volgt het vastgelegde beheerraamwerk en is bij beheerpartijen in het contract vastgelegd en aantoonbaar toegepast | CISO | Jaarlijks | Vastgelegde procesbeschrijving, contracten, inzage in het register van de leverancier of een onafhankelijke verklaring | 8.32.02 |
| WZB-04 | Voor elke terugkerende beheertaak van een systeem met impactniveau kritiek of hoger bestaat een werkinstructie die ten hoogste een jaar oud is, de verplichte onderdelen bevat en alleen voor bevoegden toegankelijk is | [[lijneigenaar wijzigingsbeheer]] | Jaarlijks | Lijst van beheertaken per systeem met de bijbehorende werkinstructie, datum van de laatste beoordeling, rechtenoverzicht van de beheerdocumentatie | 5.37.01 |
| WZB-05 | De geïnstalleerde software op werkplekken en servers komt overeen met de lijst van toegestane software, gebruikers hebben geen lokale beheerrechten en software buiten de lijst is binnen de termijn verwijderd | [[beheerorganisatie]] | Per kwartaal | Rapport uit het beheertool vergeleken met de lijst, overzicht van lokale beheerrechten, afhandeling per afwijking | 8.19.01 |
| WZB-06 | Ontwikkel-, test-, acceptatie- en productieomgevingen zijn gescheiden met eigen accounts en rechten, en elke test in productie of niet vooraf geteste significante wijziging heeft een voorafgaande goedkeuring van de proceseigenaar | CISO | Jaarlijks | Rechtenoverzicht per omgeving, uittreksel uit het register met de goedkeuringen van de proceseigenaar | 8.31.01, 8.31.02 |
| WZB-07 | Elke significante wijziging heeft een acceptatietestverslag volgens de vaste methode, met een beveiligingstest bij een hoog risico of een internetbereikbaar systeem, en een acceptatiebesluit van de systeemeigenaar | Wijzigingsmanager | Per kwartaal | Steekproef van vijf significante wijzigingen met het testplan, het verslag en het besluit | 8.29.01 |
| WZB-08 | Bij elke acceptatietest is vastgelegd welke testgegevens zijn gebruikt, en bij gebruik van productiegegevens zijn het advies en de verwijdering aantoonbaar | Privacy officer | Jaarlijks | Steekproef van vijf acceptatietests met de registratie van de testgegevens, adviezen en verwijderingen | 8.33.01 |

**Afwijkingen.** Afwijken van een eis kan alleen op basis van een gedocumenteerde risicoafweging. De
systeemeigenaar dient het verzoek in bij de CISO, met de reden, de compenserende maatregelen en de looptijd.
De afwijking geldt pas na acceptatie van het risico door [[risico-eigenaar: de manager die restrisico's accepteert]]
en staat in het risicoregister; afwijkingen worden ten minste jaarlijks opnieuw beoordeeld.

**Niet naleven.** Het niet naleven van dit beleid wordt behandeld als beveiligingsincident en kan leiden tot
het intrekken van toegangsrechten of tot maatregelen volgens de rechtspositieregeling of het contract.

## 10. Samenhang

Dit beleid valt onder het strategisch informatiebeveiligingsbeleid. Het raakt het beleid veilige
softwareontwikkeling (testgegevens, bouwstraat en acceptatie van opleveringen), het beleid kwetsbaarheden
en patchmanagement (patches als standaardwijziging, configuratiebeheer en software zonder updates), het
beleid informatieclassificatie (impactniveau als maat voor de zwaarte van de beoordeling), het beleid
informatiebeveiliging bij inkoop en contractbeheer (afspraken over wijzigingen door leveranciers), het beleid
back-up en recovery (werkinstructies voor back-up en herstel) en het beleid logische toegangsbeveiliging
(rechten in productie en in de beheerdocumentatie).
