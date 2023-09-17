

number = 0
count = 0

print(f"{'Number':<10}{'square':<10}{'cube':>7}")

while number <= 5:
    float_square = pow(number, 2)
    cube = float_square * number

    print(f"{number}\t\t\t{float_square}\t\t\t{cube}")
    number += 1
    count += 1


