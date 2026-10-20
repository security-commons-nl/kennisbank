# Windows + R uitschakelen

- Start regedit.exe op.

- Ga naar registry key: HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced

- Maak een Tekenreekswaarde aan met de exacte naam “DisabledHotkeys” en de waarde “R” (hoofdletter!)

Dit is het resultaat:

Deze registry wijziging is pas actief nadat het systeem een herstart heeft gekregen.

Impact

Zodra de gebruiker de toets combinatie “Windows + R” gebruikt zal dit niet meer functioneren. Alleen een foutmelding in de vorm van een kort geluidje zal hoorbaar zijn.
