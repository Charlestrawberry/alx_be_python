class Shape:
    def calculate_area(self):
        print("Area not defined for generic shape")
            

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        return ( f"Area of rectangle:  {area}" )

class Circle(Shape):
    def __init__(self, breadth, height):
        self.breadth = breadth
        self.height = height

    def calculate_area(self):
        area = 0.5 * (self.breadth * self.height)
        return ( f"Area of circle:  {area}" )

class Subcircle(Circle, Rectangle,  Shape):
    def __init__(self, pi, radius):
        self.radius = radius
        self.pi = pi

    def calculate_area(self):
        area = self.pi * self.radius ** 2
        return ( f"Area of Subcircle:  {area}" )
        

rec = Rectangle(5, 8)
cir = Circle(4, 4)
sub = Subcircle(3.142, 5)
print(rec.calculate_area())
# polymorphism
trig = [rec, cir, sub]

for trigs in trig:
    print(trigs.calculate_area())

print("\n---\n")
shape1 = Shape()
shape = Rectangle(7,3)
print(f"{shape.calculate_area()}")

shape1.calculate_area()