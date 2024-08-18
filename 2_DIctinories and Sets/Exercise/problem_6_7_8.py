# Create an empty dictionary. Allow 4 friends to add their favourite language as value and use key as their names. Assume that the names are unique.

# dic = {}

# name = input("Enter your name: ")
# lan = input("Enter your language ")
# dic.update({name: lan})

# name = input("Enter your name: ")
# lan = input("Enter your language ")
# dic.update({name: lan})

# name = input("Enter your name: ")
# lan = input("Enter your language ")
# dic.update({name: lan})

# name = input("Enter your name: ")
# lan = input("Enter your language ")
# dic.update({name: lan})

# print(dic)

# More consice method.

dic = {}

for i in range(4):
    name = input(f"Enter the name of friend {i+1}: ")
    lan = input(f"Enter {name}'s favourite programming language: ")
    dic[name] = lan

# Display the final result.

print("\nFavourite language dictionary:")
print(dic)

# If the names of 2 friends are same; what will happen to the program in problem 
# 6? 

# The second entry will overwrite the first one in dictionary.

dic = {}

# Allow 4 friends to add their favorite language
for i in range(4):
    while True:
        name = input(f"Enter the name of friend {i+1}: ")
        if name in dic:
            print(f"The name '{name}' is already used. Please enter a different name.")
        else:
            break
    language = input(f"Enter {name}'s favorite programming language: ")
    dic[name] = language

# Display the final dictionary
print("\nFavorite languages dictionary:")
print(dic)

# If languages of two friends are same; what will happen to the program in problem 
# 6? 


# If two friends list the same favorite language in the program from problem #6, the dictionary will still function correctly, as dictionaries in Python can have multiple keys with the same value.