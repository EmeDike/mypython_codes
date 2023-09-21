
current_population = 7.9
growth_rate = 1.05

year = 1
population = current_population
doubling_year = None
quadrupling_year = None

print("Year | Population (billions) | Increase (billions)")
while year <= 100:
    increase = population * (growth_rate - 1)

    population += increase

    print(f"{year:4d} | {population:.2f} | {increase:.2f}")

    if doubling_year is None and population >= (current_population * 2):
        doubling_year = year

    if quadrupling_year is None and population >= (current_population * 4):
        quadrupling_year = year

    year += 1

print(f"\nThe population doubles around year {doubling_year}.")
print(f"The population quadruples around year {quadrupling_year}.")

