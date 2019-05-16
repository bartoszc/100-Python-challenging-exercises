"""Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
    Suppose the following input is supplied to the program:
    9
    Then, the output should be:
    11106
    """
N = int(input())
DIGIT = 4
s = 0
for i in range(1, DIGIT+1):
    s += int(str(N)*i)  # '9'*3 = '999'
print(s)
