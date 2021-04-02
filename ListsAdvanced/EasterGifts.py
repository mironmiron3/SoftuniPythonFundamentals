list_of_planned_gifts = input().split()
command = input()

while command != "No Money":
    if "OutOfStock" in command:
        list_of_acts = command.split()
        for index in range(len(list_of_planned_gifts)):
            if list_of_planned_gifts[index] == list_of_acts[1]:
                list_of_planned_gifts.remove(list_of_planned_gifts[index])
                list_of_planned_gifts.insert(index, "None")
    if "Required" in command:
        list_of_acts = command.split()
        if int(list_of_acts[2]) < len(list_of_planned_gifts):

            list_of_planned_gifts.pop(int(list_of_acts[2]))
            list_of_planned_gifts.insert(int(list_of_acts[2]), list_of_acts[1])
        else:
            list_of_planned_gifts.append(list_of_acts[1])
    if "JustInCase" in command:
        list_of_acts = command.split()
        list_of_planned_gifts.pop()
        list_of_planned_gifts.append(list_of_acts[1])
    list_of_acts = []
    command = input()
for el in list_of_planned_gifts:
    if el == "None":
        list_of_planned_gifts.remove(el)
print(" ".join(list_of_planned_gifts))
