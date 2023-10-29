def cal_nested_list_sum(my_list):
    total_sum = 0
    for element in my_list:
        for index in element:
            total_sum = total_sum + index
    return total_sum


my_list = [[2, 4, 5, 6], [2, 3, 5, 6]]
result = cal_nested_list_sum(my_list)
print(result)
