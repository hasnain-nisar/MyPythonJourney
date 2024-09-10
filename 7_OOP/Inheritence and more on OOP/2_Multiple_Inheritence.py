# Multiple Inheritence

# Multiple inheritence involves a child class inheriting from more than one parent class.

# Parent class 1
class Mammal:
    def __init__(self, name):
        self.name = name

    def characteristic(self):
        return f"{self.name} is warm-blooded."
    
# Parent class 2
class AquaticAnimal:
    def can_swim(self):
        return f"Can swim in water."
    

# Child class inheriting from both Mammal and AquaticAnimal
class Dolphin(Mammal, AquaticAnimal):
    def speak(self):
        return f"{self.name} clicks."
    
# Creating an object of the dolphin class.

dolphin = Dolphin("Flipper")
print(dolphin.characteristic())
print(dolphin.can_swim())
print(dolphin.speak())