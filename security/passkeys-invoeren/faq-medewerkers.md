---
titel: Veelgestelde vragen over passkeys voor medewerkers (sjabloon)
vakgebied: security
type: sjabloon
normen: [BIO2]
versie: 2026-08
herkomst: bijlage bij "Passkeys invoeren"; intranet-FAQ van een gemeentelijke uitrol, placeholders op de plek van datum, locatie en organisatienaam
status: sjabloon
samenvatting: Vijfentwintig vragen die medewerkers stelden tijdens de overstap naar passkeys, met de antwoorden zoals ze op het intranet stonden. Van "wat is het" tot "wat gebeurt er als ik niks doe", plus het verschil tussen Windows Hello en een passkey.
---

# Veelgestelde vragen: wachtwoordsleutel (passkey)

Bijlage bij [Passkeys invoeren](README.md), stap 7. Dit zijn de vragen die medewerkers echt stelden, met de
antwoorden in de toon van het intranet. Placeholders staan tussen `[ ]`. "Wachtwoordsleutel" is de
Nederlandse term die Microsoft zelf gebruikt; medewerkers zoeken op beide woorden.

---

Het kan zijn dat je nog vragen hebt voordat je hiermee aan de slag gaat. Toch nog vragen? Meld je bij de
servicebalie op `[locatie]`.

**1. Wat is een passkey eigenlijk?**
Een passkey is een digitale wachtwoordsleutel waarmee je inlogt zonder wachtwoord. De sleutel staat alleen
op jouw apparaat.

**2. Waarom gaan we over op passkeys?**
We stappen organisatiebreed over op volledig wachtwoordloos inloggen. Vanaf `[datum]` logt iedere
medewerker in met gezichtsherkenning, vingerafdruk of pincode (afhankelijk van wat je apparaat ondersteunt
en wat je zelf instelt). Zonder wachtwoorden en zonder sms-codes.

**3. Wat zijn de voordelen?**
Nooit meer je wachtwoord voor `[organisatie]` onthouden. Inloggen gaat net zo snel als je telefoon
ontgrendelen. Veel minder verzoeken om gedeblokkeerd te worden, en dus minder frustratie.

**4. Waarom is dit veiliger?**
Wachtwoorden zijn de belangrijkste oorzaak van incidenten: gestolen via phishing en neplinks, geraden of
hergebruikt, onderschept via malware. Passkeys zijn niet te stelen of te onderscheppen, werken alleen op
jouw apparaat en zijn phishing-proof.

**5. Zijn er ook nadelen?**
Minder tijd om koffie of thee te halen.

**6. Wie stelt de passkey in?**
Dat doe je zelf.

**7. Wanneer kan ik passkeys gebruiken?**
Nu al.

**8. Krijg ik een seintje als ik het kan instellen?**
Nee, je kunt het instellen op een moment dat het jou uitkomt. Wacht niet te lang: je hebt tijd tot
`[datum]`. Daarna is de passkey verplicht en kun je niet meer op de oude manier inloggen.

**9. Wat gebeurt er als ik niks doe?**
Dan heb je vanaf `[datum]` geen toegang meer tot je programma's en gegevens.

**10. Stel ik de passkey eenmalig in?**
Ja.

**11. Verloopt een passkey na een tijd?**
Nee.

**12. Hoeveel tijd kost het instellen?**
*Windows-laptop van de organisatie:* gezichtsherkenning 5 minuten, vingerafdruk 10 minuten, pincode heb je
eerder al ingesteld.
*Smartphone van de organisatie of eigen smartphone:* Microsoft Authenticator instellen, 5 minuten.
*Apple MacBook of privé-laptop:* daarop log je in met de Microsoft Authenticator op je smartphone.

**13. Waar vind ik uitleg?**
Op `[intranetpagina]`.

**14. Kan ik een passkey gebruiken vanaf mijn privécomputer?**
Ja, zie vraag 12.

**15. Stel ik de passkey in op mijn laptop, op mijn smartphone, of op beide?**
Beide, zie vraag 12.

**16. Ik ben extern ingehuurd en gebruik een smartphone van mijn werkgever. Kan ik daarop een passkey
instellen?**
Ja, zie vraag 12.

**17. Ik ben extern ingehuurd en gebruik een laptop van mijn werkgever. Kan ik daarop een passkey
instellen?**
Nee. Om in te loggen op die laptop gebruik je de Microsoft Authenticator op je smartphone.

**18. Werkt het op Android en Apple?**
Ja, allebei.

**19. Is er een volgorde: eerst laptop, dan smartphone?**
De volgorde maakt niet uit. Let wel op: de passkey op je smartphone stel je in vanaf je smartphone, niet
vanaf je laptop.

**20. Ik durf het niet; wat als het mislukt?**
Loop langs bij het shared service center op `[locatie]`. Ze helpen je graag om het samen in te stellen.

**21. Bij wie kan ik langsgaan voor hulp?**
Het shared service center op `[locatie]`.

**22. Maakt het uit wanneer ik het instel?**
Nee, zie vraag 8.

**23. Werken alle applicaties met een passkey?**
De meeste wel. Heb je een applicatie waar je nog met gebruikersnaam en wachtwoord inlogt, meld dat bij
`[servicedesk]` onder "applicatiehulp: passkey".

**24. Ik heb een vraag over passkeys, bij wie moet ik zijn?**
Het shared service center op `[locatie]`.

**25. Waarom moet ik een passkey instellen? Ik heb toch al een pincode, vingerafdruk of
gezichtsherkenning?**
Windows Hello en een passkey lijken op elkaar, maar hebben verschillende doelen.

*Windows Hello* gebruik je om lokaal op je Windows-apparaat in te loggen. Het vervangt je wachtwoord voor
toegang tot het device zelf, via biometrie of pincode, gekoppeld aan dat ene apparaat.

*Een passkey* is een wachtwoordloze inlogmethode voor online accounts en diensten (websites, apps),
gebaseerd op FIDO2/WebAuthn: een publieke sleutel bij de dienst, een privésleutel op jouw apparaat. Je
telefoon werkt als veilige authenticator, vaak met biometrie. Phishing-bestendig en niet afhankelijk van
één device.

*Waarom beide?* Windows Hello beveiligt je device. Passkeys beveiligen je accounts. Met alleen Windows
Hello ben je veilig op je laptop, maar niet automatisch op je online accounts. Met een passkey log je ook
vanaf je telefoon veilig in op de apps van de organisatie, zonder wachtwoord.
