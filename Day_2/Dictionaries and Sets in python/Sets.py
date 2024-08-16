# Set is a collection of non-repetive elements.

# For empty set.
empty_set = set()
print(type(empty_set))

s = {1, 2, 2, 2, 3, 3, 3, 4, 4, 55, 5, 6, 4, "Hasnain"}
print(s) # Output: {1, 2, 3, 4, 5, 6, 55}

# Properties of set

# 1. Sets are unordered => Element’s order doesn’t matter 
# 2. Sets are unindexed => Cannot access elements by index 
# 3. There is no way to change items in sets. 
# 4. Sets cannot contain duplicate values. 