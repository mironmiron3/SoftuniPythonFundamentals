list_of_strings = input().split()
all_numbers = []
total_sum = 0
for string in list_of_strings:
    number = int(string[1:-1])
    if string[0].isupper():
        number /= (ord(string[0])-64)
    else:
        number *= (ord(string[0])-96)
    if string[-1].isupper():
        number -= (ord(string[-1])-64)
    else:
        number += (ord(string[-1])-96)
    total_sum += number

print(f'{total_sum:.2f}')