import re
pattern = r"\d+"
text = input()
while text:
    match = re.findall(pattern,text)
    print(" ".join(match),end=" ")
    text = input()