list_of_numbers_as_strings = input().split(", ")

for index in range(len(list_of_numbers_as_strings)):
    number = int(list_of_numbers_as_strings[index])
    if number == 0:
        list_of_numbers_as_strings.remove(str(0))
        list_of_numbers_as_strings.append(str(0))

print(list_of_numbers_as_strings)
