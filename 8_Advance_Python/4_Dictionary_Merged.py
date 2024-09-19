# Method 1: Merging using | pipe method.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5, 'e': 6}

merged_dict = dict1 | dict2
print(merged_dict) # Output {'a': 1, 'b': 4, 'c': 3, 'd': 5, 'e': 6}

# The values from dict2 overwrite any duplicate keys from dict1

# Method 2: Using the update() Method
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5, 'e': 6}

dict1.update(dict2)
print(dict1) # Output {'a': 1, 'b': 4, 'c': 3, 'd': 5, 'e': 6}

# This modifies dict1 by adding or updating the entries from dict2

# Method 3: Using Dictionary Unpacking (**)
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5, 'e': 6}
merged_dict = {**dict1, **dict2}
print(merged_dict) # Output {'a': 1, 'b': 4, 'c': 3, 'd': 5, 'e': 6}

# Method 4: Merging Multiple Dictionaries with |= (Python 3.9+)
dict1 = {"a": 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1 |= dict2
print(dict1) # Output {'a': 1, 'b': 3, 'c': 4}

# This updates dict1 with the contents of dict2