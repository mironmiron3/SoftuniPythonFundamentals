list_of_nums_as_strings = input().split(", ")
list_of_nums = [int(num) for num in list_of_nums_as_strings]
group = 10
while len(list_of_nums) > 0:

    current_list = list(filter(lambda x: x <= group, list_of_nums))
    list_of_nums = list(filter(lambda x: x > group, list_of_nums))

    print(f"Group of {group}'s: {current_list}")
    group += 10


