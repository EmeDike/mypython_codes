def calculate_investment_growth(investment, interest_rate, years):
    for year in range(1, years + 1):
        interest = investment * interest_rate
        new_investment = investment + interest
        investment = new_investment
        print(f"Year {year}: Current investment = {investment:.2f}")
    return investment

interest_rate = 0.10
investment = float(input("Enter your initial amount: "))
years = 30

final_investment = calculate_investment_growth(investment, interest_rate, years)
print(f"After {years} years, your final investment is {final_investment:.2f}")


