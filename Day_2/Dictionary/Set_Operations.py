s = {1, 2, 8, 3}

# len(), the length of the set.
print(len(s))

# .copy() method, it returns a shallow copy of the set.
new_set = s.copy()
print(new_set)

# remove(), remove specific element from the set.
s.remove(1)
print(s)

# .pop(), Removes an arbitrary element from the set and return the # element removed.

print(s.pop())

# .add() method in set.

s.add("Nisar")
print(s)

# .clear()method in set. It removes all elements from the set.

set = {1, 22, 3, "hja"}
set.clear()
print(set)

# Unions and Intersection

s1 = {1, 2, 3, 332}
s2 = {0, 2, 1, 2, 1}

print(s1.union(s2))
print(s1.intersection(s2))

# .issubset() and .issuperset() methods.

s3 = {1, 3}
s4 = {"Hasnain"}

print(s1.issubset(s3)) # False
print(s3.issubset(s1)) #True

print(s1.issuperset(s3)) # True
print(s3.issuperset(s1)) # False

print(s4.issubset(s1)) # False
print({"Hasnain"}.issubset({"Hasnain", "Nisar", 12})) # True

# .difference() method

print(s1)
print(s3)
print(s1.difference(s3))
