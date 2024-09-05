# Write a python program to rename a file to “renamed_by_ python.txt. 

import os

current_name = 'problem_11.txt'
new_name = 'renamed_by_python.txt'

os.rename(current_name, new_name)
print(f'The old file name {current_name} is renamed to new file name as {new_name}')