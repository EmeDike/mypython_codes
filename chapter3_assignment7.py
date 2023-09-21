factorial = 1
num_terms = 10
e_approximation = 0
for n in range(1, num_terms + 1):
    largest1 = float('-inf')
    largest2 = float('-inf')

for i in range(10):
    number = float(input(f"Enter number {i + 1}: "))

    if number > largest1:
        largest2 = largest1
        largest1 = number
    elif number > largest2 and number != largest1:
        largest2 = number

print(f"The largest value is: {largest1}")
print(f"The second largest value is: {largest2}")

factorial *= n
e_approximation += 1 / factorial

print(f"Approximation of 'e' using {num_terms} terms: {e_approximation:.10f}")
