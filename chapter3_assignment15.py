values = [9, 11, 22, 34, 17, 22, 34, 22, 40]

mean_value = sum(values) / len(values)

sorted_values = sorted(values)
median_index = len(sorted_values) // 2

if len(sorted_values) % 2 == 0:
    median_value = (sorted_values[median_index - 1] + sorted_values[median_index]) / 2
else:
    median_value = sorted_values[median_index]

value_counts = {}
for value in values:
    if value in value_counts:
        value_counts[value] += 1
    else:
        value_counts[value] = 1

mode_value = max(value_counts, key=lambda x: value_counts[x])

print(f"Mean (Average): {mean_value:.2f}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")