sum = 0

while True:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    user_input = input("Enter 'Quit' to quit: ")

    sum = first_number + second_number

    if user_input.lower() == "quit":
        break
    else:
        print(f"Sum of {first_number} and {second_number} is: {sum}")

# rewrite this code using sentinel loop
