'''
Write a program to read the text from a given file 'poems.txt'and find out 
whether it contains the word 'twinkle'.
'''

# Function to check if the word "twinkle" is in the file and count its occurence.

def find_twinkle(filename):
    try:
        with open(filename, 'r') as file:
            # Read the content of the file
            content = file.read()

            # Convert the content to lower case to make the search case-insensitive.
            content_lower = content.lower()

            # Count the occurence of the word 'twinkle'
            twinkle_count = content_lower.count('twinkle')

            if twinkle_count > 0:
                print(f"The word 'twinkle' is present in the file {twinkle_count} time(s).")
            else:
                print("The word 'twinkle' is not present in the file.")

    except FileNotFoundError:
        print(f"The file {filename} does not exist.")


# Specify the filename.

filename = 'problem_1.txt'
find_twinkle(filename)
