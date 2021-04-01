n = int(input())
pieces = {}
for piece in range(n):
    command = input().split("|")
    pieces[command[0]] = {}
    pieces[command[0]]['composer'] = command[1]
    pieces[command[0]]['key'] = command[2]
command = input()
while not command == "Stop":
    command = command.split("|")
    if command[0] == "Add":
        if command[1] in pieces:
            print(f"{command[1]} is already in the collection!")
        else:
            pieces[command[1]] = {}
            pieces[command[1]]['composer'] = command[2]
            pieces[command[1]]['key'] = command[3]
            print(f"{command[1]} by {command[2]} in {command[3]} added to the collection!")
    elif command[0] == "Remove":
        if command[1] in pieces:
            pieces.pop(command[1])
            print(f"Successfully removed {command[1]}!")
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")
    elif command[0] == "ChangeKey":
        if command[1] in pieces:
            pieces[command[1]]['key'] = command[2]
            print(f"Changed the key of {command[1]} to {command[2]}!")
        else:
            print(f"Invalid operation! {command[1]} does not exist in the collection.")
    command = input()
#print(sorted(pieces.items(),key=lambda tuple:(tuple[0],tuple[1]['composer'])))
for kvp in sorted(pieces.items(),key=lambda kvp:(kvp[0],kvp[1]['composer'])):

    print(f"{kvp[0]} -> Composer: {kvp[1]['composer']}, Key: {kvp[1]['key']}")
