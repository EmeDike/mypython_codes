import random

while True:
    number = int(input("Enter a number between 1 and 10: "))

    if 1 <= number <= 10:
        print(f"Valid number: {number}")
        break
    else:
        print("Number is invalid. Please try again.")

count = 1
while count < 11:
    generated_number = random.randint(1, 10)
    print(f"Generated number {count}: {generated_number}")
    count += 1
