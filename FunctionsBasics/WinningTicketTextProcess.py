winning_symbols = ['@', '#', '$','^']
def is_valid(ticket):
    if len(ticket) == 20:
        return True
    return False

def is_jackpot(ticket):
    for item in winning_symbols:
        if item * 20 in ticket:
            return True
    return False

def is_winning(ticket):
    for item in winning_symbols:
        if item * 6 in ticket[:10] and item * 6 in ticket[10:]:
            return True, min(ticket[:10].count(item),ticket[10:].count(item)), item
    return [False]
tickets = input().split(", ")
for ticket in tickets:
    ticket = ticket.strip()
    if is_valid(ticket):
        if is_jackpot(ticket):
            print(f'ticket "{ticket}" - 10{ticket[0]} Jackpot!')
        elif is_winning(ticket)[0]:
            print(f'ticket "{ticket}" - {is_winning(ticket)[1]}{is_winning(ticket)[2]}')
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")

a = [1,2,4]

b = a
b.reverse()
print(a)
