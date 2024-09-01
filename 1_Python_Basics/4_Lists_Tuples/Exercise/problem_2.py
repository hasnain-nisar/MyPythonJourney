# Write a program to accept marks om 6 students and display them in a sorted 
# manner. 

Marks = []

m1 = int(input("Enter marks here: "))
Marks.append(m1)
m2 = int(input("Enter marks here: "))
Marks.append(m2)
m3 = int(input("Enter marks here: "))
Marks.append(m3)
m4 = int(input("Enter marks here: "))
Marks.append(m4)
m5 = int(input("Enter marks here: "))
Marks.append(m5)
m6 = int(input("Enter marks here: "))
Marks.append(m6)

# Marks = Marks.sort() 
# print(Marks) 

# OR

# print(Marks.sort())

# These two methods above will encounter an issue where the output was None. This happens because the sort() method in Python doesn't return the sorted list. Instead, it sorts the list in place and returns None.

# The correct method is

Marks.sort()
print(Marks)