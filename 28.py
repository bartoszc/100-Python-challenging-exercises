def conv(str1, str2):
    """Define a function that can receive two integral numbers in string form and compute their sum and then print
    it in console."""
    try:
        str1 = int(str1)
        str2 = int(str2)
        print(str1+str2)
    except ValueError:
        print('This conversion is not possible')


conv('1', '2')
conv('1.0', '2.5')
conv('1', 'ttt')

