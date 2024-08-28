'''
Recursion is programming technique where a function calls itself in order to solve a problem. A recursive function typically has two key components:

1. Base Case: The condition under which the function stops calling itself. Without a base case, the function would continue to call itself indefinitely, leading to a stack overflow error.

2. Recursive Case: The part of the function where it calls itself to break down the problem into smaller, more manageable sub-problems.

'''

# Example: Factorial of a number:

n = int(input("Enter the number: "))

def factorial(n):
    if n==0 or n==1: # Base case: when n = 0, 1.
        return 1
    else:            # Recursive case: n * factorial of (n-1)
        return n * factorial(n-1)
    
print(f"The factorial of {n} is {factorial(n)}")