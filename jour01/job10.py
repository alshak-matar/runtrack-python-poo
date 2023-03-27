class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche=False):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.en_marche = en_marche
        self.reservoir = 50

    def get_marque(self):
        return self.marque

    def set_marque(self, marque):
        self.marque = marque

    def get_modele(self):
        return self.modele

    def set_modele(self, modele):
        self.modele = modele

    def get_annee(self):
        return self.annee

    def set_annee(self, annee):
        self.annee = annee

    def get_kilometrage(self):
        return self.kilometrage

    def set_kilometrage(self, kilometrage):
        self.kilometrage = kilometrage

    def get_en_marche(self):
        return self.en_marche

    def demarrer(self):
        if self.verifier_plein() and not self.en_marche:
            self.en_marche = True
            print("La voiture démarre.")
        else:
            print("La voiture ne peut pas démarrer.")

    def arreter(self):
        self.en_marche = False
        print("La voiture s'arrête.")

    def verifier_plein(self):
        if self.reservoir > 5:
            return True
        else:
            return False
ma_voiture = Voiture("Renault", "Clio", 2015, 80000)
ma_voiture.demarrer()
ma_voiture.arreter()

