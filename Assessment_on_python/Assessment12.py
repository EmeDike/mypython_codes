def concatenate_list_elements(my_list):

    resultant_string = ''.join(map(str, my_list))
    return resultant_string

my_list = ['Hello', ' ', 'World', '!']
result = concatenate_list_elements(my_list)
print(result)
