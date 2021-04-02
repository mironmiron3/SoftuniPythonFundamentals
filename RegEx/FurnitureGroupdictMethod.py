import re
pattern = r">>(?P<furniture>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"
text = input()
total_money_spent = 0
print("Bought furniture:")
while not text == "Purchase":
    match = re.search(pattern, text)
    if match:

        print(match.groupdict()['furniture'])
        total_money_spent += float(match.groupdict()['price']) * int(match.groupdict()['quantity'])
    text = input()

print(f"Total money spend: {total_money_spent:.2f}")
