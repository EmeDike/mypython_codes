def find_largest_element(arr):
    maximum_number = arr[0]
    for element in arr:
        if element > maximum_number:
            maximum_number = element

    return maximum_number


arr = [1, 2, 3, 4, 5]
result = find_largest_element(arr)
print(result)



