# Multilevel inheritence involves a chain of inheritence where a class inherits from another derived class.

# Base class
class LivingBeing:
    def is_alive(self):
        return f"Is alive."
    
# Intermediate class inherited from LivingBeing.

class Animal(LivingBeing):
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} can walk."
    
# Detived class inheritefd from Animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} barks."
    
# Creating an object of the dog class.
dog = Dog('Max')
print(dog.is_alive())
print(dog.walk())
print(dog.bark())