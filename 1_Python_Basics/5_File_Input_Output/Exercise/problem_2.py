'''
The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file 'Hi-score.txt' which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hi
score whenever the game() function breaks the Hi-score. 
'''

import random

def game():
    # Simulating a game that returns a random score btween 0 and 100.
    return random.randint(0, 100)

def update_hi_score():

    # Read the existing hi-score from the file.
    with open('problem_2.txt', 'r') as file:
        hi_score = file.read().strip()

        # Convert the hi_score to an integer or assume 0 if the file is empty.
        hi_score = int(hi_score) if hi_score else 0

    # Play the game and get the current score.
    current_score = game()
    print(f'Your current score is: {current_score}.')

    # Chech if the current score is higher then the existing Hi-score.
    if current_score > hi_score:
        print(f'New Hi-score!, updating from {current_score} to {hi_score}.')
        
        # Update the Hi-score in the file.
        with open('problem_2.txt', 'w') as file:
            file.write(str(current_score))
    else:
        print(f"No new Hi-score. The current hi-score is still: {hi_score}")


# Run the function to check and update hi-score.
update_hi_score()




