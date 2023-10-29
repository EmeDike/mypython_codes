def combine_alternate_elements(arr1, arr2):
    length = max(len(arr1), len(arr2)) * 2
    result = []

    for i in range(length):
        if i < len(arr1):
            result.append(arr1[i])
        else:
            result.append(0)

    for i in range(1, length, 2):
        if i // 2 < len(arr2):
            result[i] = arr2[i // 2]
        else:
            result[i] = 0

    return result
