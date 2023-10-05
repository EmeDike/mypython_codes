def remove_duplicates():
    my_list = [15, 20, 25, 20, 10, 5]
    unique_list = []

    for element in my_list:
        if element not in unique_list:
            unique_list.append(element)

    return unique_list


result = remove_duplicates()
print(result)
