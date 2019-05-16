def listt():
    """Define a function which can generate a list where the values are square of numbers between 1 and 20
    (both included). Then the function needs to print the last 5 elements in the list."""
    tab = []
    for i in range(1, 21):
        tab.append(i**2)
    print(tab[-5:])


listt()
