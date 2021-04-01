material = input()
resources = {}
while not material == "stop":
    quantity = int(input())
    if material not in resources:
        resources[material] = quantity
    else:
        resources[material] += quantity
    material = input()

for pair in resources.items():
    print(f"{pair[0]} -> {pair[1]}")
