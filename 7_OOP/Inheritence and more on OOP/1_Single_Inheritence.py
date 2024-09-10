'''
Inheritence in OPP allows a class to inherit attributes and method from another class. It promets code reusibility,
allowing us to define a class that inherits the functionality of another, reducing redundancy and creating
a hirearchy.

In python inheritence allows us to create a new class (child class) that can use methods and properties of an 
existing class (parent class) with the option to override and add new functionality.
'''

# Single Inheritence

# Single inheritence is when a class inherits from one parent class.

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def Speak(self):
        return f"{self.name} makes a sound."
    
# Child class inherited from parent.
class Dog(Animal):
    def speak(self):
        return f"{self.name} Barks."
    
# Object of Dog class.

dog = Dog("Buddy")
print(dog.speak())
print(dog.Speak())