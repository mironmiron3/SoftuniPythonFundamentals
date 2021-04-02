list_of_houses = list(map(int, input().split("@")))
command = input()
last_position = 0
while not command == "Love!":
    command_as_list = command.split()
    if (last_position + int(command_as_list[1])) in range(0, len(list_of_houses)):
        list_of_houses[last_position + int(command_as_list[1])] -= 2
        if list_of_houses[last_position + int(command_as_list[1])] == 0:
            print(f"Place {(last_position + int(command_as_list[1]))} has Valentine's day." )
        elif list_of_houses[last_position + int(command_as_list[1])] < 0:
            print(f"Place {(last_position + int(command_as_list[1]))} already had Valentine's day.")

        last_position += int(command_as_list[1])
    else:
        list_of_houses[0] -= 2
        if list_of_houses[0] == 0:
            print(f"Place {0} has Valentine's day." )
        elif list_of_houses[0] < 0:
            print(f"Place {0} already had Valentine's day.")

        last_position = 0
    command = input()

print(f"Cupid's last position was {last_position}.")
list_of_loved_ones = list(filter(lambda x: x <= 0, list_of_houses))
if len(list_of_loved_ones) == list_of_houses:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(list_of_houses)- len(list_of_loved_ones)} places.")



