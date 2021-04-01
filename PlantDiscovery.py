n = int(input())
plants = {}
for i in range(n):
    plant, rarity = input().split("<->")
    if plant not in plants:
        plants[plant] = {}
    plants[plant]['rarity'] = int(rarity)
    plants[plant]['ratings'] = []
command = input()
while not command == "Exhibition":
    command = command.split(": ")
    try:
        if command[0] == "Rate":
            plant, rating = command[1].split(" - ")
            plants[plant]['ratings'].append(int(rating))
        elif command[0] == 'Update':
            plant, new_rarity = command[1].split(" - ")
            plants[plant]['rarity'] = int(new_rarity)
        elif command[0] == "Reset":
            plant = command[1]
            plants[plant]['ratings'].clear()
        else:
            print("error")
    except KeyError:
        print("error")
    command = input()

for x in plants.values():
    if not len(x['ratings']) == 0:
        x['ratings'] = sum(x['ratings'])/len(x['ratings'])
    else:
        x['ratings'] = 0

print(f'Plants for the exhibition:')
for kvp in sorted(plants.items(),key=lambda kvp:(-kvp[1]['rarity'],-kvp[1]['ratings'])):
    print(f"- {kvp[0]}; Rarity: {kvp[1]['rarity']}; Rating: {kvp[1]['ratings']:.2f}")





