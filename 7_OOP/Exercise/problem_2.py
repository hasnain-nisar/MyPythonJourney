# Write a class “Calculator” capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self, n):
        self.n = n

    def square_cube_squareroot(self):
        print(f"The square of {self.n} is {self.n ** 2}")
        print(f"The cube of {self.n} is {self.n ** 3}")
        print(f"The square root of {self.n} is {self.n ** (1/2)}")

# Taking input from the user
user_input = float(input("Enter a number: "))

# Creating a Calculator object with the user input
number = Calculator(user_input)

# Calling the method to perform calculations
number.square_cube_squareroot()