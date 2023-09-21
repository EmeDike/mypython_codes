
e_approximation = 1.0
factorial = 1
num_terms = 10

for i in range(1, num_terms + 1):
    factorial *= i
    e_approximation += 1 / factorial

print(f"Approximation of 'e' using {num_terms} terms: {e_approximation:.10f}")