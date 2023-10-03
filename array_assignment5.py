

def even_position_elements(arr):
    length = len(arr) // 2
    result = [arr[i * 2 + 1] for i in range(length)]
    return result