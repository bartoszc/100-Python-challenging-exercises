class Division(object):
    """Question:
    Define a class with a generator which can iterate the numbers which are divisible by 7,between a given range 0 and n

    Hints:
    Consider use yield
    """
    def __init__(self, n):
        self.__n = n

    def div(self):
        num = 1
        while num <= self.__n:
            if num % 7 == 0:
                yield num
            num += 1

    def print_num(self):
        for x in Division.div(self):
            print(x)


a1 = Division(50)
a1.div()
a1.print_num()





