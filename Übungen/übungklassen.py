# Klassendiagramm in eine Funktion umwandeln

class Auto(): 

    def __init__(self, Name, Motor, Restreichweite, KMzahl):
        self.Name = Name
        self.Motor = Motor
        self.Restreichweite = Restreichweite
        self.KMzahl = KMzahl

    def fahren(self,km):
        if self Restreichweite >= km:
         self.kilometerzahl += km
        self.restreichweite -= km
        print(f"Auto fährt {km} km")
        else: 
            print("Reichweite nicht ausreichend")

    def tanken(self,km):
        self.restreichweite += km

    my_car = Auto("Audi","Verbrenner",200,0) 