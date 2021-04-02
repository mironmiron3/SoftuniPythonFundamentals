friends_list = input().split(", ")
command = input()

while command != "Report":
    commands = command.split()
    is_blacklisted = False
    if commands[0] == "Blacklist":
        for i in range(len(friends_list)):
            if commands[1] == friends_list[i]:
                print(f"{friends_list[i]} was blacklisted.")
                friends_list[i] = "Blacklisted"
                is_blacklisted = True
                break
        if not is_blacklisted:
            print(f"{commands[1]} was not found.")
    if commands[0] == "Error":
        given_index = int(commands[1])
        if friends_list[given_index] != "Blacklisted" and friends_list[given_index] != "Lost":
            print(f"{friends_list[given_index]} was lost due to an error.")
            friends_list[given_index] = "Lost"
    if commands[0] == "Change":
        if int(commands[1]) in range(len(friends_list)):
            print(f"{friends_list[int(commands[1])]} changed his username to {commands[2]}.")
            friends_list[int(commands[1])] = commands[2]
    command = input()

counter_of_blacklists = friends_list.count("Blacklisted")
print(f"Blacklisted names: {counter_of_blacklists}")
counter_of_lost_ones = friends_list.count("Lost")
print(f"Lost names: {counter_of_lost_ones}")
print(" ".join(friends_list))

