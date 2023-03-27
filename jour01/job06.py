class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def get_longueur(self):
        return self.longueur
    
    def set_longueur(self, longueur):
        self.longueur = longueur
    
    def get_largeur(self):
        return self.largeur
    
    def set_largeur(self, largeur):
        self.largeur = largeur

mon_rectangle = Rectangle(10, 5)

print("Longueur :", mon_rectangle.get_longueur())
print("Largeur :", mon_rectangle.get_largeur())

mon_rectangle.set_longueur(100)
mon_rectangle.set_largeur(50)

print("Longueur modifiée :", mon_rectangle.get_longueur())
print("Largeur modifiée :", mon_rectangle.get_largeur())
