def calculate_total_product():
    my_list = [15, 20, 25, 20, 10, 5]
    total_product = 1

    for items in my_list:
        total_product *= items

    return total_product

result = calculate_total_product()
print(result)
