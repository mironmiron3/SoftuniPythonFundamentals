txt = input()
new_txt = ''
for index in range(len(txt)):
    new_txt += chr(ord(txt[index])+3)
print(new_txt)