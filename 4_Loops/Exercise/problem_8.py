'''Write a program to print the following star pattern: 
* 
** 
***      for n = 3
'''

n = int(input("Enter your Number: "))

for i in range(1, n+1):
    print("*" * i)

# OR

# for i in range(n):
#     print("*" * (i+1))