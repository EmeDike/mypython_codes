import math

def triple_element_function(numbers):
    new_list = []
    for number in numbers:
        result = int(math.pow(number, 3))
        new_list.append(result)
    print(new_list)
    return new_list
