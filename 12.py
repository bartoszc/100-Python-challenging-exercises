def find():
    """Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of
    the number is an even number.
    The numbers obtained should be printed in a comma-separated sequence on a single line.
    """
    first = []
    for number in range(1000, 3001):
        first.append(str(number))

    result = []
    for word in first:
        if int(word[0]) % 2 == 0 and int(word[1]) % 2 == 0 and int(word[2]) % 2 == 0 and int(word[3]) % 2 == 0:
            result.append(str(word))
    print(', '.join(result))


find()