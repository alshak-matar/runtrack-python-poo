class Personne:
    def __init__(self, age=14):
        self.age = age
        
    def afficherAge(self):
        print("J'ai", self.age, "ans")
        
    def bonjour(self):
        print("Hello")
        
    def modifierAge(self, nouvel_age):
        self.age = nouvel_age
        
        
class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
        
    def affichageAge(self):
        print("J'ai", self.age, "ans")
        
        
class Professeur(Personne):
    def __init__(self, age, matiereEnseignee):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee
        
    def enseigner(self):
        print("Le cours va commencer")
        

personne = Personne()
eleve = Eleve()


print("Age de l'élève :", eleve.age)


eleve.bonjour()
eleve.allerEnCours()


eleve.modifierAge(15)


professeur = Professeur(40, "Mathématiques")


professeur.bonjour()
professeur.enseigner()
