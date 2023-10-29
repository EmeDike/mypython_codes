def repeat_string(input_string, n):

    if not isinstance(n, int) or n < 0:
        return "Please enter a non-negative integer for 'n.'"

    result_string = input_string * n
    return result_string

user_string = input("Enter a string: ")
user_n = input("Enter a non-negative integer (n): ")

if user_n.isdigit():
    user_n = int(user_n)
    result = repeat_string(user_string, user_n)
    print("Result:", result)
else:
    print("Please enter a valid integer for 'n'.")
