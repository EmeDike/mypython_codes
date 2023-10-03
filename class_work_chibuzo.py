scores = []


sum = 0

for i in range(10):
    maximum = scores[_inf_]
    minimum = scores[i]

    students_scores = int(input("Enter students scores  "))
    scores.append(students_scores)
    sum = sum + students_scores
    average = sum / len(scores)
    if maximum > scores[i]:
            maximum = scores[i]
    elif minimum < scores[i]:
            minimum = scores[i]

print(sum)
print(average)
print(maximum)
print(minimum)