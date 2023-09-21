# Loop for the rows (1 to 5)
for row in range(1, 6):
    # Pattern (a)
    for i in range(row):
        print('*', end='')
    print("   ", end='')

    # Pattern (b)
    for i in range(5, 0, -1):
         if i > row:
            print(' ', end='')
        else:
            print('*', end='')
    print("   ", end='')

    # Pattern (c)
    for i in range(5 - row):
        print(' ', end='')
    for i in range(row):
        print('*', end='')
    print("   ", end='')

    # Pattern (d)
    for i in range(row):
        print(' ', end='')
    for i in range(5 - row):
        print('*', end='')
    print()

print()