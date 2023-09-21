opening_balance = 0
balance_after_inflow = 0
balance_after_dispense = 0

while True:
    print("\nInventory Management System")
    print("1. Add Products")
    print("2. Dispense Products")
    print("3. Display Balance")
    print("4. Exit")

    # use one print statement

    choice = int(input("Enter your choice: "))
    if choice == 1:
        quantity = int(input("Enter received quantity "))
        balance_after_inflow += quantity
        print(f"QUANTITY RECEIVED IS {quantity} ")
        print("ITEM CURRENTLY AVAILABLE IN STOCK")
    elif choice != 1:
        print("OUT OF STOCK")

    if choice == 2:
        quantity_dispensed = int(input("Enter quatity of Stock dispensed"))
        balance_after_inflow -= quantity_dispensed
        print(f"ITEMS SUCCESSFULLY DELIVERED")

# refactr this code.







