import re

def is_valid_phone_number(phone):
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return bool(re.match(pattern, phone))

print(is_valid_phone_number("123-456-7890"))
print(is_valid_phone_number("1234567890"))
print(is_valid_phone_number("123-45-6789"))
print(is_valid_phone_number("abc-def-ghij"))