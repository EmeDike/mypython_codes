
binary_str = input("Enter a binary number: ")
decimal = 0

for digit in binary_str[::-1]:
    if digit == '1':
        decimal += 2**binary_str.index(digit)

print(f"The decimal equivalent of binary {binary_str} is {decimal}")