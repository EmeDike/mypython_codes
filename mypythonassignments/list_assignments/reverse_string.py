def reverse_string(input_str):
    words = input_str.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return reversed_words

input_str = "we outside"
output = reverse_string(input_str)
print(output)
