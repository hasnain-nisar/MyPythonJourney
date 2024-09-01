'''
To open a file, you use the open() function. This function requires the file path and an optional mode argument. Common modes are:

'r': Read (default mode).
'w': Write (creates a new file or truncates an existing file).
'a': Append (writes data to the end of the file).
'b': Binary mode (used with other modes to handle binary files).
'+': Open for updating.

'''

'''
Ensure that working directory of your script is set to the directory where the file is located. The FileNotFoundError occurs when Python cannot locate the file specified in the open() function. This often happens when the file path is relative, and the script is executed from a different directory than where the file resides.

'''


f = open("read.txt")  # open() function has its default mode set to 'r', for other specify.
data = f.read()
print(data)
f.close()   # f.close() makes sure the file is properly saved and frees up system resources.

# readlines() function.

f = open('read.txt')
lines = f.readlines()  # .readlines() generates a list of lines.
print(lines)
print(type(lines))
f.close()


# readline() function

# readline() is used to read a single line from a file.

# reads from the current position in the file until it encounters a newline character (\n) or reaches the end of the file.

# readline() returns a string. 

f = open('read.txt')

line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2)) 

# for line 2 if you see in read.txt there is blank line, but it will give blank line in output,

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))

line5 = f.readline()
print(line5, type(line5))

line6 = f.readline()
print(line6, type(line6))  
print(line6 == "") #Output: True

# Even there are only 5 lines, this is still giving me empty string as a output.

f.close()


'''
When readline() reaches the end of the file and is called again, it doesn’t raise an error. Instead, it returns an empty string (''), which can be used to check for the end of the file in loops or conditions.

'''

f = open('read.txt')

line = f.readline()
while line != '':
    print(line)
    line = f.readline()

f.close()