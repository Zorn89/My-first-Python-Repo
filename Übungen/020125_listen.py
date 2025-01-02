#Die Summe aller Zahlen berechnen

zahlen = [1, 2, 12, 4, 8]  # Beispiel-Liste von Zahlen
summe = sum(zahlen)       # Berechnung der Summe
print("Die Summe der Zahlen ist:", summe)

# Nur die ungeraden Zahlen ausgeben
for zahl in range(1, 8):  
    if zahl % 2 != 0:  # ob die Zahl ungerade ist
        print(zahl)


# Größte Zahl in der Liste

groesste_zahl = max(zahlen)
print("Die größte Zahl in der Liste ist:", groesste_zahl)


# Größte Zahl Schleife


groesste_zahl = zahlen[0]


for zahl in zahlen:
    if zahl > groesste_zahl:
        groesste_zahl = zahl


print("Die größte Zahl in der Liste ist:", groesste_zahl)
