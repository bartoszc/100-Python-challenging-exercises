import math as m


class Circle:
    """Define a class named Circle which can be constructed by a radius.
    The Circle class has a method which can compute the area"""
    def __init__(self, radius):
        self.__radius = radius

    def count_area(self):
        return m.pi * self.__radius ** 2

    def print_area(self):
        print(self.count_area())


objs = [Circle(i) for i in range(1, 10)]
for obj in objs:
    obj.print_area()

