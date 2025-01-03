# Aufgabe: Wörterbuch erstellen und Abfragen

## Hauptaufgabe:

#1.Erstelle ein Python-Programm, in dem die Teilnehmer ein Dictionary erstellen. Das Dictionary soll mindestens 10 deutsche Wörter mit ihren englischen Übersetzungen enthalten.
#2.Danach soll das Programm den Benutzer per Eingabe (input) fragen, welches deutsche Wort ins Englische übersetzt werden soll.Falls das Wort nicht im Dictionary ist, soll eine entsprechende Fehlermeldung angezeigt werden.

## Zusatzaufgabe:

#1. Einheitliche Eingaben: Stelle sicher, dass die Eingaben unabhängig von der Groß- und Kleinschreibung erkannt werden (arbeite mit .lower()).
#2. Erweiterung des Wörterbuchs: Implementiere eine Funktion, mit der Benutzer das Wörterbuch erweitern können:Verwende eine while True-Schleife mit einer Abbruchbedingung (z. B. Eingabe von „exit“), um neue Übersetzungen hinzuzufügen.


woerterbuch = {
"haus": "house",
"baum": "tree",
"auto": "car",
"buch": "book",
"tisch": "table",
"stuhl": "chair",
"hund": "dog",
"katze": "cat",
"apfel": "apple",
"wasser": "water"
}

deutsches_wort = input("Bitte geben Sie ein deutsches Wort ein: ").lower() 

if deutsches_wort in woerterbuch:
    print(f"Die englische Übersetzung von '{deutsches_wort}' ist '{woerterbuch[deutsches_wort]}'.")
else:
    print(f"Fehler: Das Wort '{deutsches_wort}' ist nicht im Wörterbuch enthalten.")


# Zusatzaufbabe Das Wort gibt es nicht und wird ins Dic aufgenommen

my_dict = {"apfel": "Apple", "wörterbuch": "dictionary"}
my_userinput = input("Gib ein deutsches Wort ein: ")
if my_userinput in my_dict:
    print(f"Die Übersetzung zu {my_userinput} ist {my_dict[my_userinput]}")
else:
    actual_translation = input(
        "Das Wort gibt es noch nicht, gib die engl. Übersetzung ein: "
    )
    my_dict[my_userinput] = actual_translation
    print(f"Die Übersetzung zu {my_userinput} ist {my_dict[my_userinput]}")