class Animal:
    def __init__(self):
        self.age = 0
        self.pernom = ""
    
    def vieillir(self,):
        self.age += 1

    def nommer(self,nom):
        self.nom = nom


mon_animal = Animal()
print("L'age de l'animal ", mon_animal.age)

mon_animal.vieillir()
print("L'age de l'animal ", mon_animal.age)

mon_animal.nommer("Luna")
print("L'animal se nomme ", mon_animal.nom)

