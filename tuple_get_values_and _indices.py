def get_values_and_indices(input_tuple):
    result_list = []

    for index, element in enumerate(input_tuple):
        if isinstance(element, (list, tuple)):
            if 20 in element:
                result_list.append((index, 20))
            if 25 in element:
                result_list.append((index, 25))
    return result_list


input_tuple = ("Orange", [10, 20, 30], (5, 15, 25))

result = get_values_and_indices(input_tuple)
print(result)
