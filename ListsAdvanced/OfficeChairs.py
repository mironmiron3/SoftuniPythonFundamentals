number_of_rooms = int(input())
free_chairs = 0
insufficiency = False
for i in range(1, number_of_rooms + 1):
    list_of_chairs_and_people = input().split()
    chairs = len(list_of_chairs_and_people[0])
    needed_ones = int(list_of_chairs_and_people[1])
    if chairs >= needed_ones:
        free_chairs += chairs - needed_ones
    else:
        insufficiency = True
        print(f"{needed_ones-chairs} more chairs needed in room {i}")

if not insufficiency:
    print(f"Game On, {free_chairs} free chairs left")

