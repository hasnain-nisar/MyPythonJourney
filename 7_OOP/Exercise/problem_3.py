'''
Create a class with a class attribute a; create an object from it and set 'a'
directly using 'object.a = 0'. Does this change the class attribute?
'''

class Myclass:
    a = 10 # Class attribute

# Create an object of Myclass
obj = Myclass()

# Print the class attribute through the object.
print("Before changing: ", obj.a)

# Modify the attribute using object.
obj.a = 0

# Print after changing it using object
print("After changing: ", obj.a)

# Check the class attribute itself.
print("Class Attribuete: ", Myclass.a)


'''
Explanation:
No, modifying an attribute using obj.a = 0 does not change the class attribute. Instead it creates or modifies an
instance attribute for that specific object. The class attribute remains unchanged for the class and other 
instances.

'''