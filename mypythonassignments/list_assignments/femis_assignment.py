def is_target_between_indices(input1, target, index1, index2):
    number_str = str(input1)

    for i in range(index1, index2 + 1):
        sub_number = int(number_str[i])
        if target == sub_number:
            return True
    return False

input1 = 13579
target = 4
index1 = 1
index2 = 2

result = is_target_between_indices(input1, target, index1, index2)
print(result)
