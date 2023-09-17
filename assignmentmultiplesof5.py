# multiples of 5
count = 1
maximum_number = int(input("enter maximum_number " ))
multiple_str = " "

while maximum_number >= 5:
    if maximum_number % 5 == 0:
        multiple_str += str(maximum_number) + " "

    maximum_number -= 1
    count += 1

print(multiple_str )
