n = int(input())
for i in range(n):
    sentence = input()
    name = ''
    age = ''
    start_name = 0
    end_name = 0
    start_age = 0
    end_age = 0
    for index in range(0, len(sentence)):
        if sentence[index] == "@":
            start_name = index
        if sentence[index] == "|":
            end_name = index
        if sentence[index] == "#":
            start_age = index
        if sentence[index] == "*":
            end_age = index
    print(f"{sentence[start_name+1:end_name]} is {sentence[start_age+1:end_age]} years old.")