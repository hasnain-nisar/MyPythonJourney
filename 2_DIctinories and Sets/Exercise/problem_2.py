# Write a programme to input 8 numbers from the user and dispaly all the unique numbers (once)

s = set() # Initialize an empty set.

n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))   
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))
n = input("Enter number: ")
s.add(int(n))

print(s)

# More consice way of doing this:

# Initialize an empty list to store the numbers.
numbers = []

# Input 8 numbers from the user.
for i in range(8):
    num = int(input(f"Enter the number {i+1}: "))
    numbers.append(num)

# Convert the list to set to get unique numbers.
unique_num = set(numbers)

# Display the unique numbers
print("Unique numbers are:")
for num in unique_num:
    print(num)