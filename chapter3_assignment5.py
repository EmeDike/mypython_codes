
approx_pi = 0
num_terms = 0

desired_values = [3.14, 3.141, 3.1415, 3.14159]
while True:
    current_term = 4 * ((-1) ** num_terms) / (2 * num_terms + 1)

    approx_pi += current_term

    num_terms += 1

    print(f"Approximation using {num_terms} terms: {approx_pi:.10f}")

    for value in desired_values:
        if abs(approx_pi - value) < 0.00001:
            print(f"Reached {value} after {num_terms} terms.")
            desired_values.remove(value)

    if not desired_values:
        break