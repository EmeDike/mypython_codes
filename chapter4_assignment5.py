def celsius_to_fahrenheit(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    return round(fahrenheit, 1)

print("Celsius\tFahrenheit")
print("-------------------")
for celsius in range(101):
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}\t{fahrenheit}")
