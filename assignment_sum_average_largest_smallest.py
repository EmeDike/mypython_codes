
first_number = int(input("ENTER FIRST NUMBER  "))
largest_number = first_number
smallest_number = first_number

while True:
    second_number = int(input("ENTER SECOND NUMBER  "))
    third_number = int(input("ENTER THIRD NUMBER  "))

    user_input = input("ENTER EXIT TO EXIT  ")

    sum = first_number + second_number + third_number
    average = sum / 3
    product = first_number * second_number * third_number

    largest_number = max(largest_number, second_number, third_number)
    smallest_number = min(smallest_number, second_number, third_number)

    print("Sum of the three integers is:", sum)
    print("Average of the three integers is:", average)
    print("product of the three integers is:", product)
    print("The largest number is:", largest_number)
    print("The smallest number is:", smallest_number)
