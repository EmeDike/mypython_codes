total_score = 0
count = 0

while True:
    students_score = int(input("Enter Student's Score (terminate with 0): "))

    if students_score == -1:
        print("Terminating input.")
        break

    total_score += students_score
    count += 1

average = total_score / count
print(f"Average is: {average}")
