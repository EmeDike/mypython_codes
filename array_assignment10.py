

def combine_alternate_elements(arr1, arr2):
    length = max(len(arr1), len(arr2)) * 2
    result = [arr1[i] if i < len(arr1) else 0 for i in range(length)]
    result[1::2] = [arr2[i] if i < len(arr2) else 0 for i in range(length // 2)]
    return result