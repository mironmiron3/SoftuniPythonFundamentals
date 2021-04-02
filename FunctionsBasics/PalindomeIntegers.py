def check_if_palindrome_number(string1):
    result = ""
    list_of_nums = string1.split(", ")
    for element in list_of_nums:
        if element[::-1] == element:
            result += "True\n"
        else:
            result += "False\n"

    return result


nums_as_strings = input()
outcome = check_if_palindrome_number(nums_as_strings)
print(outcome)