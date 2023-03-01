class Student():
    def __init__(self, nom, prenom, id):
        self.__nom = nom
        self.__prenom = prenom
        self.__id = id
        self.__credits = 0
        self.__level = ""
    def set_nom(self, nom):
        self.__nom = nom
    def set_prenom(self, prenom):
        self.__prenom = prenom
    def set_id(self, id):
        self.__id = id
    def set_credits(self, credits):
        self.__credits = credits
    def set_level(self):
        self.__level = self.__studentEval(self.get_credits())
    def get_nom(self):
        return(self.__nom)
    def get_prenom(self):
        return(self.__prenom)
    def get_id(self):
        return(self.__id)
    def get_credits(self):
        return(self.__credits)
    def get_level(self):
        self.set_level()
        return(self.__level)

    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits

    def __studentEval(self, credits):
        if credits >= 90:
            return("Excellent")
        elif credits >= 80:
            return("Très bien")
        elif credits >= 70:
            return("Bien")
        elif credits >= 60:
            return("Passable")
        elif credits < 60:
            return("Insufisant")


    def studentInfos(self):
        print("Nom = " ,self.get_nom())
        print("Prenom = ", self.get_prenom())
        print("Id = ", self.get_id())
        print("Level = ", self.get_level())

student1 = Student("Jhon",  "Doe", 145)
print("Le nombre de crédit de ", student1.get_prenom(), student1.get_nom(), "est de", student1.get_credits())
print(student1.get_level())
student1.add_credits(10)
student1.add_credits(10)
student1.add_credits(70)
print("Le nombre de crédit de ", student1.get_prenom(), student1.get_nom(), "est de", student1.get_credits())



student1.studentInfos()
