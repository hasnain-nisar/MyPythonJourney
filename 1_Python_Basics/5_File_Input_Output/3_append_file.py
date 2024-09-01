# 'a': Append (writes data to the end of the file).

f = open('append.txt', 'a')

f.write('\nThis is a new line added to append.txt file.\n')
f.write('This is another new line without using backslashn at the end')
f.write('This is another new line.')

f.close()

# Remember every time you ru the programme, it appends new lines to the end of the file.

# To avoid same lines multiple times we can use this code.

# Open the file in read mode to check existing content
with open("file.txt", "r") as f:
    lines = f.readlines()

'''

# The line you want to add
new_line = "This is a new line added to the file.\n"

# Check if the line already exists
if new_line not in lines:
    # Open the file in append mode and write the line
    with open("file.txt", "a") as f:
        f.write(new_line)

'''