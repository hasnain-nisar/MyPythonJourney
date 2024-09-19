'''
A lambda function in python is small anonymous, inline function defined using lambda keyword, typically used for short, single-expression functions without a name. It is often employed in scenarios requiring short, temoaray functions, such as sorting, filtering, or mapping.
'''

# Basic Syntax
# lambda arguments: expression

# To create a simple lamda function, that adds two numbers, we can use the following code:

add_number = lambda x, y: x + y
# Now, we can call this function and pass two numbers as arguments:
print(add_number(2, 3)) # Output: 5

# OR
# We can also use lambda function to sort a list of numbers in ascending order:

sort_list = lambda lst: sorted(lst) 
# Now, we can call this function and pass a list of numbers as an argument:
print(sort_list([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])) # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# OR

# We can also use lambda function to give square of a number:
square = lambda x: x**2
# Now, we can call this function and pass a number as an argument: 
print(square(5)) # Output: 25

# USing Lambda with Higher-Order Functions

# 1. map()
# map() applies a function to all the items in an input list.

# Example: Squaring all the numbers in a list using map()

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# 2. filter()
# filter() filters element from a list based on a condition.

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers) # Output: [2, 4, 6]

# 3. sorted() with key parameter.
# sorted can take a key parameter, which is a function used to customize sorting. This is often where lambda functions shines.

pairs = [('apple', 3), ('banana', 2), ('cherry', 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs) # Output: [('cherry', 1), ('banana', 2), ('apple', 3),]


# Custom sorting of dictionary based on specific key.
data = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Bob', 'age': 20}]
sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data) # Output: [{'name': 'Bob', 'age': 20}, {'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}]

# 4. Lambda with reduce()
from functools import reduce

nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y : x*y, nums)
print(product) # Output: 120

# 5. Lambda with Conditional Expressions

# Example: Check if a number is even or odd using lambda function

num = 5 
is_even = lambda x: "Even" if x%2 == 0 else "Odd"
print(is_even(num)) # Output: odd

# OR
max_fun = lambda a, b: a if a > b else b
print(max_fun(5, 10)) # Output: 10