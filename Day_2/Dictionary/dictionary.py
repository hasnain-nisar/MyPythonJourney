# Dictinory is a collection of keys-value pairs.

empty_dict = {} # It cretaes an empty dictionary.

marks = {
    "Hasnain": 100,
    "Ali": 92,
    "Ayesha": 88
}

print(marks, type(marks))
print(marks["Hasnain"])

a = { 
    "key": "value", 
    "hasnain": "code", 
    "marks": "100", 
    "list": [1, 2, 9], 
    0: "has"
} 

print(a["key"])
print(a["list"])
print(a[0])

# Properties of python dictionaries.

# 1. It is unordered.
# 2. It is mutable.
# 3. it is indexed.
# 4. Cannot contain duplicate keys.


# Dictionary methods.

b = {
    "Name": "Hasnain",
    "From": "Pakistan",
    "Age":  23,
    "Marks": [92, 98, 96]
}

# .items(): Returns a list of (key,value)tuples.
print(b.items())

# .keys(): Returns a list containing dictionary's keys. 
print(b.keys())

# .values(): Return a list containing dictionary's values.
print(b.values())

# .update({"friends":}): Updates the dictionary with supplied key-value pairs. 

b.update({"Age": 24, "Martial Status": "Single"})  # Even we can add a new pair in existing dictionary.
print(b)

# .get("name"): Returns the value of the specified keys

print(b.get("Name")) # It returns None if the key is not in dict.

# This is as same as

print(b["Name"]) # It returns error if the specified key is not in dict.

