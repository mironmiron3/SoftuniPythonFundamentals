destinations = input()

command = input()
while not command == "Travel":
    command = command.split(":")
    if command[0] == "Add Stop":
        index = int(command[1])
        stop = command[2]
        if index in range(len(destinations)):
            destinations = destinations[:index] + stop + destinations[index:]

    elif command[0] == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])
        if start_index in range(len(destinations)) and end_index in range(len(destinations)):
            destinations = destinations[:start_index] + destinations[end_index+1:]

    elif command[0] == 'Switch':
        old_string = command[1]
        new_string = command[2]
        if old_string in destinations:
            destinations = destinations.replace(old_string,new_string)

    print(destinations)
    command = input()
print(f"Ready for world tour! Planned stops: {destinations}")