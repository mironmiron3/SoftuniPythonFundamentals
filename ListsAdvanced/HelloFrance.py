list_of_items = input().split("|")
budget = float(input())
initial_money = budget
profit = 0

for i in range(len(list_of_items)):
    product_characteristics = list_of_items[i].split("->")
    type1 = product_characteristics[0]
    value = float(product_characteristics[1])
    new_price = 0
    if value > budget:
        continue
    if type1 == "Clothes" and value <= 50:
        budget -= value
        new_price = value * 1.4
        profit += (new_price - value)
        print(f"{new_price:.2f}", end=" ")
    elif type1 == "Shoes" and value <= 35:
        budget -= value
        new_price = value * 1.4
        profit += (new_price - value)
        print(f"{new_price:.2f}", end=" ")
    elif type1 == "Accessories" and value <= 20.50:
        budget -= value
        new_price = value * 1.4
        profit += (new_price - value)
        print(f"{new_price:.2f}", end=" ")

print()
print(f"Profit: {profit:.2f}")
if initial_money + profit >= 150:
    print("Hello, France!")
else:
    print("Time to go.")


