list_of_fires = input().split("#")
all_water = int(input())
diff = all_water

print("Cells:")

for i in range(len(list_of_fires)):
    fire_list = list_of_fires[i].split(" = ")
    type1 = fire_list[0]
    value = int(fire_list[1])
    if type1 == "Low" and 1 <= value <= 50:
        if value > all_water:
            continue
        else:
            all_water -= value
            print(f"- {value}")
    elif type1 == "Medium" and 51 <= value <= 80:
        if value > all_water:
            continue
        else:
            all_water -= value
            print(f"- {value}")
    elif type1 == "High" and 81 <= value <= 125:
        if value > all_water:
            continue
        else:
            all_water -= value
            print(f"- {value}")

total_fire = diff - all_water
effort = 0.25 * total_fire
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")