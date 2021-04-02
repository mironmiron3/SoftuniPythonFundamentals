def split_list_after_index(list1, index):
    if index > len(list1):
        return "Invalid index"
    list_with_first_items = []
    for i in range(index + 1):
        list_with_first_items.append(list1[0])
        list1.pop(0)
    list1 += list_with_first_items
    return list1



def max_even_and_odd_numbers_index(list1):
    found_odd_max = False
    found_even_max = False
    max_even = 0
    max_odd = 0
    max_odd_index = 1001
    max_even_index = 1001

    for i in range(0, len(list1)):
        num = int(list1[i])
        if num > max_odd and num % 2 != 0:
            max_odd = num
            found_odd_max = True
            max_odd_index = i
        if num > max_even and num % 2 == 0:
            max_even = num
            found_even_max = True
            max_even_index = i
    return max_even_index, max_odd_index

def min_even_and_odd_numbers_index(list1):
    found_odd_min = False
    found_even_min = False
    min_even = 1001
    min_odd = 1001
    min_odd_index = 1001
    min_even_index = 1001
    for i in range(0, len(list1)):
        num = int(list1[i])
        if num < min_odd and num % 2 != 0:
            min_odd = num
            found_odd_min = True
            min_odd_index = i
        if num < min_even and num % 2 == 0:
            min_even = num
            found_even_min = True
            min_even_index = i
    return min_even_index, min_odd_index

def first_count_even_numbers(list1, count):
    if count > len(list1):
        return "Invalid count"
    list_of_evens = []
    for i in range(len(list1)):
        num = int(list1[i])
        if num % 2 == 0:
            list_of_evens.append(num)
        if len(list_of_evens) == count:
            break
    return list_of_evens

def first_count_odd_numbers(list1, count):
    if count > len(list1):
        return "Invalid count"
    list_of_odds = []
    for i in range(len(list1)):
        num = int(list1[i])
        if num % 2 != 0:
            list_of_odds.append(num)
        if len(list_of_odds) == count:
            break
    return list_of_odds

def last_count_even_numbers(list1, count):
    if count > len(list1):
        return "Invalid count"
    list_of_evens = []
    for i in range(len(list1) - 1, -1, -1):
        num = int(list1[i])
        if num % 2 == 0:
            list_of_evens.append(num)
        if len(list_of_evens) == count:
            break
    return list_of_evens
def last_count_odd_numbers(list1, count):
    if count > len(list1):
        return "Invalid count"
    list_of_odds = []
    for i in range(len(list1) - 1, -1, -1):
        num = int(list1[i])
        if num % 2 != 0:
            list_of_odds.append(num)
        if len(list_of_odds) == count:
            break
    return list_of_odds


numbers_as_strings_in_list = input().split()
command = input()

while command != "end":
    list_of_acts = command.split()
    if list_of_acts[0] == "exchange":

        outcome = split_list_after_index(numbers_as_strings_in_list, int(list_of_acts[1]))
        if outcome == "Invalid index":
            print("Invalid index")
    if list_of_acts[0] == "max":
        if list_of_acts[1] == "odd":
            outcome = max_even_and_odd_numbers_index(numbers_as_strings_in_list)[1]
            if outcome == 1001:
                print("No matches")
            else:
                print(outcome)
        elif list_of_acts[1] == "even":
            outcome = max_even_and_odd_numbers_index(numbers_as_strings_in_list)[0]
            if outcome == 1001:
                print("No matches")
            else:
                print(outcome)
    if list_of_acts[0] == "min":
        if list_of_acts[1] == "odd":
            result = min_even_and_odd_numbers_index(numbers_as_strings_in_list)[1]
            if result == 1001:
                print("No matches")
            else:
                print(result)
        if list_of_acts[1] == "even":
            result = min_even_and_odd_numbers_index(numbers_as_strings_in_list)[0]
            if result == 1001:
                print("No matches")
            else:
                print(result)
    if list_of_acts[0] == "first":
        if list_of_acts[2] == "even":
            list1 = first_count_even_numbers(numbers_as_strings_in_list, int(list_of_acts[1]))
            print(list1)
        elif list_of_acts[2] == "odd":
            list1 = first_count_odd_numbers(numbers_as_strings_in_list,int(list_of_acts[1]))
            print(list1)
    if list_of_acts[0] == "last":
        if list_of_acts[2] == "even":
            list2 = last_count_even_numbers(numbers_as_strings_in_list, int(list_of_acts[1]))
            print(list2)
        elif list_of_acts[2] == "odd":
            list2 = last_count_odd_numbers(numbers_as_strings_in_list, int(list_of_acts[1]))
            print(list2)
    command = input()
nums = []
for element in numbers_as_strings_in_list:
    num = int(element)
    nums.append(num)

print(nums)
