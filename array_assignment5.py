def even_position_elements(arr):

    even_position = []

    for element in arr[2:6:2]:
        even_position.append(element)
    return even_position


my_list = [1, 2, 3, 4, 5, 6, 7]
result = even_position_elements(my_list)
print(result)
