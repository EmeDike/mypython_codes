def fibonacci_sequence(number):
    number_one = 0
    number_two = 1
    sumz = number_one + number_two

    while number_one < number:
        print(number_one, end=" ")
        sumz = number_one + number_two
        number_one = number_two
        number_two = sumz

fibonacci_sequence(50)
