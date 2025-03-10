"""
Name: N'din Assi 
CIS 216 OBJECT ORIENTED PROGRAMMING 
Guesing Game week 2 
"""
import random

def display_heading():
    """Displays the game heading."""
    print("Guess the number!")

def get_limit():
    """Prompts the user for the upper limit of the guessing range."""
    while True:
        try:
            limit = int(input("Enter the limit: "))
            if limit > 0:
                return limit
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def play_game(limit):
    """Plays the number guessing game."""
    random_number = random.randint(1, limit)
    print(f"I'm thinking of a number from 1 to {limit}")

    tries = 0
    while True:
        try:
            guess = int(input("Your guess: "))
            tries += 1
            if guess < 1 or guess > limit:
                print(f"Please enter a number between 1 and {limit}.")
            elif guess < random_number:
                print("Too low.")
            elif guess > random_number:
                print("Too high.")
            else:
                print(f"You guessed it in {tries} tries.")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    display_heading()

    while True:
        limit = get_limit()
        play_game(limit)

        play_again = input("Would you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Bye!")
            break

if __name__ == "__main__":
    main()