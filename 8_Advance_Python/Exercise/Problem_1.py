'''
Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not 
present, a message without exiting the program must be printed prompting the same. 
'''

try:
    with open("1.txt", 'r') as file:
        print(file.read())
except Exception as e:
    print(e)

try:
    with open("2.txt", 'r') as file:
        print(file.read())
except Exception as e:
    print(e)

try:
    with open("3.txt", 'r') as file:
        print(file.read())
except Exception as e:
    print(e)


# OR

filename = ['1.txt', '2.txt', '3.txt']

for file in filename:
    try:
        with open(file) as f:
            print(f.read()) 
    except FileNotFoundError:
        print(f"Error: {file} not found.")


