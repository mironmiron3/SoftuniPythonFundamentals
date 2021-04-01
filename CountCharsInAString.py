given_text = input()
chars = {}
for element in given_text:
    if element == " ":
        continue
    elif element not in chars:
        chars[element] = 1
        continue
    chars[element] += 1
for tuple in chars.items():
    print(f"{tuple[0]} -> {tuple[1]}")