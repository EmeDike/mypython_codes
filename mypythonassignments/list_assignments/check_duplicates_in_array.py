def check_duplicate(my_list):
    unique_list = []
    check_duplicate = []

    for element in my_list:
        if element in unique_list:
            check_duplicate.append(element)
        else:
            unique_list.append(element)

    result = sorted(check_duplicate)
    return result


my_list = [1, 2, 3, 3, 2, 4, 5, 6]
output = check_duplicate(my_list)
print(output)
