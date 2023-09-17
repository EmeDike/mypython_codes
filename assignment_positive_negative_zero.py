total_positive = 0
total_negative = 0
total_zero = 0
range = int(input("Enter Range  "))
count = 1

while count <= range:
    number = int(input("Enter a number: "))

    if number > 0:
        total_positive += 1
    elif number < 0:
        total_negative += 1
    elif number == 0:
        total_zero += 1
    count += 1

print("Total number of positive numbers is", total_positive)
print("Total number of negative numbers is", total_negative)
print("Total number of zero numbers is", total_zero)
