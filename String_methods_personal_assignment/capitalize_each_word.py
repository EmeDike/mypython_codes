
def capitalize_each_word(my_list):

    capitalized_str = []

    for element in my_list:
        formatted_list = element.upper()
        capitalized_str.append(formatted_list)

    return capitalized_str

my_list = ["apple", "orange", "mango", "beans"]
result = capitalize_each_word(my_list)
print(result)