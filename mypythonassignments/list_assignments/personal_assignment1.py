# Create a Python list named fruits containing the following items: "apple", "banana", "orange", "grape", and "kiwi".

def create_lists():
    fruits = ["apple", "banana", "orange"]


# Create a Python function named get_third_fruit that takes a list as an argument and returns the third item from the list.

def get_third_fruit(fruits_list):
    return fruits_list[2]


my_fruits = ["apple", "banana", "orange"]
result = get_third_fruit(my_fruits)
print(result)

#Create a Python function named select_fruits that takes a list as an argument and
# returns a new list containing the second to fourth items.

def get_second_and_fouth_number(number_slicing):
    sliced_numbers = number_slicing[1:3]


my_list = [0, 1, 2, 3, 4]
result = get_second_and_fouth_number(my_list)
print(result)