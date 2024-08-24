# range() function.

# The range function in python is used to generate a sequence of characters.

# We can aslo specify the start,stop and step size.

# range(start, stop, step_size)

for i in range(1, 50, 10):
    print(i)


for i in range(1, 50): # If step size is not specified it will take step sie as 1.
    print(i)


for i in range(5): # If start is not specified it will start from 0, with step size of 1.
    print(i)

''' Output:
         0
         1
         2
         3
         4
'''


# For loop with else.

# An optional else can be used with a for loop. The else block will execute after the for loop finishes iterating over all items.

num = [1, 2, 3, 4, 5, 6]

for number in num:
    print(number)

else:
    print('Loop completed without break.')

# For loop with else and break.

list = [1, 2, 3, 4, 5, 6, 7]

for item in list:
    if item == 5:
        print("Break at number 5")
        break
    print(item)

else:
    print("Loop completed without break")