def strip(string):
    stripped_string = list(filter(None, map(str.strip, string)))
    return stripped_string


my_string = ("goat", "", "apple", "", "mango")
result = strip(my_string)
print(result)
