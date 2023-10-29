def biggest_odd_number(numbers_str):
    odd_number = []
    for number in numbers_str:
        if int(number) % 2 != 0:
            odd_number.append(int(number))

    if odd_number:
        return max(odd_number)
    else:
        return None


numbers_str = [1, 2, 3, 4, 5, 6]
result = biggest_odd_number(numbers_str)
print(result)
