for word in input().split(", "):
    is_valid = True
    if 3 <= len(word) <= 16:

        for symbol in word:
            if symbol.isalnum() or symbol == "-" or symbol == "_":
                continue
            else:
                is_valid = False
    else:
        is_valid = False

    if is_valid:
        print(word)