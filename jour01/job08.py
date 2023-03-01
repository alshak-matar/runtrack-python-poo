import math




class Cercle():
    def __init__(self, rayon):
        self.rayon = rayon
    def changerRayon(self, rayon):
        self.rayon = rayon
    def circonference(self):
        return((2 * math.pi) * self.rayon)
    def aire(self):
        return((self.rayon * self.rayon) * math.pi)
    def diametre(self):
        return(self.rayon * 2)
    def afficherInfos(self):
        print(self.aire())
        print(self.diametre())
        print(self.circonference())
cerc1 = Cercle(4)
cerc2 = Cercle(7)
cerc1.afficherInfos()
cerc2.afficherInfos()
