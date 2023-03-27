class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.titre = titre
        self.auteur = auteur
        self.nb_pages = nb_pages
        self.disponible = True
    
    def get_titre(self):
        return self.titre
    
    def set_titre(self, titre):
        self.titre = titre
    
    def get_auteur(self):
        return self.auteur
    
    def set_auteur(self, auteur):
        self.auteur = auteur
    
    def get_nb_pages(self):
        return self.nb_pages
    
    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.nb_pages = nb_pages
        else:
            print("Erreur! le nombre de pages doit être un entier positif.")
    
    def verification(self):
        return self.disponible
    
    def emprunter(self):
        if self.verification():
            self.disponible = False
            print("Le livre a été emprunté.")
        else:
            print("Le livre n'est pas disponible pour le moment.")
    
    def rendre(self):
        if not self.verification():
            self.disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté auparavant.")

mon_livre = Livre("Harry Potter à l'école des sorciers", " Rowling", 300)

print("Titre :", mon_livre.get_titre())
print("Auteur :", mon_livre.get_auteur())
print("Nombre de pages :", mon_livre.get_nb_pages())


mon_livre.set_nb_pages(-50)


mon_livre.set_nb_pages(400)
print("Nouveau nombre de pages :", mon_livre.get_nb_pages())


print("Le livre est disponible :", mon_livre.verification())


mon_livre.emprunter()


mon_livre.emprunter()


mon_livre.rendre()


mon_livre.rendre()
