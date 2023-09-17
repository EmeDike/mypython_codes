
name_of_item = input("Enter Name Of Item ")
credit_score = int(input("Enter credit score: "))
price = int(input("Enter price of item: "))

if 0 < credit_score <= 50:
    down_payment = price * 0.25
elif credit_score > 50:
    discount = price * 0.10
    amount = price - discount
    down_payment = amount * 0.10
else:
    print("INVALID CREDIT SCORE")
    down_payment = 0



print("*****************************")

print(f"\t\t\tINVOICE")

print("*****************************")
print(f"Name Of The Item is:", name_of_item)
print("Discount is: ", discount)
print("Down Payment:", down_payment)
