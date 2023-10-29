
input_sequence = input("Enter a sequence of comma-separated numbers: ")

numbers_list = input_sequence.split(',')

numbers_list = [int(num) for num in numbers_list]

numbers_tuple = tuple(numbers_list)

print("List:", numbers_list)
print("Tuple:", numbers_tuple)
