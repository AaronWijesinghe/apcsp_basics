class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, width, height):
        super()