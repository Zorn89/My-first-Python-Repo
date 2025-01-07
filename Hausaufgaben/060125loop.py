# Aufgabe 1

# Schreibe ein Programm, das die Häufigkeit eines Buchstabens in einem Text zählt. 
# 1. Der Benutzer gibt einen Text und einen Buchstaben ein. 
# 2. Dein Programm zählt mit einer Schleife, wie oft dieser Buchstabe im Text vorkommt.

# Benutzer gibt den Text und den Buchstaben ein
text = input("Bitte geben Sie einen Text ein: ")
buchstabe = input("Bitte geben Sie einen Buchstaben ein: ")

# Überprüfen, ob der Benutzer nur einen Buchstaben eingegeben hat
if len(buchstabe) != 1:
    print("Bitte geben Sie nur einen einzelnen Buchstaben ein.")
else: haeufigkeit = 0 # Zähler für die Häufigkeit des Buchstabens

# Schleife, um den Text zu durchlaufen
for zeichen in text:
    if zeichen == buchstabe:haeufigkeit += 1

# Ausgabe der Häufigkeit
print(f"Der Buchstabe '{buchstabe}' kommt {haeufigkeit} mal im Textvor.")


# Aufgabe 2 

# Schreibe ein Programm, das: 
# 1. Den Benutzer auffordert, 5 Zahlen einzugeben. 
# 2. Mit einer Schleife die Summe und den Durchschnitt der Zahlen berechnet. 
# 3. Die Ergebnisse ausgibt.

# Benutzer auffordern, 5 Zahlen einzugeben
zahlen = [] #Liste
for i in range(5):
    zahl = float(input(f"Gib die {i+1}. Zahl ein: "))
    zahlen.append(zahl)

# Summe und Durchschnitt berechnen
summe = sum(zahlen)
durchschnitt = summe / len(zahlen)

# Ergebnisse ausgeben
print(f"Die Summe ist: {summe}")
print(f"Der Durchschnitt ist: {durchschnitt}") 

#Aufgabe 3
#Muster erstellen
def print_stars(x): 
        for i in range(x):  # [0,1,2,3,4,5,6,7,8,9]
            print("o" * i)

print_stars(10)