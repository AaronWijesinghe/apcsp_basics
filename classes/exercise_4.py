class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print(f"The area of the rectangle is {self.width * self.height}.")

    def perimeter(self):
        print(f"The perimeter of the rectangle is {2 * self.width + 2 * self.height}.")

rectangle1 = Rectangle(6, 9)
rectangle1.area()
rectangle1.perimeter()