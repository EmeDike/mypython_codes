
total_positive = 0
total_negative = 0
total_zero = 0

while True:
    user_input = input("Enter a number or 00 to stop: ")

    if user_input == '00':
        break

    number = int(user_input)

    if number < 0:
        total_negative += 1

    elif number > 0:
        total_positive += 1

    elif number == 0:
        total_zero += 1

    elif number == "00":
        break


print("Total number of positive numbers: ", total_positive)
print("Total number of negative numbers: ", total_negative)
print("Total number of zeros: ", total_zero)

if total_positive == 0:
    print("No positive numbers were entered.")
if total_negative == 0:
    print("No negative numbers were entered.")
if total_zero == 0:
    print("No zero values were entered.")
