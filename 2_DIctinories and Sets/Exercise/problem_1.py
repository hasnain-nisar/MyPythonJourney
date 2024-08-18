# Write a programme to cretae a dictionary of urdu words with values as theor english     # translation. Provide user with an option to look at it.
urdu_to_eng = {
    "kitab": "Book",
    "pani": "Water",
    "dost": "Friend",
    "Zindagi": "Life",
    "Soraj": "Sun"
}

word = input("Enter the wor you want meaning of: ").lower()

if word in urdu_to_eng:
    print(f"The English translation of {word} is: {urdu_to_eng[word]}")
else:
    print(f"Sorry, the word {word} is not in the dictionary.")

