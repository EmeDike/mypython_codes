
age = int(input("Enter your age: "))

max_heart_rate = 220 - age

min_target_rate = 0.5 * max_heart_rate
max_target_rate = 0.85 * max_heart_rate

print(f"Your maximum heart rate is: {max_heart_rate} beats per minute.")
print(f"Your target heart rate range is: {min_target_rate} - {max_target_rate} beats per minute.")
