# Create Shape with area() returning 0. Create Circle and Square that override area() correctly.
# (Light inheritance — no super() deep-dive needed.)

class Shape : 
    def area(self) :
        return 0

class Circle (Shape) :
    def __init__(self,radius):
        self.radius = radius

    def area(self) :
        return ( 3.14 * self.radius * self.radius)

class Square(Shape) :
    def __init__(self,side):
        self.side = side

    def area(self) :
        return (self.side * self.side)

c1 = Circle(5)
print(c1.area())
s1 = Square(4)
print(s1.area())