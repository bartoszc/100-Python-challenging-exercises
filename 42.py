def tup(n):
    """With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the
    last half values in one line. """
    print(n[:int(len(n)/2)])
    print(n[int(len(n)/2):])


tuple_n = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tup(tuple_n)
