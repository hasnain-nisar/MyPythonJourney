# Write a program to find the greatest of four numbers entered by the user. 

a1 = int(input("Enter number 1: "))
a2 = int(input("Enter number 2: "))
a3 = int(input("Enter number 3: "))
a4 = int(input("Enter number 4: "))

if a1 > a2 and a1 > a3 and a1 > a4:
    print("Greates number is a1", a1)

if a2 > a1 and a2 > a3 and a2 > a4:
    print("Greatest number is a2", a2)

if a3 > a1 and a3 > a2 and a3 > a4:
    print("Greates number is a3", a3)

if a4 > a1 and a4 > a2 and a4 > a3:
    print("Greates number is a4", a4)


# Developing the function to find greatest of 4 numbers.

def find_greatest(num1, num2, num3, num4):
    greatest = num1 # Assume the first number is greatest initially

    # Compare with the second number.
    if num2 > greatest:
        greatest = num2
    
    # Compare with the third number.
    if num3 > greatest:
        greatest = num3

    # Compare with the fourth number.
    if num4 > greatest:
        greatest = num4

    return greatest

# Input four numbers from the user.

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
num4 = float(input("Enter number 4: "))

# Call the function and print the greatest number

greatest_number = find_greatest(num1, num2, num3, num4)
print(f"Greatest number is {greatest_number}")


# Another more concise way
nums = [float(input("Enter a number: ")) for _ in 4*[None]]

# Find and print the greatest number.
print(f"The greatest number is {max(nums)}")
