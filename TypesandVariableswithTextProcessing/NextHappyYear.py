import sys
year = int(input()) + 1
is_happy = True

for i in range (year, sys.maxsize):

    year_as_string = str(i)
    for index_1 in range (len(year_as_string)):
        for index_2 in range (len(year_as_string)):
            if index_1 == index_2:
                continue
            if year_as_string[index_1] == year_as_string[index_2]:
                is_happy = False
    if is_happy == True:
            print(year_as_string)
            break
    is_happy = True

