def get_student_age():
    name = input("Enter your name: ").lower()

    if name in student_age:
        age = student_age[name]
        return f"Hi {name}, you are {age} years old."
    else:
        print("The name is not in the dictionary.")
        age = int(input("Enter your age: "))
        student_age[name] = age
        return f"Hi {name}, you are {age} years old."

student_age = {"dike": 33, "ope": 22, "melody": 20, "precious": 25}
result = get_student_age()
print(result)
print("current student_age dictionary:", student_age)
