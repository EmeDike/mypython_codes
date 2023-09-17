even_sum = 0
odd_sum = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:

    if number % 2 == 0:
        even_sum += 1

    else:
        odd_sum += 1

print(f"Number of even numbers: {even_sum}\nNumber of odd numbers: {odd_sum}")


