# Global Keyword is used to modify the variable that exists at the global scope (outside the current function or scope)

a = 13

def my_func():
    global a
    a = 15
    print(a)

my_func()

# x = 10  # Global variable

# def modify_variable():
#     x = x + 1  # Trying to modify the global variable without using `global`
#     print(x)

# modify_variable() # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value

# Using `global` keyword to modify the global variable
x = 10  # Global variable

def modify_variable():
    global x  # Declare that we are using the global `x`
    x = x + 1  # Modify the global variable
    print(x)

modify_variable()  # Output: 11
print(x)  # Output: 11


# Enumerate function is used to get the index and value of each element in a list

# Without enumerate.

my_list = [1, 2, 3, 4, 5]
index = 0
for item in my_list:
    print(f"Index: {index}", "Value: {item}")
    index += 1

# With enumerate.
my_list = [1, 2, 3, 4, 5]
for index, item in enumerate(my_list):
    print(f"Index: {index}", "Value: {item}")

# Starting index at different level..
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits, start=1):
    print(f"Index: {index}, Fruit: {fruit}")

# Using enumerate with List Comprehensions
fruits = ['apple', 'banana', 'cherry']

indexed_fruits = [(index, fruit) for index, fruit in enumerate(fruits)]
print(indexed_fruits) # Output: [(0, 'apple'), (1, 'banana'), (2, 'cherry')]
# This creates a list of tuples where each tuple contains the index and the corresponding fruit.


# LIst comprehension
# List Comprehension is an elegant way to create lists based on existing lists. 

my_list = [1, 2, 3, 3, 46, 74, 75, 56, 55, 6]
squared_list = []
for item in my_list:
    squared_list.append(item**2)

print(squared_list) # [1, 4, 9, 9, 2116, 5476, 5625, 3136, 3025, 36]

# Using List Comprehension
squared_list_2 = [item*item for item in my_list]
print(squared_list_2)