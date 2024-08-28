'''
A function is a group of statement performing specific task.
It can take inputs called paramenters or arguments process them and return an output.
'''

# A function to calculate average of three numbers.

def avg():
    a = int(input("Enter your Number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a + b + c)/3
    print(average)

# # Calling the function

avg()
print('Thankyou!')
avg()
print('Thank You!')
avg()

# A function to calculate average of n numbers.

def calculate_average():
    n = int(input("Enter the number of values: ")) # Ask the user how many values they have.

    # Initialize a variable to store the sum of numbers.
    total = 0

    # Loop to get each number from the user.
    for i in range(n):
        number = float(input(f"Enter number {i + 1}: "))
        total += number

    # Calculatre the avg
    average = total/n

    # Return the calculated average.
    return average

# Call the function

avg = calculate_average()
print(f'The average of entered numbers is {avg}')

# A function can be called any number of times, anywhere in th eprogramme

'''
There are 2 types of function in python.

1. Built-in function (Already present in python)

2. User-defined function (Defined by the user.)

'''