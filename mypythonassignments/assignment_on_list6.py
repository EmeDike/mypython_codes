def sort_list():
    my_list = ["A", "M", "C", "W", "I", "T"]
    first_list = my_list[0:5:3]
    second_list = my_list[1:6:3]
    third_list = my_list[2:5:2]
    result = first_list + second_list + third_list
    return result


print(sort_list())
