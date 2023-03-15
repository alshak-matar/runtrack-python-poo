class Vehicle:
    def __init__(self, brand, year, price):
        self.brand = brand
        self.year = year
        self.price = price
    
    def vehicle_information(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}")
    

    def start(self):
        print("Warning, I rolled.")

class Car(Vehicle):
    def __init__(self, brand, year, price):
        super().__init__(brand, year, price)
        self.doors = 4
    
    def vehicle_information(self):
        super().vehicle_information()
        print(f"Doors: {self.doors}")

    def start(self):
        print(f"{self.brand} is started.")


class Motorcycle(Vehicle):
    def __init__(self, brand, year, price):
        super().__init__(brand, year, price)
        self.wheel = 2
    
    def information_vehicle(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")
        print(f"Price: {self.price}")
        print(f"Wheels: {self.wheel}")

    def start(self):
        print(f"{self.brand} motorcycle is started.")


car = Car("Toyota", 2022, 25000)
car.vehicle_information()
car.start()

motorcycle = Motorcycle("Honda", 2021, 12000)
motorcycle.information_vehicle()
motorcycle.start()
