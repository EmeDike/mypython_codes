#Write a function that takes a list of numbers and returns a new list with only the even numbers squared.
import math


def square_even_numbers(my_list):

    squared_list = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            math.pow(i, 2)

            squared_list.append(i)
    return squared_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = square_even_numbers(my_list)
print(result)