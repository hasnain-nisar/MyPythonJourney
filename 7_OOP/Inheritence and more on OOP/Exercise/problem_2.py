'''
Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from 
'Pets'. Add a method 'bark' to class 'Dog'.
'''

class Animal:
    def __init__(self, name):
        self.name = name

    # Method to display animals name.
    def display(self):
        print(f'Animal: {self.name}')

# Derived class pets from animals.
class Pets(Animal):
    def __init__(self, name):
        super().__init__(name)  # Inherit the name from Animals

# Further derived class 'Dog' from 'Pets'
class Dog(Pets):
    def __init__(self, name):
        super().__init__(name) # Inherit the name from Pets

    # Method specific to dog class
    def bark(self):
        print(f"{self.name} is barking: woof! woof!")


# Create an object of the Dog class
buddy = Dog('buddy')
buddy.display()
buddy.bark() 
