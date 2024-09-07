'''
OOP in python is a programming paradigm that structure codes using 'objects' which bundles both data(attributes)
and behaviour(methods). 

The core concept of OOP include classes and object, incapsulation, inheritence and polymorphism.

Solving a problem by creating objects is one of the most popular approaches in programming. This concept focuses on 
using reusable code (Don't repeat yourself) DRY principle

'''


# A class is a blueprint for creating object.

class Employee():
    language = "English" # Class attribute. Specific to each class.
    salary = "20000"


Hasnain = Employee() # Object instantation  
Hasnain.name = "Hansain Nisar" # An instance/object attribute
print(Hasnain.name, Hasnain.language, Hasnain.salary)


Ali = Employee()
Ali.name = "Ali"
print(Ali.name, Ali.language, Ali.salary)

# In the above example name is instance attribute and salary and language are class 
# attributes as they directly belong to the class.

'''

Instance attribute take prefrence over class attributes during assignment and retrival.

When looking up for xyz.attribute it checks for the following: 

1) Is attribute present in object?

2) Is attribute present in class? 

'''

Hasnain = Employee()
Hasnain.language = 'Urdu'
print(Hasnain.language, Hasnain.salary)