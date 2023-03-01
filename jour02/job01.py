class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def __setLongeur(self):
        self.longueur = input('entrer une longeur: ')
        return self.longueur

    def getLongeur(self):
        self.__setLongeur()

    def __setLargeur(self):
        self.largeur = input('Entrer une largeur : ')
        return self.largeur

    def getLargeur(self):
        self.__setLargeur()

    def AfficherLongeur(self):
        return self.longueur

    def AfficherLargeur(self):
        return self.largeur
rectangle = Rectangle(10,5)
print('la longeur est de',rectangle.AfficherLongeur())
print('La largeur est de', rectangle.AfficherLargeur())
rectangle.getLongeur()
rectangle.getLargeur()
print('la longeur est de',rectangle.AfficherLongeur())
print('La largeur est de', rectangle.AfficherLargeur())
