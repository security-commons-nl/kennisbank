---
titel: Acht procedures voor informatiebeveiliging, van incident tot beleidsafwijking
vakgebied: security
type: aanpak
normen: [BIO2, AVG]
peildatum: 2026-10-20
herkomst: procedures van het team informatiebeveiliging en privacy (IB&P) van een regionale samenwerking van gemeenten, opgesteld 2024 tot 2025
status: in gebruik
route: [eerste-honderd-dagen]
samenvatting: De procedures die een IB&P-team dagelijks nodig heeft, als startpunt voor je eigen set. Een incidentprocedure voor datalekken en beveiligingsincidenten met de meldplicht onder AVG en Cbw, cyberdreigingen en kwetsbaarheden beoordelen met een handelingskader per risiconiveau, afwijkingen van beleid aanvragen en bijhouden, classificatie van systemen op beschikbaarheid, integriteit en vertrouwelijkheid (BIV), inzage in de mailbox van een collega, de periodieke rapportage, leveranciersmanagement en het vaststellen van strategisch beleid. Per procedure staat erbij voor welke BIO 2.0-maatregelen hij bewijs helpt leveren.
barrieres: [vuln, exploitresponse, review, treatment]
rol: alternatief
---

# Acht procedures voor informatiebeveiliging, van incident tot beleidsafwijking

> **Lees de procedures online:** [security-commons-nl.github.io/kennisbank/security/procedures-informatiebeveiliging](https://security-commons-nl.github.io/kennisbank/security/procedures-informatiebeveiliging/)

Beleid zegt wat er moet. Een procedure zegt wie wat doet als het zover is. Deze acht komen uit de praktijk
van een team dat informatiebeveiliging en privacy regelt voor meerdere gemeenten tegelijk. Voor de commons
zijn ze in één vaste opbouw gezet: doel, wanneer, rollen, stappen, vastlegging en bewijs, en per procedure
de BIO 2.0-maatregelen waarvoor zij bewijs helpt leveren. Waar de oorspronkelijke procedure iets open liet
dat BIO 2.0 of de Cyberbeveiligingswet wel vraagt, staat dat in een apart blok *Aanvulling van de commons*,
zodat je ziet wat van het team is en wat erbij is gezet.

De twee kernprocedures, datalekken en beveiligingsincidenten en cyberdreigingen en kwetsbaarheden, zijn
uitgewerkt als handleiding, met "Wanneer wel, wanneer niet", "Bewijs" en "Zo leg je het uit".

## Wat er in deze map staat

| Procedure | Waarvoor | BIO 2.0 |
|---|---|---|
| [Datalekken en beveiligingsincidenten](incident-response.md) | Van melding tot verbeterplan, met rollen per stap, de meldplicht aan de Autoriteit Persoonsgegevens, P1-criteria en vragen voor tijdens het incident | 5.24 t/m 5.28, 5.34, 6.8; AVG art. 33 en 34; Cbw-meldplicht als aanvulling |
| [Cyberdreigingen en kwetsbaarheden](cyberdreigingen-en-kwetsbaarheden.md) | Een dreiging is nog geen incident. Kans maal impact, drie risiconiveaus met doorlooptijden, wie je informeert, en twee vuistregels: "zien is doen" en "toch escaleren" | 5.7, 8.8, 5.25, 5.4 |
| [Afwijking van het beleid](afwijking-van-beleid.md) | Aanvragen, beoordelen, besluiten en jaarlijks nalopen, met vervaldatum en verbeterplan | 5.36, 5.4 |
| [Security classificatie](security-classificatie.md) | De BIV-classificatie per applicatie, met een vragenlijst voor beschikbaarheid, integriteit en vertrouwelijkheid en de vier niveaus per aspect | 5.12, 5.9, 5.13 |
| [Inzage in mailbox of documenten](inzage-mailbox-en-documenten.md) | Wanneer een collega in de mailbox van een ander mag, wie dat toetst en wie het goedkeurt | 5.15, 5.18, 5.34, 8.15 |
| [Rapporteren](rapporteren.md) | Een kwartaalrapportage uit vier delen: risicoprofiel, voortgang, indicatoren en problemen | 5.4, 5.36; ISO 27001 9.1 en 9.3 |
| [Leveranciersmanagement](leveranciersmanagement.md) | Grip op leveranciers die gevoelige informatie verwerken, met een vragenlijst voor het periodieke leveranciersoverleg | 5.19, 5.20, 5.21, 5.22 |
| [Vaststellen strategisch beleid](vaststellen-strategisch-beleid.md) | De route langs de gremia van een regionale samenwerking tot vaststelling door de colleges | 5.1, 5.4, 5.36 |

De nummers zijn de ISO 27002-nummers waaronder BIO 2.0 zijn overheidsmaatregelen ordent. Een procedure
helpt bewijs leveren voor zo'n maatregel; hij is niet het hele bewijs. Dat is pas rond als je laat zien dat
de procedure ook gevolgd wordt: een ingevuld register, een rapportage, een verslag van een oefening.

## Hoe je ze gebruikt

Neem ze niet een op een over. Vervang de rollen door die van je eigen organisatie en loop elke stap na met
de mensen die hem moeten uitvoeren. Een procedure die niemand kent, werkt niet onder druk.

Begin bij de procedure **cyberdreigingen en kwetsbaarheden**. Die vult het gat tussen een signaal en een
incident, waar de meeste organisaties niets hebben: een kwetsbaarheid met een hoge score is nog geen
incident, maar wachten tot het er een is, is te laat. Het handelingskader per risiconiveau en de regel
"bij twijfel toch escaleren" zijn direct over te nemen.

Zie ook [Incidentprocedures die je hebt geoefend](../incident-response-procedures/) voor de handleiding
bij het oefenen, en [Een digitaal calamiteitenteam opzetten](../../bcm/calamiteitenteam-digitaal-opzetten/)
voor wat er gebeurt als een incident een calamiteit wordt.
