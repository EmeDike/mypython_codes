def calculate_Area(numbers):

    pi = 3.41

    rounded_area = 2 * pi * radius
    return rounded_area

radius = float(input("Enter the Radius  "))
result = calculate_Area(radius)
print(f"The area of the circle is {result:.2f}")
