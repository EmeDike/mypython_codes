def get_values_indices(input_tuple):
    result_list = []

    for index, element in enumerate(input_tuple):
        if isinstance(element, (list, tuple)):
            if 20 in element:
                result_list.append((index-1, 20))
            if 25 in element:
                result_list.append((index-1, 25))
    return result_list
