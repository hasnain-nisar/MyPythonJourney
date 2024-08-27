'''
Write a program to print the following star pattern. 
* * * 
*   *    
* * *  for n = 3
'''

n = int(input("Enter your number: "))

for i in range(n):
    if i==0 or i==(n-1):
        print("*" * n)
    else:
       print("*" + " " * (n-2) + "*")


# OR

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()