'''
A class method is a method that is bound to the class rather than its insatance. It means that the method 
operates on class itself, not on any specific object created from the class
'''

# In Python, class methods are created using the @classmethod decorator and they take cls as the first parameter.

class Employee:
    # Class attribute shared by all instances
    raise_percentage = 0.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    # Instance method
    def apply_raise(self):
        self.salary += self.salary * Employee.raise_percentage

    # Class Method
    @classmethod
    def set_raise_percentage(cls, percentage): # The class method allows you to change the class-level attribute raise_percentage for all current and future instances of the class.
        cls.raise_percentage = percentage


# Create an instance of Employee
emp1 = Employee("John", 50000)

# Apply the raise using instance method.
emp1.apply_raise()
print(emp1.salary) # Output: 52500.0

# Use the class method to raise the percentage.
Employee.set_raise_percentage(0.10)

'''
The set_raise_percentage() class method is called with the argument 0.10, changing the class-level attribute raise_percentage to 0.10 (10%).
This change applies to all current and future instances of the class because it modifies the class attribute, which is shared by all instances.
'''

# Apply thr new raise percentage to another employee
emp2 = Employee("Alice", 50000)
emp2.apply_raise()
print(emp2.salary)


# As we know instance attribute take prefrence over class attribute while execution.

class abc:
    a = 1
    @classmethod
    def show(cls):
        print(f"the class attribute of a is {cls.a}")

    def show_instance(self):
        print(f"The instance attribute of a is {self.a}")

xyz = abc()
xyz.a = 33

# Creates an instance attribute a for the object xyz, which will override the class attribute a when accessed through this instance. If we dont call @classmethod


xyz.show()
xyz.show_instance()