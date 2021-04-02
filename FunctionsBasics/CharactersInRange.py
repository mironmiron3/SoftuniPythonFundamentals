def characters_in_asci_range(char1, char2):
    result = ''
    for i in range(ord(char1) + 1, ord(char2)):
        result += chr(i) + " "
    return result

a = input()
b = input()
print(characters_in_asci_range(a,b))
