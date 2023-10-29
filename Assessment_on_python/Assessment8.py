def calculate_first_and_last_colour(colour_list):
    first_colour = colour_list[0]

    last_colour = colour_list[-1]
    return first_colour, last_colour


colour_list = ["red", "green", "white", "black"]
first_colour, last_colour = calculate_first_and_last_colour(colour_list)
print(f"First colour is {first_colour}\nLast_colour is {last_colour}")
