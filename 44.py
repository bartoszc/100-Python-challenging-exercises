"""Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes",
otherwise print "No". """
strr = input('Enter a string: ')
print('Yes') if strr.lower() == 'yes' else print('No')
