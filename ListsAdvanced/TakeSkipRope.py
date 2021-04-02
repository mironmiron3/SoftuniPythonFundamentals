message= input()
list_of_nonnumbers = []
list_of_numbers = []
for character in message:
    if character.isalpha():
        list_of_nonnumbers.append(character)
    elif character.isdigit():
        list_of_numbers.append(int(character))
take_list = []
skip_list = []
for i in range(len(list_of_numbers)):
    if i % 2 == 0:
        take_list.append(list_of_numbers[i])
    else:
        skip_list.append(list_of_numbers[i])
non_number_joined = "".join(list_of_nonnumbers)
result_string = ''
cursor = 0
for i in range(len(take_list)):
    if cursor + take_list[i] >= len(non_number_joined):
        result_string += non_number_joined[cursor:]
        break
    result_string += non_number_joined[cursor:cursor+take_list[i]]
    cursor += take_list[i] -1
    if i < len(skip_list):
        cursor += skip_list[i]
print(result_string)



