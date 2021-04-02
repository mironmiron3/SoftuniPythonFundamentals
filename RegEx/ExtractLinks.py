import re
link_pattern = r"www\.[a-zA-Z0-9]+(\-[a-zA-Z0-9]+)?(\.[a-z]+)+"
text = input()
while text:
    match = re.search(link_pattern, text)
    if match:
        print(match.group())
    text = input()

