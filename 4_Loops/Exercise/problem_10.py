# Write a program to print multiplication table of n using for loops in reversed 
# order.


# An example of table from 1 to 10

n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} * {i} = {n*i}")


# Now for table to be in reverse

n = int(input("Enter the number: "))

for i in range(1, 11):
    print(f"{n} * {11 - i} = {n*(11- i)}")