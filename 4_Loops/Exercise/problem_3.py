# Write a program to print multiplication table of a given number using while loop.

num = int(input('Enter the number: '))

i = 0
while i < 11:
    print(f" {num} * {i} = {num * i}")
    i += 1