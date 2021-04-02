word = input()
new_word = ''
new_word += word[0]
for index in range(1, len(word)):
    if word[index] == new_word[len(new_word)-1]:
        continue
    else:
        new_word += word[index]
print(new_word)