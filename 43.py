def tup(t):
    """Write a program to generate and print another tuple whose values are even numbers in the given tuple
    (1,2,3,4,5,6,7,8,9,10). """
    new_t = tuple(list(filter(lambda x: x % 2 == 0, t)))
    print(new_t)


tup_10 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tup(tup_10)