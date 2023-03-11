import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    
    def attaquer(self, autre_personnage):
        degats = random.randint(1, 10)
        print(f"{self.nom} attaque {autre_personnage.nom} et lui inflige {degats} points de dégâts.")
        autre_personnage.vie -= degats
    
    def est_en_vie(self):
        return self.vie > 0

class Jeu:
    def __init__(self):
        self.niveau = None
    
    def choisir_niveau(self):
        self.niveau = int(input("Choisissez votre niveau (1, 2 ou 3) : "))
    
    def lancer_jeu(self):
        if self.niveau is None:
            self.choisir_niveau()
        
        if self.niveau == 1:
            joueur = Personnage("Joueur", 50)
            ennemi = Personnage("Ennemi", 30)
        elif self.niveau == 2:
            joueur = Personnage("Joueur", 40)
            ennemi = Personnage("Ennemi", 40)
        elif self.niveau == 3:
            joueur = Personnage("Joueur", 30)
            ennemi = Personnage("Ennemi", 50)
        else:
            print("Niveau invalide")
            return
        
        print(f"Vous commencez le combat contre {ennemi.nom} avec {joueur.vie} points de vie.")
        print("Que le combat commence !")
        
        while joueur.est_en_vie() and ennemi.est_en_vie():
            joueur.attaquer(ennemi)
            ennemi.attaquer(joueur)
            
            print(f"Vous avez {joueur.vie} points de vie.")
            print(f"{ennemi.nom} a {ennemi.vie} points de vie.")
        
        if joueur.est_en_vie():
            print("Vous avez gagné !")
        else:
            print("Vous avez perdu...")

jeu = Jeu()
jeu.lancer_jeu()
