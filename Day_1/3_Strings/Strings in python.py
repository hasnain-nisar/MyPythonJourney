# String in pthon is a datatype.
# String is seq of characters enclposed in quotes.


name = "Hasnain"
print(len(name))

# Slicing in strings.

nameshort = name[0:3] # Start from index 0 all the way till 3 (excluding 3)
print(nameshort)

print(name[-7:-4])

print(name[:4]) # This means 0 to 4 (excluding 4), is same as print(name[0:4])
print(name[1:]) # This means 1 to len(name) i.e. 7, is same as print(name[1:7])
print(name[1:6])

# Slicing with skip values

name = "0123456789"

print(name[0: 8: 2]) # It will print 0246
print(name[1: 9: 3]) # It will print 147

Strings Functions

str = "Hasnain"

# 1. Length Function

print(len(str)) # dispaly the length of the string.

# 2. String.endswith function.

print(str.endswith("ain")) # output: True

# This function_ tells whether the variable string ends with 
# the string "rry" or not.

# 3. string.count('n') function. 

print(str.count("n")) # This function counts the total number of occurence of any chracter.


