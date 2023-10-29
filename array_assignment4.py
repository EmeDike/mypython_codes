def odd_position_elements(arr):
    odd_elements = []
    for elements in my_array[1:6:2]:

        odd_elements.append(elements)
    return odd_elements


my_array = [1, 2, 3, 4, 5, 6, 7]
result = odd_position_elements(my_array)
print(result)
