class Animal():

    def __init__(self):
        self.age = 0
        self.prenom = ""
    def vieillir(self):
        self.age +=1
    def nommer(self, prenom):
        self.prenom = prenom
animal1 = Animal()
print(animal1.age,"ans")
print(animal1.prenom)
animal1.vieillir()
animal1.nommer("Bob")
print(animal1.age, "ans")
print(animal1.prenom)
