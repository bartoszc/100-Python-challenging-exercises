def task(minn, maxx):
    """Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
    between 2000 and 3200 (both included).
    The numbers obtained should be printed in a comma-separated sequence on a single line.

    Hints:
    Consider use range(#begin, #end) method
    """
    tab = []
    for i in range(minn, maxx):
        if i % 5 != 0 and i % 7 == 0:
            tab.append(i)
    print(tab)


task(2000, 3201)
