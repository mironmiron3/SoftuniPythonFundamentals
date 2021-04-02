import math
biscuits_per_day = int(input())
number_of_workers = int(input())
biscuits_of_the_competitor = int(input())
our_biscuits = 0

for day in range(1, 31):
    if day % 3 == 0:
        our_biscuits += math.floor(number_of_workers * biscuits_per_day * 0.75)
        continue
    our_biscuits += number_of_workers * biscuits_per_day

print(f"You have produced {our_biscuits} biscuits for the past month.")
difference = our_biscuits - biscuits_of_the_competitor
if difference > 0:
    percentage = (difference / biscuits_of_the_competitor) * 100
    print(f"You produce {percentage:.2f} percent more biscuits.")
elif difference < 0:
    percentage = -(difference / biscuits_of_the_competitor) * 100
    print(f"You produce {percentage:.2f} percent less biscuits.")

