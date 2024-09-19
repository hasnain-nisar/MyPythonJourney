'''
In python try and except bloks are used to handle exceptions (runtime errors) in a controlled way. This allows your programme to continue executing or gracefully handle errors when something unexcepted happens.
'''

# Handling a specific exception.
try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Handling multiple exceptions.
try: 
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("That's not a valid number!")


# Using else and finally

'''
else: The else block is executed if no execptions are raised in the try block.
finally: The finally block is always executrd, wheather an execption occur or not. It is typically used for cleanup actions such as closing files or database connections.
'''

try:
    num = int(input("Enter a number: "))
    result = 10 / num   
except ZeroDivisionError:
    print("You cannot divide by zero")
except ValueError:
    print("That's not a valid number!")
else:
    print("The result is:", result)
finally:
    print("This will run no matter what.")

# We can achieve the same result without using the finally statement by using simple print() statement outside from try-except block

'''
The finally block is used for scenarios where you need to guarantee that certain actions are performed (like cleaning up resources), regardless of whether an exception occurs. Just placing a print statement after the try-except block doesn't have the same guarantee, especially when an early exit happens (due to return, break, or an unhandled exception).
'''

# For Example, the print() statement will not be executed if return statement is used in the try block.

def divide_numbers(x, y):
    try:
        result = x / y
        return result  # The function returns here, but the finally block will still run
    except ZeroDivisionError:
        print("You cannot divide by zero!")
        return None
    finally:
        print("Cleaning up resources!")  # This will run no matter what

print(divide_numbers(10, 2))  # Output: 5.0
print(divide_numbers(10, 0))  # Output: You cannot divide by zero!


# Catching all exceptions using the "Exception" class

'''
If you are unaware what kind of error might occur, you can catch all execptions using a generic execpt block without specifying a execption type. However, this should be used with caution, as it hides the specific error type.
'''

try:
    result = 10 / 0
except Exception as e:
    print(f"An error occur {e}")


# Raising Execption
# ou can raise execptions using the "raise" keyword. This can be useful for creating custom error messages or for handling errors in a more structured way.

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)    