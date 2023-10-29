#Given a list of names, how can you capitalize the first letter of each name using a string method?

def capitalize_each_letter(string):
    formatted_list = []
    for element in my_list_str:
        capitalized_string = element.capitalize()
        formatted_list.append(capitalized_string)
    return formatted_list

my_list_str = ["apple", "orange", "mango", "beans"]
result = capitalize_each_letter(my_list_str)
print(result)
