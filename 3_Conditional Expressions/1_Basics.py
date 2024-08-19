# In programming we must be able to execute instructions on certain conditions(s) being met.

# An example of if else statement

a = int(input("Enter your number: "))

if(a>=10):
    print(f"{a} is greater than or equal to 10.")

else:
    print(f"{a} is less than 10.")

# Below is the example of if elif else ladder.

name = input("Enter your name: ")
a = int(input(f"{name} enter your age: "))

if(a>=18):
    print(f"{name} you are above the age of consent")

elif(a<0):
    print(f"{name} you are entering an invalid age")

else:
    print(f"{name} you are below the age of consent")


# elif statement
# elif in python means [else if]. An if statements can be chained together with a lot of 
# these elif statements followed by an else statement

# 1. There can be any number of elif statements.
# 2. Last else is executed only if all the conditions inside elifs fail.

score = int(input("Netr your score: "))

# If-elif-else statement with more than 2 elif conditions
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")