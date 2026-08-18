import re

def find_words_starting_with_a(text):
    pattern = r"\bA\w*"
    my_words = re.findall(pattern, text)
    return my_words

print(find_words_starting_with_a("Alice and Bob met Amy at an Airport."))
print(find_words_starting_with_a("Amazing! An_underscore, A1, and A-B were noted; also an apple."))