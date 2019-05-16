class Shape(object):
    """Define a class named Shape and its subclass Square. The Square class has an init function which takes a length
    as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by
    default."""
    def __init__(self, length):
        self.length = length
        self.field = 0

    def area(self):
        print(str(self.field))


class Square(Shape):
    def area(self):
        self.field = self.length * self.length
        print(str(self.field))


sh1 = Shape(4)
sh1.area()

sq1 = Square(4)
sq1.area()
