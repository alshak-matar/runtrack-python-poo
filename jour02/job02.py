class Livre():

    def __init__(self, titre, auteur, nombrePages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombrePages = nombrePages


    def set_titre(self, titre):
        self.__titre = titre
    def set_auteur(self, auteur):
        self.__auteur = auteur
    def set_nombrePages(self, nombrePages):
        if nombrePages > 0:
            self.__nombrePages = nombrePages
        else:
            print("the page number must be an integer")
    
    def get_titre(self):
        return(self.__titre)
    def get_auteur(self):
        return(self.__auteur)
    def get_nombrePages(self):
        return(self.__nombrePages)



livre1  = Livre("bob", "bob", 5)
print(livre1.get_titre())
print(livre1.get_auteur())
print(livre1.get_nombrePages())
livre1.set_auteur("eric")
livre1.set_titre("eric")
livre1.set_nombrePages(7)
print(livre1.get_titre())
print(livre1.get_auteur())
print(livre1.get_nombrePages())
