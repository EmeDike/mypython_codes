scores = [
    [25, 50, 75],
    [40, 50, 60],
    [75, 65, 80]
]

averages = []

for row in scores:
    row_average = sum(row) / len(row)
    averages.append(row_average)

total_average = sum(averages) / len(averages)

print("Averages for each list:", averages)
print("Average of averages:", total_average)
