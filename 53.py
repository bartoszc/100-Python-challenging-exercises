class Rectangle:
    """Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method
    which can compute the area. """
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width
        self.result = None

    def compute(self):
        self.result = self.width * self.length

    def __str__(self):
        res = ""
        res += 'Field: ' + str(self.result)
        return res


r1 = Rectangle(2, 3)
r1.compute()
print(r1)
