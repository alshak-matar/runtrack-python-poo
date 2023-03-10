class Ville:
    def __init__(self, nom, nb_habitants):
        self.nom = nom
        self.nb_habitants = nb_habitants

    def get_nom(self):
        return self.nom

    def get_nb_habitants(self):
        return self.nb_habitants

    def set_nb_habitants(self, nb_habitants):
        self.nb_habitants = nb_habitants


class Personne:
    def __init__(self, nom, age, ville):
        self.nom = nom
        self.age = age
        self.ville = ville

    def ajouterPopulation(self):
        self.ville.set_nb_habitants(self.ville.get_nb_habitants() + 1)


ville_paris = Ville("Paris", 1000000)
print("Nombre d'habitants de la ville de", ville_paris.get_nom(), ":", ville_paris.get_nb_habitants())

ville_marseille = Ville("Marseille", 861635)
print("Nombre d'habitants de la ville de", ville_marseille.get_nom(), ":", ville_marseille.get_nb_habitants())

john = Personne("John", 45, ville_paris)
john.ajouterPopulation()
print("Nombre d'habitants de la ville de", ville_paris.get_nom(), "après l'ajout de John :", ville_paris.get_nb_habitants())

myrtille = Personne("Myrtille", 4, ville_paris)
myrtille.ajouterPopulation()
print("Nombre d'habitants de la ville de", ville_paris.get_nom(), "après l'ajout de Myrtille :", ville_paris.get_nb_habitants())

chloe = Personne("Chloé", 18, ville_marseille)
chloe.ajouterPopulation()
print("Nombre d'habitants de la ville de", ville_marseille.get_nom(), "après l'ajout de Chloé :", ville_marseille.get_nb_habitants())
