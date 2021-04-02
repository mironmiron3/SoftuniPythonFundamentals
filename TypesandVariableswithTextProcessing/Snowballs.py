import sys
n = int(input())
highest_snowball_value = -sys.maxsize
quality = 0
time = 0
snow = 0

for i in range (n):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = ((snowball_snow / snowball_time) ** snowball_quality)
    if snowball_value > highest_snowball_value:
        highest_snowball_value = snowball_value
        snow = snowball_snow
        time = snowball_time
        quality = snowball_quality
print(f'{snow:.0f} : {time:.0f} = {highest_snowball_value:.0f} ({quality:.0f})')


