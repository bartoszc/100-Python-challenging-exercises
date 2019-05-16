from pprint import pprint as pp
"""Please write a program which count and print the numbers of each character in a string input by console."""

message = "abcdefgabc"
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pp(count)
