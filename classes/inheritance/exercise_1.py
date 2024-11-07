import math

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

shape_1 = Rectangle(10, 20)
shape_2 = Circle(10)

print(str(shape_1.area()))
print(str(shape_1.perimeter()))
print(str(shape_2.area()))
print(str(shape_2.circumference()))
