lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
sum = 0
shield_breaks = 0


for i in range (1, lost_fights + 1):
    if i % 2 == 0:
        sum += helmet_price
    if i % 3 == 0:
        sum += sword_price
        if i % 2 == 0:
            sum += shield_price
            shield_breaks += 1
    if shield_breaks != 0 and shield_breaks % 2 == 0:
        sum += armor_price
    if shield_breaks == 2:
        shield_breaks = 0

print(f'Gladiator expenses: {sum:.2f} aureus')


