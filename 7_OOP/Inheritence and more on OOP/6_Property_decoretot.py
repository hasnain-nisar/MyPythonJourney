'''
In Python, the property decorator is a built-in decorator that allows you to define methods in a class that can be accessed like attributes.

The property decoretor allows you to define methods for getting, setting and deleting an attribute. These are commanly referred to as getter, setter and deleter methods.
'''

class Employee:
    def __init__(self, name, salary): # Note: Using underscore to indicate a private attribute
        self._name = name
        self._salary = salary

    @property
    def name(self):
        # Getter method for name attribute.
        return self._name
    
    @name.setter
    def name(self, value):
        # Setter method for the name attribute.
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def salary(self):
        # Getter method for tha salary attributr.
        return self._salary
    
    @salary.setter
    def salary(self, value):
        # Setter method for the sallary attribute.
        if value < 0:
            raise ValueError("Salary can't be negative.")
        self._salary = value

    @salary.deleter
    def salary(self):
        # Deleter method for the salary attribute.
        del self._salary

# Create an instane of Employee
emp = Employee("John", 50000)

# Access and modify attributes using property methods
print(emp.name)  # Output: John
print(emp.salary)  # Output: 50000

emp.name = "Alice"  # Using setter method
print(emp.name)  # Output: Alice

try:
    emp.name = ""  # Raises ValueError
except ValueError as e:
    print(e)  # Output: Name cannot be empty

emp.salary = 60000  # Using setter method
print(emp.salary)  # Output: 60000

del emp.salary  # Using deleter method