"""By using list comprehension, please write a program to print the list after removing delete numbers which are
divisible by 5 and 7 in [12,24,35,70,88,120,155]."""

LI = [5, 6, 77, 45, 22, 12, 24]
print([x for x in LI if x % 5 != 0 and x % 7 != 0])
