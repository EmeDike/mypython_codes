number = input("Enter a five-digit integer: ")

if number.isdigit() and len(number) == 5:
    print("Digits in the integer:")
    for digit in number:
        print(digit, end=" ")
    print()
else:
    print("Please enter a valid five-digit integer.")
