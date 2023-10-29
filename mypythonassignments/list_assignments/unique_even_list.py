def calculate_even(my_list):
    even_list = []
    unique_list = []
    for element in my_list:

        if element % 2 == 0:
            even_list.append(element)
    for item in even_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


my_list = [1, 3, 2, 5, 3, 4, 6, 4, 6, 9, 8, 2, 10, 8, 6, 12, 15, 10, 4, 6, 14]
result = calculate_even(my_list)
print(result)
