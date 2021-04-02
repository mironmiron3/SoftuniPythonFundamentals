list_of_commands = input().split("|")
energy = 100
coins = 100
is_closed = False

for command in range(len(list_of_commands)):

    if is_closed:
        break
    current_act = list_of_commands[command].split("-")
    event = current_act[0]
    value = int(current_act[1])
    if event == "rest":
        if energy + value > 100:
            value = 100 - energy
            energy = 100


        else:
            energy += value
        print(f"You gained {value} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")

        else:
            energy += 50
            print("You had to rest!")
            continue

    else:
        if value > coins:
            print(f"Closed! Cannot afford {event}.")
            is_closed = True
            break
        else:
            coins -= value
            print(f"You bought {event}.")

if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")






