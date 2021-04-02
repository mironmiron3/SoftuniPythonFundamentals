import re
pattern = r"(=|\/)(?P<destination>[A-Z][a-zA-Z][a-zA-Z]+)\1"
text = input()
matches = [match.group('destination') for match in re.finditer(pattern,text)]
points = len("".join(matches))
destinations_joined = ", ".join(matches)
print(f"Destinations: {destinations_joined}")
print(f"Travel Points: {points}")