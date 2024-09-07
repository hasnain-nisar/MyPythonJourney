# Add a static method in problem 2, to greet the user with hello.

'''
Problem_2 Statement:
Write a class “Calculator” capable of finding square, cube and square root of a number.
'''

class Calculator:
    def __init__(self, n):
        self.n = n

    @staticmethod
    def hello():
        print("Hello!")

    def square_cube_squareroot(self):
        print(f"The square of {self.n} is {self.n ** 2}")
        print(f"The cube of {self.n} is {self.n ** 3}")
        print(f"The square root of {self.n} is {self.n ** (1/2)}")

# Taking input from the user
user_input = float(input("Enter a number: "))

# Creating a Calculator object with the user input
obj = Calculator(user_input)

# Greeting function
obj.hello()

# Calling the method to perform calculations
obj.square_cube_squareroot()