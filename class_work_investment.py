
year = 1
interest_per_year = 0.10
investment = float(input("Enter your amount:  "))
while year < 31:
    interest = investment * interest_per_year
    new_investment = investment + interest
    investment = new_investment
    print(f"year {year} current investment = {investment:.2f}")
    year += 1