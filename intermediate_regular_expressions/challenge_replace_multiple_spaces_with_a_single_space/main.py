import re

def normalize_spaces(text):
    pattern = r" {2,}"
    replacement = " "
    return(re.sub(pattern, replacement, text))

print(normalize_spaces("Hello   world   !"))
print(normalize_spaces("A  B    C     D"))