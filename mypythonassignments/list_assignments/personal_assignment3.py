#Create a Python function named replace_third_fruit that takes a list as an argument,
# replaces the third item with "pineapple", and returns the updated list.

def replace_third_element(my_fruits_list):
    my_fruits_list[3] = "pinnapple"
    return my_fruits_list


my_fruits = ["orange", "mango", "apple", "banana"]
result = replace_third_element(my_fruits)
print(result)
