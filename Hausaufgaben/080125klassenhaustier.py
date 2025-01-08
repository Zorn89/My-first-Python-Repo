class Haustier:
    def __init__(self, name, species, age, favorite_food):
        self.name = name  # Name des Haustiers
        self.species = species  # Tierart
        self.age = age  # Alter
        self.favorite_food = favorite_food  # Lieblingsessen
        self.energy_level = 100  # Energielevel, Standardwert ist 100

    # Methode zur Beschreibung des Haustiers
    def get_description(self):
        return f"{self.name} ist ein {self.age} Jahre alter {self.species}."

    # Methode für das Spielen
    def play(self, duration):
        energy_loss = duration * 5  # Energieverlust pro Minute
        self.energy_level = max(self.energy_level - energy_loss, 0)  # Energie kann nicht unter 0 fallen
        print(f"{self.name} hat {duration} Minuten gespielt und hat nun {self.energy_level} Energie.")

    # Methode für das Füttern
    def feed(self, food):
        if food == self.favorite_food:
            self.energy_level = min(self.energy_level + 30, 100)  # Maximale Energie ist 100
            print(f"{self.name} hat seinen Lieblingsfisch gegessen und hat nun {self.energy_level} Energie.")
        else:
            self.energy_level = min(self.energy_level + 10, 100)  # Maximale Energie ist 100
            print(f"{self.name} hat {food} gegessen und hat nun {self.energy_level} Energie.")

# Erstelle das Haustier-Objekt
mimi = Haustier("Mimi", "Katze", 3, "Fisch")

# Teste die Methoden
print(mimi.get_description())
mimi.play(15)  # 15 Minuten spielen
mimi.feed("Fisch")  # Lieblingsessen 
mimi.feed("Katzennahrung")  # Anderes Essen füttern