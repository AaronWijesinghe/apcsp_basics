class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("The car is starting.")

    def info(self):
        print(f"This car is a {self.year} {self.brand} Model {self.model}.")

car1 = Car("Tesla", "S", "2024")
car1.start()
car1.info()