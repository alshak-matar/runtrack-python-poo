class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    def changer_nom(self, nom):
        self.nom = nom
    def changer_prix(self, prixHT):
        self.prixHT = prixHT
    def nom_produit(self):
        return self.nom
    def prixHT_produit(self):
        return self.prixHT
    def TVA_produit(self):
        return self.TVA
    def CalculerPrixTTC(self):
        prixTTC = self.prixHT + (self.prixHT * self.TVA)
        return prixTTC
    def afficher(self):
        liste_produit = (self.nom, self.prixHT, str(self.TVA), self.CalculerPrixTTC())
        return liste_produit
patate= Produit('patate', 10, 0.20)
ps5 = Produit('PS5', 400, 0.20)
tele = Produit('télé', 250, 0.20)
print(patate.afficher())
print(ps5.afficher())
print(tele.afficher())
print(patate.nom_produit())
print(str(patate.prixHT_produit())+'€ HT')
print(str(patate.TVA_produit()*100)+'%','TVA')
print(str(patate.CalculerPrixTTC())+ '€ TTC\n')
