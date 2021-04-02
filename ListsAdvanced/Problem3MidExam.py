available_cards = input().split(":")
new_deck = []
command = input()

while not command == "Ready":
    commands = command.split()
    if commands[0] == "Add":
        if not commands[1] in available_cards:
            print("Card not found.")
            command = input()
            continue
        new_deck.append(commands[1])
    if commands[0] == "Insert":
        if commands[1] not in available_cards or int(commands[2]) not in range(len(new_deck)):
            print("Error!")
            command = input()
            continue
        new_deck.insert(int(commands[2]), commands[1])
    if commands[0] == "Remove":
        if commands[1] in new_deck:
            new_deck.remove(commands[1])
        else:
            print("Card not found.")
    if commands[0] == "Swap":
        index1 = new_deck.index(commands[1])
        index2 = new_deck.index(commands[2])
        new_deck[index1], new_deck[index2] = new_deck[index2], new_deck[index1]
    if commands[0] == "Shuffle":
        new_deck.reverse()
    command = input()

print(" ".join(new_deck))
