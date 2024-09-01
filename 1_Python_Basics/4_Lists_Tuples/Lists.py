# Lists and Tuples

# Python lists are containners to store a set of values of any data type.

# list = ["Apple", "hasnain", 23, 2.222, False]
# print(list)
# print(list[0])
# print(list[3])

# # we can change elemnts of list

# # Unlike strings lista re mutable.

# list[0] = "123"
# print(list) 

# # Sliciung in lists

# print(list[1:4]) # Same as strings it will exclude 4.

# l1 = [0,1,2,3,4,5,6,7,8,9]
# print(type(l1))

# l1.sort()
# l1.reverse()
# print(l1)

# l1.append(10)
# print(l1)

# l1.insert(1, 0.5)
# print(l1)

# l1.pop(2) # Will delete element at index 2.
# print(l1) 

# print(l1.pop(2)) # Will delete element at index 2 and print its value.  # Return value of the method

# l1.remove(3)
# print(l1)


# Tuples
# A tuple is an immutable data type in python.

# a = () # empty tuple
# print(type(a))

# b = (1)
# print(type(b)) # Output: <class 'int'>

# # If you want to make a tuple having single elemnt then
# b = (1,) # Use , after the single element.
# print(type(b))

# t1 = (1,33, 42, "hasnain", False, 42, True)
# print(t1)

# t2 = t1.count(33)
# print(t2)

# print(t1.count(42))

# i = t1.index(42)
# print(i) # As there are two 42 in tuple 't1'. But it will return the 2nd index 42 position, and will not look further in

# # Concatination
# T1 = (1, 2, 3, "hasnain")
# T2 = (1, 2, 3, "Nisar")

# con = T1 + T2
# print(con)
# print(len(con))

# # Membership

# # You can check if an item exits in a tuple using the keyword "in" 

# my_tup = (1, 2, 3)
# print(2 in my_tup) # Output: True
# print(4 in my_tup) # Output: False


# # Min/Max functions

# my_tup = (1, 3, 4, 45, 5, 5, 5,3)
# print(min(my_tup))


# # Unpacking

# my_tuple = (1, 2, 3)
# a, b, c = my_tuple
# print(a)
# print(b)
# print(c)

# Practice set
