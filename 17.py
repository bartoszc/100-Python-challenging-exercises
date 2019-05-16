"""Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""

amount = 0

while True:
    answer = input('Enter value: ')
    values = answer.split(" ")
    if not answer:
        print(amount)
        break
    else:
        operation = values[0]
        quantity = int(values[1])
        if operation == 'D':
            amount += quantity
            print(amount)
        elif operation == 'W':
            if amount < quantity:
                print('Incorrect operation')
            else:
                amount -= quantity
                print(amount)
        else:
            print('Incorrect operation')