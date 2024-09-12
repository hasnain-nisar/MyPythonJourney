'''
We are going to write a program that generates a random number and asks the user to 
guess it. 
If the player's guess is higher than the actual number, the program displays “Lower 
number please”. Similarly, if the user’s guess is too low, the program prints “higher 
number please” When the user guesses the correct number, the program displays the 
number of guesses the player used to arrive at the number.
'''

import random

def guess_the_number():
    number = random.randint(1, 100)
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    while True:
        try:
            guess = int(input("Guess the number: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number {number} correctly!, in {guess} guesses.")
            break

if __name__ == "__main__":
    guess_the_number()


'''
The code implicitly tracks the number of guesses by the number of iterations of the while True loop. Each iteration represents one guess by the user. The continue statement is used to handle invalid inputs and prompt the user again, while the break statement is used to exit the loop when the user guesses the correct number.
'''
