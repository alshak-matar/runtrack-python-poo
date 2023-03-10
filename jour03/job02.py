class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Numéro de compte : {self.__numero}")
        print(f"Titulaire : {self.__prenom} {self.__nom}")
        print(f"Solde : {self.__solde} euros")
        if self.__decouvert:
            print("Découvert autorisé")
        else:
            print("Découvert non autorisé")

    def afficherSolde(self):
        print(f"Le solde du compte est de {self.__solde} euros")

    def versement(self, montant):
        self.__solde += montant
        print(f"{montant} euros ont été ajoutés au compte")
        self.afficherSolde()

    def retrait(self, montant):
        if self.__decouvert or self.__solde >= montant:
            self.__solde -= montant
            print(f"{montant} euros ont été retirés du compte")
            self.afficherSolde()
        else:
            print("Opération impossible : solde insuffisant")

    def agios(self, taux):
        if self.__solde < 0:
            montant_agios = -self.__solde * taux
            self.__solde -= montant_agios
            print(f"{montant_agios} euros d'agios ont été prélevés sur le compte")
            self.afficherSolde()

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print("Virement effectué avec succès")
            self.afficherSolde()
        else:
            print("Opération impossible : solde insuffisant")


compte1 = CompteBancaire("85303427", "Dupont", "Jean", 3000, False)
compte1.afficher()

compte1.versement(300)
compte1.retrait(250)
compte1.agios(0.06)

compte2 = CompteBancaire("93472465", "Martin", "Sophie", -600, True)
compte2.afficher()

compte1.virement(compte2, 800)
compte1.afficher()
compte2.afficher()
