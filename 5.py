class Toupper(object):
    """Define a class which has at least two methods:
    getString: to get a string from console input
    printString: to print the string in upper case.
    Also please include simple test function to test the class methods.
    """
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input('Enter a string: ')

    def print_string(self):
        print(self.s.upper())


t1 = Toupper()
t1.get_string()
t1.print_string()
