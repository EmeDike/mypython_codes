def convert_picture_to_string(picture):
    converted_picture = []
    for row in picture:
        converted_row = [' ' if pixel == 0 else '*' for pixel in row]
        converted_picture.append(' '.join(converted_row))
    return converted_picture

def print_picture(picture):
    for row in picture:
        print(row)

def main():
    picture = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0]
    ]

    converted_picture = convert_picture_to_string(picture)
    print_picture(converted_picture)

if __name__ == "__main__":
    main()
