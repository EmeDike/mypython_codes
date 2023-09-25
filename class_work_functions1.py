def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

def main():
    ls = (10, 20, 15, 25, 5, 30, 35, 20, 10, 20)
    average = calculate_average(ls)
    print(f"Average: {average}")

if __name__ == "__main__":
    main()
