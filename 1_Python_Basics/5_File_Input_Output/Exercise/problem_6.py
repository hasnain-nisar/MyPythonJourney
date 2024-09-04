# Write a program to mine a log file and find out whether it contains ‘python’. 

with open('problem_6.txt', 'r') as file:
    content = file.read().lower()

if 'python' in content:
    print('Yes python is present in content.')

else:
    print('No python is not present in content.')