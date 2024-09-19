'''
Write a program to display a/b where a and b are integers. If b=0, display infinite by 
handling the 'ZeroDivisionError'. 
'''

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))   
try: 
    result = a/b
    print(result)
except ZeroDivisionError:
    print("Infinite")