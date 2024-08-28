# Write a python function to remove a given word from a list and strip it at the same 
# time.

def remove(l, word):
    n = []
    for item in l:
        if not item == word:
            n.append(item.strip(word))
    return n

l = ["Hasnain", "Nisar", "ain"]

print(remove(l, "ain"))


# Another example

def remove_and_strip(word_list, word_to_remove):
    # Create a new list with the word removed and elements stripped of whitespace
    return [word.strip() for word in word_list if word.strip() != word_to_remove]

# Example usage
words = ["  apple ", "banana", " orange", "apple  ", "  grape"]
word_to_remove = "apple"

# Remove "apple" and strip the remaining words
cleaned_words = remove_and_strip(words, word_to_remove)

print(cleaned_words)