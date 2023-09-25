import math



def divide_or_square(number):
    if number % 5 == 0:
        return math.sqrt(number)
    else:
        return number % 5


if __name__ == "__main__":
   result = divide_or_square(10)
   print(f"{result:.2f}")
