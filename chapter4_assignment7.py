import random

def get_valid_guess():
    while True:
        guess = input("Guess my number between 1 and 1000 with the fewest guesses: ")
        if guess.isdigit():
            return int(guess)
        else:
            print("Invalid input. Please enter a valid number between 1 and 1000.")

def play_guess_the_number():
    play_again = "yes"

    while play_again == "yes":
        secret_number = random.randint
