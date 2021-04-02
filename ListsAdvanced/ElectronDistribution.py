number_of_electrons = int(input())
shell = 1
list_of_layers = []
while number_of_electrons > 0:
    shell_max_capacity = 2 * (shell ** 2)
    if number_of_electrons >= shell_max_capacity:
        list_of_layers.append(shell_max_capacity)
        number_of_electrons -= shell_max_capacity
    else:
        list_of_layers.append(number_of_electrons)
        number_of_electrons -= number_of_electrons

    shell += 1
print(list_of_layers)

