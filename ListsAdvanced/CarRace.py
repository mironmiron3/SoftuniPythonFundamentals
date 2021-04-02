import math
list_of_numbers = [int(num) for num in input().split()]
score_of_first = 0
score_of_second = 0
for index in range(0, math.ceil((len(list_of_numbers)/2))-1):
    if list_of_numbers[index] == 0:
        score_of_first *= 0.8
    else:
        score_of_first += list_of_numbers[index]
for index in range(len(list_of_numbers)-1, math.floor(len(list_of_numbers)/2),-1):
    if list_of_numbers[index] == 0:
        score_of_second *= 0.8
    else:
        score_of_second += list_of_numbers[index]

if score_of_first < score_of_second:
    print(f"The winner is left with total time: {score_of_first:.1f}")
else:
    print(f"The winner is right with total time: {score_of_second:.1f}")


