text = input()
longest_palindrome = ''
longest_palindrome_length = 0
for index in range(0,len(text)-1):
    for second_index in range(index+1,len(text)):
        if index == 0:
            if text[index:second_index + 1] == text[second_index::-1]:
                if len(text[index:second_index+1]) > longest_palindrome_length:
                    longest_palindrome_length = len(text[index:second_index])
                    longest_palindrome = text[index:second_index+1]
                    continue
        else:
            if text[index:second_index+1] == text[second_index:index-1:-1]:
                if len(text[index:second_index+1]) > longest_palindrome_length:
                    longest_palindrome_length = len(text[index:second_index+1])
                    longest_palindrome = text[index:second_index+1]
print(longest_palindrome)


