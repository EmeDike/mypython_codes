def difference_between_max_min(my_list):
    largest_value = max(my_list)
    smallest_value = min(my_list)
    difference = largest_value - smallest_value
    return difference


my_list = [2, 3, 5, 6, 89, 30]
result = difference_between_max_min(my_list)
print(result)
