class Food:
    def __init__(self, name, origin, flavor):
        self.name = name
        self.origin = origin
        self.flavor = flavor
    
    def eat():
        pass

class Pizza(Food):
    def __init__(self):
        self.name = "pizza"
        self.origin = "italy"
        self.flavor = "savory"
    
    def eat(self):
        print(f"That is some {self.flavor} {self.name} from {self.origin.capitalize()}!")

Pizza().eat()