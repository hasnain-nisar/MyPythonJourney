'''
 When you open a file using the with statement, Python automatically takes care of closing the file for you, even if an error occurs during file operations. This ensures that resources are properly released, which is particularly important when working with files, as forgetting to close a file can lead to memory leaks or data corruption.

'''

with open('with.txt', 'r') as f:
    content = f.read()
    print(content)