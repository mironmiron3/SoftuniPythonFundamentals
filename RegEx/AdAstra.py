import re
pattern = r"(\#|\|)(?P<product>([a-zA-Z]|\s)+)\1(?P<date>\d{2}\/\d{2}\/\d{2})\1(?P<calories>\d+)\1"
items = []
text = input()
total_calories = 0
for match in re.finditer(pattern, text):
    items.append(match.groupdict())
    total_calories += int(match.groupdict()["calories"])
print(f"You have food to last you for: {total_calories//2000} days!")
for item in items:
    print(f"Item: {item['product']}, Best before: {item['date']}, Nutrition: {item['calories']}")

