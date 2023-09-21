total_miles = 0
total_gallons = 0

gallons_used = float(input("Enter the gallons used (-1 to end): "))


while gallons_used != -1:
    miles_driven = float(input("Enter the miles driven: "))

    miles_per_gallon = miles_driven / gallons_used

    print(f"The miles/gallon for this tank was {miles_per_gallon}")

    total_miles += miles_driven
    total_gallons += gallons_used

    gallons_used = float(input("Enter the gallons used (-1 to end): "))

if total_gallons != 0:
    combined_miles_per_gallon = total_miles / total_gallons
    print(f"\nThe combined miles/gallon for all tankfuls was {combined_miles_per_gallon}")
else:
    print("\nNo data entered.")