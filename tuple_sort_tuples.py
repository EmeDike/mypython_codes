original_tuples = (('a', 23), ('b', 37), ('c', 11), ('d', 29))

sorted_list = list(original_tuples)
def get_second_element(tuple_item):
    return tuple_item[1]

sorted_list.sort(key=get_second_element)

sorted_tuples = tuple(sorted_list)

print(sorted_tuples)
