import math

class Shape:
    def __init__(self, length=None, width=None, radius=None):
        self.length = length
        self.width = width
        self.radius = radius

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length=length, width=width)

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius=radius)

    def area(self):
        return math.pi * self.radius ** 2


# Example usage
rect = Rectangle(10, 5)
circle = Circle(7)

print("Rectangle Area:", rect.area())
print("Circle Area:", circle.area())

