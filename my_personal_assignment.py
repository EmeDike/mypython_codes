# Write a Python script to print all the even numbers between 1 and 50.

number = 1
even_sum = 0

while number <= 50:
    if number % 2 == 0:
        even_sum += number
    number += 1

print("Sum of all even numbers is : ", even_sum )