# number = 1
# count = 0
#
# print(f"{'Number':<10}{'square':<10}{'cube':>7}")
#
# while number <=11:
#     float_square = pow(number, 2)
#     cube = float_square * number
#
#     print(f"{number}\t\t\t{float_square}\t\t\t{cube}")
#     number += 1
#     count += 1

number = 1
print (f"{'Number':<10}{'square':<10}{'cube':>7}")
for number in range(1, 10):
    float_square = pow(number, 2)
    cube = float_square * number

    print(f"{number: <10}{float_square: <10}{cube: >5}")


