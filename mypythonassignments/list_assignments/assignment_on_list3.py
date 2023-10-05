def largest_number():

    my_list = [15, 20, 25, 20, 10, 5]
    largest_number = my_list[0]

    for number in my_list:
        if number > largest_number:
            largest_number = number

    return largest_number

result = largest_number()
print(result)