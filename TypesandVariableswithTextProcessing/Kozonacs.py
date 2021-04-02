import math
budget = float(input())
flour_price = float(input())
eggs_price= 0.75 * flour_price
milk_price = (1.25 * flour_price) / 4
price_of_kozonac = flour_price + eggs_price + milk_price
kozonacs = 0
colored_eggs = 0

while budget >= price_of_kozonac:
    kozonacs += 1
    colored_eggs += 3
    if kozonacs % 3 == 0:
        colored_eggs = colored_eggs - (kozonacs - 2)
    budget = budget - price_of_kozonac

print(f"You made {kozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
