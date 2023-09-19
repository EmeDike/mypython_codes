
sum = 0
average = 0
for number in range (1, 52):
    if number % 2 == 0:
        print(f"{number}", end= "\t\t")
        sum = sum + number
        average = sum / 25
print()
print(f"Sum is: {sum}")
print (f"Average is: {average}")
