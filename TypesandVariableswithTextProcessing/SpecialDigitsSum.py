n = int(input())

for num in range (1, n + 1):
    num_as_string = str(num)
    sum_of_digits = 0
    for digit in num_as_string:
        digit_num = int(digit)
        sum_of_digits += digit_num
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')
