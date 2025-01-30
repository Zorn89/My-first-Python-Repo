# Generieren Sie eine Zufallszahl zwischen 1 und 9 
# (einschließlich 1 und 9). Bitten Sie den Benutzer, 
# die Zahl zu erraten, dann sagen Sie ihm, ob er zu 
# niedrig, zu hoch oder genau richtig ahnte. 
# (Hin: denken Sie daran, den Benutzer Eingabeunterricht 
# von der ersten Übung zu verwenden).

# Extras:
# Halten Sie das Spiel am Gang, bis die Benutzertypen "Exit"
# Behalten Sie den Überblick darüber, wie viele Vermutungen der Benutzer genommen hat, 
# und wenn das Spiel endet, drucken Sie dies aus.


import random

def main():
    # Zufallszahl zwischen 1 und 9 generieren
    zahl = random.randint(1, 9)
    
    versuche = 0  # Zähler für die Anzahl der Versuche
    
    while True:
        # Benutzereingabe
        benutzer_eingabe = input("Errate eine Zahl zwischen 1 und 9 (oder 'Exit' zum Beenden): ")

        if benutzer_eingabe.lower() == "exit":
            print(f"Das Spiel ist beendet. Du hast {versuche} Versuche gemacht.")
            break
        
        # Versuche zu zählen
        versuche += 1
        
        # Eingabe in eine Zahl umwandeln und prüfen
        try:
            benutzer_zahl = int(benutzer_eingabe)
        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")
            continue

        # Überprüfen, ob die Eingabe zu hoch, zu niedrig oder korrekt ist
        if benutzer_zahl < zahl:
            print("Zu niedrig! Versuch es noch einmal.")
        elif benutzer_zahl > zahl:
            print("Zu hoch! Versuch es noch einmal.")
        else:
            print(f"Genau richtig! Die Zahl war {zahl}. Du hast {versuche} Versuche gebraucht.")
            break

if __name__ == "__main__":
    main()