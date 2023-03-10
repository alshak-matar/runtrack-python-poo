class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"
        
class ListeDeTaches:
    def __init__(self):
        self.taches = []
    
    def ajouterTache(self, tache):
        self.taches.append(tache)
        
    def supprimerTache(self, tache):
        self.taches.remove(tache)
        
    def marquerCommeFinie(self, tache):
        tache.statut = "terminé"
        
    def afficherListe(self):
        for tache in self.taches:
            print("Tache : {}\nDescription : {}\nStatut : {}\n".format(tache.titre, tache.description, tache.statut))
            
    def filterListe(self, statut):
        return [tache for tache in self.taches if tache.statut == statut]

tache1 = Tache("Faire les courses", "Acheter du pain, du lait et des oeufs")
tache2 = Tache("Faire du sport", "Aller à la salle de sport")
tache3 = Tache("Faire la vaisselle", "Nettoyer les assiettes et les couverts")

liste_taches = ListeDeTaches()

liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

liste_taches.afficherListe()


taches_a_faire = liste_taches.filterListe("à faire")
print("Taches à faire : ")
for tache in taches_a_faire:
    print("- {}".format(tache.titre))
    
liste_taches.supprimerTache(tache2)

liste_taches.marquerCommeFinie(tache1)


liste_taches.afficherListe()
