

def reverse_list(arr):
    length = len(arr)
    reversed_arr = [arr[length - 1 - i] for i in range(length)]
    return reversed_arr