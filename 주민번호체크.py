import re

def format_korean_resident_number(rrn):
    # Check if the input consists of exactly 13 digits
    if not re.match(r'^\d{13}$', rrn):
        return "Invalid"

    # Split the input into the first six digits and the last seven digits
    first_six = rrn[:6]
    last_seven = rrn[6:]

    # Check if the first digit of the last seven digits is 1 or 2
    if last_seven[0] not in ['1', '2']:
        return "Invalid"

    # Format the RRN as 6 digits - hyphen - 7 digits
    formatted_rrn = f"{first_six}-{last_seven}"

    return formatted_rrn

# Sample Korean resident registration numbers
sample_rrns = ["0001011000000", "0701014211111", "9901232123456", "0202291234567",
               "5502262123456", "0912302123456", "7801011212121", "2111119999999",
               "9502151111111", "8101012000000"]

for rrn in sample_rrns:
    formatted_rrn = format_korean_resident_number(rrn)
    print(f"Original: {rrn}")
    print(f"Formatted: {formatted_rrn}")
    print()

