class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        
    def perimetre(self):
        return 2 * (self.longueur + self.largeur)
        
    def surface(self):
        return self.longueur * self.largeur
        
    def get_longueur(self):
        return self.longueur
    
    def set_longueur(self, nouvelle_longueur):
        self.longueur = nouvelle_longueur
        
    def get_largeur(self):
        return self.largeur
    
    def set_largeur(self, nouvelle_largeur):
        self.largeur = nouvelle_largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur
        
    def volume(self):
        return self.surface() * self.hauteur
        
    def get_hauteur(self):
        return self.hauteur
    
    def set_hauteur(self, nouvelle_hauteur):
        self.hauteur = nouvelle_hauteur



rectangle = Rectangle(5, 3)


print("Périmètre :", rectangle.perimetre())
print("Surface :", rectangle.surface())


rectangle.set_longueur(8)
rectangle.set_largeur(4)
print("Nouvelle longueur :", rectangle.get_longueur())
print("Nouvelle largeur :", rectangle.get_largeur())


parallelepipede = Parallelepipede(5, 3, 2)


print("Volume :", parallelepipede.volume())


parallelepipede.set_longueur(8)
parallelepipede.set_largeur(4)
print("Nouvelle longueur :", parallelepipede.get_longueur())
print("Nouvelle largeur :", parallelepipede.get_largeur())


parallelepipede.set_hauteur(5)
print("Nouvelle hauteur :", parallelepipede.get_hauteur())


