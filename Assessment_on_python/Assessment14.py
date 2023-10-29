#write a python  program that will accept the base and height of a triangle and compute its area

def calculate_area_of_a_triangle(base, height):

    area = 0.5 * base * height
    return area

base = int(input("Enter base value "))
height = int(input("Enter height "))
result = calculate_area_of_a_triangle(base, height)

print(result)
