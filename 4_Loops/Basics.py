# to print numbers from 1 to 5.
print(1)
print(2)
print(3)
print(4)
print(5)

# Same task can be done using for loop.
for i in range(1, 6):
    print(i)

# There are primarily two types of loops.

# for loop
# while loop

# same problem can be solved using while loop.

i = 1

while i < 6:
    print(i)
    i += 1

# Write a programme to print 1 to 50 using a while loop.

i = 1
while i < 51:
    print(i)
    i += 1

# Write a program to print the content of a list using while loops. 

list = [1, "Hasnain", "Nisar", 0.01, 11212, '112']

i = 0

while i < len(list):
    print(list[i])
    i += 1

# for loops.
# A for loop is used to iterate through a sequence like list, tuples, or strings [iterable]

# Iterations over list and tuples.

l = [1, 7, "Hasnain", 8] # list
for item in l:
    print(item)

t = (1, "Hasnain", 11, "123") # Tuple
for item in t:
    print(item)

s = "hasnain nisar" # String
for item in s:
    print(item)

dict = {'a': 1, 'b': 2, 'c': 3}
for key in dict: # This will print the keys.
    print(key)

'''Output:
        a
        b
        c
'''

# Iterating over values.

for value in dict.values(): # This will print the values.
    print(value) 

'''Output:
        1
        2
        3
'''

# Iterating over key-value pair.

for key, value in dict.items():  # This will print both keys and values.
    print(f"{key}: {value}") 

'''Output:
        a: 1
        b: 2
        c:3
'''