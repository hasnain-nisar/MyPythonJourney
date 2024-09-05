# Write a program to make a copy of a text file “this. txt” 

with open('problem_8_this.txt', 'r') as file:
    content = file.read()

with open('problem_8_copy_this.txt', 'w') as file:
    file.write(content)