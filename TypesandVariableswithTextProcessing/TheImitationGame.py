def move_letters(word,number_of_letters):
    new = word[number_of_letters:] + word[:number_of_letters]
    return new
def insert_value(word,index,value):
    return word[:index] + value + word[index:]
text = input()
command = input()

while not command == "Decode":
    command = command.split("|")
    if command[0] == "Move":
        text = move_letters(text,int(command[1]))
    elif command[0] == "Insert":
        text = insert_value(text,int(command[1]),command[2])
    elif command[0] == "ChangeAll":
        text = text.replace(command[1],command[2])
    command = input()

print(f"The decrypted message is: {text}")