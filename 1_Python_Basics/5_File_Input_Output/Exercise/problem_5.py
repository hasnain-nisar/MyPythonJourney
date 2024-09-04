# Repeat program 4 for a list of such words to be censored. 

words = ['donkey', 'cat', 'dog']  # List of words to be censored

with open("problem_5.txt", 'r') as file:
    content = file.read().lower()


for word in words:
    content = content.replace(word, "#" * len(word))

with open('problem_5.txt', 'w') as file:
    file.write(content)
