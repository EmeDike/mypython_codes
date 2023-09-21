
purchase_price = float(input("Enter the purchase price (dollars or less): "))

if purchase_price > 1.0:
    print("Invalid input. Purchase price must be a dollar or less.")
else:
    purchase_price_cents = int(purchase_price * 100)
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    change = 100 - purchase_price_cents

    quarters = change // 25
    change %= 25

    dimes = change // 10
    change %= 10

    nickels = change // 5
    change %= 5

    pennies = change

    print("Change to be given:")
    if quarters > 0:
        print(f"Quarters: {quarters}")
    if dimes > 0:
        print(f"Dimes: {dimes}")
    if nickels > 0:
        print(f"Nickels: {nickels}")
    if pennies > 0:
        print(f"Pennies: {pennies}")