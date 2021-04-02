def smallest_of_three(num1,num2,num3):
    min = num1
    if num2 < min:
        min = num2
    if num3 < min:
        min = num3

    return min

a = int(input())
b = int(input())
c = int(input())
result = smallest_of_three(a,b,c)
print(result)