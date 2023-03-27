class Personne:
    def __init__(self, nom, pernom):
        self.nom = nom
        self.pernom = pernom


    def sePersenter(self):
        print("je suis  " + self.nom)
        print("je suis " + self.pernom)
    
    
    
nom_pernom = Personne("John Doe", "Jean Dupond")
nom_pernom.sePersenter()
