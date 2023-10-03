import random

def generate_random_question(difficulty_level):
    if difficulty_level == 1:
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
    elif difficulty_level == 2:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
    return num1, num2

def get_user_answer():
    while True:
        user_input = input(f"How much is {num1} times {num2}? ")
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter an integer.\n")

correct_responses = ['Very good!', 'Nice work!', 'Keep up the good work!']
incorrect_responses = ['No. Please try again.', 'Wrong. Try once more.', 'No. Keep trying.']

while True:
        difficulty_level = int(input("Select a difficulty level (1 or 2): "))
        if difficulty_level not in (1, 2):
            print("Invalid difficulty level. Please choose 1 or 2.")
            continue

        num1, num2 = generate_random_question(difficulty_level)
        correct_answer = num1 * num2

        user_answer = get_user_answer()

        if user_answer == correct_answer:
            print(random.choice(correct_responses) + '\n')
        else:
            print(random.choice(incorrect_responses) + '\n')

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break