def sum_with_for_loop(arr):
    total = sum(arr)
    return total

def sum_with_while_loop(arr):
    total = 0
    i = 0
    while i < len(arr):
        total += arr[i]
        i += 1
    return total

def sum_with_do_while(arr):
    total = 0
    i = 0
    while i < len(arr):
        total += arr[i]
        i += 1
    return total