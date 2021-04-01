products = {}
data = input()
while not data == "buy":
    product, price, quantity = data.split()
    if product not in products:
        products[product] = {}
        products[product]["quantity"] = 0
    products[product]["quantity"] += int(quantity)
    products[product]["price"] = float(price)
    data = input()
for product, info in products.items():
    total = info["price"]*info["quantity"]
    print(f"{product} -> {total:.2f}")
