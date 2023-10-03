import random
def move_tortoise():
    move = random.randint(1, 10)
    if move <= 5:
        return 3
    elif 6 <= move <= 7:
        return -6
    else:
        return 1

def move_hare():
    move = random.randint(1, 10)
    if move <= 2:
        return 0
    elif 3 <= move <= 4:
        return 9
    elif move == 5:
        return -12
    elif 6 <= move <= 8:
        return 1
    else:
        return -2

def display_race(tortoise_pos, hare_pos):
    race_track = [' '] * 70
    race_track[tortoise_pos - 1] = 'T'
    race_track[hare_pos - 1] = 'H'

    for position in race_track:
        print(position, end='')
    print()

tortoise_position = 1
hare_position = 1

print("BANG !!!!!")
print("AND THEY'RE OFF !!!!!")

while True:
    tortoise_position += move_tortoise()
    hare_position += move_hare()

    if tortoise_position < 1:
        tortoise_position = 1
    if hare_position < 1:
        hare_position = 1

    display_race(tortoise_position, hare_position)

    if tortoise_position >= 70 and hare_position >= 70:
        print("It's a tie!")
        break
    elif tortoise_position >= 70:
        print("TORTOISE WINS!!! YAY!!!")
        break
    elif hare_position >= 70:
        print("Hare wins. Yuch.")
        break
