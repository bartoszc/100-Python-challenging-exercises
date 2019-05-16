def fib(i):
    """The Fibonacci Sequence is computed based on the following formula:
    f(n)=0 if n=0
    f(n)=1 if n=1
    f(n)=f(n-1)+f(n-2) if n>1
    Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given
    n input by console.
    Example:
    If the following n is given as input to the program:
    7
    Then, the output of the program should be:
    0,1,1,2,3,5,8,13
    """
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i-1) + fib(i-2)


def fib_p(n):
    values = [fib(x) for x in range(0, n+1)]
    print(values)


fib_p(7)
