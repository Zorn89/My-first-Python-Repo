class BauplanKatzenKlasse():
    """ Klasse für das Erstellen von Katzen """

    def __init__(self, rufname, farbe, alter):
        self.rufname = rufname
        self.farbe   = farbe
        self.alter   = alter

    def tut_miauen(self):
        print("miau")

katze_sammy = BauplanKatzenKlasse("Sammy", "orange", 3)
katze_sammy.tut_miauen()