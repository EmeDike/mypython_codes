

def running_total(arr):
    length = len(arr)
    result = [sum(arr[:i + 1]) for i in range(length)]
    return result