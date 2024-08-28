# Write a program using functions to find greatest of three numbers.

a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))

def greatest(a, b, c):
    if a > b and a > c:
        return f"{a} is greatest."
    elif b > a and b > c:
        return f"{b} is greatest."
    else:
        return f"{c} is greatest"
    
print(greatest(a, b, c))
