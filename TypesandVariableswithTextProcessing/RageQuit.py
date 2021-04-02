message = input()
new_message = ''
index = 0
current_text = ''
multiplier = ''
while index < len(message):
    if message[index].isdigit():
        multiplier += message[index]
        if index+1 < len(message):
            if message[index+1].isdigit():
                multiplier += message[index+1]
                index += 1
        multiplier = int(multiplier)
        new_message += current_text * multiplier
        index += 1
        multiplier = ''
        current_text = ''
        continue
    current_text += message[index].upper()
    index += 1
print(f"Unique symbols used: {len(set(new_message))}")
print(new_message)




