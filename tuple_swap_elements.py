def swap_first_and_last(selection):
    first, *middle, last = selection
    return last, *middle, first


tuple3 = (15, 25, 60, 50, 30, 40, 45, 55)
result = swap_first_and_last(tuple3)
print(result)
