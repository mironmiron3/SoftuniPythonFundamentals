import re
text = input()
pattern = r"((?<=\s)|^)[a-zA-Z0-9]+[\.\-\_]?[a-zA-Z0-9]+@[a-zA-Z]+-?[a-zA-Z]+(\.[a-z]+)+\b"
matches = re.finditer(pattern,text)
for match in matches:
    print(match.group())