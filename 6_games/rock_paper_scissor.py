import random

# Funtion to determine the winner

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    # Define the rules of the game.
    if (user_choice == 'rock' and computer_choice == 'scissor') or \
        (user_choice == 'paper' and computer_choice == 'rock') or \
        (user_choice == 'scissor' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You Lose!"

# Define the function to run the programme.

def play_game():
    choices = ["rock", "paper", "scissor"]

    # Take user input
    user_choice = input("Enter your choice ('rock', 'paper', 'scissor'): ").lower()

    computer_choice = random.choice(choices)

    print(f"you choose {user_choice}")
    print(f"Computer choose {computer_choice}")

    if user_choice not in choices:
        print("Invalid choice! Please choose either 'rock', 'paper', or 'scissors'.")

    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    print(result)


# Run the game

if __name__ == "__main__":
    play_game()