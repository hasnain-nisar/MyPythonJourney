# The supere() function in OOP is used to call methods from a super class (parent class) in a subclass (child class).

class Employee:
    def __init__(self):
        print("Constructor of Employee.")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer.")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager.")
    c = 3


obj = Manager()
print(obj.a, obj.b, obj.c)
print()
print(obj.a, obj.b)


