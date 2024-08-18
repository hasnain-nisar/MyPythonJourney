# Write a programme to store 7 fruits in a list entered by the users.

FruitList = []

f1 = input("Enter fruit name: ")
FruitList.append(f1)
f2 = input("Enter fruit name: ")
FruitList.append(f2)
f3 = input("Enter fruit name: ")
FruitList.append(f3)
f4 = input("Enter fruit name: ")
FruitList.append(f4)
f5 = input("Enter fruit name: ")
FruitList.append(f5)
f6 = input("Enter fruit name: ")
FruitList.append(f6)
f7 = input("Enter fruit name: ")
FruitList.append(f7)

print(FruitList)

# Another more consice way

FruitList = []

for i in range(7):
    fruit = input(f"Enter the fruit name{i + 1}: ") # Used f string.  
    FruitList.append(fruit) 


print(FruitList)
