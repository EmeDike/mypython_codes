def check_dominant_elements(my_list):
    dominant_list = []

    for x in range(len(my_list)):  # [0] - [5]
        print(x)
        is_dominant = True
        for y in range(x + 1, len(my_list)):  # [1] - [5]
            if my_list[y] >= my_list[x]:
                is_dominant = False

                break
        if is_dominant:
            dominant_list.append(my_list[x])

    return dominant_list



