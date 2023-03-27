#JOB07
class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.titre = titre
        self.auteur = auteur
        self.nb_pages = nb_pages
    
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
            print("Erreur! le nombre de pages doit être un entier positif")

mon_livre = Livre("Get Riche", " Tolkien", 10000)


print("Titre :", mon_livre.get_titre())
print("Auteur :", mon_livre.get_auteur())
print("Nombre de pages :", mon_livre.get_nb_pages())


mon_livre.set_nb_pages(12000)


print("Nombre de pages modifié :", mon_livre.get_nb_pages())


mon_livre.set_nb_pages("10000")

print("Nombre de pages inchangé :", mon_livre.get_nb_pages())
