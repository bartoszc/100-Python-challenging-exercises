from pprint import pprint


def dicti():
    """Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included)
    and the values are square of keys."""
    d = {}
    for i in range(1, 21):
        d[i] = i**2
    pprint(d)


dicti()
