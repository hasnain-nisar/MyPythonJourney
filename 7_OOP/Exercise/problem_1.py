# Create a class “Programmer” for storing information of few programmers 
# working at Microsoft. 

class Programmer:
    # Class attribute fo rthe company's name.
    company = "Microsoft"


    # Constructor to initialize individual attributes for each programmer.
    def __init__(self, name, age, salary, origin):
        self.name = name
        self.age = age
        self.salary = salary
        self.origin = origin

    
    # Method to display programmer details.
    def show_details(self):
        print(f"Programmer Name: {self.name}")
        print(f"Programmer Age: {self.age}")
        print(f"Programmer Salary: {self.salary}")
        print(f"Programmer origin: {self.origin}")

# Creating instance of the programmer class

programmer_1 = Programmer('Hasnain', 23, 123344432, 'Pakistan')
programmer_2 = Programmer('Ali', 25, 12121212, 'Pakistan')

programmer_1.show_details()
print()
programmer_2.show_details()