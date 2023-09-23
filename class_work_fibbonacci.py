number_one = 0;
number_two = 1;
count = 0

while count <= 50:

        print (number_one, end=" ")
        output = number_one + number_two
        number_one = number_two
        number_two = output
        count += 1
        if count == 50:
                break