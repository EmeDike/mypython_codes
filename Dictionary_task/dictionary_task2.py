def list_return_dictionary(my_list):
    new_dict = {}

    for fruits in my_list:
        key = fruits[0].lower()
        if key in new_dict:
            key = fruits[0].upper()
        new_dict[key] = fruits

    return new_dict


my_list = ["apple", "banana", "orange", "mango"]
output = list_return_dictionary(my_list)
print(output)
