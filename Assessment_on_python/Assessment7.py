def calculate_even_odd_numbers(numbers):
    even_sum = 0
    odd_sum = 0
    for number in range(0, 10):
        if number % 2 == 0:
            even_sum = even_sum + 1

        elif number % 2 != 0:
            odd_sum = odd_sum + 1

    return even_sum, odd_sum


number = (0, 10)
even_sum, odd_sum = calculate_even_odd_numbers(number)
print(f"Even_sum is: {even_sum}\nOdd_sum is: {odd_sum}")
