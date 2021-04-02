import re
pattern = r"((?<=\s)|^)%(?P<customer>[A-Z][a-z]+)%[^|$%.]?\<(?P<product>[a-zA-Z]+)\>([^|$%.]+)?\|(?P<count>\d+)\|([^|$%.0-9]+)?(?P<price>\d+(.\d+)?)(?=\$)"
text = input()
total_income = 0
while not text == "end of shift":
    match = re.search(pattern, text)
    characteristics = {}
    if match:
        characteristics = match.groupdict()
        revenue = float(characteristics['price']) * int(characteristics['count'])
        print(f"{characteristics['customer']}: {characteristics['product']} - {revenue:.2f}")
        total_income += revenue
    text = input()
print(f"Total income: {total_income:.2f}")
