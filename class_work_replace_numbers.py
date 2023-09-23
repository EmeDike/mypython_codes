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

# Replace 0s with ' ' and 1s with '*'
for row in picture:
    for i in range(len(row)):
        if row[i] == 0:
            row[i] = ' '
        else:
            row[i] = '*'

# Printing the modified picture
for row in picture:
    print(' '.join(map(str, row)))