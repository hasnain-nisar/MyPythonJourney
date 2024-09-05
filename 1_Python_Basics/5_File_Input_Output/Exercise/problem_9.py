# Write a program to find out whether a file is identical & matches the content of 
# another file. 

with open('problem_9_1.txt') as file:
    content1 = file.read()

with open('problem_9_2.txt') as file:
    content2 = file.read()


if content1 == content2:
    print('Files are identical.')

else:
    print('Files are not identical.')