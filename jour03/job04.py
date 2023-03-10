class Joueur:
    def __init__(self, nom, numero, position, nb_buts=0, passes_decisives=0, cartons_jaunes=0, cartons_rouges=0):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.nb_buts = nb_buts
        self.passes_decisives = passes_decisives
        self.cartons_jaunes = cartons_jaunes
        self.cartons_rouges = cartons_rouges

    def marquerUnBut(self):
        self.nb_buts += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"{self.nom} ({self.position}, n°{self.numero}): {self.nb_buts} buts, {self.passes_decisives} passes décisives, {self.cartons_jaunes} cartons jaunes, {self.cartons_rouges} cartons rouges")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, numero_joueur, methode, *args):
        for joueur in self.joueurs:
            if joueur.numero == numero_joueur:
                methode(joueur, *args)
                break
        else:
            print(f"Joueur n°{numero_joueur} non trouvé dans l'équipe {self.nom}.")



j1 = Joueur("Ronaldo", 7, "attaquant")
j2 = Joueur("Messi", 10, "attaquant")
j3 = Joueur("Mbappé", 11, "attaquant")
j4 = Joueur("Varane", 4, "défenseur")
j5 = Joueur("Kanté", 6, "milieu")


equipe1 = Equipe("Real Madrid")
equipe2 = Equipe("Barcelone")


equipe1.ajouterJoueur(j1)
equipe1.ajouterJoueur(j4)
equipe1.ajouterJoueur(j5)
equipe2.ajouterJoueur(j2)
equipe2.ajouterJoueur(j3)
equipe2.ajouterJoueur(j5)


equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

