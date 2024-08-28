'''
A function with argument is a function that takes inputs called (arguments or parameters) and perform an action using thoes inputs.
'''

def greet(name):
    '''This function greet the person whoes name is passed as an argument.'''
    print(f"Hello, {name}!")

# Calling the function.

greet("Hasnain")
greet("Nisar")

# Another example with return statement.

def greeting(Name):
    gr = 'Hello ' + Name
    return gr

a = greeting('Hasnain') # a will now contain Hello Hasnain
print(a)

# Default parameter value:

# We can have some value as default argument in a function.

def goodday(name, ending = "Thankyou"):
    print(f'Good Day, {name}')
    print(ending) 

goodday("Hasnain")  # This will print Good Day, Hasnain and Thankyou in next line.
goodday('Hasnain', 'Thanks') # Now it will take 'Thanks" argument, instead of default