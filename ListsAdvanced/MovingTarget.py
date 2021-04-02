list_of_targets = [int(target) for target in input().split()]
command = input()
while not command == "End":
    list_of_acts = command.split()
    if list_of_acts[0] == "Shoot":
        if int(list_of_acts[1]) in range(0, len(list_of_targets)):
            list_of_targets[int(list_of_acts[1])] -= int(list_of_acts[2])
            if list_of_targets[int(list_of_acts[1])] <= 0:
                list_of_targets.pop(int(list_of_acts[1]))



    if list_of_acts[0] == "Add":
        if int(list_of_acts[1]) in range(0, len(list_of_targets)):
            list_of_targets.insert(int(list_of_acts[1]),int(list_of_acts[2]))
        else:
            print("Invalid placement!")



    if list_of_acts[0] == "Strike":
        if int(list_of_acts[1]) in range(0, len(list_of_targets)) and (int(list_of_acts[1])-int(list_of_acts[2])) in range(0, len(list_of_targets)) and (int(list_of_acts[1])+int(list_of_acts[2])) in range(0, len(list_of_targets)):
            start_index = int(list_of_acts[1]) - int(list_of_acts[2])
            end_index = int(list_of_acts[1]) + int(list_of_acts[2])

            for i in range(start_index,end_index + 1):
                list_of_targets[i] = -1000
            list_of_targets = [e for e in list_of_targets if not e == -1000]
        else:
            print("Strike missed!")
    command = input()
list_of_targets_end = [str(num) for num in list_of_targets]
print("|".join(list_of_targets_end))