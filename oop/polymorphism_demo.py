import math

class Shape:
    def __init__(self):
        return

    def area(self):
        raise NotImplementedError("Subclasses must implement __str__ method")
    
class Rectangle(Shape):
    def __init__(self, length,  width):
        self.length =length
        self.width = width
    
    def area(self):
        area = self.length * self.width
        return area

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * (self.radius ** 2)
        return area

if __name__ == "__main__":
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
