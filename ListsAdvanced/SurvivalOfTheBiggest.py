import sys
numbers_as_string = input()
removed_ones = int(input())


list_of_numbers = numbers_as_string.split()
for i in range(removed_ones):
    min_number = sys.maxsize
    for el in list_of_numbers:
        if int(el) < min_number:
            min_number = int(el)
    list_of_numbers.remove(str(min_number))


print(list_of_numbers)







