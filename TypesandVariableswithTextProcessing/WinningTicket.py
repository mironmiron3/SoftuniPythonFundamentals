list_of_tickets = input().split(",")
winning_symbols = ['@', '#', '$', '^']
for ticket in list_of_tickets:
    ticket = ticket.strip()
    if not len(ticket) == 20:
        print("invalid ticket")
        continue
    else:
        win_streak_left = 0
        win_streak_right = 0
        last_symbol_left = None
        last_symbol_right = None
        for index in range(0,10):
            if ticket[index] in winning_symbols:
                if last_symbol_left and last_symbol_left == ticket[index]:
                    win_streak_left += 1
                    last_symbol_left = ticket[index]
                else:
                    win_streak_left = 1
                    last_symbol_left = ticket[index]
        for index in range(19,9,-1):
            if ticket[index] in winning_symbols:
                if last_symbol_right and last_symbol_right == ticket[index]:
                    win_streak_right += 1
                    last_symbol_right = ticket[index]
                else:
                    win_streak_right = 1
                    last_symbol_right = ticket[index]
        if win_streak_right < 6 or win_streak_left < 6:
            print(f'ticket "{ticket}" - no match')
        elif win_streak_left == 10 and win_streak_right == 10 and last_symbol_left == last_symbol_right:
            print(f'ticket "{ticket}" - {win_streak_left}{last_symbol_left} Jackpot!')
        elif 6 <= win_streak_left <= 10 and 6 <= win_streak_right < 10 and last_symbol_left == last_symbol_right:
            if win_streak_left < win_streak_right:
                print(f'ticket "{ticket}" - {win_streak_left}{last_symbol_left}')
            else:
                print(f'ticket "{ticket}" - {win_streak_right}{last_symbol_left}')



