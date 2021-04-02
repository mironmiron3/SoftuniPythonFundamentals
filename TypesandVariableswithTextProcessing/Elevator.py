import math
all_passengers = int(input())
capacity = int(input())

tours = math.ceil((all_passengers / capacity))
print(tours)

dictionary1 = {"cherry": "banana"}
print(type(dictionary1))