str_of_numbers = input().split(", ")
number_of_beggars = int(input())
starting_index = 0
new_list = []
for beggar in range(number_of_beggars):
    current_sum = 0
    for index in range(starting_index, len(str_of_numbers), number_of_beggars):
        current_sum += int(str_of_numbers[index])

    new_list.append(current_sum)
    starting_index += 1

print(new_list)




