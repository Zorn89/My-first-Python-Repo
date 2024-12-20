# Hausaufgaben

## Aufgabe 1: Einfache Entscheidungen mit `if`-Statements (25 Punkte)

**Ziel:** Verstehen, wie Entscheidungen im Code in Arbeitsschritte übersetzt werden können.

Code-Beispiel:

```python
zahl = int(input("Gib eine Zahl ein: "))
if zahl > 10:
    print("Die Zahl ist größer als 10.")
else:
    print("Die Zahl ist 10 oder kleiner.")
```

- Schreibe die Arbeitsschritte auf.

---

## Antwort:

***1. Benutzereingabe:*** 
Der Code beginnt mit der Aufforderung an den Benutzer, eine Zahl einzugeben. Dies geschieht durch die Funktion
input(), die eine Eingabe vom Benutzer erwartet. 

Die Eingabe wird in einen Integer (ganzzahligen Wert) umgewandelt, indem int() verwendet wird. 

***2. Zuweisung:*** 
Die eingegebene Zahl wird der Variablen zahl zugewiesen.

***3. Bedingte Überprüfung:*** 
Der Code überprüft dann, ob die eingegebene Zahl größer als 10 ist. Dies geschieht mit einer
if -Anweisung:
    - Wenn die Bedingung zahl > 10 wahr ist, wird der       folgende Schritt ausgeführt.
    - Andernfalls wird der Code im else -Block ausgeführt.

***4. Ausgabe für größere Zahlen:*** 
Wenn die Zahl größer als 10 ist, wird die Nachricht "Die Zahl ist größer als 10."auf dem Bildschirm ausgegeben.

***5. Ausgabe für kleinere oder gleich große Zahlen:*** 
Wenn die Zahl 10 oder kleiner ist, wird die Nachricht "Die Zahl ist 10 oder kleiner." ausgegeben.



## Aufgabe 2: Listen verstehen und mit Python erstellen (20 Punkte)

**Ziel:** Verstehen, wie Datenstrukturen wie Listen verwendet werden können.

Code-Beispiel:

```python
zahlen = [1, 2, 3, 4, 5]
print("Die erste Zahl ist:", zahlen[0])
print("Die letzte Zahl ist:", zahlen[-1])
```

- Schreibe die Arbeitsschritte auf.

**Zusatzaufgabe:** Erstelle selbst eine Liste mit Wochentagen und schreibe die Arbeitsschritte auf.

---

## Antwort

***1. Liste erstellen:*** 
Zuerst wird eine Liste mit dem Namen "Zahlen" erstellt, die die Werte 1, 2, 3, 4 und 5 enthält.

python-zahlen = [1, 2, 3, 4, 5]
   


***2. Erste Zahl ausgeben:*** 
Der Code verwendet print, um die erste Zahl der Liste auszugeben. In Python kann auf das erste Element einer Liste mit dem Index 0 zugegriffen werden. Daher wird zahlen[0] verwendet, um die erste Zahl (1) zu erhalten.

in python
   print("Die erste Zahl ist:", zahlen[0])
   

***3. Letzte Zahl ausgeben:*** 
Um die letzte Zahl der Liste auszugeben, wird der negative Index -1 verwendet. In Python bedeutet zahlen[-1], dass auf das letzte Element der Liste zugegriffen wird. In diesem Fall ist das die Zahl 5.

in python
   print("Die letzte Zahl ist:", zahlen[-1])
   


***4. Ausgabe:*** 
Der Code gibt zwei Zeilen aus:
- Die erste Zeile zeigt die erste Zahl: "Die erste Zahl ist: 1"
- Die zweite Zeile zeigt die letzte Zahl: "Die letzte Zahl ist: 5"


## Aufgabe 3: Entscheidungslogik erweitern (25 Punkte)

**Ziel:** Die Funktionsweise von mehreren Bedingungen in Python verstehen und in Arbeitsschritte übertragen.

Code-Beispiel:

```python
zahl = int(input("Gib eine Zahl ein: "))
if zahl > 0:
    print("Die Zahl ist positiv.")
elif zahl < 0:
    print("Die Zahl ist negativ.")
else:
    print("Die Zahl ist null.")
```

- Schreibe die Arbeitsschritte auf.

---

## Antwort 

***1. Eingabeaufforderung:***
Der Benutzer wird aufgefordert, eine Zahl einzugeben. Dies geschieht durch die
input()-Funktion, die eine Eingabe vom Benutzer erwartet.

