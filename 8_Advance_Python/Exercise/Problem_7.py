'''
A list contains the multiplication table of 7. write a program to convert it to vertical 
string of same numbers.
'''

table = [7*i for i in range(1, 11)]

vertical_string = "\n".join(map(str, table))

print(vertical_string)