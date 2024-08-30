import random

# Function to determine the winner.

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    
    # Define the rules of the game
    if (user_choice == 'snake' and computer_choice == 'water') or \
       (user_choice == 'water' and computer_choice == 'gun') or \
       (user_choice == 'gun' and computer_choice == 'snake'):
        return "You win!"
    else:
        return "You Lose!"
    
# Main function to play the game.

def play_game():
    choices = ['snake', 'water', 'gun']

    user_choice = input("Enter your choice (snake, water, gun): ").lower()

    computer_choice = random.choice(choices)

    if user_choice not in choices:
        print("Invalid choice! Please choose from 'snake', 'water' or 'gun'.")

    print(f"You choose {user_choice}")
    print(f"Computer choose {computer_choice}")

    # Determine the winner.
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Run the game

if __name__ == "__main__":
    play_game()
    