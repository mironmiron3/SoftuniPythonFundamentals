list_of_items = input().split(", ")

command = input()
while not command == "Craft!":
    list_of_acts = command.split(" - ")
    if list_of_acts[0] == "Collect":
        if not list_of_acts[1] in list_of_items:
            list_of_items.append(list_of_acts[1])
    if list_of_acts[0] == "Drop":
        if list_of_acts[1] in list_of_items:
            list_of_items.remove(list_of_acts[1])
    if list_of_acts[0] == "Combine Items":
        old_item, new_item = list_of_acts[1].split(":")
        if old_item in list_of_items:
            index_old_item = list_of_items.index(old_item)
            list_of_items.insert((index_old_item + 1),new_item)
    if list_of_acts[0] == "Renew":
        if list_of_acts[1] in list_of_items:
            list_of_items.remove(list_of_acts[1])
            list_of_items.append(list_of_acts[1])

    command = input()

print(", ".join(list_of_items))