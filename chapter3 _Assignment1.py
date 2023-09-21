print("Welcome to the Medical Diagnosis Simulator!")

while True:
    response = input("Have you had this problem before?    (yes or no): ").strip().lower()

    if response == "yes":
        print("You have it again.")
    elif response == "no":
        print("You have it now.")
    else:
        print("Invalid response. Please answer 'yes' or 'no'.")

    another_problem = input("Do you have another problem to discuss? (yes or no) ").strip().lower()
    if another_problem != "yes":
        break

print("Thank you for using the Medical Diagnosis Simulator!")
