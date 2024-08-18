# What will be the length of following set s: 

s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(s)
print(len(s))

# Output: 
# {'20', 20}
# 2


# 2o is an integer, and 20.0 is a floating-point number.
# When comparing an integer with a floating-point number, Python automatically converts   # the integer to a float for the comparison.