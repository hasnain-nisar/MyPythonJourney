# Write a function which converts inches to cm.

inch = int(input("Enter value in inches: "))

def inch_to_cm(inch):
    return inch * 2.54

print(f"{inch} inches is equal to {inch_to_cm(inch)} in cm.")