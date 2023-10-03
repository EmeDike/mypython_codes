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
        secret_number = random.randint(1, 1000)
        attempts = 0

        print("Welcome to Guess the Number!")

        while True:
            guessed_number = get_valid_guess()
            attempts += 1

            if guessed_number < secret_number:
                print("Too low. Try again.")
            elif guessed_number > secret_number:
                print("Too high. Try again.")
            else:
                print(f"Congratulations. You guessed the number in {attempts} attempts!")
                break

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()

    print("Thanks for playing!")


if __name__ == "__main__":
    play_guess_the_number()
