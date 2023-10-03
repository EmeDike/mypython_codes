import random

def generate_random_question():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    return num1, num2

def main():
    while True:
        num1, num2 = generate_random_question()
        correct_answer = num1 * num2

        while True:
            try:
                user_answer = int(input(f"How much is {num1} times {num2}? "))
                if user_answer == correct_answer:
                    print("Very good!\n")
                    break
                else:
                    print("No. Please try again.\n")
            except ValueError:
                print("Invalid input. Please enter an integer.\n")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
