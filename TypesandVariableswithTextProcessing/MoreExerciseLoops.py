first_string = input()
second_string = input()
result = ''
previous_string = ''
for i in range(len(first_string)):
    for index in range(i + 1):
        result += second_string[index]
    for index_2 in range(i + 1,len(second_string)):
        result += first_string[index_2]
    if not result == previous_string:
        print(result)
    previous_string = result
    result = ''

