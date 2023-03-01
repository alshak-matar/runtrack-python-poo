class Persone():

    def __init__(self, second_name, first_name):
        self.first_name = first_name 
        self.second_name = second_name
    def persention(self):
        print("I'm", self.first_name,self.second_name)
persone1 = Persone("Jhon", "Doe")
persone2 = Persone("Jean", "Dupond")

persone1.persention()
persone2.persention()
