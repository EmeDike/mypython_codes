number = int(input("Enter Number: "))
factorial = 1

while number > 0:
    factorial = factorial * number
    number -= 1
    print(number)
print("Factorial:", factorial)

# this factorial is not working
