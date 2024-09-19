'''
The warlus operator := allows you to assign value to variables as part of the expression. It helps reduce redundancy and improve readability.
'''

# Without warlus operator
data = [1, 22, 32, 425]
filtered_data = []
for value in data:
    if len(str(value)) > 1:
        filtered_data.append(value)

print(filtered_data)

# With the warlus operator.
filtered_data = [value for value in data if (n := len(str(value))) > 1]

print(filtered_data)

# Another example.
# Without walus operator.
data = [1, 2, 3, 34, 5, 33]
n = len(data) # First assigning the value to n.
if n > 1: # Checking if n is greater than 1.
    print(f'List contains more than 1 element, list has {n} elemets.')


# With warlus operator.
if (n := len(data)) > 1:
    print(f'List contains more than 1 element, list has {n} elemets.')