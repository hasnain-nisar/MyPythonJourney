'''
Store the multiplication tables generated in problem 3 in a file named Tables.txt.
'''

num = int(input("Enter a number: "))

table = [num *i for i in range(1, 11)]

print(table)


with open('Table.txt', 'a') as f:
    f.write(f"Table of {num} {str(table)} \n")