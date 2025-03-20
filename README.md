# Urlaubskosten-Teiler
Dies ist die erste Hausübung für die Lehrveranstaltung Open Source Modeling.

## Programmbeschreibung
Die Aufgabenstellung ein kleines Programms auf GitHub hochzuladen wird mit einem Urlaubskosten-Teiler erledigt. In diesem Programm können mehrere Kosten angegeben werden, von wem diese übernommen wurden und wer an ihnen beteiligt war. Das Programm rechnet sich die Bilanz aus und erleichtert es somit die Kosten gerecht aufzuteilen.

## Funktionsbeschreibung
Die Funktion **teilnehmer_eingeben()** fragt die Namen der Teilnehmer ab und gibt sie als Liste zurück. Der Nutzer gibt die Namen als kommagetrennte Zeichenkette ein (z. B. "Alice, Bob, Charlie"). Die Funktion trennt die Eingabe in einzelne Namen, entfernt überflüssige Leerzeichen und gibt eine bereinigte Liste zurück, z. B. ["Alice", "Bob", "Charlie"].

Die Funktion **ausgabe_erfassen()** ermöglicht das Erfassen einer neuen Ausgabe. Der Nutzer gibt an, wer bezahlt hat, den Betrag sowie die beteiligten Personen. Die Funktion überprüft, ob die Eingaben gültig sind (z. B. ob der Zahlende existiert und der Betrag eine Zahl ist). Falls alles korrekt ist, wird die Ausgabe in die Liste ausgaben gespeichert.

Die Funktion **berechnung()** ermittelt, wie viel jeder Teilnehmer noch zahlen oder zurückbekommen muss. Dafür wird für jede Ausgabe berechnet, wie der Betrag auf die beteiligten Personen aufgeteilt wird. Die Funktion führt alle Transaktionen zusammen und gibt ein Saldo-Dictionary zurück, das für jede Person den aktuellen Kontostand enthält: Positive Werte bedeuten Guthaben, negative Werte Schulden.
