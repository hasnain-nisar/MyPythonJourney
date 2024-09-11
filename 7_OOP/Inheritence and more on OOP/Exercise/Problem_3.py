# Create a class ‘Employee’ and add salary and increment properties to it.

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         self.increment = 0 # Default increment is 0

#     # Increment Method
#     def set_increment(self, increment_percentage):
#         self.increment = increment_percentage

#     # Method to calculate and apply the increment to the salary
#     def apply_increment(self):
#         new_salary = self.salary + (self.salary * self.increment / 100)
#         self.salary = new_salary
#         print(f'New salary of {self.name} after increment of {self.increment} is {self.salary}')

#     # Method to display employee details
#     def display(self):
#         print(f"Employee: {self.name}, Salary: {self.salary}, Increment: {self.increment}%")


# emp = Employee("Alice", 50000)
# emp.display()


# emp.set_increment(5)
# emp.apply_increment()
# emp.display()

'''
Create a class 'Employee' and add salary and increment properties to it. 
Write a method 'salaryAfterIncrement' method with a @property decorator with a setter 
which changes the value of increment based on the salary. 
'''


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self._increment = 0  # Default increment is 0

    # Property to get the current increment
    @property
    def increment(self):
        return self._increment
    
    # Property setter to change the increment percentage
    @increment.setter
    def increment(self, value):
        self._increment = value

    # Property to calculate the salary after applying the increment
    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self._increment / 100)
    
    # Property setter to adjust the increment based on the updated salary
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        # Calculate the new increment based on the new salary
        self._increment = ((new_salary - self.salary) / self.salary) * 100

    # Method to display employee details
    def display(self):
        print(f"Employee: {self.name}, Salary: {self.salary}, Increment: {self._increment}%")
        print(f"Salary after increment: {self.salaryAfterIncrement}")


# Example usage
emp = Employee("Alice", 50000)

# Display initial details
emp.display()  # Output: Employee: Alice, Salary: 50000, Increment: 0%, Salary after increment: 50000

# Set an increment of 10% using the setter
emp.increment = 10

# Display updated details
emp.display()  # Output: Employee: Alice, Salary: 50000, Increment: 10%, Salary after increment: 55000

# Set the salaryAfterIncrement directly, which adjusts the increment
emp.salaryAfterIncrement = 60000

# Display updated details
emp.display()  # Output: Employee: Alice, Salary: 50000, Increment: 20.0%, Salary after increment: 60000

