'''
A file contains a word “Donkey” multiple times. You need to write a program 
which replace this word with ##### by updating the same file.
'''

with open('problem_4.txt', 'r') as file:
    content = file.read()

# Replace all occurence of "donkey" with "######"
updated_content = content.replace('Donkey'.lower(), '######')

# Open the file in write mode and update it with the modified content
with open('problem_4.txt', 'w') as file:
    file.write(updated_content)

print("The word 'Donkey' has been replaced with '#####' in the file.")