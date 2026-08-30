# Create Rectangle with width, height, and a method area()
class Rectangle :
    def __init__(self, width, height):
        self.width = width 
        self.height = height

    def area(self) :
        return (self.width * self.height)

rect1 = Rectangle(2,3)
print(f"Area : {rect1.area()}")