# Can you change the values inside a list which is contained in set S?

s = {8, 7, 12, "Harry", [1,2]} 
print(s)

# TypeError: unhashable type: 'list'

# 1. Sets must contain immutable elements. Sets in Python can only contain immutable (hashable) elements. This means that the elements inside a set must be of a type that is immutable, like integers, floats, strings, and tuples.

# 2. Lists Are Mutable: Lists are mutable, meaning their content can be changed after creation. Because of this, lists are not hashable and cannot be used as elements of a set.