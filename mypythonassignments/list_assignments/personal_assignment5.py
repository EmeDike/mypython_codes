# Create a Python function named add_mango that takes a list as an argument,
# adds "mango" to the end, and returns the updated list.

def append_item(my_list):
    item = "sugar"
    my_list.append(item)
    return my_list


my_list = ["garri", "milk"]
result = append_item(my_list)
print(result)
