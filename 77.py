"""Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 200 inclusive using
random module and list comprehension."""

import random

print(random.choice([i for i in range(201) if i % 5 == 0 and i % 7 == 0]))

