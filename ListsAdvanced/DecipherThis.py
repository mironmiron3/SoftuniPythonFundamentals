secret_message_as_list = input().split()
for i in range(len(secret_message_as_list)):
    final_word = []
    num_as_string = []
    rest_of_word = []
    for symbol in secret_message_as_list[i]:


        if symbol.isdigit():
            num_as_string.append(symbol)
        if symbol.isalpha():
            rest_of_word.append(symbol)
    final_word.append(chr(int("".join(num_as_string))))
    rest_of_word[0], rest_of_word[-1] = rest_of_word[-1], rest_of_word[0]
    final_word.extend(rest_of_word)
    "".join(final_word)

    print("".join(final_word), end=" ")




