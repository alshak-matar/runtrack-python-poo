class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def bonjour(self):
        print("Bonjour, je m'appelle", self.nom)
    
    def allerEnCours(self):
        print("Je vais en cours")

class Eleve(Personne):
    def __init__(self, nom, age):
        super().__init__(nom, age)
        self.age = 15

class Professeur(Personne):
    def enseigner(self):
        print("Le cours commence !")

eleve = Eleve("Jean", 13)
eleve.bonjour()
eleve.allerEnCours()

professeur = Professeur("Dupont", 40)
professeur.bonjour()
professeur.enseigner()
