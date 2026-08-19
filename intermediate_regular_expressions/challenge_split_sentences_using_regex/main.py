import re

def split_sentences(paragraph):
    pattern = r"[^.!?]+[.!?]"
    matches = re.findall(pattern, paragraph, re.DOTALL)
    sentences = [sentence.strip() for sentence in matches]
    return sentences

print(split_sentences("Hello world. How are you? I'm fine!"))
print(split_sentences("First sentence across " + 
                      "multiple lines! Second one."))