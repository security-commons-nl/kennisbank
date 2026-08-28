---
titel: Herstelprocedure met Temporary Access Pass (sjabloon)
vakgebied: security
type: sjabloon
normen: [BIO2]
versie: 2026-08
herkomst: bijlage bij "Passkeys invoeren"; tekst van de interne herstelpagina van een gemeentelijke uitrol
status: sjabloon
samenvatting: Na de overstap is de Temporary Access Pass (TAP) de enige manier om een passkey te registreren of te herstellen. Dit is de tekst van de interne pagina waarmee het shared service center dat afhandelt, met de stappen voor de medewerker.
---

# Herstelprocedure: Temporary Access Pass

Bijlage bij [Passkeys invoeren](README.md), stap 4 en 8. Zodra phishing-resistente authenticatie wordt
afgedwongen, kan registratie via wachtwoord en MFA niet meer. De TAP-procedure is dan de enige route om
een passkey te registreren, bijvoorbeeld bij een nieuw of verloren toestel. De pagina hieronder is alleen
toegankelijk voor het shared service center en IT.

## Waarom TAP en niets anders

Een Temporary Access Pass is een tijdelijke code die de identity provider uitgeeft en die in de bootstrap-
en recovery-policy als enige registratieroute is toegestaan. Sta je daarnaast wachtwoord plus Authenticator
toe, dan blijft die zwakkere route na de omzetting bestaan en ben je nooit echt wachtwoordloos. De TAP is
kort geldig, wordt uitgegeven door een mens die de aanvrager kent of verifieert, en laat een spoor na.

## De interne pagina (tekst)

> **Herstel toegang**
>
> Privé-mailadres: `[invoerveld]`
> Gebruiker: `[gebruikersnaam@organisatie.nl]`
> `[knop: Verstuur herstel-e-mail]`
>
> **Een Temporary Access Pass (TAP) is geen wachtwoord.**
> De TAP is 2 uur geldig en kan in die periode onbeperkt worden gebruikt. Hij is bedoeld om toegang te
> herstellen wanneer inloggen met een passkey niet meer werkt of nooit is ingesteld.
>
> Na ontvangst van de TAP moet de gebruiker via de beveiligingsinformatiepagina van het account zelf de
> niet-werkende inlogmethoden verwijderen en een nieuwe, geldige methode toevoegen. Zodra alles correct is
> ingesteld, graag de tijdelijke passkey weer verwijderen.

## Werkwijze voor het shared service center

1. Verifieer de aanvrager op een manier die niet via het gecompromitteerde of verloren kanaal loopt:
   persoonlijk aan de balie, of via een vooraf bekend privé-mailadres of telefoonnummer uit het
   HR-systeem. Geen TAP op verzoek via een onbekend kanaal.
2. Geef de TAP uit via de interne pagina; de code gaat naar het privé-mailadres.
3. Laat de gebruiker inloggen met de TAP, de oude methoden verwijderen en een nieuwe passkey registreren
   (Authenticator op de telefoon, of Windows Hello op het beheerde device).
4. Controleer dat de nieuwe methode werkt en dat er geen legacy-methode is achtergebleven.
5. Leg de uitgifte vast: wie, wanneer, waarom, hoe geverifieerd.

## Keuzes om vooraf te maken

- Geldigheidsduur van de TAP (hier: 2 uur, onbeperkt herbruikbaar binnen die tijd).
- Wie mag uitgeven: alleen SSC en IT, geen zelfbediening.
- Hoe je verifieert bij iemand die zijn telefoon kwijt is én thuiswerkt; spreek dat vooraf af, niet op het
  moment zelf.
- Monitoring: een melding bij elke TAP-uitgifte, en een periodieke blik op wie er vaak een nodig heeft.
