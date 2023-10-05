


def calculate_smallest_number():
    my_list = [15, 20, 25, 20, 10, 5]
    smallest_number = my_list[0]

    for number in my_list:
        if number < smallest_number:
            smallest_number = number

    return smallest_number


result = calculate_smallest_number()
print(result)
