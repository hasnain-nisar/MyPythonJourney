# Write a program to find out the line number where python is present from ques 6. 

with open('problem_7.txt', 'r') as file:
    lines = file.readlines()

# Loop through each line and check if the word 'Python' is in the line
for i,line in enumerate(lines, start=1):
    if 'python' in line:
        print(f"'python' found on line {i}")
