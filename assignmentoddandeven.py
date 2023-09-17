number = 1
even_sum = 0
odd_sum = 0
count = 0

while number <= 9:

    if number % 2 == 0:
        even_sum += 1
    elif number % 2 != 0:
        odd_sum += 1

    number += 1

print("Number of even numbers :", even_sum)
print("Number of odd numbers :", odd_sum)
