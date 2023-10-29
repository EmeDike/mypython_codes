# Create a Python function named uppercase_fruits that takes a list as an argument
# and returns a new list with the uppercase version of each fruit.

def upper_case_fruits(my_fruits):
    for i in range(len(my_fruits)):
        my_fruits[i] = my_fruits[i].upper()
    return my_fruits


my_list = ["mango", "rice"]
result = upper_case_fruits(my_list)
print(result)
