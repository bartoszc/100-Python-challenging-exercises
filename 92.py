"""By using list comprehension, please write a program to print the list after removing the value 24 in
[12,24,35,24,88,120,155]."""

li = [12, 24, 35, 70, 88, 120, 155]
print(([x for x in li if x != 24]))
