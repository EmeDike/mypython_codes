
def reassign_string(my_string, unique_letter):

    first_occurrence_index = my_string.find(unique_letter)

    part1 = my_string[:first_occurrence_index + 1]

    part2 = my_string[first_occurrence_index + 1:]

    part2_modified = part2.replace(unique_letter, "$")

    modified_string = part1 + part2_modified

    return modified_string


given_string = "restart"
unique_letter = "r"
output = reassign_string(given_string, unique_letter)
print(output)
