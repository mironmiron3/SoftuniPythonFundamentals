def password_validation(string1):
    result = ''
    has_valid_length = False
    if 6 <= len(string1) <= 10:
        has_valid_length = True
    has_valid_characters = True
    for element in string1:
        character_validation = False
        for ref in range(48, 58):
            if element == chr(ref):
                character_validation = True
        for ref in range(65, 91):
            if element == chr(ref):
                character_validation = True
        for ref in range(97, 123):
            if element == chr(ref):
                character_validation = True
        if character_validation:
            continue
        else:
            has_valid_characters = False
            break
    digits = 0
    for element in string1:
        for reference in range(48, 58):
            if chr(reference) == element:
                digits += 1
    if digits >= 2 and has_valid_characters and has_valid_length:
        result = "Password is valid"
    if digits < 2 or not has_valid_characters or not has_valid_length:
        if not has_valid_length:
            result += "Password must be between 6 and 10 characters\n"
        if not has_valid_characters:
            result += "Password must consist only of letters and digits\n"
        if digits < 2:
            result += "Password must have at least 2 digits"
    return result

password = input()
outcome = password_validation(password)
print(outcome)






