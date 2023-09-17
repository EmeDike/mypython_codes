
while True:

    employees_name = input("Enter Employees Name " )
    if employees_name.lower() == "exit":
        break

    number_of_hours_worked = int(input("Enter Number Of Hours Worked "))
    hourly_pay_rate = int(input("Enter Hourly Pay Rate "))
    federal_tax_withholding_rate = float(input ("Enter fedral tax withholding ratefedral tax withholding rate "))
    state_tax_withholding_rate = float(input("Enter State tax withholding rate "))
    month = input("Enter month ")

    gross_pay = number_of_hours_worked * hourly_pay_rate
    federal_tax_withholding = federal_tax_withholding_rate * gross_pay
    state_tax_withholding = state_tax_withholding_rate * gross_pay

    total_deductions = federal_tax_withholding + state_tax_withholding
    net_pay = gross_pay - total_deductions

    print("\nPAYROLL STATEMENT")
    print(f"Employee: {employees_name}")
    print(f"Month: {month}")
    print(f"Number of Hours Worked: {number_of_hours_worked}")
    print(f"Hourly Pay Rate: ${hourly_pay_rate:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Federal Tax Withholding: ${federal_tax_withholding_rate:.2f}")
    print(f"State Tax Withholding: ${state_tax_withholding:.2f}")
    print(f"Total Deductions: ${total_deductions:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")