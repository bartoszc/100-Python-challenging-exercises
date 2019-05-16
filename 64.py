def exc(n):
    """Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0)."""
    total = 0
    for x in range(1, n+1):
        total += x/(x+1)
    return total


print(exc(5))
