def find_middle_number(numbers):
    sorted_numbers = sorted(numbers)
    middle_index = len(sorted_numbers) // 2
    middle_number = sorted_numbers[middle_index]
    return middle_number

def main():
    numbers = [10, 20, 15, 25, 5, 30, 35, 20, 10, 20]
    middle_number = find_middle_number(numbers)
    print("The middle number is:", middle_number)

if __name__ == "__main__":
    main()
