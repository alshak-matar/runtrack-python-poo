class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix
        
    def informationsVehicule(self):
        print("Marque : ", self.marque)
        print("Année : ", self.annee)
        print("Prix : ", self.prix)

    def demarrer(self):
        print("Je roule.")

class Voiture(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.portes = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes : ", self.portes)
        
    def demarrer(self):
        print("La voiture démarre.")

class Moto(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.roue = 2
        
    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues : ", self.roue)
        
    def demarrer(self):
        print("La moto démarre.")

voiture = Voiture("Audi TT", 2020, 80000)
voiture.informationsVehicule()
voiture.demarrer()

moto = Moto("BMW", 2020, 25000)
moto.informationsVehicule()
moto.demarrer()
