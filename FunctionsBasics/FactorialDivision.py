def factorial_division(num1,num2):
    factorial1 = 1
    factorial2 = 1

    for number in range(1, num1 + 1):
        factorial1 *= number
    for number1 in range(1, num2 + 1):
        factorial2 *= number1
    result = factorial1 / factorial2
    return result

a = int(input())
b = int(input())
outcome = factorial_division(a,b)
print(f"{outcome:.2f}")
