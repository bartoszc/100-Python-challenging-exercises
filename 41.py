def func():
    """Define a function which can generate and print a tuple where the value are square of numbers between
    1 and 20 (both included). """
    tab = []
    for i in range(1, 21):
        tab.append(i**2)
    print(tuple(tab))


func()
