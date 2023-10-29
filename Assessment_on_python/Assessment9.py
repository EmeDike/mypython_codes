def repeat_string(input_string, n):
    if n >= 0:
        return input_string * n
    else:
        return None

input_str = input("Enter String: ")
input_val = int(input("Enter the value of n: "))

resultant_string = repeat_string(input_str, input_val)

if resultant_string is not None:
    print(resultant_string, end=" \t")
else:
    print("Please enter a non-negative integer for 'n.'")
