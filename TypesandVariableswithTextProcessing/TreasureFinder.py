list_of_numbers = [int(element) for element in input().split()]
encrypt = input()
while not encrypt == 'find':
    numbers_index = 0
    message = ''
    for index in range(len(encrypt)):
        new_asci_order = ord(encrypt[index]) - list_of_numbers[numbers_index]
        message += chr(new_asci_order)
        if numbers_index == len(list_of_numbers)-1:
            numbers_index = 0
        else:
            numbers_index += 1
    starting_index_of_the_type = 0
    number_of_signs1 = 0
    type = ''
    coordinates = ''
    for sub_index in range(len(message)):
        if message[sub_index] == "&":
            if number_of_signs1 == 1:
                type = message[starting_index_of_the_type+1:sub_index]
                break
            starting_index_of_the_type = sub_index
            number_of_signs1 += 1
    starting_index_of_coordinates = 0
    end_index = 0

    for sub_index in range(len(message)):
        if message[sub_index] == "<":
            starting_index_of_coordinates = sub_index
        if message[sub_index] == ">":
            end_index = sub_index
    coordinates = message[starting_index_of_coordinates+1:end_index]


    print(f"Found {type} at {coordinates}")
    encrypt = input()