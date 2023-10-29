def is_vowel(vowels, user_input):
    if len(user_input) == 1 and user_input.isalpha():
        if user_input.lower() in vowels:
            return "yes"
        else:
            return "no"
    else:
        return "NO"


vowels = "aeiouAEIOU"
user_input = input("Enter character for check ")
result = is_vowel(vowels, user_input)
print(result)

