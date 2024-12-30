# Aufgbabe 1 
## Taxometer

start_price = 4.50 
km = int(input("Bitte KM eingeben:"))
if km > 2:
    costs = 2.5
else: 
    costs = 2.7
total_expenses = start_price + costs * km
print("Die Kosten:", total_expenses)



# Aufgabe 2 
#schreibe ein Programm mit Rezepten:

# Zutatenlisten für verschiedene Rezepte
spiegelei = ["Ei", "Salz", "Maggi"]
pasta = ["Pasta", "Wasser", "Salz", "Olivenöl", "Tomatensauce"]
kaffee = ["Kaffeepulver", "Zucker", "Jack Daniels"]

# Funktion, die beim Ausführen der Datei gestartet wird

def rezept_ausgeben():
    print("Willkommen! Welches Rezept möchtest du sehen?")
    print("1. Spiegelei")
    print("2. Pasta")
    print("3. Kaffee")
    
    auswahl = input("Bitte gib die Nummer des Rezepts ein (1-3): ")
    
    if auswahl == "1":
        print("Zutaten für Spiegelei:", spiegelei)
    elif auswahl == "2":
        print("Zutaten für Pasta:", pasta)
    elif auswahl == "3":
        print("Zutaten für Kaffee:", kaffee)
    else:
        print("Ungültige Auswahl. Bitte wähle eine Nummer zwischen 1 und 3.")

# Die Funktion aufrufen, wenn das Skript ausgeführt wird
if __name__ == "__main__":
    rezept_ausgeben() 







# Turtle Paket

import turtle

# Funktion zum Zeichnen des Buchstabens M

def draw_J():
turtle.left(90)
turtle.forward(100)
turtle.right(150)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.right(150)
turtle.forward(100)
turtle.right(90)

# Funktion zum Zeichnen des Buchstabens A
def draw_A():
turtle.left(75)
turtle.forward(100)
turtle.right(150)
turtle.forward(100)
turtle.right(180)
turtle.forward(50)
turtle.right(105)
turtle.forward(30)
turtle.right(150)
turtle.forward(30)
turtle.right(105)
turtle.forward(50)
turtle.right(180)

# Funktion zum Zeichnen des Buchstabens X
def draw_N():
turtle.left(75)
turtle.forward(100)
turtle.right(150)
turtle.forward(100)
turtle.left(150)
turtle.forward(100)
turtle.right(150)
turtle.forward(100)
turtle.right(90)

# Hauptprogramm
turtle.speed(1) # Geschwindigkeit der Zeichnung

# Zeichne den Namen "Jan"
draw_J()
turtle.penup()
turtle.forward(20) # Abstand zwischen den Buchstaben
turtle.pendown()
draw_A()
turtle.penup()
turtle.forward(20) # Abstand zwischen den Buchstaben
turtle.pendown()
draw_N()

turtle.hideturtle() # Versteckt die Schildkröte
turtle.done() # Beendet die Zeichnung








#OS Paket

import os

def main():
# Frage den Benutzer nach dem Dateinamen
dateiname = input("Bitte geben Sie den Namen der .txt-Datei ein (mit .txt): ")

# Überprüfen, ob die Datei existiert
if not os.path.isfile(dateiname):
print("Die Datei existiert nicht. Bitte überprüfen Sie den Dateinamen.")
return

# Datei öffnen und Inhalt lesen
with open(dateiname, 'r', encoding='utf-8') as datei:
inhalt = datei.read()
print("\nInhalt der Datei:")
print(inhalt)

# Anzahl der Wörter berechnen
woerter = inhalt.split()
anzahl_woerter = len(woerter)
print(f"\nAnzahl der Wörter in der Datei: {anzahl_woerter}")

if __name__ == "__main__":

main()














#Wochentag ausgeben

def weekday_after(weekday, days):
    # Liste der Wochentage
    weekdays = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    
    # Finde den Index des übergebenen Wochentags
    index = weekdays.index(weekday)
    
    # Berechne den neuen Index unter Verwendung des Modulo-Operators
    new_index = (index + days) % len(weekdays)
    
    # Gebe den neuen Wochentag zurück
    return weekdays[new_index]

print(weekday_after("Dienstag", 10))  # Ausgabe: Freitag

