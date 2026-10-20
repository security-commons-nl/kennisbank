# Procedure afwijking van het beleid

> **Herkomst:** procedure van het team informatiebeveiliging en privacy (IB&P) van een regionale samenwerking van gemeenten, versie 0.1 (maart 2024), geschreven onder de eerste BIO. Voor de commons herschreven in een vaste opbouw en gekoppeld aan BIO 2.0.

## Doel

Soms kan of moet een afdeling afwijken van het informatiebeveiligings- of privacybeleid. Dat mag, mits het
is aangevraagd, gewogen, besloten en bijgehouden, met een einddatum en een plan om weer aan het beleid te
voldoen. Een afwijking die niet is aangevraagd, is een beveiligingsincident en wordt zo behandeld.

## Wanneer

Bij elke situatie waarin een regel uit het beleid niet kan worden nageleefd: een applicatie die geen MFA
ondersteunt, een leverancier die een eis niet haalt, een werkproces dat een uitzondering nodig heeft. Niet
voor eenmalige incidenten; wel voor alles wat langer dan een paar dagen duurt.

## Rollen

| Rol | Doet |
|---|---|
| Aanvrager | Dient de aanvraag in via het formulier en stelt na goedkeuring het verbeterplan op |
| ISO's en privacy officers (team IB&P) | Registreren, maken het risicoprofiel, documenteren het besluit, eisen het verbeterplan |
| CISO | Eindverantwoordelijk voor de beoordeling; controleert de lijst jaarlijks |
| MT IT | Besluit over de aanvraag en koppelt terug |

## Stappen

| # | Stap | Wanneer | Wat | R | A | I |
|---|---|---|---|---|---|---|
| 1 | Aanvraag | Continu | Via het formulier "Aanvragen beleidsafwijking" | Aanvrager | Aanvrager | |
| 2 | Beoordeling | | Registratie in de afwijkingenlijst; team IB&P maakt een risicoprofiel op basis van de aangeleverde informatie | ISO's en PO's | CISO | |
| 3 | Besluit | | Het risicoprofiel gaat naar het MT IT, dat definitief beslist | ISO's en PO's | CISO | Aanvrager |
| 4 | Terugkoppeling | | Het MT IT meldt het besluit aan team IB&P en de aanvrager; in de lijst komt goedgekeurd of afgewezen, bij goedkeuring met vervaldatum | MT IT | MT IT | Aanvrager, team IB&P |
| 5 | Documentatie | | Het besluit en de vervaldatum staan in de lijst | ISO's en PO's | CISO | |
| 6 | Verbeterplan | | Team IB&P eist van de aanvrager een plan om binnen de termijn weer aan het beleid te voldoen | ISO's en PO's | CISO | Aanvrager |
| 7 | Controle | Jaarlijks | De lijst wordt nagelopen op juistheid en verlopen afwijkingen | CISO | CISO | |

## Aanvulling van de commons

> Twee punten die de oorspronkelijke procedure open laat.

- **Een verlopen afwijking is een nieuwe aanvraag**, geen stilzwijgende verlenging. Zet in stap 7 dat elke
  afwijking waarvan de vervaldatum is verstreken, terug naar stap 1 gaat, en dat de aanvrager daar een maand
  vooraf op wordt gewezen.
- **Koppel de afwijkingenlijst aan het risicoregister.** Een goedgekeurde afwijking is een geaccepteerd
  risico en hoort met eigenaar en termijn in het register van het managementsysteem, niet alleen in een
  losse lijst.

## Vastlegging en bewijs

- De **afwijkingenlijst** met per afwijking: aanvrager, risicoprofiel, besluit, vervaldatum, verbeterplan, status.
- Het **verslag van de jaarlijkse controle** door de CISO.
- De **MT-besluiten** over afwijkingen, terug te vinden in de verslagen van het MT IT.

## BIO 2.0

De oorspronkelijke procedure verwees naar BIO-maatregel 5.18 (toegangsrechten), omdat de eerste BIO geen
maatregel over beleidsafwijkingen kende. In BIO 2.0 is dat anders.

| Maatregel | Wat deze procedure daarvoor levert |
|---|---|
| 5.36 Naleving van beleid, regels en normen voor informatiebeveiliging | Afwijkingen worden geregistreerd, gewogen en periodiek gecontroleerd |
| 5.4 Managementverantwoordelijkheden | Het besluit ligt bij het management (MT IT), niet bij de uitvoering |
| 5.18 Toegangsrechten | Voor afwijkingen in toegangsrechten: een ongeautoriseerde afwijking is een beveiligingsgebeurtenis |
