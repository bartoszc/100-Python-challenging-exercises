def sset(li):
    """With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all
    duplicate values with original order reserved."""
    new_l = []
    set_l = set()
    for item in li:
        if item not in set_l:
            set_l.add(item)
            new_l.append(item)
    print(set_l)
    print(new_l)


sset([12, 24, 35, 24, 88, 120, 155, 88, 120, 155])
