# Pseudocode und Programm

def ungerade_zahlen_berechnen(start, ende):
    ungerade_zahlen = []
    
    for zahl in range(start, ende + 1):
        if zahl % 2 != 0:  # Überprüfen, ob die Zahl ungerade ist
            ungerade_zahlen.append(zahl)
    
    anzahl = len(ungerade_zahlen)  # Anzahl der ungeraden Zahlen
    summe = sum(ungerade_zahlen)   # Summe der ungeraden Zahlen
    
    return anzahl, summe

# Eingabe der zwei Zahlen
start_zahl = int(input("Geben Sie die Startzahl ein: "))
ende_zahl = int(input("Geben Sie die Endzahl ein: "))

anzahl, summe = ungerade_zahlen_berechnen(start_zahl, ende_zahl)

print(f"Anzahl der ungeraden Zahlen zwischen {start_zahl} und {ende_zahl}: {anzahl}")
print(f"Summe der ungeraden Zahlen zwischen {start_zahl} und {ende_zahl}: {summe}")
