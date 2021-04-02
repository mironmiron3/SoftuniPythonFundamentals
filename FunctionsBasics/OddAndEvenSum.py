def Odd_and_Even_Sum(number_as_string):
    odd_sum = 0
    even_sum = 0
    for element in number_as_string:
        if int(element) % 2 == 0:
            even_sum += int(element)
        else:
            odd_sum += int(element)
    return (f"Odd sum = {odd_sum}, Even sum = {even_sum}")

number = input()
result = Odd_and_Even_Sum(number)
print(result)


