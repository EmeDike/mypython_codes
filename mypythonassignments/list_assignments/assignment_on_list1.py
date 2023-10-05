def calculate_sum():
    my_list = [15, 20, 25, 20, 10, 5]
    total_sum = 0

    for item in my_list:
        total_sum += item

    return total_sum


result = calculate_sum()
print(result)
