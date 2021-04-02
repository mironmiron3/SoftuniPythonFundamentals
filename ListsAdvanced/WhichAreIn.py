first_list_of_words = input().split(", ")
second_list_of_words = input().split(", ")
new_list = []

for small_string in first_list_of_words:
    for word in second_list_of_words:

        if small_string in word:
            if not small_string in new_list:
                new_list.append(small_string)
print(new_list)
