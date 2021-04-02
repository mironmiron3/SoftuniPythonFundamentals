n = int(input())

liters_in_tank = 0

for i in range (n):
    pour = int(input())
    if pour > (255 - liters_in_tank):
        print("Insufficient capacity!")
        continue
    liters_in_tank += pour

print(f"{liters_in_tank:.0f}")

