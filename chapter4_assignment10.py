def product(*args):
    result = 1
    for num in args:
        result *= num
    return result


result1 = product(2, 3, 4)
result2 = product(5, 6)
result3 = product(1, 2, 3, 4, 5)

print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)
