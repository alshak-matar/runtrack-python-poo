class Student:
    def __init__(self, nom, prenom, num_etudiant, credits=0):
        self.nom = nom
        self.prenom = prenom
        self.num_etudiant = num_etudiant
        self.credits = credits
        self.level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.credits += credits
            self.level = self.__studentEval()

    def __studentEval(self):
        if self.credits >= 90:
            return "Excellent"
        elif self.credits >= 80:
            return "Très bien"
        elif self.credits >= 70:
            return "Bien"
        elif self.credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print("Nom: ", self.nom)
        print("Prénom: ", self.prenom)
        print("ID: ", self.num_etudiant)
        print("Niveau: ", self.level)
john_doe = Student("John", "Doe", 145)
john_doe.add_credits(20)
john_doe.add_credits(40)
john_doe.add_credits(30)
john_doe.studentInfo()
