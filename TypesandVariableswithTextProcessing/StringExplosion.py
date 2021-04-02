string_given = input()
new_string = ''
index = 0
explosion_power = 0
while index < len(string_given):
    if not string_given[index] == ">":
        new_string += string_given[index]
        index += 1
        continue
    else:
        new_string += ">"
        index += 1
        explosion_power += int(string_given[index])
        for i in range(1, explosion_power+1):
            if string_given[index] == ">":
                break
            index += 1
            explosion_power -= 1
print(new_string)

