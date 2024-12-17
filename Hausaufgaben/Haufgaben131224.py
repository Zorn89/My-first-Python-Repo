# Aufgabe 1

date= input("Geben Sie ein Datum ein und erfahren Sie ob Ferien sind oder nicht (YYYY.MM.DD):")

if date >= "2024.12.24" and date <= "2025.01.01":
    print("Es sind Winterferien")
elif date >= "2025.04.18" and date <= "2025.04.21":
    print("Es sind Osterferien")
elif date >= "2025.08.11" and date <= "2025.08.08":
    print("Es sind Sommerferien")
elif date >= "2025.12.24" and date <= "2026.01.01":
    print("Es sind Winterferien")
else :
    print("Du musst Malochen")


