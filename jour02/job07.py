import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    
    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"

class Jeu:
    couleurs = ["coeur", "carreau", "pique", "trèfle"]
    valeurs = [str(i) for i in range(2, 11)] + ["valet", "dame", "roi", "as"]
    valeurs_points = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "valet": 10, "dame": 10, "roi": 10, "as": 11}

    def __init__(self):
        self.paquet = [Carte(valeur, couleur) for couleur in self.couleurs for valeur in self.valeurs]
    
    def melanger(self):
        random.shuffle(self.paquet)
    
    def distribuer_cartes(self):
        return [self.paquet.pop(), self.paquet.pop()]
    
    def donner_carte(self):
        return self.paquet.pop()
    
    @staticmethod
    def calculer_points(main):
        total = sum([Jeu.valeurs_points[carte.valeur] for carte in main])
        as_count = sum([1 for carte in main if carte.valeur == "as"])
        while as_count > 0 and total > 21:
            total -= 10
            as_count -= 1
        return total

class Joueur:
    def __init__(self):
        self.main = []
    
    def recevoir_cartes(self, cartes):
        self.main += cartes
    
    def jouer(self, jeu):
        while True:
            print("Votre main :", self.main, "Total :", jeu.calculer_points(self.main))
            choix = input("Voulez-vous prendre une carte ? (o/n) ")
            if choix.lower() == "o":
                carte = jeu.donner_carte()
                self.recevoir_cartes([carte])
                print("Vous avez reçu :", carte)
                if jeu.calculer_points(self.main) > 21:
                    print("Vous avez dépassé 21, vous avez perdu.")
                    return "perdu"
            else:
                return "reste"

class Croupier(Joueur):
    def __init__(self):
        super().__init__()
    
    def jouer(self, jeu):
        while jeu.calculer_points(self.main) < 17:
            carte = jeu.donner_carte()
            self.recevoir_cartes([carte])
            print("Le croupier a reçu :", carte)
        if jeu.calculer_points(self.main) > 21:
            print("Le croupier a dépassé 21, vous avez gagné.")
            return "gagné"
        else:
            return "reste"
def jouer_blackjack():
    jeu = Jeu()
    jeu.melanger()
    joueur = Joueur()
    croupier = Croupier()
    
    joueur.recevoir_cartes(jeu.distribuer_cartes())
    croupier.recevoir_cartes(jeu.distribuer_cartes())

    resultat = joueur.jouer(jeu)
    if resultat == "perdu":
        print("Vous avez perdu.")
        return

    resultat = croupier.jouer(jeu)
    if resultat == "gagné":
        print("Vous avez gagné !")
    else:
        total_joueur = jeu.calculer_points(joueur.main)
        total_croupier = jeu.calculer_points(croupier.main)
        if total_joueur > total_croupier:
            print("Vous avez gagné !")
        elif total_joueur == total_croupier:
            print("Match nul.")
        else:
            print("Le croupier a gagné.")
jouer_blackjack()
