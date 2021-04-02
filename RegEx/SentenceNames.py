import re
pattern = r"\b_[a-zA-Z0-9]+\b"
text = input()
matches = re.findall(pattern,text)
matches_list = []
for match in matches:
    matches_list.append(match[1:])
print(",".join(matches_list))
