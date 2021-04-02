list_of_numbers = input().split()
string_given = input()

for element in list_of_numbers:
    index_needed = 0
    for digit in element:
        index_needed += int(digit)
    while index_needed > len(string_given):
        index_needed -= len(string_given)
    print(string_given[index_needed], end="")
    first_part = string_given[:index_needed]
    second_part = string_given[index_needed+1:]
    string_given = first_part + second_part






