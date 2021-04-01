legendaries = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
is_obtained = False

while True:
    data = input().lower()
    info = data.split()
    for i in range(0, len(info), 2):
        quantity = int(info[i])
        item = info[i+1]
        if item in materials:
            materials[item] += quantity
            if materials[item] >= 250:
                print(f"{legendaries[item]} obtained!")
                is_obtained = True
                materials[item] -= 250
                break
        else:
            if item not in junk:
                junk[item] = 0
            junk[item] += quantity
    if is_obtained:
        break
sorted_key_materials = sorted(materials.items(),key=lambda kvp: (-kvp[1],kvp[0]))
for quantity, material in sorted_key_materials:
    print(f"{quantity}: {material}")
sorted_junk = sorted(junk.items(), key=lambda kvp: kvp[0])
for junk_item, number in sorted_junk:
    print(f"{junk_item}: {number}")
