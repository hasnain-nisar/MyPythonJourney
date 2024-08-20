# Write a program which finds out whether a given name is present in a list or not.

name_list = ["Hasnain", "Nisar", "Ali", "Umer"]

name = input('Enter your name: ')

if name in name_list:
    print(f'{name} is in the list.')

else:
    print(f"{name} is not in the list.")