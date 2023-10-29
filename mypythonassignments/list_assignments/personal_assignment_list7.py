#Create a Python function named sort_fruits that takes a list as an argument,
# sorts it in alphabetical order, and returns the result.

def sort_fruits(my_list):
    my_list.sort()
    return my_list

my_list = ["garri", "maize", "orange", "banana"]
result = sort_fruits(my_list)
print(result)