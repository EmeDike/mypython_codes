def main():
    credit_card_number = input("Kindly Enter Card Details To Verify: ")
    result = validate_credit_card(credit_card_number)
    print("Result:", result)

def validate_credit_card(card_number):
    card_number = ''.join(filter(str.isdigit, card_number))

    if not (13 <= len(card_number) <= 16):
        return "Invalid Card Length"

    card_type = identify_card_type(card_number)
    total_sum = calculate_total_sum(card_number)
    is_valid = total_sum % 10 == 0

    return f"{card_type} - {'Valid' if is_valid else 'Invalid'}"

def identify_card_type(card_number):
    if card_number.startswith("4"):
        return "Visa"
    elif card_number.startswith("5"):
        return "MasterCard"
    elif card_number.startswith("37"):
        return "American Express"
    elif card_number.startswith("6"):
        return "Discover"
    else:
        return "Unknown Card Type"

def calculate_total_sum(card_number):
    total_sum = 0
    reverse_digits = list(reversed(card_number))

    for i, digit in enumerate(reverse_digits):
        digit = int(digit)
        if i % 2 == 1:
            doubled_digit = digit * 2
            total_sum += doubled_digit if doubled_digit < 10 else (doubled_digit - 9)
        else:
            total_sum += digit

    return total_sum

if __name__ == "__main__":
    main()
