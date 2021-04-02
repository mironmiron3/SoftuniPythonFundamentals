import re
pattern = r"[star]"
pattern_for_details = r"(?<=@)(?P<planet>[a-zA-Z]+)[^@\-!:>]?:(?P<population>\d+)[^@\-!:>]?!(?P<type>A|D)![^@\-!:>]?\-\>(?P<soldiers>\d+)"
counter = int(input())
attacked_planets = []
destroyed_planets = []
for i in range(counter):
    text = input()
    new_text = ''
    count = len(re.findall(pattern, text, re.IGNORECASE))
    for index in range(len(text)):
        new_ascii_order = ord(text[index]) - count
        new_text += chr(new_ascii_order)
    match = re.search(pattern_for_details, new_text)
    if match:
        if match.groupdict()['type'] == "D":
            destroyed_planets.append(match.groupdict()['planet'])
        else:
            attacked_planets.append(match.groupdict()['planet'])
separator = "\n-> "
if len(attacked_planets) == 0:
    print(f"Attacked planets: 0")
else:
    print(f"Attacked planets: {len(attacked_planets)}\n-> {separator.join(sorted(attacked_planets))}")
if len(destroyed_planets) == 0:
    print(f"Destroyed planets: 0")
else:
    print(f"Destroyed planets: {len(destroyed_planets)}\n-> {separator.join(sorted(destroyed_planets))}")



