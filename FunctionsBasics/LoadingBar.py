def loading_bar_visualization(num):
    result = ''
    if num == 100:
        result = "100% Complete!\n"
        result += "[%%%%%%%%%%]"
        return result
    result += str(num) + "%" + " " + "[" + (int((num/10)) * "%") + (int((100-num)/10) * ".") + "]\n"
    result += "Still loading..."
    return result

number = int(input())
print(loading_bar_visualization(number))
word = "magic"
word1 = " ".join(reversed(word))
print(word1)
