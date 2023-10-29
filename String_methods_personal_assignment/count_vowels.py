def count_vowel(my_list_str):
    vowel = "aeiouAEIOU"
    count = 0
    for element in my_list_str:
        for character in element:
            if character in vowel:
                return True
            else:
                return False


my_list_str = ["rhythm", "banana"]
result = count_vowel(my_list_str)
print(result)
