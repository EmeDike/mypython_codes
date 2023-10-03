def round_to_nearest_integer(value):
    return round(value)

def round_to_nearest_tenth(value):
    return round(value, 1)

def round_to_nearest_hundredth(value):
    return round(value, 2)

def round_to_nearest_thousandth(value):
    return round(value, 3)

original_value = 13.56449

rounded_integer = round_to_nearest_integer(original_value)
rounded_tenths = round_to_nearest_tenth(original_value)
rounded_hundredths = round_to_nearest_hundredth(original_value)
rounded_thousandths = round_to_nearest_thousandth(original_value)

print(f"Original Value: {original_value}")
print(f"Rounded to nearest integer: {rounded_integer}")
print(f"Rounded to nearest tenth: {rounded_tenths}")
print(f"Rounded to nearest hundredth: {rounded_hundredths}")
print(f"Rounded to nearest thousandth: {rounded_thousandths}")
