class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def info(self):
        print(f"{self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def info(self):
        print(f"{self.year} {self.make} {self.model} with {self.doors} doors")

class Truck(Vehicle):
    def __init__(self, make, model, year, bed_length):
        super().__init__(make, model, year)
        self.bed_length = bed_length

    def info(self):
        print(f"{self.year} {self.make} {self.model} with a bed length of {self.bed_length} feet")

vehicle_1 = Car("Tesla", "Model S", 2024, 4)
vehicle_2 = Truck("Ford", "F-150", 2024, 8)

vehicle_1.info()
vehicle_2.info()
