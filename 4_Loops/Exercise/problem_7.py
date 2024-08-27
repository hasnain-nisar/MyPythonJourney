'''
Write a program to print the following star pattern. 
   * 
  *** 
 ***** for n = 3 
'''
 
n = int(input('Enter the number: '))

for i in range(n):
    print(" " * (n - i - 1), end="") # The end="" means the next print function will print in the same line, otherwise print function will move to next line.
    print("*" * (2*i + 1))