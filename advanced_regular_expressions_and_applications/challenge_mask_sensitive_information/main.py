import re

def mask_credit_card_numbers(text):
    pattern = r'((?:\d{4}[- ]?){3}\d{4})'
    def mask_match(match):
        number = match.group()
        digits = re.sub(r"[ -]", "", number)
        if len(digits) != 16:
            return number
        masked = []
        count = 0
        for c in reversed(number):
            if c.isdigit():
                count += 1
                masked.append(c if count <= 4 else "*")
            else:
                masked.append(c)
        return "".join(reversed(masked))

    return re.sub(pattern, mask_match, text)

print(mask_credit_card_numbers("Pay with 4111 1111 1111 1111 or 5500-0000-0000-0004 today."))
print(mask_credit_card_numbers("Card: 1234-5678-9012-3456; Backup: 4444 3333 2222 1111."))