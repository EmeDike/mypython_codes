is_natural = True
range_value = 11
sum_value = 0
number = 1

while number < 11:

    if number <= 0:
        is_natural = False
        print("number is not a natural number")
        break
    else:
        sum_value += number
        number += 1

print("sum of first natural numbers is equal to", sum_value)
