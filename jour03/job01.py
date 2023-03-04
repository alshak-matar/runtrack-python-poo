#most of time I don't understand the instruction in french
#that why i prefer to write everything in english

class City():
  def __init__(self, name,numberOfResident):
    self.name = name
    self.numberOfResident = numberOfResident
    def get_name(self):
      return self.name
    def get_numberOfResident(self):
      return self.numberOfResident
class Persone():
  def __init--(self, name, age, city):
    self.name = name
    self.age = age
    self.city = city
  def resident(self):
    self.city.numberOfResident += 1
city1 : city("NEW YORK", 10000000)
city2 : city("MIAMI", 5000000)
print(city1.get_numberOfResident())
print(city2.get_numberOfResident())
persone1 = Persone("George", 35, city1)
persone2 = Persone("Danisse", 5, city1)
persone3 = Persone("Sara", 15, city2)
persone1.resident()
persone2.resident()
persone3.resident()
print(city1.get_numberOfResident())
print(city2.get_numberOfResident())
