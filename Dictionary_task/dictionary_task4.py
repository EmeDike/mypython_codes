def two_list_to_dictionary(first_list, second_list):
    new_dict = {}

    for i in range(len(first_list)):
        key = first_list[i]
        value = second_list[i]
        new_dict[key] = value

    return new_dict

first_list = ["a", "b", "c", "d", "e"]
second_list = [1, 2, 3, 4, 5]
result = two_list_to_dictionary(first_list, second_list)
print(result)
