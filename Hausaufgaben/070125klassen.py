#Implementiere folgendes UML Klassendiagramm:
# Die __init__ Methode ist hierbei der Konstruktor, der die entsprechenden Eigenschaften eines Zutat Objekts setzt

class Zutat:
    def __init__(self, name: str, kalorien_pro_100g: int, zubereitungszeit: int):
        self.name = name
        self.kalorien_pro_100g = kalorien_pro_100g
        self.zubereitungszeit = zubereitungszeit 


class ZutatenListe:
    def __init__(self):
        self.zutaten = {}  # Dictionary, um Zutaten als Schlüssel und Menge als Wert zu speichern
    
    def zutat_hinzufuegen(self, zutat: Zutat, menge: str):
#Fügt eine Zutat zur Zutatenliste hinzu.
        self.zutaten[zutat] = menge
    
    def kalorien(self):
    # Berechnet und gibt die Kalorien aller Zutaten in der Zutatenliste aus.
        gesamt_kalorien = 0
        for zutat, menge in self.zutaten.items():
            gesamt_kalorien += zutat.kalorien_pro_100g  # Es könnte auch eine Berechnung der Menge hier erfolgen
        print(f"Gesamt Kalorien: {gesamt_kalorien}")
    
    def kochzeit(self):
    #Gibt die Kochzeit der Zutat mit der höchsten Zubereitungszeit aus.
        if not self.zutaten:
            print("Keine Zutaten in der Liste.")
            return
        max_zubereitungszeit = max(self.zutaten, key=lambda zutat: zutat.zubereitungszeit)
        print(f"Die längste Kochzeit beträgt: {max_zubereitungszeit.zubereitungszeit} Minuten (für {max_zubereitungszeit.name})") 

    def rezept_anzeigen(self):
    #Zeigt das Rezept mit allen Zutaten und deren Mengen an.
        print(f"Rezept: {self.name}")
        print("Zutaten:")
        for zutat, menge in self.zutatenliste.items():
            print(f"- {zutat.name}: {menge}")
        print(f"\nBeschreibung: {self.beschreibung}") 

# Beispiel 
tomate = Zutat("Tomate", 18, 5)
kartoffel = Zutat("Kartoffel", 77, 25)
salz = Zutat("Salz", 0, 0)

rezept = Rezept=("Kartoffelsalat", "Ein erfrischender Kartoffelsalat, ideal für warme Tage.")
rezept.zutat_hinzufuegen(tomate, "200g")
rezept.zutat_hinzufuegen(kartoffel, "500g")
rezept.zutat_hinzufuegen(salz, "1 Prise")

# Anzeige der Kalorien
rezept.kalorien()

# Anzeige der Kochzeit
rezept.kochzeit()

# Anzeige des Rezepts
rezept.rezept_anzeigen()