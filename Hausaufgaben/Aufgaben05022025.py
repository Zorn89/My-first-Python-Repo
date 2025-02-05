# Ein Programm, das den Benutzer um eine Zahl bittet und dann eine Liste aller Teiler dieser Zahl ausgibt. 

# Funktion, um alle Teiler einer Zahl zu finden
def finde_teiler(zahl):
    teiler = []
    for i in range(1, zahl + 1):
        if zahl % i == 0:
            teiler.append(i)
    return teiler

# Benutzer nach einer Zahl fragen
zahl = int(input("Geben Sie eine Zahl ein: "))

# Teiler der Zahl finden
teiler = finde_teiler(zahl)

# Teiler ausgeben
print(f"Die Teiler von {zahl} sind: {teiler}")