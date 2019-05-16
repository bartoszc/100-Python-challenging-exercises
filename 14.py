def count(strr):
    """Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
    Suppose the following input is supplied to the program:
    Hello world!
    Then, the output should be:
    UPPER CASE 1
    LOWER CASE 9
    """
    result = {'UPPER CASE': 0, 'LOWER CASE': 0}

    for i in strr:
        if i.isupper():
            result['UPPER CASE'] += 1
        else:
            if i.islower():
                result['LOWER CASE'] += 1

    print('UPPER CASE', result['UPPER CASE'])
    print('LOWER CASE', result['LOWER CASE'])


content = input()
count(content)
