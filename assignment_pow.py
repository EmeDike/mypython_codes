

number = 1
count = 2

print(f"{'Number':<10}{'Count':<10}{'Float Square':<15}")

while number <= 5:
    float_square = pow(number, count)
    number += 1
    count += 1

    print(f"{number:<10}{count:<10}{float_square:<15}")
