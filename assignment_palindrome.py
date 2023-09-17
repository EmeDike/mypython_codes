
number = input("Enter a five-digit integer: ")

for digit in number:
    print(digit, end="    ")

    if len(number) != 5:
        print("Invalid input. Please enter a five-digit integer.")

