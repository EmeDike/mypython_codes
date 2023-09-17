
principal = 1000
annual_rate = 0.07

for i in [10, 20, 30]:
    amount = principal * (1 + annual_rate) ** i
    print(f"Amount after {i} years: ${amount:.2f}")