***2. Umwandlung in eine Ganzzahl:***
Die eingegebene Zahl wird mit
int() in einen ganzzahligen Datentyp umgewandelt, um sicherzustellen, dass die Eingabe als Zahl verarbeitet werden kann.

***3. Bedingte Überprüfung:***
- Erste Bedingung (if zahl > 0): Es wird überprüft, ob die eingegebene Zahl größer als 0 ist. Wenn dies der Fall ist, wird die Nachricht "Die Zahl ist positiv." ausgegeben.
- Zweite Bedingung (elif zahl < 0): Wenn die erste Bedingung nicht erfüllt ist, wird überprüft, ob die Zahl kleiner als 0 ist. Wenn dies zutrifft, wird die Nachricht "Die Zahl ist negativ." ausgegeben.
- Sonst-Fall (else): Wenn keine der vorherigen Bedingungen erfüllt ist (d.h. die Zahl ist 0), wird die Nachricht "Die Zahl ist null." ausgegeben.

***4. Ausgabe:***
Je nach Ergebnis der Bedingungen wird die entsprechende Nachricht an den Benutzer ausgegeben.


## Aufgabe 4: Funktionen verstehen (20 Punkte)

**Ziel:** Lernen, wie Funktionen in Python definiert werden und was in jedem Arbeitsschritt passiert.

Code-Beispiel:

```python
def ist_gerade(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False

zahl = int(input("Gib eine Zahl ein: "))
if ist_gerade(zahl):
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")
```

- Schreibe die Arbeitsschritte auf.

---

# Antwort

***1. Definition der Funktion:***
- Die Funktion ist_gerade(zahl) wird definiert. Sie nimmt einen Parameter zahl entgegen.

***2. Überprüfung auf gerade Zahl:***
- Innerhalb der Funktion wird überprüft, ob die Zahl gerade ist, indem der Modulo-Operator % verwendet wird.
- Wenn zahl % 2 == 0 (d.h. der Rest der Division von zahl durch 2 ist 0), wird True zurückgegeben, was bedeutet, dass die Zahl gerade ist.
- Andernfalls wird False zurückgegeben, was bedeutet, dass die Zahl ungerade ist.

***3. Eingabe der Zahl:***
- Der Benutzer wird aufgefordert, eine Zahl einzugeben. Diese Eingabe wird mit int(input(...)) in einen ganzzahligen Wert umgewandelt und der Variablen zahl zugewiesen.

***4. Aufruf der Funktion:***
- Die Funktion ist_gerade(zahl) wird mit der eingegebenen Zahl aufgerufen.

***5. Ausgabe des Ergebnisses:***
- Wenn die Funktion True zurückgibt (die Zahl ist gerade), wird die Nachricht "Die Zahl ist gerade." ausgegeben.
- Wenn die Funktion False zurückgibt (die Zahl ist ungerade), wird die Nachricht "Die Zahl ist ungerade." ausgegeben.

## Aufgabe 5: Benutzerinteraktion (10 Punkte)

**Ziel:** Die Struktur eines Programms mit Benutzereingaben und Ausgaben analysieren.

Code-Beispiel:

```python
name = input("Wie heißt du? ")
alter = int(input("Wie alt bist du? "))
print(f"Hallo {name}, in 10 Jahren wirst du {alter + 10} Jahre alt sein!")
```

- Schreibe die Arbeitsschritte auf.


## Antwort

***1. Benutzereingabe für den Namen:***
- Der Code verwendet die input() -Funktion, um den Benutzer nach seinem Namen zu fragen.
- Der eingegebene Name wird in der Variablen name gespeichert.

***2. Benutzereingabe für das Alter:***
- Der Code fragt den Benutzer nach seinem Alter und verwendet ebenfalls die input() -Funktion.
- Da das Alter als Ganzzahl benötigt wird, wird die Eingabe mit int() in einen Integer umgewandelt und in der Variablen
alter gespeichert.

***3. Berechnung des Alters in 10 Jahren:***
- Der Code addiert 10 zum aktuellen Alter (alter + 10), um das Alter in 10 Jahren zu berechnen.

***4. Ausgabe der Nachricht:***
- Schließlich wird eine formatierte Zeichenkette (f-String) verwendet, um eine personalisierte Nachricht zu erstellen, die den Namen des Benutzers und sein zukünftiges Alter enthält.
- Diese Nachricht wird mit der print()-Funktion ausgegeben.