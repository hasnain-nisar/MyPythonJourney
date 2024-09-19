def greet():
    print("Hello from greet.")

def another_greet():
    print("Hello from another_greet.")

# This code will run whether the module is executed directly or imported
another_greet()

if __name__ == "__main__":
    # This code will only run if the module is executed directly
    print("This is the main program.")
    greet()

# This will print the value of __name__, which is either "__main__" or the module name
print(__name__)
