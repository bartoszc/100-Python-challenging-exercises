def exc(n):
    """Write a program to compute:

    f(n)=f(n-1)+100 when n>0
    and f(0)=1
    """
    if n == 0:
        return 0
    else:
        return exc(n-1) + 100


print(exc(5))
